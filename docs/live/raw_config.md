# `nbu.raw.config`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_bulk_server_group_request` - GET /config/bulk-server-group-requests/{requestId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_cdp_gateway` - GET /config/cdp-gateway/{hostId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/cdp-gateway` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/config/cdp-gateway?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/cdp-gateway?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `get_credential` - GET /config/credentials/{credentialId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/credentials` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/config/credentials?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=CreatedDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/credentials?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=CreatedDateTime"
      }
    }
  }
  ```

  </details>

## `get_drive_name_rule_fields` - GET /config/drive-name-rule-fields

> **SKIPPED** on this run: NetBackup answered: 500 (error 130) - system error occurred

```python
nbu.raw.config.get_drive_name_rule_fields()
```

**On the wire**

- `GET /config/drive-name-rule-fields` -> **500** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 130,
    "errorMessage": "system error occurred",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `get_drive_name_rules` - GET /config/drive-name-rules

> **SKIPPED** on this run: NetBackup answered: 500 (error 130) - system error occurred

```python
nbu.raw.config.get_drive_name_rules()
```

**On the wire**

- `GET /config/drive-name-rules` -> **500** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 130,
    "errorMessage": "system error occurred",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `get_ecms_agent` - GET /config/ecms-agents/{ecmsAgentId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/ecms-agents` -> **200** (0.19 s)

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
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=credentialName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=credentialName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=credentialName"
      }
    }
  }
  ```

  </details>

## `get_ecms_provider` - GET /config/ecms-providers/{configName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/ecms-providers` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=ConfigName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=ConfigName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=ConfigName"
      }
    }
  }
  ```

  </details>

## `get_host` - GET /config/hosts/{hostId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/hosts` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hosts": [
      {
        "hostKey": null,
        "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
        "osType": "UNIX",
        "hostName": "primary-01",
        "nbuVersion": "NetBackup_10.2",
        "masterServer": "primary-01",
        "installedPackages": "warning: Could not load key gpg_pubkey,VRTSnbpck_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0,VRTSpddes_18.0.0.0,VRTSpddeu_18.0.0.0,VRTSpddea_18.0.0.0,VRTSpddei_4.0,VRTSnbcfg_10.2.0.0,VRTSpostgresql_14.7.4.0,VRTSnetbp_10.2.0.0,VRTSnbmqbrkr_10.2.0.0,VRTSnbweb_10.2.0.0,VRTSnbslibs_10.2.0.0",
        "hwDescription": "AuthenticAMD AMD EPYC 7551P 32-Core Processor, 16 CPUs",
        "vxUpdatePlatform": "redhat_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "9",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "user-04",
        "createdDateTime": 1647492988000,
        "lastUpdatedDateTime": 1793687304000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "PRIMARY_SERVER",
        "nbuReleaseVersion": "10.2",
        "createdTimeUTC": "2022-03-17T04:56:28.000Z",
        "lastUpdateTimeUTC": "2026-11-03T06:28:24.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "primary-01",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1647492988000,
            "updatedOn": 1647492988000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "host-03",
            "isApproved": true,
            "isConflicting": false,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1705869412000,
            "updatedOn": 1705869412000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          }
        ]
      },
      {
        "hostKey": null,
        "osVersion": "Linux Mint 21.3 (5.15.0-140-generic)",
        "osType": "UNIX",
        "hostName": "host-01",
        "nbuVersion": "NetBackup_10.5",
        "masterServer": "primary-01",
        "installedPackages": "VRTSpddea_20.5,VRTSnbclt_10.5.0.0,VRTSnbclibs_10.5.0.0,VRTSpbx_1.19.37.0,VRTSnbcfg_10.5.0.0,VRTSnbpck_10.5.0.0,VRTSnbjre_10.5.0.0,VRTSnbjava_10.5.0.0",
        "hwDescription": "GenuineIntel 11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz, 6 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "d33ecc4d-c807-429f-b871-c5fac7766064",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "",
        "createdDateTime": 1705868746000,
        "lastUpdatedDateTime": 1747677600000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "PRIMARY_SERVER",
        "nbuReleaseVersion": "10.5",
        "createdTimeUTC": "2024-01-21T20:25:46.000Z",
        "lastUpdateTimeUTC": "2025-05-19T18:00:00.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-01",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705868746000,
            "updatedOn": 1705868746000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "host-04",
            "isApproved": true,
            "isConflicting": false,
            "origin": "USER_ADDED",
            "isShared": false,
            "createdOn": 1705871748000,
            "updatedOn": 1705871748000,
            "isAddedManually": true,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "primary-01",
            "isApproved": false,
            "isConflicting": true,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1708898758000,
            "updatedOn": 1708898758000,
            "isAddedManually": false,
            "approved": false,
            "conflicting": true,
            "shared": false
          }
        ]
      },
      {
        "hostKey": null,
        "osVersion": "Linux Mint 21.3 (5.15.0-91-generic)",
        "osType": "UNIX",
        "hostName": "host-02",
        "nbuVersion": "NetBackup_10.2",
        "masterServer": "primary-01",
        "installedPackages": "VRTSpddea_18.0,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbcfg_10.2.0.0,VRTSnbpck_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0",
        "hwDescription": "GenuineIntel Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 4 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "815af09c-a09e-4003-94e3-3a2e7bf27446",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "",
        "createdDateTime": 1705981153000,
        "lastUpdatedDateTime": 1706151003000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "CLIENT",
        "nbuReleaseVersion": "10.2",
        "createdTimeUTC": "2024-01-23T03:39:13.000Z",
        "lastUpdateTimeUTC": "2024-01-25T02:50:03.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-02",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705981153000,
            "updatedOn": 1705981153000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          }
        ]
      }
    ]
  }
  ```

  </details>

## `get_host_configuration` - GET /config/hosts/{hostId}/configurations/{configurationName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_host_configurations` - GET /config/hosts/{hostId}/configurations

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_host_hostmappings` - GET /config/hosts/{hostId}/hostmappings

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_host_server_lists` - GET /config/hosts/{hostId}/server-lists

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_hosts_hostmappings` - GET /config/hosts/hostmappings

```python
nbu.raw.config.get_hosts_hostmappings()
```

**On the wire**

- `GET /config/hosts/hostmappings` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hosts": [
      {
        "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384",
        "hostName": "primary-01",
        "masterServer": "primary-01",
        "installedEEBs": "",
        "installedPackages": "warning: Could not load key gpg_pubkey,VRTSnbpck_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0,VRTSpddes_18.0.0.0,VRTSpddeu_18.0.0.0,VRTSpddea_18.0.0.0,VRTSpddei_4.0,VRTSnbcfg_10.2.0.0,VRTSpostgresql_14.7.4.0,VRTSnetbp_10.2.0.0,VRTSnbmqbrkr_10.2.0.0,VRTSnbweb_10.2.0.0,VRTSnbslibs_10.2.0.0",
        "osType": "UNIX",
        "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
        "osReleaseVersion": "9",
        "cpuArchitecture": "x86_64",
        "hwDescription": "AuthenticAMD AMD EPYC 7551P 32-Core Processor, 16 CPUs",
        "vxUpdatePlatform": "redhat_x64",
        "nbuVersion": "NetBackup_10.2",
        "comment": "",
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "nbuReleaseVersion": "10.2",
        "serviceUser": "user-04",
        "nbuHostType": "PRIMARY_SERVER",
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "dteClientMode": "AUTOMATIC",
        "isSecureEnabled": true,
        "autoReissue": false,
        "autoReissueDuration": 0,
        "createdDateTime": 1647492988000,
        "lastUpdatedDateTime": 1793687304000,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-03",
            "isApproved": true,
            "isConflicting": false,
            "isAddedManually": false,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1705869412000,
            "updatedOn": 1705869412000
          },
          {
            "mappedHostName": "primary-01",
            "isApproved": true,
            "isConflicting": false,
            "isAddedManually": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1647492988000,
            "updatedOn": 1647492988000
          }
        ]
      },
      {
        "uuid": "d33ecc4d-c807-429f-b871-c5fac7766064",
        "hostName": "host-01",
        "masterServer": "primary-01",
        "installedEEBs": "",
        "installedPackages": "VRTSpddea_20.5,VRTSnbclt_10.5.0.0,VRTSnbclibs_10.5.0.0,VRTSpbx_1.19.37.0,VRTSnbcfg_10.5.0.0,VRTSnbpck_10.5.0.0,VRTSnbjre_10.5.0.0,VRTSnbjava_10.5.0.0",
        "osType": "UNIX",
        "osVersion": "Linux Mint 21.3 (5.15.0-140-generic)",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "hwDescription": "GenuineIntel 11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz, 6 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "nbuVersion": "NetBackup_10.5",
        "comment": "",
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "nbuReleaseVersion": "10.5",
        "serviceUser": "",
        "nbuHostType": "PRIMARY_SERVER",
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "dteClientMode": "AUTOMATIC",
        "isSecureEnabled": true,
        "autoReissue": false,
        "autoReissueDuration": 0,
        "createdDateTime": 1705868746000,
        "lastUpdatedDateTime": 1747677600000,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "primary-01",
            "isApproved": false,
            "isConflicting": true,
            "isAddedManually": false,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1708898758000,
            "updatedOn": 1708898758000
          },
          {
            "mappedHostName": "host-01",
            "isApproved": true,
            "isConflicting": false,
            "isAddedManually": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705868746000,
            "updatedOn": 1705868746000
          },
          {
            "mappedHostName": "host-04",
            "isApproved": true,
            "isConflicting": false,
            "isAddedManually": true,
            "origin": "USER_ADDED",
            "isShared": false,
            "createdOn": 1705871748000,
            "updatedOn": 1705871748000
          }
        ]
      },
      {
        "uuid": "815af09c-a09e-4003-94e3-3a2e7bf27446",
        "hostName": "host-02",
        "masterServer": "primary-01",
        "installedEEBs": "",
        "installedPackages": "VRTSpddea_18.0,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbcfg_10.2.0.0,VRTSnbpck_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0",
        "osType": "UNIX",
        "osVersion": "Linux Mint 21.3 (5.15.0-91-generic)",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "hwDescription": "GenuineIntel Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 4 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "nbuVersion": "NetBackup_10.2",
        "comment": "",
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "nbuReleaseVersion": "10.2",
        "serviceUser": "",
        "nbuHostType": "CLIENT",
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "dteClientMode": "AUTOMATIC",
        "isSecureEnabled": true,
        "autoReissue": false,
        "autoReissueDuration": 0,
        "createdDateTime": 1705981153000,
        "lastUpdatedDateTime": 1706151003000,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-02",
            "isApproved": true,
            "isConflicting": false,
            "isAddedManually": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705981153000,
            "updatedOn": 1705981153000
          }
        ]
      }
    ]
  }
  ```

  </details>

