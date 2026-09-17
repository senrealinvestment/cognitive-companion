import pytest
from pydantic import ValidationError

from cognitive_companion.contracts import EncounterState, JevAssessment

BASE = dict(revision=3, selected_id="anaphylaxis",
            probabilities=dict(anaphylaxis=.8, malignant_hyperthermia=.1, other_or_unclear=.1),
            confidence=.8, latency_ms=12.5)


@pytest.mark.parametrize("field,value", [
    ("session_id", ""), ("session_id", "  "), ("transcript", "\n"),
    ("revision", 0), ("revision", -1), ("revision", True),
    ("revision", 1.5), ("revision", "1"),
])
def test_invalid_encounter(field, value):
    data = dict(session_id="synthetic-1", revision=1, transcript="Synthetic text")
    data[field] = value
    with pytest.raises(ValidationError):
        EncounterState(**data)


@pytest.mark.parametrize("field,value", [
    ("selected_id", "unknown"), ("revision", 0), ("revision", True),
    *[(f, v) for f in ("confidence", "latency_ms")
      for v in (float("nan"), float("inf"), -1, True, "0.5")],
    ("confidence", 1.1),
    *[("probabilities", p) for p in (
        {}, {"anaphylaxis": 1},
        dict(BASE["probabilities"], extra=0),
        dict(BASE["probabilities"], anaphylaxis=.9),
        *[dict(BASE["probabilities"], anaphylaxis=v)
          for v in (float("nan"), float("inf"), -.1, 1.1, True, "0.8")]
    )],
])
def test_invalid_assessment(field, value):
    with pytest.raises(ValidationError):
        JevAssessment(**(BASE | {field: value}))


@pytest.mark.parametrize("mass,accepted", [(.991, True), (1.009, True), (.989, False), (1.011, False)])
def test_mass_preserved(mass, accepted):
    p = dict(anaphylaxis=mass-.2, malignant_hyperthermia=.1, other_or_unclear=.1)
    if not accepted:
        with pytest.raises(ValidationError):
            JevAssessment(**(BASE | {"probabilities": p}))
        return
    result = JevAssessment(**(BASE | {"probabilities": p}))
    assert result.model_dump()["probabilities"] == p
    p["anaphylaxis"] = 0
    assert result.probabilities["anaphylaxis"] == mass-.2
    with pytest.raises(TypeError):
        result.probabilities["anaphylaxis"] = 0
    with pytest.raises(ValidationError):
        result.revision = 4
