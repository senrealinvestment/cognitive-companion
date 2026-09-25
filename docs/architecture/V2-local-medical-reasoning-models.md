# Local Medical Reasoning Models — Options and Caveats

> Used by the **local deep-research / local-reasoning path** (primary) documented in [`V2-shared-layers.md`](./V2-shared-layers.md). Applies identically to **V2A (Spark)**, **V2B (Mac)**, and **Hybrid**. Hardware fit: [`V2-hardware-options.md`](./V2-hardware-options.md).

## Global caveats (read first)

1. **None of these models is validated on real-time ICU / crisis companion scenarios.** Scores are exam-style MCQA, HealthBench-style conversational rubrics, or literature QA — **benchmark ≠ bedside**.
2. For Cognitive Companion’s research path, any local LLM **must** be paired with **local literature retrieval + mandatory citations** (“no source = no claim”). A naked model is not a substitute for OpenEvidence’s licensed corpus.
3. Closing the gap means **fine-tune / eval on Sergio’s sim-lab data** — tie to **T2** (MedGemma cue track) and research-path eval gates (hallucination, dosing refusal, advisory phrasing, regression). No bedside self-updates; version pin + rollback.
4. Memory numbers below are **estimates** (weights ≈ params×bytes; Q4 ≈ 0.5 B/param rough; real residency = weights + KV + concurrent ASR/System One). Label as estimates.

---

## Comparison table (verified where possible)

| Model | Headline score (verified) | License | Params | Q4 fit est. Spark 128 / Mac 256 / Mac 512 | ICU/crisis caveat |
|-------|---------------------------|---------|--------|-------------------------------------------|-------------------|
| **MedGemma 27B** | MedQA **87.7%** 0-shot (text); R1 **90.1%** in same Google table (~2.4 pts) | HAI-DEF | 27B | Easy / easy / easy (~14–20 GB Q4) | Exam-strong; **not** ICU-crisis validated; cue + research candidate |
| **MedGemma 4B** | MedQA **64.4%** (v1); **69.1%** (1.5) | HAI-DEF | 4B | Easy / easy / easy (~2–4 GB Q4) | Fast draft / edge only |
| **Med42-v2 70B** | MedQA **79.1%**, USMLE **83.8%** | Llama 3 Community (+ M42 terms) | 70B | Mid (tight w/ concurrent) / yes / yes (~35–40 GB Q4) | MCQA clinical; not crisis HUD |
| **Med42-v2 8B** | USMLE **67.0%**, MedQA **62.8%** | Llama 3 Community | 8B | Easy / easy / easy | Light option; weaker scores |
| **OpenBioLLM 70B** | MedQA **76.9%**, USMLE **79.0%** | **Llama 3 Community** (not Apache) | 70B | Mid / yes / yes | Same class as Med42; older vs 2025–26 reasoners |
| **DeepSeek R1 671B MoE** | MedQA **90.1%** (Google table); **93%** on **n=100** MedQA subset (separate study) | MIT | 671B MoE | No / crowded Q4 / yes Q4; dual-Spark 405B-class **slow** | Visible CoT useful; decode bandwidth-limited |
| **HuatuoGPT-o1** (7/8/70/72B) | Think-before-answer; RL+verifier (paper/HF) | Inherits Llama/Qwen base | 7–72B | 8B easy; 70B mid–yes | Reasoning-oriented; not ICU-validated |
| **BioMed-R1 8B** | Strong among ~8B biomedical (stratified eval paper) | Llama 3.1 Community (base) | 8B | Easy / easy / easy | Knowledge/reasoning split research model |
| **QVAC MedPsy 4B** | HealthBench **74.0** / Hard **58.0** (vs MedGemma 27B **65.0** / **42.0**, their judge) | Apache 2.0 | 4B | Easy / easy / easy | Very new; English text; judge-protocol dependent |
| **gpt-oss-120b** | HealthBench **57.6** (Baichuan table / OpenAI card) | Apache 2.0 | 120B | Mid / yes / yes (~60–70 GB Q4) | Generalist; single ~80 GB GPU claim |
| **Baichuan-M2 32B** | HealthBench **60.1** / Hard **34.7** | Apache 2.0 (per project README) | 32B | Easy–mid / yes / yes (~16–20 GB Q4) | Strong HealthBench; **English coverage** / Chinese-origin caveat |

