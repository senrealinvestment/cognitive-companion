# Cognitive Companion — research pack summary

**For:** Sergio  
**Source:** researcher pack, retrieved 2026-08-18  
**This file:** short readout of that pack, not a new study  
**Status:** local only — `research/` is not on GitHub  
**Not:** a protocol, IRB letter, buy order, or legal opinion

Full pack: `~/Projects/cognitive-companion/research/`  
Preferred original: `cognitive-companion-v2-evidence-brief.md`  
Bibliography: `citations.md` `[1]`–`[48]`

---

## Bottom line

Keep v1 **camera-free**. Do **not** claim glasses improve patient outcomes.

What you can honestly claim: a **test** of whether HUD + short audio cues improve **process adherence** versus phone-only, using checklist-grade content.

| Claim | Status |
| --- | --- |
| Halo exists, ~40 g, $399, dual mics, bone-conduction speakers, 256×256 HUD, 640×480 camera, 300 mAh, OTA firmware | Fact `[1]` `[3]` |
| Halo is **not** verified for health-critical use | Fact `[3]` |
| Even G2 is camera-free by design, 36 g, 4 mics, 640×350, IP65, G2-A $599 | Fact `[4]` `[6]` |
| G2 speakers / audio-out | **Unknown** |
| Crisis checklists in high-fidelity sim: 6% vs 23% missed lifesaving steps | Fact `[34]` |
| Tablet CDS (PediAppRREST) cut guideline deviations vs paper card or no aid | Fact `[45]` |
| Those two trials support the **content**, not glasses | Fact / pack lock |
| Anesthesia HMD studies change detection or gaze — not clinical outcomes | Fact `[18]` `[20]` `[35]` |
| Camera-free is the right privacy posture for a VCU sim pilot | Inference |
| Halo can be the pilot SKU **only if** cam hard-off is a documented disable, not a software mute next to an OTA camera | Inference |
| Phone/iPad-only is the honest control arm and the fallback | Inference |

**Decision the pack already made:**

1. Halo-with-camera-disabled = procurement path **iff** disable is written down. Do not call Halo “camera-free.”
2. G2 = factory-camera-free alternative, pending speaker confirmation.
3. Phone/iPad-only = arm 3, not a failure.

---

## What the pack is

Seven files, written 2026-08-18. v1 brief from 2026-08-17 was **kept**, not rewritten.

| File | Role |
| --- | --- |
| `cognitive-companion-v2-evidence-brief.md` | Shareable brief. Start here. |
| `cognitive-companion-v1-evidence-brief.md` | Frozen prior brief. |
| `citations.md` | Live URLs `[1]`–`[48]`. |
| `hardware-halo-g2-phone.md` | Halo vs G2 vs phone/iPad. |
| `literature-cognitive-forcing-hud-sim.md` | Forcing functions, HUD/HMD, sim CDS. |
| `privacy-phi-irb-camera-free-audio.md` | HIPAA / Common Rule / VA 19.2-62 / VCU HRPP / FDA CDS 2026. |
| `gaps-and-open-questions.md` | What still blocks over-claim. |

Committed product docs (not this pack): `README.md`, `ONEPAGER.md`, `FUNDING.md` (GitHub sponsors file, **not** a grant map), `VCU-ANESTHESIOLOGY-FUNDS-REQUEST.md`, `Cognitive-Companion-Presentation.pptx`.

**Conflict with committed copy:** live Halo list is **$399**, not the older $299–$349 band. Update the $12.5k / $7.5k ask or footnote the date. Do not split the difference.

---

## Hardware, one table

| | Halo | Even G2 / G2-A | Phone / iPad only |
| --- | --- | --- | --- |
| Price (2026-08-18) | $399 `[1]` | $599 `[6]` | $0 incremental if device already there |
| Mass | ~40 g `[1]` | 36 g `[4]` | Handheld |
| Camera | Yes — 640×480 on the board `[3]` | None, by design `[4]` | Exists; keep unused |
| Mics | Dual / stereo `[1]` `[3]` | Four `[4]` | Device mics |
| Audio out | Bone conduction `[1]` `[3]` | **Unknown** | Speaker / AirPods / cart |
| Display | 256×256 `[3]` | 640×350 `[4]` | Full screen |
| Battery | 300 mAh stated; **runtime unknown** `[3]` | Not extracted | Hours, but gaze leaves the manikin |
| Durability | No IP on fetched pages | IP65, 40k hinges, 2 m drop `[4]` `[5]` | Varies |
| Health disclaimer | Not verified for health-critical use `[3]` | Not seen | Consumer device |

Mentra Live is **camera-enabled** (43 g). Not a v1 candidate. MentraOS listing Even Realities is an OS path for G2, not a headset choice `[7]`.

**“Cam hard-off” is not a SKU.** Docs describe the PixArt sensor and OTA firmware. They do not describe a kill-switch, module-removed SKU, or documented firmware flag. If OTA can re-enable the camera, a one-time software mute is not hard-off.

If G2 has no speakers, voice comes from the phone — a different product than Halo’s bone-conduction path. Absence of a spec line is **unknown**, not “G2 has no speakers.”

---

## What the literature actually buys you

### Content (transfers)

- Croskerry: forcing functions / cognitive forcing as debiasing theory `[37]` `[38]`. Parent of “consider X / do not skip Y,” not of Halo’s camera.
- Arriaga 2013: 17 teams, 106 simulated crises; 6% vs 23% missed lifesaving steps with vs without checklists; every team better with the list `[34]`.
- Harrison 2006: MH sim — aid use correlated with treatment score; best teams used the aid extensively `[29]`.
- Corazza 2023: tablet app, fewer guideline deviations than a PALS card or no aid `[45]`.

