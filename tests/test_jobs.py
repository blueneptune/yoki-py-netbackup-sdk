"""Jobs: the filter each collection question becomes, paging, reading."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta, timezone

import pytest
import respx
from conftest import BASE, listing, resource

from netbackup_sdk import ChangesNotAllowed, NetBackupClient
from netbackup_sdk.models import job_from

ATTRS = {
    "jobId": 4711,
    "parentJobId": 4710,
    "jobType": "BACKUP",
    "policyName": "sql-daily",
    "policyType": "MS_SQL_SERVER",
    "scheduleType": "FULL",
    "clientName": "bob01.corp.local",
    "state": "DONE",
    "status": 1,
    "startTime": "2026-10-20T22:00:00.000Z",
    "endTime": "2026-10-20T22:31:10.000Z",
    "lastUpdateTime": "2026-10-20T22:31:11.000Z",
    "kilobytesTransferred": 1048576,
    "kilobytesDataTransferred": 1000000,
    "somethingNewer": True,
}


def test_a_job_is_read_and_keeps_netbackups_record() -> None:
    job = job_from(resource("job", 4711, ATTRS))
    assert (job.job_id, job.state, job.status, job.client_name) == (
        4711,
        "DONE",
        1,
        "bob01.corp.local",
    )
    assert job.end_time == datetime(2026, 10, 20, 22, 31, 10, tzinfo=UTC)
    assert job.kilobytes_data_transferred == 1000000
    assert not job.is_active
    assert job.raw == ATTRS


def test_an_unfinished_jobs_empty_end_time_is_none() -> None:
    running = job_from(
        resource("job", 1, {**ATTRS, "state": "ACTIVE", "endTime": "1970-01-01T00:00:00.000Z"})
    )
    assert running.end_time is None and running.is_active


def test_the_delta_asks_for_everything_changed_since_in_job_id_order(
    nbu_api: respx.MockRouter,
) -> None:
    route = nbu_api.get("/admin/jobs").respond(json=listing([resource("job", 4711, ATTRS)]))
    since = datetime(2026, 10, 20, 23, 0, tzinfo=timezone(timedelta(hours=1)))
    with NetBackupClient(BASE, api_key="k") as nbu:
        (page,) = list(nbu.jobs.iter_pages(updated_after=since, job_types=["BACKUP", "RESTORE"]))
    assert page[0].job_id == 4711
    params = route.calls[0].request.url.params
    assert params["filter"] == (
        "lastUpdateTime ge 2026-10-20T22:00:00.000Z and "
        "(jobType eq 'BACKUP' or jobType eq 'RESTORE')"
    )
    assert (params["sort"], params["page[offset]"], params["page[limit]"]) == ("jobId", "0", "100")


def test_active_and_history_windows_and_quoting(nbu_api: respx.MockRouter) -> None:
    route = nbu_api.get("/admin/jobs").respond(json=listing([]))
    start = datetime(2026, 10, 1, tzinfo=UTC)
    with NetBackupClient(BASE, api_key="k") as nbu:
        list(nbu.jobs.iter_pages(active_only=True, client="o'brien"))
        list(nbu.jobs.iter_pages(ended_after=start, ended_before=start + timedelta(days=1)))
    first, second = (c.request.url.params["filter"] for c in route.calls)
    assert first == "state ne 'DONE' and clientName eq 'o''brien'"
    assert second == "endTime ge 2026-10-01T00:00:00.000Z and endTime lt 2026-10-02T00:00:00.000Z"


def test_paging_walks_offsets_of_at_most_100(nbu_api: respx.MockRouter) -> None:
    def page(request):  # type: ignore[no-untyped-def]
        offset = int(request.url.params["page[offset]"])
        count = 100 if offset < 200 else 7
        return respx.MockResponse(
            200,
            json=listing(
                [resource("job", offset + i, {**ATTRS, "jobId": offset + i}) for i in range(count)]
            ),
        )

    route = nbu_api.get("/admin/jobs").mock(side_effect=page)
    with NetBackupClient(BASE, api_key="k", page_size=500) as nbu:
        sizes = [len(p) for p in nbu.jobs.iter_pages()]
    assert sizes == [100, 100, 7]
    assert [c.request.url.params["page[offset]"] for c in route.calls] == ["0", "100", "200"]


def test_naive_times_are_refused(nbu_api: respx.MockRouter) -> None:
    with NetBackupClient(BASE, api_key="k") as nbu:
        with pytest.raises(ValueError, match="timezone-aware"):
            list(nbu.jobs.iter_pages(updated_after=datetime(2026, 10, 1)))  # noqa: DTZ001


def test_a_job_netbackup_no_longer_has_is_none(nbu_api: respx.MockRouter) -> None:
    nbu_api.get("/admin/jobs/4711").respond(json={"data": resource("job", 4711, ATTRS)})
    nbu_api.get("/admin/jobs/1").respond(404, json={"errorCode": 404})
    with NetBackupClient(BASE, api_key="k") as nbu:
        job = nbu.jobs.get(4711)
        assert job is not None and job.policy_name == "sql-daily"
        assert nbu.jobs.get(1) is None


def test_the_api_key_is_sent_bare_and_a_password_login_is_used_for_jwts(
    nbu_api: respx.MockRouter,
) -> None:
    jobs = nbu_api.get("/admin/jobs").respond(json=listing([]))
    with NetBackupClient(BASE, api_key="A1-key") as nbu:
        list(nbu.jobs.iter_pages())
    with NetBackupClient(
        BASE, username="svc", password="pw", domain_type="nt", domain_name="CORP"
    ) as nbu:
        list(nbu.jobs.iter_pages())
    assert [c.request.headers["authorization"] for c in jobs.calls] == ["A1-key", "jwt-1"]
    login = nbu_api.routes[0].calls[0].request
    assert b'"domainType":"nt"' in login.content.replace(b" ", b"")
    assert b'"domainName":"CORP"' in login.content.replace(b" ", b"")


def test_changes_are_refused_by_default_and_never_retried(nbu_api: respx.MockRouter) -> None:
    import httpx

    with NetBackupClient(BASE, api_key="k") as nbu:
        for change in (nbu.jobs.cancel, nbu.jobs.suspend, nbu.jobs.resume, nbu.jobs.restart):
            with pytest.raises(ChangesNotAllowed):
                change(1)
    assert nbu_api.calls.call_count == 0

    restart = nbu_api.post("/admin/jobs/9/restart").mock(side_effect=httpx.ReadTimeout("slow"))
    with NetBackupClient(BASE, api_key="k", allow_changes=True) as nbu:
        with pytest.raises(Exception):  # noqa: B017
            nbu.jobs.restart(9)
    assert restart.call_count == 1
