# companion-next — Jev slice 1

Simulation / education / shadow only. Not a clinical device. Synthetic text only.
Python validates state and assessments; models cannot author algorithms or activate
cards. No audio is captured or persisted.

This isolated service uses hosted TypeSafe Jev, model `jev-latest`, through
`typesafe-sdk==0.6.0` at `https://api.typesafe.ai/v1/systemone`. One SDK `Choice`
question named `algorithm` selects `anaphylaxis`, `malignant_hyperthermia`, or
`other_or_unclear`. No alternate model or raw-HTTP fallback exists.

## Run from this directory

Python 3.11+ and uv are required. This checkout also has an ignored uv bootstrap
at `.tool-venv/bin/uv`; use `export PATH="$PWD/.tool-venv/bin:$PATH"` if needed.

```bash
uv sync --locked --all-groups
uv run ruff check src tests
uv run pytest -m "not integration"
uv run uvicorn cognitive_companion.api:create_app --factory --host 127.0.0.1 --port 8767
```

Configured bind: **127.0.0.1:8767**. Port 8766 was occupied by unrelated Access
Health (PID 94163), so it is left untouched. Never use or stop the live PoC at
8765. No server is left running by the coder; the listener/API walk follows
Grok Build review. OpenAPI is at `http://127.0.0.1:8767/openapi.json`.

Credentials are loaded inside the service lifespan (or explicitly opted-in smoke)
from the authorized external credential file, represented here as **[REDACTED]**.
The file must have mode 600 and a nonblank `TYPESAFE_API_KEY` assignment; optional
`export` and shell-style quotes are supported without executing shell content.
Environment variables alone do not supply credentials. No repository dotenv file
is used. Importing the app does not read credentials or create a client.
Missing credentials or an invalid catalog prevents SDK construction and calls.
SDK body logging is disabled; external exceptions become bounded reason codes.

## API

`POST /v1/assess` accepts exactly:

```json
{"session_id":"synthetic-demo","revision":1,"transcript":"Synthetic simulation: isolated fever."}
```

A valid assessment returns HTTP 200 with only `revision`, `selected_id`,
`probabilities`, `confidence`, and `latency_ms`. Valid abstention is also 200.
Invalid input returns 422. An unavailable or invalid assessment returns 503:

```json
{"reason":"unavailable"}
```

Reasons are `unauthorized`, `rate_limited`, `unavailable`, `timeout`, and
`invalid_response`. Failure never fabricates an abstention or probabilities.
The SDK gets zero retries and a 10-second timeout; an asyncio deadline bounds the
whole call to 10 seconds. Lifespan closes the client using `aclose()`.

Contracts are frozen with immutable nested probabilities. Probability keys must
exactly match the three catalog IDs; finite values must lie in [0,1] and total
1 within absolute 0.01, inclusive. Accepted values are preserved, never normalized.
Latency uses a monotonic clock. Confidence describes distribution concentration,
not clinical truth or permission to act. Typed output guarantees an interface,
not correctness. See the [Choice docs](https://docs.typesafe.ai/primitives/choice.md)
and [Python SDK docs](https://docs.typesafe.ai/sdk/python.md).

## Scope and evidence

`config/scenarios.json` copies parent architecture plan **Task 1.2** verbatim:
`../.hermes/plans/2026-09-17_084647-jev-medgemma27b-new-architecture.md`.
A digest pins its complete content and schema. Review provenance was not supplied;
**catalog acceptance remains blocked pending review evidence**. Offline scaffolding
and tests do not establish clinical accuracy or catalog acceptance.

`GrokStandinAdapter` is an unused **temporary Grok 4.6 stand-in** that raises
`NotImplementedError("not_in_slice")`. It is not MedGemma or evidence of convergence.
`NullLiteratureAdapter` reports only `research_status="unavailable"`.
Neither has a network client or is invoked by the API. Second-lane execution,
agreement types, convergence, research scheduling, treatment text and HUD output
are not in this slice.

Default pytest is offline even when credentials exist. Unit tests inject a fake
SDK and block socket connections. Explicitly opt into the one hosted, nonmedical
synthetic smoke with:

```bash
uv run pytest -m integration --live tests/test_integration.py
```

Without `--live`, or with unavailable external credentials, the integration test
skips. It sends a nonmedical bicycle/library sentence through the same Choice
adapter. See [EVIDENCE.md](EVIDENCE.md) for executed results and red/green checkpoints.
Fake-backed API fixtures are in `tests/test_api.py`; hosted smoke is not medical
accuracy validation. Grok Build PASS/BLOCK and its subsequent port-8767 API walk
remain external review steps. No merge or push is performed.