## `get_hosts_pending_renewal` - GET /config/hosts-pending-renewal

```python
nbu.raw.config.get_hosts_pending_renewal()
```

**On the wire**

- `GET /config/hosts-pending-renewal` -> **200** (0.22 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_ir_setting` - GET /config/ir-settings/{workloadType}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_iscsi_setting` - GET /config/iscsi-settings/{workloadType}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_media_server` - GET /config/media-servers/{hostName}

```python
nbu.raw.config.get_media_server('primary-01')
```

**On the wire**

- `GET /config/media-servers` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "mediaServer",
        "id": "primary-01",
        "attributes": {
          "hostName": "primary-01",
          "isMachineUp": true,
          "osType": "Linux",
          "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
          "osReleaseVersion": "9",
          "nbuVersion": "10.2",
          "supportedStoragesInfo": [
            {
              "storageProviderId": "NetBackup",
              "storageCategory": "MSDP"
            },
            {
              "storageProviderId": "NetBackup",
              "storageCategory": "ADVANCED_DISK"
            },
            {
              "storageProviderId": "scalitywan",
              "storageCategory": "CLOUD"
            },
            "... 117 more"
          ],
          "dteMode": "ON",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
        },
        "links": {
          "self": {
            "href": "/netbackup/config/media-servers/primary-01"
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
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /config/media-servers/primary-01` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "mediaServer",
      "id": "primary-01",
      "attributes": {
        "hostName": "primary-01",
        "isMachineUp": true,
        "osType": "Linux",
        "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
        "osReleaseVersion": "9",
        "nbuVersion": "10.2",
        "supportedStoragesInfo": [
          {
            "storageProviderId": "NetBackup",
            "storageCategory": "MSDP"
          },
          {
            "storageProviderId": "NetBackup",
            "storageCategory": "ADVANCED_DISK"
          },
          {
            "storageProviderId": "scalitywan",
            "storageCategory": "CLOUD"
          },
          "... 117 more"
        ],
        "dteMode": "ON",
        "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
      },
      "links": {
        "self": {
          "href": "/netbackup/config/media-servers/primary-01"
        }
      }
    }
  }
  ```

  </details>

## `get_policies_bulk_policy_request` - GET /config/policies/bulk-policy-requests/{requestId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_policy` - GET /config/policies/{policyName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_proxy_server` - GET /config/proxy-servers/{proxyId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_remote_master_server_cacert`

GET /config/remote-master-server-cacerts/{remoteMasterServer}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_resource_limit` - GET /config/resource-limits/{workloadType}

```python
nbu.raw.config.get_resource_limit('vmware')
```

**On the wire**

- `GET /config/resource-limits` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "resource-limits",
        "id": "vmware",
        "attributes": {
          "resources": [
            {
              "resourceType": "vCenter",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "snapshot",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Cluster",
              "resourceName": "",
              "resourceLimit": 0
            },
            "... 8 more"
          ],
          "workloadType": "VMware"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/vmware"
          }
        }
      },
      {
        "type": "resource-limits",
        "id": "asset-18",
        "attributes": {
          "resources": [
            {
              "resourceType": "Backup Jobs per asset-18 Cluster",
              "resourceName": "",
              "resourceLimit": 1
            },
            {
              "resourceType": "Backup from Snapshot Jobs per asset-18 Cluster",
              "resourceName": "",
              "resourceLimit": 4
            }
          ],
          "workloadType": "asset-18"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/asset-18"
          }
        }
      },
      {
        "type": "resource-limits",
        "id": "hyperv",
        "attributes": {
          "resources": [
            {
              "resourceType": "Active Snapshots Per Server",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Active Snapshots Per Cluster",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Snapshot Operations Per Server",
              "resourceName": "",
              "resourceLimit": 0
            },
            "... 3 more"
          ],
          "workloadType": "Hyper-V"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/hyperv"
          }
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

- `GET /config/resource-limits/vmware` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "resource-limits",
      "id": "vmware",
      "attributes": {
        "resources": [
          {
            "resourceType": "vCenter",
            "resourceName": "",
            "resourceLimit": 0
          },
          {
            "resourceType": "snapshot",
            "resourceName": "",
            "resourceLimit": 0
          },
          {
            "resourceType": "Cluster",
            "resourceName": "",
            "resourceLimit": 0
          },
          "... 8 more"
        ],
        "workloadType": "VMware"
      },
      "links": {
        "self": {
          "href": "/config/resource-limits/vmware"
        }
      }
    }
  }
  ```

  </details>

## `get_resource_limit_template` - GET /config/resource-limit-templates/{workloadType}

```python
nbu.raw.config.get_resource_limit_template('cdp')
```

**On the wire**

- `GET /config/resource-limit-templates` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "resource-limit-templates",
        "id": "cdp",
        "attributes": {
          "resources": [
            {
              "resourceType": "CDP-Backup",
              "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
            },
            {
              "resourceType": "CDP-Backup",
              "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
            }
          ],
          "workloadType": "CDP"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/cdp"
          }
        }
      },
      {
        "type": "resource-limit-templates",
        "id": "cloud",
        "attributes": {
          "resources": [
            {
              "resourceType": "Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous jobs per Snapshot Manager."
            },
            {
              "resourceType": "Snapshot Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous snapshots jobs per Snapshot Manager."
            },
            {
              "resourceType": "Snapshot Diff Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous snapshot diff per Snapshot Manager."
            },
            "... 9 more"
          ],
          "workloadType": "Cloud"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/cloud"
          }
        }
      },
      {
        "type": "resource-limit-templates",
        "id": "hyperv",
        "attributes": {
          "resources": [
            {
              "resourceType": "Active Snapshots Per Server",
              "resourceDescription": "Controls the maximum number of active backup jobs per Hyper-V server. This resource limit applies to a standalone Hyper-V server as well as every Hyper-V server in a cluster.\n\nThe typical setting for this resource type is 2.",
              "backupMethod": "VSS"
            },
            {
              "resourceType": "Active Snapshots Per Cluster",
              "resourceDescription": "Controls the maximum number of active backup jobs per Hyper-V cluster.\n\nThe typical setting for this resource type is 4.",
              "backupMethod": "VSS"
            },
            {
              "resourceType": "Snapshot Operations Per Server",
              "resourceDescription": "Controls the maximum number of simultaneous VSS operations such as create snapshot and delete snapshot on a Hyper-V server or a Hyper-V server in a cluster. This resource limit applies only during the snapshot creation and snapshot deletion phase of a backup. It does not control the number of simultaneous backup jobs.\n\nThe typical setting for this resource type is 1.",
              "backupMethod": "VSS"
            },
            "... 3 more"
          ],
          "workloadType": "Hyper-V"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/hyperv"
          }
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

- `GET /config/resource-limit-templates/cdp` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "resource-limit-templates",
      "id": "cdp",
      "attributes": {
        "resources": [
          {
            "resourceType": "CDP-Backup",
            "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
          },
          {
            "resourceType": "CDP-Backup",
            "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
          }
        ],
        "workloadType": "CDP"
      },
      "links": {
        "self": {
          "href": "/config/resource-limit-templates/cdp"
        }
      }
    }
  }
  ```

  </details>

## `get_resource_limit_templates` - GET /config/resource-limit-templates

```python
nbu.raw.config.get_resource_limit_templates()
```

**On the wire**

- `GET /config/resource-limit-templates` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "resource-limit-templates",
        "id": "cdp",
        "attributes": {
          "resources": [
            {
              "resourceType": "CDP-Backup",
              "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
            },
            {
              "resourceType": "CDP-Backup",
              "resourceDescription": "Controls the maximum number of simultaneous backup jobs on CDP gateway."
            }
          ],
          "workloadType": "CDP"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/cdp"
          }
        }
      },
      {
        "type": "resource-limit-templates",
        "id": "cloud",
        "attributes": {
          "resources": [
            {
              "resourceType": "Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous jobs per Snapshot Manager."
            },
            {
              "resourceType": "Snapshot Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous snapshots jobs per Snapshot Manager."
            },
            {
              "resourceType": "Snapshot Diff Jobs per CloudPoint Server",
              "resourceDescription": "Controls the maximum number of simultaneous snapshot diff per Snapshot Manager."
            },
            "... 9 more"
          ],
          "workloadType": "Cloud"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/cloud"
          }
        }
      },
      {
        "type": "resource-limit-templates",
        "id": "hyperv",
        "attributes": {
          "resources": [
            {
              "resourceType": "Active Snapshots Per Server",
              "resourceDescription": "Controls the maximum number of active backup jobs per Hyper-V server. This resource limit applies to a standalone Hyper-V server as well as every Hyper-V server in a cluster.\n\nThe typical setting for this resource type is 2.",
              "backupMethod": "VSS"
            },
            {
              "resourceType": "Active Snapshots Per Cluster",
              "resourceDescription": "Controls the maximum number of active backup jobs per Hyper-V cluster.\n\nThe typical setting for this resource type is 4.",
              "backupMethod": "VSS"
            },
            {
              "resourceType": "Snapshot Operations Per Server",
              "resourceDescription": "Controls the maximum number of simultaneous VSS operations such as create snapshot and delete snapshot on a Hyper-V server or a Hyper-V server in a cluster. This resource limit applies only during the snapshot creation and snapshot deletion phase of a backup. It does not control the number of simultaneous backup jobs.\n\nThe typical setting for this resource type is 1.",
              "backupMethod": "VSS"
            },
            "... 3 more"
          ],
          "workloadType": "Hyper-V"
        },
        "links": {
          "self": {
            "href": "/config/resource-limit-templates/hyperv"
          }
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

## `get_resource_limits` - GET /config/resource-limits

```python
nbu.raw.config.get_resource_limits()
```

**On the wire**

- `GET /config/resource-limits` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "resource-limits",
        "id": "vmware",
        "attributes": {
          "resources": [
            {
              "resourceType": "vCenter",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "snapshot",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Cluster",
              "resourceName": "",
              "resourceLimit": 0
            },
            "... 8 more"
          ],
          "workloadType": "VMware"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/vmware"
          }
        }
      },
      {
        "type": "resource-limits",
        "id": "asset-18",
        "attributes": {
          "resources": [
            {
              "resourceType": "Backup Jobs per asset-18 Cluster",
              "resourceName": "",
              "resourceLimit": 1
            },
            {
              "resourceType": "Backup from Snapshot Jobs per asset-18 Cluster",
              "resourceName": "",
              "resourceLimit": 4
            }
          ],
          "workloadType": "asset-18"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/asset-18"
          }
        }
      },
      {
        "type": "resource-limits",
        "id": "hyperv",
        "attributes": {
          "resources": [
            {
              "resourceType": "Active Snapshots Per Server",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Active Snapshots Per Cluster",
              "resourceName": "",
              "resourceLimit": 0
            },
            {
              "resourceType": "Snapshot Operations Per Server",
              "resourceName": "",
              "resourceLimit": 0
            },
            "... 3 more"
          ],
          "workloadType": "Hyper-V"
        },
        "links": {
          "self": {
            "href": "/config/resource-limits/hyperv"
          }
        }
      },
      "... 4 more"
    ]
  }
  ```

  </details>

