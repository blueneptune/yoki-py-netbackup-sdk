# `nbu.raw.accesscontrol`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_managed_object` - GET /access-control/managed-objects/{objectId}

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

## `get_managed_object_access_definition` - GET /access-control/managed-objects/{objectId}/access-definitions/{accessDefinitionId}

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

## `get_managed_object_access_definitions` - GET /access-control/managed-objects/{objectId}/access-definitions

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

## `get_managed_object_access_definitions_effective_acl` - GET /access-control/managed-objects/{objectId}/access-definitions/effective-acl

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

## `get_operation` - GET /access-control/operations/{operationId}

> **SKIPPED** on this run: NetBackup answered: 400

```python
nbu.raw.accesscontrol.get_operation('|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|')
```

**On the wire**

- `GET /access-control/operations` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|",
        "attributes": {
          "description": "Restore to existing vApp",
          "name": "Allow restore to existing VMware Cloud vApp"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|"
          }
        }
      },
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RESTORE_OVERWRITE|",
        "attributes": {
          "description": "Restore overwrite to existing vApp",
          "name": "Allow restore to overwrite VMware Cloud vApp"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RESTORE_OVERWRITE|"
          }
        }
      },
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|asset-23|CLEANUP_ASSETS|",
        "attributes": {
          "description": "Generic assets cleanup",
          "name": "Cleanup"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|asset-23|CLEANUP_ASSETS|"
          }
        }
      },
      "... 245 more"
    ],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 2147483647,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/access-control/operations?page%5Boffset%5D=0&page%5Blimit%5D=2147483647"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/operations?page%5Boffset%5D=0&page%5Blimit%5D=2147483647"
      }
    }
  }
  ```

  </details>

- `GET /access-control/operations/|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|` -> **400** (0.00 s)

  <details><summary>Answer</summary>

  ```
  <!doctype html><html lang="en"><head><title>HTTP Status 400 – Bad Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 – Bad Request</h1></body></html>
  ```

  </details>

## `get_role` - GET /access-control/roles/{roleId}

```python
nbu.raw.accesscontrol.get_role('0')
```

**On the wire**

- `GET /access-control/roles` -> **200** (0.17 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "accessControlRoleV8",
        "id": "0",
        "attributes": {
          "uuid": "520dc02e-a55a-11ec-8000-b0f20f829588",
          "systemDefined": true,
          "template": false,
          "roleType": "USER",
          "name": "Administrator",
          "description": "Can manage all aspects of NetBackup."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/0/relationships/user-principals"
              }
            },
            "data": [
              {
                "type": "userPrincipalV8",
                "id": ":user-04:unixpwd:1001"
              },
              {
                "type": "userPrincipalV8",
                "id": ":user-03:unixpwd:8888"
              },
              {
                "type": "userPrincipalV8",
                "id": ":user-02:unixpwd:9999"
              },
              "... 1 more"
            ]
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/0/relationships/group-principals"
              }
            },
            "data": [
              {
                "type": "groupPrincipalV8",
                "id": ":nbwebgrp:unixpwd:3001"
              }
            ]
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/0"
          }
        }
      },
      {
        "type": "accessControlRoleV8",
        "id": "1",
        "attributes": {
          "uuid": "66c2a8f0-f620-47ab-8445-b6e81ce11cc0",
          "systemDefined": true,
          "template": false,
          "roleType": "HOST",
          "name": "Any Server",
          "description": "Any NetBackup Server."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/1/relationships/user-principals"
              }
            },
            "data": []
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/1/relationships/group-principals"
              }
            },
            "data": []
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/1"
          }
        }
      },
      {
        "type": "accessControlRoleV8",
        "id": "2",
        "attributes": {
          "uuid": "9003064b-e75b-452e-af83-838fd866d61f",
          "systemDefined": true,
          "template": false,
          "roleType": "HOST",
          "name": "Any Machine",
          "description": "Any NetBackup Machine."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/2/relationships/user-principals"
              }
            },
            "data": []
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/2/relationships/group-principals"
              }
            },
            "data": []
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/2"
          }
        }
      },
      "... 26 more"
    ],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 2147483647,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/access-control/roles?page%5Boffset%5D=0&page%5Blimit%5D=2147483647&sort=id"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/roles?page%5Boffset%5D=0&page%5Blimit%5D=2147483647&sort=id"
      }
    }
  }
  ```

  </details>

