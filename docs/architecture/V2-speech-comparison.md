# V2 Speech Layer — A/B Comparison

Side-by-side for Crisis Mirror V2 on-device speech. Shared downstream: [`V2-shared-layers.md`](./V2-shared-layers.md). Detail: [`V2A-nvidia-speech.md`](./V2A-nvidia-speech.md), [`V2B-google-speech.md`](./V2B-google-speech.md).

**V2 (both lanes):** speech → de-ID summary → **Jev** (Noul / Choice category / Score) → gate → HUD display label + tone; evidence API **only** on Jev escalation. **No protocol cards / card lookup** (V1 superseded for V2).

## Quick table

| Dimension | V2A NVIDIA | V2B Google / MedASR |
|-----------|------------|---------------------|
| ASR | Parakeet-TDT 0.6B (v2 En / v3 multilingual) | MedASR 105M Conformer |
| ASR license | **CC-BY-4.0** | **HAI-DEF Terms** (not Apache 2.0) |
| Diarization | **Nemotron-3-Diarization** (~100M, OpenMDW-1.1, ≤8 spk, streaming) | Separate: **Nemotron-3** (recommended) / pyannote community-1 / sherpa-onnx (license audit) |
| Medical prior | General ASR; DE medical PEFT exists; **no** verified EN ICU fine-tune yet | Strong **dictation** medical prior; ambient conversational gap |
| Streaming | Chunked ASR + native streaming diarization | Chunked / sliding-window ASR + chosen diarizer |
| On-device weight | Heavier (~600M + diar) | Lighter ASR (~105M); diar may dominate |
| Phone feasibility | Quantized CoreML (FluidAudio) on recent Apple Silicon; dual-model may need edge box | ASR easier on phone; diarization still hard |
| Fine-tune path | NeMo PEFT / LoRA + replay | Transformers SFT (+ PEFT); HAI-DEF on derivatives |
| Best fit | Noisy multi-speaker accuracy | Phone-first footprint / medical vocab bootstrap |
| Main risk | Thermals / RAM / no EN medical adapter yet | License complexity + domain shift dictation→ICU |

## Recommended V2B diarization

1. **MedASR + Nemotron-3-Diarization** (default)  
2. MedASR + pyannote `community-1` on edge box  
3. MedASR + sherpa-onnx **after** weight-license audit  

## Shared (identical across A/B)

ASR flywheel · **Jev as core decision/categorization** · simplified safety gate · conditional evidence API · offline labels → ASR flywheel **and** Jev thresholds · thin category→display-label map **or** generative cue (**OQ-1**, undecided).

## Corrections worth memorizing

1. MedASR ≠ Apache 2.0 (weights = HAI-DEF).  
2. Nemotron 3 Diarization **does** exist (2026-09-23).  
3. OpenMDW covers Nemotron diarization; Parakeet is CC-BY-4.0.  
4. “Medical Parakeet on HF” ≠ English ICU (DE fine-tune only at write time).  
5. **V2 has no protocol-card layer** — do not reintroduce card boxes in diagrams or notes.

## Reset open questions (both stacks)

| ID | Question |
|----|----------|
| OQ-1 | Category→≤8-word vetted HUD label (default proposal) vs generative LLM cue? |
| OQ-2 | Who owns taxonomy; how many categories; `none`/`other`? |
| OQ-3 | Escalation: separate Noul vs category flag; evidence UI; latency? |
| OQ-4 | Gate on Noul only vs also Choice confidence? |
| OQ-5 | Labels tune thresholds (± taxonomy revisions); Jev not fine-tuned by us |

## Excalidraw

`crisis-mirror-flow.excalidraw` was **not** updated in this PR (non-trivial layout). Use `crisis-mirror-architecture.html` as the V2A/V2B source of truth (dual speech lanes, Jev core, no cards).
