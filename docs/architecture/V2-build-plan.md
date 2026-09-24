# V2 Build Plan (draft)

> Source: PR #1 `v2-speech-layer-ab` @ `d0d101f`.  
> **Hard constraints:** advisory only (never clinical decisions); **sim lab only** — no real patients, no VCU institutional systems, no QI/QA content, no patient data; push cues separate from opt-in deep research (wake **"Hey Dr. Bellomo"** or button, then local RAG with citations); OpenEvidence only with enterprise BAA; models gated, versioned, rollback-able — never bedside self-update. Live ICU cues would very likely be an FDA CDS device function; stay sim-only until a regulatory consultant reviews. Latency figures elsewhere are **estimates**.

**Roles:** CC Architect; Speech Engineer; Clinical Models Lead; Clinical Safety & Eval; Regulatory & Privacy; Sergio’s engineer.

## Decisions

| Decision | Status | Notes |
|----------|--------|-------|
| Sim-only scope | **CONFIRMED** | Sergio approved, Sep 24 2026. No live-unit cues until consultant review. |
| Cue-text default | **Recorded default (pending final confirmation)** | MedGemma plus wording gate; vetted labels as fallback. |
| Gold-nudge authors and approvers | **OPEN** | Who writes and who approves is undecided. |
| Hardware path | **OPEN** | V2A DGX Spark, V2B Mac Studio, or Hybrid (see Phases 1+). |

## Ownership

| Phase | Primary | Specialists (deliverable only) |
|-------|---------|--------------------------------|
| 0 | CC Architect; Sergio’s engineer | Regulatory & Privacy (dataset, sim-consent); Clinical Safety & Eval (metrics, wording-gate); Models/Speech only if a contract needs them |
| 0.5 | Clinical Safety & Eval; Sergio’s engineer; clinician operator + observer | Regulatory & Privacy (consent; IRB/exemption before session 1) |
| 1 | Sergio’s engineer; Speech Engineer | CC Architect (profile); Regulatory & Privacy (sim network) |
| 2 | Speech Engineer | Clinical Safety & Eval (labels); CC Architect (thresholds); Sergio’s engineer (tooling) |
| 3 | Clinical Models Lead; Sergio’s engineer | Clinical Safety & Eval; CC Architect (latency) |
| 4 | Clinical Models Lead; Sergio’s engineer | Speech Engineer (wake); Clinical Safety & Eval; Regulatory & Privacy |

---

## Phase 0 — Contracts & harness (**Before hardware purchase**)

**Goal:** Lean scaffolds: interface stubs, eval harness skeleton, dataset/consent specs, and sim scenarios. No model training and no hardware-dependent cue work.

**Done when:** `SystemOneClient` contract drafted (`laya`/`nanojev` mapping to `/v1/systemone` or `/api/evaluate` :8765) for salience, category, escalate, action/urgency, mocks green; wording-gate stub (HUD ≤8 words, advisory refuse rules, research “no source means no claim”) with fixture tests; message types for the push cue path, deep research as a separate non-auto module; eval skeleton (T1 KER/WER/DER; T2 dosing-refusal, advisory phrasing, MedQA hooks; T3 ECE/routing; version registry + rollback); dataset and sim-consent specs (manikin/standardized participant; audio de-ID) and gold-nudge schema with no EHR/patient fields; 3–5 education-only scenarios.

**Owners:** CC Architect and Sergio’s engineer (see table for specialists).

**Still open before start:** category vocabulary size (sim-only and cue-text settled above).

---

## Phase 0.5 — Wizard-of-Oz sim (**Before hardware purchase**)

**Goal:** Before buying boxes or training models, run 3–5 sim sessions where a human hand-sends cues to a display the team already has. Learn whether cues help, which categories matter, timing, and distraction. Tooling suggestion (not a purchase): laptop/phone cue-sender UI, or a pre-written cue card deck on an existing display.

**Who:** **Clinician operator** (sim faculty or clinician on Sergio’s team) follows a scripted cue sheet and may send allowed free-text cues under Clinical Safety & Eval wording rules; separate **observer/timekeeper** (does not send cues); **Sergio’s engineer** runs cue-sender tooling; **Clinical Safety & Eval** owns metrics and wording rules.

**Measured:** time to key actions; missed-action rate versus checklist; latency from trigger to display; acted-on versus ignored; false or unhelpful rate in debrief; short survey on distraction and usefulness; debrief notes on timing.

