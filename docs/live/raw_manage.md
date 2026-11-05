# `nbu.raw.manage`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_alert` - GET /manage/alerts/{alertId}

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

**On the wire**

- `GET /manage/alerts` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>

## `get_notification_category` - GET /manage/notification-categories/{categoryId}

```python
nbu.raw.manage.get_notification_category('1')
```

**On the wire**

- `GET /manage/notification-categories` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "notificationCategory",
        "id": "1",
        "attributes": {
          "category": "JOB",
          "categoryExcluded": false,
          "excludedStatusCodes": "",
          "createdDateTime": "2022-03-17T04:53:08.392Z",
          "lastUpdatedDateTime": "2022-03-17T04:53:08.392Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/manage/notification-categories/1"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 1,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      }
    }
  }
  ```

  </details>

- `GET /manage/notification-categories/1` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "notificationCategory",
      "id": "1",
      "attributes": {
        "category": "JOB",
        "categoryExcluded": false,
        "excludedStatusCodes": "",
        "createdDateTime": "2022-03-17T04:53:08.392Z",
        "lastUpdatedDateTime": "2022-03-17T04:53:08.392Z"
      },
      "links": {
        "self": {
          "href": "https://primary-01:1556/netbackup/manage/notification-categories/1"
        }
      }
    }
  }
  ```

  </details>

## `list_alerts` - GET /manage/alerts

```python
nbu.raw.manage.list_alerts()
```

**On the wire**

- `GET /manage/alerts` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/manage/alerts?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>

## `list_notification_categories` - GET /manage/notification-categories

```python
nbu.raw.manage.list_notification_categories()
```

**On the wire**

- `GET /manage/notification-categories` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "notificationCategory",
        "id": "1",
        "attributes": {
          "category": "JOB",
          "categoryExcluded": false,
          "excludedStatusCodes": "",
          "createdDateTime": "2022-03-17T04:53:08.392Z",
          "lastUpdatedDateTime": "2022-03-17T04:53:08.392Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/manage/notification-categories/1"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 1,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/manage/notification-categories?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-id"
      }
    }
  }
  ```

  </details>
