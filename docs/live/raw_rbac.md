# `nbu.raw.rbac`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_access_rule` - GET /rbac/access-rules/{ruleId}

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

- `GET /rbac/access-rules` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_access_rules` - GET /rbac/access-rules

```python
nbu.raw.rbac.get_access_rules()
```

**On the wire**

- `GET /rbac/access-rules` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `get_object_group` - GET /rbac/object-groups/{objectGroupId}

```python
nbu.raw.rbac.get_object_group('1')
```

**On the wire**

- `GET /rbac/object-groups` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "object-group",
        "id": "1",
        "attributes": {
          "name": "All Objects",
          "description": "Represents all objects",
          "isSystemDefined": true,
          "criteria": [
            {
              "criterionId": 1,
              "objectCriterion": "true",
              "objectType": "NBAppserver",
              "isSystemDefined": true
            },
            {
              "criterionId": 4,
              "objectCriterion": "true",
              "objectType": "NBPolicy",
              "isSystemDefined": true
            },
            {
              "criterionId": 6,
              "objectCriterion": "true",
              "objectType": "NBVmwareAsset",
              "isSystemDefined": true
            },
            "... 5 more"
          ]
        },
        "links": {
          "self": {
            "href": "/rbac/object-groups/1"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /rbac/object-groups/1` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "object-group",
      "id": "1",
      "attributes": {
        "name": "All Objects",
        "description": "Represents all objects",
        "isSystemDefined": true,
        "criteria": [
          {
            "criterionId": 1,
            "objectCriterion": "true",
            "objectType": "NBAppserver",
            "isSystemDefined": true
          },
          {
            "criterionId": 4,
            "objectCriterion": "true",
            "objectType": "NBPolicy",
            "isSystemDefined": true
          },
          {
            "criterionId": 6,
            "objectCriterion": "true",
            "objectType": "NBVmwareAsset",
            "isSystemDefined": true
          },
          "... 5 more"
        ]
      },
      "links": {
        "self": {
          "href": "/rbac/object-groups/1"
        }
      }
    }
  }
  ```

  </details>

## `get_object_groups` - GET /rbac/object-groups

```python
nbu.raw.rbac.get_object_groups()
```

**On the wire**

- `GET /rbac/object-groups` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "object-group",
        "id": "1",
        "attributes": {
          "name": "All Objects",
          "description": "Represents all objects",
          "isSystemDefined": true,
          "criteria": [
            {
              "criterionId": 1,
              "objectCriterion": "true",
              "objectType": "NBAppserver",
              "isSystemDefined": true
            },
            {
              "criterionId": 4,
              "objectCriterion": "true",
              "objectType": "NBPolicy",
              "isSystemDefined": true
            },
            {
              "criterionId": 6,
              "objectCriterion": "true",
              "objectType": "NBVmwareAsset",
              "isSystemDefined": true
            },
            "... 5 more"
          ]
        },
        "links": {
          "self": {
            "href": "/rbac/object-groups/1"
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_object_types` - GET /rbac/object-types

```python
nbu.raw.rbac.get_object_types()
```

**On the wire**

- `GET /rbac/object-types` -> **200** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "object-type",
        "id": "NBClient",
        "attributes": {
          "filterableAttributes": [
            {
              "name": "clientName",
              "type": "Edm.String"
            },
            {
              "name": "clientType",
              "type": "Edm.Int32"
            }
          ]
        },
        "links": {
          "self": {
            "href": "/rbac/object-types"
          }
        }
      },
      {
        "type": "object-type",
        "id": "NBRHVAsset",
        "attributes": {
          "filterableAttributes": [
            {
              "name": "displayName",
              "type": "Edm.String"
            },
            {
              "name": "extendedAttributes/vmAbsolutePath",
              "type": "Edm.String"
            }
          ]
        },
        "links": {
          "self": {
            "href": "/rbac/object-types"
          }
        }
      },
      {
        "type": "object-type",
        "id": "NBVmwareAsset",
        "attributes": {
          "filterableAttributes": [
            {
              "name": "displayName",
              "type": "Edm.String"
            },
            {
              "name": "extendedAttributes/vmAbsolutePath",
              "type": "Edm.String"
            }
          ]
        },
        "links": {
          "self": {
            "href": "/rbac/object-types"
          }
        }
      },
      "... 5 more"
    ]
  }
  ```

  </details>

## `get_permission` - GET /rbac/permissions/{permissionId}

```python
nbu.raw.rbac.get_permission('8')
```

**On the wire**

- `GET /rbac/permissions` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "permission",
        "id": "8",
        "attributes": {
          "name": "View Audit Logs",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      {
        "type": "permission",
        "id": "32",
        "attributes": {
          "name": "Manage Storage",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      {
        "type": "permission",
        "id": "11",
        "attributes": {
          "name": "Manage Protection Plans",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      "... 35 more"
    ]
  }
  ```

  </details>

