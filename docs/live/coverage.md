# Coverage, proven live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:47 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

**163 of 733** operations in the server's own API description were called by the live tests and answered without an error.

| Area | Proven | Operations |
|---|---|---|
| config | 43 | 176 |
| recovery | 14 | 100 |
| security | 32 | 88 |
| bmr | 0 | 72 |
| storage | 15 | 53 |
| catalog | 6 | 34 |
| accesscontrol | 5 | 25 |
| admin | 6 | 25 |
| hostproperties | 7 | 25 |
| rbac | 9 | 19 |
| malware | 5 | 18 |
| config_workloads | 1 | 15 |
| servicecatalog | 1 | 14 |
| assetdb | 1 | 11 |
| gateway | 4 | 10 |
| assetservice | 5 | 9 |
| troubleshooting | 0 | 9 |
| globalmanagementservice | 2 | 6 |
| deployment | 2 | 5 |
| eventlog | 2 | 5 |
| manage | 3 | 5 |
| recoverypointservice | 0 | 4 |
| diagnostics | 0 | 2 |
| licensing | 0 | 2 |
| netbackup-self-service | 0 | 1 |

## Proven

### accesscontrol

- `GET /access-control/operations`
- `GET /access-control/roles`
- `GET /access-control/roles/{roleId}`
- `GET /access-control/roles/{roleId}/access-definitions`
- `GET /access-control/service-namespaces`

### admin

- `GET /admin/jobs`
- `GET /admin/jobs/{jobId}`
- `GET /admin/jobs/{jobId}/file-lists`
- `GET /admin/jobs/{jobId}/progress-logs`
- `GET /admin/jobs/{jobId}/try-logs`
- `GET /admin/user-operation-logs`

### assetdb

- `GET /asset-groups`

### assetservice

- `GET /asset-service/workloads`
- `GET /asset-service/workloads/{workload}`
- `GET /asset-service/workloads/{workload}/assets`
- `GET /asset-service/workloads/{workload}/schemas`
- `GET /asset-service/workloads/{workload}/schemas/{schemaId}`

### catalog

- `GET /catalog/images`
- `GET /catalog/latest-vmware-images`
- `GET /catalog/rollback-images`
- `GET /catalog/slp-images`
- `GET /catalog/tape-media`
- `GET /catalog/vmware-images`

### config

- `DELETE /config/policies/{policyName}`
- `DELETE /config/policies/{policyName}/clients/{clientName}`
- `DELETE /config/policies/{policyName}/schedules/{scheduleName}`
- `DELETE /config/slps/{slpName}`
- `GET /config/agentless-hosts`
- `GET /config/cdp-gateway`
- `GET /config/credential-schemas`
- `GET /config/credentials`
- `GET /config/disk-array-hosts`
- `GET /config/ecms-agents`
- `GET /config/ecms-providers`
- `GET /config/hosts`
- `GET /config/hosts-pending-renewal`
- `GET /config/hosts/hostmappings`
- `GET /config/media-servers`
- `GET /config/media-servers/{hostName}`
- `GET /config/policies/`
- `GET /config/policies/{policyName}`
- `GET /config/resource-limit-templates`
- `GET /config/resource-limit-templates/{workloadType}`
- `GET /config/resource-limits`
- `GET /config/resource-limits/{workloadType}`
- `GET /config/server-groups`
- `GET /config/servers/snapshot-mgmt-servers`
- `GET /config/servers/trusted-master-servers`
- `GET /config/servers/vmservers`
- `GET /config/servers/vmservers/{serverName}`
- `GET /config/servers/wssendpoints`
- `GET /config/slp-windows`
- `GET /config/slp-windows/{slpWindowName}`
- `GET /config/slps`
- `GET /config/slps/{slpName}`
- `GET /config/snapshotproviders/configuredplugins`
- `GET /config/snapshotproviders/supported-replication-destinations`
- `GET /config/unique-policy-clients`
- `GET /config/workloads/cloud-object-store/providers`
- `GET /config/workloads/ndmp/hosts`
- `POST /config/policies/`
- `POST /config/slps`
- `PUT /config/policies/{policyName}`
- `PUT /config/policies/{policyName}/clients/{clientName}`
- `PUT /config/policies/{policyName}/schedules/{scheduleName}`
- `PUT /config/slps/{slpName}`

### config_workloads

- `GET /config/workloads/vmware/query-builder-fields`

### deployment

- `GET /deployment/eebs`
- `GET /deployment/packages`

### eventlog

- `GET /eventlog/messages`
- `GET /eventlog/notifications`

