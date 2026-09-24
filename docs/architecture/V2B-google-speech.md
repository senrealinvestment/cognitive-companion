# V2B — MedASR speech + local System One (NanoJev default)

**Differs from V2A:** ASR + diarization only.  
**Shared:** [`V2-shared-layers.md`](./V2-shared-layers.md). **NanoJev default · Laya fallback.**  
**Edge target:** laptop / small Apple Silicon Mac.

## Speech (verified)
MedASR 105M (**HAI-DEF**, not Apache) + open diarization (**Nemotron-3 recommended**). Dictation-prior; ambient ICU gap to fine-tune.

## Flow
Same shared NanoJev router path as V2A after de-ID.

## Open decisions
Diar pairing; NanoJev CUDA vs Laya on Apple; hierarchy if >255 categories.

## See also (shared, identical)

- Fine-tune tracks T1/T2/T3 + data platform: [`V2-shared-layers.md`](./V2-shared-layers.md) § WORKSTREAM A
- Deep research clinician opt-in (never auto-fire): same file § WORKSTREAM B
