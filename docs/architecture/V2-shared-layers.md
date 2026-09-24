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
