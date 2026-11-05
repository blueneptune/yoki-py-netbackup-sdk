"""A real backup, end to end: policy, manual backup, job, image, expiry.

Only with NBU_LIVE_CHANGES=yes. The run makes its own `bltlive-<run>-bkp`
policy, backs up one small file that is on every NetBackup server - its
own version file - from the primary to a disk storage unit the server
already writes to, follows the job to the end, reads the image back from
the catalog, and expires that image again. The image is found by its
policy name and checked to be this run's before it is expired, and it is
expired by its backup id alone: never the catalog-wide forms of the same
call (by server, by recalculating), which would touch other images.
"""

from __future__ import annotations

import copy
import time
from collections.abc import Iterator
from typing import Any

import pytest
from sdk_primer import NotFoundError, SDKError

from netbackup_sdk import NetBackupClient

from .conftest import PREFIX
from .recorder import Entry

pytestmark = pytest.mark.usefixtures("changes")

POLICY = f"{PREFIX}-bkp"
SCHEDULE = "bltlive-full"
# Small, and on every NetBackup server, primary or media.
SELECTION = "/usr/openv/netbackup/bin/version"
# The special date NetBackup reads as "expire now" (bpexpdate 0).
NOW = "1970-01-01T00:00:00.000Z"
JOB_TIMEOUT = 900


def _expire(nbu: NetBackupClient, backup_id: str) -> None:
    """Expire one image, by its backup id only."""
    nbu.raw.catalog.post_images_update_expiration_date(
        body={
            "data": {
                "type": "byBackupId",
                "attributes": {
                    "backupId": backup_id,
                    "date": NOW,
                    "delete": True,
                    "immediate": True,
                    "followDependee": False,
                },
            }
        }
    )


def _ours(nbu: NetBackupClient, prefix: str) -> list[dict[str, Any]]:
    """Recent images (the catalog's default window, the last day) whose
    policy name starts with `prefix`. The catalog filters on equality
    only - `startswith` is refused - so the prefix is checked here."""
    answer = nbu.raw.catalog.list_images(page_limit=100)
    return [
        image
        for image in answer.get("data", [])
        if str(image["attributes"].get("policyName", "")).startswith(prefix)
    ]


@pytest.fixture(scope="module", autouse=True)
def tidy(nbu: NetBackupClient) -> Iterator[None]:
    """At the end: expire every bltlive image and delete every bltlive
    backup policy, this run's or a failed run's."""
    yield
    if not nbu.allow_changes:
        return
    for image in _ours(nbu, "bltlive-"):
        try:
            _expire(nbu, image["id"])
        except SDKError:
            pass
    for policy in nbu.raw.config.list_policies().get("data", []):
        if str(policy["id"]).startswith("bltlive-"):
            nbu.raw.config.delete_policy(policy["id"])


def _primary(nbu: NetBackupClient) -> str:
    for host in nbu.raw.config.list_hosts().get("hosts", []):
        if host.get("masterServer"):
            return str(host["masterServer"])
    pytest.skip("the primary's own name is not in /config/hosts")


def _disk_unit(nbu: NetBackupClient) -> str:
    """A disk storage unit on the server's own disk (not cloud), the one
    with the most free space."""
    units = [
        u["attributes"]
        for u in nbu.raw.storage.list_storage_units().get("data", [])
        if u["attributes"].get("storageType") == "Disk" and not u["attributes"].get("isCloudSTU")
    ]
    if not units:
        pytest.skip("no disk storage unit that is not cloud")
    return str(max(units, key=lambda u: u.get("freeCapacityBytes") or 0)["name"])


def _template(nbu: NetBackupClient) -> dict[str, Any]:
    for policy in nbu.raw.config.list_policies().get("data", []):
        if policy["attributes"]["policy"]["policyType"] == "Standard":
            full = nbu.raw.config.get_policy(policy["id"])["data"]["attributes"]["policy"]
            if full.get("schedules"):
                return copy.deepcopy(full)
    pytest.skip("no Standard policy with a schedule to copy settings from")


