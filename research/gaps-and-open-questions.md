# Gaps and open questions for Sergio

2026-08-18. Things this pack cannot honestly close.

## Hardware

1. **How is Halo’s camera actually hard-off?** Docs describe the PixArt sensor and OTA firmware [3]. They do not describe a disable procedure. Is the plan a custom firmware image, a disconnected flex, a physical cover, or a software mute?
2. **Does G2 have speakers?** Re-fetched Even pages still have no audio-out line [4] [5] [6]. If the answer is no, the companion’s voice has to come from the phone.
3. **What is Halo runtime on 300 mAh in a noisy sim bay?** Capacity is stated [3]. Runtime is not.
4. **G2 battery / charge-case numbers** were not extracted this session [unverified].
5. **Can MentraOS run the companion on G2 without Mentra Live’s camera?** Mentra lists Even Realities as supported hardware [7]. App-level capability is untested here.
6. **Price collision.** Live Halo is $399 [1]. Older committed copy used $299–$349. Which number is in the $12.5k / $7.5k ask?

## Evidence

7. **No trial of this product class.** Closest HUD evidence is anesthesia vital-sign HMDs with process/gaze outcomes, not patient outcomes [18] [20] [35].
8. **Audio may beat HUD-alone** in one 2008 sim [18]. Has the team decided whether v1 is audio-first, HUD-first, or both?
9. **Checklist benefit is real in sim** (Arriaga 6% vs 23% missed steps [34]; PediAppRREST fewer deviations [45]). That is the *content*, not the glasses. What is the minimum viable content library for the first VCU session?
10. **Interruptibility metric is undefined.** What will you count as a harmful interruption vs a useful force function [38]?
11. Westbrook-style medication-interruption numbers were **not retrieved** this session [unverified]. Do not put them in the deck.

## Privacy / IRB / FDA

12. **QI or research?** VCU says most QI is not research, and to submit in VIRBs when unclear [16]. Is the first pilot a curriculum QI cycle or a publishable study?
13. **Who is the human subject?** Learners only? Faculty? Confederate SP? [unverified]
14. **Audio retention default?** On-device ephemeral vs transcript store vs vendor cloud. Even claims no cloud without consent [4]. That is marketing.
15. **Halo “Noa” memory** is on the product page [1]. Can it be off for a VCU image?
16. **FDA CDS 2026 guidance** flags time-critical use and automation bias [13]. Is the sim script going to show the *basis* of each cue, or just the cue?
17. HHS OCR wearable-audio pages were **HTTP 403** this session [unverified]. Someone with a browser session should pull them.

## Product / ops (outside researcher scope, still blocking)

18. OpenEvidence / UpToDate: license, offline, what the glasses are allowed to quote [unverified].
19. Edge brain: on-device model vs campus API vs vendor. Not researched here [unverified].
20. Standardized cue library vs free-form LLM. The literature supports checklists [34], not unconstrained generation.
21. Team roles (Navarrete / Kazior / Beltoja) and who owns IRB vs hardware vs sim-center access. Named in committed docs; not re-verified this session [unverified].
22. Deck (`Cognitive-Companion-Presentation.pptx`) exists. This pack does not audit whether the deck pricing ($299 Halo) and “camera-free Halo” claims are current [unverified].

## Recommended next actions (not implementation)

- Sergio: answer 1, 2, 8, 12, 14. Those five change the protocol [unverified].
- Link / Coder: do not start firmware work until (1) is a written decision [unverified].
- Counsel / HRPP: 10-minute VIRBs determination request using the privacy note [15] [16].
- Researcher: stop. Pack is on disk. No PR.

## What would close the pack later

- A vendor email or photo of G2 audio-out [unverified].
- A Brilliant firmware note that the camera pipeline can be compiled out [unverified].
- VCU HRPP determination letter (exempt / QI / convened) [unverified].
- One methods paragraph: primary endpoint (process adherence vs time-to-cue vs NASA-TLX) [unverified].

## Sources

[1] https://brilliant.xyz/products/halo — Brilliant Labs Halo product page
    > "Regular price $399.00 USD"
    > "The device weighs just over than 40g"
    > "dual mics with audio activity detection, a low-power AI processor, and dual bone conduction speakers"
    > "shipments beginning in early August"
