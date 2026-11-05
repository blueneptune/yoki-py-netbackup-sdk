# `nbu.raw.eventlog`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

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

- `GET /eventlog/notifications` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "notifications",
        "id": "2465",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T06:45:23.747Z",
          "insertionDateTime": "2026-11-05T06:45:29.397Z",
          "displayString": "The policy bltlive-11050645-parts was deleted.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "policyName": "bltlive-11050645-parts",
            "policyType": "Standard",
            "action": "Delete"
          },
          "namespace": "eventlog.vrts.nbu.audit.policy.delete"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202465)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2464",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T06:45:23.543Z",
          "insertionDateTime": "2026-11-05T06:45:29.394Z",
          "displayString": "The client bltlive-client.example.com was removed from the policy bltlive-11050645-parts.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "clientNames": "bltlive-client.example.com",
            "policyName": "bltlive-11050645-parts",
            "action": "Update"
          },
          "namespace": "eventlog.vrts.nbu.audit.policy.client.delete"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202464)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2463",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T06:45:23.432Z",
          "insertionDateTime": "2026-11-05T06:45:29.391Z",
          "displayString": "The schedule bltlive-full was removed from the policy bltlive-11050645-parts.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "policyName": "bltlive-11050645-parts",
            "scheduleNames": "bltlive-full",
            "action": "Update"
          },
          "namespace": "eventlog.vrts.nbu.audit.schedule.delete"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202463)"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 6,
        "offset": 0,
        "last": 50,
        "limit": 10,
        "count": 60,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=50&page%5Blimit%5D=10&sort=-createdDateTime"
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
