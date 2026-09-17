import pytest
from fastapi.testclient import TestClient

from cognitive_companion.adapters.grok import GrokStandinAdapter
from cognitive_companion.adapters.literature import NullLiteratureAdapter
from cognitive_companion.api import create_app

from .failure_cases import INVALID_RESPONSES, SENTINEL, SERVICE_FAILURES
from .fakes import FakeSDK, answer, gate_response, response
from .test_jev_gate import INVALID_GATE_RESPONSES

FIXTURES = [
    (
        "anaphylaxis",
        "Synthetic simulation: abrupt hypotension, bronchospasm and urticaria after exposure.",
    ),
    (
        "malignant_hyperthermia",
        "Synthetic simulation: compatible exposure, rising end-tidal carbon dioxide and rigidity.",
    ),
    (
        "other_or_unclear",
        "Synthetic simulation: isolated fever; insufficient evidence.",
    ),
]


@pytest.fixture(autouse=True)
def unused_lane_tripwires(monkeypatch):
    async def forbidden(*args, **kwargs):
        pytest.fail("unused lane invoked")

    monkeypatch.setattr(GrokStandinAdapter, "assess", forbidden)
    monkeypatch.setattr(NullLiteratureAdapter, "assess", forbidden)


def payload(text="Synthetic simulation."):
    return {"session_id": "synthetic-api", "revision": 9, "transcript": text}


def test_openapi_service_unavailable():
    with TestClient(create_app(client=None)) as client:
        document = client.get("/openapi.json").json()
    responses = document["paths"]["/v1/assess"]["post"]["responses"]
    assert "503" in responses
    schema = responses["503"]["content"]["application/json"]["schema"]
    assert schema["type"] == "object"
    assert schema["required"] == ["reason"]
    assert set(schema["properties"]) == {"reason"}
    reason = schema["properties"]["reason"]
    assert reason["type"] == "string"
    assert set(reason["enum"]) == {
        "unauthorized",
        "rate_limited",
        "unavailable",
        "timeout",
        "invalid_response",
    }


@pytest.mark.parametrize("selected,text", FIXTURES)
def test_success(selected, text):
    sdk = FakeSDK(response(answer(choice=selected)))
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/assess", json=payload(text))
        assert result.status_code == 200
        data = result.json()
        assert set(data) == {
            "revision",
            "selected_id",
            "probabilities",
            "confidence",
            "latency_ms",
        }
        assert data["selected_id"] == selected
        assert data["revision"] == 9
        assert data["probabilities"] == sdk.result.choices["algorithm"].probabilities
        assert data["confidence"] == 0.73
        assert data["latency_ms"] >= 0
        assert len(sdk.calls) == 1
        schema = client.get("/openapi.json").json()
        assert schema["paths"]["/v1/assess"]["post"]["responses"]["200"]["content"][
            "application/json"
        ]["schema"]["$ref"].endswith("JevAssessment")
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


@pytest.mark.parametrize(
    "changes",
    [
        {"session_id": " "},
        {"transcript": ""},
        {"revision": 0},
        {"revision": True},
        {"revision": "1"},
        {"extra": "value"},
    ],
)
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


@pytest.mark.parametrize("decision,outcome", [(0.9, "retrieve"), (0.5, "silence")])
def test_gate_success_isolated(decision, outcome, monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("gate invoked assess or catalog loading")

    monkeypatch.setattr("cognitive_companion.adapters.jev.JevAdapter.assess", forbidden)
    monkeypatch.setattr("cognitive_companion.adapters.jev.load_catalog", forbidden)
    monkeypatch.setattr("cognitive_companion.catalog.load_catalog", forbidden)
    sdk = FakeSDK(gate_response(decision=decision))
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/gate", json=payload())
    assert result.status_code == 200
    data = result.json()
    assert set(data) == {
        "revision",
        "outcome",
        "pack",
        "mode_hint",
        "mode_hint_advisory",
        "latency_ms",
    }
    assert data["outcome"] == outcome
    assert data["pack"] == ("other" if outcome == "retrieve" else None)
    assert len(sdk.calls) == 1
    assert sdk.closed


@pytest.mark.parametrize("error,reason", SERVICE_FAILURES)
def test_gate_service_failures(error, reason, caplog):
    sdk = FakeSDK(error=error)
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/gate", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": reason}
    assert SENTINEL not in result.text + caplog.text
    assert len(sdk.calls) == 1


