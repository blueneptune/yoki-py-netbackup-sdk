# `nbu.raw.deployment`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_eebs` - GET /deployment/eebs

```python
nbu.raw.deployment.get_eebs()
```

**On the wire**

- `GET /deployment/eebs` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "eebResponse",
      "id": "0",
      "attributes": {
        "eebList": []
      },
      "meta": {
        "eebDetails": {
          "eebCount": 0
        }
      }
    }
  }
  ```

  </details>

## `get_package` - GET /deployment/packages/{packageIdentifier}

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

- `GET /deployment/packages` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "repoDetails": {
        "packagesTotal": 0,
        "repoSize": 0
      }
    }
  }
  ```

  </details>

## `list_packages` - GET /deployment/packages

```python
nbu.raw.deployment.list_packages()
```

**On the wire**

- `GET /deployment/packages` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "repoDetails": {
        "packagesTotal": 0,
        "repoSize": 0
      }
    }
  }
  ```

  </details>
