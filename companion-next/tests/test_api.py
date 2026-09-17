import pytest
from fastapi.testclient import TestClient

from cognitive_companion.api import create_app
from cognitive_companion.adapters.grok import GrokStandinAdapter
from cognitive_companion.adapters.literature import NullLiteratureAdapter

from .failure_cases import INVALID_RESPONSES, SENTINEL, SERVICE_FAILURES
from .fakes import FakeSDK, answer, response

FIXTURES = [
    ("anaphylaxis", "Synthetic simulation: abrupt hypotension, bronchospasm and urticaria after exposure."),
    ("malignant_hyperthermia", "Synthetic simulation: compatible exposure, rising end-tidal carbon dioxide and rigidity."),
    ("other_or_unclear", "Synthetic simulation: isolated fever; insufficient evidence."),
]


@pytest.fixture(autouse=True)
def unused_lane_tripwires(monkeypatch):
    async def forbidden(*args, **kwargs):
        pytest.fail("unused lane invoked")
    monkeypatch.setattr(GrokStandinAdapter, "assess", forbidden)
    monkeypatch.setattr(NullLiteratureAdapter, "assess", forbidden)


def payload(text="Synthetic simulation."):
    return dict(session_id="synthetic-api", revision=9, transcript=text)


@pytest.mark.parametrize("selected,text", FIXTURES)
def test_success(selected, text):
    sdk = FakeSDK(response(answer(choice=selected)))
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/assess", json=payload(text))
        assert result.status_code == 200
        data = result.json()
        assert set(data) == {"revision", "selected_id", "probabilities", "confidence", "latency_ms"}
        assert data["selected_id"] == selected
        assert data["revision"] == 9
        assert data["probabilities"] == sdk.result.choices["algorithm"].probabilities
        assert data["confidence"] == .73
        assert data["latency_ms"] >= 0
        assert len(sdk.calls) == 1
        schema = client.get("/openapi.json").json()
        assert schema["paths"]["/v1/assess"]["post"]["responses"]["200"]["content"]["application/json"]["schema"]["$ref"].endswith("JevAssessment")
    assert sdk.closed


@pytest.mark.parametrize("error,reason", SERVICE_FAILURES)
def test_service_errors(error, reason, caplog):
    with TestClient(create_app(client=FakeSDK(error=error))) as client:
        result = client.post("/v1/assess", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": reason}
    assert SENTINEL not in result.text + caplog.text


@pytest.mark.parametrize("result", INVALID_RESPONSES)
def test_malformed_response(result):
    with TestClient(create_app(client=FakeSDK(result))) as client:
        result = client.post("/v1/assess", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "invalid_response"}


@pytest.mark.parametrize("changes", [
    {"session_id": " "}, {"transcript": ""}, {"revision": 0},
    {"revision": True}, {"revision": "1"}, {"extra": "value"},
])
def test_invalid_input(changes):
    sdk = FakeSDK()
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/assess", json=payload() | changes)
    assert result.status_code == 422
    assert not sdk.calls


def test_unavailable_client():
    with TestClient(create_app(client=None)) as client:
        result = client.post("/v1/assess", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "unauthorized"}
