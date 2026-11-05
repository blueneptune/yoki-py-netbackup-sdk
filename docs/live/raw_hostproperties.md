# `nbu.raw.hostproperties`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_data_classifications` - GET /config/data-classifications

```python
nbu.raw.hostproperties.get_data_classifications()
```

**On the wire**

- `GET /config/data-classifications` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "dataClassifications",
      "id": "primary-01",
      "attributes": {
        "dataClassifications": [
          {
            "id": "0D05DF5AA98511ECB182A67FB754C3FD",
            "name": "Platinum",
            "description": "highest rank",
            "rank": 1
          },
          {
            "id": "0D05E068A98511EC8B4B43463631AF66",
            "name": "Gold",
            "description": "high rank",
            "rank": 2
          },
          {
            "id": "0D05E13AA98511EC8E5CEEA69A5A7CFF",
            "name": "Silver",
            "description": "low rank",
            "rank": 3
          },
          "... 1 more"
        ]
      }
    }
  }
  ```

  </details>

## `get_host_authentication_broker_domains` - GET /config/hosts/{hostId}/authentication-brokers/{brokerName}/domains

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

## `get_host_authentication_brokers` - GET /config/hosts/{hostId}/authentication-brokers

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

## `get_host_host_properties` - GET /config/hosts/{hostId}/host-properties

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

## `get_host_media_settings` - GET /config/hosts/{hostId}/media-settings

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

## `get_login_banner_details` - GET /config/login-banner-details

```python
nbu.raw.hostproperties.get_login_banner_details()
```

**On the wire**

- `GET /config/login-banner-details` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_ndmp_global_credentials` - GET /config/ndmp-global-credentials

> **SKIPPED** on this run: NetBackup answered: 404

```python
nbu.raw.hostproperties.get_ndmp_global_credentials()
```

**On the wire**

- `GET /config/ndmp-global-credentials` -> **404** (0.05 s)

  <details><summary>Answer</summary>

  ```
  <!doctype html><html lang="en"><head><title>HTTP Status 404 – Not Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 – Not Found</h1></body></html>
  ```

  </details>

## `get_retentionlevels` - GET /config/retentionlevels

```python
nbu.raw.hostproperties.get_retentionlevels()
```

**On the wire**

- `GET /config/retentionlevels` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "retentionlevel",
        "id": "0",
        "attributes": {
          "retentionPeriod": {
            "value": 1,
            "unit": "WEEKS"
          },
          "retentionPeriodInSeconds": 604800,
          "retentionPeriodLabel": "1 week"
        },
        "links": {
          "self": {
            "href": "/netbackup/config/retentionlevels/0"
          }
        }
      },
      {
        "type": "retentionlevel",
        "id": "1",
        "attributes": {
          "retentionPeriod": {
            "value": 2,
            "unit": "WEEKS"
          },
          "retentionPeriodInSeconds": 1209600,
          "retentionPeriodLabel": "2 weeks"
        },
        "links": {
          "self": {
            "href": "/netbackup/config/retentionlevels/1"
          }
        }
      },
      {
        "type": "retentionlevel",
        "id": "2",
        "attributes": {
          "retentionPeriod": {
            "value": 3,
            "unit": "WEEKS"
          },
          "retentionPeriodInSeconds": 1814400,
          "retentionPeriodLabel": "3 weeks"
        },
        "links": {
          "self": {
            "href": "/netbackup/config/retentionlevels/2"
          }
        }
      },
      "... 100 more"
    ]
  }
  ```

  </details>

## `get_slp_settings` - GET /config/slp-settings

```python
nbu.raw.hostproperties.get_slp_settings()
```

**On the wire**

- `GET /config/slp-settings` -> **200** (0.56 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slpSettings",
      "id": "primary-01",
      "attributes": {
        "minSizePerDuplicationJob": {
          "value": 8,
          "unit": "GB"
        },
        "maxSizePerDuplicationJob": {
          "value": 100,
          "unit": "GB"
        },
        "maxSizePerAIRReplicationJob": {
          "value": 100,
          "unit": "GB"
        },
        "maxImagesPerSnapshotReplicationJob": 50,
        "minImagesPerAIRImportJob": 1,
        "maxImagesPerAIRImportJob": 250,
        "forceIntervalForSmallJob": {
          "value": 30,
          "unit": "MINUTES"
        },
        "jobSubmissionInterval": {
          "value": 5,
          "unit": "MINUTES"
        },
        "imageProcessingInterval": {
          "value": 5,
          "unit": "MINUTES"
        },
        "cleanupInterval": {
          "value": 24,
          "unit": "HOURS"
        },
        "extendedImageRetryInterval": {
          "value": 2,
          "unit": "HOURS"
        },
        "unusedSlpDefinitionVersionCleanupDelay": {
          "value": 14,
          "unit": "DAYS"
        },
        "tapeResourceMultiplier": 2,
        "diskResourceMultiplier": 2,
        "groupImagesAcrossSlps": true,
        "windowCloseBufferTime": {
          "value": 15,
          "unit": "MINUTES"
        },
        "deferredDuplicationOffset": {
          "value": 4,
          "unit": "HOURS"
        },
        "autoCreateAIRImportSlp": true,
        "retryFailedAIRImportJobsDuration": {
          "value": 0,
          "unit": "HOURS"
        },
        "pendingAIRImportThreshold": {
          "value": 24,
          "unit": "HOURS"
        },
        "notificationEmailAddress": ""
      }
    }
  }
  ```

  </details>

