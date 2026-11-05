# `nbu.raw.bmr`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_client` - GET /bare-metal-restore/clients/{clientName}

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

**On the wire**

- `GET /bare-metal-restore/clients` -> **503** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/clients` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/clients` -> **503** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `get_client_configuration_hosts`

GET /bare-metal-restore/clients/{clientName}/configurations/{configurationName}/hosts

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

## `get_client_configuration_network_routes`

GET /bare-metal-restore/clients/{clientName}/configurations/{configurationName}/network-routes

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

## `get_client_configuration_system_info`

GET /bare-metal-restore/clients/{clientName}/configurations/{configurationName}/system-info

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

## `get_configuration_layouts`

GET /bare-metal-restore/configurations/{configurationId}/{layoutResourceType}/{layoutResourceId}/layouts

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

## `get_shared_resource_tree`

GET /bare-metal-restore/shared-resource-trees/{sharedResourceTreeId}

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

**On the wire**

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_boot_servers` - GET /bare-metal-restore/boot-servers

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_boot_servers()
```

**On the wire**

- `GET /bare-metal-restore/boot-servers` -> **503** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/boot-servers` -> **503** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/boot-servers` -> **503** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_client_configurations` - GET /bare-metal-restore/clients/{clientName}/configurations

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

## `list_clients` - GET /bare-metal-restore/clients

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_clients()
```

**On the wire**

- `GET /bare-metal-restore/clients` -> **503** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/clients` -> **503** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/clients` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_configuration_disks`

GET /bare-metal-restore/configurations/{configurationId}/disks

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

## `list_configuration_empty_disks`

GET /bare-metal-restore/configurations/{configurationId}/empty-disks

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

## `list_configuration_licenses`

GET /bare-metal-restore/configurations/{configurationId}/licenses

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

## `list_configuration_multiple_devices`

GET /bare-metal-restore/configurations/{configurationId}/multiple-devices

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

## `list_configuration_native_disks`

GET /bare-metal-restore/configurations/{configurationId}/native-disks

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

## `list_configuration_native_partitions`

GET /bare-metal-restore/configurations/{configurationId}/native-partitions

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

## `list_configuration_network_interfaces`

GET /bare-metal-restore/configurations/{configurationId}/network-interfaces

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

## `list_configuration_non_managed_disks`

GET /bare-metal-restore/configurations/{configurationId}/non-managed-disks

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

## `list_configuration_packages`

GET /bare-metal-restore/configurations/{configurationId}/packages

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

## `list_configuration_partitions`

GET /bare-metal-restore/configurations/{configurationId}/partitions

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

## `list_configuration_slices`

GET /bare-metal-restore/configurations/{configurationId}/slices

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

## `list_configuration_storage_pools`

GET /bare-metal-restore/configurations/{configurationId}/storage-pools

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

## `list_configuration_volume_group_thin_pools`

GET /bare-metal-restore/configurations/{configurationId}/volume-groups/{volumeGroupId}/thin-pools

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

## `list_configuration_volume_groups`

GET /bare-metal-restore/configurations/{configurationId}/volume-groups

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

## `list_configuration_volumes`

GET /bare-metal-restore/configurations/{configurationId}/volumes

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

## `list_configuration_windows_devices`

GET /bare-metal-restore/configurations/{configurationId}/windows-devices

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

## `list_configuration_zfs_file_systems`

GET /bare-metal-restore/configurations/{configurationId}/zfs-file-systems

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

## `list_configuration_zfs_volumes`

GET /bare-metal-restore/configurations/{configurationId}/zfs-volumes

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

## `list_discovered_configurations` - GET /bare-metal-restore/discovered-configurations

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_discovered_configurations()
```

**On the wire**

- `GET /bare-metal-restore/discovered-configurations` -> **503** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/discovered-configurations` -> **503** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/discovered-configurations` -> **503** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_packages` - GET /bare-metal-restore/packages

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_packages()
```

**On the wire**

- `GET /bare-metal-restore/packages` -> **503** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/packages` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/packages` -> **503** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_shared_resource_trees` - GET /bare-metal-restore/shared-resource-trees

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_shared_resource_trees()
```

**On the wire**

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/shared-resource-trees` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_tasks` - GET /bare-metal-restore/tasks

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_tasks()
```

**On the wire**

- `GET /bare-metal-restore/tasks` -> **503** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/tasks` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/tasks` -> **503** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_vm_conversion_tasks` - GET /bare-metal-restore/vm-conversion-tasks

> **SKIPPED** on this run: NetBackup answered: 503 (error 3100) - Unable to reach the BMR server due to downtime or not configured.

```python
nbu.raw.bmr.list_vm_conversion_tasks()
```

**On the wire**

- `GET /bare-metal-restore/vm-conversion-tasks` -> **503** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/vm-conversion-tasks` -> **503** (0.18 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

- `GET /bare-metal-restore/vm-conversion-tasks` -> **503** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 3100,
    "errorMessage": "Unable to reach the BMR server due to downtime or not configured.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>
