# `nbu.raw.security`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_anomaly_configurations` - GET /security/anomaly-configurations

```python
nbu.raw.security.get_anomaly_configurations()
```

**On the wire**

- `GET /security/anomaly-configurations` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "anomalyConfig",
        "id": "1",
        "attributes": {
          "anomalyProxyServer": "",
          "sensitivity": 0,
          "purgeDataIntervalInMonths": 12,
          "liveDataGatherFrequencyInMins": 15,
          "disableAnomalyDetection": 0,
          "disableDetectionService": 1,
          "disableAlertService": 1,
          "lastupdatedTime": "2024-01-21T17:44:38.000Z"
        }
      }
    ]
  }
  ```

  </details>

## `get_api_key` - GET /security/api-keys/{apiKeyTag}

```python
nbu.raw.security.get_api_key('A-2XUsd63hA=')
```

**On the wire**

- `GET /security/api-keys` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "apiKeyDetails",
        "id": "A-2XUsd63hA=",
        "attributes": {
          "userName": "user-02",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2022-08-15T17:08:26.421Z",
          "lastModifiedDateTime": "2022-08-15T17:08:26.421Z",
          "expiryDateTime": "2032-08-15T17:08:26.365Z",
          "description": "",
          "issuer": {
            "principalName": "user-03",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/A-2XUsd63hA="
          }
        }
      },
      {
        "type": "apiKeyDetails",
        "id": "AyYxS9RM9vE=",
        "attributes": {
          "userName": "user-01",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2026-11-02T17:54:10.355Z",
          "lastModifiedDateTime": "2026-11-02T17:54:10.355Z",
          "expiryDateTime": "2027-11-02T17:54:10.391Z",
          "description": "blt2",
          "issuer": {
            "principalName": "user-01",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/AyYxS9RM9vE="
          }
        }
      },
      {
        "type": "apiKeyDetails",
        "id": "A4ylPRv5UUc=",
        "attributes": {
          "userName": "user-03",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2026-11-02T15:54:09.863Z",
          "lastModifiedDateTime": "2026-11-02T15:54:09.863Z",
          "expiryDateTime": "2027-11-02T15:54:09.896Z",
          "description": "",
          "issuer": {
            "principalName": "user-03",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/A4ylPRv5UUc="
          }
        }
      },
      "... 1 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 4,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      }
    }
  }
  ```

  </details>

- `GET /security/api-keys/A-2XUsd63hA=` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "apiKeyDetails",
      "id": "A-2XUsd63hA=",
      "attributes": {
        "userName": "user-02",
        "userDomain": "",
        "userDomainType": "unixpwd",
        "createdDateTime": "2022-08-15T17:08:26.421Z",
        "lastModifiedDateTime": "2022-08-15T17:08:26.421Z",
        "expiryDateTime": "2032-08-15T17:08:26.365Z",
        "description": "",
        "issuer": {
          "principalName": "user-03",
          "principalDomain": "",
          "principalDomainType": "unixpwd"
        },
        "samlSessionValidated": false
      },
      "links": {
        "self": {
          "href": "/netbackup/security/api-keys/A-2XUsd63hA="
        }
      }
    }
  }
  ```

  </details>

## `get_auditlog` - GET /security/auditlogs/{auditId}

```python
nbu.raw.security.get_auditlog('3440')
```

**On the wire**

- `GET /security/auditlogs` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3440",
        "attributes": {
          "category": "EVENT_AUDIT",
          "operation": "ACCESS",
          "messageId": 4990,
          "message": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-05",
            "domainName": "primary-01",
            "domainType": "LOCAL_HOST"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:25:56.694Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3440"
          }
        }
      },
      {
        "type": "audit",
        "id": "3439",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1100,
          "message": "User 'user-06' was successfully authenticated with host 'host-13'",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-06"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "host-13"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "0",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup Administration Console",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-06",
            "domainName": "domain-01",
            "domainType": "UNKNOWN"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:25:56.655Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3439"
          }
        }
      },
      {
        "type": "audit",
        "id": "3438",
        "attributes": {
          "category": "EVENT_LOG",
          "operation": "DELETE",
          "messageId": 3730,
          "message": "Automatic cleanup process deleted '4' system events.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "4"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-06",
            "domainName": "domain-01",
            "domainType": "VXAT_PRIVATE"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:20:49.389Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3438"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 12,
        "offset": 0,
        "last": 110,
        "limit": 10,
        "count": 118,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=110&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      }
    }
  }
  ```

  </details>

