# `nbu.raw.admin`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_host_service` - GET /admin/hosts/{hostId}/services/{serviceName}

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

## `get_host_services` - GET /admin/hosts/{hostId}/services

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

## `get_job` - GET /admin/jobs/{jobId}

```python
nbu.raw.admin.get_job('1712')
```

**On the wire**

- `GET /admin/jobs` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1712",
        "attributes": {
          "jobId": 1712,
          "parentJobId": 0,
          "activeProcessId": 897548,
          "jobType": "BACKUP",
          "jobSubType": "IMMEDIATE",
          "policyType": "STANDARD",
          "policyName": "bltlive-11051551-bkp",
          "scheduleType": "FULL_BACKUP",
          "scheduleName": "bltlive-full",
          "clientName": "primary-01",
          "jobOwner": "root",
          "jobGroup": "other",
          "backupId": "primary-01_1793893889",
          "destinationStorageUnitName": "storage-unit-02",
          "destinationMediaServerName": "primary-01",
          "dataMovement": "STANDARD",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 1,
          "estimatedFiles": 0,
          "kilobytesTransferred": 32,
          "kilobytesToTransfer": 0,
          "transferRate": 87,
          "percentComplete": 100,
          "restartable": 1,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "dedupRatio": 95.1,
          "currentOperation": -99,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-05T15:51:29.000Z",
          "endTime": "2026-11-05T15:51:39.000Z",
          "activeTryStartTime": "2026-11-05T15:51:29.000Z",
          "lastUpdateTime": "2026-11-05T15:51:49.095Z",
          "childCount": 0,
          "jobPath": "1712",
          "retentionLevel": 0,
          "try": 1,
          "cancellable": 0,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT10S",
          "activeElapsedTime": "PT10S",
          "dteMode": "OFF",
          "dedupSpaceRatio": 17.1,
          "compressionSpaceRatio": 78.0,
          "workloadDisplayName": "primary-01",
          "offHostType": "STANDARD"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1712"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1712/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1712/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893889000:1712"
          }
        }
      },
      {
        "type": "job",
        "id": "1711",
        "attributes": {
          "jobId": 1711,
          "parentJobId": 0,
          "activeProcessId": 896063,
          "jobType": "IMAGEDELETE",
          "clientName": "",
          "jobOwner": "root",
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
          "startTime": "2026-11-05T15:48:09.000Z",
          "endTime": "2026-11-05T15:48:10.000Z",
          "activeTryStartTime": "2026-11-05T15:48:09.000Z",
          "lastUpdateTime": "2026-11-05T15:48:18.468Z",
          "childCount": 0,
          "jobPath": "1711",
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
            "href": "/admin/jobs/1711"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1711/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1711/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893689000:1711"
          }
        }
      },
      {
        "type": "job",
        "id": "1710",
        "attributes": {
          "jobId": 1710,
          "parentJobId": 0,
          "activeProcessId": 895944,
          "jobType": "BACKUP",
          "jobSubType": "IMMEDIATE",
          "policyType": "STANDARD",
          "policyName": "bltlive-11051547-bkp",
          "scheduleType": "FULL_BACKUP",
          "scheduleName": "bltlive-full",
          "clientName": "primary-01",
          "jobOwner": "root",
          "jobGroup": "other",
          "backupId": "primary-01_1793893677",
          "destinationStorageUnitName": "storage-unit-02",
          "destinationMediaServerName": "primary-01",
          "dataMovement": "STANDARD",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 1,
          "estimatedFiles": 0,
          "kilobytesTransferred": 32,
          "kilobytesToTransfer": 0,
          "transferRate": 75,
          "percentComplete": 100,
          "restartable": 1,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "dedupRatio": 95.1,
          "currentOperation": -99,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-05T15:47:57.000Z",
          "endTime": "2026-11-05T15:48:07.000Z",
          "activeTryStartTime": "2026-11-05T15:47:57.000Z",
          "lastUpdateTime": "2026-11-05T15:48:08.471Z",
          "childCount": 0,
          "jobPath": "1710",
          "retentionLevel": 0,
          "try": 1,
          "cancellable": 0,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT10S",
          "activeElapsedTime": "PT10S",
          "dteMode": "OFF",
          "dedupSpaceRatio": 14.6,
          "compressionSpaceRatio": 80.5,
          "workloadDisplayName": "primary-01",
          "offHostType": "STANDARD"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1710"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1710/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1710/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893677000:1710"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": "1793807792000:1703",
        "limit": 10
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&page%5Bafter%5D=1793807792000:1703&sort=-startTime,jobId"
      },
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

- `GET /admin/jobs/1712` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "job",
      "id": "1712",
      "attributes": {
        "jobId": 1712,
        "parentJobId": 0,
        "activeProcessId": 897548,
        "jobType": "BACKUP",
        "jobSubType": "IMMEDIATE",
        "policyType": "STANDARD",
        "policyName": "bltlive-11051551-bkp",
        "scheduleType": "FULL_BACKUP",
        "scheduleName": "bltlive-full",
        "clientName": "primary-01",
        "jobOwner": "root",
        "jobGroup": "other",
        "backupId": "primary-01_1793893889",
        "destinationStorageUnitName": "storage-unit-02",
        "destinationMediaServerName": "primary-01",
        "dataMovement": "STANDARD",
        "streamNumber": 0,
        "copyNumber": 0,
        "priority": 0,
        "compression": 0,
        "status": 0,
        "state": "DONE",
        "numberOfFiles": 1,
        "estimatedFiles": 0,
        "kilobytesTransferred": 32,
        "kilobytesToTransfer": 0,
        "transferRate": 87,
        "percentComplete": 100,
        "restartable": 1,
        "suspendable": 0,
        "resumable": 0,
        "frozenImage": 0,
        "transportType": "LAN",
        "dedupRatio": 95.1,
        "currentOperation": -99,
        "sessionId": 0,
        "numberOfTapeToEject": 0,
        "submissionType": 0,
        "auditDomainType": 0,
        "startTime": "2026-11-05T15:51:29.000Z",
        "endTime": "2026-11-05T15:51:39.000Z",
        "activeTryStartTime": "2026-11-05T15:51:29.000Z",
        "lastUpdateTime": "2026-11-05T15:51:49.095Z",
        "childCount": 0,
        "jobPath": "1712",
        "retentionLevel": 0,
        "try": 1,
        "cancellable": 0,
        "jobQueueReason": -99,
        "kilobytesDataTransferred": 0,
        "elapsedTime": "PT10S",
        "activeElapsedTime": "PT10S",
        "dteMode": "OFF",
        "dedupSpaceRatio": 17.1,
        "compressionSpaceRatio": 78.0,
        "workloadDisplayName": "primary-01",
        "offHostType": "STANDARD"
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1712"
        },
        "file-lists": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/file-lists"
        },
        "try-logs": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/try-logs"
        }
      }
    }
  }
  ```

  </details>

## `get_job_file_lists` - GET /admin/jobs/{jobId}/file-lists

```python
nbu.raw.admin.get_job_file_lists('1712')
```

**On the wire**

- `GET /admin/jobs/1712/file-lists` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "file-lists",
      "id": "1712",
      "attributes": {
        "fileList": [
          "/usr/openv/netbackup/bin/version"
        ]
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1712/file-lists"
        }
      }
    }
  }
  ```

  </details>

