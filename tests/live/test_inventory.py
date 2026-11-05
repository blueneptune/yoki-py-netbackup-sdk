"""What exists: policies, backup images, hosts, storage and discovered assets."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from netbackup_sdk import NetBackupClient

from .recorder import Entry


def test_policies(nbu: NetBackupClient, record: Entry) -> None:
    """Every policy: name, type, active or not."""
    policies = record.result(nbu.policies.list())
    assert all("policyName" in p or "id" in p for p in policies)


def test_policy_in_full(nbu: NetBackupClient, record: Entry) -> None:
    """One policy in full: its clients, schedules and backup selections.

    Read in NetBackup's generic schema (the client sends
    `X-NetBackup-Policy-Use-Generic-Schema: true`), which has one shape for
    every policy type."""
    policies = nbu.policies.list()
    if not policies:
        return
    name = policies[0].get("policyName") or policies[0]["id"]
    policy = record.result(nbu.policies.get(name))
    assert policy is not None


def test_missing_policy_is_none(nbu: NetBackupClient, record: Entry) -> None:
    """A policy that does not exist gives `None`."""
    assert nbu.policies.get("bltlive-no-such-policy") is None


def test_images(nbu: NetBackupClient, record: Entry) -> None:
    """Backup images from the last 30 days, newest first."""
    since = datetime.now(UTC) - timedelta(days=30)
    first = next(nbu.images.iter_pages(backed_up_after=since), [])
    record.result(first[:3])


def test_hosts(nbu: NetBackupClient, record: Entry) -> None:
    """The hosts the primary knows: itself, media servers, clients.

    Not a JSON:API listing like the rest: `{"hosts": [...]}`, all at once."""
    hosts = record.result(nbu.hosts.list())
    assert hosts and all("hostName" in h for h in hosts)


def test_storage_units(nbu: NetBackupClient, record: Entry) -> None:
    """Storage units: where a policy's backups are written."""
    record.result(nbu.storage.units())


def test_disk_pools(nbu: NetBackupClient, record: Entry) -> None:
    """Disk pools, with their capacity and use."""
    record.result(nbu.storage.disk_pools())


def test_vmware_assets(nbu: NetBackupClient, record: Entry) -> None:
    """Virtual machines NetBackup has discovered in vCenter."""
    assets = nbu.assets.workload("vmware")
    record.result(assets[:3])
