from contextlib import asynccontextmanager
from typing import get_args

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from . import runtime
from .adapters.jev import AssessmentUnavailable, JevAdapter, Reason
from .adapters.jev_gate import GateUnavailable, JevGateAdapter
from .contracts import EncounterState, JevAssessment, JevGate

_DEFAULT = object()


def create_app(*, client=_DEFAULT) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app):
        active_client = client
        app.state.startup_reason = None
        if active_client is _DEFAULT:
            try:
                active_client = runtime.open_client()
            except AssessmentUnavailable as error:
                active_client = None
                app.state.startup_reason = error.reason
        app.state.jev = JevAdapter(active_client)
        app.state.jev_gate = JevGateAdapter(active_client)
        try:
            yield
        finally:
            if active_client is not None:
                await active_client.aclose()

    app = FastAPI(
        title="Jev synthetic encounter assessment",
        description="Simulation / education / shadow only. Not a clinical device.",
        lifespan=lifespan,
    )

    @app.post(
        "/v1/assess",
        response_model=JevAssessment,
        responses={
            503: {
                "description": "Assessment unavailable or invalid; returns a bounded reason code.",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": ["reason"],
                            "properties": {
                                "reason": {
                                    "type": "string",
                                    "enum": [
                                        "unauthorized",
                                        "rate_limited",
                                        "unavailable",
                                        "timeout",
                                        "invalid_response",
                                    ],
                                }
                            },
                            "additionalProperties": False,
                        }
                    }
                },
            }
        },
    )
    async def assess(state: EncounterState):
        try:
            if app.state.startup_reason:
                raise AssessmentUnavailable(app.state.startup_reason)
            return await app.state.jev.assess(state)
        except AssessmentUnavailable as error:
            return JSONResponse(status_code=503, content={"reason": error.reason})

    @app.post(
        "/v1/gate",
        response_model=JevGate,
        description="Synthetic, unvalidated gate. Mode hints are advisory; Python owns mode. "
        "Retrieve identifies a family pack only; no retrieval or reasoner runs.",
        responses={
            200: {
                "description": "Valid silence or family-pack decision.",
                "content": {
                    "application/json": {
                        "examples": {
                            "silence": {
                                "value": {
                                    "revision": 1,
                                    "outcome": "silence",
                                    "pack": None,
                                    "mode_hint": "neither",
                                    "mode_hint_advisory": True,
                                    "latency_ms": 25.0,
                                }
                            },
                            "retrieve": {
                                "value": {
                                    "revision": 1,
                                    "outcome": "retrieve",
                                    "pack": "other",
                                    "mode_hint": "rounds",
                                    "mode_hint_advisory": True,
                                    "latency_ms": 25.0,
                                }
                            },
                        }
                    }
                },
            },
            503: {
                "description": "Service failure or malformed response; bounded reason only.",
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "required": ["reason"],
                            "properties": {
                                "reason": {
                                    "type": "string",
                                    "enum": list(get_args(Reason)),
                                }
                            },
                            "additionalProperties": False,
                        }
                    }
                },
            },
        },
    )
    async def gate(state: EncounterState):
        try:
            if app.state.startup_reason:
                raise GateUnavailable(app.state.startup_reason)
            return await app.state.jev_gate.gate(state)
        except GateUnavailable as error:
            return JSONResponse(status_code=503, content={"reason": error.reason})

    return app