@pytest.mark.parametrize("response", INVALID_GATE_RESPONSES)
def test_gate_invalid_answers(response, caplog):
    with TestClient(create_app(client=FakeSDK(response))) as client:
        result = client.post("/v1/gate", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "invalid_response"}
    assert SENTINEL not in result.text + caplog.text


@pytest.mark.parametrize(
    "changes",
    [
        {"session_id": " "},
        {"transcript": ""},
        {"revision": 0},
        {"revision": True},
        {"revision": "1"},
        {"extra": "value"},
    ],
)
def test_gate_invalid_input(changes):
    sdk = FakeSDK()
    with TestClient(create_app(client=sdk)) as client:
        result = client.post("/v1/gate", json=payload() | changes)
    assert result.status_code == 422
    assert not sdk.calls


def test_gate_missing_client():
    with TestClient(create_app(client=None)) as client:
        result = client.post("/v1/gate", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "unauthorized"}


@pytest.mark.parametrize(
    "failure,reason",
    [
        ("credentials", "unauthorized"),
        ("catalog", "unavailable"),
        ("construction", "unavailable"),
    ],
)
def test_gate_startup_failures(failure, reason, monkeypatch, caplog):
    from pydantic import SecretStr

    from cognitive_companion import runtime

    def broken(*args, **kwargs):
        raise RuntimeError(SENTINEL)

    def forbidden(*args, **kwargs):
        pytest.fail("client constructed after startup validation failed")

    monkeypatch.setattr(
        runtime,
        "load_key",
        lambda: None if failure == "credentials" else SecretStr(SENTINEL),
    )
    monkeypatch.setattr(
        runtime,
        "AsyncTypeSafeClient",
        broken if failure == "construction" else forbidden,
    )
    if failure == "catalog":
        monkeypatch.setattr(runtime, "load_catalog", broken)
    with TestClient(create_app()) as client:
        result = client.post("/v1/gate", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": reason}
    assert SENTINEL not in result.text + caplog.text


def test_gate_openapi():
    with TestClient(create_app(client=None)) as client:
        document = client.get("/openapi.json").json()
    operation = document["paths"]["/v1/gate"]["post"]
    assert "advisory" in operation["description"]
    responses = operation["responses"]
    assert set(responses) == {"200", "422", "503"}
    success = responses["200"]["content"]["application/json"]
    assert set(success["examples"]) == {"silence", "retrieve"}
    assert success["schema"]["discriminator"]["propertyName"] == "outcome"
    assert len(success["schema"]["oneOf"]) == 2
    error = responses["503"]["content"]["application/json"]["schema"]
    assert error["additionalProperties"] is False
    assert error["required"] == ["reason"]
    assert set(error["properties"]) == {"reason"}
    assert set(error["properties"]["reason"]["enum"]) == {
        "unauthorized",
        "rate_limited",
        "unavailable",
        "timeout",
        "invalid_response",
    }
    fields = {
        "revision",
        "outcome",
        "pack",
        "mode_hint",
        "mode_hint_advisory",
        "latency_ms",
    }
    for name in ("JevGateSilence", "JevGateRetrieve"):
        schema = document["components"]["schemas"][name]
        assert set(schema["properties"]) == fields
        assert set(schema["required"]) == fields
        assert schema["additionalProperties"] is False
        assert "Advisory" in schema["properties"]["mode_hint_advisory"]["description"]
    assert not document["paths"]["/v1/assess"]["post"].get("deprecated", False)


def test_gate_and_assess_share_one_client(monkeypatch):
    from cognitive_companion import runtime

    class SharedSDK(FakeSDK):
        closes = 0

        async def aclose(self):
            self.closes += 1
            await super().aclose()

    sdk = SharedSDK()
    opened = []

    def open_client():
        opened.append(True)
        return sdk

    monkeypatch.setattr(runtime, "open_client", open_client)
    with TestClient(create_app()) as client:
        assert client.post("/v1/assess", json=payload()).status_code == 200
        sdk.result = gate_response()
        assert client.post("/v1/gate", json=payload()).status_code == 200
    assert len(opened) == 1
    assert len(sdk.calls) == 2
    assert sdk.closes == 1