## `get_job_try_log` - GET /admin/jobs/{jobId}/try-logs/{attempt}

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.admin.get_job_try_log('1712', '1712-1')
```

**On the wire**

- `GET /admin/jobs/1712/try-logs` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "parsedTryLogResponse",
        "id": "1712-1",
        "attributes": {
          "tryNumber": 1,
          "jobId": 1712,
          "tryStartTimestamp": "2026-11-05T15:51:29.000Z",
          "tryEndTimestamp": "2026-11-05T15:51:39.000Z",
          "tryTransport": "LAN",
          "tryStatusCode": 0,
          "tryStatusMessage": "the requested operation was successfully completed",
          "tryKbps": 87.0,
          "tryKbWritten": 32.0,
          "tryFilesWritten": 1,
          "trySourceStorageUnit": "",
          "tryDestinationStorageUnit": "storage-unit-02",
          "tryMediaServer": "primary-01",
          "tryProcessId": 897548,
          "trySessionId": 0,
          "tryLogEntries": [
            {
              "message": "nbjm (pid=100352) starting backup job (jobid=1712) for client primary-01, policy bltlive-11051551-bkp, schedule bltlive-full",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            {
              "message": "bpbrm (pid=897548) The data-in-transit encryption (DTE) is disabled for the client (primary-01) as the global DTE mode is set to 'Preferred Off' and the client DTE mode is set to 'Automatic'",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            {
              "message": "nbjm (pid=100352) requesting STANDARD_RESOURCE resources from RB for backup job (jobid=1712, request id:{C3ECC01E-D930-11F1-AB6F-A20C30030A81})",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            "... 28 more"
          ]
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1712/try-logs/1"
          },
          "last": {
            "href": "/admin/jobs/1712/try-logs/1"
          },
          "first": {
            "href": "/admin/jobs/1712/try-logs/1"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /admin/jobs/1712/try-logs/1712-1` -> **400** (0.05 s)

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
nbu.raw.admin.get_job_try_logs('1712')
```

**On the wire**

- `GET /admin/jobs/1712/try-logs` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "parsedTryLogResponse",
        "id": "1712-1",
        "attributes": {
          "tryNumber": 1,
          "jobId": 1712,
          "tryStartTimestamp": "2026-11-05T15:51:29.000Z",
          "tryEndTimestamp": "2026-11-05T15:51:39.000Z",
          "tryTransport": "LAN",
          "tryStatusCode": 0,
          "tryStatusMessage": "the requested operation was successfully completed",
          "tryKbps": 87.0,
          "tryKbWritten": 32.0,
          "tryFilesWritten": 1,
          "trySourceStorageUnit": "",
          "tryDestinationStorageUnit": "storage-unit-02",
          "tryMediaServer": "primary-01",
          "tryProcessId": 897548,
          "trySessionId": 0,
          "tryLogEntries": [
            {
              "message": "nbjm (pid=100352) starting backup job (jobid=1712) for client primary-01, policy bltlive-11051551-bkp, schedule bltlive-full",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            {
              "message": "bpbrm (pid=897548) The data-in-transit encryption (DTE) is disabled for the client (primary-01) as the global DTE mode is set to 'Preferred Off' and the client DTE mode is set to 'Automatic'",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            {
              "message": "nbjm (pid=100352) requesting STANDARD_RESOURCE resources from RB for backup job (jobid=1712, request id:{C3ECC01E-D930-11F1-AB6F-A20C30030A81})",
              "severity": "INFO",
              "timestamp": "2026-11-05T15:51:29.000Z"
            },
            "... 28 more"
          ]
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1712/try-logs/1"
          },
          "last": {
            "href": "/admin/jobs/1712/try-logs/1"
          },
          "first": {
            "href": "/admin/jobs/1712/try-logs/1"
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

## `get_user_operation_log_content` - GET /admin/user-operation-log-contents/{fileName}

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

## `list_discovery_workload_status` - GET /admin/discovery/workloads/{workloadType}/status

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

## `list_host_processes` - GET /admin/hosts/{hostId}/processes

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

## `list_job_progress_logs` - GET /admin/jobs/{jobId}/progress-logs

```python
nbu.raw.admin.list_job_progress_logs('1712')
```

**On the wire**

- `GET /admin/jobs/1712/progress-logs` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/admin/jobs/1712/progress-logs?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs/1712/progress-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs/1712/progress-logs?page%5Boffset%5D=0&page%5Blimit%5D=10"
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
        "id": "1713",
        "attributes": {
          "jobId": 1713,
          "parentJobId": 0,
          "activeProcessId": 897675,
          "jobType": "IMAGEDELETE",
          "clientName": "",
          "jobOwner": "root",
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
          "startTime": "2026-11-05T15:51:51.000Z",
          "endTime": "2026-11-05T15:51:52.000Z",
          "activeTryStartTime": "2026-11-05T15:51:51.000Z",
          "lastUpdateTime": "2026-11-05T15:51:59.093Z",
          "childCount": 0,
          "jobPath": "1713",
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
            "href": "/admin/jobs/1713"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1713/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1713/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893911000:1713"
          }
        }
      },
      {
        "type": "job",
        "id": "1712",
        "attributes": {
          "jobId": 1712,
          "parentJobId": 0,
          "activeProcessId": 897548,
          "jobType": "BACKUP",
          "jobSubType": "IMMEDIATE",
          "policyType": "STANDARD",
          "policyName": "bltlive-11051551-bkp",
          "scheduleType": "FULL_BACKUP",
          "scheduleName": "bltlive-full",
          "clientName": "primary-01",
          "jobOwner": "root",
          "jobGroup": "other",
          "backupId": "primary-01_1793893889",
          "destinationStorageUnitName": "storage-unit-02",
          "destinationMediaServerName": "primary-01",
          "dataMovement": "STANDARD",
          "streamNumber": 0,
          "copyNumber": 0,
          "priority": 0,
          "compression": 0,
          "status": 0,
          "state": "DONE",
          "numberOfFiles": 1,
          "estimatedFiles": 0,
          "kilobytesTransferred": 32,
          "kilobytesToTransfer": 0,
          "transferRate": 87,
          "percentComplete": 100,
          "restartable": 1,
          "suspendable": 0,
          "resumable": 0,
          "frozenImage": 0,
          "transportType": "LAN",
          "dedupRatio": 95.1,
          "currentOperation": -99,
          "sessionId": 0,
          "numberOfTapeToEject": 0,
          "submissionType": 0,
          "auditDomainType": 0,
          "startTime": "2026-11-05T15:51:29.000Z",
          "endTime": "2026-11-05T15:51:39.000Z",
          "activeTryStartTime": "2026-11-05T15:51:29.000Z",
          "lastUpdateTime": "2026-11-05T15:51:49.095Z",
          "childCount": 0,
          "jobPath": "1712",
          "retentionLevel": 0,
          "try": 1,
          "cancellable": 0,
          "jobQueueReason": -99,
          "kilobytesDataTransferred": 0,
          "elapsedTime": "PT10S",
          "activeElapsedTime": "PT10S",
          "dteMode": "OFF",
          "dedupSpaceRatio": 17.1,
          "compressionSpaceRatio": 78.0,
          "workloadDisplayName": "primary-01",
          "offHostType": "STANDARD"
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1712"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1712/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1712/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893889000:1712"
          }
        }
      },
      {
        "type": "job",
        "id": "1711",
        "attributes": {
          "jobId": 1711,
          "parentJobId": 0,
          "activeProcessId": 896063,
          "jobType": "IMAGEDELETE",
          "clientName": "",
          "jobOwner": "root",
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
          "startTime": "2026-11-05T15:48:09.000Z",
          "endTime": "2026-11-05T15:48:10.000Z",
          "activeTryStartTime": "2026-11-05T15:48:09.000Z",
          "lastUpdateTime": "2026-11-05T15:48:18.468Z",
          "childCount": 0,
          "jobPath": "1711",
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
            "href": "/admin/jobs/1711"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1711/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1711/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793893689000:1711"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": "1793850993000:1704",
        "limit": 10
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=10&page%5Bafter%5D=1793850993000:1704&sort=-startTime,jobId"
      },
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

- `GET /admin/user-operation-logs` -> **200** (0.17 s)

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