## `get_server_group` - GET /config/server-groups/{serverGroupId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/server-groups` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_servers_snapshot_mgmt_server`

GET /config/servers/snapshot-mgmt-servers/{snapshotMgmtServer}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/servers/snapshot-mgmt-servers` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `get_servers_snapshot_mgmt_server_array_array_head_volume`

GET /config/servers/snapshot-mgmt-servers/{snapshot-mgmt-server}/arrays/{array}/array-heads/{array-head-id}/volumes/{volume}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_servers_snapshot_mgmt_server_array_array_head_volumes`

GET /config/servers/snapshot-mgmt-servers/{snapshot-mgmt-server}/arrays/{array}/array-heads/{array-head-id}/volumes

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_servers_snapshot_mgmt_server_array_array_heads`

GET /config/servers/snapshot-mgmt-servers/{snapshot-mgmt-server}/arrays/{array}/array-heads

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_servers_trusted_master_server`

GET /config/servers/trusted-master-servers/{trustedMasterServerName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/servers/trusted-master-servers` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_servers_vmserver` - GET /config/servers/vmservers/{serverName}

```python
nbu.raw.config.get_servers_vmserver('host-05')
```

**On the wire**

- `GET /config/servers/vmservers` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "vmServer",
        "id": "host-05",
        "attributes": {
          "vmServer": {
            "serverName": "host-05",
            "vmType": "VMWARE_VIRTUAL_CENTER_SERVER",
            "userId": "administrator@host-16",
            "password": "",
            "port": 443
          }
        },
        "links": {
          "self": {
            "href": "/config/servers/vmservers/host-05"
          }
        },
        "meta": {
          "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|"
        }
      }
    ]
  }
  ```

  </details>

- `GET /config/servers/vmservers/host-05` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "vmServer",
      "id": "host-05",
      "attributes": {
        "vmServer": {
          "serverName": "host-05",
          "vmType": "VMWARE_VIRTUAL_CENTER_SERVER",
          "userId": "administrator@host-16",
          "password": "",
          "port": 443
        }
      },
      "links": {
        "self": {
          "href": "/config/servers/vmservers/host-05"
        }
      },
      "meta": {
        "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|"
      }
    }
  }
  ```

  </details>

