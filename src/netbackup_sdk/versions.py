"""Which NetBackup API version to ask for.

Every request names an API version in its media type
(`application/vnd.netbackup+json;version=13.0`), and a server answers
406 Not Acceptable to a version it does not support. Each NetBackup
release supports its own API version and some older ones; old ones are
eventually dropped. Maintenance releases (10.0.0.1, 10.5.0.1, 11.0.0.1)
keep their release's API version.

| NetBackup | API version |
|---|---|
| 11.0 (11.0.0.1) | 13.0 |
| 10.5 (10.5.0.1) | 12.0 |
| 10.0 (10.0.0.1) | 7.0 |

With `api_version="auto"` (the default) the client starts at the newest
version it knows and steps down on each 406 until the server accepts
one, then keeps it for the rest of the session. A fixed version is never
changed.

Sources: Veritas's API guide for 10.0 (versions up to 7.0), the
NetBackup 10.5 migration notes of nbu_exporter ("NetBackup 10.5 and
later support API version 12.0", 406 otherwise), and NetBackup 11
requests using version 13.0. None of it checked against a server yet.
"""

from __future__ import annotations

# Newest first: the order "auto" tries them in.
KNOWN = {"11.0": "13.0", "10.5": "12.0", "10.0": "7.0"}
AUTO_ORDER = ["13.0", "12.0", "7.0"]


def media_type(version: str) -> str:
    return f"application/vnd.netbackup+json;version={version}"


class ApiVersion:
    """The version a client is using, shared by its login and its calls."""

    def __init__(self, requested: str = "auto") -> None:
        if requested == "auto":
            self.candidates = list(AUTO_ORDER)
        elif requested in KNOWN:  # a NetBackup release, e.g. "10.5"
            self.candidates = [KNOWN[requested]]
        else:  # an API version, e.g. "12.0"
            self.candidates = [requested]
        self.fixed = requested != "auto"
        self.current = self.candidates[0]
        self.settled = self.fixed

    def apply(self, request: object) -> None:
        headers = request.headers  # type: ignore[attr-defined]
        headers["Accept"] = media_type(self.current)
        if headers.get("Content-Type", "").startswith("application/"):
            headers["Content-Type"] = media_type(self.current)

    def step_down(self) -> bool:
        """After a 406: move to the next older version. False if there is
        none left to try (or the version was fixed)."""
        if self.settled:
            return False
        index = self.candidates.index(self.current)
        if index + 1 >= len(self.candidates):
            return False
        self.current = self.candidates[index + 1]
        return True

    def settle(self) -> None:
        """The server accepted the current version: stop trying others."""
        self.settled = True
