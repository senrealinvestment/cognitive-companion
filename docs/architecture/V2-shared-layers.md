# V2 Shared Layers — Local System One (NanoJev default · Laya fallback)

> Identical for V2A and V2B. Only ASR + diarization differ.  
> **No cloud Jev. No protocol cards.** Cloud = deep research only (dashed, BAA).

**Edge target (stated):** laptop or small Apple Silicon Mac (edge brain) — **not** a phone. Extra System One capacity is worth it for a larger crisis/ICU category vocabulary with fewer routing stages.

---

## CRITICAL FLAGS

### FLAG-1 RESOLVED — no continuous cloud streaming for decisions
System One is local → de-ID routing text stays on the box. **No BAA for the decision layer.** Cloud deep-research still needs BAA if PHI. Local box still needs HIPAA Security Rule basics (encryption at rest, access control, audit logs, device management).

### FLAG-2 — Stack ASR + diar + NanoJev 0.6B + MedGemma on one laptop/Mac
**Estimates:** NanoJev 0.6B + MedGemma 4B Q4 (~2.3–2.5 GB) + ASR/diar. Feasible on a **laptop / small Mac** with enough unified/VRAM; still measure thermals. Phone-only excluded as primary.

### FLAG-2b — NanoJev host vs Apple Silicon Mac
Public NanoJev serve path docs emphasize **CUDA** (`POST /api/evaluate` :8765); independent review: “requires a CUDA device,” no CPU/remote fallback. **Apple Silicon Mac as sole host is a gap** unless we add Metal/MLX/CPU support or use an eGPU/CUDA box. **Laya (MLX) is the documented Apple-native fallback** when CUDA is unavailable.

### FLAG-3 — Generative cue wording check (MedGemma)
### FLAG-4 — Domain sub-agents = prompts / LoRA / separate models
### FLAG-5 — No VCU systems via Grok Bot; antibiogram = local static table

### FLAG-6 — Corrections to brief
| Brief | Verified |
|-------|----------|
| TypeSafe publisher | **No** — NanoJev = C-Tianyu/TianyuCodings; Laya = Convai Innovations; TypeSafe = cloud Jev |
| Drop-in `/v1/systemone` | **Goal via adapter.** Laya has `laya-serve` `/v1/systemone`. NanoJev native = `/api/evaluate`; contract audit notes incompatibilities (`boolean` vs `noul`, etc.). Config swap assumes our **SystemOneClient** façade |
| Choice >255 removed by 0.6B | **No.** NanoJev documents **Choice: 2–255** candidates — same **API-shape cap** as Jev. Larger model can improve accuracy **among** many categories; **vocab >255 still needs hierarchical/two-level routing** |

