# `nbu.raw.eventlog`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `list_messages` - GET /eventlog/messages

```python
nbu.raw.eventlog.list_messages()
```

**On the wire**

- `GET /eventlog/messages` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/eventlog/messages?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/eventlog/messages?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/eventlog/messages?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>

## `list_notifications` - GET /eventlog/notifications

```python
nbu.raw.eventlog.list_notifications()
```

**On the wire**

- `GET /eventlog/notifications` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "notifications",
        "id": "2430",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T06:37:49.079Z",
          "insertionDateTime": "2026-11-05T06:37:49.080Z",
          "displayString": "One or more files and/or directories do not have the required web service user permissions.",
          "notificationType": "Web Server Certificate Health",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Healthchecker",
          "extendedAttributes": {
            "hostName": "primary-01",
            "File Path": "/usr/openv/var/global/vxss/tomcatcreds/user-06/.VRTSat/profile/certstore/trusted/a76c2ae0.0\n/usr/openv/var/global/vxss/tomcatcreds/nbwebservice.bcfks\n/usr/openv/var/global/vxss/tomcatcreds/user-06/.VRTSat/profile/certstore/trusted/a76c2ae0.0\n/usr/openv/var/global/vxss/tomcatcreds/user-06/.VRTSat/profile/certstore/trusted/a76c2ae0.0\n/usr/openv/var/global/vxss/tomcatcreds/user-06/.VRTSat/profile/cer... (3001 characters)"
          },
          "namespace": "eventlog.vrts.nbu.healthcheck.websvcusr.permissions"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202430)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2429",
        "attributes": {
          "version": "1.0",
          "priority": "LOW",
          "severity": "INFO",
          "createdDateTime": "2026-11-05T06:15:54.260Z",
          "insertionDateTime": "2026-11-05T06:15:54.261Z",
          "displayString": "Successfully completed the discovery of server host-05.",
          "notificationType": "DiscoveryEvent",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Discovery",
          "extendedAttributes": {
            "workloadSubType": "VMWARE_VIRTUAL_CENTER_SERVER",
            "discoveryHost": "primary-01",
            "scheduled": "true",
            "serverName": "host-05",
            "attemptCount": "1",
            "discoveryType": "FULL",
            "workloadType": "VMware",
            "status": "SUCCESS"
          },
          "namespace": "eventlog.vrts.nbu.auto-discovery.completed"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202429)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2428",
        "attributes": {
          "version": "1.0",
          "priority": "LOW",
          "severity": "INFO",
          "createdDateTime": "2026-11-05T06:15:50.556Z",
          "insertionDateTime": "2026-11-05T06:15:50.562Z",
          "displayString": "Started the discovery of server host-05.",
          "notificationType": "DiscoveryEvent",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Discovery",
          "extendedAttributes": {
            "workloadSubType": "VMWARE_VIRTUAL_CENTER_SERVER",
            "discoveryHost": "primary-01",
            "scheduled": "true",
            "serverName": "host-05",
            "attemptCount": "1",
            "discoveryType": "FULL",
            "workloadType": "VMware",
            "status": "RUNNING"
          },
          "namespace": "eventlog.vrts.nbu.auto-discovery.started"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202428)"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 3,
        "offset": 0,
        "last": 20,
        "limit": 10,
        "count": 25,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=20&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>
