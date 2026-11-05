# Changes

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## A Standard policy: create, read back, change, delete

The body is NetBackup's generic policy schema - the same shape GET
returns - wrapped as a JSON:API resource. A changed policy is sent
whole with PUT; NetBackup checks it against the version it last
gave out (the ETag) when `If-Match` is sent.

```python
name = f"{PREFIX}-std"
policy = _template(nbu, "Standard")
policy["policyName"] = name
policy["policyAttributes"]["active"] = False
policy["clients"] = []
policy["backupSelections"] = {"selections": ["/tmp/bltlive"]}
body = {"data": {"type": "policy", "id": name, "attributes": {"policy": policy}}}

nbu.raw.config.post_policies(body=body)
created = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
assert created["policyName"] == name
assert created["policyAttributes"]["active"] is False

created["policyAttributes"]["priority"] = 7
created["policyAttributes"]["keyword"] = "bltlive"
nbu.raw.config.put_policy(
    name, body={"data": {"type": "policy", "id": name, "attributes": {"policy": created}}}
)
changed = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
record.result({k: changed["policyAttributes"][k] for k in ("priority", "keyword", "active")})
assert changed["policyAttributes"]["priority"] == 7

nbu.raw.config.delete_policy(name)
with pytest.raises(NotFoundError):
    nbu.raw.config.get_policy(name)
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

- `POST /config/policies/` -> **204** (0.18 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-std",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-std",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
          "clients": [],
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
              "/tmp/bltlive"
            ]
          },
          "excludeSelections": {
            "selections": []
          },
          "catDRInfo": null
        }
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/policies/bltlive-11050645-std` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-std",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-std",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
          "clients": [],
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
              "/tmp/bltlive"
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
          "href": "/config/policies/bltlive-11050645-std"
        }
      }
    }
  }
  ```

  </details>

- `PUT /config/policies/bltlive-11050645-std` -> **204** (0.20 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-std",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-std",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
            "keyword": "bltlive",
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
            "priority": 7,
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
          "clients": [],
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
              "/tmp/bltlive"
            ]
          },
          "excludeSelections": {
            "selections": []
          },
          "catDRInfo": null
        }
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/policies/bltlive-11050645-std` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-std",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-std",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
            "keyword": "bltlive",
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
            "priority": 7,
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
          "clients": [],
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
              "/tmp/bltlive"
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
          "href": "/config/policies/bltlive-11050645-std"
        }
      }
    }
  }
  ```

  </details>

- `DELETE /config/policies/bltlive-11050645-std` -> **204** (0.14 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/policies/bltlive-11050645-std` -> **404** (0.10 s)

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

**What the SDK gave back**

```json
{
  "priority": 7,
  "keyword": "bltlive",
  "active": false
}
```

## A policy's parts on their own: add a client and a schedule, then

take them out again, without sending the whole policy.

```python
name = f"{PREFIX}-parts"
policy = _template(nbu, "Standard")
# Hardware and OS as the server already knows them from another client.
known = (policy.get("clients") or [{}])[0]
template_schedules = policy.get("schedules") or []
hardware, os_name = known.get("hardware", "Linux"), known.get("OS", "RedHat2.6.18")
policy["policyName"] = name
policy["policyAttributes"]["active"] = False
policy["clients"] = []
policy["schedules"] = []
policy["backupSelections"] = {"selections": ["/tmp/bltlive"]}
nbu.raw.config.post_policies(
    body={"data": {"type": "policy", "id": name, "attributes": {"policy": policy}}}
)
client = "bltlive-client.example.com"
nbu.raw.config.put_policy_client(
    name,
    client,
    body={
        "data": {
            "type": "client",
            "id": client,
            "attributes": {"hardware": hardware, "OS": os_name},
        }
    },
)
# A schedule as the server already has one, renamed.
if not template_schedules:
    pytest.skip("the template policy has no schedule to copy")
schedule = copy.deepcopy(template_schedules[0])
schedule["scheduleName"] = "bltlive-full"
try:
    nbu.raw.config.put_policy_schedule(
        name,
        "bltlive-full",
        body={"data": {"type": "schedule", "id": "bltlive-full", "attributes": schedule}},
    )
except SDKError as error:
    record.note(f"Adding the schedule was refused: {getattr(error, 'detail', error)}")
    raise
full = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
record.result(
    {
        "clients": [c["hostName"] for c in full["clients"]],
        "schedules": [s["scheduleName"] for s in full["schedules"]],
    }
)
assert [c["hostName"] for c in full["clients"]] == [client]
assert [s["scheduleName"] for s in full["schedules"]] == ["bltlive-full"]

nbu.raw.config.delete_policy_schedule(name, "bltlive-full")
nbu.raw.config.delete_policy_client(name, client)
empty = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
assert empty["clients"] == [] and empty["schedules"] == []
nbu.raw.config.delete_policy(name)
```

**On the wire**

- `GET /config/policies/` -> **200** (0.06 s)

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