def _wait(nbu: NetBackupClient, job_ids: list[int]) -> list[Any]:
    deadline = time.monotonic() + JOB_TIMEOUT
    while True:
        jobs = [nbu.jobs.get(job_id) for job_id in job_ids]
        if all(job is not None and job.state == "DONE" for job in jobs):
            return jobs
        if time.monotonic() > deadline:
            pytest.fail(f"jobs {job_ids} not done after {JOB_TIMEOUT}s")
        time.sleep(10)


def test_backup_and_expire(nbu: NetBackupClient, record: Entry) -> None:
    """Back up one file with a policy made for the purpose; follow the job;
    find the image; expire it.

    The policy is a copy of an existing Standard policy's settings: one
    client (the primary itself), one file, one Full schedule with no start
    window - so it only ever runs when asked - writing to a disk storage
    unit on the server's own disk, kept for the shortest retention level."""
    template = _template(nbu)
    client = _primary(nbu)
    unit = _disk_unit(nbu)
    known = (template.get("clients") or [{}])[0]

    policy = copy.deepcopy(template)
    policy["policyName"] = POLICY
    attributes = policy["policyAttributes"]
    attributes["active"] = True
    attributes["storage"] = unit
    attributes["storageIsSLP"] = False
    attributes["useAccelerator"] = False
    attributes["keyword"] = "bltlive"
    policy["clients"] = [
        {
            "hostName": client,
            "hardware": known.get("hardware", "Linux"),
            "OS": known.get("OS", "RedHat2.6.32"),
        }
    ]
    policy["backupSelections"] = {"selections": [SELECTION]}
    schedule = copy.deepcopy(template["schedules"][0])
    schedule["scheduleName"] = SCHEDULE
    schedule["scheduleType"] = "Calendar"
    schedule["backupType"] = "Full Backup"
    for window in schedule.get("startWindow") or []:
        window["startSeconds"] = 0
        window["durationSeconds"] = 0
    schedule["storageIsSLP"] = False
    schedule["backupCopies"] = {
        "copies": [
            {
                "retentionLevel": 0,
                "retentionPeriod": {"value": 1, "unit": "WEEKS"},
                "storage": unit,
            }
        ],
        "priority": -1,
    }
    policy["schedules"] = [schedule]
    nbu.raw.config.post_policies(
        body={"data": {"type": "policy", "id": POLICY, "attributes": {"policy": policy}}}
    )

    started = nbu.raw.admin.post_manual_backup(
        body={
            "data": {
                "type": "backupRequest",
                "attributes": {
                    "policyName": POLICY,
                    "scheduleName": SCHEDULE,
                    "clientName": client,
                    "keyword": "bltlive",
                },
            }
        }
    )
    job_ids = [int(job["id"]) for job in started.get("data", [])]
    assert job_ids, f"the manual backup started no job: {started}"
    jobs = _wait(nbu, job_ids)
    record.result(
        {
            "jobs": [
                {
                    "jobId": job.job_id,
                    "jobType": job.job_type,
                    "state": job.state,
                    "status": job.status,
                    "storageUnit": job.storage_unit,
                }
                for job in jobs
            ]
        }
    )
    assert all(job.status in (0, 1) for job in jobs), [(j.job_id, j.status) for j in jobs]

    images = _ours(nbu, POLICY)
    assert images, "no image in the catalog for the policy"
    backup_id = images[0]["id"]
    image = nbu.raw.catalog.get_image(backup_id)["data"]["attributes"]
    assert image["policyName"] == POLICY  # ours, before anything is expired
    record.result(
        {
            k: image.get(k)
            for k in ("policyName", "scheduleName", "clientName", "backupTime", "kilobytes")
        }
    )
    record.result(nbu.raw.catalog.list_image_contents_by_backup_id(backup_id))

    _expire(nbu, backup_id)
    with pytest.raises(NotFoundError):
        nbu.raw.catalog.get_image(backup_id)

    nbu.raw.config.delete_policy(POLICY)