- `GET /security/auditlogs/3440` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "audit",
      "id": "3440",
      "attributes": {
        "category": "EVENT_AUDIT",
        "operation": "ACCESS",
        "messageId": 4990,
        "message": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]",
        "auditKeyList": [
          {
            "typeId": 1,
            "typeIdDisplayString": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]"
          }
        ],
        "auditRecordAttributeList": [],
        "auditUserIdentity": {
          "userName": "user-05",
          "domainName": "primary-01",
          "domainType": "LOCAL_HOST"
        },
        "reason": "",
        "auditDateTime": "2026-11-05T06:25:56.694Z"
      },
      "links": {
        "self": {
          "href": "https://primary-01:1556/netbackup/security/auditlogs/3440"
        }
      }
    }
  }
  ```

  </details>

## `get_cacert` - GET /security/cacert

```python
nbu.raw.security.get_cacert()
```

**On the wire**

- `GET /security/cacert` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "webRootCertificateData": "<masked>",
    "trustVersion": "UFYNKZJ0UEEKqbv",
    "nbcaCertificateData": "<masked>"
  }
  ```

  </details>

## `get_certificate` - GET /security/certificates/{serialNumber}

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

## `get_certificate_authorities_hosts_pending_trust_propagation` - GET /security/certificate-authorities/hosts-pending-trust-propagation

```python
nbu.raw.security.get_certificate_authorities_hosts_pending_trust_propagation()
```

**On the wire**

- `GET /security/certificate-authorities/hosts-pending-trust-propagation` -> **200** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_certificate_authorities_migration_summary` - GET /security/certificate-authorities/migration-summary

```python
nbu.raw.security.get_certificate_authorities_migration_summary()
```

**On the wire**

- `GET /security/certificate-authorities/migration-summary` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "nbcaMigrationSummary",
      "id": "<hex>",
      "attributes": {
        "caMigrationStatus": "NO_MIGRATION",
        "activeCaCert": "<certificate masked>\n"
      },
      "links": {
        "self": {
          "href": "/netbackup/security/certificate-authorities/<hex>"
        }
      }
    }
  }
  ```

  </details>

## `get_certificate_authority` - GET /security/certificate-authorities/{fingerprint}

```python
nbu.raw.security.get_certificate_authority('<hex>')
```

**On the wire**

- `GET /security/certificate-authorities` -> **200** (0.01 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "netbackupCADetails",
        "id": "<hex>",
        "attributes": {
          "nbcaCertDetails": {
            "subjectCN": "nbatd",
            "serialNumber": "<masked>",
            "notBefore": "2022-03-17T03:39:00.000Z",
            "notAfter": "2042-03-12T04:54:00.000Z",
            "subjectName": "O=vx,OU=user-05@primary-01,CN=nbatd",
            "subjectOU": "user-05@primary-01",
            "state": "ACTIVE",
            "keySize": 2048,
            "fingerprint": "<masked>",
            "sha-256Fingerprint": "<masked>"
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/security/certificate-authorities/<hex>"
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
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      }
    }
  }
  ```

  </details>

- `GET /security/certificate-authorities/<hex>` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "netbackupCADetails",
      "id": "<hex>",
      "attributes": {
        "nbcaCertDetails": {
          "subjectCN": "nbatd",
          "serialNumber": "<masked>",
          "notBefore": "2022-03-17T03:39:00.000Z",
          "notAfter": "2042-03-12T04:54:00.000Z",
          "subjectName": "O=vx,OU=user-05@primary-01,CN=nbatd",
          "subjectOU": "user-05@primary-01",
          "state": "ACTIVE",
          "keySize": 2048,
          "fingerprint": "<masked>",
          "sha-256Fingerprint": "<masked>"
        }
      },
      "links": {
        "self": {
          "href": "/netbackup/security/certificate-authorities/<hex>"
        }
      }
    }
  }
  ```

  </details>

