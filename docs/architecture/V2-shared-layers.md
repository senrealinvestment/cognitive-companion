# V2 Shared Layers — Jev as multi-point router (identical for V2A and V2B)

> **Scope.** Everything downstream of the on-device speech layer is **textually identical** for V2A (NVIDIA) and V2B (Google). Only ASR + diarization differ. V2A/V2B notes point here; a verbatim summary is also in each note.
>
> **No protocol cards.** V2 has no Stanford / pocket-binder / fixed card library. Categories are a **large ICU+crisis vocabulary** used for routing, not pre-written cue cards.

**Product:** Crisis Mirror — ambient, camera-free cognitive-forcing companion for transplant ICU / critical care.  
**Phase 1:** 4-week sim MVP (no PHI); Jev + local fast path included.  
**Phase 2 gates:** BAA or provable de-ID, thresholds from labels, IRB, Halo camera-off.  
**Design law:** no wearable camera · advisory only · human decides · offline-only learning · full audit · role separation.  
**Standing conflict:** “no continuous cloud streaming” vs Jev-cloud first-pass salience — see **FLAG-1**.

---

## CRITICAL FLAGS (read before design lock)

### FLAG-1 — Jev salience ≈ continuous cloud text streaming

Jev is **cloud-only**. Using it as first-pass salience over the speech stream means **de-identified text continuously (or near-continuously) leaves the edge**. That **conflicts** with the V1/V2 design rule *no continuous cloud streaming*.

| Option | Meaning |
|--------|---------|
| **Relax the rule** | Explicitly allow continuous/near-continuous **de-ID text** to Jev; treat BAA (or equivalent) as a **hard Phase-2 gate** even for text |
| **On-device pre-filter** | Keyword spotting / small local classifier / local Gemma keep most audio local; **only candidate segments** go to Jev |
| Hybrid | Pre-filter + batched Jev windows (e.g. every N seconds), not every utterance |

Also: **call-volume + latency** — per-segment Jev Noul/Choice adds RTT (~70–500 ms claimed) × segment rate. Budget this or salience will dominate cost/latency.

### FLAG-2 — On-device compute stacking likely exceeds phone

Rough concurrent footprint (**estimates**):

| Component | Params / size (est.) | Source basis |
|-----------|----------------------|--------------|
| Parakeet-TDT ASR | ~600M; ~0.65–1.2 GB quantized/FP16 | prior V2A notes / community CLI |
| MedASR | 105M; ~0.2 GB class | MedASR card |
| Nemotron-3 Diarization | ~100M | HF card |
| MedGemma 4B Q4 | ~2.3–2.5 GB weights; often **3–5 GB** runtime RAM | GGUF community quants / catalogs |
| MedGemma vs Parakeet | ~**7×** param count (4B / 0.6B) | arithmetic |

**ASR + diarization + MedGemma 4B on one phone is unlikely for sustained ICU ambient.** Default recommendation: **edge box** (Mac mini / laptop / Jetson Orin class) for speech + MedGemma; phone/glasses = mic + HUD + labels. Phone-only may work for **lighter** Gemma 3n E2B path **without** MedGemma, or sequential load (never simultaneous) — measure.

### FLAG-3 — Generated cue text reintroduces hallucination

Leading cue path is **MedGemma generates ≤8-word advisory text** (Sergio lean). That **re-adds** an **output wording check** in the safety gate (advisory phrasing, length, consistency with Jev category, no dosing orders). Say plainly: wording check returns **because free text is back**, not because cards returned.

### FLAG-4 — “Sub-part of Gemma” is not native

There is no built-in “ID sub-slice” of MedGemma. Choose explicitly:

1. **Prompt / tool-conditioned** same model (cheap, weaker specialization)  
2. **LoRA / PEFT adapters** per domain (ID, airway, hemodynamics, …) hot-swapped  
3. **Separate fine-tuned models** per domain (clearest isolation; heaviest ops)

### FLAG-5 — Institutional data access (VCU / Grok Bot)

**VCU will not allow institutional systems connected to Grok Bot.** Live EHR / lab / antibiogram feeds need **institutional approval** on an approved runtime, not this agent. Crisis Mirror sim uses a **mock or published** antibiogram. Production antibiogram = static/versioned local file maintained by pharmacy/micro — **no live lab pipe** without separate IT/security sign-off.

---

## Pipeline (shared)

