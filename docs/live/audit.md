# Audit

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## Create, change and delete a policy

The audit log then holds one record for each - the operation, the user who made it, and for the change each setting's old and new value. The create and the delete send a reason (`X-NetBackup-Audit-Reason`), which the record of what happened keeps.

NetBackup writes two records per change: one as the user starts it
("User 'x' is modifying policy 'p'"), and one per part that changed
("Attributes of Policy 'p' were modified", "Include list settings of
Policy 'p' were modified"), which hold the old and new values.
Filtered by `id gt <the last id before>` and `category eq 'POLICY'`,
so only this test's records come back (the audit log filters on id,
category, operation, userName, domainName and auditDateTime).

```python
name = f"{PREFIX}-audit"
reason = f"{PREFIX}: change CHG0000001"
before = _last_audit_id(nbu)
body = _policy(nbu, name)
nbu.raw.config.post_policies(
    body={"data": {"type": "policy", "id": name, "attributes": {"policy": body}}},
    x_net_backup_audit_reason=reason,
)
body = nbu.raw.config.get_policy(name)["data"]["attributes"]["policy"]
body["policyAttributes"]["priority"] = 9
nbu.raw.config.put_policy(
    name, body={"data": {"type": "policy", "id": name, "attributes": {"policy": body}}}
)
nbu.raw.config.delete_policy(name, x_net_backup_audit_reason=reason)

ours = [
    r
    for r in _audit_since(nbu, before, "POLICY")
    if name in [k.get("typeIdDisplayString") for k in r.get("auditKeyList") or []]
]
record.result(
    [
        {
            "operation": r.get("operation"),
            "message": r.get("message"),
            "user": (r.get("auditUserIdentity") or {}).get("userName"),
            "reason": r.get("reason"),
            "changed": [
                (a.get("attributeName"), a.get("oldValue"), a.get("newValue"))
                for a in r.get("auditRecordAttributeList") or []
            ],
        }
        for r in ours
    ]
)
operations = {r.get("operation") for r in ours}
assert {"CREATE", "MODIFY", "DELETE"} <= operations, operations
assert all((r.get("auditUserIdentity") or {}).get("userName") for r in ours)
priority = [
    a
    for r in ours
    if r.get("operation") == "MODIFY"
    for a in r.get("auditRecordAttributeList") or []
    if "priority" in str(a.get("attributeName", "")).lower()
]
assert priority and priority[0].get("newValue") == "9", priority
# Each change leaves two kinds of record: one as the user starts it
# ("User 'x' is deleting policy ..."), without the reason, and one
# for what happened ("Policy ... was deleted"), with it. A reason sent
# with the change is how a change made through blt can carry its
# change number into NetBackup's own log.
done = [r for r in ours if " was " in str(r.get("message"))]
assert {r.get("operation") for r in done} >= {"CREATE", "DELETE"}
assert all(
    r.get("reason") == reason for r in done if r.get("operation") in ("CREATE", "DELETE")
), [(r.get("operation"), r.get("reason")) for r in done]
starting = [r for r in ours if " is " in str(r.get("message"))]
assert {r.get("operation") for r in starting} >= {"CREATE", "MODIFY", "DELETE"}
```

**On the wire**

- `GET /security/auditlogs?page%5Blimit%5D=1&sort=-id` -> **200** (0.07 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3629",
        "attributes": {
          "category": "SLP",
          "operation": "DELETE",
          "messageId": 3001,
          "message": "Storage Lifecycle Policy 'bltlive-11051547-slp' was deleted.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "bltlive-11051547-slp"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "null",
              "oldValueDisplayString": "(none specified)",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "Data classification",
              "attributeId": "__UMI__3008"
            },
            {
              "oldValue": "bltlive-11051547-slp",
              "newValue": "null",
              "oldValueDisplayString": "bltlive-11051547-slp",
              "newValueDisplayString": "",
              "typeId": 1,
              "attributeName": "SLP name",
              "attributeId": "__UMI__3009"
            },
            {
              "oldValue": "2147483647",
              "newValue": "null",
              "oldValueDisplayString": "Unlimited",
              "newValueDisplayString": "",
              "typeId": 2,
              "attributeName": "Max jobs",
              "attributeId": "__UMI__3010"
            },
            "... 35 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T15:48:14.002Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3629"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "next": 1,
        "pages": 307,
        "offset": 0,
        "last": 306,
        "limit": 1,
        "count": 307,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "next": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=1&page%5Blimit%5D=1&sort=-id"
      },
      "last": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=306&page%5Blimit%5D=1&sort=-id"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=1&sort=-id"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=1&sort=-id"
      }
    }
  }
  ```

  </details>

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

- `POST /config/policies/` -> **204** (0.47 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11051551-audit",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11051551-audit",
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

- `GET /config/policies/bltlive-11051551-audit` -> **200** (0.08 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11051551-audit",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11051551-audit",
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
          "href": "/config/policies/bltlive-11051551-audit"
        }
      }
    }
  }
  ```

  </details>

