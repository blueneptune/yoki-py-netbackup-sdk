# `nbu.raw.servicecatalog`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_slo` - GET /servicecatalog/slos/{sloID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(
    nbu: NetBackupClient, recorder: Recorder, record: Entry, area: str, name: str, template: str
) -> None:
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
    except SDKError:
        pytest.skip(f"NetBackup answered: {_why(recorder)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /servicecatalog/slos` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/servicecatalog/slos?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-name"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/servicecatalog/slos?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-name"
      }
    }
  }
  ```

  </details>

## `get_slo_subscription` - GET /servicecatalog/slos/{sloID}/subscriptions/{subscriptionID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(
    nbu: NetBackupClient, recorder: Recorder, record: Entry, area: str, name: str, template: str
) -> None:
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
    except SDKError:
        pytest.skip(f"NetBackup answered: {_why(recorder)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_slos` - GET /servicecatalog/slos

```python
nbu.raw.servicecatalog.list_slos()
```

**On the wire**

- `GET /servicecatalog/slos` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/servicecatalog/slos?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-name"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/servicecatalog/slos?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-name"
      }
    }
  }
  ```

  </details>
