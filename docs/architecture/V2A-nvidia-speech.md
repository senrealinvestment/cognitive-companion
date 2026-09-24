# V2A — NVIDIA speech + local System One (NanoJev default)

**Differs from V2B:** ASR + diarization only.  
**Shared:** [`V2-shared-layers.md`](./V2-shared-layers.md). **NanoJev default · Laya fallback.** No cloud Jev. No cards.  
**Edge target:** laptop / small Apple Silicon Mac.

## Speech (verified)
Parakeet-TDT 0.6B (**CC-BY-4.0**) + Nemotron-3-Diarization (~100M, **OpenMDW-1.1**, ≤8 spk, streaming). Chunked ASR. No verified EN ICU Parakeet fine-tune (DE PEFT only).

## Flow
Mics → Parakeet + Nemotron-3 → de-ID → **NanoJev (Laya fallback)** (a–d) → MedGemma fast / cloud deep → gate → HUD → labels (incl. NanoJev offline fine-tune).

## Open decisions
Speech compute on laptop/Mac; v2 vs v3; CUDA for NanoJev vs Laya fallback on Apple-only; Choice hierarchy if vocab >255.