- `PUT /config/policies/bltlive-11051551-audit` -> **204** (0.17 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11051551-audit",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11051551-audit",
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
            "priority": 9,
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

- `DELETE /config/policies/bltlive-11051551-audit` -> **204** (0.13 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /security/auditlogs?filter=category+eq+%27POLICY%27+and+id+gt+3629&page%5Blimit%5D=100&sort=id` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "audit",
        "id": "3630",
        "attributes": {
          "category": "POLICY",
          "operation": "CREATE",
          "messageId": 1816,
          "message": "User 'user-01' is creating policy 'bltlive-11051551-audit' of type 'Standard'.",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "user-01"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "bltlive-11051551-audit"
            },
            {
              "typeId": 1,
              "typeIdDisplayString": "Standard"
            }
          ],
          "auditRecordAttributeList": [],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "",
          "auditDateTime": "2026-11-05T15:51:27.311Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3630"
          }
        }
      },
      {
        "type": "audit",
        "id": "3631",
        "attributes": {
          "category": "POLICY",
          "operation": "CREATE",
          "messageId": 1,
          "message": "Policy 'bltlive-11051551-audit' was created",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "bltlive-11051551-audit"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "0",
              "oldValueDisplayString": "",
              "newValueDisplayString": "Standard",
              "typeId": 2,
              "attributeName": "Policy Type",
              "attributeId": "__UMI__500"
            },
            {
              "oldValue": "",
              "newValue": "0",
              "oldValueDisplayString": "",
              "newValueDisplayString": "No",
              "typeId": 2,
              "attributeName": "Follow NFS Mounts",
              "attributeId": "__UMI__501"
            },
            {
              "oldValue": "",
              "newValue": "0",
              "oldValueDisplayString": "",
              "newValueDisplayString": "No",
              "typeId": 2,
              "attributeName": "Client Compress",
              "attributeId": "__UMI__502"
            },
            "... 43 more"
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "bltlive-11051551: change CHG0000001",
          "auditDateTime": "2026-11-05T15:51:27.374Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3631"
          }
        }
      },
      {
        "type": "audit",
        "id": "3632",
        "attributes": {
          "category": "POLICY",
          "operation": "MODIFY",
          "messageId": 12,
          "message": "Include list settings of Policy 'bltlive-11051551-audit' were modified",
          "auditKeyList": [
            {
              "typeId": 1,
              "typeIdDisplayString": "bltlive-11051551-audit"
            }
          ],
          "auditRecordAttributeList": [
            {
              "oldValue": "",
              "newValue": "/tmp/bltlive",
              "oldValueDisplayString": "",
              "newValueDisplayString": "/tmp/bltlive",
              "typeId": 1,
              "attributeName": "Backup Selection",
              "attributeId": "__UMI__562"
            },
            {
              "oldValue": "",
              "newValue": "1",
              "oldValueDisplayString": "",
              "newValueDisplayString": "1",
              "typeId": 2,
              "attributeName": "Policy Generation",
              "attributeId": "__UMI__539"
            }
          ],
          "auditUserIdentity": {
            "userName": "user-01",
            "domainName": "primary-01",
            "domainType": "UNIX_PASSWORD"
          },
          "reason": "bltlive-11051551: change CHG0000001",
          "auditDateTime": "2026-11-05T15:51:27.374Z"
        },
        "links": {
          "self": {
            "href": "https://primary-01:1556/netbackup/security/auditlogs/3632"
          }
        }
      },
      "... 5 more"
    ],
    "meta": {
      "pagination": {
        "pages": 1,
        "offset": 0,
        "last": 0,
        "limit": 100,
        "count": 8,
        "page": 0,
        "first": 0
      }
    },
    "links": {
      "last": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=id&filter=category%20eq%20'POLICY'%20and%20id%20gt%203629"
      },
      "self": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=id&filter=category%20eq%20'POLICY'%20and%20id%20gt%203629"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/security/auditlogs?page%5Boffset%5D=0&page%5Blimit%5D=100&sort=id&filter=category%20eq%20'POLICY'%20and%20id%20gt%203629"
      }
    }
  }
  ```

  </details>

**What the SDK gave back**

```json
[
  {
    "operation": "CREATE",
    "message": "User 'user-01' is creating policy 'bltlive-11051551-audit' of type 'Standard'.",
    "user": "user-01",
    "reason": "",
    "changed": []
  },
  {
    "operation": "CREATE",
    "message": "Policy 'bltlive-11051551-audit' was created",
    "user": "user-01",
    "reason": "bltlive-11051551: change CHG0000001",
    "changed": [
      [
        "Policy Type",
        "",
        "0"
      ],
      [
        "Follow NFS Mounts",
        "",
        "0"
      ],
      [
        "Client Compress",
        "",
        "0"
      ],
      "... 43 more"
    ]
  },
  {
    "operation": "MODIFY",
    "message": "Include list settings of Policy 'bltlive-11051551-audit' were modified",
    "user": "user-01",
    "reason": "bltlive-11051551: change CHG0000001",
    "changed": [
      [
        "Backup Selection",
        "",
        "/tmp/bltlive"
      ],
      [
        "Policy Generation",
        "",
        "1"
      ]
    ]
  },
  "... 5 more"
]
```

## An access-control role with nobody in it: create, read, rename, delete

Its access definitions (what the role may do, on what) start empty.

```python
name = f"{PREFIX}-role"
created = nbu.raw.accesscontrol.post_roles(
    body={"data": {"type": "accessControlRoleV8", "attributes": {"name": name}}}
)
role_id = created["data"]["id"]
role = nbu.raw.accesscontrol.get_role(role_id)["data"]
assert role["attributes"]["name"] == name
definitions = nbu.raw.accesscontrol.list_role_access_definitions(role_id)

renamed = f"{name}-2"
nbu.raw.accesscontrol.put_role(
    role_id,
    body={"data": {"type": "accessControlRoleV8", "attributes": {"name": renamed}}},
)
after = nbu.raw.accesscontrol.get_role(role_id)["data"]["attributes"]
record.result({"name": after.get("name"), "accessDefinitions": definitions.get("data")})
assert after["name"] == renamed

nbu.raw.accesscontrol.delete_role(role_id)
with pytest.raises(NotFoundError):
    nbu.raw.accesscontrol.get_role(role_id)
```

**On the wire**

- `POST /access-control/roles` -> **201** (0.14 s)

  Sent:

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "attributes": {
        "name": "bltlive-11051551-role"
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "id": "33",
      "attributes": {
        "uuid": "250789b0-1d19-4174-8014-b6816e6f7974",
        "systemDefined": false,
        "template": false,
        "roleType": "USER",
        "name": "bltlive-11051551-role"
      },
      "relationships": {
        "userPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/user-principals"
            }
          },
          "data": []
        },
        "groupPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/group-principals"
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
          "href": "/access-control/roles/33"
        }
      }
    }
  }
  ```

  </details>

- `GET /access-control/roles/33` -> **200** (0.05 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "id": "33",
      "attributes": {
        "uuid": "250789b0-1d19-4174-8014-b6816e6f7974",
        "systemDefined": false,
        "template": false,
        "roleType": "USER",
        "name": "bltlive-11051551-role",
        "description": ""
      },
      "relationships": {
        "userPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/user-principals"
            }
          },
          "data": []
        },
        "groupPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/group-principals"
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
          "href": "/access-control/roles/33"
        }
      }
    }
  }
  ```

  </details>

