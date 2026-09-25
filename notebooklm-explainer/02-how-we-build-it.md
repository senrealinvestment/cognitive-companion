# Cognitive Companion — how we will build it

A 12-month implementation plan for department leadership. Simulation first. Camera-free. Phone-only is a real arm.

## What “build” means in year one

Year one is not a commercial launch and not a live-unit deployment. Year one is a working camera-free prototype in the simulation lab, a small scenario pack drawn from critical-care crises, process measurements against a phone-only control, and a write-up clean enough to take to the next internal or society dollar.

If we cannot show that in twelve months, we should stop, not scale.

## The engineering shape

Glasses do not think. The phone or iPad thinks.

Ambient audio hits a gate so we are not cueing on every word in the room. A local protocol pack — structured checklist cards, not a general chatbot — proposes a short cue. A safety gate blocks reckless language (no “you must,” no drug-dose invention, no mid-code model updates). The glasses show eight words or fewer and, when audio is available, a short earcon or phrase. After the case, the user grades the cue. The grade does not retrain anything while a scenario is running.

Broader evidence lookup is opt-in and de-identified. It is not the hot path.

This split is how we keep version 1 out of “the glasses are diagnosing the patient.”

## Hardware, in the order we will actually buy it

We will not pick a winner on a slide.

1. **Phone or iPad only.** Mic, headphones, on-screen stand-in for the HUD. This is the control arm and the fallback if glasses procurement stalls. It is also the fastest path to content testing.
2. **Halo with camera hard-off.** Open software stack, bone conduction onboard, list price about $399. Allowed in clinical-mode testing only if disable of the camera is written down as a hard off, not a software mute. Halo documentation already says the device is not verified for health-critical use. We treat that as a constraint, not a footnote to ignore.
3. **Even G2.** Factory camera-free, about $599, HUD and microphones. Audio-out is the open question; we will not pretend speakers are confirmed. Phone or earbuds cover the ear.

Quantities in year one are small: a handful of glasses, a dedicated tablet or two, cases and mounts. Hardware is not where the $155,000 program lives. People and engineering time are.

## Content before spectacle

The first scenario pack will be a short list of crises we already teach, not a fantasy of every ICU emergency. Candidates include anaphylaxis, malignant hyperthermia, hemorrhage, airway cannot-intubate-cannot-oxygenate, and a shock/decompensation case. The exact first pack is still an open product decision and will be locked with simulation faculty before we write cues.

Each card is a cognitive-forcing prompt in the Croskerry sense: a short interrupt that makes a latent miss harder to ignore. It is not a lecture. It is not a differential-diagnosis essay on the lens.

We will use local protocol language first. Literature APIs later, on demand.

## Twelve months, four quarters

**Quarter 1 — stand it up.** Buy the phone/tablet control kit. Confirm Halo camera-off in writing or do not use Halo in the sim room. Confirm G2 audio path. Stand up the edge app far enough to deliver a canned cue from a protocol card. No model theater.

**Quarter 2 — content and safety.** Write the first scenario pack with simulation faculty. Implement the safety gate. Dry-run with the clinical collaborators until cues are short enough to be usable under load. Decide whether OpenEvidence or UpToDate is wired at all in year one.

**Quarter 3 — measure in sim.** Run sessions. Primary process measure: missed critical actions. Secondary: time to first correct action. Safety: unnecessary interruptions and accepted-wrong cues. Phone-only versus glasses. Room cameras, if used for scoring, are room cameras — not wearable cameras.

**Quarter 4 — write and springboard.** A methods-and-process report, not a claim of outcome benefit. That packet is what the seed was for: something a dean, a School of Medicine research office, or a society grant can fund without buying a story.

Regulatory posture in year one: simulation and education, possibly QI if VCU HRPP agrees it is not generalizable research. If we want generalizable claims, we go through VIRBs. We will not freelance that distinction. FDA clinical-decision-support guidance from January 2026 is on our reading list because automation bias is a real failure mode; we are not seeking device clearance in year one.

## What we will not do with year-one money

We will not build a camera pipeline “just in case.”
We will not run silent learning at the bedside or in sim while a case is live.
We will not write to the EMR.
We will not hire a vendor to own the protocol content.
We will not spend the bulk of the budget on glasses.
We will not skip the phone-only arm.

## Risks we are naming in advance

Halo camera-off may be unverifiable; then Halo is out and G2 or phone carries the lab.
G2 may have no usable speakers; then audio is phone or earbuds.
Cues may annoy more than they help; that is a result, and we will count interruptions.
Automation bias may make a wrong cue worse than no cue; that is why accepted-wrong is a safety endpoint.
Engineering time is the scarce resource. That is why the College of Engineering partnership is in the plan rather than “we will figure out the app later.”

## What done looks like

At month 12, a chair should be able to watch a simulation in which a resident runs a crisis with camera-free cues, see the phone-only comparison, and read a short process report. That is the artifact that unlocks the rest of the money. That is also the off-ramp if the packaging adds nothing.
