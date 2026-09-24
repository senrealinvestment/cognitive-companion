# V2 Speech + Router — A/B Comparison

Speech differs; **Jev-router shared path identical**. No protocol cards. Full shared design: [`V2-shared-layers.md`](./V2-shared-layers.md).

## Speech table

| Dimension | V2A NVIDIA | V2B Google |
|-----------|------------|------------|
| ASR | Parakeet-TDT 0.6B · CC-BY-4.0 | MedASR 105M · **HAI-DEF** |
| Diarization | Nemotron-3 · OpenMDW-1.1 | Nemotron-3 (rec.) / pyannote / sherpa |
| Fit | Noisy multi-speaker | Lighter ASR / dictation prior |
| + MedGemma | Edge box likely (FLAG-2) | Edge box likely (FLAG-2) |

## Shared router (both)

Speech → de-ID → **Jev (a salience · b category · c escalate · d action/urgency)** → fast MedGemma (+ domain LoRA/prompt + antibiogram) **and/or** delayed deep research → reconcile → gate (+ wording check) → HUD → labels (ASR + Jev thresholds + Gemma cue quality).

## Critical flags (both)

1. Continuous Jev salience vs no-continuous-cloud-streaming  
2. ASR+diar+MedGemma exceeds phone → edge box  
3. Generative cues need wording check  
4. Domain specialization = prompts / LoRA / separate models (not “sub-part”)  
5. No VCU institutional systems via Grok Bot; antibiogram = local static

## Verified MedGemma / OE (short)

- MedGemma 4B multi (1.0 + **1.5** Jan 2026), 27B text, 27B multi; **HAI-DEF**  
- OE: HIPAA/BAA for covered entities; **no public self-serve developer API** verified Sep 2026  
- Antibiogram: CLSI M39-style organism×drug %S table, annual, no PHI  

## Excalidraw

Not updated; HTML diagram is source of truth.
