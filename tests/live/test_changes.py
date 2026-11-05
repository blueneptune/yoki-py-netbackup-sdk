"""Changes: create, read back, change and delete - on the real server.

Only with NBU_LIVE_CHANGES=yes, and only ever this run's own objects,
named `bltlive-<run>-...`; anything of that name a failed run left behind
is removed at the end. Nothing else on the server is touched: a new
object is a copy of an existing one's settings under a new name, with no
clients and switched off, so it never runs.
"""

from __future__ import annotations

import copy
from collections.abc import Iterator
from typing import Any

import pytest
from sdk_primer import NotFoundError, SDKError

from netbackup_sdk import NetBackupClient

from .conftest import PREFIX
from .recorder import Entry

pytestmark = pytest.mark.usefixtures("changes")


@pytest.fixture(scope="module", autouse=True)
def tidy(nbu: NetBackupClient) -> Iterator[None]:
    """Remove every bltlive policy and SLP when the module ends, ours or a
    failed run's."""
    yield
    if not nbu.allow_changes:
        return
    for policy in nbu.raw.config.list_policies().get("data", []):
        if str(policy["id"]).startswith("bltlive-"):
            nbu.raw.config.delete_policy(policy["id"])
    for slp in nbu.raw.config.list_slps().get("data", []):
        if str(slp["id"]).startswith("bltlive-"):
            nbu.raw.config.delete_slp(slp["id"])


def _template(nbu: NetBackupClient, policy_type: str) -> dict[str, Any]:
    for policy in nbu.raw.config.list_policies().get("data", []):
        if policy["attributes"]["policy"]["policyType"] == policy_type:
            full = nbu.raw.config.get_policy(policy["id"])
            return copy.deepcopy(full["data"]["attributes"]["policy"])
    pytest.skip(f"no {policy_type} policy on the server to copy settings from")


def test_policy_lifecycle(nbu: NetBackupClient, record: Entry) -> None:
    """A Standard policy: create, read back, change, delete.

    The body is NetBackup's generic policy schema - the same shape GET
    returns - wrapped as a JSON:API resource. A changed policy is sent
    whole with PUT; NetBackup checks it against the version it last
    gave out (the ETag) when `If-Match` is sent."""
    name = f"{PREFIX}-std"
    policy = _template(nbu, "Standard")
    policy["policyName"] = name
    policy["policyAttributes"]["active"] = False
    policy["clients"] = []
    policy["backupSelections"] = {"selections": ["/tmp/bltlive"]}
    body = {"data": {"type": "policy", "id": name, "attributes": {"policy": policy}}}

    nbu.raw.config.post_policies(body=body)
    created = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
    assert created["policyName"] == name
    assert created["policyAttributes"]["active"] is False

    created["policyAttributes"]["priority"] = 7
    created["policyAttributes"]["keyword"] = "bltlive"
    nbu.raw.config.put_policy(
        name, body={"data": {"type": "policy", "id": name, "attributes": {"policy": created}}}
    )
    changed = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
    record.result({k: changed["policyAttributes"][k] for k in ("priority", "keyword", "active")})
    assert changed["policyAttributes"]["priority"] == 7

    nbu.raw.config.delete_policy(name)
    with pytest.raises(NotFoundError):
        nbu.raw.config.get_policy(name)


def test_policy_schedules_and_clients(nbu: NetBackupClient, record: Entry) -> None:
    """A policy's parts on their own: add a client and a schedule, then
    take them out again, without sending the whole policy."""
    name = f"{PREFIX}-parts"
    policy = _template(nbu, "Standard")
    # Hardware and OS as the server already knows them from another client.
    known = (policy.get("clients") or [{}])[0]
    template_schedules = policy.get("schedules") or []
    hardware, os_name = known.get("hardware", "Linux"), known.get("OS", "RedHat2.6.18")
    policy["policyName"] = name
    policy["policyAttributes"]["active"] = False
    policy["clients"] = []
    policy["schedules"] = []
    policy["backupSelections"] = {"selections": ["/tmp/bltlive"]}
    nbu.raw.config.post_policies(
        body={"data": {"type": "policy", "id": name, "attributes": {"policy": policy}}}
    )
    client = "bltlive-client.example.com"
    nbu.raw.config.put_policy_client(
        name,
        client,
        body={
            "data": {
                "type": "client",
                "id": client,
                "attributes": {"hardware": hardware, "OS": os_name},
            }
        },
    )
    # A schedule as the server already has one, renamed.
    if not template_schedules:
        pytest.skip("the template policy has no schedule to copy")
    schedule = copy.deepcopy(template_schedules[0])
    schedule["scheduleName"] = "bltlive-full"
    try:
        nbu.raw.config.put_policy_schedule(
            name,
            "bltlive-full",
            body={"data": {"type": "schedule", "id": "bltlive-full", "attributes": schedule}},
        )
    except SDKError as error:
        record.note(f"Adding the schedule was refused: {error.server_message or error}")
        raise
    full = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
    record.result(
        {
            "clients": [c["hostName"] for c in full["clients"]],
            "schedules": [s["scheduleName"] for s in full["schedules"]],
        }
    )
    assert [c["hostName"] for c in full["clients"]] == [client]
    assert [s["scheduleName"] for s in full["schedules"]] == ["bltlive-full"]

    nbu.raw.config.delete_policy_schedule(name, "bltlive-full")
    nbu.raw.config.delete_policy_client(name, client)
    empty = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
    assert empty["clients"] == [] and empty["schedules"] == []
    nbu.raw.config.delete_policy(name)


def test_slp_lifecycle(nbu: NetBackupClient, record: Entry) -> None:
    """A storage lifecycle policy: create, read back, change, delete.

    Copied from an existing SLP, so its operations point at storage that
    exists on this server."""
    existing = nbu.raw.config.list_slps().get("data", [])
    if not existing:
        pytest.skip("no SLP on the server to copy from")
    source = copy.deepcopy(existing[0]["attributes"])
    name = f"{PREFIX}-slp"
    attributes = {
        k: v
        for k, v in source.items()
        if k in ("slpName", "duplicationPriority", "operationList", "dataClassification")
    }
    attributes["slpName"] = name
    nbu.raw.config.post_slps(body={"data": {"type": "slp", "id": name, "attributes": attributes}})
    created = nbu.raw.config.get_slp(name)["data"]["attributes"]
    assert created["slpName"] == name

    attributes["duplicationPriority"] = 5
    nbu.raw.config.put_slp(
        name, body={"data": {"type": "slp", "id": name, "attributes": attributes}}
    )
    changed = nbu.raw.config.get_slp(name)["data"]["attributes"]
    record.result({k: changed.get(k) for k in ("slpName", "versionNumber", "duplicationPriority")})
    assert changed["duplicationPriority"] == 5

    nbu.raw.config.delete_slp(name)
    with pytest.raises(NotFoundError):
        nbu.raw.config.get_slp(name)
