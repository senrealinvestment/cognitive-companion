# Cognitive Companion — One-Pager

**Smart glasses ambient AI — cognitive companion for clinical medicine**  
Real-time cost + cue quality feedback loop  
*Audio + HUD only — no wearable camera (PHI / unit optics)*

---

## One sentence

Ambient **audio** from clinician smart glasses (or phone) feeds a local protocol brain on a nearby phone/iPad that delivers a **discrete cue** (short HUD text + tone). The clinician acts; we log whether the cue was **helpful** and **accurate** for offline training.

---

## Loop (physics of the product)

| Stage | What happens | Non-negotiable |
|---|---|---|
| **Sense** | Ambient listening (glasses mics and/or phone) | **No wearable camera.** Gate when possible; no continuous cloud stream |
| **Reason** | Cognitive-forcing suggestion (not autopilot orders) | Local protocol pack first; evidence API second |
| **Cue** | Tone + short visual HUD text | Discrete in ICU; no patient-facing spectacle |
| **Act** | Natural verbal response or clinical action | Human remains decision-maker |
| **Label** | Was cue helpful? Accurate? Cost/latency? | Required for every fired cue eventually |
| **Train** | Offline policy / model update | Never silent online self-modification at bedside |

---

## Where the brain lives (3 layers)

| Layer | Hardware | Job |
|---|---|---|
| **1 · Glasses** | Display + mics (+ bone conduction if available) | Hear the room + show/play short cue. **Tiny** computer. **No camera.** |
| **2 · Edge** | iPhone / iPad nearby (pocket/belt) | **Real-time brain:** gate → local protocols → safety → send cue. Label taps after. Audio-out fallback if glasses lack speakers. |
| **3 · Cloud (optional)** | Private cloud + OpenEvidence / UpToDate-class APIs | **Deep consult** after a trigger or on demand — stripped questions, not room audio dumps. |

**Rule:** fast whisper from the pocket binder; broad literature is the consultant on call.

---

## Why no camera (design law)

A face-worn camera in any ICU is a **PHI + consent + culture** problem, not just a tech feature:

- Patients, families, and staff in frame without clean consent
- Harder IRB / compliance / “what is that recording?” optics
- Little extra value for v0 cognitive-forcing if **speech + protocol context** carry the trigger

**Cognitive Companion v1 is audio-in → brain-on-phone → HUD + tone out.**  
Vision is out of scope until a separate, explicit, approved program exists.

---

## What this is / is not

**Is**
- Cognitive forcing for decompensations (sim + learners first)
- Ambient **listening** co-pilot with a closed quality loop
- Camera-free wearable path for Tx ICU / regulated care

**Is not**
- Body-worn video surveillance
- Autodiagnosis or automatic order entry
- Always-on cloud wiretap of the unit
- A replacement for board-certified judgment

---

## Hardware map (camera-free)

**Honest gap:** There is **no perfect** open-source glass today that is all of: *no camera + mics + bone-conduction speakers + HUD + fully open stack*.

We pick a **primary clinical path** and an **open build path**.

Sources: Brilliant Labs Halo materials; Even Realities G2 support/reviews (mics, no camera, no speakers on core G2); MentraOS ecosystem notes. Verify price/availability before buy.

### Scorecard (camera-free requirements)

| Requirement | Brilliant Labs **Halo** (open) | Even Realities **G2** (privacy-native) |
|---|---|---|
| **No wearable camera** | **Policy/firmware: camera OFF / unused** (hardware has one — must be hard-disabled for clinical mode) | **Native — no camera** |
| **Visual cue (HUD)** | Yes — color microOLED | Yes — binocular waveguide, mono green **640×350**, **27.5° FoV**, strong daylight text |
| **Ambient mics** | Yes | Yes — **four mics** (reviews/specs) |
| **Tone / audio out on glass** | Yes — **dual bone conduction** | **No speakers** on core G2 → use **phone / BC earbuds / AirPods** for earcons |
| **Open / hackable** | **Best** — open HW/SW, Zephyr, SDKs | Consumer product; **MentraOS**-class app layer helps |
| **All-day wear** | ~40 g, up to ~**14 h** claimed | ~**36 g**, multi-day with case (claims) |
| **Price (ballpark)** | ~**$299–349** | ~**$599** (+ Rx; optional ring) |
| **Fit to camera-free Cognitive Companion** | **Open prototype** if camera is truly off | **Clinical wear favorite** for unit optics |

### Recommendation (updated)

1. **Clinical / unit optics primary: Even Realities G2**  
   - No camera by design  
   - Strong discrete HUD + mics  
   - Pair with **phone edge brain** + **bone-conduction earbuds or phone earcon** for tone (G2 has no speakers)

2. **Open-source build primary: Brilliant Labs Halo with camera hard-off**  
   - Only serious open stack for custom cue firmware  
   - Onboard **bone conduction** = cleaner “tone on glass”  
   - **Clinical mode requirement:** camera powered off, no capture APIs, no LED/record UX — treat any camera use as a different product

3. **Do not depend on POV video** in protocols, diagrams, or IRB framing.

4. **Sim lab:** phone-only path works before any glasses arrive (mic + headphones + on-screen “HUD”).

### Hard gaps

- Neither is a medical device. Use = education / QI / research framing + IRB as required.
- G2 needs a **separate audio-out** plan for earcons.
- Halo needs a **written camera-off clinical profile** (not “we pinky-promise not to look”).
- PHI: short buffers, on-edge redaction, BAA only for stripped evidence queries.

---

## MVP slice (4 weeks of real work, not theater)

1. **Sim only** — scripted decompensations (post-reperfusion hypotension, rising lactate, airway risk, etc.).
2. **Cue types v0** — 3 earcons + ≤8-word HUD text; no free-form speech-to-clinician during crisis.
3. **Reasoner v0** — protocol card pack + optional OpenEvidence behind `{trigger, differential_nudge, next_check, confidence}`.
4. **Label UI** — Helpful Y/N, Accurate Y/N, optional 5-sec note.
5. **Metrics** — cue latency p50/p95, $/cue, %helpful, %accurate, interruptibility.

**Exit criterion:** learners prefer on vs off on ≥1 scenario class with no increase in harmful actions.

---

## Safety / ethics firewall

- Advisory language only (“consider”, “check”, “diff includes”).
- **No wearable camera** in v1 product definition.
- No automatic EMR write without explicit commit.
- Role separation if donor / prior-recipient edge cases appear in ambient audio (Prior Recipient→Donor Ethical Firewall).
- Full audit log of cues + labels; deletable retention.

---

## Artifact index

| File | Purpose |
|---|---|
| `cognitive-companion-architecture.html` | Architecture diagram (open in browser) |
| `cognitive-companion-flow.excalidraw` | Editable flow (excalidraw.com) |
| `ONEPAGER.md` | This brief |
| `assets/original-sketch.jpg` | Original whiteboard (historical; video path retired) |

---

## Next decisions for Sergio

1. **G2 vs Halo (camera-off)** for first sim-lab unit — or phone-only first?
2. First scenario pack: liver reperfusion instability vs generic ICU decompensation?
3. Evidence backend: OpenEvidence API vs local protocol YAML first?
4. Audio-out for G2 path: BC earbuds vs phone speaker vs skip earcon and HUD-only?

---

*Cognitive Companion • Tx ICU • Link / Hermes • camera-free v1*