### gateway

- `GET /authorization-context`
- `GET /ping`
- `GET /tokenkey`
- `GET /user-sessions`

### globalmanagementservice

- `GET /alta-view/data-collection/status`
- `GET /alta-view/servers`

### hostproperties

- `GET /config/all-hosts`
- `GET /config/data-classifications`
- `GET /config/login-banner-details`
- `GET /config/paused-clients`
- `GET /config/retentionlevels`
- `GET /config/slp-settings`
- `GET /config/user-session-settings`

### malware

- `GET /malware/latest-scan-results`
- `GET /malware/scan-host-pools`
- `GET /malware/scan-hosts`
- `GET /malware/scan-results`
- `GET /malware/tools`

### manage

- `GET /manage/alerts`
- `GET /manage/notification-categories`
- `GET /manage/notification-categories/{categoryId}`

### rbac

- `GET /rbac/access-rules`
- `GET /rbac/object-groups`
- `GET /rbac/object-groups/{objectGroupId}`
- `GET /rbac/object-types`
- `GET /rbac/permission-categories`
- `GET /rbac/permissions`
- `GET /rbac/permissions/{permissionId}`
- `GET /rbac/roles`
- `GET /rbac/roles/{roleId}`

### recovery

- `GET /recovery/check-dr-in-cloud`
- `GET /recovery/workloads/cloud/paas/instant-access-images`
- `GET /recovery/workloads/cloud/paas/instant-access-mounts`
- `GET /recovery/workloads/cloud/vm/instant-access-mounts`
- `GET /recovery/workloads/dynamic-nas/instant-access-mounts`
- `GET /recovery/workloads/ms-windows/instant-access-mounts`
- `GET /recovery/workloads/mssql/instant-access-mounts`
- `GET /recovery/workloads/oracle/instant-access-mounts`
- `GET /recovery/workloads/standard/instant-access-mounts`
- `GET /recovery/workloads/universal-share/instant-access-mounts`
- `GET /recovery/workloads/vmware/instant-access-mounts`
- `GET /recovery/workloads/vmware/instant-access-vms`
- `GET /recovery/workloads/vmware/malware-scan-mounts`
- `GET /recovery/workloads/vmware/scenarios/instant-recovery-vms`

### security

- `GET /security/anomalies`
- `GET /security/anomaly-configurations`
- `GET /security/api-keys`
- `GET /security/api-keys/{apiKeyTag}`
- `GET /security/auditlogs`
- `GET /security/auditlogs/{auditId}`
- `GET /security/cacert`
- `GET /security/certificate-authorities`
- `GET /security/certificate-authorities/hosts-pending-trust-propagation`
- `GET /security/certificate-authorities/migration-summary`
- `GET /security/certificate-authorities/{fingerprint}`
- `GET /security/certificates/crl`
- `GET /security/certificates/current`
- `GET /security/domains/vxat`
- `GET /security/external-cacerts`
- `GET /security/identity-providers`
- `GET /security/key-management-services`
- `GET /security/logindetails`
- `GET /security/logindetails/{auditId}`
- `GET /security/passphrase-constraints`
- `GET /security/passphrase-constraints/{workflowType}`
- `GET /security/ping`
- `GET /security/properties`
- `GET /security/properties/default`
- `GET /security/securitytokens`
- `GET /security/securitytokens/state/valid`
- `GET /security/securitytokens/{tokenName}`
- `GET /security/serverinfo`
- `GET /security/servertime`
- `GET /security/service-principal-configs`
- `GET /security/trust-versions`
- `GET /security/trust-versions/{trustVersion}`

### servicecatalog

- `GET /servicecatalog/slos`

### storage

- `GET /storage/cloud/providers`
- `GET /storage/cloud/providers/{providerId}`
- `GET /storage/disk-pools`
- `GET /storage/disk-pools/{diskPoolId}`
- `GET /storage/drives`
- `GET /storage/key-management-services`
- `GET /storage/storage-servers`
- `GET /storage/storage-servers/{storageServerId}`
- `GET /storage/storage-servers/{storageServerId}/disk-volumes`
- `GET /storage/storage-servers/{storageServerId}/disk-volumes/{diskVolumeId}`
- `GET /storage/storage-servers/{storageServerId}/disk-volumes/{diskVolumeId}/replication-targets`
- `GET /storage/storage-units`
- `GET /storage/storage-units/{storageUnitName}`
- `GET /storage/storage-units/{storageUnitName}/replication-relationships`
- `GET /storage/target-storage-servers`
