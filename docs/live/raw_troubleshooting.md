# `nbu.raw.troubleshooting`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_log_record` - GET /troubleshooting/log-records/{recordId}

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
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
```

## `get_log_records` - GET /troubleshooting/log-records

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
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
```

## `get_root` - GET /status-codes/{statusCode}

> **SKIPPED** on this run: nothing on this server to look at here

```python
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
```

## `list_log_record_settings` - GET /troubleshooting/log-records/{recordId}/settings

> **SKIPPED** on this run: not swept: starts work or returns a file

```python
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
```
