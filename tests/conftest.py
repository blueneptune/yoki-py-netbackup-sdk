from __future__ import annotations

from collections.abc import Iterator
from typing import Any

import pytest
import respx

BASE = "https://nbu.test:1556/netbackup"


def resource(kind: str, rid: object, attributes: dict[str, Any]) -> dict[str, Any]:
    return {"type": kind, "id": str(rid), "attributes": attributes}


def listing(items: list[dict[str, Any]], count: int | None = None) -> dict[str, Any]:
    return {
        "data": items,
        "meta": {"pagination": {"count": len(items) if count is None else count}},
    }


@pytest.fixture
def nbu_api() -> Iterator[respx.MockRouter]:
    """Every request intercepted; one nobody mocked fails the test
    instead of reaching the network."""
    with respx.mock(base_url=BASE, assert_all_called=False) as router:
        router.post("/login").respond(json={"token": "jwt-1", "validity": 86400})
        router.post("/logout").respond(204)
        yield router
