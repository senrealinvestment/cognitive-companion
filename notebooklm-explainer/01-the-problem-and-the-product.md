# Cognitive Companion — the problem and the product

A briefing document for department leadership. Simulation and education first. Not a live-patient device. Not a diagnostic model.

## The problem we already know

Critical-care crises are rare, fast, and cognitively expensive. Even excellent clinicians miss steps when memory, hands, and eyes are all occupied. High-fidelity simulation is how we train that moment. The content problem is not mysterious: crisis checklists and cognitive aids improve process adherence.

A 2013 high-fidelity simulation trial (Arriaga and colleagues, New England Journal of Medicine) found that teams using crisis checklists missed 6 percent of lifesaving steps versus 23 percent without the checklist. A 2023 tablet cognitive-aid study in pediatric resuscitation (PediAppRREST) cut guideline deviations compared with a paper card or no aid. Those results support **content**. They do not prove that putting the same content on glasses will save lives.

Paper and tablet aids still compete with the work. Someone has to look down, tap, or hold a card. In a real code or a dense simulation, that look-down is the tax. Head-worn displays have been studied in anesthesia as a way to keep vital signs in view. A 2021 systematic review of head-worn vital-sign displays found **no clinical outcome benefit** in the clinical-context studies it included. Some anesthesia HMD work improved event detection or reduced gaze-away from the field; some did not. That literature is analog, not this product.

So the honest problem statement is narrower than “AI will fix critical care.” It is this: we already have checklist-grade content that works in simulation. We do not yet have a camera-free, hands-free way to deliver that content without pulling the clinician’s eyes and hands off the patient or the manikin.

## What Cognitive Companion is

Cognitive Companion is a camera-free ambient aid for critical-care **simulation**.

In one sentence: glasses listen with microphones, never with a camera, and show a short heads-up cue; a phone or iPad next to the room decides the whisper from local protocols; the clinician remains the decision-maker.

It is a **packaging** test of known-good cognitive-aid content. It is not a new diagnosis engine. It is not watching faces. It is not writing to the medical record. It is not learning online at the bedside.

Version 1 lives in the simulation lab, not in a live ICU of any kind.

## Three layers, on purpose

The system has three layers. Mixing them up is how this idea turns into a surveillance product or a vaporware model.

**Layer 1 — glasses.** Lightweight smart glasses. Ambient microphones. A tiny HUD, on the order of a few words, not a page of text. Optional short audio cue. No wearable camera in the product definition.

**Layer 2 — edge.** An iPhone or iPad in the room. This is the brain for version 1. It gates noisy speech, matches a local protocol card, applies a safety check, and sends a short cue. After the case, the clinician can grade the cue. Improvement happens offline, never mid-crisis.

**Layer 3 — cloud, optional.** Broader evidence (OpenEvidence or UpToDate-class) only on demand or after an explicit trigger. Questions are stripped of identifiers. Ambient speech does not wait on a literature API.

Wrong designs we are not building: a face-worn video stack; every utterance waiting on the cloud; silent chart writes; a model that “takes over” the code.

## Camera-free is the product, not a slogan

A manikin is not a patient. A standardized patient’s voice can still identify a person. Faculty and residents in a sim lab did not consent to a wearable camera. Virginia is a one-party-consent state for intercepting communications, which is not the same thing as an IRB-ready recording protocol.

Camera-free is the privacy posture that makes a VCU simulation pilot discussable. Two hardware paths respect that posture:

- Brilliant Labs Halo, listed near $399, open stack, onboard bone-conduction speakers, **onboard camera that must be documented hard-off** — not a software mute next to an over-the-air camera.
- Even Realities G2, factory camera-free, listed near $599, strong HUD, four microphones. Speakers are not a settled spec in our research pack, so audio-out may be phone or bone-conduction earbuds.

A third arm is first-class, not a consolation prize: **phone or iPad only**, same cues, no glasses. If glasses add nothing over the phone, we will say so. That is a successful test, not a failed purchase.

Halo’s own hardware documentation states the device is not verified for use where performance and accuracy would be critical to human health. We will not claim otherwise.

## What we will measure, and what we will not claim

Primary process endpoint, inferred from the checklist literature: missed critical actions in simulation, Arriaga-style. Secondary: time to first correct action. Safety: unnecessary interruptions, and accepted-wrong cues — automation bias, which FDA clinical-decision-support guidance flags as worse when action is urgent.

We will not claim mortality benefit. We will not claim this is an FDA device. We will not claim the glasses themselves are the evidence. The evidence we can borrow is about checklists and cognitive aids. The evidence we must generate is whether HUD plus short audio packaging improves process adherence versus phone-only, using that same content.

## Why this department

This work sits in anesthesiology and critical-care simulation because that is where crisis checklists, airway, hemorrhage, and decompensation already live as teaching problems. The target setting is critical care broadly: medical, surgical, transplant, neuro, cardiac, and other intensive care units, where the same crises recur. Version 1 does not touch live patients. It borrows the cognitive structure of that work and tests it where we are allowed to be wrong: in sim.

The product name in conversation is Cognitive Companion. The repository still carries an older working title, Crisis Mirror. Same project.