## `get_certificates_crl` - GET /security/certificates/crl

```python
nbu.raw.security.get_certificates_crl()
```

**On the wire**

- `GET /security/certificates/crl` -> **200** (0.00 s)

  <details><summary>Answer</summary>

  ```
  0��0��0  	*�H��     0710  Unbatd10U  user-05@primary-011  0	U
  vx  261105063614Z  261112063614Z�00.0U  #0��͔m� ��Wt�X5ض쿳�0  U  2b0  	*�H��     � vT)�W��p��֝p�������'����Ը�c��jKY*���g�  �"� ��;xӼ
  8Ղ��̌Z�9�1~�6Fͼ�\���V�/��+쨍F��g�T��+zs�~�h�B��Z��m����"��-���TH�s��
  U
  �DDo�^s��P�BxW�V��נ  ��u@e|p;��~�g#�17�InC6���W����T䉌�5����$oW�Ҁ��͌�n[�~e����r�Xq�4D>�v0-8ܡ
  ```

  </details>

## `get_certificates_current` - GET /security/certificates/current

```python
nbu.raw.security.get_certificates_current()
```

**On the wire**

- `GET /security/certificates/current` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "certificateList": "<masked>"
  }
  ```

  </details>

## `get_credential_isset` - GET /security/credentials/{credname}/isset

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

## `get_domains_vxat` - GET /security/domains/vxat

```python
nbu.raw.security.get_domains_vxat()
```

**On the wire**

- `GET /security/domains/vxat` -> **200** (0.30 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_domains_vxat_by_domain_name` - GET /security/domains/vxat/{domainName}

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

## `get_external_cacert` - GET /security/external-cacerts/{certificateId}

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

- `GET /security/external-cacerts` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_external_cacerts` - GET /security/external-cacerts

```python
nbu.raw.security.get_external_cacerts()
```

**On the wire**

- `GET /security/external-cacerts` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_identity_provider` - GET /security/identity-providers/{name}

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

- `GET /security/identity-providers` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-enable"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-enable"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-enable"
      }
    }
  }
  ```

  </details>

## `get_key_management_service` - GET /security/key-management-services/{kmsId}

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

- `GET /security/key-management-services` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `get_logindetail` - GET /security/logindetails/{auditId}

```python
nbu.raw.security.get_logindetail('3437')
```

**On the wire**

- `GET /security/logindetails` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3437",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1401,
          "message": "User 'user-01' authenticated successfully",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "primary-01"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "2",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup API",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "",
              "oldValueDisplayString": "",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:08:43.582Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3437"
          }
        }
      },
      {
        "type": "audit",
        "id": "3434",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1410,
          "message": "User 'user-01@primary-01' is logged out.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01@primary-01"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-02T21:20:29.301Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3434"
          }
        }
      },
      {
        "type": "audit",
        "id": "3433",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1401,
          "message": "User 'user-01' authenticated successfully",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "primary-01"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "2",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup API",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "",
              "oldValueDisplayString": "",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-02T17:56:06.165Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3433"
          }
        }
      },
      "... 6 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 9,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      }
    }
  }
  ```

  </details>

