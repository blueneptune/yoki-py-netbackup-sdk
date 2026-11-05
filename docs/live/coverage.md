# Coverage, proven live

> Recorded from a real NetBackup 10.2 primary (API 9.0) on 2026-11-05 06:16 UTC, by `pytest -m live` (tests/live). Generated - do not edit; names and addresses are masked.

**12 of 733** operations in the server's own API description were called by the live tests and answered without an error.

| Area | Proven | Operations |
|---|---|---|
| config | 2 | 176 |
| recovery | 0 | 100 |
| security | 1 | 88 |
| bmr | 0 | 72 |
| storage | 2 | 53 |
| catalog | 1 | 34 |
| accesscontrol | 0 | 25 |
| admin | 4 | 25 |
| hostproperties | 0 | 25 |
| rbac | 0 | 19 |
| malware | 0 | 18 |
| config_workloads | 0 | 15 |
| servicecatalog | 0 | 14 |
| assetdb | 0 | 11 |
| gateway | 1 | 10 |
| assetservice | 1 | 9 |
| troubleshooting | 0 | 9 |
| globalmanagementservice | 0 | 6 |
| deployment | 0 | 5 |
| eventlog | 0 | 5 |
| manage | 0 | 5 |
| recoverypointservice | 0 | 4 |
| diagnostics | 0 | 2 |
| licensing | 0 | 2 |
| netbackup-self-service | 0 | 1 |

## Proven

### admin

- `GET /admin/jobs`
- `GET /admin/jobs/{jobId}`
- `GET /admin/jobs/{jobId}/file-lists`
- `GET /admin/jobs/{jobId}/try-logs`

### assetservice

- `GET /asset-service/workloads/{workload}/assets`

### catalog

- `GET /catalog/images`

### config

- `GET /config/hosts`
- `GET /config/policies/{policyName}`

### gateway

- `GET /ping`

### security

- `GET /security/serverinfo`

### storage

- `GET /storage/disk-pools`
- `GET /storage/storage-units`
