import pytest

from cognitive_companion.adapters.grok import GrokStandinAdapter
from cognitive_companion.adapters.literature import NullLiteratureAdapter


async def test_grok_tripwire():
    assert "temporary Grok 4.6 stand-in" in GrokStandinAdapter.__doc__
    with pytest.raises(NotImplementedError, match="not_in_slice"):
        await GrokStandinAdapter().assess(None)


async def test_literature_unavailable():
    assert await NullLiteratureAdapter().assess(None) == {
        "research_status": "unavailable"
    }