- `POST /config/policies/` -> **204** (0.17 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-parts",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-parts",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
          "clients": [],
          "schedules": [],
          "backupSelections": {
            "selections": [
              "/tmp/bltlive"
            ]
          },
          "excludeSelections": {
            "selections": []
          },
          "catDRInfo": null
        }
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `PUT /config/policies/bltlive-11050645-parts/clients/bltlive-client.example.com` -> **201** (0.12 s)

  Sent:

  ```json
  {
    "data": {
      "type": "client",
      "id": "bltlive-client.example.com",
      "attributes": {
        "hardware": "Linux",
        "OS": "RedHat2.6.32"
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `PUT /config/policies/bltlive-11050645-parts/schedules/bltlive-full` -> **201** (0.14 s)

  Sent:

  ```json
  {
    "data": {
      "type": "schedule",
      "id": "bltlive-full",
      "attributes": {
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
        "scheduleName": "bltlive-full",
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
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/policies/bltlive-11050645-parts` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-parts",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-parts",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
              "hostName": "bltlive-client.example.com",
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
              "scheduleName": "bltlive-full",
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
              "/tmp/bltlive"
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
          "href": "/config/policies/bltlive-11050645-parts"
        }
      }
    }
  }
  ```

  </details>

- `DELETE /config/policies/bltlive-11050645-parts/schedules/bltlive-full` -> **204** (0.11 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `DELETE /config/policies/bltlive-11050645-parts/clients/bltlive-client.example.com` -> **204** (0.10 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/policies/bltlive-11050645-parts` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11050645-parts",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11050645-parts",
          "policyType": "Standard",
          "policyAttributes": {
            "active": false,
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
          "clients": [],
          "schedules": [],
          "backupSelections": {
            "selections": [
              "/tmp/bltlive"
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
          "href": "/config/policies/bltlive-11050645-parts"
        }
      }
    }
  }
  ```

  </details>

- `DELETE /config/policies/bltlive-11050645-parts` -> **204** (0.13 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

**What the SDK gave back**

```json
{
  "clients": [
    "bltlive-client.example.com"
  ],
  "schedules": [
    "bltlive-full"
  ]
}
```

## A storage lifecycle policy: create, read back, change, delete

Copied from an existing SLP, so its operations point at storage that
exists on this server.

```python
existing = nbu.raw.config.list_slps().get("data", [])
if not existing:
    pytest.skip("no SLP on the server to copy from")
source = copy.deepcopy(existing[0]["attributes"])
name = f"{PREFIX}-slp"
attributes = {
    k: v
    for k, v in source.items()
    if k in ("slpName", "duplicationPriority", "operationList", "dataClassification")
}
attributes["slpName"] = name
nbu.raw.config.post_slps(body={"data": {"type": "slp", "id": name, "attributes": attributes}})
created = nbu.raw.config.get_slp(name)["data"]["attributes"]
assert created["slpName"] == name

attributes["duplicationPriority"] = 5
nbu.raw.config.put_slp(
    name, body={"data": {"type": "slp", "id": name, "attributes": attributes}}
)
changed = nbu.raw.config.get_slp(name)["data"]["attributes"]
record.result({k: changed.get(k) for k in ("slpName", "versionNumber", "duplicationPriority")})
assert changed["duplicationPriority"] == 5

nbu.raw.config.delete_slp(name)
with pytest.raises(NotFoundError):
    nbu.raw.config.get_slp(name)
```

**On the wire**

- `GET /config/slps` -> **200** (0.09 s)

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

- `POST /config/slps` -> **201** (0.22 s)

  Sent:

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
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
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
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
      "links": {
        "self": {
          "href": "/config/slps/bltlive-11050645-slp"
        }
      }
    }
  }
  ```

  </details>

- `GET /config/slps/bltlive-11050645-slp` -> **200** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
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
              "href": "/config/slps/bltlive-11050645-slp/versions"
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
          "href": "/config/slps/bltlive-11050645-slp"
        }
      }
    }
  }
  ```

  </details>

- `PUT /config/slps/bltlive-11050645-slp` -> **200** (0.19 s)

  Sent:

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
        "duplicationPriority": 5,
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
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
        "versionNumber": 1,
        "flagValues": [],
        "active": true,
        "activationTime": "1970-01-01T00:00:00Z",
        "duplicationPriority": 5,
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
      "links": {
        "self": {
          "href": "/config/slps/bltlive-11050645-slp"
        }
      }
    }
  }
  ```

  </details>

- `GET /config/slps/bltlive-11050645-slp` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "slp",
      "id": "bltlive-11050645-slp",
      "attributes": {
        "slpName": "bltlive-11050645-slp",
        "versionNumber": 1,
        "flagValues": [],
        "active": true,
        "activationTime": "1970-01-01T00:00:00Z",
        "duplicationPriority": 5,
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
              "href": "/config/slps/bltlive-11050645-slp/versions"
            }
          },
          "data": [
            {
              "type": "version",
              "id": "0"
            },
            {
              "type": "version",
              "id": "1"
            }
          ]
        }
      },
      "links": {
        "self": {
          "href": "/config/slps/bltlive-11050645-slp"
        }
      }
    }
  }
  ```

  </details>

- `DELETE /config/slps/bltlive-11050645-slp` -> **204** (0.13 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /config/slps/bltlive-11050645-slp` -> **404** (0.11 s)

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

**What the SDK gave back**

```json
{
  "slpName": "bltlive-11050645-slp",
  "versionNumber": 1,
  "duplicationPriority": 5
}
```
