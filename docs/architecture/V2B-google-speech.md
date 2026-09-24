# V2B — Full Apple stack (Mac Studio path)

> **Retitled:** V2B is the **Apple full stack**, not speech-only. Shared: [`V2-shared-layers.md`](./V2-shared-layers.md). Hardware: [`V2-hardware-options.md`](./V2-hardware-options.md).

## Stack
| Layer | Choice |
|-------|--------|
| Box | **Mac Studio** target **512 GB** M3 Ultra (819 GB/s); new-buy may be **256 GB max** |
| System One | **Laya** (MLX native; hierarchical Choice if 50+) |
| ASR | MedASR 105M (HAI-DEF) |
| Diarization | Sortformer CoreML / pyannote / Nemotron port |
| Training | MLX-LM LoRA (T2 MedGemma, T3 Laya); T1 MedASR via HF/MPS |
| Fast LLM | **MedGemma 27B** baseline (+ 4B draft optional) |
| Deep research | **Local research LLM + literature RAG** primary; OE optional |

## Why V2B
Max memory for 27B + large RAG + research models; Laya without CUDA port. NeMo/NanoJev not native.

## Thin clients
Glasses/phone stream audio over **LAN** to Studio (sim OK; hospital IT for clinical).

## Local medical reasoning models
Catalog (benchmarks, licenses, Spark/Mac fit, shortlist): [`V2-local-medical-reasoning-models.md`](./V2-local-medical-reasoning-models.md).
