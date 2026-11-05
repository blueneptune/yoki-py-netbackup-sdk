"""The generated layer (netbackup_sdk.raw): every one of its calls sends the
method and path its docstring names, and a read-only client refuses every
call that is not a GET."""

from __future__ import annotations

import inspect
import re
from collections.abc import Iterator

import httpx
import pytest
import respx
from conftest import BASE

from netbackup_sdk import NetBackupClient
from netbackup_sdk._base import ChangesNotAllowed


def calls() -> Iterator[tuple[str, str, str, str]]:
    client = NetBackupClient(BASE, api_key="k")
    for area_name, area in vars(client.raw).items():
        for name, method in inspect.getmembers(area, inspect.ismethod):
            if name.startswith("_"):
                continue
            doc = inspect.getdoc(method) or ""
            match = re.match(r"`(GET|POST|PUT|PATCH|DELETE) (\S+)`", doc)
            assert match, f"{area_name}.{name} has no `METHOD /path` docstring"
            yield area_name, name, match.group(1), match.group(2)


CALLS = list(calls())


def test_every_operation_is_there() -> None:
    assert len(CALLS) == 733


@pytest.mark.parametrize(("area", "name", "verb", "template"), CALLS, ids=lambda v: str(v))
def test_sends_its_method_and_path(area: str, name: str, verb: str, template: str) -> None:
    pattern = re.compile(
        "^/netbackup" + re.sub(r"\\\{[^}]+\\\}", "[^/]+", re.escape(template)) + "$"
    )
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        route = router.route().respond(200, json={})
        nbu = NetBackupClient(BASE, api_key="k", allow_changes=True, api_version="9.0")
        method = getattr(getattr(nbu.raw, area), name)
        args = [
            f"x{i}"
            for i, p in enumerate(inspect.signature(method).parameters.values())
            if p.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD
        ]
        method(*args)
    request: httpx.Request = route.calls.last.request
    assert request.method == verb
    assert pattern.match(request.url.path), (request.url.path, template)
    accept = request.headers["Accept"]
    # Pings take no version (auth.UNVERSIONED); a standard media type such
    # as application/pkix-crl is sent as it is.
    if not template.endswith("/ping") and "vnd.netbackup" in accept:
        assert "version=9.0" in accept


def test_read_only_client_refuses_changes() -> None:
    nbu = NetBackupClient(BASE, api_key="k")
    with pytest.raises(ChangesNotAllowed):
        nbu.raw.config.delete_policy("bltlive-x")


def test_text_answers_keep_their_media_type() -> None:
    """A call that answers CSV asks for CSV, with the version added."""
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        route = router.route().respond(200, text="a,b\n", headers={"content-type": "text/csv"})
        nbu = NetBackupClient(BASE, api_key="k", api_version="9.0")
        assert nbu.raw.security.list_anomalies_exports() == "a,b\n"
    accept = route.calls.last.request.headers["Accept"]
    assert accept == "text/vnd.netbackup+csv;version=9.0"
