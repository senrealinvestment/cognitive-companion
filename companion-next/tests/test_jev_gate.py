import asyncio
import math
import traceback
from types import SimpleNamespace

import pytest
from pydantic import TypeAdapter, ValidationError
from typesafe_sdk import Choice, ChoiceAnswer, Noul, NoulAnswer, SystemOneResponse
from typesafe_sdk._core.response_types import Usage

from cognitive_companion.adapters.jev_gate import (
    GateUnavailable,
    JevGateAdapter,
    decide_gate,
)
from cognitive_companion.contracts import GateJudgments, JevGate

from .failure_cases import SENTINEL, SERVICE_FAILURES
from .fakes import FakeSDK, gate_response
from .test_jev_adapter import STATE


def judgments(result=None):
    result = result or gate_response()
    return GateJudgments(
        decision_shaped=result.nouls["decision_shaped"].noul,
        enough_evidence=result.nouls["enough_evidence"].noul,
        mode_hint=vars(result.choices["mode_hint"]),
        family=vars(result.choices["family"]),
    )


@pytest.mark.parametrize("mode", ["emergency", "rounds"])
@pytest.mark.parametrize("family", ["airway", "circulation", "metabolic", "other"])
async def test_retrieve_and_request(mode, family):
    sdk = FakeSDK(gate_response(mode=mode, family=family))
    ticks = iter([12.0, 12.025])
    result = await JevGateAdapter(sdk, clock=lambda: next(ticks)).gate(STATE)
    assert result.outcome == "retrieve"
    assert result.reasons == ["gate_passed"]
    assert result.pack == family
    assert result.mode_hint == mode
    assert result.mode_hint_advisory is True
    assert result.revision == STATE.revision
    assert result.latency_ms == pytest.approx(25)
    assert len(sdk.calls) == 1
    call = sdk.calls[0]
    assert call["state"] == STATE.model_dump()
    assert call["model"] == "jev-latest"
    assert call["retry"].max_retries == 0
    assert 0 < call["timeout"] <= 10
    questions = call["questions"]
    assert set(questions) == {
        "decision_shaped",
        "enough_evidence",
        "mode_hint",
        "family",
    }
    for name, question in questions.items():
        assert isinstance(
            question, Noul if name in ("decision_shaped", "enough_evidence") else Choice
        )
        assert "Synthetic" in question.instructions
        assert "unvalidated" in question.instructions
        assert "data" in question.instructions
        assert "transcript" in question.instructions
    assert set(questions["mode_hint"].criteria) == {"emergency", "rounds", "neither"}
    assert set(questions["family"].criteria) == {
        "airway",
        "circulation",
        "metabolic",
        "other",
    }


@pytest.mark.parametrize(
    "field,threshold",
    [
        ("decision_shaped", 0.8),
        ("enough_evidence", 0.8),
        ("mode_hint", 0.7),
        ("family", 0.7),
    ],
)
@pytest.mark.parametrize("direction", [-1, 0, 1])
def test_exact_boundaries(field, threshold, direction):
    value = (
        math.nextafter(threshold, 0 if direction < 0 else 1) if direction else threshold
    )
    result = gate_response()
    if field in result.nouls:
        result.nouls[field].noul = value
    else:
        result.choices[field].confidence = value
    gate = decide_gate(STATE, judgments(result), latency_ms=0)
    assert gate.outcome == ("silence" if direction < 0 else "retrieve")
    assert gate.pack == (None if direction < 0 else "other")
    codes = {
        "decision_shaped": "decision_shaped_below_threshold",
        "enough_evidence": "insufficient_evidence",
        "mode_hint": "mode_confidence_below_threshold",
        "family": "family_confidence_below_threshold",
    }
    assert gate.reasons == [codes[field] if direction < 0 else "gate_passed"]


@pytest.mark.parametrize(
    "changes,reasons",
    [
        ({"mode": "neither"}, ["mode_neither"]),
        ({"decision": 0.5}, ["decision_shaped_below_threshold"]),
        ({"evidence": 0.5}, ["insufficient_evidence"]),
        (
            {"decision": 0, "evidence": 0, "mode": "neither"},
            [
                "decision_shaped_below_threshold",
                "insufficient_evidence",
                "mode_neither",
            ],
        ),
    ],
)
def test_silence(changes, reasons):
    result = decide_gate(STATE, judgments(gate_response(**changes)), latency_ms=0)
    assert result.outcome == "silence"
    assert result.pack is None
    assert result.reasons == reasons


@pytest.mark.parametrize("field", ["mode_hint", "family"])
def test_ties_are_valid_silence(field):
    result = gate_response()
    choice = result.choices[field]
    other = next(k for k in choice.probabilities if k != choice.choice)
    choice.probabilities = {
        k: 0.5 if k in (other, choice.choice) else 0 for k in choice.probabilities
    }
    decision = decide_gate(STATE, judgments(result), latency_ms=0)
    assert decision.outcome == "silence"
    assert decision.reasons == ["mode_tied" if field == "mode_hint" else "family_tied"]