## `get_servers_wssendpoints` - GET /config/servers/wssendpoints

```python
nbu.raw.config.get_servers_wssendpoints()
```

**On the wire**

- `GET /config/servers/wssendpoints` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  []
  ```

  </details>

## `get_slp` - GET /config/slps/{slpName}

```python
nbu.raw.config.get_slp('1M_primary-01_DS3')
```

**On the wire**

- `GET /config/slps` -> **200** (0.15 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "slp",
        "id": "1M_primary-01_DS3",
        "attributes": {
          "slpName": "1M_primary-01_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/1M_primary-01_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/1M_primary-01_DS3"
          }
        }
      },
      {
        "type": "slp",
        "id": "1M_name-01_DS3",
        "attributes": {
          "slpName": "1M_name-01_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/1M_name-01_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/1M_name-01_DS3"
          }
        }
      },
      {
        "type": "slp",
        "id": "TEST_1M_name-02_DS3",
        "attributes": {
          "slpName": "TEST_1M_name-02_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/TEST_1M_name-02_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/TEST_1M_name-02_DS3"
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
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /config/slps/1M_primary-01_DS3` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slp",
      "id": "1M_primary-01_DS3",
      "attributes": {
        "slpName": "1M_primary-01_DS3",
        "versionNumber": 0,
        "flagValues": [],
        "active": true,
        "activationTime": "1970-01-01T00:00:00Z",
        "duplicationPriority": 0,
        "operationList": [
          {
            "flagValues": [],
            "alternateReadServer": null,
            "operationActivationTime": "1970-01-01T00:00:00Z",
            "operationIndex": 1,
            "preserveMultiplexing": false,
            "operationType": "BACKUP",
            "retentionPeriod": {
              "unit": "MONTHS",
              "value": 1
            },
            "retentionType": "FIXED",
            "serverGroup": null,
            "sourceOperationIndex": 0,
            "targetImportSLP": null,
            "targetMasterServer": null,
            "operationPriority": 0,
            "storage": {
              "name": "storage-unit-02",
              "stype": "PureDisk",
              "dpCapabilities": [
                "DSM_DG_FLAG_PATCHWORK",
                "DSM_DG_FLAG_VISIBLE",
                "DSM_DG_FLAG_STSDYNAMIC",
                "... 10 more"
              ],
              "ssCapabilities": [
                "DSM_STS_FLAG_MODEL",
                "DSM_STS_FLAG_SRV_EVSYNC",
                "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                "... 12 more"
              ]
            },
            "volumePool": null
          },
          {
            "flagValues": [],
            "alternateReadServer": "primary-01",
            "operationActivationTime": "1970-01-01T00:00:00Z",
            "operationIndex": 2,
            "preserveMultiplexing": false,
            "operationType": "DUPLICATE",
            "retentionPeriod": {
              "unit": "MONTHS",
              "value": 1
            },
            "retentionType": "FIXED",
            "serverGroup": null,
            "sourceOperationIndex": 1,
            "targetImportSLP": null,
            "targetMasterServer": null,
            "operationPriority": 0,
            "storage": {
              "name": "storage-unit-01",
              "stype": "PureDisk",
              "dpCapabilities": [
                "DSM_DG_FLAG_PATCHWORK",
                "DSM_DG_FLAG_VISIBLE",
                "DSM_DG_FLAG_STSDYNAMIC",
                "... 10 more"
              ],
              "ssCapabilities": [
                "DSM_STS_FLAG_MODEL",
                "DSM_STS_FLAG_SRV_EVSYNC",
                "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                "... 12 more"
              ]
            },
            "volumePool": null,
            "slpWindowName": "Default_24x7_Window",
            "slpWindowClose": "FINISH"
          }
        ]
      },
      "relationships": {
        "versions": {
          "links": {
            "self": {
              "href": "/config/slps/1M_primary-01_DS3/versions"
            }
          },
          "data": [
            {
              "type": "version",
              "id": "0"
            }
          ]
        }
      },
      "links": {
        "self": {
          "href": "/config/slps/1M_primary-01_DS3"
        }
      }
    }
  }
  ```

  </details>

## `get_slp_version` - GET /config/slps/{slpName}/versions/{versionNumber}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_slp_window` - GET /config/slp-windows/{slpWindowName}

```python
nbu.raw.config.get_slp_window('Default_24x7_Window')
```

**On the wire**

