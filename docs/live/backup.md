# Backup

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 15:54 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

## Back up one file with a policy made for the purpose

Follow the job; find the image; expire it.

The policy is a copy of an existing Standard policy's settings: one
client (the primary itself), one file, one Full schedule with no start
window - so it only ever runs when asked - writing to a disk storage
unit on the server's own disk, kept for the shortest retention level.

```python
template = _template(nbu)
client = _primary(nbu)
unit = _disk_unit(nbu)
known = (template.get("clients") or [{}])[0]

policy = copy.deepcopy(template)
policy["policyName"] = POLICY
attributes = policy["policyAttributes"]
attributes["active"] = True
attributes["storage"] = unit
attributes["storageIsSLP"] = False
attributes["useAccelerator"] = False
attributes["keyword"] = "bltlive"
policy["clients"] = [
    {
        "hostName": client,
        "hardware": known.get("hardware", "Linux"),
        "OS": known.get("OS", "RedHat2.6.32"),
    }
]
policy["backupSelections"] = {"selections": [SELECTION]}
schedule = copy.deepcopy(template["schedules"][0])
schedule["scheduleName"] = SCHEDULE
schedule["scheduleType"] = "Calendar"
schedule["backupType"] = "Full Backup"
for window in schedule.get("startWindow") or []:
    window["startSeconds"] = 0
    window["durationSeconds"] = 0
schedule["storageIsSLP"] = False
schedule["backupCopies"] = {
    "copies": [
        {
            "retentionLevel": 0,
            "retentionPeriod": {"value": 1, "unit": "WEEKS"},
            "storage": unit,
        }
    ],
    "priority": -1,
}
policy["schedules"] = [schedule]
nbu.raw.config.post_policies(
    body={"data": {"type": "policy", "id": POLICY, "attributes": {"policy": policy}}}
)

started = nbu.raw.admin.post_manual_backup(
    body={
        "data": {
            "type": "backupRequest",
            "attributes": {
                "policyName": POLICY,
                "scheduleName": SCHEDULE,
                "clientName": client,
                "keyword": "bltlive",
            },
        }
    }
)
job_ids = [int(job["id"]) for job in started.get("data", [])]
assert job_ids, f"the manual backup started no job: {started}"
jobs = _wait(nbu, job_ids)
record.result(
    {
        "jobs": [
            {
                "jobId": job.job_id,
                "jobType": job.job_type,
                "state": job.state,
                "status": job.status,
                "storageUnit": job.storage_unit,
            }
            for job in jobs
        ]
    }
)
assert all(job.status in (0, 1) for job in jobs), [(j.job_id, j.status) for j in jobs]

images = _ours(nbu, POLICY)
assert images, "no image in the catalog for the policy"
backup_id = images[0]["id"]
image = nbu.raw.catalog.get_image(backup_id)["data"]["attributes"]
assert image["policyName"] == POLICY  # ours, before anything is expired
record.result(
    {
        k: image.get(k)
        for k in ("policyName", "scheduleName", "clientName", "backupTime", "kilobytes")
    }
)
record.result(nbu.raw.catalog.list_image_contents_by_backup_id(backup_id))

_expire(nbu, backup_id)
with pytest.raises(NotFoundError):
    nbu.raw.catalog.get_image(backup_id)

nbu.raw.config.delete_policy(POLICY)
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

- `GET /config/policies/policy-01` -> **200** (0.06 s)

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

- `GET /config/hosts` -> **200** (0.05 s)

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

- `POST /config/policies/` -> **204** (0.24 s)

  Sent:

  ```json
  {
    "data": {
      "type": "policy",
      "id": "bltlive-11051551-bkp",
      "attributes": {
        "policy": {
          "policyName": "bltlive-11051551-bkp",
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
            "priority": 0,
            "readOnlyTablespaceOptions": null,
            "retainSnapshot": false,
            "secondarySnapshotMethodArgs": null,
            "skipOfflineDatafiles": null,
            "snapshotBackup": false,
            "snapshotFreeBackupInfo": null,
            "snapshotMethod": null,
            "snapshotMethodArgs": null,
            "storage": "storage-unit-02",
            "storageIsSLP": false,
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
              "hostName": "primary-01",
              "hardware": "Linux",
              "OS": "RedHat2.6.32"
            }
          ],
          "schedules": [
            {
              "acceleratorForcedRescan": false,
              "backupCopies": {
                "copies": [
                  {
                    "retentionLevel": 0,
                    "retentionPeriod": {
                      "value": 1,
                      "unit": "WEEKS"
                    },
                    "storage": "storage-unit-02"
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
              "scheduleType": "Calendar",
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
              "/usr/openv/netbackup/bin/version"
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

- `POST /admin/manual-backup` -> **202** (1.17 s)

  Sent:

  ```json
  {
    "data": {
      "type": "backupRequest",
      "attributes": {
        "policyName": "bltlive-11051551-bkp",
        "scheduleName": "bltlive-full",
        "clientName": "primary-01",
        "keyword": "bltlive"
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "job",
        "id": "1712",
        "attributes": {
          "jobId": 1712
        },
        "links": {
          "self": {
            "href": "/admin/jobs/1712"
          }
        }
      }
    ]
  }
  ```

  </details>

- `GET /admin/jobs/1712` -> **404** (0.05 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /admin/jobs/1712` -> **200** (0.11 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "job",
      "id": "1712",
      "attributes": {
        "jobId": 1712,
        "parentJobId": 0,
        "activeProcessId": 897548,
        "jobType": "BACKUP",
        "jobSubType": "IMMEDIATE",
        "policyType": "STANDARD",
        "policyName": "bltlive-11051551-bkp",
        "scheduleType": "FULL_BACKUP",
        "scheduleName": "bltlive-full",
        "clientName": "primary-01",
        "jobOwner": "root",
        "jobGroup": "other",
        "backupId": "primary-01_1793893889",
        "destinationStorageUnitName": "storage-unit-02",
        "destinationMediaServerName": "primary-01",
        "dataMovement": "STANDARD",
        "streamNumber": 0,
        "copyNumber": 0,
        "priority": 0,
        "compression": 0,
        "state": "ACTIVE",
        "numberOfFiles": 1,
        "estimatedFiles": 0,
        "kilobytesTransferred": 32,
        "kilobytesToTransfer": 0,
        "transferRate": 87,
        "percentComplete": 0,
        "currentFile": "/usr/openv/netbackup/bin/version",
        "restartable": 1,
        "suspendable": 0,
        "resumable": 0,
        "frozenImage": 0,
        "transportType": "LAN",
        "dedupRatio": 95.1,
        "currentOperation": 3,
        "sessionId": 0,
        "numberOfTapeToEject": 0,
        "submissionType": 0,
        "auditDomainType": 0,
        "startTime": "2026-11-05T15:51:29.000Z",
        "endTime": "1970-01-01T00:00:00.000Z",
        "activeTryStartTime": "2026-11-05T15:51:29.000Z",
        "lastUpdateTime": "2026-11-05T15:51:39.093Z",
        "childCount": 0,
        "jobPath": "1712",
        "retentionLevel": 0,
        "try": 1,
        "cancellable": 1,
        "jobQueueReason": -99,
        "kilobytesDataTransferred": 0,
        "elapsedTime": "PT11.547S",
        "activeElapsedTime": "PT11.547S",
        "dteMode": "OFF",
        "dedupSpaceRatio": 17.1,
        "compressionSpaceRatio": 78.0,
        "workloadDisplayName": "primary-01",
        "offHostType": "STANDARD"
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1712"
        },
        "file-lists": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/file-lists"
        },
        "try-logs": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/try-logs"
        }
      }
    }
  }
  ```

  </details>

- `GET /admin/jobs/1712` -> **200** (0.12 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "job",
      "id": "1712",
      "attributes": {
        "jobId": 1712,
        "parentJobId": 0,
        "activeProcessId": 897548,
        "jobType": "BACKUP",
        "jobSubType": "IMMEDIATE",
        "policyType": "STANDARD",
        "policyName": "bltlive-11051551-bkp",
        "scheduleType": "FULL_BACKUP",
        "scheduleName": "bltlive-full",
        "clientName": "primary-01",
        "jobOwner": "root",
        "jobGroup": "other",
        "backupId": "primary-01_1793893889",
        "destinationStorageUnitName": "storage-unit-02",
        "destinationMediaServerName": "primary-01",
        "dataMovement": "STANDARD",
        "streamNumber": 0,
        "copyNumber": 0,
        "priority": 0,
        "compression": 0,
        "status": 0,
        "state": "DONE",
        "numberOfFiles": 1,
        "estimatedFiles": 0,
        "kilobytesTransferred": 32,
        "kilobytesToTransfer": 0,
        "transferRate": 87,
        "percentComplete": 100,
        "restartable": 1,
        "suspendable": 0,
        "resumable": 0,
        "frozenImage": 0,
        "transportType": "LAN",
        "dedupRatio": 95.1,
        "currentOperation": -99,
        "sessionId": 0,
        "numberOfTapeToEject": 0,
        "submissionType": 0,
        "auditDomainType": 0,
        "startTime": "2026-11-05T15:51:29.000Z",
        "endTime": "2026-11-05T15:51:39.000Z",
        "activeTryStartTime": "2026-11-05T15:51:29.000Z",
        "lastUpdateTime": "2026-11-05T15:51:49.095Z",
        "childCount": 0,
        "jobPath": "1712",
        "retentionLevel": 0,
        "try": 1,
        "cancellable": 0,
        "jobQueueReason": -99,
        "kilobytesDataTransferred": 0,
        "elapsedTime": "PT10S",
        "activeElapsedTime": "PT10S",
        "dteMode": "OFF",
        "dedupSpaceRatio": 17.1,
        "compressionSpaceRatio": 78.0,
        "workloadDisplayName": "primary-01",
        "offHostType": "STANDARD"
      },
      "links": {
        "self": {
          "href": "/admin/jobs/1712"
        },
        "file-lists": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/file-lists"
        },
        "try-logs": {
          "href": "https://primary-01:1556/netbackup/admin/jobs/1712/try-logs"
        }
      }
    }
  }
  ```

  </details>

- `GET /catalog/images?page%5Blimit%5D=100` -> **200** (0.14 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": [
      {
        "type": "image",
        "id": "primary-01_1793893889",
        "attributes": {
          "policyType": "Standard",
          "clientName": "primary-01",
          "policyName": "bltlive-11051551-bkp",
          "scheduleType": "FULL",
          "backupCopyType": "DEFAULT",
          "backupTime": "2026-11-05T15:51:29.000Z",
          "backupStatus": 0,
          "clientCharset": 1,
          "compression": false,
          "contentFile": "bltlive-11051551-bkp_1793893889_FULL.f",
          "contentFileSize": "1132",
          "contentFileCompressed": "NOT",
          "creator": "root",
          "dataClassification": "",
          "drMediaList": [],
          "elapsedTimeSeconds": 9,
          "encryption": "NONE",
          "expiration": "2026-11-12T15:51:29.000Z",
          "extendedSecurityInfo": false,
          "fileSystemOnly": false,
          "fragments": [
            {
              "blockSize": 262144,
              "checkpoint": 0,
              "copyDate": "2026-11-05T15:51:38.000Z",
              "copyNumber": 1,
              "dataFormat": "TAR",
              "density": 0,
              "deviceWrittenOn": -1,
              "expiration": "2026-11-12T15:51:29.000Z",
              "fragmentFlags": 256,
              "fileNumber": 0,
              "firstBlock": 0,
              "fragmentNumber": -2147482648,
              "host": "primary-01",
              "mediaId": "@aaaah",
              "kbytes64": 1,
              "keyTag": "*NULL*",
              "lastBlock": 0,
              "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
              "mediaSequenceNumber": 0,
              "mediaSubtype": 6,
              "mediaType": 0,
              "multiplex": 0,
              "offset": 0,
              "remainder": 823,
              "resumeNumber": 0,
              "retentionLevel": 0,
              "slpTag": "*NULL*",
              "wormFlags": 0,
              "wormUnlockTime": "1970-01-01T00:00:00.000Z",
              "copyDteMode": "OFF",
              "hierarchicalDteMode": "OFF",
              "heldForDependentCopy": "NO",
              "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
            },
            {
              "blockSize": 262144,
              "checkpoint": 0,
              "copyDate": "2026-11-05T15:51:38.000Z",
              "copyNumber": 1,
              "dataFormat": "TAR",
              "density": 0,
              "deviceWrittenOn": -1,
              "expiration": "2026-11-12T15:51:29.000Z",
              "fragmentFlags": 128,
              "fileNumber": 0,
              "firstBlock": 0,
              "fragmentNumber": -1,
              "host": "primary-01",
              "mediaId": "@aaaah",
              "kbytes64": 1,
              "keyTag": "*NULL*",
              "lastBlock": 0,
              "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
              "mediaSequenceNumber": 0,
              "mediaSubtype": 6,
              "mediaType": 0,
              "multiplex": 0,
              "offset": 0,
              "remainder": 108,
              "resumeNumber": 0,
              "retentionLevel": 0,
              "slpTag": "*NULL*",
              "wormFlags": 0,
              "wormUnlockTime": "1970-01-01T00:00:00.000Z",
              "copyDteMode": "OFF",
              "hierarchicalDteMode": "OFF",
              "heldForDependentCopy": "NO",
              "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
            },
            {
              "blockSize": 262144,
              "checkpoint": 0,
              "copyDate": "2026-11-05T15:51:38.000Z",
              "copyNumber": 1,
              "dataFormat": "TAR",
              "density": 0,
              "deviceWrittenOn": -1,
              "expiration": "2026-11-12T15:51:29.000Z",
              "fragmentFlags": 4,
              "fileNumber": 0,
              "firstBlock": 0,
              "fragmentNumber": 1,
              "host": "primary-01",
              "mediaId": "@aaaah",
              "kbytes64": 32,
              "keyTag": "*NULL*",
              "lastBlock": 0,
              "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
              "mediaSequenceNumber": 0,
              "mediaSubtype": 6,
              "mediaType": 0,
              "multiplex": 0,
              "offset": 0,
              "remainder": 0,
              "resumeNumber": 0,
              "retentionLevel": 0,
              "slpTag": "*NULL*",
              "wormFlags": 0,
              "wormUnlockTime": "1970-01-01T00:00:00.000Z",
              "copyDteMode": "OFF",
              "hierarchicalDteMode": "OFF",
              "heldForDependentCopy": "NO",
              "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
            }
          ],
          "imageDumpLevel": 0,
          "imageType": "NORMAL",
          "jobId": 1712,
          "kbytes": 33,
          "keyword": "bltlive",
          "kbytesDataTransferred": 0,
          "mpx": false,
          "numCopies": 1,
          "numFiles": 1,
          "streamAggregatedKbytes": -1,
          "streamAggregatedFiles": -1,
          "numberFragments": 3,
          "originMasterServer": "",
          "pfiType": 0,
          "primaryCopy": 1,
          "proxyClient": "",
          "retentionLevel": 0,
          "scheduleName": "bltlive-full",
          "slpVersion": 0,
          "slpCompleted": 0,
          "slpName": "",
          "version": 15,
          "providerGeneratedId": "",
          "vmType": "NONE",
          "intelligentCatalogArchiving": "NO",
          "streamNumber": 0,
          "remoteExpirationDate": "1970-01-01T00:00:00.000Z",
          "tirExpirationDate": "1970-01-01T00:00:00.000Z",
          "imageDteMode": "OFF",
          "malwareScanResult": "NOT_SCANNED"
        },
        "links": {
          "self": {
            "href": "/catalog/images/primary-01_1793893889"
          }
        }
      }
    ],
    "meta": {
      "pagination": {
        "last": 0,
        "offset": 0,
        "count": 1,
        "limit": 100,
        "first": 0
      }
    }
  }
  ```

  </details>

- `GET /catalog/images/primary-01_1793893889` -> **200** (0.09 s)

  <details><summary>Answer</summary>

  ```json
  {
    "data": {
      "type": "image",
      "id": "primary-01_1793893889",
      "attributes": {
        "policyType": "Standard",
        "clientName": "primary-01",
        "policyName": "bltlive-11051551-bkp",
        "scheduleType": "FULL",
        "backupCopyType": "DEFAULT",
        "backupTime": "2026-11-05T15:51:29.000Z",
        "backupStatus": 0,
        "clientCharset": 1,
        "compression": false,
        "contentFile": "bltlive-11051551-bkp_1793893889_FULL.f",
        "contentFileSize": "1132",
        "contentFileCompressed": "NOT",
        "creator": "root",
        "dataClassification": "",
        "drMediaList": [],
        "elapsedTimeSeconds": 9,
        "encryption": "NONE",
        "expiration": "2026-11-12T15:51:29.000Z",
        "extendedSecurityInfo": false,
        "fileSystemOnly": false,
        "fragments": [
          {
            "blockSize": 262144,
            "checkpoint": 0,
            "copyDate": "2026-11-05T15:51:38.000Z",
            "copyNumber": 1,
            "dataFormat": "TAR",
            "density": 0,
            "deviceWrittenOn": -1,
            "expiration": "2026-11-12T15:51:29.000Z",
            "fragmentFlags": 256,
            "fileNumber": 0,
            "firstBlock": 0,
            "fragmentNumber": -2147482648,
            "host": "primary-01",
            "mediaId": "@aaaah",
            "kbytes64": 1,
            "keyTag": "*NULL*",
            "lastBlock": 0,
            "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
            "mediaSequenceNumber": 0,
            "mediaSubtype": 6,
            "mediaType": 0,
            "multiplex": 0,
            "offset": 0,
            "remainder": 823,
            "resumeNumber": 0,
            "retentionLevel": 0,
            "slpTag": "*NULL*",
            "wormFlags": 0,
            "wormUnlockTime": "1970-01-01T00:00:00.000Z",
            "copyDteMode": "OFF",
            "hierarchicalDteMode": "OFF",
            "heldForDependentCopy": "NO",
            "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
          },
          {
            "blockSize": 262144,
            "checkpoint": 0,
            "copyDate": "2026-11-05T15:51:38.000Z",
            "copyNumber": 1,
            "dataFormat": "TAR",
            "density": 0,
            "deviceWrittenOn": -1,
            "expiration": "2026-11-12T15:51:29.000Z",
            "fragmentFlags": 128,
            "fileNumber": 0,
            "firstBlock": 0,
            "fragmentNumber": -1,
            "host": "primary-01",
            "mediaId": "@aaaah",
            "kbytes64": 1,
            "keyTag": "*NULL*",
            "lastBlock": 0,
            "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
            "mediaSequenceNumber": 0,
            "mediaSubtype": 6,
            "mediaType": 0,
            "multiplex": 0,
            "offset": 0,
            "remainder": 108,
            "resumeNumber": 0,
            "retentionLevel": 0,
            "slpTag": "*NULL*",
            "wormFlags": 0,
            "wormUnlockTime": "1970-01-01T00:00:00.000Z",
            "copyDteMode": "OFF",
            "hierarchicalDteMode": "OFF",
            "heldForDependentCopy": "NO",
            "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
          },
          {
            "blockSize": 262144,
            "checkpoint": 0,
            "copyDate": "2026-11-05T15:51:38.000Z",
            "copyNumber": 1,
            "dataFormat": "TAR",
            "density": 0,
            "deviceWrittenOn": -1,
            "expiration": "2026-11-12T15:51:29.000Z",
            "fragmentFlags": 4,
            "fileNumber": 0,
            "firstBlock": 0,
            "fragmentNumber": 1,
            "host": "primary-01",
            "mediaId": "@aaaah",
            "kbytes64": 32,
            "keyTag": "*NULL*",
            "lastBlock": 0,
            "mediaDesc": "1;PureDisk;primary-01;disk-pool-01;volume-01;0",
            "mediaSequenceNumber": 0,
            "mediaSubtype": 6,
            "mediaType": 0,
            "multiplex": 0,
            "offset": 0,
            "remainder": 0,
            "resumeNumber": 0,
            "retentionLevel": 0,
            "slpTag": "*NULL*",
            "wormFlags": 0,
            "wormUnlockTime": "1970-01-01T00:00:00.000Z",
            "copyDteMode": "OFF",
            "hierarchicalDteMode": "OFF",
            "heldForDependentCopy": "NO",
            "slpTryToKeepDate": "1970-01-01T00:00:00.000Z"
          }
        ],
        "imageDumpLevel": 0,
        "imageType": "NORMAL",
        "jobId": 1712,
        "kbytes": 33,
        "keyword": "bltlive",
        "kbytesDataTransferred": 0,
        "mpx": false,
        "numCopies": 1,
        "numFiles": 1,
        "streamAggregatedKbytes": -1,
        "streamAggregatedFiles": -1,
        "numberFragments": 3,
        "originMasterServer": "",
        "pfiType": 0,
        "primaryCopy": 1,
        "proxyClient": "",
        "retentionLevel": 0,
        "scheduleName": "bltlive-full",
        "slpVersion": 0,
        "slpCompleted": 0,
        "slpName": "",
        "version": 15,
        "providerGeneratedId": "",
        "vmType": "NONE",
        "intelligentCatalogArchiving": "NO",
        "streamNumber": 0,
        "remoteExpirationDate": "1970-01-01T00:00:00.000Z",
        "tirExpirationDate": "1970-01-01T00:00:00.000Z",
        "imageDteMode": "OFF",
        "malwareScanResult": "NOT_SCANNED"
      },
      "links": {
        "self": {
          "href": "/catalog/images/primary-01_1793893889"
        }
      }
    }
  }
  ```

  </details>

- `GET /catalog/images/primary-01_1793893889/contents` -> **202** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "requestId": "56042d4e-53a4-4c36-8003-52ae7bcf2e4d"
  }
  ```

  </details>

- `POST /catalog/images/update-expiration-date` -> **204** (1.34 s)

  Sent:

  ```json
  {
    "data": {
      "type": "byBackupId",
      "attributes": {
        "backupId": "primary-01_1793893889",
        "date": "1970-01-01T00:00:00.000Z",
        "delete": true,
        "immediate": true,
        "followDependee": false
      }
    }
  }
  ```

  <details><summary>Answer</summary>

  (no body)

  </details>

- `GET /catalog/images/primary-01_1793893889` -> **404** (0.13 s)

  <details><summary>Answer</summary>

  ```json
  {
    "errorCode": 227,
    "errorMessage": "no entity was found",
    "attributeErrors": {},
    "fileUploadErrors": [],
    "errorDetails": [
      "The image with backup ID primary-01_1793893889"
    ]
  }
  ```

  </details>

- `DELETE /config/policies/bltlive-11051551-bkp` -> **204** (0.17 s)

  <details><summary>Answer</summary>

  (no body)

  </details>

**What the SDK gave back**

```json
{
  "jobs": [
    {
      "jobId": 1712,
      "jobType": "BACKUP",
      "state": "DONE",
      "status": 0,
      "storageUnit": "storage-unit-02"
    }
  ]
}
```

**What the SDK gave back**

```json
{
  "policyName": "bltlive-11051551-bkp",
  "scheduleName": "bltlive-full",
  "clientName": "primary-01",
  "backupTime": "2026-11-05T15:51:29.000Z",
  "kilobytes": null
}
```

**What the SDK gave back**

```json
{
  "requestId": "56042d4e-53a4-4c36-8003-52ae7bcf2e4d"
}
```
