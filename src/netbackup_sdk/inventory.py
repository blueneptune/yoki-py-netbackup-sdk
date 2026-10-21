"""What exists and how it is protected: policies, backup images, hosts,
storage, and the workload assets NetBackup has discovered.

In NetBackup's terms: a *policy* says what to back up (its clients and
backup selections), when (its schedules) and where (a storage unit); a
*backup image* is one backup of one client, kept until it expires.
"Is this client protected, and since when?" is answered by its policies
and its newest image.
"""

from __future__ import annotations

from collections.abc import Iterator
from datetime import datetime
from typing import Any

from sdk_primer import NotFoundError

from ._base import Entities, Entity, Resource, all_of, flatten, quoted, timestamp

# The policy endpoints answer in one shape for every policy type only
# with X-NetBackup-Policy-Use-Generic-Schema: true, which the client
# sends on every request (client.DEFAULT_HEADERS).


class Policies(Resource):
    def list(self) -> Entities:
        """Every policy (GET /config/policies): name, type, and whether
        it is active."""
        return self._all("/config/policies")

    def get(self, name: str) -> Entity | None:
        """One policy in full - clients, schedules, backup selections
        (GET /config/policies/{name})."""
        try:
            body = self._get(f"/config/policies/{name}")
        except NotFoundError:
            return None
        return flatten(body.get("data", body))


class Images(Resource):
    def iter_pages(
        self,
        *,
        backed_up_after: datetime | None = None,
        backed_up_before: datetime | None = None,
        client: str | None = None,
        policy: str | None = None,
    ) -> Iterator[Entities]:
        """Backup images in the catalog (GET /catalog/images), a page at
        a time: backupId, clientName, policyName, policyType,
        scheduleType, backupTime, expiration, kilobytes, ..."""
        query = all_of(
            f"backupTime ge {timestamp(backed_up_after)}" if backed_up_after else None,
            f"backupTime lt {timestamp(backed_up_before)}" if backed_up_before else None,
            f"clientName eq {quoted(client)}" if client else None,
            f"policyName eq {quoted(policy)}" if policy else None,
        )
        for page in self._pages("/catalog/images", {"filter": query, "sort": "-backupTime"}):
            yield [flatten(item) for item in page]

    def latest(self, client: str) -> Entity | None:
        """A client's newest backup image - one request."""
        params: dict[str, Any] = {
            "filter": f"clientName eq {quoted(client)}",
            "sort": "-backupTime",
        }
        items, _ = self._page("/catalog/images", params, 0, 1)
        return flatten(items[0]) if items else None


class Hosts(Resource):
    def list(self) -> Entities:
        """Hosts the primary server knows (GET /config/hosts): hostName,
        uuid, operating system, and whether it is a media server or a
        client."""
        return self._all("/config/hosts")


class Storage(Resource):
    def units(self) -> Entities:
        """Storage units (GET /storage/storage-units)."""
        return self._all("/storage/storage-units")

    def disk_pools(self) -> Entities:
        """Disk pools with their capacity and use (GET /storage/disk-pools)."""
        return self._all("/storage/disk-pools")


class Assets(Resource):
    def workload(self, workload: str, *, extra_filter: str | None = None) -> Entities:
        """Assets NetBackup has discovered for one workload - `vmware`,
        `mssql`, `oracle`, ... (GET /asset-service/workloads/{w}/assets)."""
        return self._all(f"/asset-service/workloads/{workload}/assets", {"filter": extra_filter})


class Server(Resource):
    def ping(self) -> Entity:
        """The primary server's time (GET /ping) - the cheapest call that
        proves the server is answering and the API version is accepted."""
        body = self._get("/ping")
        return body if isinstance(body, dict) else {"answer": body}
