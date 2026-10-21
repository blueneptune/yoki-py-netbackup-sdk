"""Policies, images, hosts, storage, assets, and the probe."""

from __future__ import annotations

import respx
from conftest import BASE, listing, resource

from netbackup_sdk import NetBackupClient
from netbackup_sdk.probe import run_probe


def test_policies_ask_for_the_generic_schema(nbu_api: respx.MockRouter) -> None:
    nbu_api.get("/config/policies").respond(
        json=listing([resource("policy", "sql-daily", {"policyType": "MS-SQL-Server"})])
    )
    one = nbu_api.get("/config/policies/sql-daily").respond(
        json={"data": resource("policy", "sql-daily", {"policy": {"clients": []}})}
    )
    with NetBackupClient(BASE, api_key="k") as nbu:
        assert nbu.policies.list() == [{"policyType": "MS-SQL-Server", "id": "sql-daily"}]
        assert nbu.policies.get("sql-daily") == {"policy": {"clients": []}, "id": "sql-daily"}
    assert one.calls[0].request.headers["x-netbackup-policy-use-generic-schema"] == "true"


def test_a_clients_newest_image_is_one_request(nbu_api: respx.MockRouter) -> None:
    images = nbu_api.get("/catalog/images").respond(
        json=listing([resource("image", "bob01_1729", {"backupTime": "2026-10-20T22:31:10.000Z"})])
    )
    with NetBackupClient(BASE, api_key="k") as nbu:
        latest = nbu.images.latest("bob01.corp.local")
    assert latest is not None and latest["backupTime"].startswith("2026-10-20")
    params = images.calls[0].request.url.params
    assert (params["filter"], params["sort"], params["page[limit]"]) == (
        "clientName eq 'bob01.corp.local'",
        "-backupTime",
        "1",
    )


def test_the_probe_reports_each_call_and_the_version(nbu_api: respx.MockRouter) -> None:
    job = resource(
        "job",
        7,
        {"jobId": 7, "jobType": "BACKUP", "state": "DONE", "status": 0, "clientName": "bob01"},
    )
    nbu_api.get("/ping").respond(json={"serverTime": "2026-10-21T12:00:00Z"})
    nbu_api.get("/admin/jobs").respond(json=listing([job], count=412))
    nbu_api.get("/admin/jobs/7").respond(json={"data": job})
    nbu_api.get("/admin/jobs/7/try-logs").respond(json=listing([resource("log", 1, {})]))
    nbu_api.get("/config/policies").respond(json=listing([]))
    nbu_api.get("/catalog/images").respond(json=listing([]))
    nbu_api.get("/config/hosts").respond(json=listing([]))
    nbu_api.get("/storage/storage-units").respond(json=listing([]))
    nbu_api.get("/storage/disk-pools").respond(403)
    nbu_api.get("/asset-service/workloads/vmware/assets").respond(json=listing([]))

    lines: list[str] = []
    with NetBackupClient(BASE, api_key="k") as nbu:
        failed = run_probe(nbu, lines.append)
    assert failed == 1
    by_name = {line[8:36].strip(): line for line in lines}
    assert "API version 13.0" in by_name["ping and API version"]
    assert "412 jobs changed" in by_name["job listing (delta)"]
    assert by_name["disk pools"].startswith("FAILED")
    assert len(lines) == 13
