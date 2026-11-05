# `nbu.raw.assetservice`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:40 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_query` - GET /asset-service/queries/{queryId}

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

## `get_workload` - GET /asset-service/workloads/{workload}

```python
nbu.raw.assetservice.get_workload('asset-18')
```

**On the wire**

- `GET /asset-service/workloads` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "workload",
        "id": "asset-18",
        "attributes": {
          "workloadName": "asset-18"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "asset-18"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18"
          }
        }
      },
      {
        "type": "workload",
        "id": "rhv",
        "attributes": {
          "workloadName": "rhv"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "rhv"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/rhv"
          }
        }
      },
      {
        "type": "workload",
        "id": "genericpolicyapp",
        "attributes": {
          "workloadName": "genericpolicyapp"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "genericpolicyapp"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/genericpolicyapp"
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
        "count": 15,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /asset-service/workloads/asset-18` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "workload",
      "id": "asset-18",
      "attributes": {
        "workloadName": "asset-18"
      },
      "relationships": {
        "workloadDetails": {
          "data": {
            "type": "workloadDetails",
            "id": "asset-18"
          }
        }
      },
      "links": {
        "self": {
          "href": "/asset-service/workloads/asset-18"
        }
      }
    }
  }
  ```

  </details>

## `get_workload_asset_by_workload_asset_id` - GET /asset-service/workloads/{workload}/assets/{assetId}

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

- `GET /asset-service/workloads/asset-18/assets` -> **200** (0.09 s)

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
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/assets?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/assets?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `get_workload_asset_by_workload_asset_id_relationship_name` - GET /asset-service/workloads/{workload}/assets/{assetId}/{relationshipName}

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

## `get_workload_schema` - GET /asset-service/workloads/{workload}/schemas/{schemaId}

```python
nbu.raw.assetservice.get_workload_schema('asset-18', 'asset-asset')
```

**On the wire**

- `GET /asset-service/workloads/asset-18/schemas` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "schemas",
        "id": "asset-asset",
        "attributes": {
          "schemaType": "ASSET",
          "schemaName": "asset"
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/asset-asset"
          }
        }
      },
      {
        "type": "schemas",
        "id": "assets-named-query-request",
        "attributes": {
          "schemaType": "NAMED_QUERY_REQUEST",
          "schemaName": "assets",
          "schema": {
            "type": "object",
            "description": "Request data for executing the assets named query.",
            "x-netbackup": {
              "accessControls": [
                "Namespace:(Reference the `data.meta.accessControlId` metadata response attribute for specific object-level namespaces)",
                "Requires Operation: |OPERATIONS|VIEW|"
              ]
            },
            "properties": {
              "attributes": {
                "queryName": {
                  "type": "string",
                  "description": "Name of this query, 'assets.'",
                  "enum": [
                    "assets"
                  ]
                },
                "workloads": {
                  "type": "array",
                  "description": "List of workloads to execute the query. An empty list means query will be executed by all workloads.",
                  "items": {
                    "type": "string",
                    "enum": [
                      "asset-18"
                    ]
                  }
                },
                "sort": {
                  "type": "array",
                  "description": "Names of fields to sort on. Preceded by '-' for descending sort.  If multiple sort fields are supplied, the result set is sorted on the first field, with subsequent fields used as secondary sort criteria.",
                  "items": {
                    "type": "string"
                  }
                },
                "fields": {
                  "type": "array",
                  "description": "Specifies the fields to be returned in the response of the named query.",
                  "items": {
                    "type": "string"
                  }
                },
                "required": [
                  "queryName",
                  "workloads"
                ]
              }
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/assets-named-query-request"
          }
        }
      },
      {
        "type": "schemas",
        "id": "assets-named-query-response",
        "attributes": {
          "schemaType": "NAMED_QUERY_RESPONSE",
          "schemaName": "assets",
          "schema": {
            "type": "array",
            "items": {
              "allOf": [
                {
                  "type": "object",
                  "properties": {
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "object",
                          "properties": {
                            "href": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "type": {
                      "type": "string",
                      "description": "Type of asset",
                      "enum": [
                        "k8sAsset"
                      ]
                    },
                    "id": {
                      "type": "string",
                      "description": "The global unique identifier of the asset."
                    },
                    "attributes": {
                      "allOf": [
                        {
                          "type": "object",
                          "properties": {
                            "commonAssetAttributes": {
                              "type": "object",
                              "properties": {
                                "activeProtection": {
                                  "type": "object",
                                  "description": "Details of how this asset is currently being protected.",
                                  "properties": {
                                    "protectionDetailsList": {
                                      "type": "array",
                                      "description": "Details of subscribed protection plans or policies of this asset.",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "protectionPlanName": {
                                            "type": "string",
                                            "description": "Associated protection plan name",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "sloId": {
                                            "type": "string",
                                            "description": "Service level objective identifier (SLO ID)",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "isProtectionPlanCustomized": {
                                            "type": "string",
                                            "description": "Is this protection plan customized.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            },
                                            "enum": [
                                              "YES",
                                              "NO"
                                            ],
                                            "default": "NO"
                                          },
                                          "policyName": {
                                            "type": "string",
                                            "description": "The NetBackup policy protecting this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "lastSuccessfulBackupTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "Last successful backup time.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "jobId": {
                                            "type": "integer",
                                            "description": "The NetBackup job ID of last successful backup of this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "subscriptionId": {
                                            "type": "string",
                                            "description": "Asset subscription identifier",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "protectionInheritedFromAsset": {
                                            "type": "object",
                                            "description": "Asset from which the protection is inherited.",
                                            "properties": {
                                              "assetId": {
                                                "type": "string",
                                                "description": "The identifier, which is unique within the workloadType context.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "workloadType": {
                                                "type": "string",
                                                "description": "Asset workload type. For example, \"VMware\".",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "displayName": {
                                                "type": "string",
                                                "description": "The display name of this asset in the NetBackup Web UI.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              }
                                            },
                                            "required": [
                                              "assetId",
                                              "workloadType",
                                              "displayName"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "policyName"
                                        ]
                                      }
                                    }
                                  },
                                  "required": [
                                    "protectionDetailsList"
                                  ]
                                },
                                "credentials": "<masked>",
                                "detection": {
                                  "type": "object",
                                  "description": "Details of how NetBackup has detected this asset. If an asset is auto-discovered or imported, a discoveryHost entry is required. If an asset is manually entered, a discoveryHost entry is not required.",
                                  "properties": {
                                    "detectionMethod": {
                                      "type": "string",
                                      "description": "Describes how the asset record was last detected.",
                                      "enum": [
                                        "DISCOVERY",
                                        "IMPORT",
                                        "MANUAL"
                                      ],
                                      "default": "DISCOVERY",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "discoveryHosts": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "description": "The NetBackup host that discovered this asset and details regarding that discovery.",
                                        "properties": {
                                          "createdBy": {
                                            "type": "string",
                                            "description": "Describes how the asset's data was obtained.",
                                            "enum": [
                                              "DISCOVERY",
                                              "IMPORT"
                                            ],
                                            "default": "DISCOVERY",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "host": {
                                            "type": "object",
                                            "properties": {
                                              "hostName": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "uuid": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "ipAddress": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              }
                                            },
                                            "required": [
                                              "hostName",
                                              "uuid"
                                            ]
                                          },
                                          "firstDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time that the asset was first discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "lastDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time at which the asset was last discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          }
                                        },
                                        "required": [
                                          "createdBy",
                                          "host",
                                          "lastDiscoveredTime"
                                        ]
                                      },
                                      "description": "A list of NetBackup hosts that discovered this asset and details regarding its discovery."
                                    },
                                    "firstDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was first detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "lastDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was last detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    }
                                  },
                                  "required": [
                                    "detectionMethod",
                                    "lastDiscoveredTime"
                                  ]
                                },
                                "displayName": {
                                  "type": "string",
                                  "description": "The display name of this asset in the NetBackup Web UI.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "masters": {
                                  "type": "array",
                                  "items": {
                                    "type": "object",
                                    "properties": {
                                      "hostName": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      },
                                      "uuid": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      },
                                      "ipAddress": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      }
                                    },
                                    "required": [
                                      "hostName",
                                      "uuid"
                                    ]
                                  },
                                  "maxItems": 1,
                                  "description": "The list of NetBackup master servers associated with this asset. When an asset is updated with new master servers, they are appended to the existing list of master servers."
                                },
                                "protectionCapabilities": {
                                  "type": "object",
                                  "description": "The details of how NetBackup protects this asset.",
                                  "properties": {
                                    "isProtectable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can protect the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isProtectableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot protect the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    },
                                    "isRecoverable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can recover the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isRecoverableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot recover the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    }
                                  },
                                  "required": [
                                    "isProtectable",
                                    "isProtectableReason",
                                    "isRecoverable",
                                    "... 1 more"
                                  ]
                                },
                                "providerGeneratedId": {
                                  "type": "string",
                                  "description": "The provider identifier, which is unique within the workloadType context that is provided by the workload.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "accessControlId": {
                                  "type": "string",
                                  "description": "Access control namespace Id for this asset."
                                },
                                "deleted": {
                                  "type": "boolean",
                                  "description": "Represents asset deleted state of this asset.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "NO"
                                  }
                                },
                                "workloadFamily": {
                                  "type": "string",
                                  "description": "The workload family to which this asset belongs. For example, \"Virtualization\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "workloadType": {
                                  "type": "string",
                                  "description": "The workload type to which this asset belongs. For example, \"VMware\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                }
                              },
                              "required": [
                                "detection",
                                "masters",
                                "providerGeneratedId",
                                "... 2 more"
                              ]
                            }
                          }
                        },
                        {
                          "type": "object",
                          "description": "The details of the asset",
                          "properties": {
                            "namespace": {
                              "type": "string",
                              "description": "The asset-18 namespace.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "name": {
                              "type": "string",
                              "description": "The asset name.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "clusterFqdn": {
                              "type": "string",
                              "description": "The fully qualified domain name of the cluster.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "uid": {
                              "type": "string",
                              "description": "The unique identifier for this asset-18 resource.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "parentId": {
                              "type": "string",
                              "description": "The unique identifier of the parent this asset-18 resource belongs to.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "creationTimestamp": {
                              "type": "string",
                              "description": "A timestamp when the asset is created on the asset-18 cluster."
                            },
                            "group": {
                              "type": "string",
                              "description": "Specifies the asset-18 API group belongs to the resource.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "version": {
                              "type": "string",
                              "description": "Specifies the resource version running on the asset-18 cluster.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "kind": {
                              "type": "string",
                              "description": "The kind of asset-18 resource. For example: namespace, secret, deployment.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "labels": {
                              "type": "array",
                              "description": "This is the Key/value pairs of the asset-18 labels attached to the resource object",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "labelKey": {
                                    "type": "string",
                                    "description": "The key for the label",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "labelValue": {
                                    "type": "string",
                                    "description": "The value for the label",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  }
                                }
                              }
                            },
                            "annotations": {
                              "type": "array",
                              "description": "The key/value pairs used to describe the underlying resource in asset-18.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "annotationKey": {
                                    "type": "string",
                                    "description": "The key for the annotation",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "annotationValue": {
                                    "type": "string",
                                    "description": "The value for the annotation",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  }
                                }
                              }
                            }
                          },
                          "required": [
                            "namespace",
                            "name",
                            "clusterFqdn",
                            "... 4 more"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "links",
                    "type",
                    "id",
                    "... 1 more"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "object",
                          "properties": {
                            "href": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "type": {
                      "type": "string",
                      "enum": [
                        "k8sAssetGroup"
                      ]
                    },
                    "id": {
                      "type": "string",
                      "description": "A asset-18 systems-generated string to uniquely identify objects of the K8s group asset."
                    },
                    "attributes": {
                      "allOf": [
                        {
                          "type": "object",
                          "description": "The common asset attributes applicable to the asset groups.",
                          "properties": {
                            "commonAssetAttributes": {
                              "type": "object",
                              "properties": {
                                "detection": {
                                  "type": "object",
                                  "description": "Details of how NetBackup has detected this asset. If an asset is auto-discovered or imported, a discoveryHost entry is required. If an asset is manually entered, a discoveryHost entry is not required.",
                                  "properties": {
                                    "detectionMethod": {
                                      "type": "string",
                                      "description": "Describes how the asset record was last detected.",
                                      "enum": [
                                        "DISCOVERY",
                                        "IMPORT",
                                        "MANUAL"
                                      ],
                                      "default": "DISCOVERY",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "discoveryHosts": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "description": "The NetBackup host that discovered this asset and details regarding that discovery.",
                                        "properties": {
                                          "createdBy": {
                                            "type": "string",
                                            "description": "Describes how the asset's data was obtained.",
                                            "enum": [
                                              "DISCOVERY",
                                              "IMPORT"
                                            ],
                                            "default": "DISCOVERY",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "host": {
                                            "type": "object",
                                            "properties": {
                                              "hostName": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "uuid": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "ipAddress": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              }
                                            },
                                            "required": [
                                              "hostName",
                                              "uuid"
                                            ]
                                          },
                                          "firstDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time that the asset was first discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "lastDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time at which the asset was last discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          }
                                        },
                                        "required": [
                                          "createdBy",
                                          "host",
                                          "lastDiscoveredTime"
                                        ]
                                      },
                                      "description": "A list of NetBackup hosts that discovered this asset and details regarding its discovery."
                                    },
                                    "firstDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was first detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "lastDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was last detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    }
                                  },
                                  "required": [
                                    "detectionMethod",
                                    "lastDiscoveredTime"
                                  ]
                                },
                                "displayName": {
                                  "type": "string",
                                  "description": "Specifies the display name of the asset.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "protectionCapabilities": {
                                  "type": "object",
                                  "description": "The details of how NetBackup protects this asset.",
                                  "properties": {
                                    "isProtectable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can protect the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isProtectableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot protect the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    },
                                    "isRecoverable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can recover the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isRecoverableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot recover the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    }
                                  },
                                  "required": [
                                    "isProtectable",
                                    "isProtectableReason",
                                    "isRecoverable",
                                    "... 1 more"
                                  ]
                                },
                                "providerGeneratedId": {
                                  "type": "string",
                                  "description": "Specifies the unique provider identifier for the workload type.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "accessControlId": {
                                  "type": "string",
                                  "description": "Access control namespace Id for this asset."
                                },
                                "workloadType": {
                                  "type": "string",
                                  "description": "The workload type of the asset. For example, \"asset-18\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "workloadFamily": {
                                  "type": "string",
                                  "description": "The workload family of the asset. For example, \"Virtualization\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "activeProtection": {
                                  "type": "object",
                                  "description": "Details of how this asset is currently being protected.",
                                  "properties": {
                                    "protectionDetailsList": {
                                      "type": "array",
                                      "description": "Details of subscribed protection plans or policies of this asset.",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "protectionPlanName": {
                                            "type": "string",
                                            "description": "Associated protection plan name",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "sloId": {
                                            "type": "string",
                                            "description": "Service level objective identifier (SLO ID)",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "isProtectionPlanCustomized": {
                                            "type": "string",
                                            "description": "Is this protection plan customized.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            },
                                            "enum": [
                                              "YES",
                                              "NO"
                                            ],
                                            "default": "NO"
                                          },
                                          "policyName": {
                                            "type": "string",
                                            "description": "The NetBackup policy protecting this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "lastSuccessfulBackupTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "Last successful backup time.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "jobId": {
                                            "type": "integer",
                                            "description": "The NetBackup job ID of last successful backup of this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "subscriptionId": {
                                            "type": "string",
                                            "description": "Asset subscription identifier",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "protectionInheritedFromAsset": {
                                            "type": "object",
                                            "description": "Asset from which the protection is inherited.",
                                            "properties": {
                                              "assetId": {
                                                "type": "string",
                                                "description": "The identifier, which is unique within the workloadType context.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "workloadType": {
                                                "type": "string",
                                                "description": "Asset workload type. For example, \"VMware\".",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "displayName": {
                                                "type": "string",
                                                "description": "The display name of this asset in the NetBackup Web UI.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              }
                                            },
                                            "required": [
                                              "assetId",
                                              "workloadType",
                                              "displayName"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "policyName"
                                        ]
                                      }
                                    }
                                  },
                                  "required": [
                                    "protectionDetailsList"
                                  ]
                                }
                              },
                              "required": [
                                "displayName",
                                "providerGeneratedId",
                                "accessControlId",
                                "... 1 more"
                              ]
                            }
                          }
                        },
                        {
                          "type": "object",
                          "description": "asset-18 asset group attributes.",
                          "properties": {
                            "assetType": {
                              "type": "string",
                              "description": "The asset type which represents the asset-18 asset group.",
                              "enum": [
                                "assetGroup"
                              ],
                              "default": "assetGroup",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "description": {
                              "type": "string",
                              "description": "The brief description of the asset-18 asset group.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "oDataQueryFilter": {
                              "type": "string",
                              "description": "Defines the filter criteria in the OData query format.",
                              "default": "true",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "clusters": {
                              "type": "array",
                              "description": "The list of cluster name associated with the asset group. Each cluster name has an associated flag.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "serverName": {
                                    "type": "string",
                                    "description": "Name of the cluster.",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "isDeleted": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the cluster is deleted."
                                  },
                                  "hasVIEWPermission": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the user has view permission."
                                  },
                                  "hasPROTECTPermission": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the user has protect permission."
                                  }
                                },
                                "required": [
                                  "serverName",
                                  "isDeleted"
                                ]
                              }
                            },
                            "isdeletedAny": {
                              "type": "boolean",
                              "description": "Flag to indicate if any of the server is deleted from the server list."
                            },
                            "consistentViewPermission": {
                              "type": "boolean",
                              "description": "Flag to indicate if user has a consistent view permission on the cluster."
                            },
                            "consistentProtectPermission": {
                              "type": "boolean",
                              "description": "Flag to indicate if user has a consistent protect permission on the cluster."
                            }
                          },
                          "required": [
                            "clusters",
                            "isdeletedAny"
                          ]
                        }
                      ]
                    },
                    "meta": {
                      "accessControlId": {
                        "type": "string",
                        "description": "Fetches the access control namespace ID for the asset."
                      }
                    }
                  },
                  "required": [
                    "links",
                    "type",
                    "id",
                    "... 1 more"
                  ]
                }
              ]
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/assets-named-query-response"
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
        "count": 28,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=20&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /asset-service/workloads/asset-18/schemas/asset-asset` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "schemas",
      "id": "asset-asset",
      "attributes": {
        "schemaType": "ASSET",
        "schemaName": "asset"
      },
      "links": {
        "self": {
          "href": "/asset-service/workloads/asset-18/schemas/asset-asset"
        }
      }
    }
  }
  ```

  </details>

## `get_workloads` - GET /asset-service/workloads

```python
nbu.raw.assetservice.get_workloads()
```

**On the wire**

- `GET /asset-service/workloads` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "workload",
        "id": "asset-18",
        "attributes": {
          "workloadName": "asset-18"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "asset-18"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18"
          }
        }
      },
      {
        "type": "workload",
        "id": "rhv",
        "attributes": {
          "workloadName": "rhv"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "rhv"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/rhv"
          }
        }
      },
      {
        "type": "workload",
        "id": "genericpolicyapp",
        "attributes": {
          "workloadName": "genericpolicyapp"
        },
        "relationships": {
          "workloadDetails": {
            "data": {
              "type": "workloadDetails",
              "id": "genericpolicyapp"
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/genericpolicyapp"
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
        "count": 15,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_workload_assets` - GET /asset-service/workloads/{workload}/assets

```python
nbu.raw.assetservice.list_workload_assets('asset-18')
```

**On the wire**

- `GET /asset-service/workloads/asset-18/assets` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/assets?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/assets?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_workload_schemas` - GET /asset-service/workloads/{workload}/schemas

```python
nbu.raw.assetservice.list_workload_schemas('asset-18')
```

**On the wire**

- `GET /asset-service/workloads/asset-18/schemas` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "schemas",
        "id": "asset-asset",
        "attributes": {
          "schemaType": "ASSET",
          "schemaName": "asset"
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/asset-asset"
          }
        }
      },
      {
        "type": "schemas",
        "id": "assets-named-query-request",
        "attributes": {
          "schemaType": "NAMED_QUERY_REQUEST",
          "schemaName": "assets",
          "schema": {
            "type": "object",
            "description": "Request data for executing the assets named query.",
            "x-netbackup": {
              "accessControls": [
                "Namespace:(Reference the `data.meta.accessControlId` metadata response attribute for specific object-level namespaces)",
                "Requires Operation: |OPERATIONS|VIEW|"
              ]
            },
            "properties": {
              "attributes": {
                "queryName": {
                  "type": "string",
                  "description": "Name of this query, 'assets.'",
                  "enum": [
                    "assets"
                  ]
                },
                "workloads": {
                  "type": "array",
                  "description": "List of workloads to execute the query. An empty list means query will be executed by all workloads.",
                  "items": {
                    "type": "string",
                    "enum": [
                      "asset-18"
                    ]
                  }
                },
                "sort": {
                  "type": "array",
                  "description": "Names of fields to sort on. Preceded by '-' for descending sort.  If multiple sort fields are supplied, the result set is sorted on the first field, with subsequent fields used as secondary sort criteria.",
                  "items": {
                    "type": "string"
                  }
                },
                "fields": {
                  "type": "array",
                  "description": "Specifies the fields to be returned in the response of the named query.",
                  "items": {
                    "type": "string"
                  }
                },
                "required": [
                  "queryName",
                  "workloads"
                ]
              }
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/assets-named-query-request"
          }
        }
      },
      {
        "type": "schemas",
        "id": "assets-named-query-response",
        "attributes": {
          "schemaType": "NAMED_QUERY_RESPONSE",
          "schemaName": "assets",
          "schema": {
            "type": "array",
            "items": {
              "allOf": [
                {
                  "type": "object",
                  "properties": {
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "object",
                          "properties": {
                            "href": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "type": {
                      "type": "string",
                      "description": "Type of asset",
                      "enum": [
                        "k8sAsset"
                      ]
                    },
                    "id": {
                      "type": "string",
                      "description": "The global unique identifier of the asset."
                    },
                    "attributes": {
                      "allOf": [
                        {
                          "type": "object",
                          "properties": {
                            "commonAssetAttributes": {
                              "type": "object",
                              "properties": {
                                "activeProtection": {
                                  "type": "object",
                                  "description": "Details of how this asset is currently being protected.",
                                  "properties": {
                                    "protectionDetailsList": {
                                      "type": "array",
                                      "description": "Details of subscribed protection plans or policies of this asset.",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "protectionPlanName": {
                                            "type": "string",
                                            "description": "Associated protection plan name",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "sloId": {
                                            "type": "string",
                                            "description": "Service level objective identifier (SLO ID)",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "isProtectionPlanCustomized": {
                                            "type": "string",
                                            "description": "Is this protection plan customized.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            },
                                            "enum": [
                                              "YES",
                                              "NO"
                                            ],
                                            "default": "NO"
                                          },
                                          "policyName": {
                                            "type": "string",
                                            "description": "The NetBackup policy protecting this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "lastSuccessfulBackupTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "Last successful backup time.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "jobId": {
                                            "type": "integer",
                                            "description": "The NetBackup job ID of last successful backup of this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "subscriptionId": {
                                            "type": "string",
                                            "description": "Asset subscription identifier",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "protectionInheritedFromAsset": {
                                            "type": "object",
                                            "description": "Asset from which the protection is inherited.",
                                            "properties": {
                                              "assetId": {
                                                "type": "string",
                                                "description": "The identifier, which is unique within the workloadType context.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "workloadType": {
                                                "type": "string",
                                                "description": "Asset workload type. For example, \"VMware\".",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "displayName": {
                                                "type": "string",
                                                "description": "The display name of this asset in the NetBackup Web UI.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              }
                                            },
                                            "required": [
                                              "assetId",
                                              "workloadType",
                                              "displayName"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "policyName"
                                        ]
                                      }
                                    }
                                  },
                                  "required": [
                                    "protectionDetailsList"
                                  ]
                                },
                                "credentials": "<masked>",
                                "detection": {
                                  "type": "object",
                                  "description": "Details of how NetBackup has detected this asset. If an asset is auto-discovered or imported, a discoveryHost entry is required. If an asset is manually entered, a discoveryHost entry is not required.",
                                  "properties": {
                                    "detectionMethod": {
                                      "type": "string",
                                      "description": "Describes how the asset record was last detected.",
                                      "enum": [
                                        "DISCOVERY",
                                        "IMPORT",
                                        "MANUAL"
                                      ],
                                      "default": "DISCOVERY",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "discoveryHosts": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "description": "The NetBackup host that discovered this asset and details regarding that discovery.",
                                        "properties": {
                                          "createdBy": {
                                            "type": "string",
                                            "description": "Describes how the asset's data was obtained.",
                                            "enum": [
                                              "DISCOVERY",
                                              "IMPORT"
                                            ],
                                            "default": "DISCOVERY",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "host": {
                                            "type": "object",
                                            "properties": {
                                              "hostName": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "uuid": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "ipAddress": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              }
                                            },
                                            "required": [
                                              "hostName",
                                              "uuid"
                                            ]
                                          },
                                          "firstDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time that the asset was first discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "lastDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time at which the asset was last discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          }
                                        },
                                        "required": [
                                          "createdBy",
                                          "host",
                                          "lastDiscoveredTime"
                                        ]
                                      },
                                      "description": "A list of NetBackup hosts that discovered this asset and details regarding its discovery."
                                    },
                                    "firstDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was first detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "lastDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was last detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    }
                                  },
                                  "required": [
                                    "detectionMethod",
                                    "lastDiscoveredTime"
                                  ]
                                },
                                "displayName": {
                                  "type": "string",
                                  "description": "The display name of this asset in the NetBackup Web UI.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "masters": {
                                  "type": "array",
                                  "items": {
                                    "type": "object",
                                    "properties": {
                                      "hostName": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      },
                                      "uuid": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      },
                                      "ipAddress": {
                                        "type": "string",
                                        "x-netbackup": {
                                          "filterable": false,
                                          "sortable": "NO"
                                        }
                                      }
                                    },
                                    "required": [
                                      "hostName",
                                      "uuid"
                                    ]
                                  },
                                  "maxItems": 1,
                                  "description": "The list of NetBackup master servers associated with this asset. When an asset is updated with new master servers, they are appended to the existing list of master servers."
                                },
                                "protectionCapabilities": {
                                  "type": "object",
                                  "description": "The details of how NetBackup protects this asset.",
                                  "properties": {
                                    "isProtectable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can protect the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isProtectableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot protect the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    },
                                    "isRecoverable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can recover the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isRecoverableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot recover the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    }
                                  },
                                  "required": [
                                    "isProtectable",
                                    "isProtectableReason",
                                    "isRecoverable",
                                    "... 1 more"
                                  ]
                                },
                                "providerGeneratedId": {
                                  "type": "string",
                                  "description": "The provider identifier, which is unique within the workloadType context that is provided by the workload.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "accessControlId": {
                                  "type": "string",
                                  "description": "Access control namespace Id for this asset."
                                },
                                "deleted": {
                                  "type": "boolean",
                                  "description": "Represents asset deleted state of this asset.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "NO"
                                  }
                                },
                                "workloadFamily": {
                                  "type": "string",
                                  "description": "The workload family to which this asset belongs. For example, \"Virtualization\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "workloadType": {
                                  "type": "string",
                                  "description": "The workload type to which this asset belongs. For example, \"VMware\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                }
                              },
                              "required": [
                                "detection",
                                "masters",
                                "providerGeneratedId",
                                "... 2 more"
                              ]
                            }
                          }
                        },
                        {
                          "type": "object",
                          "description": "The details of the asset",
                          "properties": {
                            "namespace": {
                              "type": "string",
                              "description": "The asset-18 namespace.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "name": {
                              "type": "string",
                              "description": "The asset name.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "clusterFqdn": {
                              "type": "string",
                              "description": "The fully qualified domain name of the cluster.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "uid": {
                              "type": "string",
                              "description": "The unique identifier for this asset-18 resource.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "parentId": {
                              "type": "string",
                              "description": "The unique identifier of the parent this asset-18 resource belongs to.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "creationTimestamp": {
                              "type": "string",
                              "description": "A timestamp when the asset is created on the asset-18 cluster."
                            },
                            "group": {
                              "type": "string",
                              "description": "Specifies the asset-18 API group belongs to the resource.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "version": {
                              "type": "string",
                              "description": "Specifies the resource version running on the asset-18 cluster.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "kind": {
                              "type": "string",
                              "description": "The kind of asset-18 resource. For example: namespace, secret, deployment.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "labels": {
                              "type": "array",
                              "description": "This is the Key/value pairs of the asset-18 labels attached to the resource object",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "labelKey": {
                                    "type": "string",
                                    "description": "The key for the label",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "labelValue": {
                                    "type": "string",
                                    "description": "The value for the label",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  }
                                }
                              }
                            },
                            "annotations": {
                              "type": "array",
                              "description": "The key/value pairs used to describe the underlying resource in asset-18.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "annotationKey": {
                                    "type": "string",
                                    "description": "The key for the annotation",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "annotationValue": {
                                    "type": "string",
                                    "description": "The value for the annotation",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  }
                                }
                              }
                            }
                          },
                          "required": [
                            "namespace",
                            "name",
                            "clusterFqdn",
                            "... 4 more"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "links",
                    "type",
                    "id",
                    "... 1 more"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "object",
                          "properties": {
                            "href": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    },
                    "type": {
                      "type": "string",
                      "enum": [
                        "k8sAssetGroup"
                      ]
                    },
                    "id": {
                      "type": "string",
                      "description": "A asset-18 systems-generated string to uniquely identify objects of the K8s group asset."
                    },
                    "attributes": {
                      "allOf": [
                        {
                          "type": "object",
                          "description": "The common asset attributes applicable to the asset groups.",
                          "properties": {
                            "commonAssetAttributes": {
                              "type": "object",
                              "properties": {
                                "detection": {
                                  "type": "object",
                                  "description": "Details of how NetBackup has detected this asset. If an asset is auto-discovered or imported, a discoveryHost entry is required. If an asset is manually entered, a discoveryHost entry is not required.",
                                  "properties": {
                                    "detectionMethod": {
                                      "type": "string",
                                      "description": "Describes how the asset record was last detected.",
                                      "enum": [
                                        "DISCOVERY",
                                        "IMPORT",
                                        "MANUAL"
                                      ],
                                      "default": "DISCOVERY",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "discoveryHosts": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "description": "The NetBackup host that discovered this asset and details regarding that discovery.",
                                        "properties": {
                                          "createdBy": {
                                            "type": "string",
                                            "description": "Describes how the asset's data was obtained.",
                                            "enum": [
                                              "DISCOVERY",
                                              "IMPORT"
                                            ],
                                            "default": "DISCOVERY",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "host": {
                                            "type": "object",
                                            "properties": {
                                              "hostName": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "uuid": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              },
                                              "ipAddress": {
                                                "type": "string",
                                                "x-netbackup": {
                                                  "filterable": false,
                                                  "sortable": "NO"
                                                }
                                              }
                                            },
                                            "required": [
                                              "hostName",
                                              "uuid"
                                            ]
                                          },
                                          "firstDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time that the asset was first discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          },
                                          "lastDiscoveredTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "The date and time at which the asset was last discovered by this discovery host, in ISO 8601 format.",
                                            "x-netbackup": {
                                              "filterable": false,
                                              "sortable": "NO"
                                            }
                                          }
                                        },
                                        "required": [
                                          "createdBy",
                                          "host",
                                          "lastDiscoveredTime"
                                        ]
                                      },
                                      "description": "A list of NetBackup hosts that discovered this asset and details regarding its discovery."
                                    },
                                    "firstDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was first detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "lastDiscoveredTime": {
                                      "type": "string",
                                      "format": "date-time",
                                      "description": "The date and time that the asset was last detected globally, in ISO 8601 format.",
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    }
                                  },
                                  "required": [
                                    "detectionMethod",
                                    "lastDiscoveredTime"
                                  ]
                                },
                                "displayName": {
                                  "type": "string",
                                  "description": "Specifies the display name of the asset.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "protectionCapabilities": {
                                  "type": "object",
                                  "description": "The details of how NetBackup protects this asset.",
                                  "properties": {
                                    "isProtectable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can protect the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isProtectableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot protect the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    },
                                    "isRecoverable": {
                                      "type": "string",
                                      "description": "Indicates if and how NetBackup can recover the asset.",
                                      "enum": [
                                        "YES",
                                        "NO",
                                        "INDIRECTLY"
                                      ],
                                      "x-netbackup": {
                                        "filterable": true,
                                        "sortable": "ASC_AND_DESC"
                                      }
                                    },
                                    "isRecoverableReason": {
                                      "type": "string",
                                      "description": "The reason why NetBackup can or cannot recover the asset.",
                                      "x-netbackup": {
                                        "filterable": false,
                                        "sortable": "NO"
                                      }
                                    }
                                  },
                                  "required": [
                                    "isProtectable",
                                    "isProtectableReason",
                                    "isRecoverable",
                                    "... 1 more"
                                  ]
                                },
                                "providerGeneratedId": {
                                  "type": "string",
                                  "description": "Specifies the unique provider identifier for the workload type.",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "accessControlId": {
                                  "type": "string",
                                  "description": "Access control namespace Id for this asset."
                                },
                                "workloadType": {
                                  "type": "string",
                                  "description": "The workload type of the asset. For example, \"asset-18\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "workloadFamily": {
                                  "type": "string",
                                  "description": "The workload family of the asset. For example, \"Virtualization\".",
                                  "x-netbackup": {
                                    "filterable": true,
                                    "sortable": "ASC_AND_DESC"
                                  }
                                },
                                "activeProtection": {
                                  "type": "object",
                                  "description": "Details of how this asset is currently being protected.",
                                  "properties": {
                                    "protectionDetailsList": {
                                      "type": "array",
                                      "description": "Details of subscribed protection plans or policies of this asset.",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "protectionPlanName": {
                                            "type": "string",
                                            "description": "Associated protection plan name",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "sloId": {
                                            "type": "string",
                                            "description": "Service level objective identifier (SLO ID)",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "isProtectionPlanCustomized": {
                                            "type": "string",
                                            "description": "Is this protection plan customized.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            },
                                            "enum": [
                                              "YES",
                                              "NO"
                                            ],
                                            "default": "NO"
                                          },
                                          "policyName": {
                                            "type": "string",
                                            "description": "The NetBackup policy protecting this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "lastSuccessfulBackupTime": {
                                            "type": "string",
                                            "format": "date-time",
                                            "description": "Last successful backup time.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "jobId": {
                                            "type": "integer",
                                            "description": "The NetBackup job ID of last successful backup of this asset.",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "subscriptionId": {
                                            "type": "string",
                                            "description": "Asset subscription identifier",
                                            "x-netbackup": {
                                              "filterable": true,
                                              "sortable": "ASC_AND_DESC",
                                              "modifiable": true
                                            }
                                          },
                                          "protectionInheritedFromAsset": {
                                            "type": "object",
                                            "description": "Asset from which the protection is inherited.",
                                            "properties": {
                                              "assetId": {
                                                "type": "string",
                                                "description": "The identifier, which is unique within the workloadType context.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "workloadType": {
                                                "type": "string",
                                                "description": "Asset workload type. For example, \"VMware\".",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              },
                                              "displayName": {
                                                "type": "string",
                                                "description": "The display name of this asset in the NetBackup Web UI.",
                                                "x-netbackup": {
                                                  "filterable": true,
                                                  "sortable": "ASC_AND_DESC"
                                                }
                                              }
                                            },
                                            "required": [
                                              "assetId",
                                              "workloadType",
                                              "displayName"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "policyName"
                                        ]
                                      }
                                    }
                                  },
                                  "required": [
                                    "protectionDetailsList"
                                  ]
                                }
                              },
                              "required": [
                                "displayName",
                                "providerGeneratedId",
                                "accessControlId",
                                "... 1 more"
                              ]
                            }
                          }
                        },
                        {
                          "type": "object",
                          "description": "asset-18 asset group attributes.",
                          "properties": {
                            "assetType": {
                              "type": "string",
                              "description": "The asset type which represents the asset-18 asset group.",
                              "enum": [
                                "assetGroup"
                              ],
                              "default": "assetGroup",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "description": {
                              "type": "string",
                              "description": "The brief description of the asset-18 asset group.",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "oDataQueryFilter": {
                              "type": "string",
                              "description": "Defines the filter criteria in the OData query format.",
                              "default": "true",
                              "x-netbackup": {
                                "filterable": true,
                                "sortable": "ASC_AND_DESC"
                              }
                            },
                            "clusters": {
                              "type": "array",
                              "description": "The list of cluster name associated with the asset group. Each cluster name has an associated flag.",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "serverName": {
                                    "type": "string",
                                    "description": "Name of the cluster.",
                                    "x-netbackup": {
                                      "filterable": true
                                    }
                                  },
                                  "isDeleted": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the cluster is deleted."
                                  },
                                  "hasVIEWPermission": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the user has view permission."
                                  },
                                  "hasPROTECTPermission": {
                                    "type": "boolean",
                                    "description": "Flag to indicate if the user has protect permission."
                                  }
                                },
                                "required": [
                                  "serverName",
                                  "isDeleted"
                                ]
                              }
                            },
                            "isdeletedAny": {
                              "type": "boolean",
                              "description": "Flag to indicate if any of the server is deleted from the server list."
                            },
                            "consistentViewPermission": {
                              "type": "boolean",
                              "description": "Flag to indicate if user has a consistent view permission on the cluster."
                            },
                            "consistentProtectPermission": {
                              "type": "boolean",
                              "description": "Flag to indicate if user has a consistent protect permission on the cluster."
                            }
                          },
                          "required": [
                            "clusters",
                            "isdeletedAny"
                          ]
                        }
                      ]
                    },
                    "meta": {
                      "accessControlId": {
                        "type": "string",
                        "description": "Fetches the access control namespace ID for the asset."
                      }
                    }
                  },
                  "required": [
                    "links",
                    "type",
                    "id",
                    "... 1 more"
                  ]
                }
              ]
            }
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/asset-18/schemas/assets-named-query-response"
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
        "count": 28,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=20&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/asset-18/schemas?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>