- `GET /config/slp-windows` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "slpWindow",
        "id": "Default_24x7_Window",
        "attributes": {
          "excludeDates": {
            "lastDayOfMonth": false,
            "recurringDaysOfMonth": [],
            "recurringDaysOfWeek": [],
            "specificDates": []
          },
          "scheduleName": "Default_24x7_Window",
          "startWindow": [
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 1
            },
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 2
            },
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 3
            },
            "... 4 more"
          ]
        },
        "links": {
          "self": {
            "href": "/config/slp-windows/Default_24x7_Window"
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
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /config/slp-windows/Default_24x7_Window` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slpWindow",
      "id": "Default_24x7_Window",
      "attributes": {
        "excludeDates": {
          "lastDayOfMonth": false,
          "recurringDaysOfMonth": [],
          "recurringDaysOfWeek": [],
          "specificDates": []
        },
        "scheduleName": "Default_24x7_Window",
        "startWindow": [
          {
            "durationSeconds": 86400,
            "startSeconds": 0,
            "dayOfWeek": 1
          },
          {
            "durationSeconds": 86400,
            "startSeconds": 0,
            "dayOfWeek": 2
          },
          {
            "durationSeconds": 86400,
            "startSeconds": 0,
            "dayOfWeek": 3
          },
          "... 4 more"
        ]
      },
      "links": {
        "self": {
          "href": "/config/slp-windows/Default_24x7_Window"
        }
      }
    }
  }
  ```

  </details>

## `get_smtpserver` - GET /config/smtpserver

> **SKIPPED** on this run: NetBackup answered: 404 (error 227) - no entity was found

```python
nbu.raw.config.get_smtpserver()
```

**On the wire**

- `GET /config/smtpserver` -> **404** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 227,
    "errorMessage": "no entity was found",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `get_snapshot_mgmt_servers_cacert_port`

GET /config/snapshot-mgmt-servers-cacerts/{snapshotMgmtServer}/ports/{port}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_snapshotproviders_configured_application`

GET /config/snapshotproviders/configured-applications/{applicationAssetId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_snapshotproviders_configuredplugin_instance`

GET /config/snapshotproviders/configuredplugins/{pluginType}/instances/{instanceName}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/snapshotproviders/configuredplugins` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_snapshotproviders_configuredplugin_instances`

GET /config/snapshotproviders/configuredplugins/{pluginType}/instances

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_snapshotproviders_connected_virtual_machine`

GET /config/snapshotproviders/connected-virtual-machines/{virtualMachineId}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `get_snapshotproviders_supportedplugin`

GET /config/snapshotproviders/supportedplugins/{pluginType}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/snapshotproviders/supportedplugins` -> **500** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 9802,
    "errorMessage": "Failed to retrieve the supported plug-in list from the Snapshot Manager.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `get_workloads_ndmp_host` - GET /config/workloads/ndmp/hosts/{hostID}

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

**On the wire**

- `GET /config/workloads/ndmp/hosts` -> **200** (0.26 s)

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
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_access_hosts` - GET /config/{workloadType}/access-hosts

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_agentless_hosts` - GET /config/agentless-hosts

```python
nbu.raw.config.list_agentless_hosts()
```

**On the wire**

- `GET /config/agentless-hosts` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/config/agentless-hosts?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/agentless-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/agentless-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_cdp_gateway` - GET /config/cdp-gateway

```python
nbu.raw.config.list_cdp_gateway()
```

**On the wire**

- `GET /config/cdp-gateway` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/config/cdp-gateway?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/cdp-gateway?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_credential_schemas` - GET /config/credential-schemas

```python
nbu.raw.config.list_credential_schemas()
```

**On the wire**

- `GET /config/credential-schemas` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "credentialSchema",
        "id": "1",
        "attributes": {
          "name": "EKMS",
          "displayName": "asset-16",
          "version": "1.0",
          "createdDateTime": "2022-03-17T04:55:48+0000",
          "lastUpdatedDateTime": "2022-03-17T04:55:48+0000",
          "credentialAttribute": "<masked>"
        },
        "links": {
          "self": {
            "href": "/config/credential-schemas/1"
          }
        }
      },
      {
        "type": "credentialSchema",
        "id": "2",
        "attributes": {
          "name": "SCHEMA-CLOUD-Instance",
          "displayName": "asset-17",
          "version": "1.0",
          "createdDateTime": "2022-03-17T04:55:55+0000",
          "lastUpdatedDateTime": "2024-01-21T17:38:01+0000",
          "credentialAttribute": "<masked>"
        },
        "links": {
          "self": {
            "href": "/config/credential-schemas/2"
          }
        }
      },
      {
        "type": "credentialSchema",
        "id": "3",
        "attributes": {
          "name": "SCHEMA-asset-18",
          "displayName": "asset-18",
          "version": "1.0",
          "createdDateTime": "2022-03-17T04:55:59+0000",
          "lastUpdatedDateTime": "2022-03-17T04:55:59+0000",
          "credentialAttribute": "<masked>"
        },
        "links": {
          "self": {
            "href": "/config/credential-schemas/3"
          }
        }
      },
      "... 7 more"
    ]
  }
  ```

  </details>

## `list_credentials` - GET /config/credentials

```python
nbu.raw.config.list_credentials()
```

**On the wire**

- `GET /config/credentials` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 10,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/config/credentials?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=CreatedDateTime"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/credentials?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=CreatedDateTime"
      }
    }
  }
  ```

  </details>

## `list_disk_array_hosts` - GET /config/disk-array-hosts

```python
nbu.raw.config.list_disk_array_hosts()
```

**On the wire**

- `GET /config/disk-array-hosts` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/config/disk-array-hosts?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/disk-array-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/disk-array-hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_ecms_agents` - GET /config/ecms-agents

```python
nbu.raw.config.list_ecms_agents()
```

**On the wire**

- `GET /config/ecms-agents` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=credentialName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=credentialName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/ecms-agents?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=credentialName"
      }
    }
  }
  ```

  </details>

## `list_ecms_providers` - GET /config/ecms-providers

```python
nbu.raw.config.list_ecms_providers()
```

**On the wire**

- `GET /config/ecms-providers` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=-10&page%5Blimit%5D=10&sort=ConfigName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=ConfigName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/ecms-providers?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=ConfigName"
      }
    }
  }
  ```

  </details>

## `list_host_devices` - GET /config/hosts/{hostId}/devices

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_hosts` - GET /config/hosts

```python
nbu.raw.config.list_hosts()
```

**On the wire**

