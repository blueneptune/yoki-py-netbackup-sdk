# `nbu.raw.eventlog`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

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
        "id": "2501",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T15:51:27.764Z",
          "insertionDateTime": "2026-11-05T15:51:29.085Z",
          "displayString": "The policy bltlive-11051551-audit was deleted.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "policyName": "bltlive-11051551-audit",
            "policyType": "Standard",
            "action": "Delete"
          },
          "namespace": "eventlog.vrts.nbu.audit.policy.delete"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202501)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2500",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "INFO",
          "createdDateTime": "2026-11-05T15:51:27.374Z",
          "insertionDateTime": "2026-11-05T15:51:29.081Z",
          "displayString": "The policy bltlive-11051551-audit was created.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "policyGeneration": "2",
            "policyName": "bltlive-11051551-audit",
            "policyType": "Standard",
            "action": "Create",
            "policyPriority": "9"
          },
          "namespace": "eventlog.vrts.nbu.audit.policy.create"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202500)"
          }
        }
      },
      {
        "type": "notifications",
        "id": "2499",
        "attributes": {
          "version": "1.0",
          "priority": "HIGH",
          "severity": "CRITICAL",
          "createdDateTime": "2026-11-05T15:48:13.127Z",
          "insertionDateTime": "2026-11-05T15:48:28.977Z",
          "displayString": "The policy bltlive-11051547-parts was deleted.",
          "notificationType": "Policy",
          "producerName": "primary-01",
          "producerId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "producerType": "NetBackup",
          "producerSubType": "Audit",
          "extendedAttributes": {
            "policyName": "bltlive-11051547-parts",
            "policyType": "Standard",
            "action": "Delete"
          },
          "namespace": "eventlog.vrts.nbu.audit.policy.delete"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/eventlog/notifications?filter=(id%20eq%202499)"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 10,
        "offset": 0,
        "last": 90,
        "limit": 10,
        "count": 92,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/eventlog/notifications?page%5Boffset%5D=90&page%5Blimit%5D=10&sort=-createdDateTime"
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
