# V2 Shared Layers (identical across V2A · V2B · Hybrid)

> **V2A and V2B are FULL STACKS** (NVIDIA Spark path vs Apple Mac path), not speech-only.  
> This file is the **shared product spine**: SystemOneClient adapter, safety gate, labeling loop, clinician opt-in deep research, three fine-tune tracks, data platform.  
> Hardware comparison: [`V2-hardware-options.md`](./V2-hardware-options.md) · Hybrid: [`V2-hybrid.md`](./V2-hybrid.md) · Local research LLMs: [`V2-local-medical-reasoning-models.md`](./V2-local-medical-reasoning-models.md).

> **Target setting:** all intensive care units (critical care broadly: medical, surgical, transplant, neuro, cardiac, and other critical care units). Broadened from transplant ICU on 2026-09-24. **Advisory only:** cues suggest, the clinician decides; nothing here makes or executes clinical decisions.

---  
> **No cloud Jev. No protocol cards.**  
> **Hardware axis** is separate from speech axis.

---

## HARDWARE TARGET — tension addressed plainly

### What Sergio wants
**Mac Studio with 512 GB unified memory** — maximum headroom for large models, many LoRA adapters, local research LLM + RAG, on-box fine-tuning, expansion.

### Verified availability (as of 2026-09)
| Fact | Detail | Source |
|------|--------|--------|
| Chip | **M3 Ultra** Mac Studio (2025) supports up to **512 GB** unified memory; **819 GB/s** memory bandwidth | [Apple Support specs](https://support.apple.com/en-us/122211), [Apple M3 Ultra news](https://www.apple.com/newsroom/2025/03/apple-reveals-m3-ultra-taking-apple-silicon-to-a-new-extreme/) |
| Launch price | ~**$9,499** USD for 512 GB + modest SSD configs (press/configurator era) | [ServeTheHome](https://www.servethehome.com/new-512gb-unified-memory-apple-mac-studio-is-the-local-ai-play/) |
| **New-order status** | **Apple removed the 512 GB configurator option ~March 2026**; new Store max often **256 GB** (DRAM shortage reporting) | [MacDailyNews](https://macdailynews.com/2026/03/06/apple-drops-512gb-m3-ultra-mac-studio-option-ups-256gb-memory-upgrade-by-400/), [Apfelpatient](https://www.apfelpatient.com/news/mac-studio-512gb-ram-upgrade-no-longer-available-for-order) |
| Used market | Existing 512 GB units trade at **high premiums** (listings ~$16k–$21k median — volatile) | [vramglass](https://vramglass.com/gpu/mac-studio-m3-ultra-512gb) |

**Write-up for procurement:** Design **targets M3 Ultra 512 GB** when obtainable (used/refurb/institutional stock). If only **256 GB new** is buyable, recalculate concurrent residency (still large, but tighter for full DeepSeek-671B-class + 27B + training). **OPEN DECISION:** buy used 512 GB vs new 256 GB vs wait for next Ultra / add NVIDIA H2.

### Stationary desktop ≠ pocket edge
Mac Studio lives in the **sim lab / unit rack**. **Glasses + phone are thin clients** streaming **audio over LOCAL network (LAN/Wi‑Fi)** to the Mac.  
- **“No continuous cloud streaming” still holds** (no off-prem decision stream).  
- **Bedside clinical use** implies continuous audio on the **hospital network** → needs **hospital IT/security approval**; **sim lab is fine**.  
- Network notes: encrypt in transit (TLS/mTLS or VPN segment); phone-side **minimal local buffer** on Wi‑Fi drop; degrade to phone-only keyword/HUD if Mac unreachable; measure RTT (target audio chunk delivery ≪ cue budget).

---

## HARDWARE PROFILES (axis H1 / H2) — do NOT collapse V2A/V2B

| Profile | Box | System One default | Training bias |
|---------|-----|--------------------|---------------|
| **H1 (default)** | Mac Studio 512 GB (target) / 256 GB if forced | **Laya** (MLX native) | MLX-LM LoRA; HF on MPS where needed |
| **H2 (institutional)** | NVIDIA CUDA box | **NanoJev** (:8765) | NeMo / CUDA PEFT |

**OPEN DECISION (prominent):** Mac-only with Laya (H1) **vs** keep NVIDIA as parallel institutional option (H2). Recommendation: **keep both profiles documented**; ship H1 first for VCU sim if Mac path clears IT.

### Speech × hardware matrix

| | H1 Mac Studio (MLX/CoreML/MPS) | H2 NVIDIA CUDA |
|--|--------------------------------|----------------|
| **V2A Parakeet inference** | **OK** — `parakeet-mlx`, FluidAudio CoreML | **OK** — NeMo |
| **V2A Nemotron-3 / Sortformer diar inference** | **Partial/OK** — FluidAudio / community **Sortformer CoreML**; dedicated `Nemotron-3-Diarization` NeMo weights may need ONNX/MPS port or use Sortformer CoreML stand-in until ported | **OK** — NeMo native |
| **V2B MedASR inference** | **Likely OK** — Transformers on MPS / export ONNX; less mature than Parakeet-MLX | **OK** |
| **V2A T1 training (NeMo)** | **Awkward** — NeMo is **CUDA-centric**; plan H2 or remote CUDA for V2A train, or accept limited MPS experiments | **OK** |
| **V2B T1 training (HF)** | **Feasible** — Transformers PEFT on MPS/MLX path; slower than CUDA | **OK** |
| **T2 MedGemma / T3 System One train** | **OK** on H1 via MLX-LM LoRA (esp. 4B; 27B LoRA feasible with headroom) | **OK** CUDA |

Sources: [parakeet-mlx](https://github.com/senstella/parakeet-mlx), [FluidAudio](https://github.com/FluidInference/FluidAudio) (Parakeet CoreML + Sortformer diarization).

**Recommendation:** Keep **V2A and V2B as speech options**. Pick **H1 or H2** independently. Example: H1+V2B for easiest Mac train story; H1+V2A for best Mac inference if Sortformer CoreML acceptable; H2+V2A for full NeMo train+infer.

---

## SYSTEM ONE — Laya on V2B (Mac); NanoJev on V2A (Spark)

| | **Laya — DEFAULT on H1 Mac** | **NanoJev — DEFAULT on H2 NVIDIA** |
|--|------------------------------|-------------------------------------|
| Why | Apple Silicon **MLX native**; in-process; fits “Mac path” | CUDA serve docs; more capacity after fine-tune |
| Params | ~421M (322M multi) | 0.6B |
| License | Apache-2.0 | MIT code + Qwen terms |
| API | `laya-serve` `/v1/systemone` | `/api/evaluate` :8765 → **SystemOneClient adapter** |
| Choice | Weak at **50+** options at default head budget → **hierarchical routing** + fine-tune; **512 GB does not change Laya capacity** | Documented **2–255**; hierarchy if vocab >255 |
| NanoJev on Mac | Needs **MLX/CUDA-alternative port** (Qwen3-0.6B backbone — feasible engineering, not free) or run on H2 | Native |

Swap remains config (`SystemOneClient` backend = `laya` | `nanojev`).

---

## MedGemma — 27B BASELINE

| | Role |
|--|------|
| **MedGemma 27B** (text-IT / multimodal) | **Baseline** cue / reasoning model on H1 |
| **MedGemma 4B** | Low-latency draft / speculative fast path if useful |

License: **HAI-DEF**. Memory (**estimates**):

| Precision | 27B weights (order-of-magnitude) |
|-----------|----------------------------------|
| bf16 | ~54 GB |
| 8-bit | ~27–30 GB |
| 4-bit | ~14–16 GB (MLX/GGUF class; runtime + KV higher) |

Proxy throughput: Gemma-3/MedGemma-class **27B 4-bit on M3 Max ~15–28 tok/s** (community benches; **M3 Ultra should be similar or better — measure on box**). Cue ≤8 words (~10–20 tokens) → **sub-second to ~1–2 s generation plausible** after TTFT; still validate against **&lt;1–2 s** fast-path budget including ASR+Laya. Sources: [mlx-benchmark bands](https://github.com/Travis-ML/mlx-benchmark), [LLMCheck Gemma3 27B M3 Max](https://llmcheck.net/models/gemma-3-27b-on-m3-max/).

### Concurrent residency budget on 512 GB (**estimates**)

| Resident | Est. RAM |
|----------|----------|
| ASR (Parakeet or MedASR) | 0.2–1.2 GB |
| Diarization | ~0.1–0.5 GB |
| Laya | ~0.7–1.5 GB |
| MedGemma 27B 4-bit + KV | ~20–40 GB (ctx-dependent) |
| Local research LLM (see below) | 20–400 GB depending on pick |
| Embeddings + vector index | 1–20 GB |
| OS + headroom | 20–40 GB |
| **Training job** | Do **not** co-schedule with live sim unless budgeted; prefer **off-hours** |

512 GB fits **27B + large RAG + mid/large research model**; full **DeepSeek-671B Q4 (~350–400 GB)** leaves little room for concurrent live stack — pick one heavy resident or schedule.

Fine-tune 27B on-box: **MLX-LM LoRA/QLoRA** feasible; slower than NVIDIA GPUs (**relative throughput unknown without our bench — label unknown**).

---

## LOCAL System One routing (a–d) — unchanged roles
Salience · category · escalate · action/urgency — all **local** (Laya on H1).

---

## DEEP RESEARCH — local PRIMARY; OpenEvidence OPTIONAL

### Critical honest framing
**A local LLM alone does not replace OpenEvidence.** OE’s product value is **licensed current literature + retrieval + citations**. Local path = **research LLM + corpus we have rights to + mandatory citations**.

### Primary: fully local
1. **Local research LLM** (candidates for 512 GB):
   - **MedGemma 27B** itself (reuse baseline; weaker as “deep lit” without RAG)
   - **Qwen3 / Qwen2.5 32B–72B** 4-bit (~20–50 GB class) — good RAG generators
   - **DeepSeek-R1 distill** 32B/70B — reasoning-style, fits easily
   - **Full DeepSeek-V3/R1 671B MoE** Q4 ~**350–400 GB** — fits 512 GB with little else; licenses open-weight — verify before ship  
   Sources: [inventivehq DeepSeek local](https://inventivehq.com/blog/run-deepseek-locally), DeepSeek tech reports.
2. **Local retrieval:** PubMed baseline dumps / **PMC Open Access**, open guidelines, local antibiogram/protocols; embeddings + vector index on-box.  
3. Rules: **mandatory citations**; **no source = no claim**; corpus refresh cadence; **knowledge-cutoff** caveat; **paywalled journals excluded**.  
4. Optional: de-ID **PubMed E-utilities** live query (public API, no PHI) — still a **network call** + policy decision.

### Optional cloud: OpenEvidence
Only if/when **enterprise BAA** secured. **No verified public self-serve API** (enterprise/Epic integrations). Dashed fallback in diagram.

### Still clinician opt-in
Wake word / button; never auto; soft glyph from System One. **Wake phrase (placeholder, 2026-09-24): "Hey Dr. Bellomo"**. A multi-word phrase like this is less likely to fire by accident on normal room talk. It needs a custom-trained model, because no off-the-shelf model knows this phrase. The name honors Prof. Rinaldo Bellomo AO, the intensive care researcher who died on 6 May 2025. Before any public or commercial use, get permission from his family or estate so the phrase doesn't imply an endorsement. Latency local deep: **estimate 5–30 s** depending on retrieval+gen (**labeled estimate**). Output: panel+citations primary; optional MedGemma one-liner + wording check.

---

## Fast path / gate / antibiogram / labeling
Unchanged: MedGemma (+4B draft option) · local antibiogram · gate+wording check · labels → T1/T2/T3 offline · no bedside self-update.

---

## CRITICAL FLAGS
1. **512 GB new-buy may be unavailable** — procurement reality vs design target.  
2. Thin clients + LAN audio = hospital IT for clinical; sim OK.  
3. NanoJev needs CUDA or a **port** for Mac.  
4. Laya ≠ high-cardinality Choice; hierarchy required.  
5. Local LLM ≠ OE without licensed corpus + citations.  
6. V2A NeMo **training** awkward on H1.  
7. Don’t train during live sim unless budgeted.  
8. VCU systems ≠ Grok Bot.

---

## Open decisions (updated)
- Procure **used 512 GB** vs **new 256 GB** vs wait / H2 NVIDIA  
- **H1-only vs H1+H2** institutional dual path  
- Speech choice V2A vs V2B on H1 (inference vs train tradeoff)  
- Accept Sortformer CoreML vs require Nemotron-3 port on Mac  
- Laya hierarchy cutover threshold  
- MedGemma 27B quant (4 vs 8-bit) + whether 4B speculative draft stays  
- Local research LLM pick (72B vs 671B MoE tradeoff)  
- Corpus rights (PMC OA + guidelines) + E-utilities policy  
- OE enterprise BAA pursue or defer  
- Wake-word engine (placeholder phrase: "Hey Dr. Bellomo"; custom model needed; tribute to the late Prof. Bellomo; get family/estate permission before shipping)  
- Gold nudge authors / sim consent  

---

## Sources (hardware / Mac speech / research)
- https://support.apple.com/en-us/122211  
- https://www.apple.com/newsroom/2025/03/apple-reveals-m3-ultra-taking-apple-silicon-to-a-new-extreme/  
- https://macdailynews.com/2026/03/06/apple-drops-512gb-m3-ultra-mac-studio-option-ups-256gb-memory-upgrade-by-400/  
- https://github.com/senstella/parakeet-mlx · https://github.com/FluidInference/FluidAudio  
- Prior MedGemma / OE / Laya / NanoJev sources in earlier sections / git history  

*(Prior WORKSTREAM A three fine-tune tracks and WORKSTREAM B opt-in deep research remain in force; deep path primary is now **local RAG**, OE optional — see above.)*


---

## WORKSTREAM A (retained) — Three fine-tune tracks

**KER / noise-aug / audio de-ID = speech only.** MedGemma never hears audio.

- **T1 ASR:** V2A Parakeet (NeMo — prefer H2 train) / V2B MedASR (HF — H1 feasible); KER+WER+DER; replay.  
- **T2 MedGemma:** **27B baseline** (4B draft optional); clinician gold nudges; LoRA on H1 MLX; eval gates incl. dosing refusal + MedQA regression.  
- **T3 System One:** Laya (H1) or NanoJev (H2); ECE; hierarchy if needed.  

Shared: sim consent, de-ID, DVC/HF versions, registry, rollback, no bedside self-update; VCU approval ≠ Grok Bot.

## WORKSTREAM B (retained, updated) — Deep research opt-in

Never auto-fires. Soft suggest → wake/button → **local RAG primary** (citations mandatory) → optional OE if BAA. Panel primary; optional MedGemma HUD one-liner + wording check.


### Local medical reasoning model catalog
See [`V2-local-medical-reasoning-models.md`](./V2-local-medical-reasoning-models.md) for verified benchmarks, licenses, memory fit (Spark/Mac), corrections to brief figures, and a suggested shortlist (MedGemma 27B baseline + one larger research model per profile).