- `GET /config/hosts` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "hosts": [
      {
        "hostKey": null,
        "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
        "osType": "UNIX",
        "hostName": "primary-01",
        "nbuVersion": "NetBackup_10.2",
        "masterServer": "primary-01",
        "installedPackages": "warning: Could not load key gpg_pubkey,VRTSnbpck_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0,VRTSpddes_18.0.0.0,VRTSpddeu_18.0.0.0,VRTSpddea_18.0.0.0,VRTSpddei_4.0,VRTSnbcfg_10.2.0.0,VRTSpostgresql_14.7.4.0,VRTSnetbp_10.2.0.0,VRTSnbmqbrkr_10.2.0.0,VRTSnbweb_10.2.0.0,VRTSnbslibs_10.2.0.0",
        "hwDescription": "AuthenticAMD AMD EPYC 7551P 32-Core Processor, 16 CPUs",
        "vxUpdatePlatform": "redhat_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "9",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "user-04",
        "createdDateTime": 1647492988000,
        "lastUpdatedDateTime": 1793687304000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "PRIMARY_SERVER",
        "nbuReleaseVersion": "10.2",
        "createdTimeUTC": "2022-03-17T04:56:28.000Z",
        "lastUpdateTimeUTC": "2026-11-03T06:28:24.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "primary-01",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1647492988000,
            "updatedOn": 1647492988000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "host-03",
            "isApproved": true,
            "isConflicting": false,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1705869412000,
            "updatedOn": 1705869412000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          }
        ]
      },
      {
        "hostKey": null,
        "osVersion": "Linux Mint 21.3 (5.15.0-140-generic)",
        "osType": "UNIX",
        "hostName": "host-01",
        "nbuVersion": "NetBackup_10.5",
        "masterServer": "primary-01",
        "installedPackages": "VRTSpddea_20.5,VRTSnbclt_10.5.0.0,VRTSnbclibs_10.5.0.0,VRTSpbx_1.19.37.0,VRTSnbcfg_10.5.0.0,VRTSnbpck_10.5.0.0,VRTSnbjre_10.5.0.0,VRTSnbjava_10.5.0.0",
        "hwDescription": "GenuineIntel 11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz, 6 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "d33ecc4d-c807-429f-b871-c5fac7766064",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "",
        "createdDateTime": 1705868746000,
        "lastUpdatedDateTime": 1747677600000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "PRIMARY_SERVER",
        "nbuReleaseVersion": "10.5",
        "createdTimeUTC": "2024-01-21T20:25:46.000Z",
        "lastUpdateTimeUTC": "2025-05-19T18:00:00.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-01",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705868746000,
            "updatedOn": 1705868746000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "host-04",
            "isApproved": true,
            "isConflicting": false,
            "origin": "USER_ADDED",
            "isShared": false,
            "createdOn": 1705871748000,
            "updatedOn": 1705871748000,
            "isAddedManually": true,
            "approved": true,
            "conflicting": false,
            "shared": false
          },
          {
            "mappedHostName": "primary-01",
            "isApproved": false,
            "isConflicting": true,
            "origin": "COMMUNICATION_DISCOVERY",
            "isShared": false,
            "createdOn": 1708898758000,
            "updatedOn": 1708898758000,
            "isAddedManually": false,
            "approved": false,
            "conflicting": true,
            "shared": false
          }
        ]
      },
      {
        "hostKey": null,
        "osVersion": "Linux Mint 21.3 (5.15.0-91-generic)",
        "osType": "UNIX",
        "hostName": "host-02",
        "nbuVersion": "NetBackup_10.2",
        "masterServer": "primary-01",
        "installedPackages": "VRTSpddea_18.0,VRTSnbclt_10.2.0.0,VRTSnbclibs_10.2.0.0,VRTSpbx_1.17.62.3,VRTSnbcfg_10.2.0.0,VRTSnbpck_10.2.0.0,VRTSnbjre_10.2.0.0,VRTSnbjava_10.2.0.0",
        "hwDescription": "GenuineIntel Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 4 CPUs",
        "vxUpdatePlatform": "debian_x64",
        "comment": "",
        "isSecureEnabled": true,
        "trustVersion": "UFYNKZJ0UEEKqbv",
        "uuid": "815af09c-a09e-4003-94e3-3a2e7bf27446",
        "autoReissue": false,
        "autoReissueDuration": 0,
        "machineType": "VIRTUAL",
        "hypervisorType": "VMWARE",
        "machineNbuType": "NOT_DEFINED",
        "osReleaseVersion": "21.3",
        "cpuArchitecture": "x86_64",
        "installedEEBs": "",
        "dteClientMode": "AUTOMATIC",
        "serviceUser": "",
        "createdDateTime": 1705981153000,
        "lastUpdatedDateTime": 1706151003000,
        "nbcaCert": true,
        "externalCertificateSubject": "",
        "externalCertificateFingerprintSha1": "",
        "externalCertificateFingerprintSha256": "",
        "nbuHostType": "CLIENT",
        "nbuReleaseVersion": "10.2",
        "createdTimeUTC": "2024-01-23T03:39:13.000Z",
        "lastUpdateTimeUTC": "2024-01-25T02:50:03.000Z",
        "eebsInstalled": "",
        "hasNetBackupCaHostCertificate": "<masked>",
        "servers": [
          "primary-01"
        ],
        "hostMappings": [
          {
            "mappedHostName": "host-02",
            "isApproved": true,
            "isConflicting": false,
            "origin": "CERTIFICATE_DEPLOYMENT",
            "isShared": false,
            "createdOn": 1705981153000,
            "updatedOn": 1705981153000,
            "isAddedManually": false,
            "approved": true,
            "conflicting": false,
            "shared": false
          }
        ]
      }
    ]
  }
  ```

  </details>

## `list_media_servers` - GET /config/media-servers

```python
nbu.raw.config.list_media_servers()
```

**On the wire**

- `GET /config/media-servers` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "mediaServer",
        "id": "primary-01",
        "attributes": {
          "hostName": "primary-01",
          "isMachineUp": true,
          "osType": "Linux",
          "osVersion": "RedHat Linux (5.14.0-759.el9.x86_64)",
          "osReleaseVersion": "9",
          "nbuVersion": "10.2",
          "supportedStoragesInfo": [
            {
              "storageProviderId": "NetBackup",
              "storageCategory": "MSDP"
            },
            {
              "storageProviderId": "NetBackup",
              "storageCategory": "ADVANCED_DISK"
            },
            {
              "storageProviderId": "scalitywan",
              "storageCategory": "CLOUD"
            },
            "... 117 more"
          ],
          "dteMode": "ON",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
        },
        "links": {
          "self": {
            "href": "/netbackup/config/media-servers/primary-01"
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
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/media-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_policies` - GET /config/policies/

```python
nbu.raw.config.list_policies()
```

**On the wire**

- `GET /config/policies/` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "policy",
        "id": "policy-01",
        "attributes": {
          "policy": {
            "policyType": "Standard",
            "policyAttributes": {
              "dataClassification": null,
              "storage": "1M_primary-01_DS3",
              "volumePool": "NetBackup",
              "mediaOwner": "*ANY*",
              "checkpointIntervalMinutes": 0,
              "jobLimit": 2147483647,
              "priority": 0,
              "active": true,
              "effectiveDateUTC": "2022-08-14T04:53:51Z",
              "clientCompress": false,
              "clientEncrypt": false,
              "blockIncremental": false,
              "followNFSMounts": false,
              "crossMountPoints": false,
              "individualFileRestore": false,
              "collectTrueImageRestoreInfo": "Off",
              "collectBareMetalRestoreInfo": false,
              "disableClientSideDeduplication": false,
              "granularRecovery": false,
              "snapshotBackup": false,
              "retainSnapshot": false,
              "alternateClientHostname": null,
              "dataMoverMachine": "NetBackup Media Server",
              "backupHost": null,
              "snapshotMethod": null,
              "keyword": null,
              "exchangeServerList": [],
              "useAccelerator": false,
              "optimizedBackup": false,
              "useMultipleDataStreams": false,
              "exchangeDatabaseBackupSource": "Off",
              "autoManagedType": 0,
              "backupHostPool": null
            }
          }
        },
        "links": {
          "self": {
            "href": "/config/policies/policy-01"
          }
        }
      },
      {
        "type": "policy",
        "id": "policy-02",
        "attributes": {
          "policy": {
            "policyType": "Standard",
            "policyAttributes": {
              "dataClassification": null,
              "storage": "1M_primary-01_DS3",
              "volumePool": "NetBackup",
              "mediaOwner": "*ANY*",
              "checkpointIntervalMinutes": 0,
              "jobLimit": 2147483647,
              "priority": 0,
              "active": true,
              "effectiveDateUTC": "2022-08-14T03:56:21Z",
              "clientCompress": false,
              "clientEncrypt": false,
              "blockIncremental": false,
              "followNFSMounts": false,
              "crossMountPoints": false,
              "individualFileRestore": false,
              "collectTrueImageRestoreInfo": "Off",
              "collectBareMetalRestoreInfo": false,
              "disableClientSideDeduplication": false,
              "granularRecovery": false,
              "snapshotBackup": false,
              "retainSnapshot": false,
              "alternateClientHostname": null,
              "dataMoverMachine": "NetBackup Media Server",
              "backupHost": null,
              "snapshotMethod": null,
              "keyword": null,
              "exchangeServerList": [],
              "useAccelerator": false,
              "optimizedBackup": false,
              "useMultipleDataStreams": false,
              "exchangeDatabaseBackupSource": "Off",
              "autoManagedType": 0,
              "backupHostPool": null
            }
          }
        },
        "links": {
          "self": {
            "href": "/config/policies/policy-02"
          }
        }
      },
      {
        "type": "policy",
        "id": "policy-03",
        "attributes": {
          "policy": {
            "policyType": "Standard",
            "policyAttributes": {
              "dataClassification": null,
              "storage": "1M_primary-01_DS3",
              "volumePool": "NetBackup",
              "mediaOwner": "*ANY*",
              "checkpointIntervalMinutes": 15,
              "jobLimit": 1,
              "priority": 0,
              "active": false,
              "effectiveDateUTC": "2022-04-05T02:25:59Z",
              "clientCompress": false,
              "clientEncrypt": false,
              "blockIncremental": false,
              "followNFSMounts": false,
              "crossMountPoints": false,
              "individualFileRestore": false,
              "collectTrueImageRestoreInfo": "Off",
              "collectBareMetalRestoreInfo": false,
              "disableClientSideDeduplication": false,
              "granularRecovery": false,
              "snapshotBackup": false,
              "retainSnapshot": false,
              "alternateClientHostname": null,
              "dataMoverMachine": "NetBackup Media Server",
              "backupHost": null,
              "snapshotMethod": null,
              "keyword": null,
              "exchangeServerList": [],
              "useAccelerator": true,
              "optimizedBackup": false,
              "useMultipleDataStreams": true,
              "exchangeDatabaseBackupSource": "Off",
              "autoManagedType": 0,
              "backupHostPool": null
            }
          }
        },
        "links": {
          "self": {
            "href": "/config/policies/policy-03"
          }
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 2,
        "offset": 0,
        "last": 10,
        "limit": 10,
        "count": 11,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/config/policies/?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=policyName"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/config/policies/?page%5Boffset%5D=10&page%5Blimit%5D=10&sort=policyName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/policies/?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=policyName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/policies/?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=policyName"
      }
    }
  }
  ```

  </details>

## `list_server_groups` - GET /config/server-groups

```python
nbu.raw.config.list_server_groups()
```

**On the wire**

- `GET /config/server-groups` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_servers_snapshot_mgmt_server_configured_plugin_instances`

