# `nbu.raw.licensing`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_capacity` - GET /licensing/capacity

> **SKIPPED** on this run: NetBackup answered: 404 (error 4602) - The usage report data is not available.

```python
nbu.raw.licensing.list_capacity()
```

**On the wire**

- `GET /licensing/capacity` -> **404** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 4602,
    "errorMessage": "The usage report data is not available.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_capacity_client_details` - GET /licensing/capacity/client-details

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.licensing.list_capacity_client_details()
```

**On the wire**

- `GET /licensing/capacity/client-details` -> **400** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8961,
    "errorMessage": "An invalid API request is encountered.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>
