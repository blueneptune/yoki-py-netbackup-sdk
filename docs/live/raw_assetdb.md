# `nbu.raw.assetdb`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_asset_groups` - GET /assets/{GUID}/asset-groups

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

- `GET /assets` -> **410** (0.00 s)

  <details><summary>Answer</summary>

  ```json
  "This API is no longer used for asset or asset group related operations in NetBackup and has been removed from the product.  See [Asset Service Getting Started Guide](https://host-15/content/support/en_US/doc-viewer.141221222-141221259-0.index.html) for the possible replacements of this functionality."
  ```

  </details>

## `get_user-05_by_asset_group_guid` - GET /asset-groups/{assetGroupGuid}

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

- `GET /asset-groups` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "pages": 0,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 0,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=displayName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=displayName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=displayName"
      }
    }
  }
  ```

  </details>

## `get_user-05_by_guid` - GET /assets/{GUID}

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

## `list_asset_groups` - GET /asset-groups

```python
nbu.raw.assetdb.list_asset_groups()
```

**On the wire**

- `GET /asset-groups` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "pages": 0,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 0,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=displayName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=displayName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-groups?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=displayName"
      }
    }
  }
  ```

  </details>

## `list_assets` - GET /assets

> **SKIPPED** on this run: NetBackup answered: 410

```python
nbu.raw.assetdb.list_assets()
```

**On the wire**

- `GET /assets` -> **410** (0.00 s)

  <details><summary>Answer</summary>

  ```json
  "This API is no longer used for asset or asset group related operations in NetBackup and has been removed from the product.  See [Asset Service Getting Started Guide](https://host-15/content/support/en_US/doc-viewer.141221222-141221259-0.index.html) for the possible replacements of this functionality."
  ```

  </details>
