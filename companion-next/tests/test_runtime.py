import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr

from cognitive_companion import runtime
from cognitive_companion.adapters.jev import AssessmentUnavailable
from cognitive_companion.api import create_app

from .failure_cases import SENTINEL
from .fakes import FakeSDK
from .test_api import payload


def test_secret_file_loading(tmp_path):
    path = tmp_path / "credentials"
    path.write_text('export TYPESAFE_API_KEY="' + SENTINEL + '"\n')
    path.chmod(0o600)
    key = runtime.load_key(path)
    assert key.get_secret_value() == SENTINEL
    assert SENTINEL not in repr(key)


@pytest.mark.parametrize(
    "content,mode",
    [
        (None, 0o600),
        ("", 0o600),
        ("TYPESAFE_API_KEY=   ", 0o600),
        ("TYPESAFE_API_KEY=x", 0o644),
        ('TYPESAFE_API_KEY="unterminated', 0o600),
    ],
)
def test_missing_or_unsafe_credentials(tmp_path, content, mode):
    path = tmp_path / "credentials"
    if content is not None:
        path.write_text(content)
        path.chmod(mode)
    assert runtime.load_key(path) is None


def test_runtime_client_options(monkeypatch):
    calls = []
    fake = FakeSDK()
    monkeypatch.setattr(runtime, "load_key", lambda: SecretStr(SENTINEL))

    def factory(**kwargs):
        calls.append(kwargs)
        return fake

    monkeypatch.setattr(runtime, "AsyncTypeSafeClient", factory)
    with TestClient(create_app()) as client:
        assert client.post("/v1/assess", json=payload()).status_code == 200
    assert fake.closed
    assert len(calls) == 1
    assert calls[0]["retry"].max_retries == 0
    assert calls[0]["timeout"] == 10
    assert calls[0]["model"] == "jev-latest"
    assert calls[0]["base_url"] == "https://api.typesafe.ai"


def test_missing_credentials_prevent_client_creation(monkeypatch):
    monkeypatch.setattr(runtime, "load_key", lambda: None)

    def forbidden(**kwargs):
        pytest.fail("SDK created without credentials")

    monkeypatch.setattr(runtime, "AsyncTypeSafeClient", forbidden)
    with TestClient(create_app()) as client:
        result = client.post("/v1/assess", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "unauthorized"}


def test_invalid_catalog_prevents_client_creation(monkeypatch):
    def invalid():
        raise ValueError(SENTINEL)

    def forbidden(**kwargs):
        pytest.fail("SDK created for invalid catalog")

    monkeypatch.setattr(runtime, "load_catalog", invalid)
    monkeypatch.setattr(runtime, "AsyncTypeSafeClient", forbidden)
    with TestClient(create_app()) as client:
        result = client.post("/v1/assess", json=payload())
    assert result.status_code == 503
    assert result.json() == {"reason": "unavailable"}


def test_client_creation_error_sanitized(monkeypatch, caplog):
    monkeypatch.setattr(runtime, "load_key", lambda: SecretStr(SENTINEL))

    def broken(**kwargs):
        raise RuntimeError(SENTINEL)

    monkeypatch.setattr(runtime, "AsyncTypeSafeClient", broken)
    with pytest.raises(AssessmentUnavailable) as caught:
        runtime.open_client()
    assert SENTINEL not in str(caught.value) + caplog.text
    assert caught.value.__context__ is None
