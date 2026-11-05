# `nbu.raw.globalmanagementservice`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_data_collection_status` - GET /alta-view/data-collection/status

```python
nbu.raw.globalmanagementservice.get_data_collection_status()
```

**On the wire**

- `GET /alta-view/data-collection/status` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "dcState",
      "id": "0",
      "attributes": {
        "state": "DEACTIVATED",
        "connectionState": "DISCONNECTED"
      }
    }
  }
  ```

  </details>

## `get_servers` - GET /alta-view/servers

```python
nbu.raw.globalmanagementservice.get_servers()
```

**On the wire**

- `GET /alta-view/servers` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>