[3] https://docs.brilliant.xyz/halo/hardware — Brilliant Labs Halo hardware docs
    > "640x480 global shutter color camera"
    > "256x256px drawable area"
    > "Stereo bone conduction speakers"
    > "300mAh built-in rechargeable li-ion battery"
    > "It is not verified for use where performance and accuracy would be critical to human health, safety or mission critical use."
    > "The firmware is fully updatable over the air (OTA)"
    > "The front facing camera on Halo is the PAG7982J1 from PixArt Imaging"
    > "Stereo microphones Stereo bone conduction speakers"
[4] https://www.evenrealities.com/smart-glasses — Even Realities G2 smart glasses
    > "Camera-free. By design."
    > "Just 36 grams."
    > "Even G2 relies on its integrated microphone for information input rather than a camera."
    > "Conversate captures and transcribes every word"
    > "No data is stored in the cloud without your explicit consent."
    > "Capabilities Four Microphones Auto brightness control"
    > "Even G2 resists to dust and water at IP65 rating"
    > "Resolution 640*350 FoV 27.5"
[5] https://www.evenrealities.com/tech — Even Realities G2 tech page
    > "Screwless hinges opened and closed 40,000 times."
    > "Drop-tested from 2 metres."
    > "Dust proof. Certified IP65."
[6] https://www.evenrealities.com/products/g2-a — Even Realities G2-A product
    > "Select frame shape and color$599 Even G2 A"
[7] https://mentra.glass — Mentra OS / Mentra Live
    > "support for multiple hardware platforms including Mentra Live, Even Realities, and Vuzix"
    > "Mentra Live gives enterprise teams and developers camera-enabled smart glasses"
    > "Frame Dimensions 162 L X 148 W x 47 H Weight 43g"
[13] https://www.fda.gov/media/109618/download — FDA CDS Software guidance PDF 2026-01-29
    > "Document issued on January 29, 2026."
    > "Not all clinical decision support software used in healthcare settings are devices and therefore subject to FDA oversight as a device."
    > "time-critical nature of the HCP"
    > "Automation bias is the propensity of humans to over-rely on a suggestion from an automated system."
    > "In situations that require urgent action, automation bias increases"
[15] https://research.vcu.edu/integrity-and-compliance/hrpp-irb — VCU HRPP/IRB home
    > "New IRB review system: VIRBs (VCU IRB system)"
[16] https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review — VCU activities requiring IRB review
    > "Most quality improvement efforts do not meet the definition of research because they are not designed to be generalizable."
    > "Research is a systematic investigation designed to develop or contribute to generalizable knowledge."
    > "If a determination cannot clearly be made, submit the project to the VCU IRB using VIRBs"
[18] https://europepmc.org/article/MED/18499611 — Europe PMC 18499611
    > "Participants detected significantly more events with Audio (mean = 90%, median = 100%, P < 0.02) and Both (mean = 92%, median = 100%, P < 0.05) but not with HMD (mean = 75%, median = 67%, ns) compared with the Visual condition (mean = 52%, median = 50%)."
    > "Advanced auditory displays help the distracted anesthesiologist maintain peripheral awareness of a simulated patient's status, whereas a HMD does not significantly improve performance."
[20] https://europepmc.org/article/MED/20357147 — Europe PMC 20357147
    > "When participants were using the HMD, compared with standard monitoring, they spent less time looking toward the anesthesia workstation (21.0% vs 25.3%, P = 0.003) and more time looking toward the patient and surgical field (55.9% vs 51.5%, P = 0.014)."
[34] https://europepmc.org/article/MED/23323901 — Europe PMC 23323901
    > "Failure to adhere to lifesaving processes of care was less common during simulations when checklists were available (6% of steps missed when checklists were available vs. 23% when they were unavailable, P<0.001)."
    > "Every team performed better when the crisis checklists were available than when they were not."
[35] https://europepmc.org/article/MED/33973863 — Europe PMC 33973863
    > "Of the 7 studies conducted in clinical contexts, none reported any clinical outcomes."
    > "Although there is limited and sometimes conflicting evidence about the benefits of HWDs from certain surrogate and process outcomes, evidence for clinical outcomes is lacking."
[38] https://europepmc.org/article/MED/12514691 — Europe PMC 12514691
    > "Through the process of metacognition, clinicians can develop cognitive forcing strategies to abort such latent errors."
[45] https://europepmc.org/article/MED/37535352 — Europe PMC 37535352
    > "The number of deviations from guidelines was significantly lower in the PediAppRREST group than in the control groups"
