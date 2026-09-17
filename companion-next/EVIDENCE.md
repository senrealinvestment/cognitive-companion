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
