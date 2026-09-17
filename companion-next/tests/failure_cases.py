from types import SimpleNamespace

import httpx2
import typesafe_sdk as sdk

from .fakes import PROBABILITIES, answer, response

SENTINEL = "dummy-secret-sentinel-do-not-expose"
SERVICE_FAILURES = [
    (sdk.TypeSafeAPIError(status, SENTINEL, httpx2.Headers({"Authorization": SENTINEL})), reason)
    for status, reason in [(401, "unauthorized"), (429, "rate_limited"),
                           (529, "unavailable"), (500, "unavailable")]
] + [
    (sdk.TypeSafeAPITimeoutError(10), "timeout"),
    (sdk.TypeSafeAPIConnectionError(SENTINEL), "unavailable"),
    (TimeoutError(SENTINEL), "timeout"),
    (RuntimeError(SENTINEL), "unavailable"),
]
INVALID_RESPONSES = [
    SimpleNamespace(choices={}), SimpleNamespace(), SimpleNamespace(choices=None),
    response(SimpleNamespace(choice="anaphylaxis")),
    response(answer(choice="unknown")), response(answer(probabilities={})),
    response(answer(probabilities=dict(PROBABILITIES, extra=0))),
    response(answer(probabilities=dict(anaphylaxis=.8, other_or_unclear=.2))),
    response(answer(probabilities=dict(PROBABILITIES, anaphylaxis=.5))),
    *[response(answer(probabilities=dict(PROBABILITIES, anaphylaxis=v)))
      for v in (float("nan"), float("inf"), -.1, 1.1, True, "0.8")],
    *[response(answer(confidence=v))
      for v in (float("nan"), float("inf"), -.1, 1.1, True, "0.8")],
]
