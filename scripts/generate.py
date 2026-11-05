"""Generate netbackup_sdk.raw: one method per operation in a primary's API
description (fetched by scripts/spec.py into spec/<release>/).

    uv run python scripts/generate.py 10.2

`nbu.raw.<area>.<call>(...)` is the whole API, thinly: path parameters
are positional, query parameters and headers keyword-only, a request body
is `body=`; the answer comes back decoded (JSON, text or bytes). Reads go
through the retrying transport; everything else through `_change`, so a
read-only client refuses it. The hand-written groups (`nbu.jobs`,
`nbu.policies`, ...) sit on top for what blt uses.

Names come from the path, as there are no operationIds:

    GET    /config/policies                 list_policies (it pages or filters)
    GET    /security/ping                   get_ping
    GET    /config/policies/{policyName}    get_policy
    PUT    /config/policies/{policyName}    put_policy
    POST   /admin/jobs/{jobId}/cancel       post_job_cancel

The area's own first path segment is left out; a segment followed by a
parameter is made singular; clashes get `_by_<parameter>`.
"""

from __future__ import annotations

import keyword
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "netbackup_sdk" / "raw"
METHODS = ("get", "post", "put", "patch", "delete")
BUILTINS = {
    "filter",
    "id",
    "type",
    "format",
    "input",
    "hash",
    "object",
    "list",
    "dir",
    "max",
    "min",
}


def snake(text: str) -> str:
    text = re.sub(r"[\[\]{}.\-\s/]+", "_", text)
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", text)
    return re.sub(r"_+", "_", text).strip("_").lower()


def singular(word: str) -> str:
    for plural, one in (("policies", "policy"), ("ies", "y"), ("sses", "ss"), ("xes", "x")):
        if word.endswith(plural):
            return word[: -len(plural)] + one
    if word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def py_name(name: str) -> str:
    n = snake(name) or "value"
    if n[0].isdigit():
        n = "p_" + n
    if keyword.iskeyword(n) or n in BUILTINS:
        n += "_"
    return n


_files: dict[Path, Any] = {}
_folder: list[Path] = []


def _load(path: Path) -> Any:
    if path not in _files:
        _files[path] = yaml.safe_load(path.read_text()) if path.exists() else {}
    return _files[path]


def resolve(spec: dict[str, Any], item: dict[str, Any], kind: str = "") -> dict[str, Any]:
    """Follow `$ref`s, also into the shared files beside the area's own
    (./common.yaml#/components/parameters/filter)."""
    document: Any = spec
    for _ in range(20):
        ref = item.get("$ref") if isinstance(item, dict) else None
        if not ref:
            return item
        file, _, pointer = str(ref).partition("#")
        if file:
            document = _load(_folder[0] / file.removeprefix("./"))
        node: Any = document
        for part in pointer.strip("/").split("/") if pointer else []:
            node = (
                node.get(part.replace("~1", "/").replace("~0", "~"), {})
                if isinstance(node, dict)
                else {}
            )
        item = node
    return item


def call_name(method: str, path: str, listing: bool = True) -> str:
    every = [s for s in path.strip("/").split("/") if s]
    # /config/policies -> policies; a one-segment path (/ping) keeps it.
    segments = every[1:] if len(every) > 1 else every or ["root"]
    words = []
    for i, seg in enumerate(segments):
        if seg.startswith("{"):
            continue
        nxt = segments[i + 1] if i + 1 < len(segments) else ""
        words.append(singular(snake(seg)) if nxt.startswith("{") else snake(seg))
    ends_with_param = segments[-1].startswith("{")
    verb = {"get": "list" if listing and not ends_with_param else "get"}.get(method, method)
    return f"{verb}_{'_'.join(w for w in words if w) or 'root'}"


def operations(spec: dict[str, Any]) -> list[dict[str, Any]]:
    ops = []
    for path, item in (spec.get("paths") or {}).items():
        shared = item.get("parameters", [])
        for method in METHODS:
            op = item.get(method)
            if not op:
                continue
            params = [resolve(spec, p, "parameters") for p in shared + op.get("parameters", [])]
            body = (
                resolve(spec, op["requestBody"], "requestBodies") if op.get("requestBody") else None
            )
            body_types = list((body or {}).get("content", {}))
            answers: list[str] = []
            for code, response in (op.get("responses") or {}).items():
                if str(code).startswith("2"):
                    answers += list(resolve(spec, response, "responses").get("content") or {})
            ops.append(
                {
                    "method": method,
                    "path": path,
                    "params": [p for p in params if p.get("in") in ("path", "query", "header")],
                    "body": body_types,
                    "body_required": bool((body or {}).get("required")),
                    "answers": answers,
                }
            )
    return ops


def accept_for(answers: list[str]) -> str | None:
    """An Accept to send when the operation does not answer JSON."""
    if not answers or any("+json" in a for a in answers):
        return None
    return answers[0].split(";")[0]