### Packaging (analog, not this product)

- Sanderson 2008: audio 90% and audio+HMD 92% event detection vs visual 52%; **HMD-alone 75% not significantly better**. Conclusion: advanced auditory displays helped; an HMD did not `[18]`.
- Liu 2009: HMD helped when physically constrained, not when unconstrained `[19]`.
- Liu 2010: HMD 21.0% vs 25.3% gaze at workstation; 55.9% vs 51.5% gaze at patient/field. Process, not outcomes `[20]`.
- Elrose 2021: **zero** of 7 clinical-context head-worn vital-sign studies reported clinical outcomes `[35]`.

### Does not transfer

Google Glass / AR-video CPR papers assume a camera or video stack `[23]`–`[26]`. Adjacent. Not evidence for Halo-cam-off or G2.

**Implication:** a HUD that only relocates a monitor may buy gaze time and may help only when hands are busy. Audio may be the stronger detection channel. Putting checklist content on glasses is an **untested packaging choice**.

---

## Privacy / IRB / FDA — short

- A manikin is not an individual. A standardized patient’s **voice** can still identify a person. No real-patient IIHI is the working assumption; confirm with VCU privacy before any live-bay spillover `[9]`.
- Do **not** say “HIPAA doesn’t apply, so we can record.”
- VCU: research = systematic investigation designed to contribute to generalizable knowledge. Most QI is not research. If unclear, submit in **VIRBs** `[15]` `[16]`.
- Local curriculum QI (no paper) may sit outside IRB. A paper, abstract, or “we will publish usability” plan is research. Submit. Do not self-exempt in an email.
- Virginia is one-party consent on the retrieved text `[17]`. That is the floor. Everyone in the bay should still get written notice that wearable mics are live.
- Camera-off is a **mitigation**, not privacy-complete. Audio remains: learner/staff voice, adjacent-bay speech, accidental real-name capture if the device leaves the sim center, transcripts on phone / vendor cloud / “Noa.”
- Even’s “no cloud without consent” is marketing, not a BAA `[4]`.
- FDA CDS guidance 29 Jan 2026: not all CDS is a device; **automation bias rises when action is urgent** `[13]`. Count accepted-wrong cues.

---

## What v1 should measure (pack inference)

- **Primary:** missed critical actions, Arriaga-style `[34]`.
- **Secondary:** time-to-first-correct-action; gaze-away time from a **room** camera (room ≠ wearable).
- **Safety:** unnecessary interruptions + accepted-wrong cues (automation bias `[13]`).
- **Arms:** Halo cam-off vs G2 (if speakers exist) vs phone-only.

---

## Five questions that change the protocol

Researcher asked Sergio to answer these before anyone writes firmware or an IRB:

1. How is Halo’s camera actually hard-off — custom firmware, disconnected flex, physical cover, or software mute?
2. Does G2 have speakers?
3. Is v1 audio-first, HUD-first, or both? (Sanderson says audio may beat HUD-alone.)
4. First VCU cycle: curriculum QI, or publishable research?
5. Audio retention default — ephemeral on-device, transcript store, or vendor cloud?

Also still open: Halo runtime on 300 mAh; QI vs research subjects (learners / faculty / SP); OpenEvidence / UpToDate license; edge-brain location; standardized cue library vs free-form LLM (literature supports checklists, not unconstrained generation); whether the deck pricing ($299 Halo) and “camera-free Halo” claims are current.

**Do not start firmware until (1) is a written decision.**

What would close the pack later: vendor note on G2 audio-out; Brilliant note that the camera pipeline can be compiled out; VCU HRPP determination (exempt / QI / convened); one methods paragraph on the primary endpoint.

---

## Product lock (do not drift)

- Name: Cognitive Companion (repo: `senrealinvestment/cognitive-companion`)
- Form: glasses mics + HUD → phone/iPad edge brain → optional OpenEvidence / UpToDate
- Pilot hardware: Brilliant Labs Halo, camera hard-off
- Alternative glasses: Even G2 (camera-free by design)
- Control: phone/iPad only
- Setting: critical-care **sim**, not live patients in v1
- Team in committed docs: Navarrete / Kazior / Beltoja
- VCU ask: $12.5k preferred / $7.5k minimum

---

## Sources (key only)

Full ledger: `citations.md`.

- `[1]` https://brilliant.xyz/products/halo
- `[3]` https://docs.brilliant.xyz/halo/hardware
- `[4]` https://www.evenrealities.com/smart-glasses
- `[6]` https://www.evenrealities.com/products/g2-a
- `[7]` https://mentra.glass
- `[8]` 45 CFR 46.104 — https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104
- `[9]` 45 CFR 160.103 — https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103
- `[13]` FDA CDS guidance (29 Jan 2026) — https://www.fda.gov/media/109618/download
- `[15]` https://research.vcu.edu/integrity-and-compliance/hrpp-irb
- `[16]` https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review
- `[17]` Va. Code § 19.2-62 — https://law.lis.virginia.gov/vacode/title19.2/chapter6/section19.2-62
- `[18]` Sanderson 2008 — https://europepmc.org/article/MED/18499611
- `[20]` Liu 2010 — https://europepmc.org/article/MED/20357147
- `[34]` Arriaga 2013 — https://europepmc.org/article/MED/23323901
- `[35]` Elrose 2021 — https://europepmc.org/article/MED/33973863
- `[38]` Croskerry 2003 — https://europepmc.org/article/MED/12514691
- `[45]` Corazza 2023 — https://europepmc.org/article/MED/37535352