```
Speech (V2A | V2B) → de-ID summary / segment stream
        │
        ▼
Jev router @ multiple points
  (a) Salience — which segments matter
  (b) Category routing — ICU/crisis taxonomy → sub-agents / lookups
  (c) Escalation — deep research needed?
  (d) Action + urgency — Noul + Score → gate
        │
        ├────────── LOCAL FAST PATH ──────────┐
        │  MedGemma (or alt) “quick think”     │
        │  + domain sub-agents (e.g. ID)       │
        │  + local antibiogram / institutional │
        │    static tables                     │
        │  → cue draft / nudge / timing        │
        │                                      │
        └────────── DEEP RESEARCH PATH ────────┤
           OpenEvidence or other deep model    │
           (may be delayed; only if escalated) │
                    │                          │
                    ▼                          ▼
              RECONCILE (fast first; deep augments/supersedes — OQ)
                    │
                    ▼
        Safety gate (+ wording check if Gemma text)
                    │
                    ▼
        HUD label + tone → clinician (human decides)
                    │
                    ▼
        Labels: helpful / accurate
           → ASR flywheel
           → Jev threshold tuning
           → Gemma cue-quality tuning data
```

---

## 1. ASR flywheel (unchanged process)

Capture → de-ID PHI → KER → LoRA/PEFT + replay buffer → deploy/monitor. Offline only.

---

## 2. Jev as multi-point router (core)

Jev is **not** a thin yes/no in front of cards. It routes at **four** points:

| Point | Jev type(s) | Role |
|-------|-------------|------|
| **(a) Salience** | Noul per segment and/or Choice | Which sentences/segments of the speech stream advance |
| **(b) Category routing** | Choice (≤255 options/call) | Large ICU + crisis vocabulary → which **sub-agent / lookup** runs. If taxonomy >255, use **hierarchical / two-level** Choice (family → leaf) |
| **(c) Escalation** | Noul *needs deep research?* (or category flag) | Whether to call OpenEvidence / deep model |
| **(d) Action + urgency** | Noul *action warranted?* + Score urgency | Feeds safety gate / tone |

**Example (ID):** Category ≈ *infection / organism / empiric abx* → ID sub-agent (MedGemma + **ID LoRA or prompt**) + **local antibiogram** lookup (organism × antibiotic × %S).

- Access: TypeSafe / Vercel AI Gateway `typesafe-ai/jev`. Text-only, cloud-only.  
- Latency/cost claims: ~70–500 ms; ~$0.042/M input — measure. Calibration unpublished.  
- **ZDR ≠ HIPAA BAA.**

---

## 3. Local fast path — MedGemma (leading) + alternatives

### MedGemma (verified)

| Variant | Params / modality | Notes | License |
|---------|-------------------|-------|---------|
| **MedGemma 1.5 4B** (`google/medgemma-1.5-4b-it`) | 4B multimodal | Updated Jan 13 2026; stronger medical text + imaging; Crisis Mirror uses **text** for cues | **HAI-DEF Terms** |
| MedGemma 1 4B IT/PT | 4B multimodal | Prior 4B line | HAI-DEF |
| MedGemma 27B text-only | 27B text | Stronger text reasoning; **not** phone-local | HAI-DEF |
| MedGemma 27B multimodal | 27B multi | Edge-box / server only | HAI-DEF |

