# `nbu.raw.gateway`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_authorization_context` - GET /authorization-context

```python
nbu.raw.gateway.get_authorization_context()
```

**On the wire**

- `GET /authorization-context` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "authorizationContext",
      "id": "12b94733-12c2-45eb-aa6b-36a4c4e465b9",
      "attributes": {
        "subject": "primary-01:user-01:unixpwd",
        "issuer": "nbu_master",
        "issuedAt": "2026-11-05T06:08:43.595Z",
        "expireDate": "2026-11-05T10:08:43.591Z",
        "authToken": "<masked>",
        "isAdmin": true,
        "isMachine": false,
        "permissions": [],
        "roleIds": [
          0
        ]
      },
      "relationships": {
        "authContextRoles": {
          "data": [
            {
              "type": "authContextRole",
              "id": "0"
            }
          ]
        }
      },
      "links": {
        "self": {
          "href": "/authorization-context"
        }
      }
    }
  }
  ```

  </details>

## `get_login` - GET /sso/login

> **SKIPPED** on this run: NetBackup answered: 400 (error 7812) - At least one IDP configuration must be enabled.

```python
nbu.raw.gateway.get_login()
```

**On the wire**

- `GET /sso/login` -> **400** (0.01 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 7812,
    "errorMessage": "At least one IDP configuration must be enabled.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "An identity provider configuration is not enabled for this master server."
    ]
  }
  ```

  </details>

## `get_ping` - GET /ping

```python
nbu.raw.gateway.get_ping()
```

**On the wire**

- `GET /ping` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  1793861163133
  ```

  </details>

## `get_saml2_metadata` - GET /sso/saml2/metadata

> **SKIPPED** on this run: NetBackup answered: 400 (error 7812) - At least one IDP configuration must be enabled.

```python
nbu.raw.gateway.get_saml2_metadata()
```

**On the wire**

- `GET /sso/saml2/metadata` -> **400** (0.01 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 7812,
    "errorMessage": "At least one IDP configuration must be enabled.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "An identity provider configuration is not enabled for this master server."
    ]
  }
  ```

  </details>

## `get_tokenkey` - GET /tokenkey

```python
nbu.raw.gateway.get_tokenkey()
```

**On the wire**

- `GET /tokenkey` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```
  <public key masked>

  ```

  </details>

## `get_user_sessions` - GET /user-sessions

```python
nbu.raw.gateway.get_user_sessions()
```

**On the wire**

- `GET /user-sessions` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "user-session-v4",
        "id": "101656",
        "attributes": {
          "userName": "user-01",
          "domainName": "",
          "domainType": "unixpwd",
          "expiresAt": "2026-11-05T10:08:43.591Z",
          "signedInAt": "2026-11-05T06:08:43.590Z"
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
        "href": "https://primary-01:1556/netbackup/user-sessions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=signedInAt"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/user-sessions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=signedInAt"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/user-sessions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=signedInAt"
      }
    }
  }
  ```

  </details>
