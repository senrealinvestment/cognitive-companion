from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .adapters.jev import AssessmentUnavailable, JevAdapter
from .contracts import EncounterState, JevAssessment
from . import runtime

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

    @app.post("/v1/assess", response_model=JevAssessment)
    async def assess(state: EncounterState):
        try:
            if app.state.startup_reason:
                raise AssessmentUnavailable(app.state.startup_reason)
            return await app.state.jev.assess(state)
        except AssessmentUnavailable as error:
            return JSONResponse(status_code=503, content={"reason": error.reason})

    return app
