# V2 Comparison

## Speech A/B
| | V2A | V2B |
|--|-----|-----|
| ASR | Parakeet 0.6B CC-BY-4.0 | MedASR 105M HAI-DEF |
| Diar | Nemotron-3 OpenMDW | Nemotron-3 rec. / pyannote / sherpa |

## Shared System One (identical)
| | **NanoJev DEFAULT** | Laya FALLBACK |
|--|---------------------|---------------|
| Params | 0.6B | ~421M |
| Host | Laptop/small Mac edge; CUDA preferred for serve | Apple MLX |
| Choice | **2–255** (API-shape; hierarchy if vocab larger) | Weak at high cardinality |
| Fine-tune | Yes (MIT + Qwen terms; offline, replay, eval, pin) | Yes (Apache-2.0) |

Cloud = deep research only. No protocol cards. No continuous cloud decision stream.

## Caveat
0.6B does **not** lift the 255 Choice cap — hierarchical routing still required above cap ([HF NanoJev](https://huggingface.co/C-Tianyu/NanoJev)).

## Shared workstreams (identical)
Three fine-tune tracks (ASR differs A/B; MedGemma + NanoJev shared). Deep research = clinician wake-word/button opt-in only — see shared-layers WORKSTREAM A/B.
