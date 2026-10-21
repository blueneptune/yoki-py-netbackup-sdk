"""A typed model for the thing callers work with most - a job. Everything
else the SDK returns is NetBackup's own attributes as dictionaries.

The model keeps NetBackup's record untouched in `raw`, and ignores
attributes it does not name, so a newer server does not break parsing.
"""

from __future__ import annotations

from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator

# A job in any other state has not finished.
DONE = "DONE"


class Job(BaseModel):
    """One NetBackup job: a backup, a restore, an image cleanup, ...

    `state` says where it is (QUEUED, ACTIVE, REQUEUED, SUSPENDED,
    INCOMPLETE, WAITING_FOR_RETRY, DONE). `status` is NetBackup's status
    code, meaningful once DONE: 0 succeeded, 1 partially succeeded,
    anything else failed (the code says why).
    """

    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    job_id: int = Field(alias="jobId")
    parent_job_id: int | None = Field(default=None, alias="parentJobId")
    job_type: str | None = Field(default=None, alias="jobType")
    state: str = ""
    status: int | None = None
    policy_name: str | None = Field(default=None, alias="policyName")
    policy_type: str | None = Field(default=None, alias="policyType")
    schedule_name: str | None = Field(default=None, alias="scheduleName")
    schedule_type: str | None = Field(default=None, alias="scheduleType")
    client_name: str | None = Field(default=None, alias="clientName")
    media_server: str | None = Field(default=None, alias="destinationMediaServerName")
    storage_unit: str | None = Field(default=None, alias="destinationStorageUnitName")
    backup_id: str | None = Field(default=None, alias="backupId")
    start_time: AwareDatetime | None = Field(default=None, alias="startTime")
    end_time: AwareDatetime | None = Field(default=None, alias="endTime")
    last_update_time: AwareDatetime | None = Field(default=None, alias="lastUpdateTime")
    kilobytes_transferred: int | None = Field(default=None, alias="kilobytesTransferred")
    # API 12.0 (NetBackup 10.5) and later: what was actually sent, where
    # kilobytesTransferred may be an estimate.
    kilobytes_data_transferred: int | None = Field(default=None, alias="kilobytesDataTransferred")
    number_of_files: int | None = Field(default=None, alias="numberOfFiles")
    percent_complete: int | None = Field(default=None, alias="percentComplete")
    raw: dict[str, Any] = Field(default_factory=dict)

    @field_validator("start_time", "end_time", "last_update_time", mode="before")
    @classmethod
    def _zero_is_none(cls, value: object) -> object:
        # Unset times have been reported as the epoch, or an empty string.
        if value in ("", None) or (isinstance(value, str) and value.startswith("1970-01-01")):
            return None
        return value

    @property
    def is_active(self) -> bool:
        return self.state != DONE


def job_from(resource: dict[str, Any]) -> Job:
    """A Job from a JSON:API resource, or from its bare attributes."""
    attributes = resource.get("attributes", resource)
    if "jobId" not in attributes and "id" in resource:
        attributes = {**attributes, "jobId": resource["id"]}
    return Job.model_validate({**attributes, "raw": attributes})
