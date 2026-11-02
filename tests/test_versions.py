"""Asking for an API version the server supports."""

from __future__ import annotations

import httpx
import pytest
import respx
from conftest import BASE, listing

from netbackup_sdk import NetBackupClient
from netbackup_sdk.versions import ApiVersion


def version_of(request: httpx.Request) -> str:
    return request.headers["accept"].split("version=")[1]


@pytest.mark.parametrize(
    ("server", "expected"),
    [("13.0", "13.0"), ("12.0", "12.0"), ("9.0", "9.0"), ("7.0", "7.0")],
    ids=["NetBackup 11.0", "NetBackup 10.5", "NetBackup 10.2", "NetBackup 10.0"],
)
def test_auto_steps_down_until_the_server_accepts_and_then_stays(
    nbu_api: respx.MockRouter, server: str, expected: str
) -> None:
    def answer(request: httpx.Request) -> httpx.Response:
        if version_of(request) != server:
            return httpx.Response(406, json={"errorCode": 406})
        return httpx.Response(200, json=listing([]))

    jobs = nbu_api.get("/admin/jobs").mock(side_effect=answer)
    with NetBackupClient(BASE, api_key="key") as nbu:
        list(nbu.jobs.iter_pages())
        list(nbu.jobs.iter_pages())
        assert nbu.api_version == expected

    tried = [version_of(call.request) for call in jobs.calls]
    newest_first = ["13.0", "12.0", "9.0", "7.0"]
    assert tried == newest_first[: newest_first.index(expected) + 1] + [expected]


def test_password_login_steps_down_too(nbu_api: respx.MockRouter) -> None:
    def login(request: httpx.Request) -> httpx.Response:
        if version_of(request) != "12.0":
            return httpx.Response(406)
        return httpx.Response(200, json={"token": "jwt-1", "validity": 86400})

    nbu_api.post("/login").mock(side_effect=login)
    jobs = nbu_api.get("/admin/jobs").respond(json=listing([]))
    with NetBackupClient(BASE, username="u", password="p") as nbu:
        list(nbu.jobs.iter_pages())
        assert nbu.api_version == "12.0"
    assert version_of(jobs.calls[0].request) == "12.0"


def test_a_pinned_version_is_never_changed(nbu_api: respx.MockRouter) -> None:
    jobs = nbu_api.get("/admin/jobs").respond(406)
    with NetBackupClient(BASE, api_key="key", api_version="10.5") as nbu:
        with pytest.raises(Exception):  # noqa: B017 - sdk-primer's 4xx error
            list(nbu.jobs.iter_pages())
        assert nbu.api_version == "12.0"
    assert jobs.call_count == 1


def test_ping_takes_no_version_and_settles_none(nbu_api: respx.MockRouter) -> None:
    # As a 10.2 primary does: plain text, and 406 to any versioned type.
    def answer(request: httpx.Request) -> httpx.Response:
        if "version=" in request.headers["accept"]:
            return httpx.Response(406)
        return httpx.Response(200, text="1793601950836")

    nbu_api.get("/ping").mock(side_effect=answer)
    jobs = nbu_api.get("/admin/jobs").mock(
        side_effect=lambda r: httpx.Response(
            406 if version_of(r) != "9.0" else 200, json=listing([])
        )
    )
    with NetBackupClient(BASE, api_key="key") as nbu:
        assert nbu.server.ping() == {"answer": 1793601950836}
        list(nbu.jobs.iter_pages())
        assert nbu.api_version == "9.0"
    assert [version_of(c.request) for c in jobs.calls] == ["13.0", "12.0", "9.0"]


def test_a_release_or_an_api_version_can_be_named() -> None:
    assert ApiVersion("11.0").current == "13.0"
    assert ApiVersion("10.0").current == "7.0"
    assert ApiVersion("9.0").current == "9.0"  # taken as an API version
    assert ApiVersion("10.2").current == "9.0"
    assert ApiVersion("auto").candidates == ["13.0", "12.0", "9.0", "7.0"]
