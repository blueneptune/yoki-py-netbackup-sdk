# The server: ping, version, identity

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## Ping the primary

`GET /ping` is the cheapest call there is: it needs no API version and
answers with the server's clock, in milliseconds since 1970.

```python
answer = record.result(nbu.server.ping())
assert answer
```

**On the wire**

- `GET /ping` -> **200** (0.01 s)

  <details><summary>Answer</summary>

  ```json
  1793861126627
  ```

  </details>

**What the SDK gave back**

```json
{
  "answer": 1793861126627
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

- `GET /security/serverinfo` -> **200** (0.22 s)

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
      }
    ],
    "meta": {
      "pagination": {
        "next": "1704",
        "limit": 1
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/admin/jobs?page%5Blimit%5D=1&page%5Bafter%5D=1704&sort=-jobId"
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
