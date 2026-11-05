"""Live tests: the SDK against a real NetBackup primary.

Not run by plain `pytest` (pyproject's addopts leave out the `live`
mark). Run them with:

    NBU_URL=https://primary:1556/netbackup NBU_API_KEY=... NBU_CA_BUNDLE=ca.pem \\
        uv run pytest -m live

- NBU_LIVE_CHANGES=yes also runs the tests that create, change and
  delete things - only ever their own `bltlive-<run>-*` objects, removed
  again at the end.
- NBU_LIVE_DOCS=0 skips writing docs/live/.
- NBU_LIVE_MASK="a,b" masks more names than the run finds by itself;
  NBU_LIVE_MASK_PREFIXES="lab01" masks every word starting with one.

Every request and answer is recorded (recorder.py) and written up, masked,
as docs/live/<module>.md, with docs/live/coverage.md against the spec
(scripts/spec.py).
"""

from __future__ import annotations

import os
from collections.abc import Generator, Iterator
from datetime import UTC, datetime
from pathlib import Path

import httpx
import pytest

from netbackup_sdk import NetBackupClient
from netbackup_sdk.client import tls_context

from .recorder import ROOT, Entry, Masker, Recorder, stamp, write_coverage, write_pages

RUN = datetime.now(UTC).strftime("%m%d%H%M")
PREFIX = f"bltlive-{RUN}"

_records: list[Entry] = []
_state: dict[str, object] = {}

TITLES = {
    "test_server": "The server: ping, version, identity",
    "test_jobs": "Jobs",
    "test_inventory": "Policies, images, hosts, storage, assets",
}


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    here = Path(__file__).parent
    for item in items:
        if here in Path(str(item.fspath)).parents:
            item.add_marker(pytest.mark.live)


def _require(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        pytest.exit(f"Live tests need {name}; see tests/live/conftest.py.", returncode=2)
    return value


@pytest.fixture(scope="session")
def recorder() -> Recorder:
    ca = os.environ.get("NBU_CA_BUNDLE")
    verify = tls_context(Path(ca)) if ca else True
    rec = Recorder(httpx.HTTPTransport(verify=verify))
    _state["recorder"] = rec
    return rec


@pytest.fixture(scope="session")
def nbu(recorder: Recorder) -> Iterator[NetBackupClient]:
    client = NetBackupClient(
        _require("NBU_URL"),
        api_key=_require("NBU_API_KEY"),
        transport=recorder,
        allow_changes=changes_allowed(),
    )
    _state["base_path"] = httpx.URL(client.base_url).path
    with client:
        yield client


@pytest.fixture(scope="session")
def server_info(nbu: NetBackupClient) -> dict[str, object]:
    info = nbu.server.info()
    _state["release"] = str(info.get("nbuVersion", "")).removeprefix("NetBackup_")
    return info


@pytest.fixture(scope="session")
def masker(nbu: NetBackupClient, server_info: dict[str, object]) -> Masker:
    """Everything that names the lab, learned from the server itself before
    any test runs: its own name, its hosts, policies and storage."""
    m = Masker()
    m.add(httpx.URL(nbu.base_url).host, "primary")
    m.add(str(server_info.get("serverName", "")), "primary")
    for host in nbu.hosts.list():
        m.add(host.get("hostName"), "host")
    for policy in nbu.policies.list():
        m.add(policy.get("policyName") or policy.get("id"), "policy")
    for unit in nbu.storage.units():
        m.add(unit.get("name") or unit.get("id"), "storage-unit")
    for pool in nbu.storage.disk_pools():
        m.add(pool.get("name"), "disk-pool")
        for volume in pool.get("diskVolumes") or []:
            m.add(volume.get("name"), "volume")
        for server in pool.get("storageServers") or []:
            m.add(server if isinstance(server, str) else server.get("name"), "storage-server")
    m.prefixes = [
        p.strip() for p in os.environ.get("NBU_LIVE_MASK_PREFIXES", "").split(",") if p.strip()
    ]
    for extra in os.environ.get("NBU_LIVE_MASK", "").split(","):
        m.add(extra.strip(), "name")
    _state["masker"] = m
    return m


def changes_allowed() -> bool:
    return os.environ.get("NBU_LIVE_CHANGES") == "yes"


@pytest.fixture
def changes() -> None:
    if not changes_allowed():
        pytest.skip("creates and deletes bltlive objects: set NBU_LIVE_CHANGES=yes")


@pytest.fixture(autouse=True)
def record(
    request: pytest.FixtureRequest, recorder: Recorder, masker: Masker, nbu: NetBackupClient
) -> Iterator[Entry]:
    """The test's page entry; the exchanges it caused are added after it."""
    entry = Entry(
        module=request.module.__name__.rsplit(".", 1)[-1],
        name=request.node.nodeid,
        function=request.function,
    )
    start = len(recorder.exchanges)
    _records.append(entry)  # now, so the call's report can mark it
    yield entry
    entry.exchanges = recorder.exchanges[start:]
    _state["api_version"] = nbu.api_version


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[None]
) -> Generator[None, pytest.TestReport, pytest.TestReport]:
    report = yield
    if report.when == "call" and report.outcome != "passed":
        for entry in _records:
            if entry.name == item.nodeid:
                entry.outcome = report.outcome
                longrepr = report.longrepr
                if report.skipped and isinstance(longrepr, tuple):
                    entry.reason = str(longrepr[2]).removeprefix("Skipped: ")
    return report


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    if not _records or os.environ.get("NBU_LIVE_DOCS") == "0":
        return
    recorder = _state["recorder"]
    masker = _state["masker"]
    assert isinstance(recorder, Recorder) and isinstance(masker, Masker)
    base_path = str(_state["base_path"])
    release = str(_state.get("release") or "unknown")
    header = stamp(release, str(_state.get("api_version", "?")))
    write_pages(_records, masker, title_of=TITLES, header=header, base_path=base_path)
    spec = ROOT / "spec" / f"operations-{release}.tsv"
    if spec.exists():
        write_coverage(
            (e for r in _records for e in r.exchanges), spec, base_path=base_path, header=header
        )
