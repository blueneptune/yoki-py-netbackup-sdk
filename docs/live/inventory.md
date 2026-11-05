# Policies, images, hosts, storage, assets

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## Every policy: name, type, active or not

```python
policies = record.result(nbu.policies.list())
assert all("policyName" in p or "id" in p for p in policies)
```

**On the wire**

- `GET /config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.06 s)

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
      "... 8 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 11,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
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
    },
    "id": "policy-01"
  },
  {
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
    },
    "id": "policy-02"
  },
  {
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
    },
    "id": "policy-03"
  },
  "... 8 more"
]
```

## One policy in full: its clients, schedules and backup selections

Read in NetBackup's generic schema (the client sends
`X-NetBackup-Policy-Use-Generic-Schema: true`), which has one shape for
every policy type.

```python
policies = nbu.policies.list()
if not policies:
    return
name = policies[0].get("policyName") or policies[0]["id"]
policy = record.result(nbu.policies.get(name))
assert policy is not None
```

**On the wire**

- `GET /config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.05 s)

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
      "... 8 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 11,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/config/policies?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=policyName"
      }
    }
  }
  ```

  </details>

- `GET /config/policies/policy-01` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "policy-01",
      "attributes": {
        "policy": {
          "policyName": "policy-01",
          "policyType": "Standard",
          "policyAttributes": {
            "active": true,
            "alternateClientHostname": null,
            "applicationConsistent": true,
            "applicationDiscovery": false,
            "applicationProtection": [],
            "archivedRedoLogOptions": null,
            "autoManagedLabel": null,
            "autoManagedType": 0,
            "backupFileNameFormatOverrides": {
              "archivedRedoLogs": null,
              "controlFile": null,
              "datafiles": null,
              "fastRecoveryArea": null
            },
            "backupHost": null,
            "backupHostPool": null,
            "backupSelectionType": "Clients",
            "backupSetIdentifier": null,
            "blockIncremental": false,
            "checkpointIntervalMinutes": null,
            "clientCompress": false,
            "clientEncrypt": false,
            "clientType": "Clients",
            "cloudProvider": null,
            "cloudProviderAttributes": null,
            "collectBareMetalRestoreInfo": false,
            "collectTrueImageRestoreInfo": "Off",
            "crossMountPoints": false,
            "dataClassification": null,
            "dataGuardOption": null,
            "dataMoverMachine": null,
            "databaseBackupShareOptions": null,
            "databaseOptions": null,
            "datafileCopyTag": null,
            "deploymentCertSource": null,
            "deploymentInstallable": null,
            "deploymentLimitJobs": 0,
            "deploymentMasterServer": null,
            "deploymentMediaServer": null,
            "deploymentOptions": null,
            "deploymentUnixStageLoc": null,
            "deploymentUseExistingCerts": false,
            "deploymentWinStageLoc": null,
            "disableClientSideDeduplication": false,
            "discoveryLifetime": 0,
            "dynamicMultiStreaming": false,
            "effectiveDateUTC": "2022-08-14T04:53:51Z",
            "exchangeDatabaseBackupSource": "Off",
            "exchangeServerList": [],
            "followNFSMounts": false,
            "granularRecovery": false,
            "hypervServer": null,
            "jobLimit": 0,
            "keyword": null,
            "maxFilesInBatch": 300,
            "maxStreamsPerVolume": 4,
            "maximumLimits": null,
            "mediaOwner": "*ANY*",
            "multipleStorage": null,
            "multipleStorageList": null,
            "offhostBackup": false,
            "offlineDatabaseBackup": null,
            "optimizedBackup": false,
            "parallelStreams": null,
            "priority": 0,
            "readOnlyTablespaceOptions": null,
            "retainSnapshot": false,
            "secondarySnapshotMethodArgs": null,
            "skipOfflineDatafiles": null,
            "snapshotBackup": false,
            "snapshotFreeBackupInfo": null,
            "snapshotMethod": null,
            "snapshotMethodArgs": null,
            "storage": "1M_primary-01_DS3",
            "storageIsSLP": true,
            "transactionLogOptions": null,
            "unixEcaCertPath": null,
            "unixEcaCrlCheckLevel": null,
            "unixEcaCrlPath": null,
            "unixEcaKeyPassphrasefile": null,
            "unixEcaPrivateKeyPath": null,
            "unixEcaTrustStorePath": null,
            "useAccelerator": false,
            "useBackupHostPool": false,
            "useMultipleDataStreams": false,
            "useReplicationDirector": false,
            "useVendorChangeTracking": false,
            "useVirtualMachine": 0,
            "volumeAccessProtocol": 5,
            "volumePool": "NetBackup",
            "winEcaCertPath": null,
            "winEcaCertStore": null,
            "winEcaCrlCheckLevel": null,
            "winEcaCrlPath": null,
            "winEcaKeyPassphrasefile": null,
            "winEcaPrivateKeyPath": null,
            "winEcaTrustStorePath": null
          },
          "clients": [
            {
              "databaseName": null,
              "hardware": "Linux",
              "hostName": "primary-01",
              "instanceGroup": null,
              "instanceName": null,
              "availabilityGroup": null,
              "groupID": null,
              "cluster": null,
              "dbid": null,
              "clientId": null,
              "dbUniqueName": null,
              "OS": "RedHat2.6.32",
              "osNameAndHardware": null,
              "nasVendor": null,
              "headName": null,
              "arrayName": null
            }
          ],
          "schedules": [
            {
              "acceleratorForcedRescan": false,
              "backupCopies": {
                "copies": [
                  {
                    "failStrategy": null,
                    "mediaOwner": null,
                    "retentionLevel": 1,
                    "retentionPeriod": {
                      "value": 2,
                      "unit": "WEEKS"
                    },
                    "storage": null,
                    "volumePool": null
                  }
                ],
                "priority": -1
              },
              "backupType": "Full Backup",
              "deploymentWindow": null,
              "excludeDates": {
                "lastDayOfMonth": false,
                "recurringDaysOfMonth": [],
                "recurringDaysOfWeek": [],
                "specificDates": []
              },
              "frequencySeconds": 604800,
              "includeDates": {
                "lastDayOfMonth": false,
                "recurringDaysOfMonth": [],
                "recurringDaysOfWeek": [],
                "specificDates": []
              },
              "mediaMultiplexing": 1,
              "retriesAllowedAfterRunDay": false,
              "scheduleName": "full",
              "scheduleType": "Frequency",
              "snapshotOnly": false,
              "startWindow": [
                {
                  "dayOfWeek": 1,
                  "startSeconds": 0,
                  "durationSeconds": 0
                },
                {
                  "dayOfWeek": 2,
                  "startSeconds": 0,
                  "durationSeconds": 0
                },
                {
                  "dayOfWeek": 3,
                  "startSeconds": 0,
                  "durationSeconds": 0
                },
                "... 4 more"
              ],
              "storageIsSLP": false,
              "syntheticBackup": false
            }
          ],
          "backupSelections": {
            "selections": [
              "ALL_LOCAL_DRIVES"
            ]
          },
          "excludeSelections": {
            "selections": []
          },
          "catDRInfo": null
        }
      },
      "links": {
        "self": {
          "href": "/config/policies/policy-01"
        }
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
{
  "policy": {
    "policyName": "policy-01",
    "policyType": "Standard",
    "policyAttributes": {
      "active": true,
      "alternateClientHostname": null,
      "applicationConsistent": true,
      "applicationDiscovery": false,
      "applicationProtection": [],
      "archivedRedoLogOptions": null,
      "autoManagedLabel": null,
      "autoManagedType": 0,
      "backupFileNameFormatOverrides": {
        "archivedRedoLogs": null,
        "controlFile": null,
        "datafiles": null,
        "fastRecoveryArea": null
      },
      "backupHost": null,
      "backupHostPool": null,
      "backupSelectionType": "Clients",
      "backupSetIdentifier": null,
      "blockIncremental": false,
      "checkpointIntervalMinutes": null,
      "clientCompress": false,
      "clientEncrypt": false,
      "clientType": "Clients",
      "cloudProvider": null,
      "cloudProviderAttributes": null,
      "collectBareMetalRestoreInfo": false,
      "collectTrueImageRestoreInfo": "Off",
      "crossMountPoints": false,
      "dataClassification": null,
      "dataGuardOption": null,
      "dataMoverMachine": null,
      "databaseBackupShareOptions": null,
      "databaseOptions": null,
      "datafileCopyTag": null,
      "deploymentCertSource": null,
      "deploymentInstallable": null,
      "deploymentLimitJobs": 0,
      "deploymentMasterServer": null,
      "deploymentMediaServer": null,
      "deploymentOptions": null,
      "deploymentUnixStageLoc": null,
      "deploymentUseExistingCerts": false,
      "deploymentWinStageLoc": null,
      "disableClientSideDeduplication": false,
      "discoveryLifetime": 0,
      "dynamicMultiStreaming": false,
      "effectiveDateUTC": "2022-08-14T04:53:51Z",
      "exchangeDatabaseBackupSource": "Off",
      "exchangeServerList": [],
      "followNFSMounts": false,
      "granularRecovery": false,
      "hypervServer": null,
      "jobLimit": 0,
      "keyword": null,
      "maxFilesInBatch": 300,
      "maxStreamsPerVolume": 4,
      "maximumLimits": null,
      "mediaOwner": "*ANY*",
      "multipleStorage": null,
      "multipleStorageList": null,
      "offhostBackup": false,
      "offlineDatabaseBackup": null,
      "optimizedBackup": false,
      "parallelStreams": null,
      "priority": 0,
      "readOnlyTablespaceOptions": null,
      "retainSnapshot": false,
      "secondarySnapshotMethodArgs": null,
      "skipOfflineDatafiles": null,
      "snapshotBackup": false,
      "snapshotFreeBackupInfo": null,
      "snapshotMethod": null,
      "snapshotMethodArgs": null,
      "storage": "1M_primary-01_DS3",
      "storageIsSLP": true,
      "transactionLogOptions": null,
      "unixEcaCertPath": null,
      "unixEcaCrlCheckLevel": null,
      "unixEcaCrlPath": null,
      "unixEcaKeyPassphrasefile": null,
      "unixEcaPrivateKeyPath": null,
      "unixEcaTrustStorePath": null,
      "useAccelerator": false,
      "useBackupHostPool": false,
      "useMultipleDataStreams": false,
      "useReplicationDirector": false,
      "useVendorChangeTracking": false,
      "useVirtualMachine": 0,
      "volumeAccessProtocol": 5,
      "volumePool": "NetBackup",
      "winEcaCertPath": null,
      "winEcaCertStore": null,
      "winEcaCrlCheckLevel": null,
      "winEcaCrlPath": null,
      "winEcaKeyPassphrasefile": null,
      "winEcaPrivateKeyPath": null,
      "winEcaTrustStorePath": null
    },
    "clients": [
      {
        "databaseName": null,
        "hardware": "Linux",
        "hostName": "primary-01",
        "instanceGroup": null,
        "instanceName": null,
        "availabilityGroup": null,
        "groupID": null,
        "cluster": null,
        "dbid": null,
        "clientId": null,
        "dbUniqueName": null,
        "OS": "RedHat2.6.32",
        "osNameAndHardware": null,
        "nasVendor": null,
        "headName": null,
        "arrayName": null
      }
    ],
    "schedules": [
      {
        "acceleratorForcedRescan": false,
        "backupCopies": {
          "copies": [
            {
              "failStrategy": null,
              "mediaOwner": null,
              "retentionLevel": 1,
              "retentionPeriod": {
                "value": 2,
                "unit": "WEEKS"
              },
              "storage": null,
              "volumePool": null
            }
          ],
          "priority": -1
        },
        "backupType": "Full Backup",
        "deploymentWindow": null,
        "excludeDates": {
          "lastDayOfMonth": false,
          "recurringDaysOfMonth": [],
          "recurringDaysOfWeek": [],
          "specificDates": []
        },
        "frequencySeconds": 604800,
        "includeDates": {
          "lastDayOfMonth": false,
          "recurringDaysOfMonth": [],
          "recurringDaysOfWeek": [],
          "specificDates": []
        },
        "mediaMultiplexing": 1,
        "retriesAllowedAfterRunDay": false,
        "scheduleName": "full",
        "scheduleType": "Frequency",
        "snapshotOnly": false,
        "startWindow": [
          {
            "dayOfWeek": 1,
            "startSeconds": 0,
            "durationSeconds": 0
          },
          {
            "dayOfWeek": 2,
            "startSeconds": 0,
            "durationSeconds": 0
          },
          {
            "dayOfWeek": 3,
            "startSeconds": 0,
            "durationSeconds": 0
          },
          "... 4 more"
        ],
        "storageIsSLP": false,
        "syntheticBackup": false
      }
    ],
    "backupSelections": {
      "selections": [
        "ALL_LOCAL_DRIVES"
      ]
    },
    "excludeSelections": {
      "selections": []
    },
    "catDRInfo": null
  },
  "id": "policy-01"
}
```

## A policy that does not exist gives `None`

```python
assert nbu.policies.get("bltlive-no-such-policy") is None
```

**On the wire**

- `GET /config/policies/bltlive-no-such-policy` -> **404** (0.06 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 230,
    "errorMessage": "the specified policy does not exist in the configuration database",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": []
  }
  ```

  </details>

## Backup images from the last 30 days, newest first

```python
since = datetime.now(UTC) - timedelta(days=30)
first = next(nbu.images.iter_pages(backed_up_after=since), [])
record.result(first[:3])
```

**On the wire**

- `GET /catalog/images?filter=backupTime+ge+2026-10-06T15%3A51%3A56.240Z&sort=-backupTime&page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [],
    "meta": {
      "pagination": {
        "offset": 0,
        "count": 0,
        "limit": 100
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[]
```

## The hosts the primary knows: itself, media servers, clients

Not a JSON:API listing like the rest: `{"hosts": [...]}`, all at once.

```python
hosts = record.result(nbu.hosts.list())
assert hosts and all("hostName" in h for h in hosts)
```

**On the wire**

- `GET /config/hosts` -> **200** (0.07 s)

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

**What the SDK gave back**

```json
[
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
```

## Storage units: where a policy's backups are written

```python
record.result(nbu.storage.units())
```

**On the wire**

- `GET /storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.14 s)

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
          "freeCapacityBytes": 8271525153792,
          "totalCapacityBytes": 8341450185728,
          "usedCapacityBytes": 69925031936,
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
        "limit": 100,
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/storage-units?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
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
    "fileSystemExport": true,
    "id": "storage-unit-01"
  },
  {
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
    "freeCapacityBytes": 8271525153792,
    "totalCapacityBytes": 8341450185728,
    "usedCapacityBytes": 69925031936,
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
    "fileSystemExport": true,
    "id": "storage-unit-02"
  }
]
```

## Disk pools, with their capacity and use

```python
record.result(nbu.storage.disk_pools())
```

**On the wire**

- `GET /storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.12 s)

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
              "freeSizeBytes": 8271525153792,
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
          "availableSpaceBytes": 8271525153792,
          "usedCapacityBytes": 69925031936,
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
        "limit": 100,
        "count": 2,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/storage/disk-pools?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
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
        "freeSizeBytes": 8271525153792,
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
    "availableSpaceBytes": 8271525153792,
    "usedCapacityBytes": 69925031936,
    "wormCapable": false,
    "readOnly": false,
    "mediaServersCount": 1,
    "id": "PureDisk:disk-pool-01"
  },
  {
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
    "mediaServersCount": 1,
    "id": "PureDisk:disk-pool-02"
  }
]
```

## Virtual machines NetBackup has discovered in vCenter

```python
assets = nbu.assets.workload("vmware")
record.result(assets[:3])
```

**On the wire**

- `GET /asset-service/workloads/vmware/assets?page%5Boffset%5D=0&page%5Blimit%5D=100` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "vmwareAsset",
        "id": "efbd8f9c-4f40-47a2-a9c3-99d360d3231a",
        "attributes": {
          "assetType": "vm",
          "commonAssetAttributes": {
            "displayName": "asset-01",
            "masters": [
              {
                "hostName": "primary-01",
                "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
              }
            ],
            "providerGeneratedId": "VMware_5010c433-438e-08ca-dae2-a75d31d09127",
            "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|5010c433-438e-08ca-dae2-a75d31d09127|",
            "workloadFamily": "Virtualization",
            "workloadType": "VMware",
            "protectionCapabilities": {
              "isProtectable": "YES",
              "isRecoverable": "YES"
            },
            "detection": {
              "detectionMethod": "DISCOVERY",
              "discoveryHosts": [
                {
                  "host": {
                    "hostName": "primary-01",
                    "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
                  },
                  "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
                  "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
                }
              ],
              "firstDiscoveredTime": "2026-11-04T22:15:53.429Z",
              "lastDiscoveredTime": "2026-11-05T14:16:48.309Z"
            }
          },
          "cluster": "cluster-01",
          "connectionState": "connected",
          "datacenter": "datacenter-01",
          "datastore": [
            {
              "datastoreName": "datastore-01"
            }
          ],
          "guestId": "rockylinux_64Guest",
          "host": "host-06",
          "hostPath": "cluster-01",
          "instanceUuid": "5010c433-438e-08ca-dae2-a75d31d09127",
          "mor": "vm-64",
          "network": [
            {
              "networkName": "VM Network"
            }
          ],
          "nicIpAddresses": "",
          "path": "cluster-01",
          "powerState": "poweredOn",
          "snapshotDir": "datastore-01",
          "tag": [],
          "template": "false",
          "uuid": "42108b5f-c1f4-8acd-0e00-8c7a6a269182",
          "vCenter": "host-05",
          "vCenterVersion": "8.0.3",
          "version": "vmx-20",
          "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-06",
          "vmFolder": "vm",
          "vmxDatastore": "datastore-01",
          "vmxDatastoreType": "VMFS",
          "vmxDir": "datastore-01",
          "extendedAttributes": []
        },
        "relationships": {
          "assetGroups": {
            "meta": {
              "type": "within"
            },
            "links": {
              "related": {
                "href": "/asset-service/workloads/vmware/assets/efbd8f9c-4f40-47a2-a9c3-99d360d3231a/asset-groups"
              }
            },
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/vmware/assets/efbd8f9c-4f40-47a2-a9c3-99d360d3231a"
          }
        }
      },
      {
        "type": "vmwareAsset",
        "id": "67ae7b5d-1a87-42a7-b8a6-d23121c5b035",
        "attributes": {
          "assetType": "vm",
          "commonAssetAttributes": {
            "displayName": "asset-02",
            "masters": [
              {
                "hostName": "primary-01",
                "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
              }
            ],
            "providerGeneratedId": "VMware_50107871-1a22-9132-0369-a58006e497d0",
            "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|50107871-1a22-9132-0369-a58006e497d0|",
            "workloadFamily": "Virtualization",
            "workloadType": "VMware",
            "protectionCapabilities": {
              "isProtectable": "YES",
              "isRecoverable": "YES"
            },
            "detection": {
              "detectionMethod": "DISCOVERY",
              "discoveryHosts": [
                {
                  "host": {
                    "hostName": "primary-01",
                    "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
                  },
                  "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
                  "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
                }
              ],
              "firstDiscoveredTime": "2026-11-02T14:13:21.091Z",
              "lastDiscoveredTime": "2026-11-05T14:16:48.300Z"
            }
          },
          "cluster": "cluster-01",
          "connectionState": "connected",
          "datacenter": "datacenter-01",
          "datastore": [
            {
              "datastoreName": "datastore-02"
            }
          ],
          "dnsName": "asset-02",
          "guestId": "windows9Server64Guest",
          "host": "host-06",
          "hostName": "host-07",
          "hostPath": "cluster-01",
          "instanceUuid": "50107871-1a22-9132-0369-a58006e497d0",
          "ipAddress": "192.0.2.2",
          "mor": "vm-62",
          "network": [
            {
              "networkName": "VM Network"
            }
          ],
          "nicIpAddresses": "(192.0.2.2)",
          "path": "cluster-01",
          "powerState": "poweredOn",
          "snapshotDir": "datastore-02",
          "tag": [],
          "template": "false",
          "uuid": "42104de1-b1a0-c2d5-b016-1e17cabaa3f7",
          "vCenter": "host-05",
          "vCenterVersion": "8.0.3",
          "version": "vmx-13",
          "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-06",
          "vmFolder": "vm",
          "vmxDatastore": "datastore-02",
          "vmxDatastoreType": "VMFS",
          "vmxDir": "datastore-02",
          "extendedAttributes": []
        },
        "relationships": {
          "assetGroups": {
            "meta": {
              "type": "within"
            },
            "links": {
              "related": {
                "href": "/asset-service/workloads/vmware/assets/67ae7b5d-1a87-42a7-b8a6-d23121c5b035/asset-groups"
              }
            },
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/vmware/assets/67ae7b5d-1a87-42a7-b8a6-d23121c5b035"
          }
        }
      },
      {
        "type": "vmwareAsset",
        "id": "8eee6f6f-4e78-49f3-b500-cbc0c13b9c3f",
        "attributes": {
          "assetType": "vm",
          "commonAssetAttributes": {
            "displayName": "asset-03",
            "masters": [
              {
                "hostName": "primary-01",
                "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
              }
            ],
            "providerGeneratedId": "VMware_50105e9e-71f2-0a6b-0785-907a629889f2",
            "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|50105e9e-71f2-0a6b-0785-907a629889f2|",
            "workloadFamily": "Virtualization",
            "workloadType": "VMware",
            "protectionCapabilities": {
              "isProtectable": "YES",
              "isRecoverable": "YES"
            },
            "detection": {
              "detectionMethod": "DISCOVERY",
              "discoveryHosts": [
                {
                  "host": {
                    "hostName": "primary-01",
                    "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
                  },
                  "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
                  "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
                }
              ],
              "firstDiscoveredTime": "2026-11-02T14:13:21.073Z",
              "lastDiscoveredTime": "2026-11-05T14:16:48.291Z"
            }
          },
          "annotation": "host-16 Cluster Service VM is deployed from an OVA with a minimal installed profile of PhotonOS. host-16 Cluster Service manages the resources, power state and availability of these VMs. host-16 Cluster Service VMs are required for maintaining the health and availability of host-16 Cluster Service. Any impact on the power state or resources of these VMs might degrade the health of the host-16 Clus... (470 characters)",
          "cluster": "cluster-01",
          "connectionState": "connected",
          "datacenter": "datacenter-01",
          "datastore": [
            {
              "datastoreName": "datastore-03"
            }
          ],
          "dnsName": "None",
          "guestId": "other26xLinux64Guest",
          "host": "host-08",
          "hostPath": "cluster-01",
          "instanceUuid": "50105e9e-71f2-0a6b-0785-907a629889f2",
          "mor": "vm-61",
          "network": [],
          "nicIpAddresses": "",
          "path": "cluster-01",
          "powerState": "poweredOn",
          "snapshotDir": "datastore-03",
          "tag": [],
          "template": "false",
          "uuid": "42104375-e3c1-3a18-8a2b-1b77b4965d3d",
          "vCenter": "host-05",
          "vCenterVersion": "8.0.3",
          "version": "vmx-11",
          "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-08",
          "vmFolder": "vm\\vCLS",
          "vmxDatastore": "datastore-03",
          "vmxDatastoreType": "VMFS",
          "vmxDir": "datastore-03",
          "extendedAttributes": []
        },
        "relationships": {
          "assetGroups": {
            "meta": {
              "type": "within"
            },
            "links": {
              "related": {
                "href": "/asset-service/workloads/vmware/assets/8eee6f6f-4e78-49f3-b500-cbc0c13b9c3f/asset-groups"
              }
            },
            "data": []
          }
        },
        "links": {
          "self": {
            "href": "/asset-service/workloads/vmware/assets/8eee6f6f-4e78-49f3-b500-cbc0c13b9c3f"
          }
        }
      },
      "... 12 more"
    ],
    "meta": {
      "pagination": {
        "offset": 0,
        "limit": 100,
        "hasNext": false,
        "first": 0
      }
    },
    "links": {
      "self": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/vmware/assets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/asset-service/workloads/vmware/assets?page%5Boffset%5D=0&page%5Blimit%5D=100"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "assetType": "vm",
    "commonAssetAttributes": {
      "displayName": "asset-01",
      "masters": [
        {
          "hostName": "primary-01",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
        }
      ],
      "providerGeneratedId": "VMware_5010c433-438e-08ca-dae2-a75d31d09127",
      "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|5010c433-438e-08ca-dae2-a75d31d09127|",
      "workloadFamily": "Virtualization",
      "workloadType": "VMware",
      "protectionCapabilities": {
        "isProtectable": "YES",
        "isRecoverable": "YES"
      },
      "detection": {
        "detectionMethod": "DISCOVERY",
        "discoveryHosts": [
          {
            "host": {
              "hostName": "primary-01",
              "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
            },
            "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
            "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
          }
        ],
        "firstDiscoveredTime": "2026-11-04T22:15:53.429Z",
        "lastDiscoveredTime": "2026-11-05T14:16:48.309Z"
      }
    },
    "cluster": "cluster-01",
    "connectionState": "connected",
    "datacenter": "datacenter-01",
    "datastore": [
      {
        "datastoreName": "datastore-01"
      }
    ],
    "guestId": "rockylinux_64Guest",
    "host": "host-06",
    "hostPath": "cluster-01",
    "instanceUuid": "5010c433-438e-08ca-dae2-a75d31d09127",
    "mor": "vm-64",
    "network": [
      {
        "networkName": "VM Network"
      }
    ],
    "nicIpAddresses": "",
    "path": "cluster-01",
    "powerState": "poweredOn",
    "snapshotDir": "datastore-01",
    "tag": [],
    "template": "false",
    "uuid": "42108b5f-c1f4-8acd-0e00-8c7a6a269182",
    "vCenter": "host-05",
    "vCenterVersion": "8.0.3",
    "version": "vmx-20",
    "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-06",
    "vmFolder": "vm",
    "vmxDatastore": "datastore-01",
    "vmxDatastoreType": "VMFS",
    "vmxDir": "datastore-01",
    "extendedAttributes": [],
    "id": "efbd8f9c-4f40-47a2-a9c3-99d360d3231a"
  },
  {
    "assetType": "vm",
    "commonAssetAttributes": {
      "displayName": "asset-02",
      "masters": [
        {
          "hostName": "primary-01",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
        }
      ],
      "providerGeneratedId": "VMware_50107871-1a22-9132-0369-a58006e497d0",
      "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|50107871-1a22-9132-0369-a58006e497d0|",
      "workloadFamily": "Virtualization",
      "workloadType": "VMware",
      "protectionCapabilities": {
        "isProtectable": "YES",
        "isRecoverable": "YES"
      },
      "detection": {
        "detectionMethod": "DISCOVERY",
        "discoveryHosts": [
          {
            "host": {
              "hostName": "primary-01",
              "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
            },
            "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
            "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
          }
        ],
        "firstDiscoveredTime": "2026-11-02T14:13:21.091Z",
        "lastDiscoveredTime": "2026-11-05T14:16:48.300Z"
      }
    },
    "cluster": "cluster-01",
    "connectionState": "connected",
    "datacenter": "datacenter-01",
    "datastore": [
      {
        "datastoreName": "datastore-02"
      }
    ],
    "dnsName": "asset-02",
    "guestId": "windows9Server64Guest",
    "host": "host-06",
    "hostName": "host-07",
    "hostPath": "cluster-01",
    "instanceUuid": "50107871-1a22-9132-0369-a58006e497d0",
    "ipAddress": "192.0.2.2",
    "mor": "vm-62",
    "network": [
      {
        "networkName": "VM Network"
      }
    ],
    "nicIpAddresses": "(192.0.2.2)",
    "path": "cluster-01",
    "powerState": "poweredOn",
    "snapshotDir": "datastore-02",
    "tag": [],
    "template": "false",
    "uuid": "42104de1-b1a0-c2d5-b016-1e17cabaa3f7",
    "vCenter": "host-05",
    "vCenterVersion": "8.0.3",
    "version": "vmx-13",
    "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-06",
    "vmFolder": "vm",
    "vmxDatastore": "datastore-02",
    "vmxDatastoreType": "VMFS",
    "vmxDir": "datastore-02",
    "extendedAttributes": [],
    "id": "67ae7b5d-1a87-42a7-b8a6-d23121c5b035"
  },
  {
    "assetType": "vm",
    "commonAssetAttributes": {
      "displayName": "asset-03",
      "masters": [
        {
          "hostName": "primary-01",
          "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
        }
      ],
      "providerGeneratedId": "VMware_50105e9e-71f2-0a6b-0785-907a629889f2",
      "accessControlId": "|ASSETS|VMWARE|VCENTER|host-05|VM|50105e9e-71f2-0a6b-0785-907a629889f2|",
      "workloadFamily": "Virtualization",
      "workloadType": "VMware",
      "protectionCapabilities": {
        "isProtectable": "YES",
        "isRecoverable": "YES"
      },
      "detection": {
        "detectionMethod": "DISCOVERY",
        "discoveryHosts": [
          {
            "host": {
              "hostName": "primary-01",
              "uuid": "f151f48b-17c5-4e7e-8a6b-1054db540384"
            },
            "firstDiscoveredTime": "2024-01-21T17:53:49.995Z",
            "lastDiscoveredTime": "2026-11-05T14:16:48.310Z"
          }
        ],
        "firstDiscoveredTime": "2026-11-02T14:13:21.073Z",
        "lastDiscoveredTime": "2026-11-05T14:16:48.291Z"
      }
    },
    "annotation": "host-16 Cluster Service VM is deployed from an OVA with a minimal installed profile of PhotonOS. host-16 Cluster Service manages the resources, power state and availability of these VMs. host-16 Cluster Service VMs are required for maintaining the health and availability of host-16 Cluster Service. Any impact on the power state or resources of these VMs might degrade the health of the host-16 Clus... (470 characters)",
    "cluster": "cluster-01",
    "connectionState": "connected",
    "datacenter": "datacenter-01",
    "datastore": [
      {
        "datastoreName": "datastore-03"
      }
    ],
    "dnsName": "None",
    "guestId": "other26xLinux64Guest",
    "host": "host-08",
    "hostPath": "cluster-01",
    "instanceUuid": "50105e9e-71f2-0a6b-0785-907a629889f2",
    "mor": "vm-61",
    "network": [],
    "nicIpAddresses": "",
    "path": "cluster-01",
    "powerState": "poweredOn",
    "snapshotDir": "datastore-03",
    "tag": [],
    "template": "false",
    "uuid": "42104375-e3c1-3a18-8a2b-1b77b4965d3d",
    "vCenter": "host-05",
    "vCenterVersion": "8.0.3",
    "version": "vmx-11",
    "vmAbsolutePath": "/host-05/datacenter-01/cluster-01/host-08",
    "vmFolder": "vm\\vCLS",
    "vmxDatastore": "datastore-03",
    "vmxDatastoreType": "VMFS",
    "vmxDir": "datastore-03",
    "extendedAttributes": [],
    "id": "8eee6f6f-4e78-49f3-b500-cbc0c13b9c3f"
  }
]
```
