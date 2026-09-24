# V2 Full-stack comparison (speech is only one axis)

See [`V2-hardware-options.md`](./V2-hardware-options.md) for Mac vs Spark vs Hybrid tables.

| | **V2A NVIDIA (Spark)** | **V2B Apple (Mac Studio)** |
|--|------------------------|----------------------------|
| Box | DGX Spark 128 GB · 273 GB/s · CUDA | Mac Studio ≤512 GB · 819 GB/s · MLX |
| System One | NanoJev | Laya |
| ASR | Parakeet-TDT | MedASR |
| Diarization | Nemotron-3 | Sortformer CoreML / other |
| MedGemma | 27B fits on 128 GB | 27B baseline + headroom |
| Deep research | Mid-size local; dual-Spark 405B slow | Large local RAG preferred |
| Train | NeMo native | MLX / HF MPS |

**Caveat:** Full-stack differences confound speech-only conclusions → **speech bake-off on one box**.

**Hybrid:** both machines, service split — [`V2-hybrid.md`](./V2-hybrid.md).
