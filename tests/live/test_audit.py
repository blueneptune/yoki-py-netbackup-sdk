"""Who changed what: NetBackup's audit log, and access-control roles.

Only with NBU_LIVE_CHANGES=yes. The audit test makes, changes and deletes
its own `bltlive-<run>-audit` policy, then reads back the audit records
those three changes left: what blt's change log reads to say who made a
change, and what the change was (each setting's old and new value). The
role test makes a `bltlive-<run>-role` role with no users or groups - it
grants nothing to anyone - changes it and deletes it.
"""

from __future__ import annotations

import copy
from collections.abc import Iterator
from typing import Any

import pytest
from sdk_primer import NotFoundError

from netbackup_sdk import NetBackupClient

from .conftest import PREFIX
from .recorder import Entry

pytestmark = pytest.mark.usefixtures("changes")


@pytest.fixture(scope="module", autouse=True)
def tidy(nbu: NetBackupClient) -> Iterator[None]:
    """At the end: remove every bltlive policy and role."""
    yield
    if not nbu.allow_changes:
        return
    for policy in nbu.raw.config.list_policies().get("data", []):
        if str(policy["id"]).startswith("bltlive-"):
            nbu.raw.config.delete_policy(policy["id"])
    for role in nbu.raw.accesscontrol.list_roles().get("data", []):
        if str(role["attributes"].get("name", "")).startswith("bltlive-"):
            nbu.raw.accesscontrol.delete_role(role["id"])


def _last_audit_id(nbu: NetBackupClient) -> int:
    answer = nbu.raw.security.list_auditlogs(sort="-id", page_limit=1)
    data = answer.get("data") or [{"id": 0}]
    return int(data[0]["id"])


def _audit_since(nbu: NetBackupClient, after: int, category: str) -> list[dict[str, Any]]:
    """Audit records newer than `after`, of one category, oldest first."""
    answer = nbu.raw.security.list_auditlogs(
        filter_=f"category eq '{category}' and id gt {after}", sort="id", page_limit=100
    )
    return [record["attributes"] | {"id": record["id"]} for record in answer.get("data", [])]


def _policy(nbu: NetBackupClient, name: str) -> dict[str, Any]:
    for policy in nbu.raw.config.list_policies().get("data", []):
        if policy["attributes"]["policy"]["policyType"] == "Standard":
            full = nbu.raw.config.get_policy(policy["id"])["data"]["attributes"]["policy"]
            body = copy.deepcopy(full)
            body["policyName"] = name
            body["policyAttributes"]["active"] = False
            body["clients"] = []
            body["schedules"] = []
            body["backupSelections"] = {"selections": ["/tmp/bltlive"]}
            return body
    pytest.skip("no Standard policy on the server to copy settings from")


def test_policy_changes_are_audited(nbu: NetBackupClient, record: Entry) -> None:
    """Create, change and delete a policy; the audit log then holds one
    record for each - the operation, the user who made it, and for the
    change each setting's old and new value. The create and the delete
    send a reason (`X-NetBackup-Audit-Reason`), which the record of what
    happened keeps.

    NetBackup writes two records per change: one as the user starts it
    ("User 'x' is modifying policy 'p'"), and one per part that changed
    ("Attributes of Policy 'p' were modified", "Include list settings of
    Policy 'p' were modified"), which hold the old and new values.
    Filtered by `id gt <the last id before>` and `category eq 'POLICY'`,
    so only this test's records come back (the audit log filters on id,
    category, operation, userName, domainName and auditDateTime)."""
    name = f"{PREFIX}-audit"
    reason = f"{PREFIX}: change CHG0000001"
    before = _last_audit_id(nbu)
    body = _policy(nbu, name)
    nbu.raw.config.post_policies(
        body={"data": {"type": "policy", "id": name, "attributes": {"policy": body}}},
        x_net_backup_audit_reason=reason,
    )
    body = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
    body["policyAttributes"]["priority"] = 9
    nbu.raw.config.put_policy(
        name, body={"data": {"type": "policy", "id": name, "attributes": {"policy": body}}}
    )
    nbu.raw.config.delete_policy(name, x_net_backup_audit_reason=reason)

    ours = [
        r
        for r in _audit_since(nbu, before, "POLICY")
        if name in [k.get("typeIdDisplayString") for k in r.get("auditKeyList") or []]
    ]
    record.result(
        [
            {
                "operation": r.get("operation"),
                "message": r.get("message"),
                "user": (r.get("auditUserIdentity") or {}).get("userName"),
                "reason": r.get("reason"),
                "changed": [
                    (a.get("attributeName"), a.get("oldValue"), a.get("newValue"))
                    for a in r.get("auditRecordAttributeList") or []
                ],
            }
            for r in ours
        ]
    )
    operations = {r.get("operation") for r in ours}
    assert {"CREATE", "MODIFY", "DELETE"} <= operations, operations
    assert all((r.get("auditUserIdentity") or {}).get("userName") for r in ours)
    priority = [
        a
        for r in ours
        if r.get("operation") == "MODIFY"
        for a in r.get("auditRecordAttributeList") or []
        if "priority" in str(a.get("attributeName", "")).lower()
    ]
    assert priority and priority[0].get("newValue") == "9", priority
    # Each change leaves two kinds of record: one as the user starts it
    # ("User 'x' is deleting policy ..."), without the reason, and one
    # for what happened ("Policy ... was deleted"), with it. A reason sent
    # with the change is how a change made through blt can carry its
    # change number into NetBackup's own log.
    done = [r for r in ours if " was " in str(r.get("message"))]
    assert {r.get("operation") for r in done} >= {"CREATE", "DELETE"}
    assert all(
        r.get("reason") == reason for r in done if r.get("operation") in ("CREATE", "DELETE")
    ), [(r.get("operation"), r.get("reason")) for r in done]
    starting = [r for r in ours if " is " in str(r.get("message"))]
    assert {r.get("operation") for r in starting} >= {"CREATE", "MODIFY", "DELETE"}


def test_role_lifecycle(nbu: NetBackupClient, record: Entry) -> None:
    """An access-control role with nobody in it: create, read, rename,
    delete. Its access definitions (what the role may do, on what) start
    empty."""
    name = f"{PREFIX}-role"
    created = nbu.raw.accesscontrol.post_roles(
        body={"data": {"type": "accessControlRoleV8", "attributes": {"name": name}}}
    )
    role_id = created["data"]["id"]
    role = nbu.raw.accesscontrol.get_role(role_id)["data"]
    assert role["attributes"]["name"] == name
    definitions = nbu.raw.accesscontrol.list_role_access_definitions(role_id)

    renamed = f"{name}-2"
    nbu.raw.accesscontrol.put_role(
        role_id,
        body={"data": {"type": "accessControlRoleV8", "attributes": {"name": renamed}}},
    )
    after = nbu.raw.accesscontrol.get_role(role_id)["data"]["attributes"]
    record.result({"name": after.get("name"), "accessDefinitions": definitions.get("data")})
    assert after["name"] == renamed

    nbu.raw.accesscontrol.delete_role(role_id)
    with pytest.raises(NotFoundError):
        nbu.raw.accesscontrol.get_role(role_id)
