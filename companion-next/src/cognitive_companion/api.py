from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .adapters.jev import AssessmentUnavailable, JevAdapter
from .contracts import EncounterState, JevAssessment


def create_app(*, client=None) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app):
        app.state.jev = JevAdapter(client)
        try:
            yield
        finally:
            if client is not None:
                await client.aclose()

    app = FastAPI(
        title="Jev synthetic encounter assessment",
        description="Simulation / education / shadow only. Not a clinical device.",
        lifespan=lifespan,
    )

    @app.post("/v1/assess", response_model=JevAssessment)
    async def assess(state: EncounterState):
        try:
            return await app.state.jev.assess(state)
        except AssessmentUnavailable as error:
            return JSONResponse(status_code=503, content={"reason": error.reason})

    return app
