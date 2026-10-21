"""What every group of endpoints shares: how a call is made, how
NetBackup's paged listings are walked, how filters are written, and the
rule about changes.

- `_get` / `_pages`  - reads. Retried on a timeout or a gateway error.
- `_change`          - anything that alters NetBackup (cancelling,
                       suspending or restarting a job, starting a
                       manual backup, ...). Refused unless the client was
                       built with allow_changes=True, and sent exactly
                       once: if "restart this job" times out, NetBackup
                       may well have restarted it.
"""

from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

import httpx
from sdk_primer import SDKError, ServerError

if TYPE_CHECKING:
    from .client import NetBackupClient

Entity = dict[str, Any]
Entities = list[Entity]


class NetBackupError(SDKError):
    """NetBackup answered, and the answer was not usable."""


class ChangesNotAllowed(NetBackupError):
    """A call that would alter NetBackup was made on a client that was
    not built with allow_changes=True."""


def json_body(response: httpx.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        raise ServerError(
            f"{response.request.method} {response.request.url} returned "
            f"{response.headers.get('content-type', 'no content type')} instead of JSON."
        ) from None


def timestamp(value: datetime) -> str:
    """A time as NetBackup's filters take it: ISO 8601, UTC, with Z."""
    if value.tzinfo is None:
        raise ValueError("Filter times must be timezone-aware.")
    return value.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def quoted(value: str) -> str:
    """A string literal for a filter: single quotes, doubled inside."""
    return "'" + value.replace("'", "''") + "'"


def all_of(*conditions: str | None) -> str | None:
    """Join filter conditions with `and`, leaving out the empty ones."""
    present = [c for c in conditions if c]
    return " and ".join(present) if present else None


def flatten(resource: Entity) -> Entity:
    """A JSON:API resource ({type, id, attributes, links}) as one flat
    dictionary: its attributes, plus `id` if they lack one."""
    attributes: Entity = dict(resource.get("attributes") or {})
    attributes.setdefault("id", resource.get("id"))
    return attributes


class Resource:
    """One group of related endpoints, reached as an attribute of
    NetBackupClient."""

    def __init__(self, client: NetBackupClient) -> None:
        self._client = client

    def _get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        clean = {k: v for k, v in (params or {}).items() if v is not None}
        return json_body(self._client.api.get(path, params=clean))

    def _page(
        self, path: str, params: dict[str, Any] | None, offset: int, limit: int
    ) -> tuple[Entities, int | None]:
        """One page: (resources, the total count if NetBackup gave one).

        Listings are JSON:API: {"data": [...], "meta": {"pagination":
        {"offset", "limit", "count", "last", ...}}}."""
        body = self._get(path, {**(params or {}), "page[offset]": offset, "page[limit]": limit})
        if not isinstance(body, dict) or not isinstance(body.get("data"), list):
            raise NetBackupError(f"GET {path} did not return a listing: {str(body)[:200]}")
        pagination = (body.get("meta") or {}).get("pagination") or {}
        return body["data"], pagination.get("count")

    def _pages(
        self, path: str, params: dict[str, Any] | None = None, page_size: int | None = None
    ) -> Iterator[Entities]:
        """Every page of a listing. Stops on a short page, so it does not
        depend on the server's counts."""
        size = page_size or self._client.page_size
        offset = 0
        while True:
            items, _ = self._page(path, params, offset, size)
            if items:
                yield items
            if len(items) < size:
                return
            offset += size

    def _all(self, path: str, params: dict[str, Any] | None = None) -> Entities:
        return [flatten(item) for page in self._pages(path, params) for item in page]

    def _change(self, method: str, path: str, body: Entity | None = None) -> Any:
        if not self._client.allow_changes:
            raise ChangesNotAllowed(
                f"{method} {path} would change NetBackup; this client is read-only. "
                "Build it with allow_changes=True if that is really intended."
            )
        response = self._client.api_once.request(method, path, json=body)
        return json_body(response) if response.content else None