- `GET /security/logindetails/3437` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "audit",
      "id": "3437",
      "attributes": {
        "category": "LOGIN",
        "operation": "ACCESS",
        "messageId": 1401,
        "message": "User 'user-01' authenticated successfully",
        "auditKeyList": [
          {
            "typeId": 1,
            "typeIdDisplayString": "user-01"
          },
          {
            "typeId": 1,
            "typeIdDisplayString": "primary-01"
          }
        ],
        "auditRecordAttributeList": [
          {
            "oldValue": "",
            "newValue": "2",
            "oldValueDisplayString": "",
            "newValueDisplayString": "NetBackup API",
            "typeId": 2,
            "attributeName": "Accessed From",
            "attributeId": "__UMI__1102"
          },
          {
            "oldValue": "",
            "newValue": "",
            "oldValueDisplayString": "",
            "newValueDisplayString": "",
            "typeId": 1,
            "attributeName": "Origin Host",
            "attributeId": "__UMI__1103"
          },
          {
            "oldValue": "",
            "newValue": "host-13",
            "oldValueDisplayString": "",
            "newValueDisplayString": "host-13",
            "typeId": 1,
            "attributeName": "Logged in to Host",
            "attributeId": "__UMI__1104"
          },
          "... 2 more"
        ],
        "auditUserIdentity": {
          "userName": "user-01",
          "domainName": "primary-01",
          "domainType": "UNIX_PASSWORD"
        },
        "reason": "",
        "auditDateTime": "2026-11-05T06:08:43.582Z"
      },
      "links": {
        "self": {
          "href": "https://primary-01:1556/netbackup/security/logindetails/3437"
        }
      }
    }
  }
  ```

  </details>

## `get_passphrase_constraint` - GET /security/passphrase-constraints/{workflowType}

```python
nbu.raw.security.get_passphrase_constraint('DR_PKG')
```

**On the wire**

- `GET /security/passphrase-constraints` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "passphraseConstraints",
        "id": "DR_PKG",
        "attributes": {
          "minPassphraseLength": "<masked>",
          "minUpperCaseRequired": 0,
          "minLowerCaseRequired": 0,
          "minDigitsRequired": 0,
          "minSpecialCharactersRequired": 0,
          "regex": "(.{8,1024})",
          "createdDateTime": "2022-03-17T04:53:08.392Z",
          "lastModifiedDateTime": "2022-03-17T04:53:08.392Z"
        },
        "links": {
          "self": {
            "href": "/security/passphrase-constraints/DR_PKG"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /security/passphrase-constraints/DR_PKG` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "passphraseConstraints",
      "id": "DR_PKG",
      "attributes": {
        "minPassphraseLength": "<masked>",
        "minUpperCaseRequired": 0,
        "minLowerCaseRequired": 0,
        "minDigitsRequired": 0,
        "minSpecialCharactersRequired": 0,
        "regex": "(.{8,1024})",
        "createdDateTime": "2022-03-17T04:53:08.392Z",
        "lastModifiedDateTime": "2022-03-17T04:53:08.392Z"
      },
      "links": {
        "self": {
          "href": "/security/passphrase-constraints/DR_PKG"
        }
      }
    }
  }
  ```

  </details>

## `get_passphrase_constraints` - GET /security/passphrase-constraints

```python
nbu.raw.security.get_passphrase_constraints()
```

**On the wire**

- `GET /security/passphrase-constraints` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "passphraseConstraints",
        "id": "DR_PKG",
        "attributes": {
          "minPassphraseLength": "<masked>",
          "minUpperCaseRequired": 0,
          "minLowerCaseRequired": 0,
          "minDigitsRequired": 0,
          "minSpecialCharactersRequired": 0,
          "regex": "(.{8,1024})",
          "createdDateTime": "2022-03-17T04:53:08.392Z",
          "lastModifiedDateTime": "2022-03-17T04:53:08.392Z"
        },
        "links": {
          "self": {
            "href": "/security/passphrase-constraints/DR_PKG"
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_ping` - GET /security/ping

```python
nbu.raw.security.get_ping()
```

**On the wire**

- `GET /security/ping` -> **200** (0.00 s)

  <details><summary>Answer</summary>

  ```json
  1793860725044
  ```

  </details>

## `get_properties` - GET /security/properties

```python
nbu.raw.security.get_properties()
```

**On the wire**

