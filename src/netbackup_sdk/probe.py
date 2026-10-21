"""netbackup-probe: try each call the SDK makes, once, and say what
happened - including which API version the server accepted.

    NBU_URL=https://nbu01.example.com:1556/netbackup NBU_API_KEY=... netbackup-probe

Or NBU_USERNAME / NBU_PASSWORD (+ NBU_DOMAIN_TYPE, NBU_DOMAIN_NAME)
instead of the key. Optional: NBU_API_VERSION ("auto", a release such as
"10.5", or an API version such as "12.0"), NBU_VERIFY_TLS=false,
NBU_CA_BUNDLE=/path/to/ca.pem. Reads only; stores nothing.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from pathlib import Path

from .client import NetBackupClient

Check = tuple[str, Callable[[], str]]


def checks(nbu: NetBackupClient) -> list[Check]:
    day_ago = datetime.now(UTC) - timedelta(hours=24)
    found: dict[str, object] = {}

    def ping() -> str:
        return f"answering; API version {nbu.api_version}"

    def recent() -> str:
        total, jobs = nbu.jobs.sample(updated_after=day_ago)
        if jobs:
            found["job"] = jobs[0].job_id
            found["client"] = jobs[0].client_name
        kinds = sorted({j.job_type or "?" for j in jobs})
        return f"{total} jobs changed in the last 24 h; types seen: {', '.join(kinds) or '-'}"

    def active() -> str:
        pages = list(nbu.jobs.iter_pages(active_only=True))
        return f"{sum(len(p) for p in pages)} jobs not DONE"

    def window() -> str:
        page = next(
            nbu.jobs.iter_pages(ended_after=day_ago - timedelta(hours=24), ended_before=day_ago),
            [],
        )
        return f"{len(page)} jobs on the first page ended 48-24 h ago"

    def one() -> str:
        if "job" not in found:
            return "skipped: no job to fetch"
        job = nbu.jobs.get(int(str(found["job"])))
        return f"job {found['job']}: {job.state} status {job.status}" if job else "not found"

    def try_logs() -> str:
        if "job" not in found:
            return "skipped: no job"
        return f"{len(nbu.jobs.try_logs(int(str(found['job']))))} try-log entries"

    def latest_image() -> str:
        if not found.get("client"):
            return "skipped: no client name"
        image = nbu.images.latest(str(found["client"]))
        return f"newest image of {found['client']}: {image.get('backupTime') if image else None}"

    return [
        ("ping and API version", lambda: (nbu.server.ping(), ping())[1]),
        ("job listing (delta)", recent),
        ("active jobs", active),
        ("job listing by end time", window),
        ("one job", one),
        ("job try logs", try_logs),
        ("oldest job", lambda: f"oldest job started {nbu.jobs.oldest_start()}"),
        ("policies", lambda: f"{len(nbu.policies.list())} policies"),
        ("latest image of a client", latest_image),
        ("hosts", lambda: f"{len(nbu.hosts.list())} hosts"),
        ("storage units", lambda: f"{len(nbu.storage.units())} storage units"),
        ("disk pools", lambda: f"{len(nbu.storage.disk_pools())} disk pools"),
        ("VMware assets", lambda: f"{len(nbu.assets.workload('vmware'))} assets"),
    ]


def run_probe(nbu: NetBackupClient, out: Callable[[str], None] = print) -> int:
    """Run every check; return how many failed."""
    failed = 0
    for name, check in checks(nbu):
        try:
            out(f"ok      {name:<28} {check()}")
        except Exception as exc:  # noqa: BLE001 - reporting every failure is the point
            failed += 1
            out(f"FAILED  {name:<28} {type(exc).__name__}: {str(exc)[:160]}")
    return failed


def main() -> int:
    env = os.environ
    if not env.get("NBU_URL") or not (
        env.get("NBU_API_KEY") or (env.get("NBU_USERNAME") and env.get("NBU_PASSWORD"))
    ):
        print("Set NBU_URL, and NBU_API_KEY or NBU_USERNAME + NBU_PASSWORD.", file=sys.stderr)
        return 2
    ca = env.get("NBU_CA_BUNDLE")
    with NetBackupClient(
        env["NBU_URL"],
        api_key=env.get("NBU_API_KEY") or None,
        username=env.get("NBU_USERNAME") or None,
        password=env.get("NBU_PASSWORD") or None,
        domain_type=env.get("NBU_DOMAIN_TYPE", "vx"),
        domain_name=env.get("NBU_DOMAIN_NAME") or None,
        api_version=env.get("NBU_API_VERSION", "auto"),
        verify_tls=env.get("NBU_VERIFY_TLS", "true").lower() not in ("false", "0", "no"),
        ca_bundle=Path(ca) if ca else None,
    ) as nbu:
        return 1 if run_probe(nbu) else 0


if __name__ == "__main__":
    sys.exit(main())
