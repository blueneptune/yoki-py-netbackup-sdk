"""Jobs: the activity monitor, read through the API."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from netbackup_sdk import NetBackupClient
from netbackup_sdk.models import Job

from .recorder import Entry


@pytest.fixture(scope="module")
def newest(nbu: NetBackupClient) -> Job:
    _, jobs = nbu.jobs.sample(1)
    if not jobs:
        pytest.skip("the server has no jobs")
    return jobs[0]


def test_sample(nbu: NetBackupClient, record: Entry) -> None:
    """The newest few jobs, and how many there are, in one request.

    NetBackup 10.2 (API 9.0) gives no total count; later releases do."""
    total, jobs = nbu.jobs.sample(3)
    record.result({"total": total, "jobs": jobs})
    assert all(isinstance(job, Job) for job in jobs)


def test_every_page_parses(nbu: NetBackupClient, record: Entry) -> None:
    """Walk the whole job list, a page at a time.

    Every job NetBackup still holds must parse into `Job`: an unexpected
    field or format fails here before it fails a collector."""
    count = 0
    states: dict[str, int] = {}
    for page in nbu.jobs.iter_pages():
        for job in page:
            count += 1
            states[job.state] = states.get(job.state, 0) + 1
    record.result({"jobs": count, "by state": states})
    assert count >= 0


def test_updated_since(nbu: NetBackupClient, record: Entry) -> None:
    """The collector's delta: every job created or changed in the last week.

    Built as the OData filter `lastUpdateTime ge <time>`."""
    since = datetime.now(UTC) - timedelta(days=7)
    jobs = [job for page in nbu.jobs.iter_pages(updated_after=since) for job in page]
    record.result({"since": since, "jobs": len(jobs)})
    assert all(job.last_update_time is None or job.last_update_time >= since for job in jobs)


def test_oldest_start(nbu: NetBackupClient, record: Entry) -> None:
    """When the history NetBackup still keeps begins."""
    record.result(nbu.jobs.oldest_start())


def test_get_one(nbu: NetBackupClient, newest: Job, record: Entry) -> None:
    """One job by its id."""
    job = record.result(nbu.jobs.get(newest.job_id))
    assert job is not None and job.job_id == newest.job_id


def test_missing_job_is_none(nbu: NetBackupClient, record: Entry) -> None:
    """A job id NetBackup does not have gives `None`, not an error."""
    assert nbu.jobs.get(2_000_000_000) is None


def test_try_logs(nbu: NetBackupClient, newest: Job, record: Entry) -> None:
    """A job's try logs: the detailed status lines the activity monitor shows."""
    record.result(nbu.jobs.try_logs(newest.job_id))


def test_file_lists(nbu: NetBackupClient, newest: Job, record: Entry) -> None:
    """What a job covered: its file list."""
    record.result(nbu.jobs.file_lists(newest.job_id))
