import pytest
from pydantic import ValidationError

from cognitive_companion.contracts import EncounterState, JevAssessment

BASE = {
    "revision": 3,
    "selected_id": "anaphylaxis",
    "probabilities": {
        "anaphylaxis": 0.8,
        "malignant_hyperthermia": 0.1,
        "other_or_unclear": 0.1,
    },
    "confidence": 0.8,
    "latency_ms": 12.5,
}


@pytest.mark.parametrize(
    "field,value",
    [
        ("session_id", ""),
        ("session_id", "  "),
        ("transcript", "\n"),
        ("revision", 0),
        ("revision", -1),
        ("revision", True),
        ("revision", 1.5),
        ("revision", "1"),
    ],
)
def test_invalid_encounter(field, value):
    data = {"session_id": "synthetic-1", "revision": 1, "transcript": "Synthetic text"}
    data[field] = value
    with pytest.raises(ValidationError):
        EncounterState(**data)


@pytest.mark.parametrize(
    "field,value",
    [
        ("selected_id", "unknown"),
        ("revision", 0),
        ("revision", True),
        *[
            (f, v)
            for f in ("confidence", "latency_ms")
            for v in (float("nan"), float("inf"), -1, True, "0.5")
        ],
        ("confidence", 1.1),
        *[
            ("probabilities", p)
            for p in (
                {},
                {"anaphylaxis": 1},
                dict(BASE["probabilities"], extra=0),
                dict(BASE["probabilities"], anaphylaxis=0.9),
                *[
                    dict(BASE["probabilities"], anaphylaxis=v)
                    for v in (float("nan"), float("inf"), -0.1, 1.1, True, "0.8")
                ],
            )
        ],
    ],
)
def test_invalid_assessment(field, value):
    with pytest.raises(ValidationError):
        JevAssessment(**(BASE | {field: value}))


@pytest.mark.parametrize(
    "mass,accepted", [(0.991, True), (1.009, True), (0.989, False), (1.011, False)]
)
def test_mass_preserved(mass, accepted):
    p = {
        "anaphylaxis": mass - 0.2,
        "malignant_hyperthermia": 0.1,
        "other_or_unclear": 0.1,
    }
    if not accepted:
        with pytest.raises(ValidationError):
            JevAssessment(**(BASE | {"probabilities": p}))
        return
    result = JevAssessment(**(BASE | {"probabilities": p}))
    assert result.model_dump()["probabilities"] == p
    p["anaphylaxis"] = 0
    assert result.probabilities["anaphylaxis"] == mass - 0.2
    with pytest.raises(TypeError):
        result.probabilities["anaphylaxis"] = 0
    with pytest.raises(ValidationError):
        result.revision = 4


@pytest.mark.parametrize("probability", [0.79, 0.81])
def test_inclusive_mass_boundary(probability):
    values = {
        "anaphylaxis": probability,
        "malignant_hyperthermia": 0.1,
        "other_or_unclear": 0.1,
    }
    assert JevAssessment(**(BASE | {"probabilities": values})).probabilities == values
