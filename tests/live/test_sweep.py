"""Every read in the generated layer (`nbu.raw`), against the real server.

One test per GET operation. A path that takes an id - `/storage/disk-pools/
{diskPoolId}` - gets one from the listing above it (`/storage/disk-pools`),
so the sweep reaches as deep as the server has things to show. Each call's
answer goes on the page for its area: docs/live/raw-<area>.md.

A call NetBackup answers with an error is skipped, with NetBackup's own
words: usually a feature this server does not use (cloud, BMR, malware
scanning) - the page says which, and coverage counts only real answers.
"""

from __future__ import annotations

import inspect
import re
from functools import cache
from typing import Any

import pytest
from sdk_primer import SDKError

from netbackup_sdk import NetBackupClient

from .recorder import Entry

# GETs that start work or hand back large files rather than describe
# something; read with care, not swept.
NOT_SWEPT = re.compile(r"download|/logs?\b|export|/files\b|/content|refresh|/streams?\b", re.I)


def _operations() -> list[tuple[str, str, str]]:
    """(area, method name, path template) for every raw GET."""
    nbu = NetBackupClient("https://unused.invalid/netbackup", api_key="-")
    found = []
    for area, group in vars(nbu.raw).items():
        for name, method in inspect.getmembers(group, inspect.ismethod):
            match = re.match(r"`GET (\S+)`", inspect.getdoc(method) or "")
            if match and not name.startswith("_"):
                found.append((area, name, match.group(1)))
    return sorted(found)


OPERATIONS = _operations()
_cache: dict[str, Any] = {}


def _first_ids(answer: Any) -> list[str]:
    """Ids from a listing, whatever its shape."""
    items: Any = answer
    if isinstance(answer, dict):
        items = answer.get("data", answer)
        if isinstance(items, dict):
            items = next((v for v in items.values() if isinstance(v, list)), [items])
    if not isinstance(items, list):
        return []
    ids = []
    for item in items[:3]:
        if isinstance(item, dict):
            value = item.get("id") or (item.get("attributes") or {}).get("name") or item.get("name")
            if value not in (None, ""):
                ids.append(str(value))
    return ids


@cache
def _by_template() -> dict[str, tuple[str, str]]:
    return {template: (area, name) for area, name, template in OPERATIONS}


def _resolve(nbu: NetBackupClient, template: str) -> list[str] | None:
    """Values for the template's path parameters, from the listings above
    it - or None if the server has nothing there to look at."""
    params = re.findall(r"\{[^}]+\}", template)
    values: list[str] = []
    for i, _ in enumerate(params):
        # The listing is the path up to (not including) this parameter.
        prefix = template.split(params[i])[0].rstrip("/")
        parent = _by_template().get(prefix)
        if parent is None:
            return None
        parent_values = values[: prefix.count("{")]
        key = f"{prefix}|{parent_values}"
        if key not in _cache:
            area, name = parent
            try:
                _cache[key] = getattr(getattr(nbu.raw, area), name)(*parent_values)
            except SDKError:
                _cache[key] = None
        ids = _first_ids(_cache[key])
        if not ids:
            return None
        values.append(ids[0])
    return values


def _why(error: SDKError) -> str:
    """NetBackup's own account of a refusal: status, code, message."""
    detail = error.detail if isinstance(error.detail, dict) else {}
    code = detail.get("errorCode")
    message = error.server_message or ""
    return (
        f"{error.status_code}"
        + (f" (error {code})" if code else "")
        + (f" - {message}" if message else "")
    )


@pytest.mark.parametrize(
    ("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
    record.page = f"raw_{area}"
    record.title = f"`{name}` - GET {template}"
    if NOT_SWEPT.search(template):
        pytest.skip("not swept: starts work or returns a file")
    values = _resolve(nbu, template)
    if values is None:
        pytest.skip("nothing on this server to look at here")
    shown = ", ".join(repr(v) for v in values)
    record.code = f"nbu.raw.{area}.{name}({shown})"
    try:
        answer = getattr(getattr(nbu.raw, area), name)(*values)
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