GET /config/servers/snapshot-mgmt-servers/{snapshotMgmtServer}/configuredPlugins/{pluginType}/instances

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_servers_snapshot_mgmt_server_extensions`

GET /config/servers/snapshot-mgmt-servers/{snapshotMgmtServer}/extensions

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_servers_snapshot_mgmt_server_relationships_media_servers`

GET /config/servers/snapshot-mgmt-servers/{snapshotMgmtServer}/relationships/media-servers

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_servers_snapshot_mgmt_server_tokens`

GET /config/servers/snapshot-mgmt-servers/{snapshotMgmtServer}/tokens

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_servers_snapshot_mgmt_servers` - GET /config/servers/snapshot-mgmt-servers

```python
nbu.raw.config.list_servers_snapshot_mgmt_servers()
```

**On the wire**

- `GET /config/servers/snapshot-mgmt-servers` -> **200** (0.11 s)

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
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/servers/snapshot-mgmt-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_servers_trusted_master_servers` - GET /config/servers/trusted-master-servers

```python
nbu.raw.config.list_servers_trusted_master_servers()
```

**On the wire**

- `GET /config/servers/trusted-master-servers` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_servers_vmservers` - GET /config/servers/vmservers

```python
nbu.raw.config.list_servers_vmservers()
```

**On the wire**

- `GET /config/servers/vmservers` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "vmServer",
        "id": "host-05",
        "attributes": {
          "vmServer": {
            "serverName": "host-05",
            "vmType": "VMWARE_VIRTUAL_CENTER_SERVER",
            "userId": "administrator@host-16",
            "password": "",
            "port": 443
          }
        },
        "links": {
          "self": {
            "href": "/config/servers/vmservers/host-05"
          }
        },
        "meta": {
          "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|"
        }
      }
    ]
  }
  ```

  </details>

## `list_slp_windows` - GET /config/slp-windows

```python
nbu.raw.config.list_slp_windows()
```

**On the wire**

- `GET /config/slp-windows` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "slpWindow",
        "id": "Default_24x7_Window",
        "attributes": {
          "excludeDates": {
            "lastDayOfMonth": false,
            "recurringDaysOfMonth": [],
            "recurringDaysOfWeek": [],
            "specificDates": []
          },
          "scheduleName": "Default_24x7_Window",
          "startWindow": [
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 1
            },
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 2
            },
            {
              "durationSeconds": 86400,
              "startSeconds": 0,
              "dayOfWeek": 3
            },
            "... 4 more"
          ]
        },
        "links": {
          "self": {
            "href": "/config/slp-windows/Default_24x7_Window"
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
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/slp-windows?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_slps` - GET /config/slps

```python
nbu.raw.config.list_slps()
```

**On the wire**

