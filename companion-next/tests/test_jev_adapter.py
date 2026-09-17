from typesafe_sdk import Choice

from cognitive_companion.adapters.jev import JevAdapter
from cognitive_companion.catalog import load_catalog
from cognitive_companion.contracts import EncounterState

from .fakes import PROBABILITIES, FakeSDK

STATE = EncounterState(session_id="synthetic-1", revision=7, transcript="Synthetic simulation.")


async def test_typed_choice_mapping_and_monotonic_latency():
    sdk = FakeSDK()
    ticks = iter([12., 12.025])
    result = await JevAdapter(sdk, clock=lambda: next(ticks)).assess(STATE)
    assert result.revision == 7
    assert result.selected_id == "anaphylaxis"
    assert dict(result.probabilities) == PROBABILITIES
    assert result.confidence == .73
    assert abs(result.latency_ms - 25) < .00001
    assert len(sdk.calls) == 1
    call = sdk.calls[0]
    assert call["model"] == "jev-latest"
    assert call["state"] == STATE.model_dump()
    assert set(call["questions"]) == {"algorithm"}
    q = call["questions"]["algorithm"]
    assert isinstance(q, Choice)
    assert q.criteria == dict(load_catalog())
    assert "transcript" in q.instructions
    assert call["retry"].max_retries == 0
    assert 0 < call["timeout"] <= 10
