# Jobs

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## The newest few jobs, and how many there are, in one request

NetBackup 10.2 (API 9.0) gives no total count; later releases do.

```python
total, jobs = nbu.jobs.sample(3)
record.result({"total": total, "jobs": jobs})
assert all(isinstance(job, Job) for job in jobs)
```

**On the wire**

- `GET /admin/jobs?sort=-jobId&page%5Boffset%5D=0&page%5Blimit%5D=3` -> **200** (0.07 s)

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
            "cursor": "1712"
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
            "cursor": "1711"
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
            "cursor": "1710"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "next": "1710",
        "limit": 3
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=3&page%5Bafter%5D=1710&sort=-jobId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=3&sort=-jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=3&sort=-jobId"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "total": null,
  "jobs": [
    {
      "job_id": 1712,
      "parent_job_id": 0,
      "job_type": "BACKUP",
      "state": "DONE",
      "status": 0,
      "policy_name": "bltlive-11051551-bkp",
      "policy_type": "STANDARD",
      "schedule_name": "bltlive-full",
      "schedule_type": "FULL_BACKUP",
      "client_name": "primary-01",
      "media_server": "primary-01",
      "storage_unit": "storage-unit-02",
      "backup_id": "primary-01_1793893889",
      "start_time": "2026-11-05T15:51:29Z",
      "end_time": "2026-11-05T15:51:39Z",
      "last_update_time": "2026-11-05T15:51:49.095000Z",
      "kilobytes_transferred": 32,
      "kilobytes_data_transferred": 0,
      "number_of_files": 1,
      "percent_complete": 100
    },
    {
      "job_id": 1711,
      "parent_job_id": 0,
      "job_type": "IMAGEDELETE",
      "state": "DONE",
      "status": 0,
      "policy_name": null,
      "policy_type": null,
      "schedule_name": null,
      "schedule_type": null,
      "client_name": "",
      "media_server": null,
      "storage_unit": null,
      "backup_id": null,
      "start_time": "2026-11-05T15:48:09Z",
      "end_time": "2026-11-05T15:48:10Z",
      "last_update_time": "2026-11-05T15:48:18.468000Z",
      "kilobytes_transferred": 0,
      "kilobytes_data_transferred": 0,
      "number_of_files": 0,
      "percent_complete": 100
    },
    {
      "job_id": 1710,
      "parent_job_id": 0,
      "job_type": "BACKUP",
      "state": "DONE",
      "status": 0,
      "policy_name": "bltlive-11051547-bkp",
      "policy_type": "STANDARD",
      "schedule_name": "bltlive-full",
      "schedule_type": "FULL_BACKUP",
      "client_name": "primary-01",
      "media_server": "primary-01",
      "storage_unit": "storage-unit-02",
      "backup_id": "primary-01_1793893677",
      "start_time": "2026-11-05T15:47:57Z",
      "end_time": "2026-11-05T15:48:07Z",
      "last_update_time": "2026-11-05T15:48:08.471000Z",
      "kilobytes_transferred": 32,
      "kilobytes_data_transferred": 0,
      "number_of_files": 1,
      "percent_complete": 100
    }
  ]
}
```

## Walk the whole job list, a page at a time

Every job NetBackup still holds must parse into `Job`: an unexpected
field or format fails here before it fails a collector.

```python
count = 0
states: dict[str, int] = {}
for page in nbu.jobs.iter_pages():
    for job in page:
        count += 1
        states[job.state] = states.get(job.state, 0) + 1