- `GET /config/slps` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "slp",
        "id": "1M_primary-01_DS3",
        "attributes": {
          "slpName": "1M_primary-01_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/1M_primary-01_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/1M_primary-01_DS3"
          }
        }
      },
      {
        "type": "slp",
        "id": "1M_name-01_DS3",
        "attributes": {
          "slpName": "1M_name-01_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/1M_name-01_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/1M_name-01_DS3"
          }
        }
      },
      {
        "type": "slp",
        "id": "TEST_1M_name-02_DS3",
        "attributes": {
          "slpName": "TEST_1M_name-02_DS3",
          "versionNumber": 0,
          "flagValues": [],
          "active": true,
          "activationTime": "1970-01-01T00:00:00Z",
          "duplicationPriority": 0,
          "operationList": [
            {
              "flagValues": [],
              "alternateReadServer": null,
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 1,
              "preserveMultiplexing": false,
              "operationType": "BACKUP",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 0,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-02",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null
            },
            {
              "flagValues": [],
              "alternateReadServer": "primary-01",
              "operationActivationTime": "1970-01-01T00:00:00Z",
              "operationIndex": 2,
              "preserveMultiplexing": false,
              "operationType": "DUPLICATE",
              "retentionPeriod": {
                "unit": "MONTHS",
                "value": 1
              },
              "retentionType": "FIXED",
              "serverGroup": null,
              "sourceOperationIndex": 1,
              "targetImportSLP": null,
              "targetMasterServer": null,
              "operationPriority": 0,
              "storage": {
                "name": "storage-unit-01",
                "stype": "PureDisk",
                "dpCapabilities": [
                  "DSM_DG_FLAG_PATCHWORK",
                  "DSM_DG_FLAG_VISIBLE",
                  "DSM_DG_FLAG_STSDYNAMIC",
                  "... 10 more"
                ],
                "ssCapabilities": [
                  "DSM_STS_FLAG_MODEL",
                  "DSM_STS_FLAG_SRV_EVSYNC",
                  "DSM_STS_FLAG_INCLUDE_IN_IMAGE",
                  "... 12 more"
                ]
              },
              "volumePool": null,
              "slpWindowName": "Default_24x7_Window",
              "slpWindowClose": "FINISH"
            }
          ]
        },
        "relationships": {
          "versions": {
            "links": {
              "self": {
                "href": "/config/slps/TEST_1M_name-02_DS3/versions"
              }
            },
            "data": [
              {
                "type": "version",
                "id": "0"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/config/slps/TEST_1M_name-02_DS3"
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
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/slps?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_snapshotproviders_configuredplugin_instance_configureddomain_region_networksecuritygroups`

GET /config/snapshotproviders/configuredplugins/{pluginType}/instances/{instanceName}/configureddomains/{serviceDomain}/regions/{region}/networksecuritygroups

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_snapshotproviders_configuredplugin_instance_configureddomain_resourcegroups`

GET /config/snapshotproviders/configuredplugins/{pluginType}/instances/{instanceName}/configureddomains/{subscriptionId}/resourcegroups

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_snapshotproviders_configuredplugin_instance_configureddomains`

GET /config/snapshotproviders/configuredplugins/{pluginType}/instances/{instanceName}/configureddomains

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_snapshotproviders_configuredplugins`

GET /config/snapshotproviders/configuredplugins

```python
nbu.raw.config.list_snapshotproviders_configuredplugins()
```

**On the wire**

- `GET /config/snapshotproviders/configuredplugins` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_snapshotproviders_supported_replication_destinations`

GET /config/snapshotproviders/supported-replication-destinations

```python
nbu.raw.config.list_snapshotproviders_supported_replication_destinations()
```

**On the wire**

- `GET /config/snapshotproviders/supported-replication-destinations` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "supportedReplicationDestinations",
      "attributes": {
        "defaultReplicationDestinations": []
      },
      "links": {
        "self": {
          "href": "/config/snapshotproviders/supported-replication-destinations"
        }
      }
    }
  }
  ```

  </details>

## `list_snapshotproviders_supportedplugins` - GET /config/snapshotproviders/supportedplugins

> **SKIPPED** on this run: NetBackup answered: 500 (error 9802) - Failed to retrieve the supported plug-in list from the Snapshot Manager.

```python
nbu.raw.config.list_snapshotproviders_supportedplugins()
```

**On the wire**

- `GET /config/snapshotproviders/supportedplugins` -> **500** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 9802,
    "errorMessage": "Failed to retrieve the supported plug-in list from the Snapshot Manager.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_unique_policy_clients` - GET /config/unique-policy-clients

```python
nbu.raw.config.list_unique_policy_clients()
```

**On the wire**

- `GET /config/unique-policy-clients` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "uniqueClient",
        "id": "host-33",
        "attributes": {
          "hardware": "Linux",
          "priority": 0,
          "clientInfoType": "HOST",
          "reserved2": 0,
          "policyTypes": [
            "STANDARD"
          ],
          "policyNames": [
            "policy-11"
          ],
          "OS": "RedHat2.6.32"
        },
        "links": {
          "self": {
            "href": "/config/unique-policy-clients"
          }
        }
      },
      {
        "type": "uniqueClient",
        "id": "primary-01",
        "attributes": {
          "hardware": "Linux",
          "priority": 0,
          "clientInfoType": "HOST",
          "reserved2": 0,
          "policyTypes": [
            "NBU-CATALOG",
            "STANDARD"
          ],
          "policyNames": [
            "policy-02",
            "policy-01",
            "policy-03",
            "... 3 more"
          ],
          "OS": "RedHat2.6.32"
        },
        "links": {
          "self": {
            "href": "/config/unique-policy-clients"
          }
        }
      },
      {
        "type": "uniqueClient",
        "id": "host-04",
        "attributes": {
          "hardware": "Linux",
          "priority": 0,
          "clientInfoType": "HOST",
          "reserved2": 0,
          "policyTypes": [
            "STANDARD"
          ],
          "policyNames": [
            "policy-06"
          ],
          "OS": "Debian3.10.0"
        },
        "links": {
          "self": {
            "href": "/config/unique-policy-clients"
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
        "count": 3,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/config/unique-policy-clients?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=uniqueClientName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/unique-policy-clients?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=uniqueClientName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/unique-policy-clients?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=uniqueClientName"
      }
    }
  }
  ```

  </details>

## `list_workloads_cloud_object_store_providers`

GET /config/workloads/cloud-object-store/providers

```python
nbu.raw.config.list_workloads_cloud_object_store_providers()
```

**On the wire**

- `GET /config/workloads/cloud-object-store/providers` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "cosStorage",
        "id": "scalitywan",
        "attributes": {
          "providerName": "Scality RING - WAN",
          "apiType": "S3",
          "description": "Scality S3 Multi-Cloud storage, optimized for multi-site",
          "customInstanceSupported": true,
          "bulkDeleteSupported": false,
          "objectOverwriteAllowed": true,
          "providerPortalUrl": "http://host-17",
          "sslDetails": {
            "supportedSslModes": [
              "NONE",
              "AUTH",
              "DATA"
            ],
            "defaultSSLMode": "DATA",
            "defaultCheckCertificateRevocation": "<masked>"
          },
          "urlAccessStyle": {
            "supportedUrlAccessStyles": [
              "VIRTUAL_STYLE",
              "PATH_STYLE"
            ],
            "defaultUrlAccessStyle": "PATH_STYLE"
          },
          "authenticationApiVersion": "4",
          "supportedProxyTypes": [
            "HTTP",
            "SOCKS",
            "SOCKS4",
            "... 2 more"
          ],
          "supportedProxyAuthenticationTypes": [
            "BASIC",
            "NONE",
            "NTLM"
          ]
        }
      },
      {
        "type": "cosStorage",
        "id": "asset-27",
        "attributes": {
          "providerName": "Amazon GovCloud",
          "apiType": "S3",
          "description": "Simple Storage Service",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "providerPortalUrl": "https://host-18/govcloud-us/contact/",
          "sslDetails": {
            "supportedSslModes": [
              "NONE",
              "AUTH",
              "DATA"
            ],
            "defaultSSLMode": "DATA",
            "defaultCheckCertificateRevocation": "<masked>"
          },
          "urlAccessStyle": {
            "supportedUrlAccessStyles": [
              "VIRTUAL_STYLE",
              "PATH_STYLE"
            ],
            "defaultUrlAccessStyle": "VIRTUAL_STYLE"
          },
          "authenticationApiVersion": "4",
          "providerRegionDetails": [
            {
              "serviceEndpoint": "host-19",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 0,
              "httpsPort": 443,
              "s3RegionDetails": [
                {
                  "serviceHost": "host-19",
                  "regionName": "GovCloud (US-West)",
                  "regionId": "us-gov-west-1"
                },
                {
                  "serviceHost": "host-20",
                  "regionName": "GovCloud (US-East)",
                  "regionId": "us-gov-east-1"
                }
              ]
            },
            {
              "serviceEndpoint": "host-21",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 80,
              "httpsPort": 443,
              "s3RegionDetails": [
                {
                  "serviceHost": "host-21",
                  "regionName": "GovCloud (US-West)",
                  "regionId": "us-gov-west-1",
                  "host-22ServiceHost": "host-22"
                },
                {
                  "serviceHost": "host-23",
                  "regionName": "GovCloud (US-East)",
                  "regionId": "us-gov-east-1",
                  "host-22ServiceHost": "host-24"
                }
              ]
            }
          ],
          "supportedAuthTypes": {
            "accessKey": [
              "Access key ID",
              "Secret access key"
            ],
            "credentialBroker": "<masked>"
          },
          "supportedProxyTypes": [
            "HTTP",
            "SOCKS",
            "SOCKS4",
            "... 2 more"
          ],
          "supportedProxyAuthenticationTypes": [
            "BASIC",
            "NONE",
            "NTLM"
          ]
        }
      },
      {
        "type": "cosStorage",
        "id": "host-25",
        "attributes": {
          "providerName": "host-25",
          "apiType": "S3",
          "description": "Deduplicate Cloud Storage",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "providerPortalUrl": "http://host-25/links/netbackup-cloud-connector-setup/",
          "sslDetails": {
            "supportedSslModes": [
              "NONE",
              "AUTH",
              "DATA"
            ],
            "defaultSSLMode": "DATA",
            "defaultCheckCertificateRevocation": "<masked>"
          },
          "urlAccessStyle": {
            "supportedUrlAccessStyles": [
              "PATH_STYLE"
            ],
            "defaultUrlAccessStyle": "PATH_STYLE"
          },
          "supportedProxyTypes": [
            "HTTP",
            "SOCKS",
            "SOCKS4",
            "... 2 more"
          ],
          "supportedProxyAuthenticationTypes": [
            "BASIC",
            "NONE",
            "NTLM"
          ]
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
        "count": 52,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/config/workloads/cloud-object-store/providers?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/config/workloads/cloud-object-store/providers?page%5Boffset%5D=50&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/workloads/cloud-object-store/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/workloads/cloud-object-store/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_workloads_ndmp_host_volumes` - GET /config/workloads/ndmp/hosts/{hostID}/volumes

> **SKIPPED** on this run: nothing on this server to look at here

```python
("area", "name", "template"), OPERATIONS, ids=[f"{a}.{n}" for a, n, _ in OPERATIONS]
)
def test_get(nbu: NetBackupClient, record: Entry, area: str, name: str, template: str) -> None:
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
    except SDKError as error:
        pytest.skip(f"NetBackup answered: {_why(error)}")
    _cache[f"{template}|{values}"] = answer
```

## `list_workloads_ndmp_hosts` - GET /config/workloads/ndmp/hosts

```python
nbu.raw.config.list_workloads_ndmp_hosts()
```

**On the wire**

- `GET /config/workloads/ndmp/hosts` -> **200** (0.16 s)

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
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/workloads/ndmp/hosts?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>