---

## Per-model notes

### MedGemma 27B / 4B (Google)
- **Verified:** 27B text-only MedQA **87.7%** (0-shot); with best-of-5 **89.8%** on model card. Google blog: within ~3 pts of DeepSeek R1 at ~**1/10 inference cost** ([Google Research blog](https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/), [tech report](https://arxiv.org/html/2507.05201v4), [model card](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card-v1)). R1 in same table: **90.1%**.
- **4B:** v1 MedQA **64.4%**; MedGemma **1.5** 4B MedQA **69.1%** ([1.5 report](https://arxiv.org/abs/2604.05081)).
- Variants: **4B multimodal**; **27B text-only** and **27B multimodal** (multimodal slightly lower on some text benches).
- License: **HAI-DEF** (not Apache).
- Memory: “fits ~24 GB at Q4” is a reasonable **weights+KV** ballpark for 27B Q4 on a mid GPU; on unified Mac/Spark still leave headroom for ASR + System One.
- **ICU caveat:** exam/VQA strong; **not** validated for real-time crisis companion cues.

### Med42-v2 (M42 Health)
- **Verified (HF card):** 70B MedQA **79.10**, USMLE **83.80**; 8B MedQA **62.84**, USMLE **67.04** ([Llama3-Med42-70B](https://huggingface.co/m42-health/Llama3-Med42-70B)).
- License: **Llama 3 Community** (+ M42 redistribution/acceptable-use).
- **Cerebras:** accurate for **original** Med42-70B (Llama 2) trained with Cerebras/Condor Galaxy ([Cerebras press](https://www.cerebras.ai/press-release/m42-announces-new-clinical-llm-to-transform-the-future-of-ai-in-healthcare)); v2 is M42’s Llama-3 suite — do not imply Cerebras trained every v2 checkpoint without a primary source.
- **ICU caveat:** clinical MCQA; not crisis-HUD validated.

### OpenBioLLM 70B (Saama / aaditya)
- **Verified scores (same Med42 table):** MedQA **76.90**, USMLE **79.01**.
- **License correction:** repository `LICENSE` is **Meta Llama 3 Community**, not Apache 2.0. Early README metadata incorrectly said Apache — **do not rely on that**.
- **ICU caveat:** superseded by newer reasoners for research path.

### DeepSeek R1 671B MoE
- **Verified:** Google MedGemma report lists R1 MedQA **90.1%**. A PMC analysis reports **93%** on a **100-question MedQA subset** — **not** the full benchmark ([PMC12213874](https://pmc.ncbi.nlm.nih.gov/articles/PMC12213874/)).
- License: **MIT** (DeepSeek-R1 HF).
- Fit: Mac **512 GB** Q4 practical for research; Spark 128 GB alone insufficient for full R1 + live stack; dual-Spark large-model decode **slow** (~1.8 tok/s community on 405B-class).
- **ICU caveat:** CoT helps auditability; still not crisis-validated; latency vs &lt;1–2 s cue budget.

### HuatuoGPT-o1 (7B / 8B / 70B / 72B)
- Think-before-answer with RL + verifier; bases Llama/Qwen → **licenses inherit base**.
- Useful as a mid-size reasoning candidate; cite FreedomIntelligence HF/papers for exact scores per size.
- **ICU caveat:** academic medical reasoning; not ICU companion.

### BioMed-R1 8B
- **Exists:** Zou et al. / EACL 2026 line of work; SFT+RL on reasoning-heavy medical QA; BioMed-R1-8B (Llama-3.1-8B) and 32B (Qwen2.5) ([arxiv 2505.11462](https://arxiv.org/html/2505.11462)).
- **ICU caveat:** stratified knowledge vs reasoning research; small; good experimental track, not production crisis proven.

### QVAC MedPsy 4B (Tether AI Research)
- **Verified:** HealthBench **74.00**, Hard **58.00** vs MedGemma-27B-text-it **65.00** / **42.00** under **CompassJudger-2-32B** ([HF MedPsy-4B](https://huggingface.co/qvac/MedPsy-4B), [blog](https://huggingface.co/blog/qvac/medpsy)). GGUF variants available for llama.cpp.
- License: **Apache 2.0** (card); note training data Genesis subsets CC-BY-NC.
- **Correction:** brief’s **70.33 / 54.33** figures match **MedPsy-1.7B**, not 4B.
- **ICU caveat:** very new (2026); HealthBench ≠ ICU crisis; English text-only.

### gpt-oss-120b (OpenAI)
- HealthBench **57.6** in Baichuan comparison / model card context; Apache **2.0**; marketed for single high-memory GPU (~80 GB class).
- **ICU caveat:** generalist; use with RAG if chosen for research path.

### Baichuan-M2 32B
- **Verified:** HealthBench **60.1**, Hard **34.7** ([Baichuan-M2 README](https://github.com/baichuan-inc/Baichuan-M2-32B/blob/main/README_en.md)); **higher** than gpt-oss-120b on that table — brief’s “~0.56” understated.
- License: **Apache 2.0** per project docs.
- **ICU caveat:** English coverage / evaluation language mix — verify English crisis transcripts before selecting.

### Legacy / not recommended as research primary
**Meditron, BioMistral, PMC-LLaMA** — historically important open medical LLMs, now generally **overtaken on open leaderboards** by MedGemma-class, HealthBench leaders (Baichuan-M2, MedPsy), and large reasoners (R1, gpt-oss). No single canonical “2026 finding” named that way; treat as **current consensus from newer benchmarks / Medmarks-style suites** rather than a specific citation. Keep for ablations only.

---

## Corrections to the brief

| Brief claim | Verified |
|-------------|----------|
| MedGemma 4B ~69% MedQA; v1 ~64.4% | **v1 = 64.4%**; **1.5 = 69.1%** — both true for different releases |
| MedGemma 27B 87.7% within ~3 pts of R1 @ ~1/10 cost | **Confirmed** (R1 90.1% in Google table; cost is Google claim) |
| Med42-v2 70B ~87% USMLE / ~86% MedQA | **Wrong** → **83.8% USMLE / 79.1% MedQA** |
| Med42 8B ~72% USMLE | **Wrong** → **67.0%** |
| Cerebras attribution | **OK for original Med42**; don’t over-claim for all v2 without source |
| OpenBioLLM ~84% USMLE / ~80% MedQA | **Wrong** → **~79% / ~77%** |
| OpenBioLLM Apache 2.0 | **Wrong** → **Llama 3 Community** |
| DeepSeek R1 ~93% MedQA | **Subset n=100**; full-table figure in Google report **90.1%** |
| MedPsy 4B HealthBench 70.33 / Hard 54.33 | **Those are MedPsy-1.7B**; **4B = 74.0 / 58.0** |
| Baichuan-M2 HealthBench ~0.56 | **Understated** → **60.1** |
| Legacy “2026 finding” | **No single named finding found** — state as consensus from newer benches |

---

## Suggested shortlist (suggestion only — OPEN DECISION)

| Profile | Fast / local reasoning + cues | Larger research model |
|---------|-------------------------------|------------------------|
| **V2B Mac Studio** | **MedGemma 27B** (baseline) | One of: **Baichuan-M2 32B**, **gpt-oss-120b**, or **DeepSeek R1** (512 GB) + RAG |
| **V2A Spark 128 GB** | **MedGemma 27B** Q4 **or** **MedPsy 4B** / MedGemma 4B draft | Mid: **Baichuan-M2 32B** or **Med42-v2 70B** Q4 — **not** full R1 concurrently with live stack |
| **Hybrid** | Spark: speech + System One; Mac: **MedGemma 27B** + large research RAG | Prefer Mac for literature-heavy research |

Always: **local RAG + citations**; clinician opt-in; T2/sim eval before trusting scores.

## Open decisions
- Which research model per profile?
- MedGemma 27B text-only vs multimodal for cue path?
- Adopt MedPsy 4B as experimental fast medical reasoner vs stay MedGemma-only?
- English-only eval plan for Baichuan-M2 if shortlisted?