Sources: [HF NanoJev](https://huggingface.co/C-Tianyu/NanoJev) (“Choice: 2–255”), [jevlist review](https://jevlist.ai/projects/nanojev), [OpenJev choice ≤255](https://openjev.sh/docs/advanced).

---

## DEFAULT: NanoJev · FALLBACK: Laya

| | **NanoJev (DEFAULT)** | **Laya (FALLBACK)** |
|--|----------------------|---------------------|
| Why default | Edge = laptop/small Mac; more capacity for large ICU/crisis vocab; fewer routing stages | Lightest Apple MLX path when CUDA unavailable or footprint tight |
| Params | **0.6B** (Qwen3-0.6B backbone) | ~421M English / 322M multi |
| License | **MIT** code (+ **Qwen** backbone terms — review both) | **Apache-2.0** |
| Publisher | C-Tianyu / TianyuCodings (not TypeSafe) | Convai Innovations |
| Serve | Local HTTP **:8765** `POST /api/evaluate` | In-process MLX or `laya-serve` `/v1/systemone` |
| Choice limit | **2–255** (documented) | Practical weakness at 50+ without `head_max_len` / hierarchy |
| Clinical ckpt | Public demos game-oriented → **fine-tune on our labels** | Fine-tune recommended for typed ICU tasks |
| Swap | `SystemOneClient` backend = `nanojev` \| `laya` (adapter normalizes to `/v1/systemone` shape) | |

**Rationale (Sergio):** edge brain is already a laptop/small Mac, not a phone → prefer NanoJev capacity for a larger category vocabulary with fewer stages. Laya remains documented lightweight fallback; swap = config.

---

## Pipeline

```
Speech (V2A|V2B) → de-ID (local)
  → NanoJev default (Laya fallback) @ (a) salience (b) category (c) escalate (d) action/urgency
  → Fast: MedGemma + domain tools + local antibiogram
  → Deep (cloud, only if escalated): OE-class · delayed · BAA
  → Reconcile → gate (+ wording check) → HUD
  → Labels → ASR flywheel + NanoJev thresholds/calib/fine-tune + Gemma cue quality
```

### Choice / hierarchy caveat (important)
NanoJev **Choice supports 2–255 candidates** ([HF](https://huggingface.co/C-Tianyu/NanoJev)). That cap is an **API/request-shape limit**, not removed by using 0.6B instead of 0.42B. If the ICU+crisis vocabulary exceeds 255 leaves, use **hierarchical Choice** (family → leaf) even with NanoJev. The larger model’s value is **accuracy and fewer stages within/near the cap**, not infinite flat vocab.

---

## Offline fine-tune of NanoJev (MIT / open weights)

Shown in diagram offline section. Guardrails:

1. Train **offline only** from helpful/accurate (+ structured category labels)  
2. **Held-out eval set** frozen before each train  
3. **Replay buffer** to limit catastrophic forgetting  
4. **No bedside self-updates**  
5. **Version pin + rollback** on every deploy  
6. Respect **Qwen** + MIT terms on redistribution  

Replaces “cloud Jev weights not fine-tuned by us.”

---

## Fast / deep / cue / gate / antibiogram

Unchanged medically from prior router note: MedGemma HAI-DEF; generative cue leading + wording check; OE no verified public self-serve API; antibiogram CLSI M39 local static.

Safety gate: thresholds on **local** System One probs (calibrate on our labels) · rate limits · strip IDs · wording check if Gemma text.

---

## Open questions

- OQ-S1 NanoJev on Apple Silicon Mac without CUDA? (fallback → Laya, or CUDA eGPU/box)  
- OQ-S2 SystemOneClient façade (`/v1/systemone` over NanoJev `/api/evaluate`)  
- OQ-S3 Flat vocab size vs hierarchical cutover (&lt;255 vs &gt;255)  
- OQ-S4 Fine-tune recipe + replay + eval ownership  
- OQ-S5 Salience cadence on laptop  
- Plus taxonomy, Gemma placement, antibiogram, reconcile latency, OE enterprise, speech OQs  

---

## Sources
- https://huggingface.co/C-Tianyu/NanoJev  
- https://jevlist.ai/projects/nanojev  
- https://huggingface.co/convaiinnovations/laya · https://pypi.org/project/laya-serve/ · https://pypi.org/project/laya-mlx/  
- https://openjev.sh/docs/advanced (Choice ≤255 API shape)


---

## WORKSTREAM A — Three fine-tune tracks (shared data platform)

**Correction (write plainly):** **KER, noise/overlap augmentation, and audio de-ID are speech-layer concerns.** MedGemma is **text (+ optional image)** and **never hears audio**. Do not feed wavs into MedGemma training. Structure **three separate tracks** that share one data platform (consent, de-ID, versioning, registry).

### Shared data platform (all tracks)

| Item | Rule |
|------|------|
| Source | Thousands of hours **sim-lab** crisis + edge-case sessions + ongoing helpful/accurate labels |
| De-ID | Strip staff names / free-text identifiers from transcripts; voice consent for sim recordings (no patients in Phase 1, but **staff PHI-adjacent**) |
| Rights | Sim-center ownership; if **VCU** sim lab → **institutional approval**. Known constraint: **VCU will not allow institutional systems connected to Grok Bot** — training pipelines run on approved institutional/edge compute, not this agent |
| Versioning | Dataset revisions (e.g. DVC / HF dataset revisions); immutable held-out eval sets **never trained on** |
| Registry | Semver per adapter/checkpoint; pinned manifests; canary in sim; **one-click rollback**; **no bedside self-updates** |

### Track T1 — ASR fine-tune (ONLY speech difference V2A vs V2B)

| | V2A | V2B |
|--|-----|-----|
| Base | Parakeet-TDT 0.6B | MedASR 105M |
| Manifests | NeMo JSONL | HF `datasets` |
| Supervised pairs | Audio + **corrected** transcripts | same |
| Augmentation | ICU alarm/noise mix, overlap/cross-talk, RIR, SNR sweeps | same toolkit, different trainer |
| Method | LoRA / NeMo PEFT + **replay** of general speech | PEFT/SFT + replay |
| Eval gate | **KER** (crisis-term lexicon) + WER + diarization **DER** | same metrics |

### Track T2 — MedGemma fine-tune (text nudges; identical for V2A/V2B)

**Base selection (verify current HAI-DEF line):**

| Variant | Use | Memory (**estimates**) |
|---------|-----|------------------------|
| **MedGemma 1.5 / 1 4B-IT multimodal** (text path) | **Recommended** for laptop/small Mac + quantization (Q4 ~2.3–2.5 GB weights; often 3–5 GB RAM) | edge default |
| MedGemma 27B text-IT / multimodal | Only if workstation/GPU allows | ~ tens of GB — not phone |

License: **HAI-DEF Terms** ([card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card)). Camera-free product → train/eval on **text**; ignore vision unless Phase 2 changes.

**Supervised mapping (important):**  
`(de-ID state summary + NanoJev category/urgency + tool context) → target nudge text`  
Target nudges are **written/approved by clinicians**. **Raw transcripts are not supervised targets.**

**Augment:** helpful/accurate labels → preference pairs (optional **DPO** later); synthetic scenarios with clinician review.

**Recipe (starting points — tune empirically):** LoRA/QLoRA via PEFT/TRL, or **MLX-LM LoRA** on Apple Silicon. Example starting ranges (labeled as starting points): rank 8–64, α 16–64, lr ~1e-4–2e-4, 1–3 epochs, seq len fit to nudge+context, bf16/q4 as hardware allows.

**Eval gates (all must pass to promote):**
1. Nudge accuracy vs clinician reference set  
2. Advisory phrasing + length compliance (≤8 words or chosen limit)  
3. Hallucination / unsupported-claim rate  
4. **Dosing-order refusal**  
5. Latency on target laptop/Mac  
6. **Regression** on general medical bench (e.g. MedQA subset) — detect catastrophic forgetting  

**Replay:** mix general medical instruction data + prior-version data each cycle.

### Track T3 — NanoJev decision-model fine-tune (identical for V2A/V2B)

Typed outputs only (choice/boolean/score). Train offline on labeled routing decisions. Eval: accuracy + **calibration (ECE / reliability)** on held-out labels. Replay buffer; version pin; MIT + Qwen license review. Choice still **2–255** per call — hierarchy if vocab larger.

---

## WORKSTREAM B — Deep research = clinician opt-in (never auto-fires)

**Hard rule:** OpenEvidence-class deep research **NEVER auto-fires.**  
NanoJev may raise a **soft suggestion** (“may benefit from external evidence”). The **cloud call happens only** when the clinician:

1. Speaks a **wake word**, or  
2. Presses a **button** (glasses touch / phone / Mac).

### Suggestion UX (non-intrusive)
- Small HUD **glyph/icon** (not a full cue)  
- No tone, or soft distinct tone  
- Auto-expires after **N** seconds  
- Rate-limited  
- **Never interrupts** an active advisory cue  

### Wake-word / trigger options (verify licenses)

| Option | License / notes | Fit |
|--------|-----------------|-----|
| **openWakeWord** | Code **Apache-2.0**; bundled pretrained models often **CC BY-NC-SA 4.0** → train/own custom models for commercial clinical use | Strong OSS path if we train custom wake head |
| **Porcupine (Picovoice)** | Repo Apache-2.0; **AccessKey** + commercial terms for production | Accurate; enterprise licensing |
| **sherpa-onnx KWS** | Runtime Apache-2.0; **audit each model weight license** | On-device ONNX |
| **Apple on-device** | Speech framework / custom; Apple Silicon friendly | Mac/iPad path |
| **Reuse ASR + NanoJev intent** | No separate KWS; detect phrase in transcript / noul “user requested evidence?” | Simpler ops; more latency/false triggers in noise |

**False activation in noisy ICU:** high threshold, confirm UI, button always available as fallback, ignore wake during active critical cue window.

### What’s sent
De-ID query composed from recent context; **show composed query to clinician before send** (recommended). Audit log every send.

### Latency / delivery
Expect **delayed** path (proposal **10–60 s** — **OpenEvidence typical API latency unverified**; no public self-serve API found). Delivery: HUD “evidence ready” → open **phone/Mac panel**. **Not** read aloud mid-crisis unless requested.

### OpenEvidence status (sources)
- HIPAA / BAA for covered entities: [security](https://www.openevidence.com/security), [HIPAA announce](https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant)  
- Access pattern 2026: **enterprise / Epic workflow integrations** (e.g. UTMB, Mount Sinai, Cedars, NM Epic notes) — **no verified public self-serve developer API**  
- Alternatives if no OE API: other cited-answer APIs with BAA; private literature RAG under institutional BAA  

### Output handling
| | Mode | Recommendation |
|--|------|----------------|
| **(a)** | Full evidence + citations on phone/Mac panel | **Primary** |
| **(b)** | Optional MedGemma one-line HUD summary + citation link | Optional; **safety output check** + **preserve citations** |

### Reconciliation
Fast-path nudge remains; deep result **augments** later (does not silently overwrite without clinician notice). Deduplicate / rate-limit interplay.

### Privacy
**BAA required** for cloud research model; de-ID before send; full audit.

---

## Additional open questions (from these workstreams)

- Which MedGemma variant for Phase 1 (4B-IT quantized vs 27B)?  
- Wake-word engine choice (+ custom model training if openWakeWord NC weights)?  
- OpenEvidence enterprise API + institutional BAA path vs alternative?  
- Data rights/consent for sim audio (VCU approval; not via Grok Bot)?  
- Who writes/approves target nudge gold set?  
- Training compute: local Mac MLX vs cloud GPU (if data leaves device → de-ID + agreements)?  