def malformed_responses():
    yield SimpleNamespace()
    for field in ("decision_shaped", "enough_evidence", "mode_hint", "family"):
        for mutation in ("missing", "wrong"):
            result = gate_response(
                decision=0
            )  # Even apparent silence must validate every answer.
            group = result.nouls if field in result.nouls else result.choices
            if mutation == "missing":
                del group[field]
            else:
                group[field] = SimpleNamespace(score=0.9)
            yield result
        for value in (
            float("nan"),
            float("inf"),
            -float("inf"),
            -0.1,
            1.1,
            True,
            "0.8",
        ):
            result = gate_response()
            if field in result.nouls:
                result.nouls[field].noul = value
                yield result
            else:
                result.choices[field].confidence = value
                yield result
                result = gate_response()
                choice = result.choices[field]
                choice.probabilities[choice.choice] = value
                yield result
    for field in ("mode_hint", "family"):
        for mutation in ("label", "missing", "extra", "mass", "inconsistent"):
            result = gate_response(decision=0)
            choice = result.choices[field]
            if mutation == "label":
                choice.choice = "unknown"
            elif mutation == "missing":
                del choice.probabilities[next(iter(choice.probabilities))]
            elif mutation == "extra":
                choice.probabilities["extra"] = 0
            elif mutation == "mass":
                choice.probabilities[choice.choice] = 0.5
            else:
                choice.choice = next(
                    k for k in choice.probabilities if k != choice.choice
                )
            yield result


INVALID_GATE_RESPONSES = list(malformed_responses())


@pytest.mark.parametrize("result", INVALID_GATE_RESPONSES)
async def test_malformed(result):
    sdk = FakeSDK(result)
    with pytest.raises(GateUnavailable, match="invalid_response"):
        await JevGateAdapter(sdk).gate(STATE)
    assert len(sdk.calls) == 1


@pytest.mark.parametrize("error,reason", SERVICE_FAILURES)
async def test_failures(error, reason, caplog):
    sdk = FakeSDK(error=error)
    with pytest.raises(GateUnavailable) as caught:
        await JevGateAdapter(sdk).gate(STATE)
    assert caught.value.reason == reason
    assert caught.value.__context__ is None
    assert (
        SENTINEL not in "".join(traceback.format_exception(caught.value)) + caplog.text
    )
    assert len(sdk.calls) == 1


async def test_missing_client():
    with pytest.raises(GateUnavailable, match="unauthorized"):
        await JevGateAdapter(None).gate(STATE)


async def test_deadline_and_cancellation(monkeypatch):
    monkeypatch.setattr("cognitive_companion.adapters.jev_gate.TIMEOUT_SECONDS", 0.01)
    calls = []

    class HangingSDK:
        async def system_one(self, **kwargs):
            calls.append(kwargs)
            await asyncio.sleep(10)

    with pytest.raises(GateUnavailable, match="timeout"):
        await JevGateAdapter(HangingSDK()).gate(STATE)
    assert len(calls) == 1
    with pytest.raises(asyncio.CancelledError):
        await JevGateAdapter(FakeSDK(error=asyncio.CancelledError())).gate(STATE)


@pytest.mark.parametrize("mass", [0.99, 1.01])
def test_mass_inclusive_and_preserved(mass):
    result = gate_response()
    result.choices["family"].probabilities = {
        "airway": 0.01,
        "circulation": 0,
        "metabolic": 0,
        "other": mass - 0.01,
    }
    validated = judgments(result)
    assert (
        dict(validated.family.probabilities) == result.choices["family"].probabilities
    )


def test_immutable_and_copied():
    raw = gate_response()
    validated = judgments(raw)
    raw.choices["family"].probabilities["other"] = 0
    assert validated.family.probabilities["other"] == 1
    with pytest.raises(TypeError):
        validated.family.probabilities["other"] = 0
    with pytest.raises(ValidationError):
        validated.family.confidence = 0
    with pytest.raises(ValidationError):
        validated.decision_shaped = 0
    with pytest.raises(ValidationError):
        GateJudgments(**validated.model_dump(), extra=True)


@pytest.mark.parametrize(
    "changes",
    [
        {"reasons": []},
        {"reasons": ["model-generated explanation"]},
        {"reasons": ["gate_passed"]},
        {"request_id": ""},
        {"request_id": " "},
        {"request_id": None},
        {"pack": "airway"},
        {"extra": True},
        {"latency_ms": float("nan")},
        {"mode_hint_advisory": False},
        {"outcome": "retrieve", "pack": None},
        {"outcome": "retrieve", "pack": "other", "mode_hint": "neither"},
    ],
)
def test_public_contract_rejects(changes):
    data = {
        "revision": 1,
        "outcome": "silence",
        "pack": None,
        "mode_hint": "rounds",
        "mode_hint_advisory": True,
        "latency_ms": 0,
        "reasons": ["insufficient_evidence"],
        "request_id": "server-generated-test-id",
    }
    with pytest.raises(ValidationError):
        TypeAdapter(JevGate).validate_python(data | changes)


