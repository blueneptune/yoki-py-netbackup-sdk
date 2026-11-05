"""Fetch a NetBackup primary's own API description, and list its operations.

Every primary publishes the API it speaks at https://<primary>/api-docs/:
one OpenAPI file per area (admin, config, storage, ...). This downloads
them into spec/<release>/ (not committed: Veritas's text) and writes
spec/operations-<release>.tsv (committed): one line per operation -
area, method, path, operationId. That list is what the SDK's coverage
is measured against (docs/live/coverage.md), and diffing two releases'
lists shows what changed between them.

    NBU_URL=https://primary:1556/netbackup NBU_API_KEY=... NBU_CA_BUNDLE=ca.pem \\
        uv run python scripts/spec.py
"""

from __future__ import annotations

import os
import re
import ssl
import sys
from pathlib import Path
from urllib.parse import urlsplit

import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
METHODS = ("get", "post", "put", "patch", "delete")
REF = re.compile(r"""\$ref["']?:\s*["']?(?:\./)?([\w.-]+\.(?:yaml|json))#""")


def main() -> int:
    url = os.environ["NBU_URL"].rstrip("/")
    key = os.environ["NBU_API_KEY"]
    ca = os.environ.get("NBU_CA_BUNDLE")
    verify: bool | ssl.SSLContext = True
    if ca:
        verify = ssl.create_default_context(cafile=ca)
        verify.verify_flags &= ~ssl.VERIFY_X509_STRICT  # see client.tls_context
    host = urlsplit(url).hostname
    with httpx.Client(verify=verify, timeout=60) as http:
        info = http.get(
            f"{url}/security/serverinfo",
            headers={"Authorization": key, "Accept": "application/vnd.netbackup+json;version=6.0"},
        )
        info.raise_for_status()
        release = info.json()["nbuVersion"].removeprefix("NetBackup_")
        # The API description is served by the web UI's server, on 443.
        docs = f"https://{host}/api-docs"
        index = http.get(f"{docs}/index.html")
        index.raise_for_status()
        names = sorted(set(re.findall(r"yamls/([\w.-]+\.yaml)", index.text)))
        target = ROOT / "spec" / release
        target.mkdir(parents=True, exist_ok=True)
        # The areas' files refer to shared ones (common.yaml,
        # config_policies.yaml, PolicyType_Generic.json, ...) that the index
        # does not list: fetch whatever is referred to, until nothing new is.
        wanted, fetched = list(names), set()
        while wanted:
            name = wanted.pop()
            if name in fetched:
                continue
            fetched.add(name)
            body = http.get(f"{docs}/yamls/{name}")
            body.raise_for_status()
            (target / name).write_bytes(body.content)
            wanted += [r for r in REF.findall(body.text) if r not in fetched]
        rows = []
        for name in names:
            spec = yaml.safe_load((target / name).read_text())
            area = name.removesuffix(".yaml")
            for path, item in (spec.get("paths") or {}).items():
                for method in METHODS:
                    if method in item:
                        rows.append(
                            (area, method.upper(), path, item[method].get("operationId", ""))
                        )
    rows.sort()
    out = ROOT / "spec" / f"operations-{release}.tsv"
    out.write_text("area\tmethod\tpath\toperationId\n" + "".join("\t".join(r) + "\n" for r in rows))
    where = out.relative_to(ROOT)
    print(
        f"NetBackup {release}: {len(rows)} operations in {len(names)} areas "
        f"({len(fetched)} files) -> {where}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