Sources: [MedGemma 1.5 card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card), [MedGemma 1 card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card-v1), [HF medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it), [HAI-DEF terms](https://developers.google.com/health-ai-developer-foundations/terms).

**On-device feasibility (estimates):** Q4_K_M ~2.3–2.5 GB weights; runtime often 3–5 GB RAM. Community mobile runs exist but **slow** for interactive notes on mid phones. **Realistic Crisis Mirror posture:** MedGemma 4B on **edge box**; 27B only on workstation/cloud under BAA. Camera-free product → ignore vision path for v1 cues.

### Lighter Gemma alternatives (fast local)

| Model | Footprint (est.) | License | Fit |
|-------|------------------|---------|-----|
| **Gemma 3n E2B / E4B** | ~2–3 GB effective mem (int4 LiteRT) | Gemma license (HF gated) | Strongest **phone** candidate for “quick think” if MedGemma too heavy |
| Gemma 3 1B / 4B | 1B much smaller | Gemma license | Fallback cue/nudge generator |

Sources: [Gemma 3n announce](https://developers.googleblog.com/introducing-gemma-3n/), [LiteRT-LM](https://developers.google.com/edge/litert-lm/overview). **Tradeoff:** not medically specialized like MedGemma — expect more fine-tune / prompt work.

**Fast-path jobs:** nudges, timing (“reassess in 2 min”), short cue draft, domain tool calls (antibiogram query). Target latency budget: **&lt;1–2 s** cue (OQ).

---

## 4. Deep research path

| Option | Status (as of 2026-09) | BAA / HIPAA | Notes |
|--------|------------------------|-------------|-------|
| **OpenEvidence** | Clinician product; **no public self-service developer API** found; enterprise / Epic-style integrations reported | Covered entities may use PHI under **standard BAA** ([security](https://www.openevidence.com/security), [HIPAA announce](https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant)); SOC 2 Type II claimed on security page | **Flag:** Crisis Mirror cannot assume a drop-in REST API without enterprise deal. Latency unknown for API path. |
| EvidenceMD / other cited-answer APIs | Third-party alternatives claiming API + BAA | Vendor-specific | Evaluate if OE unavailable |
| Private literature stack | Self-hosted retrieval | Under own BAA | Heavy build |

Deep path **only when Jev escalates**; may respond **delayed** (proposal: 10–60 s — OQ). Delivery: later HUD line / phone panel / post-event — OQ.

---

## 5. Antibiogram (local static — no live EHR)

Per **CLSI M39**, cumulative antibiograms are typically **annual** (or periodic) published tables: organism × antibiotic → **% susceptible**, with isolate counts; often stratified by unit/specimen. **No PHI** in the published table.

**Proposal for Crisis Mirror:**

```
antibiogram_vYYYY.json
  version, effective_date, institution, unit_scope
  rows: organism, n_isolates, antibiotics[{name, pct_S}], specimen?, notes
```

- Queried **locally** by ID sub-agent (structured lookup, not LLM memorization).  
- Update cadence: when pharmacy/micro publishes (annual ± interim).  
- **Sim:** mock or published public table.  
- **Live VCU lab feed:** blocked without institutional approval (FLAG-5).

Sources: [CLSI M39 overview (JCM)](https://journals.asm.org/doi/10.1128/jcm.02210-21), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9580356/).

---

## 6. Cue text (open — Sergio leans generative)

| Option | Role |
|--------|------|
| **(b) Leading candidate** | **MedGemma generates** ≤8-word advisory cue, conditioned on Jev category + de-ID context + tool results | Guardrails: output check (FLAG-3); no dosing orders; store prompt+output in audit |
| **(a) Fallback** | Clinician-vetted short **display label per category** rendered verbatim | Safer, less flexible; thin closed map (not a full card library) |

---

## 7. Safety gate

1. Jev probability vs threshold (≥0.9 fire / 0.6–0.9 silent log / &lt;0.6 nothing — tune).  
2. Rate limits.  
3. Strip identifiers.  
4. **If Gemma generated text:** wording check — advisory phrasing, length ≤8 (or chosen limit), **consistent with Jev category**, **no dosing/orders**.  
   → Explicitly: wording check is back **because generated text is back**.

Optional: also require Choice confidence (OQ).

---

## 8. Offline labeling loop

Fired cues → helpful / accurate → feeds:

1. ASR flywheel (KER → LoRA/replay)  
2. Jev threshold tuning  
3. **New:** Gemma cue-quality tuning data (preference pairs / reject bad cues) for offline adapter/prompt iteration  

**We do not fine-tune Jev weights.** Taxonomy revisions = clinical governance (OQ).

---

## 9. Reconciliation (fast vs deep) — open

When both paths fire: proposal — **fast nudge first**; deep result **augments or supersedes** later; conflict policy + dedupe + rate-limit interplay must be specified (OQ-R).

---

## Open questions (full list)

### Router / product
- **OQ-R1** Category vocabulary size; flat vs hierarchical (&gt;255); ownership/approval; `none`/`other`.  
- **OQ-R2** Which Gemma variant + **where it runs** (phone vs edge box vs 27B server).  
- **OQ-R3** Domain specialization: prompts vs LoRA vs separate models (FLAG-4).  
- **OQ-R4** Antibiogram schema, query API, update cadence, mock vs VCU published table.  
- **OQ-R5** Latency budgets: fast &lt;1–2 s? deep 10–60 s? delivery channel for delayed results.  
- **OQ-R6** Reconciliation when both paths fire; conflict; dedupe; rate limits.  
- **OQ-R7** Jev call budget (salience rate × cost × BAA).  
- **OQ-R8** FLAG-1 resolution: relax streaming rule vs on-device pre-filter.  
- **OQ-R9** Cue path lock: generative (b) vs label map (a).  
- **OQ-R10** Deep vendor: OE enterprise API vs alternative; BAA party.

### Speech (prior)
- On-device speech compute; V2A v2 vs v3; V2B diar pairing; fine-tune/KER/replay/IRB; streaming; speaker&gt;8; alarms; export; fallbacks.

---

## Sources (shared / router)

- MedGemma: https://developers.google.com/health-ai-developer-foundations/medgemma/model-card  
- MedGemma 1: https://developers.google.com/health-ai-developer-foundations/medgemma/model-card-v1  
- HAI-DEF terms: https://developers.google.com/health-ai-developer-foundations/terms  
- Gemma 3n: https://developers.googleblog.com/introducing-gemma-3n/  
- OpenEvidence security / BAA: https://www.openevidence.com/security  
- OpenEvidence HIPAA: https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant  
- OE public API status (secondary): https://evidencemd.ai/blogs/openevidence-api  
- Jev: https://vercel.com/ai-gateway/models/jev  
- CLSI M39 antibiogram: https://journals.asm.org/doi/10.1128/jcm.02210-21  
