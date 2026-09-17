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
