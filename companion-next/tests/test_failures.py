import asyncio
import traceback

import pytest

from cognitive_companion.adapters.jev import AssessmentUnavailable, JevAdapter
from cognitive_companion.catalog import CatalogError

from .failure_cases import INVALID_RESPONSES, SENTINEL, SERVICE_FAILURES
from .fakes import FakeSDK
from .test_jev_adapter import STATE


@pytest.mark.parametrize("error,reason", SERVICE_FAILURES)
async def test_service_failures(error, reason, caplog):
    client = FakeSDK(error=error)
    with pytest.raises(AssessmentUnavailable) as caught:
        await JevAdapter(client).assess(STATE)
    assert caught.value.reason == reason
    assert str(caught.value) == reason
    assert SENTINEL not in "".join(traceback.format_exception(caught.value))
    assert SENTINEL not in caplog.text
    assert len(client.calls) == 1


@pytest.mark.parametrize("result", INVALID_RESPONSES)
async def test_invalid_response(result):
    with pytest.raises(AssessmentUnavailable, match="invalid_response"):
        await JevAdapter(FakeSDK(result=result)).assess(STATE)


async def test_missing_client():
    with pytest.raises(AssessmentUnavailable, match="unauthorized"):
        await JevAdapter(None).assess(STATE)


async def test_invalid_catalog_prevents_call(monkeypatch):
    client = FakeSDK()
    def invalid():
        raise CatalogError(SENTINEL)
    monkeypatch.setattr("cognitive_companion.adapters.jev.load_catalog", invalid)
    with pytest.raises(AssessmentUnavailable, match="unavailable"):
        await JevAdapter(client).assess(STATE)
    assert not client.calls


async def test_wall_clock_timeout(monkeypatch):
    monkeypatch.setattr("cognitive_companion.adapters.jev.TIMEOUT_SECONDS", .01)
    class HangingSDK:
        async def system_one(self, **kwargs):
            await asyncio.sleep(1)
    with pytest.raises(AssessmentUnavailable, match="timeout"):
        await JevAdapter(HangingSDK()).assess(STATE)
