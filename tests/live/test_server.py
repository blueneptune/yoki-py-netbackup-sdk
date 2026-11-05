"""The server: is it there, which release, which API version."""

from __future__ import annotations

from netbackup_sdk import NetBackupClient

from .recorder import Entry


def test_ping(nbu: NetBackupClient, record: Entry) -> None:
    """Ping the primary.

    `GET /ping` is the cheapest call there is: it needs no API version and
    answers with the server's clock, in milliseconds since 1970."""
    answer = record.result(nbu.server.ping())
    assert answer


def test_server_info(nbu: NetBackupClient, record: Entry) -> None:
    """Ask the primary who it is.

    `nbuVersion` is the release ("NetBackup_10.2"), which decides the API
    versions the server accepts; `domainType` is how its users sign in."""
    info = record.result(nbu.server.info())
    assert str(info["nbuVersion"]).startswith("NetBackup_")
    assert info["serverName"]


def test_api_version_is_negotiated(nbu: NetBackupClient, record: Entry) -> None:
    """Settle the API version.

    With `api_version="auto"` (the default) the client offers the newest
    version it knows and steps down on a 406 until the server accepts one.
    The 406s on the wire below are that negotiation, not errors."""
    nbu.jobs.sample(1)
    record.note(f"The client settled on API version **{nbu.api_version}**.")
    assert nbu.api_version
