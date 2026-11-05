# `nbu.raw.admin`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_host_service` - GET /admin/hosts/{hostId}/services/{serviceName}

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

## `get_host_services` - GET /admin/hosts/{hostId}/services

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

## `get_job` - GET /admin/jobs/{jobId}

```python
nbu.raw.admin.get_job('1704')
```

**On the wire**

- `GET /admin/jobs` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1704",
        "attributes": {
          "jobId": 1704,
          "parentJobId": 0,
          "activeProcessId": 790091,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-05T03:56:33.000Z",
          "endTime": "2026-11-05T03:56:34.000Z",
          "activeTryStartTime": "2026-11-05T03:56:33.000Z",
          "lastUpdateTime": "2026-11-05T03:56:37.044Z",
          "childCount": 0,
          "jobPath": "1704",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT1S",
          "activeElapsedTime": "PT1S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1704"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1704/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1704/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793850993000:1704"
          }
        }
      },
      {
        "type": "job",
        "id": "1703",
        "attributes": {
          "jobId": 1703,
          "parentJobId": 0,
          "activeProcessId": 693779,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-04T15:56:32.000Z",
          "endTime": "2026-11-04T15:56:34.000Z",
          "activeTryStartTime": "2026-11-04T15:56:32.000Z",
          "lastUpdateTime": "2026-11-04T15:56:40.752Z",
          "childCount": 0,
          "jobPath": "1703",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT2S",
          "activeElapsedTime": "PT2S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1703"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1703/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1703/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793807792000:1703"
          }
        }
      },
      {
        "type": "job",
        "id": "1702",
        "attributes": {
          "jobId": 1702,
          "parentJobId": 0,
          "activeProcessId": 595274,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-04T03:56:32.000Z",
          "endTime": "2026-11-04T03:56:33.000Z",
          "activeTryStartTime": "2026-11-04T03:56:32.000Z",
          "lastUpdateTime": "2026-11-04T03:56:42.788Z",
          "childCount": 0,
          "jobPath": "1702",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT1S",
          "activeElapsedTime": "PT1S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1702"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1702/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1702/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793764592000:1702"
          }
        }
      },
      "... 4 more"
    ],
    "meta": {
      "pagination": {
        "limit": 10
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&sort=-startTime,jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&sort=-startTime,jobId"
      }
    }
  }
  ```

  </details>

- `GET /admin/jobs/1704` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "job",
      "id": "1704",
      "attributes": {
        "jobId": 1704,
        "parentJobId": 0,
        "activeProcessId": 790091,
        "jobType": "IMAGEDELETE",
        "jobOwner": "user-05",
        "streamNumber": 0,
        "copyNumber": 0,
        "priority": 0,
        "compression": 0,
        "status": 0,
        "state": "DONE",
        "numberOfFiles": 0,
        "estimatedFiles": 0,
        "kilobytesTransferred": 0,
        "kilobytesToTransfer": 0,
        "transferRate": 0,
        "percentComplete": 100,
        "restartable": 0,
        "suspendable": 0,
        "resumable": 0,
        "frozenImage": 0,
        "transportType": "LAN",
        "currentOperation": 0,
        "sessionId": 0,
        "numberOfTapeToEject": 0,
        "submissionType": 0,
        "auditDomainType": 0,
        "startTime": "2026-11-05T03:56:33.000Z",
        "endTime": "2026-11-05T03:56:34.000Z",
        "activeTryStartTime": "2026-11-05T03:56:33.000Z",
        "lastUpdateTime": "2026-11-05T03:56:37.044Z",
        "childCount": 0,
        "jobPath": "1704",
        "try": 1,
        "cancellable": 1,
        "jobQueueReason": -99,
        "kilobytesDataTransferred": 0,
        "elapsedTime": "PT1S",
        "activeElapsedTime": "PT1S",
        "dteMode": "UNKNOWN"
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1704"
        },
        "file-lists": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1704/file-lists"
        },
        "try-logs": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1704/try-logs"
        }
      }
    }
  }
  ```

  </details>

## `get_job_file_lists` - GET /admin/jobs/{jobId}/file-lists

```python
nbu.raw.admin.get_job_file_lists('1704')
```

**On the wire**

- `GET /admin/jobs/1704/file-lists` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "file-lists",
      "id": "1704",
      "attributes": {
        "fileList": []
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1704/file-lists"
        }
      }
    }
  }
  ```

  </details>

## `get_job_try_log` - GET /admin/jobs/{jobId}/try-logs/{attempt}

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.admin.get_job_try_log('1704', '1704-1')
```

**On the wire**