- `GET /security/properties` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "allowInsecureBackLevelHost": 1,
    "aliasAutoAdd": 1,
    "blockClientProtection": 0,
    "blockClientImageExpiration": 0,
    "certificateAutoDeployLevel": "<masked>",
    "externalCaUsage": 0,
    "cacpivEnabled": 0,
    "cacpivADLDAPDomainMapping": 1,
    "cacpivCertMappingAttribute": 0,
    "cacpivUserDomainName": "",
    "cacpivOcspUri": "",
    "cacpivMSADCNMappingAttribute": "cn",
    "cacpivMSADUPNMappingAttribute": "userPrincipalName",
    "cacpivLDAPCNMappingAttribute": "cn",
    "cacpivLDAPUPNMappingAttribute": "uid",
    "nbuKeySize": 2048,
    "ssoEnabled": false,
    "dteGlobalMode": "PREFERRED_OFF",
    "externalCertificateIdentityField": "<masked>",
    "performAdminUserCheck": 1,
    "cliAccessSettings": {
      "defaultCLIAccessToOSAdmins": 1,
      "cliSessionMaxExpiryInSec": 86400
    },
    "tlsSessionResumption": {
      "certificateAutoDeployLevelToHandshakeMappings": "<masked>",
      "enableOrDisable": "ENABLE",
      "customOrDefaultHandshakeInterval": "DEFAULT"
    },
    "userJwtTokenValidityInSeconds": "<masked>"
  }
  ```

  </details>

## `get_properties_default` - GET /security/properties/default

```python
nbu.raw.security.get_properties_default()
```

**On the wire**

- `GET /security/properties/default` -> **200** (0.00 s)

  <details><summary>Answer</summary>

  ```json
  {
    "allowInsecureBackLevelHost": 1,
    "aliasAutoAdd": 1,
    "blockClientProtection": 0,
    "blockClientImageExpiration": 0,
    "certificateAutoDeployLevel": "<masked>",
    "externalCaUsage": 0,
    "cacpivEnabled": 0,
    "cacpivADLDAPDomainMapping": 0,
    "cacpivCertMappingAttribute": 0,
    "cacpivUserDomainName": "",
    "cacpivOcspUri": "",
    "cacpivMSADCNMappingAttribute": "cn",
    "cacpivMSADUPNMappingAttribute": "userPrincipalName",
    "cacpivLDAPCNMappingAttribute": "cn",
    "cacpivLDAPUPNMappingAttribute": "uid",
    "nbuKeySize": 2048,
    "ssoEnabled": false,
    "dteGlobalMode": "PREFERRED_OFF",
    "externalCertificateIdentityField": "<masked>",
    "performAdminUserCheck": 1,
    "cliAccessSettings": {
      "defaultCLIAccessToOSAdmins": 1,
      "cliSessionMaxExpiryInSec": 86400
    },
    "tlsSessionResumption": {
      "certificateAutoDeployLevelToHandshakeMappings": "<masked>",
      "enableOrDisable": "ENABLE",
      "customOrDefaultHandshakeInterval": "DEFAULT"
    },
    "userJwtTokenValidityInSeconds": "<masked>"
  }
  ```

  </details>

## `get_securitytoken` - GET /security/securitytokens/{tokenName}

```python
nbu.raw.security.get_securitytoken('INSTALL')
```

**On the wire**

- `GET /security/securitytokens` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "getTokenData",
        "id": "INSTALL",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 10,
          "usedCount": 3,
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/INSTALL"
          }
        }
      },
      {
        "type": "getTokenData",
        "id": "d",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 1,
          "usedCount": 0,
          "hostId": "d33ecc4d-c807-429f-b871-c5fac7766064",
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/d"
          }
        }
      },
      {
        "type": "getTokenData",
        "id": "dd",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 1,
          "usedCount": 0,
          "hostId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/dd"
          }
        }
      },
      "... 4 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 7,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

- `GET /security/securitytokens/INSTALL` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "tokenKey": "<masked>",
    "tokenName": "<masked>",
    "tokenValue": "<masked>",
    "allowedCount": 10,
    "usedCount": 3,
    "hostId": null,
    "tokenActivationTime": "<masked>",
    "tokenExpirationTime": "<masked>",
    "tokenType": "<masked>",
    "tokenState": "<masked>"
  }
  ```

  </details>

