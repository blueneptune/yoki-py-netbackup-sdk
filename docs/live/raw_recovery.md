# `nbu.raw.recovery`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_workloads_cloud_paas_instant_access_image` - GET /recovery/workloads/cloud/paas/instant-access-images/{imageId}

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

- `GET /recovery/workloads/cloud/paas/instant-access-images` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_cloud_paas_instant_access_mount` - GET /recovery/workloads/cloud/paas/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/cloud/paas/instant-access-mounts` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_cloud_vm_instant_access_mount` - GET /recovery/workloads/cloud/vm/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/cloud/vm/instant-access-mounts` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_dynamic_nas_instant_access_mount` - GET /recovery/workloads/dynamic-nas/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/dynamic-nas/instant-access-mounts` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_ms_windows_instant_access_mount` - GET /recovery/workloads/ms-windows/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/ms-windows/instant-access-mounts` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_mssql_instant_access_mount` - GET /recovery/workloads/mssql/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/mssql/instant-access-mounts` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_oracle_instant_access_mount` - GET /recovery/workloads/oracle/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/oracle/instant-access-mounts` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_standard_instant_access_mount` - GET /recovery/workloads/standard/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/standard/instant-access-mounts` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_universal_share_instant_access_mount` - GET /recovery/workloads/universal-share/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/universal-share/instant-access-mounts` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_vmware_instant_access_mount` - GET /recovery/workloads/vmware/instant-access-mounts/{mountId}

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

- `GET /recovery/workloads/vmware/instant-access-mounts` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_vmware_instant_access_mount_download` - GET /recovery/workloads/vmware/instant-access-mounts/{mountId}/download

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

## `get_workloads_vmware_instant_access_vm` - GET /recovery/workloads/vmware/instant-access-vms/{mountId}

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

- `GET /recovery/workloads/vmware/instant-access-vms` -> **200** (0.27 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_vmware_instant_access_vms` - GET /recovery/workloads/vmware/instant-access-vms

```python
nbu.raw.recovery.get_workloads_vmware_instant_access_vms()
```

**On the wire**

- `GET /recovery/workloads/vmware/instant-access-vms` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_vmware_malware_scan_mount` - GET /recovery/workloads/vmware/malware-scan-mounts/{mountId}

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

- `GET /recovery/workloads/vmware/malware-scan-mounts` -> **200** (0.26 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_workloads_vmware_scenarios_instant_recovery_vms` - GET /recovery/workloads/vmware/scenarios/instant-recovery-vms

```python
nbu.raw.recovery.get_workloads_vmware_scenarios_instant_recovery_vms()
```

**On the wire**

- `GET /recovery/workloads/vmware/scenarios/instant-recovery-vms` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_check_dr_in_cloud` - GET /recovery/check-dr-in-cloud

```python
nbu.raw.recovery.list_check_dr_in_cloud()
```

**On the wire**

- `GET /recovery/check-dr-in-cloud` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "attributes": {
          "drInCloud": false
        },
        "type": "checkDrInCloudResponse",
        "id": "0"
      }
    ]
  }
  ```

  </details>

## `list_cloud_images_ami_ids` - GET /recovery/cloud-images/ami-ids

> **SKIPPED** on this run: NetBackup answered: 500 (error 130) - system error occurred

```python
nbu.raw.recovery.list_cloud_images_ami_ids()
```

**On the wire**

- `GET /recovery/cloud-images/ami-ids` -> **500** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 130,
    "errorMessage": "system error occurred",
    "attributeErrors": {
      "exception": "errorCode: 4032"
    },
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_cloud_images_cloud_vm_ids` - GET /recovery/cloud-images/cloud-vm-ids

> **SKIPPED** on this run: NetBackup answered: 500 (error 130) - system error occurred

```python
nbu.raw.recovery.list_cloud_images_cloud_vm_ids()
```

**On the wire**

- `GET /recovery/cloud-images/cloud-vm-ids` -> **500** (0.31 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 130,
    "errorMessage": "system error occurred",
    "attributeErrors": {
      "exception": "errorCode: 4032"
    },
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_workloads_cloud_paas_instant_access_images` - GET /recovery/workloads/cloud/paas/instant-access-images

```python
nbu.raw.recovery.list_workloads_cloud_paas_instant_access_images()
```

**On the wire**

- `GET /recovery/workloads/cloud/paas/instant-access-images` -> **200** (0.34 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_cloud_paas_instant_access_mounts` - GET /recovery/workloads/cloud/paas/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_cloud_paas_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/cloud/paas/instant-access-mounts` -> **200** (0.19 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_cloud_vm_instant_access_mounts` - GET /recovery/workloads/cloud/vm/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_cloud_vm_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/cloud/vm/instant-access-mounts` -> **200** (0.24 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_dynamic_nas_instant_access_mounts` - GET /recovery/workloads/dynamic-nas/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_dynamic_nas_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/dynamic-nas/instant-access-mounts` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_ms_windows_instant_access_mounts` - GET /recovery/workloads/ms-windows/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_ms_windows_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/ms-windows/instant-access-mounts` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_mssql_instant_access_mounts` - GET /recovery/workloads/mssql/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_mssql_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/mssql/instant-access-mounts` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_oracle_instant_access_mounts` - GET /recovery/workloads/oracle/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_oracle_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/oracle/instant-access-mounts` -> **200** (0.23 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_standard_instant_access_mounts` - GET /recovery/workloads/standard/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_standard_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/standard/instant-access-mounts` -> **200** (0.25 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_universal_share_instant_access_mounts` - GET /recovery/workloads/universal-share/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_universal_share_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/universal-share/instant-access-mounts` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_vmware_instant_access_mount_files` - GET /recovery/workloads/vmware/instant-access-mounts/{mountId}/files

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

## `list_workloads_vmware_instant_access_mount_folder` - GET /recovery/workloads/vmware/instant-access-mounts/{mountId}/folder

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

## `list_workloads_vmware_instant_access_mounts` - GET /recovery/workloads/vmware/instant-access-mounts

```python
nbu.raw.recovery.list_workloads_vmware_instant_access_mounts()
```

**On the wire**

- `GET /recovery/workloads/vmware/instant-access-mounts` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_workloads_vmware_malware_scan_mounts` - GET /recovery/workloads/vmware/malware-scan-mounts

```python
nbu.raw.recovery.list_workloads_vmware_malware_scan_mounts()
```

**On the wire**

- `GET /recovery/workloads/vmware/malware-scan-mounts` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>
