import asyncio
import time
from typing import Literal

from typesafe_sdk import (
    Choice,
    RetryPolicy,
    TypeSafeAPIConnectionError,
    TypeSafeAPIError,
    TypeSafeAPIResponseValidationError,
)

from ..catalog import CatalogError, load_catalog
from ..contracts import EncounterState, JevAssessment

TIMEOUT_SECONDS = 10.0
Reason = Literal["unauthorized", "rate_limited", "unavailable", "timeout", "invalid_response"]


class AssessmentUnavailable(Exception):
    def __init__(self, reason: Reason):
        self.reason = reason
        super().__init__(reason)


class JevAdapter:
    def __init__(self, client, *, clock=time.monotonic):
        self.client = client
        self.clock = clock

    async def assess(self, state: EncounterState) -> JevAssessment:
        if self.client is None:
            raise AssessmentUnavailable("unauthorized")
        reason: Reason = "unavailable"
        try:
            criteria = dict(load_catalog())
            start = self.clock()
            async with asyncio.timeout(TIMEOUT_SECONDS):
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
        except TimeoutError:
            reason = "timeout"
        except TypeSafeAPIResponseValidationError:
            reason = "invalid_response"
        except TypeSafeAPIError as error:
            reason = {401: "unauthorized", 429: "rate_limited"}.get(error.status, "unavailable")
        except (CatalogError, TypeSafeAPIConnectionError):
            reason = "unavailable"
        except Exception:
            reason = "unavailable"
        else:
            try:
                answer = response.choices["algorithm"]
                return JevAssessment(
                    revision=state.revision,
                    selected_id=answer.choice,
                    probabilities=answer.probabilities,
                    confidence=answer.confidence,
                    latency_ms=(self.clock() - start) * 1000,
                )
            except Exception:
                reason = "invalid_response"
        # Raise outside the handler: no upstream exception/body retained as context.
        raise AssessmentUnavailable(reason)
