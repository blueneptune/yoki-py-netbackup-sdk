# The server: ping, version, identity

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## Ping the primary

`GET /ping` is the cheapest call there is: it needs no API version and
answers with the server's clock, in milliseconds since 1970.

```python
answer = record.result(nbu.server.ping())
assert answer
```

**On the wire**

- `GET /ping` -> **200** (0.00 s)

  <details><summary>Answer</summary>

  ```json
  1793893917329
  ```

  </details>

**What the SDK gave back**

```json
{
  "answer": 1793893917329
}
```

## Ask the primary who it is

`nbuVersion` is the release ("NetBackup_10.2"), which decides the API
versions the server accepts; `domainType` is how its users sign in.

```python
info = record.result(nbu.server.info())
assert str(info["nbuVersion"]).startswith("NetBackup_")
assert info["serverName"]
```

**On the wire**

- `GET /security/serverinfo` -> **200** (0.20 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverName": "primary-01",
    "masterHostId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
    "nbuVersion": "NetBackup_10.2",
    "cacpivConnectorPort": null,
    "nbuKeySize": 2048,
    "externalCaUsage": 0,
    "cacpivEnabled": 0,
    "ssoEnabled": false,
    "domainType": "unixpwd"
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "serverName": "primary-01",
  "masterHostId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
  "nbuVersion": "NetBackup_10.2",
  "cacpivConnectorPort": null,
  "nbuKeySize": 2048,
  "externalCaUsage": 0,
  "cacpivEnabled": 0,
  "ssoEnabled": false,
  "domainType": "unixpwd"
}
```

## Settle the API version

With `api_version="auto"` (the default) the client offers the newest
version it knows and steps down on a 406 until the server accepts one.
The 406s on the wire below are that negotiation, not errors.

```python
nbu.jobs.sample(1)
record.note(f"The client settled on API version **{nbu.api_version}**.")
assert nbu.api_version
```

The client settled on API version **9.0**.

**On the wire**

- `GET /admin/jobs?sort=-jobId&page%5Boffset%5D=0&page%5Blimit%5D=1` -> **200** (0.06 s)

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
      }
    ],
    "meta": {
      "pagination": {
        "next": "1712",
        "limit": 1
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&page%5Bafter%5D=1712&sort=-jobId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&sort=-jobId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&sort=-jobId"
      }
    }
  }
  ```

  </details>