## `get_serverinfo` - GET /security/serverinfo

```python
nbu.raw.security.get_serverinfo()
```

**On the wire**

- `GET /security/serverinfo` -> **200** (0.17 s)

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

## `get_servertime` - GET /security/servertime

```python
nbu.raw.security.get_servertime()
```

**On the wire**

- `GET /security/servertime` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "serverTime": 1793860725477,
    "timeZoneName": "Central Standard Time",
    "timeZoneId": "America/Chicago"
  }
  ```

  </details>

## `get_service_principal_config` - GET /security/service-principal-configs/{id}

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

- `GET /security/service-principal-configs` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=servicePrincipalId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=servicePrincipalId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=servicePrincipalId"
      }
    }
  }
  ```

  </details>

## `get_trust_version` - GET /security/trust-versions/{trustVersion}

```python
nbu.raw.security.get_trust_version('UFYNKZJ0UEEKqbv')
```

**On the wire**

- `GET /security/trust-versions` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "trustVersionDetails",
        "id": "UFYNKZJ0UEEKqbv",
        "attributes": {
          "operation": "BOOTSTRAP",
          "createdDateTime": "2022-03-17T04:56:00.532Z"
        },
        "relationships": {
          "netbackupCADetails": {
            "links": {
              "related": {
                "href": "/netbackup/security/certificate-authorities"
              }
            },
            "data": [
              {
                "type": "netbackupCADetails",
                "id": "<hex>"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/security/trust-versions/UFYNKZJ0UEEKqbv"
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
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>

- `GET /security/trust-versions/UFYNKZJ0UEEKqbv` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "trustVersion",
      "id": "UFYNKZJ0UEEKqbv",
      "attributes": {
        "operation": "BOOTSTRAP",
        "createdDateTime": "2022-03-17T04:56:00.532Z"
      },
      "relationships": {
        "netbackupCADetails": {
          "links": {
            "related": {
              "href": "/netbackup/security/certificate-authorities"
            }
          },
          "data": [
            {
              "type": "netbackupCADetails",
              "id": "<hex>"
            }
          ]
        }
      },
      "links": {
        "self": {
          "href": "/netbackup/security/trust-versions/UFYNKZJ0UEEKqbv"
        }
      }
    }
  }
  ```

  </details>

## `list_anomalies` - GET /security/anomalies

```python
nbu.raw.security.list_anomalies()
```

**On the wire**

- `GET /security/anomalies` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "pages": 0,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 0,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/anomalies?page%5Boffset%5D=-100&page%5Blimit%5D=100&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/anomalies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/anomalies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>

## `list_anomalies_exports` - GET /security/anomalies-exports

> **SKIPPED** on this run: not swept: starts work or returns a file

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

## `list_api_keys` - GET /security/api-keys

```python
nbu.raw.security.list_api_keys()
```

**On the wire**

- `GET /security/api-keys` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "apiKeyDetails",
        "id": "A-2XUsd63hA=",
        "attributes": {
          "userName": "user-02",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2022-08-15T17:08:26.421Z",
          "lastModifiedDateTime": "2022-08-15T17:08:26.421Z",
          "expiryDateTime": "2032-08-15T17:08:26.365Z",
          "description": "",
          "issuer": {
            "principalName": "user-03",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/A-2XUsd63hA="
          }
        }
      },
      {
        "type": "apiKeyDetails",
        "id": "AyYxS9RM9vE=",
        "attributes": {
          "userName": "user-01",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2026-11-02T17:54:10.355Z",
          "lastModifiedDateTime": "2026-11-02T17:54:10.355Z",
          "expiryDateTime": "2027-11-02T17:54:10.391Z",
          "description": "blt2",
          "issuer": {
            "principalName": "user-01",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/AyYxS9RM9vE="
          }
        }
      },
      {
        "type": "apiKeyDetails",
        "id": "A4ylPRv5UUc=",
        "attributes": {
          "userName": "user-03",
          "userDomain": "",
          "userDomainType": "unixpwd",
          "createdDateTime": "2026-11-02T15:54:09.863Z",
          "lastModifiedDateTime": "2026-11-02T15:54:09.863Z",
          "expiryDateTime": "2027-11-02T15:54:09.896Z",
          "description": "",
          "issuer": {
            "principalName": "user-03",
            "principalDomain": "",
            "principalDomainType": "unixpwd"
          },
          "samlSessionValidated": false
        },
        "links": {
          "self": {
            "href": "/netbackup/security/api-keys/A4ylPRv5UUc="
          }
        }
      },
      "... 1 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 4,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/api-keys?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-expiryDateTime"
      }
    }
  }
  ```

  </details>

## `list_auditlogs` - GET /security/auditlogs

```python
nbu.raw.security.list_auditlogs()
```

**On the wire**

- `GET /security/auditlogs` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3440",
        "attributes": {
          "category": "EVENT_AUDIT",
          "operation": "ACCESS",
          "messageId": 4990,
          "message": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "[bprd],[-],[Peer:host-13, f151f48b-17c5-4e7e-8a6b-1054db540384, 192.0.2.1:51315],[Destination: 192.0.2.1:13720],[Operation:Login Attempted, UserName:user-06, DomainName:domain-01, Response time (ms):33, Exit code:0]"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-05",
            "domainName": "primary-01",
            "domainType": "LOCAL_HOST"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:25:56.694Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3440"
          }
        }
      },
      {
        "type": "audit",
        "id": "3439",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1100,
          "message": "User 'user-06' was successfully authenticated with host 'host-13'",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-06"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "host-13"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "0",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup Administration Console",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-06",
            "domainName": "domain-01",
            "domainType": "UNKNOWN"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:25:56.655Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3439"
          }
        }
      },
      {
        "type": "audit",
        "id": "3438",
        "attributes": {
          "category": "EVENT_LOG",
          "operation": "DELETE",
          "messageId": 3730,
          "message": "Automatic cleanup process deleted '4' system events.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "4"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-06",
            "domainName": "domain-01",
            "domainType": "VXAT_PRIVATE"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:20:49.389Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3438"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 12,
        "offset": 0,
        "last": 110,
        "limit": 10,
        "count": 118,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=110&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      }
    }
  }
  ```

  </details>

## `list_certificate_authorities` - GET /security/certificate-authorities

```python
nbu.raw.security.list_certificate_authorities()
```

**On the wire**

- `GET /security/certificate-authorities` -> **200** (0.01 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "netbackupCADetails",
        "id": "<hex>",
        "attributes": {
          "nbcaCertDetails": {
            "subjectCN": "nbatd",
            "serialNumber": "<masked>",
            "notBefore": "2022-03-17T03:39:00.000Z",
            "notAfter": "2042-03-12T04:54:00.000Z",
            "subjectName": "O=vx,OU=user-05@primary-01,CN=nbatd",
            "subjectOU": "user-05@primary-01",
            "state": "ACTIVE",
            "keySize": 2048,
            "fingerprint": "<masked>",
            "sha-256Fingerprint": "<masked>"
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/security/certificate-authorities/<hex>"
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
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/certificate-authorities?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=nbcaDetailsId"
      }
    }
  }
  ```

  </details>

