"""External credentials are read only during service lifespan or opted-in smoke."""

import logging
import shlex
import stat
from pathlib import Path

from pydantic import SecretStr
from typesafe_sdk import AsyncTypeSafeClient, RetryPolicy

from .adapters.jev import TIMEOUT_SECONDS, AssessmentUnavailable
from .catalog import load_catalog

SECRET_PATH = Path("/Users/senlabs/.hermes/secrets/typesafe.env")


def load_key(path: Path = SECRET_PATH) -> SecretStr | None:
    try:
        if stat.S_IMODE(path.stat().st_mode) != 0o600:
            return None
        for line in path.read_text().splitlines():
            parts = shlex.split(line, comments=True)
            if parts[:1] == ["export"]:
                parts = parts[1:]
            if len(parts) == 1 and parts[0].startswith("TYPESAFE_API_KEY="):
                value = parts[0].partition("=")[2].strip()
                return SecretStr(value) if value else None
    except (OSError, ValueError):
        pass
    return None


def open_client() -> AsyncTypeSafeClient:
    reason = "unavailable"
    try:
        load_catalog()
        key = load_key()
        if key is None:
            reason = "unauthorized"
        else:
            # SDK debug bodies are unnecessary for this service; keep them out of logs.
            logging.getLogger("typesafe_sdk").disabled = True
            return AsyncTypeSafeClient(
                api_key=key.get_secret_value(),
                model="jev-latest",
                base_url="https://api.typesafe.ai",
                retry=RetryPolicy(max_retries=0),
                timeout=TIMEOUT_SECONDS,
            )
    except Exception:  # noqa: BLE001 - sanitize the external SDK trust boundary
        reason = "unavailable"
    raise AssessmentUnavailable(reason)