- `GET /access-control/roles/33/access-definitions` -> **200** (0.10 s)

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
        "href": "https://primary-01:1556/netbackup/access-control/roles/33/access-definitions?page%5Boffset%5D=0&page%5Blimit%5D=10"
      },
      "first": {
        "href": "https://primary-01:1556/netbackup/access-control/roles/33/access-definitions?page%5Boffset%5D=0&page%5Blimit%5D=10"
      }
    }
  }
  ```

  </details>

- `PUT /access-control/roles/33` -> **204** (0.07 s)

  Sent:

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "attributes": {
        "name": "bltlive-11051551-role-2"
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /access-control/roles/33` -> **200** (0.10 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "accessControlRoleV8",
      "id": "33",
      "attributes": {
        "uuid": "250789b0-1d19-4174-8014-b6816e6f7974",
        "systemDefined": false,
        "template": false,
        "roleType": "USER",
        "name": "bltlive-11051551-role-2",
        "description": ""
      },
      "relationships": {
        "userPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/user-principals"
            }
          },
          "data": []
        },
        "groupPrincipals": {
          "links": {
            "self": {
              "href": "/access-control/roles/33/relationships/group-principals"
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
          "href": "/access-control/roles/33"
        }
      }
    }
  }
  ```

  </details>

- `DELETE /access-control/roles/33` -> **204** (0.09 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /access-control/roles/33` -> **404** (0.06 s)

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
  "name": "bltlive-11051551-role-2",
  "accessDefinitions": []
}
```