def render_area(area: str, spec: dict[str, Any], release: str) -> tuple[str, list[str]]:
    ops = operations(spec)
    names: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for op in ops:
        query = {p["name"] for p in op["params"] if p["in"] == "query"}
        listing = bool(query & {"page[limit]", "page[offset]", "filter", "sort", "page[disable]"})
        names[call_name(op["method"], op["path"], listing)].append(op)
    final: list[tuple[str, dict[str, Any]]] = []
    for name, group in names.items():
        if len(group) == 1:
            final.append((name, group[0]))
            continue
        for op in group:
            path_params = [p["name"] for p in op["params"] if p["in"] == "path"]
            extra = "_by_" + "_".join(snake(p) for p in path_params) if path_params else ""
            final.append((name + extra, op))
    seen: dict[str, int] = defaultdict(int)
    out = []
    for name, op in sorted(final, key=lambda x: (x[1]["path"], x[1]["method"])):
        seen[name] += 1
        if seen[name] > 1:
            name = f"{name}_{seen[name]}"
        out.append(render_op(name, op))
    cls = "".join(w.capitalize() for w in re.split(r"[_-]", area))
    header = (
        f'"""NetBackup {release} API, area `{area}`: every operation, thinly.\n\n'
        f"Generated by scripts/generate.py from the primary's own API description\n"
        f'(spec/{release}/{area}.yaml). Do not edit.\n"""\n\n'
        "from __future__ import annotations\n\n"
        "from typing import Any\n\n"
        "from .._base import Resource\n\n\n"
        f"class {cls}(Resource):\n"
        f'    """`{area}`: {len(ops)} operations."""\n'
    )
    return header + "\n".join(out), [cls, str(len(ops))]


def render_op(name: str, op: dict[str, Any]) -> str:
    params = op["params"]
    path_params = [p for p in params if p["in"] == "path"]
    others = [p for p in params if p["in"] in ("query", "header")]
    sig = ["self"]
    used = set()
    for p in path_params:
        n = py_name(p["name"])
        used.add(n)
        sig.append(f"{n}: str | int")
    kw = []
    for p in others:
        n = py_name(p["name"])
        while n in used:
            n += "_"
        used.add(n)
        p["py"] = n
        kw.append(f"{n}: Any = None")
    has_body = bool(op["body"])
    multipart = any(t.startswith("multipart/") for t in op["body"])
    form = any(t.startswith("application/x-www-form-urlencoded") for t in op["body"])
    if has_body:
        kw.append("files: Any = None" if multipart else "body: Any = None")
    if kw:
        sig.append("*")
        sig += kw
    path_expr = op["path"]
    for p in path_params:
        path_expr = path_expr.replace("{" + p["name"] + "}", "{" + py_name(p["name"]) + "}")
    lines = [f"    def {name}({', '.join(sig)}) -> Any:"]
    doc = f"{op['method'].upper()} {op['path']}"
    q = [p["name"] for p in others if p["in"] == "query"]
    h = [p["name"] for p in others if p["in"] == "header"]
    detail = []
    if q:
        detail.append("Query: " + ", ".join(q) + ".")
    if h:
        detail.append("Headers: " + ", ".join(h) + ".")
    if has_body:
        detail.append("Body: " + ", ".join(sorted({t.split(";")[0] for t in op["body"]})) + ".")
    lines.append(
        f'        """`{doc}`' + (("\n\n        " + " ".join(detail)) if detail else "") + '"""'
    )
    lines.append(
        f'        path = f"{path_expr}"' if path_params else f'        path = "{path_expr}"'
    )
    call = [f'"{op["method"].upper()}"', "path"]
    query = [p for p in others if p["in"] == "query"]
    headers = [p for p in others if p["in"] == "header"]
    if query:
        call.append("params={" + ", ".join(f'"{p["name"]}": {p["py"]}' for p in query) + "}")
    if headers:
        call.append("headers={" + ", ".join(f'"{p["name"]}": {p["py"]}' for p in headers) + "}")
    if has_body:
        call.append("files=files" if multipart else ("form=body" if form else "body=body"))
    accept = accept_for(op["answers"])
    if accept:
        call.append(f'accept="{accept}"')
    if op["method"] != "get":
        call.append("change=True")
    lines.append(f"        return self._call({', '.join(call)})")
    return "\n".join(lines) + "\n"


def main() -> int:
    release = sys.argv[1] if len(sys.argv) > 1 else "10.2"
    source = ROOT / "spec" / release
    if not source.is_dir():
        print(f"No spec/{release}/ - run scripts/spec.py against a {release} primary first.")
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.py"):
        old.unlink()
    _folder[:] = [source]
    areas = []
    for file in sorted(source.glob("*.yaml")):
        area = file.stem
        module = py_name(area).rstrip("_")
        spec = _load(file)
        if not spec.get("paths"):
            continue  # a shared file other areas refer to (common.yaml)
        text, (cls, count) = render_area(area, spec, release)
        (OUT / f"{module}.py").write_text(text)
        areas.append((module, cls, int(count), area))
    total = sum(a[2] for a in areas)
    init = [
        f'"""Every operation of the NetBackup {release} API, one method each, by area:\n'
        "`nbu.raw.config.list_policies()`, `nbu.raw.storage.list_disk_pools()`, ...\n\n"
        f"{total} operations in {len(areas)} areas. Generated by scripts/generate.py from\n"
        'the primary\'s own API description. Do not edit.\n"""\n',
        "from __future__ import annotations\n",
        "from typing import TYPE_CHECKING\n",
    ]
    init += [f"from .{m} import {c}" for m, c, _, _ in areas]
    init += [
        "",
        "if TYPE_CHECKING:",
        "    from ..client import NetBackupClient",
        "",
        f'RELEASE = "{release}"',
        "",
        "",
        "class Raw:",
        '    """The whole API, by area."""',
        "",
        "    def __init__(self, client: NetBackupClient) -> None:",
    ]
    init += [f"        self.{m} = {c}(client)" for m, c, _, _ in areas]
    (OUT / "__init__.py").write_text("\n".join(init) + "\n")
    print(f"netbackup_sdk.raw: {total} operations in {len(areas)} areas (NetBackup {release})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
