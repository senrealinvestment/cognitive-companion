# companion-next — Jev gate-only slice 2

Simulation / education / shadow only. Not a clinical device. Synthetic text only.
Python validates state and assessments; models cannot author algorithms or activate
cards. No audio is captured or persisted.

This isolated service uses hosted TypeSafe Jev, model `jev-latest`, through
`typesafe-sdk==0.6.0` at `https://api.typesafe.ai/v1/systemone`. One SDK `Choice`
question named `algorithm` in the unchanged slice-1 `/v1/assess` interface smoke
selects `anaphylaxis`, `malignant_hyperthermia`, or `other_or_unclear`. No alternate model or raw-HTTP fallback exists.

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

## Gate-only API

`POST /v1/gate` accepts a gate-specific request retaining the required
`session_id`, positive integer `revision`, and nonblank `transcript`:

```json
{"session_id":"synthetic-demo","revision":1,"transcript":"Synthetic simulation: review a concrete concern with an observed change.","faculty_id":"synthetic-faculty","mode_hint":"emergency"}
```

`faculty_id` is an optional string and `mode_hint` is optionally `emergency`,
`rounds`, or `neither`; both may be omitted or null. Both are inert metadata:
`faculty_id` establishes no faculty authority or approval, and client `mode_hint`
is accepted but unused in this slice. Neither controls mode. Only the original
three encounter fields reach the adapter and TypeSafe. Extra fields, including
a client-supplied `request_id`, are rejected. `/v1/assess` continues to accept only
the original `EncounterState` and rejects these metadata fields.

The gate asks two Nouls (`decision_shaped`, `enough_evidence`) and two Choices
(`mode_hint`, `family`) in one `system_one` call over the complete original
encounter state. All questions are independent; transcript content is data,
not overriding instructions.

Criteria and thresholds are **synthetic, unvalidated engineering fixtures, not
faculty-approved**. Python returns `retrieve` only when both Nouls are at least
0.80, both Choice confidences are at least 0.70, mode is `emergency` or `rounds`,
and each selected Choice label is its distribution's unique maximum. Thresholds
are inclusive; there is no averaging or compensation. `other` is an eligible
family pack, not a disease or automatic abstention. Mode hints are advisory only;
Python retains mode ownership. The response `mode_hint` remains Jev's advisory
judgment, independently of any client hint. No mode transition or faculty lock
is changed.

Both valid outcomes are HTTP 200:

```json
{"revision":1,"outcome":"silence","pack":null,"mode_hint":"neither","mode_hint_advisory":true,"latency_ms":25.0,"reasons":["mode_neither"],"request_id":"ca4019a84c914606af6d4ec27204b950"}
```

```json
{"revision":1,"outcome":"retrieve","pack":"other","mode_hint":"rounds","mode_hint_advisory":true,"latency_ms":25.0,"reasons":["gate_passed"],"request_id":"237caaade2ac4741a5ea8cba427e0eab"}
```

Every valid gate request gets a fresh server-generated opaque `request_id`
(random UUID hex), included in either 200 outcome. Repeating an identical request
gets a distinct ID; this is a per-request identifier, not a session ID, authority
claim, or idempotency key. It is not sent to TypeSafe. Error bodies remain unchanged
and contain no request ID.

`reasons` is required and nonempty. Python emits only bounded policy codes, never
model-generated explanations. Retrieve has exactly `["gate_passed"]`. Silence
includes every applicable failure code in the following fixed order:

| Code | Meaning |
| --- | --- |
| `decision_shaped_below_threshold` | Decision-shaped Noul is below 0.80. |
| `insufficient_evidence` | Enough-evidence Noul is below 0.80. |
| `mode_neither` | Jev selected `neither`. |
| `mode_confidence_below_threshold` | Mode Choice confidence is below 0.70. |
| `family_confidence_below_threshold` | Family Choice confidence is below 0.70. |
| `mode_tied` | Selected mode shares the maximum probability. |
| `family_tied` | Selected family shares the maximum probability. |

`gate_passed` means all existing policy predicates passed; it is not clinical
validation. Multiple failures do not short-circuit reason collection.

Families are `airway`, `circulation`, `metabolic`, and `other`. The wire outcome
`retrieve` is the documented synonym for `retrieve_pack`. It identifies only a
family pack; it performs no retrieval or reasoner call. Silence means a
valid policy failure or uncertainty, including tied Choice maxima. No numeric
judgments, diagnostic fields, or free-text explanation appear in the response.

All four answers must validate before policy runs, even if one already implies
silence. A selected label below the maximum, missing/wrong primitive, unknown
label, or malformed distribution is `invalid_response`. Internal judgments are
frozen, including copied nested distributions. Numbers must be finite [0,1],
not booleans or numeric strings. Distributions require exactly the declared keys
and mass within inclusive absolute 0.01 of one; values are never normalized.

Invalid input returns 422 before any SDK call. Service failures and malformed
answers return 503 with only `{"reason":"..."}`, using the same five bounded
reasons listed above. Failures never become silence. Gate uses zero retries,
a 10-second SDK timeout and enclosing asyncio deadline, and monotonic latency.
It shares the lifespan-managed client with assess. Startup catalog validation
remains required; gate calls do not load or use the catalog.

`/v1/assess` remains the unchanged slice-1 interface smoke and is not deprecated.
Its selected IDs are not clinical truth. Synthetic-only use is an operational
restriction: `EncounterState` does not prove submitted text is synthetic.
Offline tests establish interface and policy behavior, not clinical accuracy.
No hosted validation was performed for slice 2. The contract correction is
validated offline with injected failures; live 503 behavior remains unvalidated.
Verify, reasoning, retrieval,
shadow evaluation, faculty criteria, HUD, and convergence require later slices.

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
