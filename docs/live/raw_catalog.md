# `nbu.raw.catalog`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_asset-20_image` - GET /catalog/asset-20-images/{backupId}

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

## `get_hyperv_image` - GET /catalog/hyperv-images/{backupId}

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

## `get_image` - GET /catalog/images/{backupId}

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

- `GET /catalog/images` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>

## `get_images_bulk_update_primary_copy_request` - GET /catalog/images/bulk-update-primary-copy-requests/{requestId}

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

## `get_images_content` - GET /catalog/images/contents/{requestId}

> **SKIPPED** on this run: not swept: starts work or returns a file

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

## `get_vmware_image` - GET /catalog/vmware-images/{backupId}

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

- `GET /catalog/vmware-images` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>

## `list_image_contents` - GET /catalog/image-contents

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.catalog.list_image_contents()
```

**On the wire**

- `GET /catalog/image-contents` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8961,
    "errorMessage": "An invalid API request is encountered.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "Invalid filter parameters."
    ]
  }
  ```

  </details>

## `list_image_contents_by_backup_id` - GET /catalog/images/{backupId}/contents

> **SKIPPED** on this run: not swept: starts work or returns a file

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

## `list_image_copy_cloud_recovery_targets` - GET /catalog/images/{backupId}/copies/{copy}/cloud-recovery-targets

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

## `list_image_copy_cloud_recovery_targets_disk_restore` - GET /catalog/images/{backupId}/copies/{copy}/cloud-recovery-targets-disk-restore

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

## `list_image_copy_cloud_recovery_targets_files_folders` - GET /catalog/images/{backupId}/copies/{copy}/cloud-recovery-targets-files-folders

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

## `list_images` - GET /catalog/images

```python
nbu.raw.catalog.list_images()
```

**On the wire**

- `GET /catalog/images` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>

## `list_latest_vmware_images` - GET /catalog/latest-vmware-images

```python
nbu.raw.catalog.list_latest_vmware_images()
```

**On the wire**

- `GET /catalog/latest-vmware-images` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>

## `list_raw_partition_image_contents` - GET /catalog/raw-partition-image-contents

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.catalog.list_raw_partition_image_contents()
```

**On the wire**

- `GET /catalog/raw-partition-image-contents` -> **400** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8961,
    "errorMessage": "An invalid API request is encountered.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "Invalid filter parameters."
    ]
  }
  ```

  </details>

## `list_rollback_image_contents` - GET /catalog/rollback-image-contents

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.catalog.list_rollback_image_contents()
```

**On the wire**

- `GET /catalog/rollback-image-contents` -> **400** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8961,
    "errorMessage": "An invalid API request is encountered.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "Invalid filter parameters."
    ]
  }
  ```

  </details>

## `list_rollback_images` - GET /catalog/rollback-images

```python
nbu.raw.catalog.list_rollback_images()
```

**On the wire**

- `GET /catalog/rollback-images` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>

## `list_slp_images` - GET /catalog/slp-images

```python
nbu.raw.catalog.list_slp_images()
```

**On the wire**

- `GET /catalog/slp-images` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "limit": 100
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/catalog/slp-images?page%5Blimit%5D=100&sort=backupTime,clientName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/catalog/slp-images?page%5Blimit%5D=100&sort=backupTime,clientName"
      }
    }
  }
  ```

  </details>

## `list_tape_media` - GET /catalog/tape-media

```python
nbu.raw.catalog.list_tape_media()
```

**On the wire**

- `GET /catalog/tape-media` -> **200** (0.24 s)

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
        "href": "https://primary-01:1556/netbackup/catalog/tape-media?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/catalog/tape-media?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/catalog/tape-media?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_tir_images` - GET /catalog/tir-images

> **SKIPPED** on this run: NetBackup answered: 501 (error 8957) - Non supported - Standard | Windows restore lift & shift feature is disabled

```python
nbu.raw.catalog.list_tir_images()
```

**On the wire**

- `GET /catalog/tir-images` -> **501** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8957,
    "errorMessage": "Non supported - Standard | Windows restore lift & shift feature is disabled",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_vmware_images` - GET /catalog/vmware-images

```python
nbu.raw.catalog.list_vmware_images()
```

**On the wire**

- `GET /catalog/vmware-images` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 10
      }
    }
  }
  ```

  </details>
