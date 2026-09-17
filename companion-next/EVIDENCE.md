# Slice 1 coder evidence — 2026-09-17

Initial branch main; tracked working tree clean. Preserved unrelated untracked
research/architecture-literature-companion-next-2026-09-17.md.
Listener metadata only: 8765 PID 33970; 8766 PID 94163. Neither accessed or stopped.
8767 available; reserved for this service's documented local bind.
No applicable repository AGENTS.md; ancestor workspace guidance read.

Live TypeSafe SDK, Choice, async client, retry and exception docs fetched before
adapter implementation; classification cookbook inspected. SDK 0.6.0 pinned.
uv was absent from PATH; installed in ignored .tool-venv.

TDD checkpoints (commands from companion-next with .tool-venv/bin/uv):
- Catalog: run pytest tests/test_catalog.py — RED collection error, missing catalog
  module; GREEN 12 passed after frozen JSON and digest-checked loader.
  Source: parent architecture plan Task 1.2. No review provenance supplied;
  catalog acceptance remains blocked pending review evidence.
- Contracts: run pytest tests/test_contracts.py — RED missing contracts module;
  GREEN 36 passed. Includes strict numerics, unchanged near-boundary mass, defensive
  copy and nested mutation rejection.
- SDK adapter: run pytest tests/test_jev_adapter.py — RED missing adapter module;
  GREEN 1 passed. Typed Choice, exact criteria, question/model, request revision,
  preserved probabilities/confidence, zero retries and monotonic latency verified.
- Failures: run pytest tests/test_failures.py — RED missing sanitized error type;
  GREEN 32 passed (33 with adapter regression). Status errors, timeout including
  wall-clock deadline, connection, absent/malformed answers and invalid values
  fail closed. Caller traceback/log sentinel checks pass; invalid catalog makes
  zero calls. Sanitized exceptions retain no upstream exception context.
- Unused lanes: run pytest tests/test_stubs.py — RED missing stub modules;
  GREEN 2 passed. No network clients or agreement types.
- API: run pytest tests/test_api.py — RED missing API module; GREEN 39 passed.
  Three synthetic fixtures and complete failure matrix exercised in-process with
  fake SDK, including abstention success, strict 422, sanitized 503, OpenAPI
  response contract and unused-lane tripwires. Injected clients close on lifespan.
- Runtime: run pytest tests/test_runtime.py — RED missing runtime module;
  GREEN 10 passed (49 with API regression). Fixed external credential source,
  mode check, missing/invalid preflight without client creation, explicit endpoint,
  zero retries, bounded timeout and lifecycle closure verified.
- Probability tolerance boundary: run pytest tests/test_contracts.py -k
  inclusive_mass_boundary — RED 2 failed at exact totals 0.99/1.01 due to binary
  subtraction. GREEN all 38 contract cases using decimal arithmetic solely for
  the mass check; accepted probabilities remain unchanged.
- Offline socket guard added and default integration exclusion retained.
- Explicit hosted smoke: run pytest -m integration --live tests/test_integration.py
  -q — EXECUTED, 1 passed in 0.54s, using the nonmedical bicycle/library sentence
  and real SDK. Not a fake result, not a clinical accuracy assessment.

Final coder validation:
- uv sync --locked --all-groups: succeeded (32 resolved, 30 installed checked).
- uv run ruff check src tests: all checks passed.
- uv run pytest -m "not integration": 136 passed, 1 integration deselected.
  Includes SDK response-validation exception cases through adapter and API.
  One upstream Starlette/AnyIO deprecation warning; no test failures.
- Offline suite ran after the successful hosted smoke with credentials still
  available externally; no unit test read the real credential or called hosted API.
- No local service startup or listener API walk performed: per execution plan,
  that walk follows Grok Build review. README specifies 127.0.0.1:8767 because 8766
  is occupied. Three synthetic cases have in-process fake-backed API evidence only.
- Grok Build review and Astra final decision remain pending; coder does not issue
  PASS/BLOCK. Catalog acceptance still requires missing review evidence.
- Staged files and all new commits: scope and credential-pattern scan clean
  (private-key, token and credential-URL patterns; values never printed).
  Real credential was not loaded for scans. SDK sentinel tests cover caller
  tracebacks, logs and API JSON. git diff --cached --check clean.
- Final listener metadata unchanged: 8765 PID 33970 and 8766 PID 94163.
  No access to their application files, imports, endpoints, or process controls.
- Unrelated research markdown remains untracked and unstaged. All slice commits
  are local and scoped to companion-next; no merge or push.

## Astra OpenAPI 503 documentation follow-up — 2026-09-17

- Dispatch: `feat/companion-next-jev-slice-1`, HEAD `5e9fa98`.
- Added `tests/test_api.py::test_openapi_service_unavailable` before changing
  API metadata. RED: `uv run pytest
  tests/test_api.py::test_openapi_service_unavailable` exited 1 with the assertion
  `assert "503" in responses`; only 200 and 422 were documented.
  Used the existing `.tool-venv/bin` PATH bootstrap because uv was not on PATH.
- Added route response metadata only: 503 application/json object, required
  string `reason`, no additional properties, enum `unauthorized`, `rate_limited`,
  `unavailable`, `timeout`, `invalid_response`. Runtime handler is unchanged.
- GREEN: the same targeted test passed (1 passed).
- Gates: `uv run ruff check src tests` passed; `uv run pytest -m "not integration"`
  passed with 137 passed, 1 integration deselected. Existing upstream
  Starlette/AnyIO deprecation warning remains.
- OpenAPI walk passed against a fresh in-process TestClient app with `client=None`:
  GET /openapi.json, request schema, 200/422 component references, complete 503
  JSON schema and enum, GET /docs, runtime 422 and sanitized unauthorized 503.
  Existing offline API tests cover runtime 200 and the failure matrix.
  This was not a port-8767 listener walk; existing listeners were left untouched.
- No hosted calls or credential reads. No HUD or second-lane changes. Catalog
  review remains deferred. Simulation / education / shadow only; hosted
  selected_id remains an interface, not clinical truth or accuracy evidence.
- Unrelated research file remains untouched. Local commit only; no merge or push.