record.result({"jobs": count, "by state": states})
assert count >= 0
```

**On the wire**

- `GET /admin/jobs?sort=jobId&page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1698",
        "attributes": {
          "jobId": 1698,
          "parentJobId": 0,
          "activeProcessId": 197086,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-02T03:56:32.000Z",
          "endTime": "2026-11-02T03:56:33.000Z",
          "activeTryStartTime": "2026-11-02T03:56:32.000Z",
          "lastUpdateTime": "2026-11-02T03:56:33.359Z",
          "childCount": 0,
          "jobPath": "1698",
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
            "href": "/admin/jobs/1698"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1698"
          }
        }
      },
      {
        "type": "job",
        "id": "1699",
        "attributes": {
          "jobId": 1699,
          "parentJobId": 0,
          "activeProcessId": 300923,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-02T15:56:32.000Z",
          "endTime": "2026-11-02T15:56:34.000Z",
          "activeTryStartTime": "2026-11-02T15:56:32.000Z",
          "lastUpdateTime": "2026-11-02T15:56:41.788Z",
          "childCount": 0,
          "jobPath": "1699",
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
            "href": "/admin/jobs/1699"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1699/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1699/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1699"
          }
        }
      },
      {
        "type": "job",
        "id": "1700",
        "attributes": {
          "jobId": 1700,
          "parentJobId": 0,
          "activeProcessId": 399662,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-03T03:56:32.000Z",
          "endTime": "2026-11-03T03:56:34.000Z",
          "activeTryStartTime": "2026-11-03T03:56:32.000Z",
          "lastUpdateTime": "2026-11-03T03:56:37.670Z",
          "childCount": 0,
          "jobPath": "1700",
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
            "href": "/admin/jobs/1700"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1700/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1700/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1700"
          }
        }
      },
      "... 12 more"
    ],
    "meta": {
      "pagination": {
        "limit": 100
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "jobs": 15,
  "by state": {
    "DONE": 15
  }
}
```

## The collector's delta: every job created or changed in the last week

Built as the OData filter `lastUpdateTime ge <time>`.

```python
since = datetime.now(UTC) - timedelta(days=7)
jobs = [job for page in nbu.jobs.iter_pages(updated_after=since) for job in page]
record.result({"since": since, "jobs": len(jobs)})
assert all(job.last_update_time is None or job.last_update_time >= since for job in jobs)
```

**On the wire**

- `GET /admin/jobs?filter=lastUpdateTime+ge+2026-10-29T15%3A51%3A56.894Z&sort=jobId&page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1698",
        "attributes": {
          "jobId": 1698,
          "parentJobId": 0,
          "activeProcessId": 197086,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-02T03:56:32.000Z",
          "endTime": "2026-11-02T03:56:33.000Z",
          "activeTryStartTime": "2026-11-02T03:56:32.000Z",
          "lastUpdateTime": "2026-11-02T03:56:33.359Z",
          "childCount": 0,
          "jobPath": "1698",
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
            "href": "/admin/jobs/1698"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1698"
          }
        }
      },
      {
        "type": "job",
        "id": "1699",
        "attributes": {
          "jobId": 1699,
          "parentJobId": 0,
          "activeProcessId": 300923,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-02T15:56:32.000Z",
          "endTime": "2026-11-02T15:56:34.000Z",
          "activeTryStartTime": "2026-11-02T15:56:32.000Z",
          "lastUpdateTime": "2026-11-02T15:56:41.788Z",
          "childCount": 0,
          "jobPath": "1699",
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
            "href": "/admin/jobs/1699"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1699/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1699/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1699"
          }
        }
      },
      {
        "type": "job",
        "id": "1700",
        "attributes": {
          "jobId": 1700,
          "parentJobId": 0,
          "activeProcessId": 399662,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-03T03:56:32.000Z",
          "endTime": "2026-11-03T03:56:34.000Z",
          "activeTryStartTime": "2026-11-03T03:56:32.000Z",
          "lastUpdateTime": "2026-11-03T03:56:37.670Z",
          "childCount": 0,
          "jobPath": "1700",
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
            "href": "/admin/jobs/1700"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1700/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1700/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1700"
          }
        }
      },
      "... 12 more"
    ],
    "meta": {
      "pagination": {
        "limit": 100
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId&filter=lastUpdateTime%20ge%202026-10-29T15:51:56.894Z"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId&filter=lastUpdateTime%20ge%202026-10-29T15:51:56.894Z"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "since": "2026-10-29T15:51:56.894024+00:00",
  "jobs": 15
}
```

## When the history NetBackup still keeps begins

```python
record.result(nbu.jobs.oldest_start())
```

**On the wire**

- `GET /admin/jobs?sort=startTime&page%5Boffset%5D=0&page%5Blimit%5D=1` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1698",
        "attributes": {
          "jobId": 1698,
          "parentJobId": 0,
          "activeProcessId": 197086,
          "jobType": "IMAGEDELETE",
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
          "startTime": "2026-11-02T03:56:32.000Z",
          "endTime": "2026-11-02T03:56:33.000Z",
          "activeTryStartTime": "2026-11-02T03:56:32.000Z",
          "lastUpdateTime": "2026-11-02T03:56:33.359Z",
          "childCount": 0,
          "jobPath": "1698",
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
            "href": "/admin/jobs/1698"
          },
          "file-lists": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/file-lists"
          },
          "try-logs": {
            "href": "https://primary-01:1556/netbackup/admin/jobs/1698/try-logs"
          }
        },
        "meta": {
          "page": {
            "cursor": "1793591792000:1698"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "next": "1793591792000:1698",
        "limit": 1
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&page%5Bafter%5D=1793591792000:1698&sort=startTime,jobId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&sort=startTime,jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&sort=startTime,jobId"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
"2026-11-02T03:56:32+00:00"
```

## One job by its id

```python
job = record.result(nbu.jobs.get(newest.job_id))
assert job is not None and job.job_id == newest.job_id
```

**On the wire**

- `GET /admin/jobs/1712` -> **200** (0.06 s)

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

**What the SDK gave back**

```json
{
  "job_id": 1712,
  "parent_job_id": 0,
  "job_type": "BACKUP",
  "state": "DONE",
  "status": 0,
  "policy_name": "bltlive-11051551-bkp",
  "policy_type": "STANDARD",
  "schedule_name": "bltlive-full",
  "schedule_type": "FULL_BACKUP",
  "client_name": "primary-01",
  "media_server": "primary-01",
  "storage_unit": "storage-unit-02",
  "backup_id": "primary-01_1793893889",
  "start_time": "2026-11-05T15:51:29Z",
  "end_time": "2026-11-05T15:51:39Z",
  "last_update_time": "2026-11-05T15:51:49.095000Z",
  "kilobytes_transferred": 32,
  "kilobytes_data_transferred": 0,
  "number_of_files": 1,
  "percent_complete": 100
}
```

## A job id NetBackup does not have gives `None`, not an error

```python
assert nbu.jobs.get(2_000_000_000) is None
```

**On the wire**

- `GET /admin/jobs/2000000000` -> **404** (0.05 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## A job's try logs: the detailed status lines the activity monitor shows

```python
record.result(nbu.jobs.try_logs(newest.job_id))
```

**On the wire**

- `GET /admin/jobs/1712/try-logs?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.06 s)

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

**What the SDK gave back**

```json
[
  {
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
    ],
    "id": "1712-1"
  }
]
```

## What a job covered: its file list

```python
record.result(nbu.jobs.file_lists(newest.job_id))
```

**On the wire**

- `GET /admin/jobs/1712/file-lists` -> **200** (0.06 s)

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

**What the SDK gave back**

```json
{
  "fileList": [
    "/usr/openv/netbackup/bin/version"
  ],
  "id": "1712"
}
```
