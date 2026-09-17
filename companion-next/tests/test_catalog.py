import hashlib
import json
from pathlib import Path

import pytest

from cognitive_companion.catalog import CatalogError, load_catalog

PATH = Path(__file__).parents[1] / "config/scenarios.json"


def test_frozen_catalog():
    catalog = load_catalog()
    assert tuple(catalog) == ("anaphylaxis", "malignant_hyperthermia", "other_or_unclear")
    assert all(text.strip() for text in catalog.values())
    with pytest.raises(TypeError):
        catalog["other_or_unclear"] = "changed"
    data = json.loads(PATH.read_text())
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(canonical).hexdigest() == EXPECTED_DIGEST


@pytest.mark.parametrize("change", [
    lambda d: d["scenarios"].pop(),
    lambda d: d["scenarios"].append(d["scenarios"][0]),
    lambda d: d["scenarios"][0].update(id="unknown"),
    lambda d: d["scenarios"][0].update(criteria=" "),
    lambda d: d["scenarios"][0].update(criteria="changed"),
    lambda d: d.update(schema_version=2),
    lambda d: d.update(schema_version=True),
])
def test_reject_altered_catalog(tmp_path, change):
    data = json.loads(PATH.read_text())
    change(data)
    path = tmp_path / "catalog.json"
    path.write_text(json.dumps(data))
    with pytest.raises(CatalogError, match="invalid catalog"):
        load_catalog(path)


@pytest.mark.parametrize("content", [None, "{", "[]", "null"])
def test_missing_or_malformed(tmp_path, content):
    path = tmp_path / "catalog.json"
    if content is not None:
        path.write_text(content)
    with pytest.raises(CatalogError, match="invalid catalog"):
        load_catalog(path)

EXPECTED_DIGEST = "36f3e60b6ec6fc815e58544f2950ee9f199d0cba311e5d6e75c2a19687c58ef0"
