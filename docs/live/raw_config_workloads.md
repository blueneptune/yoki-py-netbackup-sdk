# `nbu.raw.config_workloads`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_workloads_rhv_rhv_recovery_topology` - GET /config/workloads/rhv/rhv-recovery-topologies/{rhv-id}

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

## `get_workloads_rhv_rhv_topology` - GET /config/workloads/rhv/rhv-topologies/{rhv-id}

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

## `get_workloads_rhv_rhv_topology_datacenter_storage_domains` - GET /config/workloads/rhv/rhv-topologies/{rhv-id}/datacenters/{datacenter-id}/storage-domains

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

## `get_workloads_vmware_vcenter_esxiserver_datastores` - GET /config/workloads/vmware/vcenters/{vcenter-id}/esxiservers/{esxiserver-id}/datastores

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

## `get_workloads_vmware_vcenter_esxiserver_networks` - GET /config/workloads/vmware/vcenters/{vcenter-id}/esxiservers/{esxiserver-id}/networks

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

## `get_workloads_vmware_vcenter_esxiserver_resource_pools` - GET /config/workloads/vmware/vcenters/{vcenter-id}/esxiservers/{esxiserver-id}/resource-pools

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

## `get_workloads_vmware_vcenter_recovery_topology` - GET /config/workloads/vmware/vcenter-recovery-topologies/{vcenter-id}

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

## `get_workloads_vmware_vcenter_topology` - GET /config/workloads/vmware/vcenter-topologies/{vcenter-id}

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

## `get_workloads_vmware_vcloud_director_organization_organization_vdc_vcenter_esxiserver_datastores` - GET /config/workloads/vmware/vcloud-directors/{vcloud-director-id}/organizations/{organization}/organization-vdcs/{organization-vdc}/vcenters/{vcenter-id}/esxiservers/{esxiserver-id}/datastores

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

## `get_workloads_vmware_vcloud_director_organization_organization_vdc_vcenter_esxiserver_resource_pools` - GET /config/workloads/vmware/vcloud-directors/{vcloud-director-id}/organizations/{organization}/organization-vdcs/{organization-vdc}/vcenters/{vcenter-id}/esxiservers/{esxiserver-id}/resource-pools

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

## `get_workloads_vmware_vcloud_recovery_topology` - GET /config/workloads/vmware/vcloud-recovery-topologies/{vcloud-director-id}

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

## `get_workloads_vmware_vcloud_topology` - GET /config/workloads/vmware/vcloud-topologies/{vcloud-director-id}

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

## `get_workloads_vmware_vcloud_vcenter_topologies_vcloud_director_organization_organization_vdc` - GET /config/workloads/vmware/vcloud-vcenter-topologies/vcloud-directors/{vcloud-director-id}/organizations/{organization}/organization-vdcs/{organization-vdc}

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

## `list_workloads_vmware_query_builder_fields` - GET /config/workloads/vmware/query-builder-fields

```python
nbu.raw.config_workloads.list_workloads_vmware_query_builder_fields()
```

**On the wire**

- `GET /config/workloads/vmware/query-builder-fields` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "getQueryBuilderFields",
      "id": "queryBuilderFields",
      "attributes": {
        "ruleFields": [
          {
            "fieldName": "Annotation",
            "fieldType": "LIST",
            "supportedOperators": [
              {
                "operatorName": "ne",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": false
              },
              {
                "operatorName": "startswith",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": false
              },
              {
                "operatorName": "in",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": true
              },
              "... 7 more"
            ],
            "odataFilterFieldName": "annotation"
          },
          {
            "fieldName": "AssetGroup",
            "fieldType": "LIST",
            "supportedOperators": [
              {
                "operatorName": "eq",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": false
              }
            ],
            "odataFilterFieldName": "assetGroup"
          },
          {
            "fieldName": "Cluster",
            "fieldType": "LIST",
            "supportedOperators": [
              {
                "operatorName": "ne",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": false
              },
              {
                "operatorName": "startswith",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": false
              },
              {
                "operatorName": "in",
                "leftValueAllowed": true,
                "rightValueAllowed": true,
                "multipleValueAllowed": true
              },
              "... 7 more"
            ],
            "odataFilterFieldName": "cluster"
          },
          "... 48 more"
        ]
      }
    }
  }
  ```

  </details>
