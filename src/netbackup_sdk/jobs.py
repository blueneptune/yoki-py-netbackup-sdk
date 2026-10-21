"""Jobs: NetBackup's activity monitor - what is running and what ran."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from datetime import datetime
from typing import Any

from loguru import logger
from pydantic import ValidationError
from sdk_primer import NotFoundError

from ._base import Entities, Entity, Resource, all_of, flatten, quoted, timestamp
from .models import Job, job_from

PATH = "/admin/jobs"
# NetBackup will not return more than 100 jobs per page.
MAX_PAGE = 100


def parse_job(resource: Entity) -> Job | None:
    """A Job, or None if this record cannot be read - one odd record
    costs that record, loudly, not the whole collection."""
    try:
        return job_from(resource)
    except ValidationError as exc:
        problems = "; ".join(
            f"{'.'.join(str(p) for p in e['loc'])}: {e['msg']}" for e in exc.errors()
        )
        logger.error("Skipping job {}: could not read it - {}", resource.get("id"), problems)
        return None


def job_filter(
    *,
    updated_after: datetime | None = None,
    ended_after: datetime | None = None,
    ended_before: datetime | None = None,
    started_after: datetime | None = None,
    active_only: bool = False,
    job_types: Sequence[str] | None = None,
    client: str | None = None,
    policy: str | None = None,
    extra: str | None = None,
) -> str | None:
    """A NetBackup (OData) filter from the conditions given."""
    types = None
    if job_types:
        types = "(" + " or ".join(f"jobType eq {quoted(t)}" for t in job_types) + ")"
    return all_of(
        f"lastUpdateTime ge {timestamp(updated_after)}" if updated_after else None,
        f"endTime ge {timestamp(ended_after)}" if ended_after else None,
        f"endTime lt {timestamp(ended_before)}" if ended_before else None,
        f"startTime ge {timestamp(started_after)}" if started_after else None,
        "state ne 'DONE'" if active_only else None,
        types,
        f"clientName eq {quoted(client)}" if client else None,
        f"policyName eq {quoted(policy)}" if policy else None,
        extra,
    )


class Jobs(Resource):
    def iter_pages(
        self,
        *,
        updated_after: datetime | None = None,
        ended_after: datetime | None = None,
        ended_before: datetime | None = None,
        started_after: datetime | None = None,
        active_only: bool = False,
        job_types: Sequence[str] | None = None,
        client: str | None = None,
        policy: str | None = None,
        extra_filter: str | None = None,
    ) -> Iterator[list[Job]]:
        """Jobs matching the conditions, a page at a time (GET /admin/jobs).

        In job-id order, so jobs that start while this is running land
        after the last page, and a job that changes state mid-walk does
        not move.

        For a collector: `updated_after` is the delta - every job created
        or changed since then, whatever its state; `active_only` is what
        is still going; `ended_after` + `ended_before` is a window of
        history. Times must be timezone-aware. `extra_filter` is any
        further OData condition, ANDed on.
        """
        query = job_filter(
            updated_after=updated_after,
            ended_after=ended_after,
            ended_before=ended_before,
            started_after=started_after,
            active_only=active_only,
            job_types=job_types,
            client=client,
            policy=policy,
            extra=extra_filter,
        )
        params: dict[str, Any] = {"filter": query, "sort": "jobId"}
        size = min(self._client.page_size, MAX_PAGE)
        for page in self._pages(PATH, params, page_size=size):
            jobs = [j for resource in page if (j := parse_job(resource)) is not None]
            if jobs:
                yield jobs

    def sample(
        self, limit: int = 5, *, updated_after: datetime | None = None
    ) -> tuple[int | None, list[Job]]:
        """A few jobs, newest first, and how many match - one request."""
        params = {"filter": job_filter(updated_after=updated_after), "sort": "-jobId"}
        items, total = self._page(PATH, params, 0, min(limit, MAX_PAGE))
        return total, [j for r in items if (j := parse_job(r)) is not None]

    def oldest_start(self) -> datetime | None:
        """When the oldest job NetBackup still has started - the point
        behind which there is no history to fetch."""
        items, _ = self._page(PATH, {"sort": "startTime"}, 0, 1)
        for resource in items:
            job = parse_job(resource)
            if job is not None:
                return job.start_time
        return None

    def get(self, job_id: int) -> Job | None:
        """One job (GET /admin/jobs/{id}), or None if NetBackup no longer
        has it."""
        try:
            body = self._get(f"{PATH}/{job_id}")
        except NotFoundError:
            return None
        return parse_job(body.get("data", body))

    def try_logs(self, job_id: int) -> Entities:
        """The job's try logs - the detailed status lines
        (GET /admin/jobs/{id}/try-logs)."""
        return self._all(f"{PATH}/{job_id}/try-logs")

    def file_lists(self, job_id: int) -> Entity:
        """What a backup job covered (GET /admin/jobs/{id}/file-lists)."""
        body: Entity = self._get(f"{PATH}/{job_id}/file-lists")
        return flatten(body.get("data", body)) if isinstance(body.get("data"), dict) else body

    # -- changes -----------------------------------------------------------

    def cancel(self, job_id: int) -> None:
        self._change("POST", f"{PATH}/{job_id}/cancel")

    def suspend(self, job_id: int) -> None:
        self._change("POST", f"{PATH}/{job_id}/suspend")

    def resume(self, job_id: int) -> None:
        self._change("POST", f"{PATH}/{job_id}/resume")

    def restart(self, job_id: int) -> None:
        self._change("POST", f"{PATH}/{job_id}/restart")