- `GET /access-control/roles/0` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "id": "0",
      "attributes": {
        "uuid": "520dc02e-a55a-11ec-8000-b0f20f829588",
        "systemDefined": true,
        "template": false,
        "roleType": "USER",
        "name": "Administrator",
        "description": "Can manage all aspects of NetBackup."
      },
      "relationships": {
        "userPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/0/relationships/user-principals"
            }
          },
          "data": [
            {
              "type": "userPrincipalV8",
              "id": ":user-04:unixpwd:1001"
            },
            {
              "type": "userPrincipalV8",
              "id": ":user-03:unixpwd:8888"
            },
            {
              "type": "userPrincipalV8",
              "id": ":user-02:unixpwd:9999"
            },
            "... 1 more"
          ]
        },
        "groupPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/0/relationships/group-principals"
            }
          },
          "data": [
            {
              "type": "groupPrincipalV8",
              "id": ":nbwebgrp:unixpwd:3001"
            }
          ]
        },
        "hostPrincipals": {
          "data": []
        }
      },
      "links": {
        "self": {
          "href": "/access-control/roles/0"
        }
      }
    }
  }
  ```

  </details>

## `get_service_namespaces` - GET /access-control/service-namespaces

```python
nbu.raw.accesscontrol.get_service_namespaces()
```

**On the wire**

- `GET /access-control/service-namespaces` -> **200** (0.38 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "managedObject",
        "id": "|ASSETS|",
        "attributes": {
          "name": "Assets",
          "systemRegistered": true
        },
        "relationships": {
          "acl": {
            "data": []
          },
          "primaryOperations": {
            "data": []
          }
        }
      },
      {
        "type": "managedObject",
        "id": "|ASSETS|asset-20|",
        "attributes": {
          "name": "asset-20 assets",
          "systemRegistered": true
        },
        "relationships": {
          "acl": {
            "data": []
          },
          "primaryOperations": {
            "data": []
          }
        }
      },
      {
        "type": "managedObject",
        "id": "|ASSETS|asset-20|CLUSTER|",
        "attributes": {
          "inherit": true,
          "state": "READY",
          "name": "asset-20 clusters, VMs and storage containers",
          "systemRegistered": true
        },
        "relationships": {
          "acl": {
            "data": [
              {
                "type": "accessDefinitionV8",
                "id": "74"
              },
              {
                "type": "accessDefinitionV8",
                "id": "10"
              }
            ]
          },
          "primaryOperations": {
            "data": [
              {
                "type": "accessControlOperation",
                "id": "|OPERATIONS|VIEW|"
              },
              {
                "type": "accessControlOperation",
                "id": "|OPERATIONS|ADD|"
              },
              {
                "type": "accessControlOperation",
                "id": "|OPERATIONS|UPDATE|"
              },
              "... 10 more"
            ]
          }
        }
      },
      "... 142 more"
    ]
  }
  ```

  </details>

## `get_user_principal_roles` - GET /access-control/user-principals/{subjectIdentifier}/roles

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

## `list_identities` - GET /rbac/identities

> **SKIPPED** on this run: NetBackup answered: 400 (error 8961) - An invalid API request is encountered.

```python
nbu.raw.accesscontrol.list_identities()
```

**On the wire**

- `GET /rbac/identities` -> **400** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 8961,
    "errorMessage": "An invalid API request is encountered.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_managed_object_primary_operations` - GET /access-control/managed-objects/{objectId}/primary-operations

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

## `list_operations` - GET /access-control/operations

```python
nbu.raw.accesscontrol.list_operations()
```

**On the wire**

