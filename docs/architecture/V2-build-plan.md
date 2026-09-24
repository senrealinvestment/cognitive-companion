# V2 Build Plan (draft)

> Source: PR #1 `v2-speech-layer-ab` @ `d0d101f`.  
> **Hard constraints:** advisory cues only (never decision-making); **sim lab only** — no real patients, no VCU institutional systems, no QI/QA content, no patient data; push-cue path separate from clinician-opt-in deep research (wake phrase placeholder **"Hey Dr. Bellomo"** or button → local RAG + citations); OpenEvidence only with enterprise BAA; model updates gated, versioned, rollback-able — **never** bedside self-update. Live ICU crisis cues would very likely be a device function under FDA CDS guidance; stay **sim-only research** until a regulatory consultant reviews. Latency/memory figures in architecture docs are **estimates**.

**Roles:** CC Architect · Speech Engineer · Clinical Models Lead · Clinical Safety & Eval · Regulatory & Privacy · Sergio’s engineer (hands-on).

---

## Phase 0 — Contracts & harness (**Before hardware purchase**)

**Goal:** Interface stubs, eval harness, dataset specs, and sim scenarios without boxes.

**Done when:**
- `SystemOneClient` contract drafted (`laya` | `nanojev` → `/v1/systemone` vs `/api/evaluate` :8765) for salience · category · escalate · action/urgency; **mock backends green**.
- Safety/wording gate stub: HUD ≤8 words, advisory refuse rules, research “no source = no claim”; fixture tests pass.
- Speech → System One → MedGemma cue **message types** defined; deep-research is a **separate** module (never auto from push cues).
- Eval skeleton: KER/WER/DER (T1); dosing-refusal + advisory phrasing + MedQA regression hooks (T2); ECE/routing (T3); version registry + rollback flags.
- Dataset + sim consent specs (manikin/standardized participant; audio de-ID); gold-nudge schema; **no** EHR/patient fields.
- 3–5 critical-care sim scenarios (education only).

**Owners:** CC Architect (contracts); Speech Engineer (ASR/diar types); Clinical Models Lead (model stubs/eval hooks); Clinical Safety & Eval (gate + gold rubric); Regulatory & Privacy (consent, sim boundary); Sergio’s engineer (scaffolds, CI).

**Decisions before start:** (1) Hardware later lock: V2A DGX Spark · V2B Mac Studio · Hybrid LAN (no memory pool). (2) Sim-only confirmed vs any live-unit cue path (reject until consultant). (3) Cue text: MedGemma + wording check · vetted labels · hybrid. (4) Category vocab size + gold-nudge authors/approvers.

---

## Phase 1 — Day-1 bring-up (**Needs hardware**)

**Goal:** Chosen profile boots; thin clients stream LAN audio; health checks green.

**Done when:** Runtime up (DGX OS or macOS/MLX); ASR smoke (Parakeet or MedASR); System One via `SystemOneClient`; MedGemma 27B (or 4B draft) loads at chosen quant (**estimate** — measure on box); glasses/phone → LAN with TLS/mTLS or VPN in **sim** network; degrade note if box unreachable.

**Owners:** Sergio’s engineer + Speech Engineer; CC Architect (profile config); Regulatory & Privacy (sim network only).

**Decisions before start:** Hardware locked (V2A / V2B / Hybrid); if Mac path, **used 512 GB vs new 256 GB vs wait**; Hybrid split confirm (Spark: speech+NanoJev+NeMo; Mac: MedGemma+RAG) or revise.

---

## Phase 2 — Speech bake-off (**Needs hardware**)

**Goal:** Compare ASR/diarization on **one box** (avoid full-stack confounders).

**Done when:** Same corpus through V2A (Parakeet + Nemotron-3) and V2B (MedASR + Sortformer/pyannote/port) on one machine; KER/WER/DER + chunk latency logged (**estimates** until measured); written speech-path recommendation.

**Owners:** Speech Engineer; Clinical Safety & Eval (labels); CC Architect (thresholds); Sergio’s engineer (tooling).

**Decisions before start:** Sortformer CoreML stand-in vs Nemotron-3 port on Mac; bake-off host = Spark or Mac.

---

## Phase 3 — System One + MedGemma cues (**Needs hardware**)

**Goal:** Sim push path: speech → System One (a–d) → MedGemma → gate → HUD.

**Done when:** Laya (Mac) or NanoJev (Spark) behind one client; hierarchy if Choice cardinality high (Laya weak at **estimate** 50+); cues ≤8 words post-gate; offline labels for T1/T2/T3; **no** bedside weight mutation.

**Owners:** Clinical Models Lead; Sergio’s engineer; Clinical Safety & Eval; CC Architect (fast-path latency target **estimate** <1–2 s — validate on hardware).

**Decisions before start:** MedGemma 27B quant (4 vs 8-bit) ± 4B draft; Laya hierarchy cutover; keep System One default per hardware profile (not older “NanoJev always default” README wording).

---

## Phase 4 — Opt-in deep research + sim dry run (**Needs hardware**)

**Goal:** Clinician-triggered local RAG + citations; full dry run; push cues stay separate.

**Done when:** Wake/button only (custom wake model for **"Hey Dr. Bellomo"**; family/estate permission before public/commercial use); rights-cleared local corpus + mandatory citations; OE optional **only with** enterprise BAA; dry run + rollback drill; deep research never auto from salience.

**Owners:** Clinical Models Lead (RAG); Speech Engineer (wake); Clinical Safety & Eval (rubric); Regulatory & Privacy (BAA, consent, tribute, sim sign-off); Sergio’s engineer.

**Decisions before start:** Research model pick per profile; wake-word engine; pursue OE BAA or defer; sim-recording usage rights.

---

## What NOT to build yet

| Do not | Why |
|--------|-----|
| Live ICU / bedside cues | Likely FDA CDS device function until consultant review |
| VCU EHR / institutional connectors | No VCU institutional systems |
| QI/QA pipelines or real patient data | Hard rule; education sim only |
| Auto deep research or cloud Jev | Opt-in only; cloud Jev removed |
| Protocol / Stanford cards | Removed in V2 |
| OpenEvidence without BAA | Shared-layers policy |
| Bedside self-updating models | Version + rollback only |
| Mac↔Spark memory pooling | Impossible; ConnectX is Spark↔Spark |
| Dual-Spark 405B in Phase 1 | Decode too slow (**estimate** ~1.8 tok/s community) |
| Public wake-phrase ship | Custom model + estate permission first |
