"""Logging in to NetBackup, and asking for the right API version.

Two kinds of credential, both sent as the bare value of the
`Authorization` header (no "Bearer"):

- **An API key** - created in the web UI or with POST
  /security/api-keys, valid until its expiry date (often months). The
  better choice for a collector: nothing to log in with, no password
  kept anywhere.
- **A user name and password** - exchanged at POST /login for a JWT that
  is valid for 24 hours. This logs in on first use, and again when the
  token is near its end or a request comes back 401. `domain_type` is
  `vx` for a NetBackup user, `unixpwd` for a local Linux one, `nt` for
  Windows/Active Directory, with `domain_name` naming the domain.

Both set the API version on every request and, while the version is
still being worked out, retry a 406 with the next older one
(versions.py).
"""

from __future__ import annotations

import time
from collections.abc import Callable, Generator

import httpx
from loguru import logger
from sdk_primer import AuthenticationError

from .versions import ApiVersion

LOGIN_PATH = "/login"
LOGOUT_PATH = "/logout"
NOT_ACCEPTABLE = 406


def _with_version(
    version: ApiVersion, request: httpx.Request
) -> Generator[httpx.Request, httpx.Response, httpx.Response]:
    """Send `request`, stepping the API version down on each 406."""
    while True:
        version.apply(request)
        response = yield request
        if response.status_code == NOT_ACCEPTABLE and version.step_down():
            logger.info("NetBackup refused its API version; trying {}", version.current)
            continue
        if response.status_code < 400:
            if not version.settled:
                logger.info("NetBackup API version {}", version.current)
            version.settle()
        return response


class ApiKeyAuth(httpx.Auth):
    def __init__(self, api_key: str, version: ApiVersion) -> None:
        self._api_key = api_key
        self._version = version

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response]:
        request.headers["Authorization"] = self._api_key
        yield from _with_version(self._version, request)


class PasswordAuth(httpx.Auth):
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        *,
        domain_type: str,
        domain_name: str | None,
        version: ApiVersion,
        client: httpx.Client,
        renew_margin: float = 300.0,
        now: Callable[[], float] = time.monotonic,
    ) -> None:
        self._login_url = base_url.rstrip("/") + LOGIN_PATH
        self._logout_url = base_url.rstrip("/") + LOGOUT_PATH
        self._body = {
            "userName": username,
            "password": password,
            "domainType": domain_type,
            **({"domainName": domain_name} if domain_name else {}),
        }
        self._username = username
        self._version = version
        self._client = client
        self._renew_margin = renew_margin
        self._now = now
        self._token: str | None = None
        self._expires_at = 0.0

    def login(self) -> None:
        logger.info("Logging in to NetBackup as {}", self._username)
        while True:
            headers = {
                "Accept": f"application/vnd.netbackup+json;version={self._version.current}",
                "Content-Type": f"application/vnd.netbackup+json;version={self._version.current}",
            }
            response = self._client.post(self._login_url, json=self._body, headers=headers)
            if response.status_code == NOT_ACCEPTABLE and self._version.step_down():
                logger.info("NetBackup refused its API version; trying {}", self._version.current)
                continue
            break
        if response.status_code >= 400:
            raise AuthenticationError(
                f"NetBackup login failed for {self._username}: HTTP {response.status_code} "
                f"{response.text[:200]}"
            )
        self._version.settle()
        body = response.json()
        self._token = str(body["token"])
        self._expires_at = self._now() + float(body.get("validity", 86400))

    def logout(self) -> None:
        """End the session on the server. Best effort."""
        if self._token is None:
            return
        try:
            self._client.post(self._logout_url, headers={"Authorization": self._token})
        except httpx.HTTPError:
            pass
        self._token = None

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response]:
        fresh = False
        if self._token is None or self._now() >= self._expires_at - self._renew_margin:
            self.login()
            fresh = True
        request.headers["Authorization"] = str(self._token)
        response = yield from _with_version(self._version, request)
        if response.status_code == 401 and not fresh:
            logger.warning("NetBackup answered 401; logging in again and retrying once")
            self.login()
            request.headers["Authorization"] = str(self._token)
            yield from _with_version(self._version, request)
