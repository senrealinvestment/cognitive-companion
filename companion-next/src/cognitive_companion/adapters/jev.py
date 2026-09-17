import time

from typesafe_sdk import Choice, RetryPolicy

from ..catalog import load_catalog
from ..contracts import EncounterState, JevAssessment

TIMEOUT_SECONDS = 10.0


class JevAdapter:
    def __init__(self, client, *, clock=time.monotonic):
        self.client = client
        self.clock = clock

    async def assess(self, state: EncounterState) -> JevAssessment:
        criteria = dict(load_catalog())
        start = self.clock()
        response = await self.client.system_one(
            state=state.model_dump(),
            questions={"algorithm": Choice(
                instructions="Classify the synthetic encounter in transcript using the criteria.",
                criteria=criteria,
            )},
            model="jev-latest",
            retry=RetryPolicy(max_retries=0),
            timeout=TIMEOUT_SECONDS,
        )
        answer = response.choices["algorithm"]
        return JevAssessment(
            revision=state.revision,
            selected_id=answer.choice,
            probabilities=answer.probabilities,
            confidence=answer.confidence,
            latency_ms=(self.clock() - start) * 1000,
        )
