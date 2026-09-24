# Crisis Mirror

**Smart glasses ambient AI — cognitive companion for clinical medicine**  
Real-time cue + cost/quality feedback loop for transplant ICU / critical care.

![Crisis Mirror Architecture](assets/crisis-mirror-architecture.png)

## Concept

Ambient **audio** (glasses mics and/or phone) → **phone/iPad edge brain** (local protocol pack + safety gate) → discrete cue (**HUD text + tone**) → clinician action → post-hoc labels (*helpful?* *accurate?*) for **offline** training.

Optional **OpenEvidence / UpToDate-class** APIs = deep consult after a trigger — not continuous cloud listening.

### Design law: no wearable camera (v1)

Face-worn video is a PHI / consent / unit-culture problem.  
**v1 senses with sound only.** Visual context is out of scope until separately approved.

### Where the brain lives

| Layer | Device | Role |
|-------|--------|------|
| Thin wearable | Smart glasses (**no camera**) | Mics + HUD (+ bone conduction if present) |
| Edge brain | iPhone / iPad nearby | Real-time detect + local protocols + safety + label UI |
| Deep consult | Secure cloud APIs | Broader evidence on demand (stripped queries) |

## Hardware lean

| Path | Device | Why |
|------|--------|-----|
| **Clinical / privacy-native** | [Even Realities G2](https://www.evenrealities.com/) | **No camera**, HUD + mics; tone via phone or BC earbuds (G2 has no speakers) |
| **Open-source build** | [Brilliant Labs Halo](https://brilliant.xyz/) | Open stack + onboard bone conduction; **camera hard-off** for clinical mode |
| **Before any glasses** | Phone only | Mic + headphones + on-screen HUD — valid sim path |

Details and scorecard: [ONEPAGER.md](ONEPAGER.md).

## Artifacts

| File | Description |
|------|-------------|
| [ONEPAGER.md](ONEPAGER.md) | Product brief, MVP, safety, hardware scorecard |
| [FUNDING.md](FUNDING.md) | Funding map: institutional → NIH/AHRQ → SBIR → ARPA-H |
| [VCU-ANESTHESIOLOGY-FUNDS-REQUEST.md](VCU-ANESTHESIOLOGY-FUNDS-REQUEST.md) | Internal funds request — VCU Dept of Anesthesiology |
| [crisis-mirror-architecture.html](crisis-mirror-architecture.html) | Interactive dark architecture diagram (V2: dual speech · Jev core · no cards) |
| [assets/crisis-mirror-architecture.png](assets/crisis-mirror-architecture.png) | Architecture diagram (PNG) |
| [crisis-mirror-flow.excalidraw](crisis-mirror-flow.excalidraw) | Editable flow (open on [excalidraw.com](https://excalidraw.com)) |
| [assets/original-sketch.jpg](assets/original-sketch.jpg) | Original whiteboard sketch (historical) |


## V2 architecture notes (speech A/B · Jev core)

V2 **supersedes the V1 protocol-card layer**. **Jev is a multi-point router** (salience · category · escalation · action/urgency) over a de-ID speech stream. **Local fast path:** MedGemma (or lighter Gemma) + domain sub-agents (e.g. ID + local antibiogram). **Deep path:** OpenEvidence-class, only when Jev escalates. Cue text: MedGemma generative (leading) or vetted category labels (fallback). Only the on-device speech stack is A/B’d. See critical flags in the shared note (continuous Jev streaming vs design rule; phone compute; etc.).

| File | Description |
|------|-------------|
| [docs/architecture/V2-shared-layers.md](docs/architecture/V2-shared-layers.md) | Shared path: Jev multi-point router, MedGemma fast path, deep research, gate, labels, critical flags |
| [docs/architecture/V2A-nvidia-speech.md](docs/architecture/V2A-nvidia-speech.md) | Parakeet-TDT + Nemotron-3 Diarization |
| [docs/architecture/V2B-google-speech.md](docs/architecture/V2B-google-speech.md) | MedASR + open-weight diarization options |
| [docs/architecture/V2-speech-comparison.md](docs/architecture/V2-speech-comparison.md) | Side-by-side table + recommended V2B diarization |
| [crisis-mirror-architecture.html](crisis-mirror-architecture.html) | Diagram: dual speech → Jev router (a–d) → fast/deep → gate → HUD (no cards) |

## Status

Early concept / sim-lab first. **Camera-free v1.** Not a medical device. Advisory cognitive-forcing only.

## License

Private working notes unless otherwise stated.