- `GET /access-control/operations` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|",
        "attributes": {
          "description": "Restore to existing vApp",
          "name": "Allow restore to existing VMware Cloud vApp"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RECOVER|"
          }
        }
      },
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RESTORE_OVERWRITE|",
        "attributes": {
          "description": "Restore overwrite to existing vApp",
          "name": "Allow restore to overwrite VMware Cloud vApp"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|VMWARE|VCLOUD_VAPP|RESTORE_OVERWRITE|"
          }
        }
      },
      {
        "type": "accessControlOperation",
        "id": "|OPERATIONS|ASSETS|asset-23|CLEANUP_ASSETS|",
        "attributes": {
          "description": "Generic assets cleanup",
          "name": "Cleanup"
        },
        "links": {
          "self": {
            "href": "/access-control/operations/|OPERATIONS|ASSETS|asset-23|CLEANUP_ASSETS|"
          }
        }
      },
      "... 245 more"
    ],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 2147483647,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/access-control/operations?page%5Boffset%5D=0&page%5Blimit%5D=2147483647"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/operations?page%5Boffset%5D=0&page%5Blimit%5D=2147483647"
      }
    }
  }
  ```

  </details>

## `list_role_access_definitions` - GET /access-control/roles/{roleId}/access-definitions

```python
nbu.raw.accesscontrol.list_role_access_definitions('0')
```

**On the wire**

- `GET /access-control/roles/0/access-definitions` -> **200** (0.07 s)

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
        "href": "https://primary-01:1556/netbackup/access-control/roles/0/access-definitions?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/roles/0/access-definitions?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_roles` - GET /access-control/roles

```python
nbu.raw.accesscontrol.list_roles()
```

**On the wire**

- `GET /access-control/roles` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "accessControlRoleV8",
        "id": "0",
        "attributes": {
          "uuid": "520dc02e-a55a-11ec-8000-b0f20f829588",
          "systemDefined": true,
          "template": false,
          "roleType": "USER",
          "name": "Administrator",
          "description": "Can manage all aspects of NetBackup."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/0/relationships/user-principals"
              }
            },
            "data": [
              {
                "type": "userPrincipalV8",
                "id": ":user-04:unixpwd:1001"
              },
              {
                "type": "userPrincipalV8",
                "id": ":user-03:unixpwd:8888"
              },
              {
                "type": "userPrincipalV8",
                "id": ":user-02:unixpwd:9999"
              },
              "... 1 more"
            ]
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/0/relationships/group-principals"
              }
            },
            "data": [
              {
                "type": "groupPrincipalV8",
                "id": ":nbwebgrp:unixpwd:3001"
              }
            ]
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/0"
          }
        }
      },
      {
        "type": "accessControlRoleV8",
        "id": "1",
        "attributes": {
          "uuid": "66c2a8f0-f620-47ab-8445-b6e81ce11cc0",
          "systemDefined": true,
          "template": false,
          "roleType": "HOST",
          "name": "Any Server",
          "description": "Any NetBackup Server."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/1/relationships/user-principals"
              }
            },
            "data": []
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/1/relationships/group-principals"
              }
            },
            "data": []
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/1"
          }
        }
      },
      {
        "type": "accessControlRoleV8",
        "id": "2",
        "attributes": {
          "uuid": "9003064b-e75b-452e-af83-838fd866d61f",
          "systemDefined": true,
          "template": false,
          "roleType": "HOST",
          "name": "Any Machine",
          "description": "Any NetBackup Machine."
        },
        "relationships": {
          "userPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/2/relationships/user-principals"
              }
            },
            "data": []
          },
          "groupPrincipals": {
            "links": {
              "self": {
                "href": "/access-control/roles/2/relationships/group-principals"
              }
            },
            "data": []
          },
          "hostPrincipals": {
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/access-control/roles/2"
          }
        }
      },
      "... 26 more"
    ],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 2147483647,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/access-control/roles?page%5Boffset%5D=0&page%5Blimit%5D=2147483647&sort=id"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/roles?page%5Boffset%5D=0&page%5Blimit%5D=2147483647&sort=id"
      }
    }
  }
  ```

  </details>
