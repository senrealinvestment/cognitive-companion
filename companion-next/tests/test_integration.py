import pytest

from cognitive_companion.adapters.jev import JevAdapter
from cognitive_companion.contracts import EncounterState
from cognitive_companion.runtime import load_key, open_client


@pytest.mark.integration
async def test_hosted_nonmedical_smoke(request):
    if not request.config.getoption("--live"):
        pytest.skip("Requires explicit --live opt-in")
    if load_key() is None:
        pytest.skip("External credential unavailable")
    client = open_client()
    try:
        result = await JevAdapter(client).assess(
            EncounterState(
                session_id="synthetic-nonmedical-smoke",
                revision=1,
                transcript="Synthetic text: a blue bicycle is parked beside a library.",
            )
        )
        assert result.revision == 1
        assert result.selected_id == "other_or_unclear"
    finally:
        await client.aclose()