## `list_identity_providers` - GET /security/identity-providers

```python
nbu.raw.security.list_identity_providers()
```

**On the wire**

- `GET /security/identity-providers` -> **200** (0.05 s)

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
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=-enable"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-enable"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/identity-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-enable"
      }
    }
  }
  ```

  </details>

## `list_key_management_service_key_details` - GET /security/key-management-services/{kmsId}/key-details

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

## `list_key_management_services` - GET /security/key-management-services

```python
nbu.raw.security.list_key_management_services()
```

**On the wire**

- `GET /security/key-management-services` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/key-management-services?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_logindetails` - GET /security/logindetails

```python
nbu.raw.security.list_logindetails()
```

**On the wire**

- `GET /security/logindetails` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3437",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1401,
          "message": "User 'user-01' authenticated successfully",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "primary-01"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "2",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup API",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "",
              "oldValueDisplayString": "",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T06:08:43.582Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3437"
          }
        }
      },
      {
        "type": "audit",
        "id": "3434",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1410,
          "message": "User 'user-01@primary-01' is logged out.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01@primary-01"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-02T21:20:29.301Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3434"
          }
        }
      },
      {
        "type": "audit",
        "id": "3433",
        "attributes": {
          "category": "LOGIN",
          "operation": "ACCESS",
          "messageId": 1401,
          "message": "User 'user-01' authenticated successfully",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "primary-01"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "2",
              "oldValueDisplayString": "",
              "newValueDisplayString": "NetBackup API",
              "typeId": 2,
              "attributeName": "Accessed From",
              "attributeId": "__UMI__1102"
            },
            {
              "oldValue": "",
              "newValue": "",
              "oldValueDisplayString": "",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "Origin Host",
              "attributeId": "__UMI__1103"
            },
            {
              "oldValue": "",
              "newValue": "host-13",
              "oldValueDisplayString": "",
              "newValueDisplayString": "host-13",
              "typeId": 1,
              "attributeName": "Logged in to Host",
              "attributeId": "__UMI__1104"
            },
            "... 2 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-02T17:56:06.165Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/logindetails/3433"
          }
        }
      },
      "... 6 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 10,
        "count": 9,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/logindetails?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-auditDateTime"
      }
    }
  }
  ```

  </details>

## `list_securitytokens` - GET /security/securitytokens

```python
nbu.raw.security.list_securitytokens()
```

**On the wire**

- `GET /security/securitytokens` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "getTokenData",
        "id": "INSTALL",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 10,
          "usedCount": 3,
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/INSTALL"
          }
        }
      },
      {
        "type": "getTokenData",
        "id": "d",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 1,
          "usedCount": 0,
          "hostId": "d33ecc4d-c807-429f-b871-c5fac7766064",
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/d"
          }
        }
      },
      {
        "type": "getTokenData",
        "id": "dd",
        "attributes": {
          "tokenKey": "<masked>",
          "tokenName": "<masked>",
          "tokenValue": "<masked>",
          "allowedCount": 1,
          "usedCount": 0,
          "hostId": "f151f48b-17c5-4e7e-8a6b-1054db540384",
          "tokenActivationTime": "<masked>",
          "tokenExpirationTime": "<masked>",
          "tokenType": "<masked>",
          "tokenState": "<masked>"
        },
        "links": {
          "self": {
            "href": "/netbackup/security/securitytokens/dd"
          }
        }
      },
      "... 4 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 7,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `list_securitytokens_state_valid` - GET /security/securitytokens/state/valid

```python
nbu.raw.security.list_securitytokens_state_valid()
```

**On the wire**

- `GET /security/securitytokens/state/valid` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "pages": 0,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 0,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens/state/valid?page%5Boffset%5D=-100&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens/state/valid?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/securitytokens/state/valid?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `list_service_principal_configs` - GET /security/service-principal-configs

```python
nbu.raw.security.list_service_principal_configs()
```

**On the wire**

- `GET /security/service-principal-configs` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=servicePrincipalId"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=servicePrincipalId"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/service-principal-configs?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=servicePrincipalId"
      }
    }
  }
  ```

  </details>

## `list_trust_versions` - GET /security/trust-versions

```python
nbu.raw.security.list_trust_versions()
```

**On the wire**

- `GET /security/trust-versions` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "trustVersionDetails",
        "id": "UFYNKZJ0UEEKqbv",
        "attributes": {
          "operation": "BOOTSTRAP",
          "createdDateTime": "2022-03-17T04:56:00.532Z"
        },
        "relationships": {
          "netbackupCADetails": {
            "links": {
              "related": {
                "href": "/netbackup/security/certificate-authorities"
              }
            },
            "data": [
              {
                "type": "netbackupCADetails",
                "id": "<hex>"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/security/trust-versions/UFYNKZJ0UEEKqbv"
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
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/trust-versions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-createdDateTime"
      }
    }
  }
  ```

  </details>
