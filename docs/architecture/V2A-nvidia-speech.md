# V2A — Full NVIDIA stack (DGX Spark path)

> **Retitled:** V2A is no longer “speech-only.” It is the **NVIDIA full stack**. Shared layers still identical: [`V2-shared-layers.md`](./V2-shared-layers.md). Hardware detail: [`V2-hardware-options.md`](./V2-hardware-options.md).

## Stack
| Layer | Choice |
|-------|--------|
| Box | **DGX Spark** (GB10, 128 GB, CUDA) — or smaller Jetson AGX Orin/Thor for reduced edge |
| System One | **NanoJev** (native CUDA, :8765) |
| ASR | Parakeet-TDT 0.6B (CC-BY-4.0) |
| Diarization | Nemotron-3-Diarization (OpenMDW-1.1) |
| Training | **NeMo on-box** (T1 ASR, T3 NanoJev) |
| Fast LLM | **MedGemma** — **27B fits** on 128 GB (bf16 ~54 GB or 4-bit ~15–20 GB); 4B optional for drafts |
| Deep research | Local research model on Spark **or** call Mac service in hybrid; OE optional BAA |

## Why V2A
Full CUDA: NanoJev + NeMo without ports. Compact, ~$4k class, low power vs Studio. Weaker for huge RAG corpora / 671B-class comfort than Mac 512.

## Speech facts (retained)
Parakeet CC-BY-4.0; Nemotron-3 ~100M OpenMDW; chunked ASR.

## See also
Shared gate, labeling, opt-in deep research, three fine-tune tracks, SystemOneClient.

## Local medical reasoning models
Catalog (benchmarks, licenses, Spark/Mac fit, shortlist): [`V2-local-medical-reasoning-models.md`](./V2-local-medical-reasoning-models.md).