## `get_user_session_settings` - GET /config/user-session-settings

```python
nbu.raw.hostproperties.get_user_session_settings()
```

**On the wire**

- `GET /config/user-session-settings` -> **200** (1.54 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "idleSessionConfig",
      "id": "global",
      "attributes": {
        "idleTimeoutMinutes": 0,
        "accountLockoutDurationMinutes": 15,
        "maxLoginAttempts": 5,
        "maxAllowedActiveLoginsPerUser": 0
      }
    }
  }
  ```

  </details>

## `list_all_hosts` - GET /config/all-hosts

```python
nbu.raw.hostproperties.list_all_hosts()
```

**On the wire**

- `GET /config/all-hosts` -> **200** (0.32 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "hostInfo",
        "id": "4:PolicyClient",
        "attributes": {
          "hostKey": "4",
          "hostName": "host-33",
          "hostMappings": [],
          "hostType": "PolicyClient",
          "isPrimaryServer": false,
          "isMediaServer": false,
          "isPolicyClient": true,
          "installedEebs": []
        }
      },
      {
        "type": "hostInfo",
        "id": "1:EmmHost",
        "attributes": {
          "hostKey": "1",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
          "osType": "UNIX",
          "osNameAndHardware": "redhat_x64",
          "hostName": "primary-01",
          "nbuVersion": "NetBackup_10.2",
          "hostMappings": [
            {
              "hostKey": 1,
              "mappedHostName": "primary-01",
              "origin": "CERTIFICATE_DEPLOYMENT",
              "createdOn": "2022-03-17T04:56:28.000Z",
              "updatedOn": "2022-03-17T04:56:28.000Z",
              "isApproved": true,
              "isConflicting": false,
              "isShared": false,
              "isAddedManually": false
            },
            {
              "hostKey": 1,
              "mappedHostName": "host-03",
              "origin": "COMMUNICATION_DISCOVERY",
              "createdOn": "2024-01-21T20:36:52.000Z",
              "updatedOn": "2024-01-21T20:36:52.000Z",
              "isApproved": true,
              "isConflicting": false,
              "isShared": false,
              "isAddedManually": false
            }
          ],
          "hostType": "EmmHost",
          "isPrimaryServer": true,
          "isMediaServer": true,
          "isPolicyClient": true,
          "installedEebs": []
        }
      },
      {
        "type": "hostInfo",
        "id": "5:PolicyClient",
        "attributes": {
          "hostKey": "5",
          "hostName": "host-05",
          "hostMappings": [],
          "hostType": "PolicyClient",
          "isPrimaryServer": false,
          "isMediaServer": false,
          "isPolicyClient": false,
          "installedEebs": []
        }
      },
      "... 2 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 5,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/config/all-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=hostName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/all-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=hostName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/all-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=hostName"
      }
    }
  }
  ```

  </details>

## `list_paused_clients` - GET /config/paused-clients

```python
nbu.raw.hostproperties.list_paused_clients()
```

**On the wire**

- `GET /config/paused-clients` -> **200** (0.12 s)

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
        "href": "https://primary-01:1556/paf/config/paused-clients?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-clientUniqueIdentifier"
      },
      "self": {
        "href": "https://primary-01:1556/paf/config/paused-clients?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-clientUniqueIdentifier"
      },
      "first": {
        "href": "https://primary-01:1556/paf/config/paused-clients?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-clientUniqueIdentifier"
      }
    }
  }
  ```

  </details>
