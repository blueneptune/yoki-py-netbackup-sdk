# yoki-py-netbackup-sdk

A small SDK for the **NetBackup REST API**, built on
[sdk-primer-core](https://github.com/blueneptune/sdk-primer-core) and
laid out like `yoki-py-commvault-sdk` and `yoki-py-veeam-sdk`: one
client per NetBackup primary server, a named group of calls for each
kind of thing, read-only unless told otherwise.

The repository is `yoki-py-netbackup-sdk`; the package is
`netbackup-sdk`, imported as `netbackup_sdk`.

> **Status: written from Veritas's documentation. No part of it has been
> run against a NetBackup server.** Every call has a test that fakes the
> server's answers. Expect corrections on first contact;
> `netbackup-probe` (below) exists to make that quick.

```python
from datetime import UTC, datetime, timedelta
from netbackup_sdk import NetBackupClient

with NetBackupClient("https://nbu01.example.com:1556/netbackup", api_key=key) as nbu:
    since = datetime.now(UTC) - timedelta(hours=1)
    for page in nbu.jobs.iter_pages(updated_after=since):
        for job in page:
            print(job.job_id, job.client_name, job.state, job.status)
    print("API version in use:", nbu.api_version)
```

## API versions: NetBackup 10.0, 10.5 and 11.0

Every request names an API version, and a server refuses (406) a version
it does not support. Maintenance releases keep their release's version.

| NetBackup | API version |
|---|---|
| 11.0, 11.0.0.1 | 13.0 |
| 10.5, 10.5.0.1 | 12.0 |
| 10.0, 10.0.0.1 | 7.0 |

`api_version="auto"` (the default) tries 13.0, then 12.0, then 7.0, and
keeps the first one the server accepts. Pin one with a release
(`api_version="10.5"`) or an API version (`api_version="12.0"`); a
pinned version is never changed. `nbu.api_version` says which is in use.

Differences between them that matter here: API 12.0 adds
`kilobytesDataTransferred` to jobs (the amount actually sent;
`kilobytesTransferred` may be an estimate) - read when present, `None`
otherwise. Everything else used here is in all three, as far as the
documentation says.

## Logging in

Either credential is sent as the bare `Authorization` value (no
"Bearer"):

- **API key** (`api_key=`) - preferred for a collector: created in the
  NetBackup web UI, valid until its expiry date, no password stored.
- **User and password** (`username=`, `password=`, `domain_type=` -
  `vx` NetBackup, `unixpwd` local Linux, `nt` Windows/AD - and
  `domain_name=`) - exchanged at `POST /login` for a 24-hour token,
  renewed five minutes before it runs out or on a 401, ended with
  `POST /logout` when the client closes.

The account needs a role that can read jobs, policies and the catalog;
a read-only administrator role is enough.

## The calls

Paths are under `https://<primary>:1556/netbackup`.

| Call | Endpoint | Returns |
|---|---|---|
| `nbu.server.ping()` | `GET /ping` | server time; proves the version is accepted |
| `nbu.jobs.iter_pages(...)` | `GET /admin/jobs` | pages of `Job`, in job-id order |
| `nbu.jobs.sample(n, ...)` | same, one request | `(total, [Job])`, newest first |
| `nbu.jobs.oldest_start()` | same, one request | when history begins |
| `nbu.jobs.get(id)` | `GET /admin/jobs/{id}` | `Job`, or `None` if gone |
| `nbu.jobs.try_logs(id)` | `GET /admin/jobs/{id}/try-logs` | detailed status lines |
| `nbu.jobs.file_lists(id)` | `GET /admin/jobs/{id}/file-lists` | what a backup covered |
| `nbu.policies.list()`, `.get(name)` | `GET /config/policies[/{name}]` | policies (generic schema) |
| `nbu.images.iter_pages(...)`, `.latest(client)` | `GET /catalog/images` | backup images |
| `nbu.hosts.list()` | `GET /config/hosts` | hosts the primary knows |
| `nbu.storage.units()`, `.disk_pools()` | `GET /storage/...` | storage units, disk pools |
| `nbu.assets.workload(w)` | `GET /asset-service/workloads/{w}/assets` | discovered VMware, SQL, ... assets |

**Changing calls** - refused unless built with `allow_changes=True`, and
never retried: `nbu.jobs.cancel(id)`, `.suspend(id)`, `.resume(id)`,
`.restart(id)`.

### Job filters

`iter_pages` builds NetBackup's OData filter from:

| Argument | Filter | For |
|---|---|---|
| `updated_after=t` | `lastUpdateTime ge t` | the delta: every job created **or changed** since `t`, running or not |
| `active_only=True` | `state ne 'DONE'` | what is still going |
| `ended_after`, `ended_before` | `endTime ge ... and endTime lt ...` | a window of history (backfill) |
| `started_after`, `job_types`, `client`, `policy` | as named | narrowing |
| `extra_filter` | any OData condition, ANDed on | anything else |

Times must be timezone-aware; they are sent as UTC with `Z`. Pages are
at most 100 jobs (NetBackup's limit).

`Job` reads: id, parent, type, state (`QUEUED`, `ACTIVE`, `REQUEUED`,
`SUSPENDED`, `INCOMPLETE`, `WAITING_FOR_RETRY`, `DONE`), status
(0 succeeded, 1 partial, other failed), policy and type, schedule and
type, client, media server, storage unit, backup id, start/end/last
update, kilobytes, files, percent complete - and keeps NetBackup's
record in `.raw`.

## netbackup-probe

```
NBU_URL=https://nbu01.example.com:1556/netbackup NBU_API_KEY='...' uv run netbackup-probe
```

One line per call, starting with the API version the server accepted.
Also `NBU_USERNAME` / `NBU_PASSWORD` / `NBU_DOMAIN_TYPE` /
`NBU_DOMAIN_NAME`, `NBU_API_VERSION`, `NBU_VERIFY_TLS=false`,
`NBU_CA_BUNDLE`. Reads only.

## What is not known

- **All of it, strictly** - see the status note.
- **Whether `lastUpdateTime` is filterable** on every version. It is the
  natural delta; if a server refuses it, fall back to `endTime` plus
  `active_only`.
- **Whether 7.0 is still accepted by 11.0**, and 12.0 by 10.0 (it is
  not, by the 406 reports). `auto` copes either way.
- **Job hierarchy.** NetBackup splits work into parent and child jobs
  (a policy run, then a job per client or stream). Both come back;
  `parent_job_id` relates them. A collector has to decide which it
  counts.
- **Database-level detail** (MS SQL): which databases a job covered is
  likely in the file lists or the image's contents - unconfirmed.
- **Rate limits:** none documented.

## Development

```
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check . && uv run mypy
```

## Sources

- [NetBackup 10.0 API - Getting Started](https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/) - base URL, login, API keys, versioned media types, paging, filters, JSON:API shape
- [nbu_exporter: API 10.5 migration notes](https://github.com/fjacquet/nbu_exporter/blob/main/docs/api-10.5-migration.md) - API 12.0 from NetBackup 10.5, 406 on unsupported versions, `kilobytesDataTransferred`
- [Veritas forum: NetBackup 11 API](https://vox.veritas.com/discussions/netbackup/netbackup-11-api---unexpected-error/907316) - requests with version 13.0 on NetBackup 11