@pytest.mark.parametrize("outcome", ["silence", "retrieve"])
@pytest.mark.parametrize(
    "field",
    [
        "revision",
        "outcome",
        "pack",
        "mode_hint",
        "mode_hint_advisory",
        "latency_ms",
        "reasons",
        "request_id",
    ],
)
def test_all_public_fields_required(outcome, field):
    data = {
        "revision": 1,
        "outcome": outcome,
        "pack": "other" if outcome == "retrieve" else None,
        "mode_hint": "rounds",
        "mode_hint_advisory": True,
        "latency_ms": 0,
    }
    data["reasons"] = [
        "gate_passed" if outcome == "retrieve" else "insufficient_evidence"
    ]
    data["request_id"] = "server-generated-test-id"
    TypeAdapter(JevGate).validate_python(data)
    del data[field]
    with pytest.raises(ValidationError):
        TypeAdapter(JevGate).validate_python(data)


async def test_installed_sdk_answer_objects():
    raw = gate_response()
    result = SystemOneResponse(
        model="jev-latest",
        usage=Usage(input_tokens=10, output_tokens=10),
        answers={
            **{k: NoulAnswer(noul=v.noul) for k, v in raw.nouls.items()},
            **{k: ChoiceAnswer(**vars(v)) for k, v in raw.choices.items()},
        },
    )
    assert (await JevGateAdapter(FakeSDK(result)).gate(STATE)).outcome == "retrieve"


@pytest.mark.parametrize("mass", [math.nextafter(0.99, 0), math.nextafter(1.01, 2)])
def test_mass_immediately_outside_tolerance(mass):
    result = gate_response()
    result.choices["family"].probabilities = {
        "airway": 0.01,
        "circulation": 0,
        "metabolic": 0,
        "other": mass - 0.01,
    }
    with pytest.raises(ValidationError):
        judgments(result)


@pytest.mark.parametrize("outcome", ["silence", "retrieve"])
def test_public_contract_frozen(outcome):
    gate = decide_gate(
        STATE,
        judgments(gate_response(decision=0 if outcome == "silence" else 1)),
        latency_ms=0,
    )
    with pytest.raises(ValidationError):
        gate.revision = 2


@pytest.mark.parametrize(
    "field", ["decision_shaped", "enough_evidence", "mode_hint", "family"]
)
async def test_sdk_wrong_primitive(field):
    raw = gate_response(decision=0)
    answers = {
        **{k: NoulAnswer(noul=v.noul) for k, v in raw.nouls.items()},
        **{k: ChoiceAnswer(**vars(v)) for k, v in raw.choices.items()},
    }
    answers[field] = (
        NoulAnswer(noul=0.9)
        if field in raw.choices
        else ChoiceAnswer(choice="other", confidence=1, probabilities={"other": 1})
    )
    result = SystemOneResponse(
        model="jev-latest",
        usage=Usage(input_tokens=1, output_tokens=1),
        answers=answers,
    )
    with pytest.raises(GateUnavailable, match="invalid_response"):
        await JevGateAdapter(FakeSDK(result)).gate(STATE)


def test_all_failures_reported_in_policy_order():
    raw = gate_response(decision=0, evidence=0, mode="neither")
    for choice in raw.choices.values():
        choice.confidence = 0.1
        other = next(k for k in choice.probabilities if k != choice.choice)
        choice.probabilities = {
            k: 0.5 if k in (other, choice.choice) else 0 for k in choice.probabilities
        }
    decision = decide_gate(STATE, judgments(raw), latency_ms=0)
    assert decision.outcome == "silence"
    assert decision.reasons == [
        "decision_shaped_below_threshold",
        "insufficient_evidence",
        "mode_neither",
        "mode_confidence_below_threshold",
        "family_confidence_below_threshold",
        "mode_tied",
        "family_tied",
    ]


@pytest.mark.parametrize(
    "reasons",
    [[], ["insufficient_evidence"], ["explanation"], ["gate_passed", "gate_passed"]],
)
def test_retrieve_reason_contract(reasons):
    decision = decide_gate(STATE, judgments(), latency_ms=0)
    data = decision.model_dump() | {"request_id": "test-id"}
    TypeAdapter(JevGate).validate_python(data)
    with pytest.raises(ValidationError):
        TypeAdapter(JevGate).validate_python(data | {"reasons": reasons})
