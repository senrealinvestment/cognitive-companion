"""Frozen demo source: parent architecture plan Task 1.2; review unverified."""
import hashlib
import json
from pathlib import Path
from types import MappingProxyType

CATALOG_PATH = Path(__file__).parents[2] / "config/scenarios.json"
FROZEN_DIGEST = "36f3e60b6ec6fc815e58544f2950ee9f199d0cba311e5d6e75c2a19687c58ef0"
IDS = ("anaphylaxis", "malignant_hyperthermia", "other_or_unclear")


class CatalogError(ValueError):
    pass


def load_catalog(path: Path = CATALOG_PATH):
    try:
        data = json.loads(path.read_text())
        canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        if hashlib.sha256(canonical).hexdigest() != FROZEN_DIGEST:
            raise ValueError
        return MappingProxyType({item["id"]: item["criteria"] for item in data["scenarios"]})
    except (OSError, ValueError, TypeError, KeyError):
        raise CatalogError("invalid catalog") from None