- `GET /rbac/permissions/8` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "permission",
      "id": "8",
      "attributes": {
        "name": "View Audit Logs",
        "isSystemDefined": true
      },
      "links": {
        "self": {
          "href": "/rbac/permissions"
        }
      }
    }
  }
  ```

  </details>

## `get_permission_categories` - GET /rbac/permission-categories

```python
nbu.raw.rbac.get_permission_categories()
```

**On the wire**

- `GET /rbac/permission-categories` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "permission-category",
        "id": "8",
        "attributes": {
          "name": "Recovery Point Management",
          "isSystemDefined": true
        },
        "relationships": {
          "permissions": {
            "links": {
              "self": {
                "href": "/rbac/permission-categories/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "34"
              },
              {
                "type": "permission",
                "id": "35"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/permission-categories"
          }
        }
      },
      {
        "type": "permission-category",
        "id": "2",
        "attributes": {
          "name": "Security Management",
          "isSystemDefined": true
        },
        "relationships": {
          "permissions": {
            "links": {
              "self": {
                "href": "/rbac/permission-categories/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "8"
              },
              {
                "type": "permission",
                "id": "3"
              },
              {
                "type": "permission",
                "id": "38"
              },
              "... 6 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/permission-categories"
          }
        }
      },
      {
        "type": "permission-category",
        "id": "4",
        "attributes": {
          "name": "Protection Plan Management",
          "isSystemDefined": true
        },
        "relationships": {
          "permissions": {
            "links": {
              "self": {
                "href": "/rbac/permission-categories/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "12"
              },
              {
                "type": "permission",
                "id": "11"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/permission-categories"
          }
        }
      },
      "... 5 more"
    ]
  }
  ```

  </details>

## `get_permissions` - GET /rbac/permissions

```python
nbu.raw.rbac.get_permissions()
```

**On the wire**

- `GET /rbac/permissions` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "permission",
        "id": "8",
        "attributes": {
          "name": "View Audit Logs",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      {
        "type": "permission",
        "id": "32",
        "attributes": {
          "name": "Manage Storage",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      {
        "type": "permission",
        "id": "11",
        "attributes": {
          "name": "Manage Protection Plans",
          "isSystemDefined": true
        },
        "links": {
          "self": {
            "href": "/rbac/permissions"
          }
        }
      },
      "... 35 more"
    ]
  }
  ```

  </details>

## `get_role` - GET /rbac/roles/{roleId}

```python
nbu.raw.rbac.get_role('4')
```

**On the wire**

- `GET /rbac/roles` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "role",
        "id": "4",
        "attributes": {
          "name": "Workload administrator",
          "isSystemDefined": true,
          "description": "Manage and recover assets"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "18"
              },
              {
                "type": "permission",
                "id": "16"
              },
              {
                "type": "permission",
                "id": "15"
              },
              "... 3 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/4"
          }
        }
      },
      {
        "type": "role",
        "id": "2",
        "attributes": {
          "name": "Security administrator",
          "isSystemDefined": true,
          "description": "Manage security and RBAC administration"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "8"
              },
              {
                "type": "permission",
                "id": "3"
              },
              {
                "type": "permission",
                "id": "5"
              },
              "... 12 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/2"
          }
        }
      },
      {
        "type": "role",
        "id": "3",
        "attributes": {
          "name": "Backup administrator",
          "isSystemDefined": true,
          "description": "Manage protection plans, assets, and jobs"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "26"
              },
              {
                "type": "permission",
                "id": "32"
              },
              {
                "type": "permission",
                "id": "21"
              },
              "... 10 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/3"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /rbac/roles/4` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "role",
      "id": "4",
      "attributes": {
        "name": "Workload administrator",
        "isSystemDefined": true,
        "description": "Manage and recover assets"
      },
      "relationships": {
        "permissions": {
          "links": {
            "related": {
              "href": "/rbac/permissions"
            }
          },
          "data": [
            {
              "type": "permission",
              "id": "18"
            },
            {
              "type": "permission",
              "id": "16"
            },
            {
              "type": "permission",
              "id": "15"
            },
            "... 3 more"
          ]
        }
      },
      "links": {
        "self": {
          "href": "/rbac/roles/4"
        }
      }
    }
  }
  ```

  </details>

## `get_roles` - GET /rbac/roles

```python
nbu.raw.rbac.get_roles()
```

**On the wire**

- `GET /rbac/roles` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "role",
        "id": "4",
        "attributes": {
          "name": "Workload administrator",
          "isSystemDefined": true,
          "description": "Manage and recover assets"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "18"
              },
              {
                "type": "permission",
                "id": "16"
              },
              {
                "type": "permission",
                "id": "15"
              },
              "... 3 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/4"
          }
        }
      },
      {
        "type": "role",
        "id": "2",
        "attributes": {
          "name": "Security administrator",
          "isSystemDefined": true,
          "description": "Manage security and RBAC administration"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "8"
              },
              {
                "type": "permission",
                "id": "3"
              },
              {
                "type": "permission",
                "id": "5"
              },
              "... 12 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/2"
          }
        }
      },
      {
        "type": "role",
        "id": "3",
        "attributes": {
          "name": "Backup administrator",
          "isSystemDefined": true,
          "description": "Manage protection plans, assets, and jobs"
        },
        "relationships": {
          "permissions": {
            "links": {
              "related": {
                "href": "/rbac/permissions"
              }
            },
            "data": [
              {
                "type": "permission",
                "id": "26"
              },
              {
                "type": "permission",
                "id": "32"
              },
              {
                "type": "permission",
                "id": "21"
              },
              "... 10 more"
            ]
          }
        },
        "links": {
          "self": {
            "href": "/rbac/roles/3"
          }
        }
      }
    ]
  }
  ```

  </details>
