"""The SDK's entry point: NetBackupClient.

A facade: one object per NetBackup primary server (one NetBackup
domain), with a named group of calls for each kind of thing -
`nbu.jobs`, `nbu.policies`, `nbu.images`, `nbu.hosts`, `nbu.storage`,
`nbu.assets`, `nbu.server`.

    with NetBackupClient("https://nbu01.example.com:1556/netbackup", api_key=key) as nbu:
        for page in nbu.jobs.iter_pages(updated_after=since):
            ...

sdk-primer supplies the transport underneath (retry and backoff, typed
exceptions, per-request log correlation).

Written from Veritas's REST API documentation. **None of it has been run
against a NetBackup server.**
"""

from __future__ import annotations

import ssl
from pathlib import Path

import httpx
from sdk_primer import APIClient

from .auth import ApiKeyAuth, PasswordAuth
from .inventory import Assets, Hosts, Images, Policies, Server, Storage
from .jobs import Jobs
from .versions import ApiVersion

# Sent on every request. Only the policy endpoints read it: without it
# they answer in an older, per-policy-type shape.
DEFAULT_HEADERS = {"X-NetBackup-Policy-Use-Generic-Schema": "true"}


class NetBackupClient:
    """One connection to one NetBackup primary server.

    Give either `api_key`, or `username` and `password` (with
    `domain_type`, and `domain_name` for a Windows or LDAP domain).
    Read-only unless built with allow_changes=True.
    """

    def __init__(
        self,
        base_url: str,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        domain_type: str = "vx",
        domain_name: str | None = None,
        api_version: str = "auto",
        verify_tls: bool = True,
        ca_bundle: Path | None = None,
        page_size: int = 100,
        timeout: float = 120.0,
        allow_changes: bool = False,
    ) -> None:
        if not api_key and not (username and password):
            raise ValueError("Give api_key, or username and password.")
        # https://<primary>:1556/netbackup - paths (/admin/jobs, /login)
        # are added by the calls.
        self.base_url = base_url.rstrip("/")
        self.page_size = page_size
        self.allow_changes = allow_changes
        # "auto", a NetBackup release ("10.5") or an API version ("12.0").
        self.version = ApiVersion(api_version)

        verify: bool | ssl.SSLContext = verify_tls
        if verify_tls and ca_bundle is not None:
            verify = ssl.create_default_context(cafile=str(ca_bundle))

        self._login_client = httpx.Client(verify=verify, timeout=timeout)
        self._auth: ApiKeyAuth | PasswordAuth
        if api_key:
            self._auth = ApiKeyAuth(api_key, self.version)
        else:
            assert username and password
            self._auth = PasswordAuth(
                self.base_url,
                username,
                password,
                domain_type=domain_type,
                domain_name=domain_name,
                version=self.version,
                client=self._login_client,
            )

        self._api = APIClient(
            base_url=self.base_url,
            auth=self._auth,
            default_headers=DEFAULT_HEADERS,
            timeout=timeout,
            transport=httpx.HTTPTransport(verify=verify),
        )
        self._api_once = APIClient(
            base_url=self.base_url,
            auth=self._auth,
            default_headers=DEFAULT_HEADERS,
            timeout=timeout,
            max_attempts=1,
            transport=httpx.HTTPTransport(verify=verify),
        )

        self.server = Server(self)
        self.jobs = Jobs(self)
        self.policies = Policies(self)
        self.images = Images(self)
        self.hosts = Hosts(self)
        self.storage = Storage(self)
        self.assets = Assets(self)

    @property
    def api_version(self) -> str:
        """The API version in use - settled after the first successful call."""
        return self.version.current

    def close(self, *, logout: bool = True) -> None:
        if logout and isinstance(self._auth, PasswordAuth):
            self._auth.logout()
        self._api.close()
        self._api_once.close()
        self._login_client.close()

    def __enter__(self) -> NetBackupClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    @property
    def api(self) -> APIClient:
        """The authenticated transport, for an endpoint not wrapped yet."""
        return self._api

    @property
    def api_once(self) -> APIClient:
        """The transport for changing calls: one attempt, no retry."""
        return self._api_once
