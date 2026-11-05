# Jobs

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:16 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

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
        "id": "1704",
        "attributes": {
          "jobId": 1704,
          "parentJobId": 0,
          "activeProcessId": 790091,
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
            "cursor": "1704"
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
            "cursor": "1703"
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
            "cursor": "1702"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "next": "1702",
        "limit": 3
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=3&page%5Bafter%5D=1702&sort=-jobId"
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
      "job_id": 1704,
      "parent_job_id": 0,
      "job_type": "IMAGEDELETE",
      "state": "DONE",
      "status": 0,
      "policy_name": null,
      "policy_type": null,
      "schedule_name": null,
      "schedule_type": null,
      "client_name": null,
      "media_server": null,
      "storage_unit": null,
      "backup_id": null,
      "start_time": "2026-11-05T03:56:33Z",
      "end_time": "2026-11-05T03:56:34Z",
      "last_update_time": "2026-11-05T03:56:37.044000Z",
      "kilobytes_transferred": 0,
      "kilobytes_data_transferred": 0,
      "number_of_files": 0,
      "percent_complete": 100
    },
    {
      "job_id": 1703,
      "parent_job_id": 0,
      "job_type": "IMAGEDELETE",
      "state": "DONE",
      "status": 0,
      "policy_name": null,
      "policy_type": null,
      "schedule_name": null,
      "schedule_type": null,
      "client_name": null,
      "media_server": null,
      "storage_unit": null,
      "backup_id": null,
      "start_time": "2026-11-04T15:56:32Z",
      "end_time": "2026-11-04T15:56:34Z",
      "last_update_time": "2026-11-04T15:56:40.752000Z",
      "kilobytes_transferred": 0,
      "kilobytes_data_transferred": 0,
      "number_of_files": 0,
      "percent_complete": 100
    },
    {
      "job_id": 1702,
      "parent_job_id": 0,
      "job_type": "IMAGEDELETE",
      "state": "DONE",
      "status": 0,
      "policy_name": null,
      "policy_type": null,
      "schedule_name": null,
      "schedule_type": null,
      "client_name": null,
      "media_server": null,
      "storage_unit": null,
      "backup_id": null,
      "start_time": "2026-11-04T03:56:32Z",
      "end_time": "2026-11-04T03:56:33Z",
      "last_update_time": "2026-11-04T03:56:42.788000Z",
      "kilobytes_transferred": 0,
      "kilobytes_data_transferred": 0,
      "number_of_files": 0,
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
      "... 4 more"
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
  "jobs": 7,
  "by state": {
    "DONE": 7
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

- `GET /admin/jobs?filter=lastUpdateTime+ge+2026-10-29T06%3A16%3A05.686Z&sort=jobId&page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.06 s)

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
      "... 4 more"
    ],
    "meta": {
      "pagination": {
        "limit": 100
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId&filter=lastUpdateTime%20ge%202026-10-29T06:16:05.686Z"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=100&sort=jobId&filter=lastUpdateTime%20ge%202026-10-29T06:16:05.686Z"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "since": "2026-10-29T06:16:05.686929+00:00",
  "jobs": 7
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

**What the SDK gave back**

```json
{
  "job_id": 1704,
  "parent_job_id": 0,
  "job_type": "IMAGEDELETE",
  "state": "DONE",
  "status": 0,
  "policy_name": null,
  "policy_type": null,
  "schedule_name": null,
  "schedule_type": null,
  "client_name": null,
  "media_server": null,
  "storage_unit": null,
  "backup_id": null,
  "start_time": "2026-11-05T03:56:33Z",
  "end_time": "2026-11-05T03:56:34Z",
  "last_update_time": "2026-11-05T03:56:37.044000Z",
  "kilobytes_transferred": 0,
  "kilobytes_data_transferred": 0,
  "number_of_files": 0,
  "percent_complete": 100
}
```

## A job id NetBackup does not have gives `None`, not an error

```python
assert nbu.jobs.get(2_000_000_000) is None
```

**On the wire**

- `GET /admin/jobs/2000000000` -> **404** (0.06 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

## A job's try logs: the detailed status lines the activity monitor shows

```python
record.result(nbu.jobs.try_logs(newest.job_id))
```

**On the wire**

- `GET /admin/jobs/1704/try-logs?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.08 s)

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

**What the SDK gave back**

```json
[
  {
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
    ],
    "id": "1704-1"
  }
]
```

## What a job covered: its file list

```python
record.result(nbu.jobs.file_lists(newest.job_id))
```

**On the wire**

- `GET /admin/jobs/1704/file-lists` -> **200** (0.11 s)

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

**What the SDK gave back**

```json
{
  "fileList": [],
  "id": "1704"
}
```