**Consent:** Written informed consent from every sim participant (including operator and faculty), covering audio/video if any, storage duration, who can access recordings, and withdrawal rights. Participants are staff/volunteers in sim, never patients. No real patient data, QI/QA, or VCU institutional systems. Phase 0 sim-consent spec must exist first. IRB review vs exemption is **open for Regulatory & Privacy** and must be settled before session 1.

**Done when:** 3–5 consented sessions complete; outputs include seed gold nudges (still pending undecided approvers), a draft cue-category list, and an explicit go/no-go for Phases 1–4.

**Proposed go/no-go (example thresholds for Sergio to set, not final):** **Go** if teams rate cues net helpful in most sessions, no cue caused harmful distraction or a wrong action, and some categories show repeated value. **No-go:** redesign or stop before buying hardware.

**Still open before start:** IRB versus exemption (Regulatory & Privacy); gold-nudge approvers remain OPEN.

---

## Phase 1 — Day-1 bring-up (**Needs hardware**)

**Goal:** Chosen profile boots; thin clients stream LAN audio; health checks green.

**Done when:** Runtime up (DGX OS or macOS/MLX); ASR smoke (Parakeet or MedASR); System One via `SystemOneClient`; MedGemma 27B (or 4B draft) loads at chosen quant (**estimate** — measure on box); glasses/phone audio over LAN with TLS/mTLS or VPN on the **sim** network; degrade note if unreachable.

**Owners:** Sergio’s engineer and Speech Engineer (see table).

**Decisions before start:** Hardware locked (V2A / V2B / Hybrid); if Mac, used 512 GB vs new 256 GB vs wait; if Hybrid, confirm Spark owns speech/NanoJev/NeMo and Mac owns MedGemma/RAG, or revise. Enter only after Phase 0.5 **go**.

---

## Phase 2 — Speech bake-off (**Needs hardware**)

**Goal:** Compare ASR/diarization on **one box** so full-stack differences do not fake a speech winner.

**Done when:** Same corpus through V2A (Parakeet + Nemotron-3) and V2B (MedASR + Sortformer/pyannote/Nemotron port) on one machine; KER/WER/DER and chunk latency logged (**estimates** until measured); written speech-path recommendation.

**Owners:** Speech Engineer (see table).

**Decisions before start:** Sortformer CoreML stand-in vs Nemotron-3 port on Mac; bake-off host Spark or Mac.

---

## Phase 3 — System One + MedGemma cues (**Needs hardware**)

**Goal:** Sim push path from speech through System One (a–d) and MedGemma to the wording gate and HUD.

**Done when:** Laya (Mac) or NanoJev (Spark) behind one client; hierarchy if Choice cardinality is high (Laya weak above an **estimate** of ~50); cues ≤8 words after the gate; offline labels for T1/T2/T3; no bedside weight mutation. Cue text uses the recorded default (MedGemma + wording gate; vetted labels as fallback).

**Owners:** Clinical Models Lead and Sergio’s engineer (see table). Fast-path latency target is an **estimate** under 1–2 s; validate on hardware.

**Decisions before start:** MedGemma 27B quant (4 vs 8-bit) and whether 4B draft stays; Laya hierarchy cutover.

---

## Phase 4 — Opt-in deep research + sim dry run (**Needs hardware**)

**Goal:** Clinician-triggered local RAG with citations; full dry run; push cues stay separate.

**Done when:** Wake or button only (custom wake model for **"Hey Dr. Bellomo"**; family/estate permission before public/commercial use); rights-cleared corpus with mandatory citations; OpenEvidence only with enterprise BAA; dry run + rollback drill; deep research never auto from salience.

**Owners:** Clinical Models Lead and Sergio’s engineer (see table).

**Decisions before start:** Research model per profile; wake-word engine; pursue OE BAA or defer; sim-recording usage rights.

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
| Bedside self-updating models | Version pin + rollback only |
| Mac↔Spark memory pooling | Impossible; ConnectX is Spark↔Spark |
| Dual-Spark 405B in Phase 1 | Decode too slow (**estimate** ~1.8 tok/s) |
| Public wake-phrase ship | Custom model + estate permission first |
| Buying hardware before Phase 0.5 go | Wizard-of-Oz may show cues hurt or do not help |
