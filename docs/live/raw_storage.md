# `nbu.raw.storage`: every read, live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## `get_bulk_drive_request` - GET /storage/bulk-drive-requests/{requestId}

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

## `get_cloud_provider` - GET /storage/cloud/providers/{providerId}

```python
nbu.raw.storage.get_cloud_provider('scalitywan')
```

**On the wire**

- `GET /storage/cloud/providers` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "cloudProvider",
        "id": "scalitywan",
        "attributes": {
          "providerName": "Scality RING - WAN",
          "apiType": "S3",
          "description": "Scality S3 Multi-Cloud storage, optimized for multi-site",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "serverSideEncryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": false,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 15,
          "defaultReadBufferSizeMegaBytes": 1024,
          "defaultWriteBufferSizeMegaBytes": 1024,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
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
          ],
          "objectLockSupported": true,
          "objectLockDetails": {
            "objectLockModes": "COMPLIANCE,GOVERNANCE",
            "objectLockMinInSeconds": 86400,
            "objectLockMaxInSeconds": 3153600000
          },
          "emptyLocationConstraint": false
        }
      },
      {
        "type": "cloudProvider",
        "id": "asset-27",
        "attributes": {
          "providerName": "Amazon GovCloud",
          "apiType": "S3",
          "description": "Simple Storage Service",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "serverSideEncryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 16,
          "defaultReadBufferSizeMegaBytes": 400,
          "defaultWriteBufferSizeMegaBytes": 400,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
          },
          "authenticationApiVersion": "4",
          "providerRegionDetails": [
            {
              "instanceName": "asset-26",
              "serviceEndpoint": "host-19",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 0,
              "httpsPort": 443,
              "userCreated": false,
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
              "instanceName": "asset-27",
              "serviceEndpoint": "host-21",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 80,
              "httpsPort": 443,
              "userCreated": false,
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
          ],
          "selectedStorageClass": "STANDARD",
          "supportedStorageClasses": [
            {
              "name": "STANDARD",
              "description": "Amazon S3 STANDARD",
              "httpKey": "x-amz-storage-class",
              "deduplicationSupported": true
            },
            {
              "name": "STANDARD_IA",
              "description": "Amazon S3 STANDARD - Infrequent Access",
              "httpKey": "x-amz-storage-class",
              "deduplicationSupported": true
            },
            {
              "name": "host-22",
              "description": "Amazon host-22",
              "httpKey": "x-amz-storage-class",
              "longTermRetentionDetails": {
                "retrievalRetentionPeriod": {
                  "description": "Retrieval retention period in number of days",
                  "range": "1-30",
                  "defaultValue": 3,
                  "minRetentionInPrevTier": 0
                }
              },
              "deduplicationSupported": true
            },
            "... 3 more"
          ],
          "objectLockSupported": true,
          "objectLockDetails": {
            "objectLockModes": "COMPLIANCE,GOVERNANCE",
            "objectLockMinInSeconds": 86400,
            "objectLockMaxInSeconds": 3153600000
          },
          "emptyLocationConstraint": false
        }
      },
      {
        "type": "cloudProvider",
        "id": "host-25",
        "attributes": {
          "providerName": "host-25",
          "apiType": "S3",
          "description": "Deduplicate Cloud Storage",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 25,
          "defaultReadBufferSizeMegaBytes": 1000,
          "defaultWriteBufferSizeMegaBytes": 1000,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
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
          ],
          "objectLockSupported": false,
          "emptyLocationConstraint": false
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 7,
        "offset": 0,
        "last": 60,
        "limit": 10,
        "count": 61,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=60&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /storage/cloud/providers/scalitywan` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "cloudProvider",
      "id": "scalitywan",
      "attributes": {
        "providerName": "Scality RING - WAN",
        "apiType": "S3",
        "description": "Scality S3 Multi-Cloud storage, optimized for multi-site",
        "needTokenRenew": "<masked>",
        "encryptionSupported": true,
        "serverSideEncryptionSupported": true,
        "compressionSupported": true,
        "supportedKind": "SourceAndTarget",
        "customInstanceSupported": true,
        "bulkDeleteSupported": false,
        "objectOverwriteAllowed": true,
        "defaultChunkSizeMegaBytes": 15,
        "defaultReadBufferSizeMegaBytes": 1024,
        "defaultWriteBufferSizeMegaBytes": 1024,
        "deduplicationSupported": true,
        "dedupDetails": {
          "defaultDeduplicationChunkSizeMegaBytes": 64,
          "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
          "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
        },
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
        "curlDetails": {
          "defaultCurlLoggingEnabled": false,
          "curlTimeOutSeconds": 0,
          "curlConnectionTimeOutSeconds": 300
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
        ],
        "objectLockSupported": true,
        "objectLockDetails": {
          "objectLockModes": "COMPLIANCE,GOVERNANCE",
          "objectLockMinInSeconds": 86400,
          "objectLockMaxInSeconds": 3153600000
        },
        "emptyLocationConstraint": false
      }
    }
  }
  ```

  </details>

## `get_disk_pool` - GET /storage/disk-pools/{diskPoolId}

```python
nbu.raw.storage.get_disk_pool('PureDisk:disk-pool-01')
```

**On the wire**

- `GET /storage/disk-pools` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "diskPool",
        "id": "PureDisk:disk-pool-01",
        "attributes": {
          "name": "disk-pool-01",
          "sType": "PureDisk",
          "storageCategory": "MSDP",
          "diskVolumes": [
            {
              "name": "volume-01",
              "id": "766F6C756D652D3031",
              "diskMediaId": "@aaaah",
              "state": "UP",
              "rawSizeBytes": 8341450185728,
              "freeSizeBytes": 8271524834304,
              "isReplicationSource": false,
              "isReplicationTarget": false,
              "wormIndelibleMinimumInterval": 0,
              "wormIndelibleMaximumInterval": 0
            }
          ],
          "highWaterMark": 98,
          "lowWaterMark": 80,
          "maximumIoStreams": {
            "limitIoStreams": false
          },
          "diskPoolState": "UP",
          "diskPoolCapabilities": [
            "PATCH_WORK",
            "VISIBLE",
            "OPEN_STORAGE",
            "... 10 more"
          ],
          "rawSizeBytes": 8341450185728,
          "usableSizeBytes": 8341450185728,
          "availableSpaceBytes": 8271524834304,
          "usedCapacityBytes": 69925351424,
          "wormCapable": false,
          "readOnly": false,
          "mediaServersCount": 1
        },
        "relationships": {
          "storageServers": {
            "links": {
              "related": {
                "href": "/netbackup/storage/storage-servers/"
              }
            },
            "data": [
              {
                "type": "storageServer",
                "id": "PureDisk:primary-01"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/disk-pools/PureDisk:disk-pool-01"
          }
        }
      },
      {
        "type": "diskPool",
        "id": "PureDisk:disk-pool-02",
        "attributes": {
          "name": "disk-pool-02",
          "sType": "PureDisk",
          "storageCategory": "MSDP",
          "diskVolumes": [
            {
              "name": "volume-02",
              "id": "766F6C756D652D3032",
              "diskMediaId": "@aaaaj",
              "state": "UP",
              "rawSizeBytes": 9007199254740992,
              "freeSizeBytes": 9007192007104915,
              "isReplicationSource": false,
              "isReplicationTarget": false,
              "wormIndelibleMinimumInterval": 0,
              "wormIndelibleMaximumInterval": 0
            }
          ],
          "highWaterMark": 98,
          "lowWaterMark": 80,
          "maximumIoStreams": {
            "limitIoStreams": true,
            "streamsPerVolume": 2
          },
          "diskPoolState": "UP",
          "diskPoolCapabilities": [
            "PATCH_WORK",
            "VISIBLE",
            "OPEN_STORAGE",
            "... 10 more"
          ],
          "rawSizeBytes": 9007199254740992,
          "usableSizeBytes": 9007199254740992,
          "availableSpaceBytes": 9007192007104915,
          "usedCapacityBytes": 7247636077,
          "wormCapable": false,
          "readOnly": false,
          "mediaServersCount": 1
        },
        "relationships": {
          "storageServers": {
            "links": {
              "related": {
                "href": "/netbackup/storage/storage-servers/"
              }
            },
            "data": [
              {
                "type": "storageServer",
                "id": "PureDisk:primary-01"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/disk-pools/PureDisk:disk-pool-02"
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
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /storage/disk-pools/PureDisk:disk-pool-01` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "diskPool",
      "id": "PureDisk:disk-pool-01",
      "attributes": {
        "name": "disk-pool-01",
        "sType": "PureDisk",
        "storageCategory": "MSDP",
        "diskVolumes": [
          {
            "name": "volume-01",
            "id": "766F6C756D652D3031",
            "diskMediaId": "@aaaah",
            "state": "UP",
            "rawSizeBytes": 8341450185728,
            "freeSizeBytes": 8271524834304,
            "isReplicationSource": false,
            "isReplicationTarget": false,
            "wormIndelibleMinimumInterval": 0,
            "wormIndelibleMaximumInterval": 0
          }
        ],
        "highWaterMark": 98,
        "lowWaterMark": 80,
        "maximumIoStreams": {
          "limitIoStreams": false
        },
        "diskPoolState": "UP",
        "diskPoolCapabilities": [
          "PATCH_WORK",
          "VISIBLE",
          "OPEN_STORAGE",
          "... 10 more"
        ],
        "rawSizeBytes": 8341450185728,
        "usableSizeBytes": 8341450185728,
        "availableSpaceBytes": 8271524834304,
        "usedCapacityBytes": 69925351424,
        "wormCapable": false,
        "readOnly": false,
        "mediaServersCount": 1
      },
      "relationships": {
        "storageServers": {
          "links": {
            "related": {
              "href": "/netbackup/storage/storage-servers/"
            }
          },
          "data": [
            {
              "type": "storageServer",
              "id": "PureDisk:primary-01"
            }
          ]
        }
      },
      "links": {
        "self": {
          "href": "/netbackup/storage/disk-pools/PureDisk:disk-pool-01"
        }
      }
    }
  }
  ```

  </details>

## `get_drive_types` - GET /storage/drive-types

> **SKIPPED** on this run: NetBackup answered: 501 (error 7417) - Storage API Management feature is disabled.

```python
nbu.raw.storage.get_drive_types()
```

**On the wire**

- `GET /storage/drive-types` -> **501** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 7417,
    "errorMessage": "Storage API Management feature is disabled.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "Device monitor API not supported."
    ]
  }
  ```

  </details>

## `get_key_management_services` - GET /storage/key-management-services

```python
nbu.raw.storage.get_key_management_services()
```

**On the wire**

- `GET /storage/key-management-services` -> **200** (19.42 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "keyManagementService",
        "id": "nbkms",
        "attributes": {
          "name": "NetBackup Key Management Service",
          "configured": false
        },
        "links": {
          "self": {
            "href": "/storage/key-management-services/nbkms"
          }
        }
      }
    ]
  }
  ```

  </details>

## `get_storage_server` - GET /storage/storage-servers/{storageServerId}

```python
nbu.raw.storage.get_storage_server('amazon_rawc:primary-01-s3')
```

**On the wire**

- `GET /storage/storage-servers` -> **200** (2.86 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "storageServer",
        "id": "amazon_rawc:primary-01-s3",
        "attributes": {
          "name": "primary-01-s3",
          "storageCategory": "CLOUD",
          "sType": "amazon_rawc",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "OPTIMIZED_IMAGE",
            "OPEN_STORAGE",
            "... 8 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": false,
          "isWormSupported": false,
          "cloudAttributes": {
            "providerId": "amazon",
            "needTokenRenew": "<masked>",
            "serviceEndpoint": "https://host-34",
            "compressionEnabled": true,
            "serverSideEncryptionEnabled": true,
            "objectSizeMegabytes": 16,
            "readBufferSizeBytes": 419430400,
            "writeBufferSizeBytes": 419430400,
            "urlAccessStyle": "VIRTUAL_STYLE",
            "offlineTransferDetails": {
              "offlineTransferMode": "NONE"
            },
            "storageClass": "ONEZONE_IA",
            "s3RegionDetails": [
              {
                "serviceHost": "host-34",
                "regionName": "US East (N. Virginia)",
                "regionId": "us-east-1"
              }
            ],
            "sslDetails": {
              "useSSLMode": "DATA",
              "checkCertificateRevocation": "<masked>",
              "httpPort": 80,
              "httpsPort": 443
            },
            "curlDetails": {
              "curlLoggingEnabled": false,
              "curlTimeOutSeconds": 900,
              "curlConnectionTimeOutSeconds": 300
            },
            "proxyServerEnabled": false,
            "cloudCredentials": "<masked>",
            "sourceKind": false
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3"
          }
        }
      },
      {
        "type": "storageServer",
        "id": "amazon_rawc:primary-01-cloud-backup",
        "attributes": {
          "name": "primary-01-cloud-backup",
          "storageCategory": "CLOUD",
          "sType": "amazon_rawc",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "OPTIMIZED_IMAGE",
            "OPEN_STORAGE",
            "... 8 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": false,
          "isWormSupported": false,
          "cloudAttributes": {
            "providerId": "amazon",
            "needTokenRenew": "<masked>",
            "serviceEndpoint": "https://host-34",
            "compressionEnabled": true,
            "serverSideEncryptionEnabled": false,
            "objectSizeMegabytes": 16,
            "readBufferSizeBytes": 419430400,
            "writeBufferSizeBytes": 419430400,
            "urlAccessStyle": "VIRTUAL_STYLE",
            "offlineTransferDetails": {
              "offlineTransferMode": "NONE"
            },
            "storageClass": "ONEZONE_IA",
            "s3RegionDetails": [
              {
                "serviceHost": "host-34",
                "regionName": "US East (N. Virginia)",
                "regionId": "us-east-1"
              }
            ],
            "sslDetails": {
              "useSSLMode": "DATA",
              "checkCertificateRevocation": "<masked>",
              "httpPort": 80,
              "httpsPort": 443
            },
            "curlDetails": {
              "curlLoggingEnabled": false,
              "curlTimeOutSeconds": 900,
              "curlConnectionTimeOutSeconds": 300
            },
            "proxyServerEnabled": false,
            "cloudCredentials": "<masked>",
            "sourceKind": false
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/amazon_rawc:primary-01-cloud-backup"
          }
        }
      },
      {
        "type": "storageServer",
        "id": "PureDisk:primary-01",
        "attributes": {
          "name": "primary-01",
          "storageCategory": "MSDP",
          "sType": "PureDisk",
          "nbuHostVersion": "10.2",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "SRV_EVSYNC",
            "OPTIMIZED_IMAGE",
            "... 12 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": true,
          "isWormSupported": true,
          "storageUnits": [
            "storage-unit-02",
            "storage-unit-01"
          ],
          "msdpAttributes": {
            "storagePath": "/msdp/data",
            "spaLogPath": "/msdp/data/log",
            "deduplicationDBPath": "/msdp/catalog",
            "specificNetworkInterface": "primary-01",
            "spaLogRetention": 90,
            "verboseLevel": 3,
            "fipsEnabled": false,
            "storagePoolDetails": {
              "rawSizeBytes": 8686141859430,
              "reservedSpaceBytes": 352616815001,
              "sizeBytes": 8356288371097,
              "usedSpaceBytes": 69900592742,
              "availableSpaceBytes": 8246337208320
            },
            "catalogLogicalSizeBytes": 116,
            "catalogFilesCount": 2,
            "deduplicationRatioPercentage": 0.0,
            "extendedCapabilities": [
              "EVENTS_V1",
              "DIRECT_REP",
              "FAST_DELETE",
              "... 32 more"
            ],
            "availDiskspace": 7806532557209,
            "defaultCloudCacheCapacity": 1091995435008,
            "requestCloudCacheCapacity": 1091995435008,
            "maxRequestCloudCacheCapacity": 6267216278323
          },
          "extendedCapabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 32 more"
          ],
          "kmsKeyGroupName": " "
        },
        "relationships": {
          "universalShareStorage": {
            "links": {
              "related": {
                "href": "/storage/storage-servers/PureDisk:primary-01/universal-shares"
              }
            },
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/PureDisk:primary-01"
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
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3` -> **200** (2.74 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "storageServer",
      "id": "amazon_rawc:primary-01-s3",
      "attributes": {
        "name": "primary-01-s3",
        "storageCategory": "CLOUD",
        "sType": "amazon_rawc",
        "additionalMediaServersDetails": [
          {
            "name": "primary-01",
            "operatingSystem": "Linux",
            "netbackupVersion": "10.2"
          }
        ],
        "encryptionEnabled": false,
        "kmsEnabled": false,
        "storageServerState": "UP",
        "storageServerCapabilities": [
          "MODEL",
          "OPTIMIZED_IMAGE",
          "OPEN_STORAGE",
          "... 8 more"
        ],
        "isSnapshotSupported": false,
        "isAcceleratorSupported": true,
        "isAIRSupported": false,
        "isWormSupported": false,
        "cloudAttributes": {
          "providerId": "amazon",
          "needTokenRenew": "<masked>",
          "serviceEndpoint": "https://host-34",
          "compressionEnabled": true,
          "serverSideEncryptionEnabled": true,
          "objectSizeMegabytes": 16,
          "readBufferSizeBytes": 419430400,
          "writeBufferSizeBytes": 419430400,
          "urlAccessStyle": "VIRTUAL_STYLE",
          "offlineTransferDetails": {
            "offlineTransferMode": "NONE"
          },
          "storageClass": "ONEZONE_IA",
          "s3RegionDetails": [
            {
              "serviceHost": "host-34",
              "regionName": "US East (N. Virginia)",
              "regionId": "us-east-1"
            }
          ],
          "sslDetails": {
            "useSSLMode": "DATA",
            "checkCertificateRevocation": "<masked>",
            "httpPort": 80,
            "httpsPort": 443
          },
          "curlDetails": {
            "curlLoggingEnabled": false,
            "curlTimeOutSeconds": 900,
            "curlConnectionTimeOutSeconds": 300
          },
          "proxyServerEnabled": false,
          "cloudCredentials": "<masked>",
          "sourceKind": false
        },
        "sambaSecurityMode": "unknown"
      },
      "links": {
        "self": {
          "href": "/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3"
        }
      }
    }
  }
  ```

  </details>

## `get_storage_server_disk_volume`

GET /storage/storage-servers/{storageServerId}/disk-volumes/{diskVolumeId}

```python
nbu.raw.storage.get_storage_server_disk_volume('amazon_rawc:primary-01-s3', '63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31')
```

**On the wire**

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes` -> **200** (5.85 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "diskVolume",
        "id": "63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31",
        "attributes": {
          "diskVolumeName": "cf-templates-hlca85lmrri6-us-east-1",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31"
          }
        }
      },
      {
        "type": "diskVolume",
        "id": "7072696D6172792D30312D73746F726167652D756E69742D3031",
        "attributes": {
          "diskVolumeName": "primary-01-storage-unit-01",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/7072696D6172792D30312D73746F726167652D756E69742D3031"
          }
        }
      },
      {
        "type": "diskVolume",
        "id": "77696C6472796465732D6D69636861656C2D62696C6C696E6773",
        "attributes": {
          "diskVolumeName": "wildrydes-michael-billings",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/77696C6472796465732D6D69636861656C2D62696C6C696E6773"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 3,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31` -> **200** (5.75 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "diskVolume",
      "id": "63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31",
      "attributes": {
        "diskVolumeName": "cf-templates-hlca85lmrri6-us-east-1",
        "storageServerType": "amazon_rawc",
        "rawSizeBytes": 9223372036854775807,
        "freeSizeBytes": 9223372036854775807,
        "state": "UNKNOWN",
        "isSnapshotEnabled": false,
        "isReplicationSource": false,
        "isReplicationTarget": false,
        "isPrimary": false,
        "isMirror": false,
        "isIndependentMirror": false,
        "numOfReadMounts": 0,
        "numOfWriteMounts": 0,
        "currentReadStreams": 0,
        "currentWriteStreams": 0,
        "requestCloudCacheCapacity": 0,
        "indelibleImageSupported": false,
        "immutableImageSupported": false,
        "wormImageAudit": false,
        "unlockedImageSupported": false,
        "nbControlledImmutablility": false,
        "deletableImageSupported": false,
        "nbControlledIndeliblity": false,
        "createImmutableAndDeletableImage": false,
        "wormCapable": 0,
        "encryptionEnabled": false,
        "kmsEnabled": false
      },
      "links": {
        "self": {
          "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31"
        }
      }
    }
  }
  ```

  </details>

## `get_storage_server_disk_volume_replication_target`

GET /storage/storage-servers/{storageServerId}/disk-volumes/{diskVolumeId}/replication-targets/{replicationTargetId}

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

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets` -> **200** (11.34 s)

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
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=-100&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `get_storage_server_replication_target`

GET /storage/storage-servers/{storageServerId}/replication-targets/{replicationTargetId}

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

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/replication-targets` -> **400** (2.69 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 7425,
    "errorMessage": "Failed to get replication targets.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "The storage server type does not support replication."
    ]
  }
  ```

  </details>

## `get_storage_server_replication_targets`

GET /storage/storage-servers/{storageServerId}/replication-targets

> **SKIPPED** on this run: NetBackup answered: 400 (error 7425) - Failed to get replication targets.

```python
nbu.raw.storage.get_storage_server_replication_targets('amazon_rawc:primary-01-s3')
```

**On the wire**

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/replication-targets` -> **400** (2.74 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 7425,
    "errorMessage": "Failed to get replication targets.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "The storage server type does not support replication."
    ]
  }
  ```

  </details>

## `get_storage_server_universal_share`

GET /storage/storage-servers/{storageServerId}/universal-shares/{shareId}

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

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/universal-shares` -> **400** (2.71 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 4045,
    "errorMessage": "Universal share capability is not supported.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "INSTANT_ACCESS capability is not supported on this storage server."
    ]
  }
  ```

  </details>

## `get_storage_server_universal_shares`

GET /storage/storage-servers/{storageServerId}/universal-shares

> **SKIPPED** on this run: NetBackup answered: 400 (error 4045) - Universal share capability is not supported.

```python
nbu.raw.storage.get_storage_server_universal_shares('amazon_rawc:primary-01-s3')
```

**On the wire**

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/universal-shares` -> **400** (2.89 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 4045,
    "errorMessage": "Universal share capability is not supported.",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "INSTANT_ACCESS capability is not supported on this storage server."
    ]
  }
  ```

  </details>

## `get_storage_unit` - GET /storage/storage-units/{storageUnitName}

```python
nbu.raw.storage.get_storage_unit('storage-unit-01')
```

**On the wire**

- `GET /storage/storage-units` -> **200** (0.16 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "storageUnit",
        "id": "storage-unit-01",
        "attributes": {
          "name": "storage-unit-01",
          "storageType": "Disk",
          "storageSubType": "DiskPool",
          "storageServerType": "PureDisk",
          "storageCategory": "MSDP",
          "okOnRoot": false,
          "stageData": false,
          "useAnyAvailableMediaServer": false,
          "accelerator": true,
          "replicationCapable": false,
          "replicationSourceCapable": false,
          "replicationTargetCapable": false,
          "snapshot": false,
          "mirror": false,
          "independent": false,
          "primary": false,
          "instantAccessEnabled": false,
          "isCloudSTU": true,
          "freeCapacityBytes": 9007192007104915,
          "totalCapacityBytes": 9007199254740992,
          "usedCapacityBytes": 7247636077,
          "mediaServerDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "maxFragmentSizeMegabytes": 51200,
          "maxConcurrentJobs": 4,
          "onDemandOnly": false,
          "wormCapable": false,
          "useWorm": false,
          "capabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 28 more"
          ],
          "highWaterMark": 0,
          "lowWaterMark": 0,
          "robotType": "NOT_ROBOTIC",
          "robotNumber": -1,
          "multiplexing": 0,
          "enableBlockSharing": true,
          "transferThrottle": 0,
          "fileSystemExport": true
        },
        "relationships": {
          "diskPool": {
            "links": {
              "related": {
                "href": "/netbackup/storage/disk-pools/"
              }
            },
            "data": {
              "type": "diskPool",
              "id": "PureDisk:disk-pool-02"
            }
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-units/storage-unit-01"
          }
        }
      },
      {
        "type": "storageUnit",
        "id": "storage-unit-02",
        "attributes": {
          "name": "storage-unit-02",
          "storageType": "Disk",
          "storageSubType": "DiskPool",
          "storageServerType": "PureDisk",
          "storageCategory": "MSDP",
          "okOnRoot": false,
          "stageData": false,
          "useAnyAvailableMediaServer": false,
          "accelerator": true,
          "replicationCapable": false,
          "replicationSourceCapable": false,
          "replicationTargetCapable": false,
          "snapshot": false,
          "mirror": false,
          "independent": false,
          "primary": false,
          "instantAccessEnabled": true,
          "isCloudSTU": false,
          "freeCapacityBytes": 8271525391360,
          "totalCapacityBytes": 8341450185728,
          "usedCapacityBytes": 69924794368,
          "mediaServerDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "maxFragmentSizeMegabytes": 51200,
          "maxConcurrentJobs": 24,
          "onDemandOnly": true,
          "wormCapable": false,
          "useWorm": false,
          "capabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 32 more"
          ],
          "highWaterMark": 0,
          "lowWaterMark": 0,
          "robotType": "NOT_ROBOTIC",
          "robotNumber": -1,
          "multiplexing": 0,
          "enableBlockSharing": true,
          "transferThrottle": 0,
          "fileSystemExport": true
        },
        "relationships": {
          "diskPool": {
            "links": {
              "related": {
                "href": "/netbackup/storage/disk-pools/"
              }
            },
            "data": {
              "type": "diskPool",
              "id": "PureDisk:disk-pool-01"
            }
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-units/storage-unit-02"
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
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `GET /storage/storage-units/storage-unit-01` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "storageUnit",
      "id": "storage-unit-01",
      "attributes": {
        "name": "storage-unit-01",
        "storageType": "Disk",
        "storageSubType": "DiskPool",
        "storageServerType": "PureDisk",
        "storageCategory": "MSDP",
        "okOnRoot": false,
        "stageData": false,
        "useAnyAvailableMediaServer": false,
        "accelerator": true,
        "replicationCapable": false,
        "replicationSourceCapable": false,
        "replicationTargetCapable": false,
        "snapshot": false,
        "mirror": false,
        "independent": false,
        "primary": false,
        "instantAccessEnabled": false,
        "isCloudSTU": true,
        "freeCapacityBytes": 9007192007104915,
        "totalCapacityBytes": 9007199254740992,
        "usedCapacityBytes": 7247636077,
        "mediaServerDetails": [
          {
            "name": "primary-01",
            "operatingSystem": "Linux",
            "netbackupVersion": "10.2"
          }
        ],
        "maxFragmentSizeMegabytes": 51200,
        "maxConcurrentJobs": 4,
        "onDemandOnly": false,
        "wormCapable": false,
        "useWorm": false,
        "capabilities": [
          "EVENTS_V1",
          "DIRECT_REP",
          "FAST_DELETE",
          "... 28 more"
        ],
        "highWaterMark": 0,
        "lowWaterMark": 0,
        "robotNumber": 0,
        "multiplexing": 0,
        "enableBlockSharing": false,
        "transferThrottle": 0,
        "fileSystemExport": false
      },
      "relationships": {
        "diskPool": {
          "links": {
            "related": {
              "href": "/netbackup/storage/disk-pools/"
            }
          },
          "data": {
            "type": "diskPool",
            "id": "PureDisk:disk-pool-02"
          }
        }
      },
      "links": {
        "self": {
          "href": "/netbackup/storage/storage-units/storage-unit-01"
        }
      }
    }
  }
  ```

  </details>

## `get_target_storage_server` - GET /storage/target-storage-servers/{replicationTargetId}

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

- `GET /storage/target-storage-servers` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>

## `list_backup_sizes` - GET /storage/backup-sizes

> **SKIPPED** on this run: NetBackup answered: 404 (error 227) - no entity was found

```python
nbu.raw.storage.list_backup_sizes()
```

**On the wire**

- `GET /storage/backup-sizes` -> **404** (0.09 s)

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

## `list_cloud_providers` - GET /storage/cloud/providers

```python
nbu.raw.storage.list_cloud_providers()
```

**On the wire**

- `GET /storage/cloud/providers` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "cloudProvider",
        "id": "scalitywan",
        "attributes": {
          "providerName": "Scality RING - WAN",
          "apiType": "S3",
          "description": "Scality S3 Multi-Cloud storage, optimized for multi-site",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "serverSideEncryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": false,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 15,
          "defaultReadBufferSizeMegaBytes": 1024,
          "defaultWriteBufferSizeMegaBytes": 1024,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
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
          ],
          "objectLockSupported": true,
          "objectLockDetails": {
            "objectLockModes": "COMPLIANCE,GOVERNANCE",
            "objectLockMinInSeconds": 86400,
            "objectLockMaxInSeconds": 3153600000
          },
          "emptyLocationConstraint": false
        }
      },
      {
        "type": "cloudProvider",
        "id": "asset-27",
        "attributes": {
          "providerName": "Amazon GovCloud",
          "apiType": "S3",
          "description": "Simple Storage Service",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "serverSideEncryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 16,
          "defaultReadBufferSizeMegaBytes": 400,
          "defaultWriteBufferSizeMegaBytes": 400,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
          },
          "authenticationApiVersion": "4",
          "providerRegionDetails": [
            {
              "instanceName": "asset-26",
              "serviceEndpoint": "host-19",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 0,
              "httpsPort": 443,
              "userCreated": false,
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
              "instanceName": "asset-27",
              "serviceEndpoint": "host-21",
              "urlAccessStyle": "VIRTUAL_STYLE",
              "httpPort": 80,
              "httpsPort": 443,
              "userCreated": false,
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
          ],
          "selectedStorageClass": "STANDARD",
          "supportedStorageClasses": [
            {
              "name": "STANDARD",
              "description": "Amazon S3 STANDARD",
              "httpKey": "x-amz-storage-class",
              "deduplicationSupported": true
            },
            {
              "name": "STANDARD_IA",
              "description": "Amazon S3 STANDARD - Infrequent Access",
              "httpKey": "x-amz-storage-class",
              "deduplicationSupported": true
            },
            {
              "name": "host-22",
              "description": "Amazon host-22",
              "httpKey": "x-amz-storage-class",
              "longTermRetentionDetails": {
                "retrievalRetentionPeriod": {
                  "description": "Retrieval retention period in number of days",
                  "range": "1-30",
                  "defaultValue": 3,
                  "minRetentionInPrevTier": 0
                }
              },
              "deduplicationSupported": true
            },
            "... 3 more"
          ],
          "objectLockSupported": true,
          "objectLockDetails": {
            "objectLockModes": "COMPLIANCE,GOVERNANCE",
            "objectLockMinInSeconds": 86400,
            "objectLockMaxInSeconds": 3153600000
          },
          "emptyLocationConstraint": false
        }
      },
      {
        "type": "cloudProvider",
        "id": "host-25",
        "attributes": {
          "providerName": "host-25",
          "apiType": "S3",
          "description": "Deduplicate Cloud Storage",
          "needTokenRenew": "<masked>",
          "encryptionSupported": true,
          "compressionSupported": true,
          "supportedKind": "SourceAndTarget",
          "customInstanceSupported": true,
          "bulkDeleteSupported": true,
          "objectOverwriteAllowed": true,
          "defaultChunkSizeMegaBytes": 25,
          "defaultReadBufferSizeMegaBytes": 1000,
          "defaultWriteBufferSizeMegaBytes": 1000,
          "deduplicationSupported": true,
          "dedupDetails": {
            "defaultDeduplicationChunkSizeMegaBytes": 64,
            "deduplicationReadBufferSizeRangeMegaBytes": "64-1024",
            "deduplicationWriteBufferSizeRangeMegaBytes": "64-1024"
          },
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
          "curlDetails": {
            "defaultCurlLoggingEnabled": false,
            "curlTimeOutSeconds": 0,
            "curlConnectionTimeOutSeconds": 300
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
          ],
          "objectLockSupported": false,
          "emptyLocationConstraint": false
        }
      },
      "... 7 more"
    ],
    "meta": {
      "pagination": {
        "next": 10,
        "pages": 7,
        "offset": 0,
        "last": 60,
        "limit": 10,
        "count": 61,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=10&page%5Blimit%5D=10"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=60&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/cloud/providers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_disk_pools` - GET /storage/disk-pools

```python
nbu.raw.storage.list_disk_pools()
```

**On the wire**

- `GET /storage/disk-pools` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "diskPool",
        "id": "PureDisk:disk-pool-01",
        "attributes": {
          "name": "disk-pool-01",
          "sType": "PureDisk",
          "storageCategory": "MSDP",
          "diskVolumes": [
            {
              "name": "volume-01",
              "id": "766F6C756D652D3031",
              "diskMediaId": "@aaaah",
              "state": "UP",
              "rawSizeBytes": 8341450185728,
              "freeSizeBytes": 8271525391360,
              "isReplicationSource": false,
              "isReplicationTarget": false,
              "wormIndelibleMinimumInterval": 0,
              "wormIndelibleMaximumInterval": 0
            }
          ],
          "highWaterMark": 98,
          "lowWaterMark": 80,
          "maximumIoStreams": {
            "limitIoStreams": false
          },
          "diskPoolState": "UP",
          "diskPoolCapabilities": [
            "PATCH_WORK",
            "VISIBLE",
            "OPEN_STORAGE",
            "... 10 more"
          ],
          "rawSizeBytes": 8341450185728,
          "usableSizeBytes": 8341450185728,
          "availableSpaceBytes": 8271525391360,
          "usedCapacityBytes": 69924794368,
          "wormCapable": false,
          "readOnly": false,
          "mediaServersCount": 1
        },
        "relationships": {
          "storageServers": {
            "links": {
              "related": {
                "href": "/netbackup/storage/storage-servers/"
              }
            },
            "data": [
              {
                "type": "storageServer",
                "id": "PureDisk:primary-01"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/disk-pools/PureDisk:disk-pool-01"
          }
        }
      },
      {
        "type": "diskPool",
        "id": "PureDisk:disk-pool-02",
        "attributes": {
          "name": "disk-pool-02",
          "sType": "PureDisk",
          "storageCategory": "MSDP",
          "diskVolumes": [
            {
              "name": "volume-02",
              "id": "766F6C756D652D3032",
              "diskMediaId": "@aaaaj",
              "state": "UP",
              "rawSizeBytes": 9007199254740992,
              "freeSizeBytes": 9007192007104915,
              "isReplicationSource": false,
              "isReplicationTarget": false,
              "wormIndelibleMinimumInterval": 0,
              "wormIndelibleMaximumInterval": 0
            }
          ],
          "highWaterMark": 98,
          "lowWaterMark": 80,
          "maximumIoStreams": {
            "limitIoStreams": true,
            "streamsPerVolume": 2
          },
          "diskPoolState": "UP",
          "diskPoolCapabilities": [
            "PATCH_WORK",
            "VISIBLE",
            "OPEN_STORAGE",
            "... 10 more"
          ],
          "rawSizeBytes": 9007199254740992,
          "usableSizeBytes": 9007199254740992,
          "availableSpaceBytes": 9007192007104915,
          "usedCapacityBytes": 7247636077,
          "wormCapable": false,
          "readOnly": false,
          "mediaServersCount": 1
        },
        "relationships": {
          "storageServers": {
            "links": {
              "related": {
                "href": "/netbackup/storage/storage-servers/"
              }
            },
            "data": [
              {
                "type": "storageServer",
                "id": "PureDisk:primary-01"
              }
            ]
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/disk-pools/PureDisk:disk-pool-02"
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
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_drives` - GET /storage/drives

```python
nbu.raw.storage.list_drives()
```

**On the wire**

- `GET /storage/drives` -> **200** (0.12 s)

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
        "href": "https://primary-01:1556/netbackup/storage/drives?page%5Boffset%5D=-10&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/drives?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/drives?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_shared_images` - GET /storage/shared-images

> **SKIPPED** on this run: NetBackup answered: 500 (error 130) - system error occurred

```python
nbu.raw.storage.list_shared_images()
```

**On the wire**

- `GET /storage/shared-images` -> **500** (0.21 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 130,
    "errorMessage": "system error occurred",
    "attributeErrors": {
      "exception": "errorCode: 4032"
    },
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## `list_storage_server_disk_volume_replication_targets`

GET /storage/storage-servers/{storageServerId}/disk-volumes/{diskVolumeId}/replication-targets

```python
nbu.raw.storage.list_storage_server_disk_volume_replication_targets('amazon_rawc:primary-01-s3', '63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31')
```

**On the wire**

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets` -> **200** (11.70 s)

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
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=-100&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31/replication-targets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `list_storage_server_disk_volumes`

GET /storage/storage-servers/{storageServerId}/disk-volumes

```python
nbu.raw.storage.list_storage_server_disk_volumes('amazon_rawc:primary-01-s3')
```

**On the wire**

- `GET /storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes` -> **200** (5.69 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "diskVolume",
        "id": "63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31",
        "attributes": {
          "diskVolumeName": "cf-templates-hlca85lmrri6-us-east-1",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/63662D74656D706C617465732D686C636138356C6D727269362D75732D656173742D31"
          }
        }
      },
      {
        "type": "diskVolume",
        "id": "7072696D6172792D30312D73746F726167652D756E69742D3031",
        "attributes": {
          "diskVolumeName": "primary-01-storage-unit-01",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/7072696D6172792D30312D73746F726167652D756E69742D3031"
          }
        }
      },
      {
        "type": "diskVolume",
        "id": "77696C6472796465732D6D69636861656C2D62696C6C696E6773",
        "attributes": {
          "diskVolumeName": "wildrydes-michael-billings",
          "storageServerType": "amazon_rawc",
          "rawSizeBytes": 9223372036854775807,
          "freeSizeBytes": 9223372036854775807,
          "state": "UNKNOWN",
          "isSnapshotEnabled": false,
          "isReplicationSource": false,
          "isReplicationTarget": false,
          "isPrimary": false,
          "isMirror": false,
          "isIndependentMirror": false,
          "numOfReadMounts": 0,
          "numOfWriteMounts": 0,
          "currentReadStreams": 0,
          "currentWriteStreams": 0,
          "requestCloudCacheCapacity": 0,
          "indelibleImageSupported": false,
          "immutableImageSupported": false,
          "wormImageAudit": false,
          "unlockedImageSupported": false,
          "nbControlledImmutablility": false,
          "deletableImageSupported": false,
          "nbControlledIndeliblity": false,
          "createImmutableAndDeletableImage": false,
          "wormCapable": 0,
          "encryptionEnabled": false,
          "kmsEnabled": false
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes/77696C6472796465732D6D69636861656C2D62696C6C696E6773"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 3,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3/disk-volumes?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `list_storage_servers` - GET /storage/storage-servers

```python
nbu.raw.storage.list_storage_servers()
```

**On the wire**

- `GET /storage/storage-servers` -> **200** (2.79 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "storageServer",
        "id": "amazon_rawc:primary-01-s3",
        "attributes": {
          "name": "primary-01-s3",
          "storageCategory": "CLOUD",
          "sType": "amazon_rawc",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "OPTIMIZED_IMAGE",
            "OPEN_STORAGE",
            "... 8 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": false,
          "isWormSupported": false,
          "cloudAttributes": {
            "providerId": "amazon",
            "needTokenRenew": "<masked>",
            "serviceEndpoint": "https://host-34",
            "compressionEnabled": true,
            "serverSideEncryptionEnabled": true,
            "objectSizeMegabytes": 16,
            "readBufferSizeBytes": 419430400,
            "writeBufferSizeBytes": 419430400,
            "urlAccessStyle": "VIRTUAL_STYLE",
            "offlineTransferDetails": {
              "offlineTransferMode": "NONE"
            },
            "storageClass": "ONEZONE_IA",
            "s3RegionDetails": [
              {
                "serviceHost": "host-34",
                "regionName": "US East (N. Virginia)",
                "regionId": "us-east-1"
              }
            ],
            "sslDetails": {
              "useSSLMode": "DATA",
              "checkCertificateRevocation": "<masked>",
              "httpPort": 80,
              "httpsPort": 443
            },
            "curlDetails": {
              "curlLoggingEnabled": false,
              "curlTimeOutSeconds": 900,
              "curlConnectionTimeOutSeconds": 300
            },
            "proxyServerEnabled": false,
            "cloudCredentials": "<masked>",
            "sourceKind": false
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/amazon_rawc:primary-01-s3"
          }
        }
      },
      {
        "type": "storageServer",
        "id": "amazon_rawc:primary-01-cloud-backup",
        "attributes": {
          "name": "primary-01-cloud-backup",
          "storageCategory": "CLOUD",
          "sType": "amazon_rawc",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "OPTIMIZED_IMAGE",
            "OPEN_STORAGE",
            "... 8 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": false,
          "isWormSupported": false,
          "cloudAttributes": {
            "providerId": "amazon",
            "needTokenRenew": "<masked>",
            "serviceEndpoint": "https://host-34",
            "compressionEnabled": true,
            "serverSideEncryptionEnabled": false,
            "objectSizeMegabytes": 16,
            "readBufferSizeBytes": 419430400,
            "writeBufferSizeBytes": 419430400,
            "urlAccessStyle": "VIRTUAL_STYLE",
            "offlineTransferDetails": {
              "offlineTransferMode": "NONE"
            },
            "storageClass": "ONEZONE_IA",
            "s3RegionDetails": [
              {
                "serviceHost": "host-34",
                "regionName": "US East (N. Virginia)",
                "regionId": "us-east-1"
              }
            ],
            "sslDetails": {
              "useSSLMode": "DATA",
              "checkCertificateRevocation": "<masked>",
              "httpPort": 80,
              "httpsPort": 443
            },
            "curlDetails": {
              "curlLoggingEnabled": false,
              "curlTimeOutSeconds": 900,
              "curlConnectionTimeOutSeconds": 300
            },
            "proxyServerEnabled": false,
            "cloudCredentials": "<masked>",
            "sourceKind": false
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/amazon_rawc:primary-01-cloud-backup"
          }
        }
      },
      {
        "type": "storageServer",
        "id": "PureDisk:primary-01",
        "attributes": {
          "name": "primary-01",
          "storageCategory": "MSDP",
          "sType": "PureDisk",
          "nbuHostVersion": "10.2",
          "additionalMediaServersDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "encryptionEnabled": false,
          "kmsEnabled": false,
          "storageServerState": "UP",
          "storageServerCapabilities": [
            "MODEL",
            "SRV_EVSYNC",
            "OPTIMIZED_IMAGE",
            "... 12 more"
          ],
          "isSnapshotSupported": false,
          "isAcceleratorSupported": true,
          "isAIRSupported": true,
          "isWormSupported": true,
          "storageUnits": [
            "storage-unit-02",
            "storage-unit-01"
          ],
          "msdpAttributes": {
            "storagePath": "/msdp/data",
            "spaLogPath": "/msdp/data/log",
            "deduplicationDBPath": "/msdp/catalog",
            "specificNetworkInterface": "primary-01",
            "spaLogRetention": 90,
            "verboseLevel": 3,
            "fipsEnabled": false,
            "storagePoolDetails": {
              "rawSizeBytes": 8686141859430,
              "reservedSpaceBytes": 352616815001,
              "sizeBytes": 8356288371097,
              "usedSpaceBytes": 69900592742,
              "availableSpaceBytes": 8246337208320
            },
            "catalogLogicalSizeBytes": 116,
            "catalogFilesCount": 2,
            "deduplicationRatioPercentage": 0.0,
            "extendedCapabilities": [
              "EVENTS_V1",
              "DIRECT_REP",
              "FAST_DELETE",
              "... 32 more"
            ],
            "availDiskspace": 7806532557209,
            "defaultCloudCacheCapacity": 1091995435008,
            "requestCloudCacheCapacity": 1091995435008,
            "maxRequestCloudCacheCapacity": 6267216278323
          },
          "extendedCapabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 32 more"
          ],
          "kmsKeyGroupName": " "
        },
        "relationships": {
          "universalShareStorage": {
            "links": {
              "related": {
                "href": "/storage/storage-servers/PureDisk:primary-01/universal-shares"
              }
            },
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-servers/PureDisk:primary-01"
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
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-servers?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_storage_unit_replication_relationships`

GET /storage/storage-units/{storageUnitName}/replication-relationships

```python
nbu.raw.storage.list_storage_unit_replication_relationships('storage-unit-01')
```

**On the wire**

- `GET /storage/storage-units/storage-unit-01/replication-relationships` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/storage/storage-units/storage-unit-01/replication-relationships?page%5Boffset%5D=-100&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units/storage-unit-01/replication-relationships?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units/storage-unit-01/replication-relationships?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

## `list_storage_units` - GET /storage/storage-units

```python
nbu.raw.storage.list_storage_units()
```

**On the wire**

- `GET /storage/storage-units` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "storageUnit",
        "id": "storage-unit-01",
        "attributes": {
          "name": "storage-unit-01",
          "storageType": "Disk",
          "storageSubType": "DiskPool",
          "storageServerType": "PureDisk",
          "storageCategory": "MSDP",
          "okOnRoot": false,
          "stageData": false,
          "useAnyAvailableMediaServer": false,
          "accelerator": true,
          "replicationCapable": false,
          "replicationSourceCapable": false,
          "replicationTargetCapable": false,
          "snapshot": false,
          "mirror": false,
          "independent": false,
          "primary": false,
          "instantAccessEnabled": false,
          "isCloudSTU": true,
          "freeCapacityBytes": 9007192007104915,
          "totalCapacityBytes": 9007199254740992,
          "usedCapacityBytes": 7247636077,
          "mediaServerDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "maxFragmentSizeMegabytes": 51200,
          "maxConcurrentJobs": 4,
          "onDemandOnly": false,
          "wormCapable": false,
          "useWorm": false,
          "capabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 28 more"
          ],
          "highWaterMark": 0,
          "lowWaterMark": 0,
          "robotType": "NOT_ROBOTIC",
          "robotNumber": -1,
          "multiplexing": 0,
          "enableBlockSharing": true,
          "transferThrottle": 0,
          "fileSystemExport": true
        },
        "relationships": {
          "diskPool": {
            "links": {
              "related": {
                "href": "/netbackup/storage/disk-pools/"
              }
            },
            "data": {
              "type": "diskPool",
              "id": "PureDisk:disk-pool-02"
            }
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-units/storage-unit-01"
          }
        }
      },
      {
        "type": "storageUnit",
        "id": "storage-unit-02",
        "attributes": {
          "name": "storage-unit-02",
          "storageType": "Disk",
          "storageSubType": "DiskPool",
          "storageServerType": "PureDisk",
          "storageCategory": "MSDP",
          "okOnRoot": false,
          "stageData": false,
          "useAnyAvailableMediaServer": false,
          "accelerator": true,
          "replicationCapable": false,
          "replicationSourceCapable": false,
          "replicationTargetCapable": false,
          "snapshot": false,
          "mirror": false,
          "independent": false,
          "primary": false,
          "instantAccessEnabled": true,
          "isCloudSTU": false,
          "freeCapacityBytes": 8271525391360,
          "totalCapacityBytes": 8341450185728,
          "usedCapacityBytes": 69924794368,
          "mediaServerDetails": [
            {
              "name": "primary-01",
              "operatingSystem": "Linux",
              "netbackupVersion": "10.2"
            }
          ],
          "maxFragmentSizeMegabytes": 51200,
          "maxConcurrentJobs": 24,
          "onDemandOnly": true,
          "wormCapable": false,
          "useWorm": false,
          "capabilities": [
            "EVENTS_V1",
            "DIRECT_REP",
            "FAST_DELETE",
            "... 32 more"
          ],
          "highWaterMark": 0,
          "lowWaterMark": 0,
          "robotType": "NOT_ROBOTIC",
          "robotNumber": -1,
          "multiplexing": 0,
          "enableBlockSharing": true,
          "transferThrottle": 0,
          "fileSystemExport": true
        },
        "relationships": {
          "diskPool": {
            "links": {
              "related": {
                "href": "/netbackup/storage/disk-pools/"
              }
            },
            "data": {
              "type": "diskPool",
              "id": "PureDisk:disk-pool-01"
            }
          }
        },
        "links": {
          "self": {
            "href": "/netbackup/storage/storage-units/storage-unit-02"
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
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

## `list_target_storage_servers` - GET /storage/target-storage-servers

```python
nbu.raw.storage.list_target_storage_servers()
```

**On the wire**

- `GET /storage/target-storage-servers` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": []
  }
  ```

  </details>