- `GET /admin/jobs/1704/try-logs` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "parsedTryLogResponse",
        "id": "1704-1",
        "attributes": {
          "tryNumber": 1,
          "jobId": 1704,
          "tryStartTimestamp": "2026-11-05T03:56:33.000Z",
          "tryEndTimestamp": "2026-11-05T03:56:34.000Z",
          "tryStatusCode": 0,
          "tryStatusMessage": "the requested operation was successfully completed",
          "tryKbps": 0.0,
          "tryKbWritten": 0.0,
          "tryFilesWritten": 0,
          "trySourceStorageUnit": "",
          "tryDestinationStorageUnit": "",
          "tryMediaServer": "",
          "tryProcessId": 790091,
          "trySessionId": 0,
          "tryLogEntries": [
            {
              "message": "bpdbm (pid=790091) image catalog cleanup",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:33.000Z"
            },
            {
              "message": "bpdbm (pid=790091) deleting images which expire before Wed Nov  4 21:56:32 2026 (1793850992)",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:33.000Z"
            },
            {
              "message": "bpdbm (pid=790091) Cleaning up tables in the relational database",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:34.000Z"
            },
            "... 1 more"
          ]
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1704/try-logs/1"
          },
          "last": {
            "href": "/admin/jobs/1704/try-logs/1"
          },
          "first": {
            "href": "/admin/jobs/1704/try-logs/1"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /admin/jobs/1704/try-logs/1704-1` -> **400** (0.06 s)

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

## `get_job_try_logs` - GET /admin/jobs/{jobId}/try-logs

```python
nbu.raw.admin.get_job_try_logs('1704')
```

**On the wire**

- `GET /admin/jobs/1704/try-logs` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "parsedTryLogResponse",
        "id": "1704-1",
        "attributes": {
          "tryNumber": 1,
          "jobId": 1704,
          "tryStartTimestamp": "2026-11-05T03:56:33.000Z",
          "tryEndTimestamp": "2026-11-05T03:56:34.000Z",
          "tryStatusCode": 0,
          "tryStatusMessage": "the requested operation was successfully completed",
          "tryKbps": 0.0,
          "tryKbWritten": 0.0,
          "tryFilesWritten": 0,
          "trySourceStorageUnit": "",
          "tryDestinationStorageUnit": "",
          "tryMediaServer": "",
          "tryProcessId": 790091,
          "trySessionId": 0,
          "tryLogEntries": [
            {
              "message": "bpdbm (pid=790091) image catalog cleanup",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:33.000Z"
            },
            {
              "message": "bpdbm (pid=790091) deleting images which expire before Wed Nov  4 21:56:32 2026 (1793850992)",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:33.000Z"
            },
            {
              "message": "bpdbm (pid=790091) Cleaning up tables in the relational database",
              "severity": "INFO",
              "timestamp": "2026-11-05T03:56:34.000Z"
            },
            "... 1 more"
          ]
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1704/try-logs/1"
          },
          "last": {
            "href": "/admin/jobs/1704/try-logs/1"
          },
          "first": {
            "href": "/admin/jobs/1704/try-logs/1"
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_restart_job_request` - GET /admin/restart-job-requests/{originalJobId}

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

## `get_user_operation_log_content` - GET /admin/user-operation-log-contents/{fileName}

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

## `list_discovery_workload_status` - GET /admin/discovery/workloads/{workloadType}/status

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

## `list_host_processes` - GET /admin/hosts/{hostId}/processes

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

## `list_job_progress_logs` - GET /admin/jobs/{jobId}/progress-logs

```python
nbu.raw.admin.list_job_progress_logs('1704')
```

**On the wire**

- `GET /admin/jobs/1704/progress-logs` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/admin/jobs/1704/progress-logs?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs/1704/progress-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs/1704/progress-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_jobs` - GET /admin/jobs

```python
nbu.raw.admin.list_jobs()
```

**On the wire**

- `GET /admin/jobs` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1704",
        "attributes": {
          "jobId": 1704,
          "parentJobId": 0,
          "activeProcessId": 790091,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-05T03:56:33.000Z",
          "endTime": "2026-11-05T03:56:34.000Z",
          "activeTryStartTime": "2026-11-05T03:56:33.000Z",
          "lastUpdateTime": "2026-11-05T03:56:37.044Z",
          "childCount": 0,
          "jobPath": "1704",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT1S",
          "activeElapsedTime": "PT1S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1704"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1704/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1704/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793850993000:1704"
          }
        }
      },
      {
        "type": "job",
        "id": "1703",
        "attributes": {
          "jobId": 1703,
          "parentJobId": 0,
          "activeProcessId": 693779,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-04T15:56:32.000Z",
          "endTime": "2026-11-04T15:56:34.000Z",
          "activeTryStartTime": "2026-11-04T15:56:32.000Z",
          "lastUpdateTime": "2026-11-04T15:56:40.752Z",
          "childCount": 0,
          "jobPath": "1703",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT2S",
          "activeElapsedTime": "PT2S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1703"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1703/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1703/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793807792000:1703"
          }
        }
      },
      {
        "type": "job",
        "id": "1702",
        "attributes": {
          "jobId": 1702,
          "parentJobId": 0,
          "activeProcessId": 595274,
          "jobType": "IMAGEDELETE",
          "jobOwner": "user-05",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 0,
          "estimatedFiles": 0,
          "kilobytesTransferred": 0,
          "kilobytesToTransfer": 0,
          "transferRate": 0,
          "percentComplete": 100,
          "restartable": 0,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "currentOperation": 0,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-04T03:56:32.000Z",
          "endTime": "2026-11-04T03:56:33.000Z",
          "activeTryStartTime": "2026-11-04T03:56:32.000Z",
          "lastUpdateTime": "2026-11-04T03:56:42.788Z",
          "childCount": 0,
          "jobPath": "1702",
          "try": 1,
          "cancellable": 1,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT1S",
          "activeElapsedTime": "PT1S",
          "dteMode": "UNKNOWN"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1702"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1702/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1702/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793764592000:1702"
          }
        }
      },
      "... 4 more"
    ],
    "meta": {
      "pagination": {
        "limit": 10
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&sort=-startTime,jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&sort=-startTime,jobId"
      }
    }
  }
  ```

  </details>

## `list_user_operation_logs` - GET /admin/user-operation-logs

```python
nbu.raw.admin.list_user_operation_logs()
```

**On the wire**

- `GET /admin/user-operation-logs` -> **200** (0.15 s)

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
        "href": "https://primary-01:1556/netbackup/admin/user-operation-logs?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/user-operation-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/user-operation-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>
