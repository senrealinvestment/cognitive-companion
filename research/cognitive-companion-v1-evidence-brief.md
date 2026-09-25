# Cognitive Companion v1 — cited evidence brief

**Scope (Link):** camera-free HUD + audio/bone-conduction cueing in anesthesia/critical-care sim, versus wearable video; live Halo vs Even G2 capability/availability; implications for Cognitive Companion v1 only. Cites-only. No code.

**v1 frame used here:** Cognitive Companion’s published one-pager is audio-in → phone brain → HUD + tone, with no wearable camera. This brief does not re-litigate that product choice; it tests it against live literature and live hardware pages.

**Date of retrieval:** 2026-08-17.

---

## Bottom line

1. In anesthesia sim, **advanced auditory displays beat a HUD** for event detection when the anesthesiologist is distracted; adding a HUD on top of audio does not add much.[1]
2. A **HUD still changes gaze** toward the patient and can speed event detection when the wearer is physically busy.[2][3][5]
It can also raise alarm notice for a supervising anesthesiologist, with a documented distraction cost during demanding procedures.[4]
3. **Wearable-video / see-what-I-see Glass** is a different product: mostly recording and remote consult. It did **not** shorten time-to-first-shock or no-flow in the two pediatric-arrest sims retrieved here; it did cut some dose/technique errors.[6][7][8]
4. **Even G2** is the live camera-free HUD (36 g, four mics, $599, customize / HSA-FSA language). Official pages do **not** specify speakers or bone conduction.[20][21]
5. **Brilliant Halo** is the live bone-conduction pair (just over 40 g, $399) **and it has a 640×480 camera**. Brilliant’s hardware page says the devices are **not verified** for uses where performance would be critical to human health or safety.[18][19]
6. **Patent corpus not retrieved.** Google Patents / Lens HTML returns were empty. Even’s G2 page claims a “patented screwless hinge” with no patent number.[20]

---

## 1. Camera-free HUD + audio cueing (anesthesia / critical-care sim)

### 1.1 Auditory displays vs HUD vs standard visual monitor

Sanderson et al. (2008), full-scale anesthesia simulator, 16 residents/attendings, reading distractor: event detection was Audio mean 90% / median 100%, Both (Audio+HMD) mean 92% / median 100%, HMD-only mean 75% / median 67% (ns vs visual), Visual mean 52% / median 50%. Detection *time* did not differ. Authors’ conclusion: advanced auditory displays help the distracted anesthesiologist; an HMD does not significantly improve performance.[1]

That is the single strongest v1-relevant RCT-style sim result retrieved: **tone/sonification is the load-bearing channel when attention is off the monitor**. A HUD is a weaker add-on in that specific distracted-supervisor design.[unverified]

### 1.2 HUD when the wearer is busy, not reading

Liu, Jenkins, Sanderson et al. (2009), two simulator experiments: wearing an HMD did not reduce event detection in naturalistic OR scenarios; when physically constrained on a part-task trainer, participants detected two of four events faster with the HMD and one event more slowly.[2]

Liu’s 2009 review of the same program: anesthesiologists detect patient events faster with an HMD when busy performing procedures, but not during normal monitoring. No evidence in that program of inattentional-blindness cost from the HMD.[5]

Liu et al. (2010), clinical OR evaluation (6 attendings, 36 rigid-cystoscopy cases, Microvision Nomad ND2000 + Philips MP70): with the HMD, time looking at the workstation fell 25.3% → 21.0% (P = 0.003) and time looking at the patient/field rose 51.5% → 55.9% (P = 0.014). Frequency and duration of looks did not change. Authors: more research needed before claiming outcome benefit.[3]

Schlosser et al. (2019), proof-of-concept multiple-OR supervision (8 supervising anesthesiologists, 3 h with / 3 h without a head-worn display): alarm notice 66.7% with the display vs 7.1% without (P = 0.028). Authors also report a tendency of the display to distract during demanding procedures.[4]

A 1995 preliminary OR evaluation of a monochrome headband HUD (11 anesthesiologists, one day) is historical only: most users adapted in about 15 minutes; complaints were cable length, resolution, and unfamiliar layout.[16]

Elrose / Sanderson systematic review (2021, 15 studies, 1995–2020): all 7 studies that measured gaze found gaze-direction changes with head-worn displays; 2 of 3 change-detection studies found improvements; in 7 of 10 ease-of-use studies most participants called the device easy to use; participants who were asked said they would consider clinical use but often wanted hardware/display changes.[24]

Andrade et al. (2021) review of wearable clinician monitors (20 studies): three device classes — tactile, head-mounted, smartwatch. HMDs judged potentially useful mainly on ergonomics (less gaze aversion from the patient). Tactile displays showed monitoring potential but comfort blocked clinical use.[11]

**Inference (labeled):** v1’s HUD is justified as a *busy-hands / eyes-on-patient* aid, not as the primary detection channel. v1’s tone channel is the one with the cleaner sim signal.[unverified]

### 1.3 Cognitive aids (paper / digital) — adjacent, not HUD

Marshall (2006), simulated malignant hyperthermia: cognitive-aid use correlated with MH treatment score (CA-1 Spearman r = 0.59; CA-2 r = 0.68); the best teams used the aid extensively.[12]

Marshall (2013) review: 22 aids, 23 studies; 10 sim studies suggested better technical performance in MH, CPR, and airway; 3 sim evaluations showed no improvement or slower/wrong diagnoses; teamwork findings conflicted, including reduced communication in some teams.[13]

Schild et al. (2019): German digital intraoperative cognitive-aid design process (three prototypes).[14]

Goldhaber-Fiebert et al. (2016): Stanford implemented emergency manuals in ORs in fall 2012 (physical copies plus training); authors call this a nascent field in health care.[15]

Arriaga et al. (2013) exists on PubMed as “A simulation-based trial of surgical-crisis checklists.” The PubMed abstract field was empty and the NEJM full text was Cloudflare-blocked in this session, so **no effect sizes from that trial are cited here**.[17]

**Inference:** crisis-checklist evidence supports a *content* layer (what the companion says). It does not by itself justify glasses.[unverified]

---

## 2. Wearable video is the wrong analog for v1

Siebert et al. (2017), RCT, 20 pediatric residents, simulated pulseless VT, AR glasses vs PALS pocket cards: time to first defibrillation (mean 146 s) and other time-to-critical-action endpoints were **not** improved. Wrong defibrillation doses fell: without AR glasses 65% (26/40) wrong doses including 21 shocks >100 J; AR glasses reduced those errors 53% (21/40, P < .001) and cumulative dose 37%.[6]

Drummond et al. (2017), RCT, 42 first-year pediatric residents, Google Glass live video to a remote intensivist in simulated pediatric arrest: **no-blow and no-flow fractions were similar** vs usual care; insufflation effectiveness and compression technique/rate improved.[7]

Wei et al. (2018), systematic review of Google Glass in surgical settings (31 studies): 68% (21/31) used Glass as videography/photography; 19% (6/31) as a vital-sign monitor; 16% as navigation; 16% as intraoperative videoconference. Main limits: short battery 26% (8/31), hands-free difficulty 16% (5/31). Most were pilots; only 2/31 were RCTs.[8]

Zhang et al. (2022), interviews with 13 EMS providers: they frame smart glasses as hands-free + **see-what-I-see remote consultation**. Preferred input: voice and gestures, not the touchpad. Barriers named: hardware, human factors, reliability, workflow, interoperability, and **privacy**.[10]

Dougherty & Badawy (2017) reviewed Glass in nonsurgical settings: 51 included studies (21 patient-centered, 30 clinician-centered). That is a camera-first literature, not a camera-free HUD literature.[9]

**Inference:** do not treat Glass/AR-video papers as evidence for Cognitive Companion v1. They test a different job (record / telementor). Where they overlap (on-display cognitive aid), they improve **dose accuracy**, not speed.[unverified]

---

## 3. Live Halo vs Even G2 (retrieved 2026-08-17)

|  | **Even G2** | **Brilliant Halo** |
|---|---|---|
| Official posture | Camera-free by design; mic is the input.[20] | Open-source glasses **with a 640×480 camera** plus stereo bone conduction.[18][19] |
| Weight | 36 g.[20] | “just over than 40g” (vendor wording).[18] |
| Display | Green Micro LED, 640×350, 27.5° FoV, 1200 nits peak, 60 Hz, binocular waveguides, 98% passthrough.[20] | 0.2″ OLEDoS; 640×480 RGB panel; 256×256 drawable area; up to 5000 nit peak.[19] |
| Audio out | **Not specified** on the official spec / FAQ pages retrieved.[20] | Stereo bone-conduction speakers.[18][19] |
| Audio in | Four microphones; Conversate AI cues / transcribe / translate.[20] | Dual T5838 MEMS mics.[18][19] |
| Battery | Up to 2 days typical use; charging case holds seven full charges.[20] | 300 mAh (2×150 mAh); product FAQ claims all-day life at estimated normal use.[18][19] |
| Durability | IP65; drop-tested 2 m; hinge cycled 40,000 times.[20][22] | No IP rating on the hardware page retrieved.[19] |
| Price / buy | G2-A listed **$599**; customize / prescription paths; HSA/FSA language on the glasses page.[20][21] | **$399.00**.[18] |
| Ship status (this fetch) | Consumer product pages present it as buyable now.[20][21] | Same page: “shipments beginning in early August” and “Halo will begin shipping soon.”[18] |
| Safety / intended use | Consumer AI glasses; no medical-device claim on pages retrieved.[20] | Consumer/R&D; **not verified** where performance would be critical to human health, safety, or mission-critical use.[19] |
| Dev surface | Even Hub / SDK; MentraOS lists Even Realities as a supported hardware target.[20][23] | Zephyr OS + Lua VM; firmware described as fully open / GitHub on the product FAQ.[18][19] |

G2 FAQ, verbatim job-to-be-done: it has no camera “to prioritize your privacy” and “relies on its integrated microphone for information input rather than a camera.”[20]

Halo hardware page lists the VGA camera among core specs and, in the same document, states the devices are intended for consumer and R&D use and are not verified where performance would be critical to human health or safety.[19]

**Conflicts / gaps**

- Halo ship wording disagrees with itself on the same product page (“beginning early August” vs “will begin shipping soon”).[18]
- G2 speaker / bone-conduction capability is **unknown from official pages**. Repo language that G2 has “no speakers” was **not confirmed** here.[unverified]
- Neither device is a cleared medical monitor. Halo says so explicitly.[19]
- Mentra Live is the camera-on adjacent platform (43 g, HD camera, speakers, 3 mics) and claims MentraOS already supports Even Realities hardware — relevant as a software path, not as a v1 camera-free device.[23]

---

## 4. Similar projects (not v1, listed so they are not rediscovered as “new”)

| Cluster | What it actually is | Why it is not v1 |
|---|---|---|
| Sanderson / Liu HMD program (2008–2010, reviewed 2021) | Vital-sign HUD + sonification in anesthesia sim and one clinical series.[1][2][3] | Closest analog. Research program, not a shippable companion.[5][24] |
| Google Glass / AR-glasses PALS (Siebert, Drummond, Wei) | Camera + remote video or AR checklist overlay.[6][7][8] | Video-first; fails v1’s camera-free constraint. |
| EMS smart glasses (Zhang 2022) | See-what-I-see teleconsult + documentation.[10] | Camera + privacy surface. |
| Stanford emergency manuals / digital CAs (Marshall, Schild, Goldhaber-Fiebert) | Paper or tablet cognitive aids.[12][13][14] | Content layer only.[15] |
| Mentra Live | Camera-enabled open-source field glasses; MentraOS lists Even as a target.[23] | Camera-on; useful as an OS option if G2 is the HUD. |
| Even Conversate | On-device consumer AI cues from the mic, no camera.[20] | Consumer cousin of v1 audio-in → cue. Not clinical. |

---

## 5. Patents

**Unknown / blocked.** Targeted Google Patents and Lens.org HTML fetches in this session returned empty or near-empty bodies. No patent numbers are cited.

Even’s G2 page uses the phrase “Patented screwless hinge”; the tech page says screwless hinges were opened and closed 40,000 times. That is vendor copy, not a patent document.[20][22]

Do not treat “patented hinge” as freedom-to-operate, and do not treat the empty search as “no patents exist.”[unverified]

---

## 6. Implications for Cognitive Companion v1 only

These are inferences from the cites above, not new facts.

1. **Keep audio-in + tone as the detection channel.** Sanderson is the cleanest sim result retrieved, and it favors sonification over HUD when the wearer is distracted.[1]
2. **Keep a HUD as a busy-hands glance surface**, not as the pager. Liu/Schlosser support gaze-on-patient and alarm notice; Schlosser also documents distraction during hard procedures — so v1 HUD content should stay sparse.[2][3][4]
3. **G2 is the default v1 HUD hardware** among the two live devices: camera-free, lighter, IP65, buyable, four mics, on-device speech features. Confirm audio-out (or accept phone/Halo-only tones) before promising bone-conduction on G2.[20][21]
4. **Do not put Halo on a patient’s or clinician’s face as a camera.** Halo ships a VGA camera, and Brilliant says the devices are not verified where performance would be critical to human health or safety — a hard v1 reject for any in-sim “wearable video” path.[18][19]
5. **Halo is only a v1 audio-out fallback** if bone conduction is required and G2 cannot do it. That is a speaker accessory, not the companion’s eyes.[18][19]
6. **Do not cite Glass RCTs as v1 efficacy.** They are video/telementor trials. The transferable scrap is Siebert’s dose-error reduction from an on-display aid — which argues for checklist content, not a camera.[6][7]
7. **Ship the cognitive-aid content even if glasses slip.** Marshall / emergency-manual evidence does not need a HUD.[12][13][15]
8. **Privacy is already a named barrier** in the camera-on EMS literature. v1’s camera-free constraint is the feature that keeps that literature from applying.[10][20]
9. **No medical-device claim.** Neither Halo nor G2 is presented as a physiologic monitor. Liu 2010 is a display-of-existing-monitor study, not a new sensor.[3][19]
10. **Patent clearance is still open work.** This brief does not clear FTO.[22]

---

## What this brief does not contain

- Full text of Arriaga NEJM 2013 (Cloudflare). Title only.[17]
- Any issued-patent table (fetch failed).
- Hardware teardown or independent lab measurements — vendor pages only for Halo/G2.
- Implementation, APIs, or firmware. Link routes code after this lands.

## Sources

[1] https://pubmed.ncbi.nlm.nih.gov/18499611
    > "Participants detected significantly more events with Audio (mean = 90%, median = 100%, P < 0.02) and Both (mean = 92%, median = 100%, P < 0.05) but not with HMD (mean = 75%, median = 67%, ns) compared with the Visual condition (mean = 52%, median = 50%)."
    > "Advanced auditory displays help the distracted anesthesiologist maintain peripheral awareness of a simulated patient's status, whereas a HMD does not significantly improve performance."
[2] https://pubmed.ncbi.nlm.nih.gov/19762741
    > "Experiment 1 showed that neither wearing the HMD nor adjusting the focus setting reduced participants' ability to detect events (the number of events detected and time to detect events)."
    > "In general, participants spent more time looking toward the patient and less time toward the anesthesia machine when they wore the HMD than when they used standard monitoring alone."
[3] https://pubmed.ncbi.nlm.nih.gov/20357147
    > "When participants were using the HMD, compared with standard monitoring, they spent less time looking toward the anesthesia workstation (21.0% vs 25.3%, P = 0.003) and more time looking toward the patient and surgical field (55.9% vs 51.5%, P = 0.014)."
[4] https://pubmed.ncbi.nlm.nih.gov/30721389
    > "However, the anesthesiologists noticed significantly more patient alarms with the head-worn display (66.7%) than without (7.1%), P = 0.028, and they reported improved situation awareness with the head-worn display."
    > "A negative effect of the head-worn display was its tendency to distract during demanding procedures."
[5] https://pubmed.ncbi.nlm.nih.gov/19770643
    > "Anesthesiologists can detect patient events faster with an HMD when they are busy performing procedures, but not during normal monitoring."
[6] https://pubmed.ncbi.nlm.nih.gov/28554878
    > "Time to first defibrillation attempt (mean: 146 s) and adherence to AHA guidelines in terms of time to other critical resuscitation endpoints and drug dose delivery were not improved using AR glasses."
    > "These errors were reduced by 53% (21/40, P<.001) and cumulative defibrillation dose by 37% (5.14/14, P=.001) with AR glasses."
[7] https://pubmed.ncbi.nlm.nih.gov/28165347
    > "Real-time video communication between the first responder and a remote intensivist through Google Glass did not decrease no-blow and no-flow fractions during the first 5 minutes of a simulated pediatric cardiopulmonary arrest but improved the quality of the insufflations and chest compressions provided."
[8] https://pubmed.ncbi.nlm.nih.gov/29510969
    > "Google Glass was utilized as a videography and photography device (21/31, 68%), a vital sign monitor (6/31, 19%), a surgical navigation display (5/31, 16%), and as a videoconferencing tool to communicate with remote surgeons intraoperatively (5/31, 16%)."
    > "The main reported limitations of using Google Glass utilization were short battery life (8/31, 26%) and difficulty with hands-free features (5/31, 16%)."
[9] https://pubmed.ncbi.nlm.nih.gov/29051136
    > "Of the 852 records examined, 51 met all predefined criteria, including patient-centered (n=21) and clinician-centered studies (n=30)."
[10] https://pubmed.ncbi.nlm.nih.gov/35225816
    > "Smart glasses have been gaining momentum as a novel technology because of their advantages in enabling hands-free operation and see-what-I-see remote consultation."
    > "They are related to hardware limitations, human factors, reliability, workflow, interoperability, and privacy."
[11] https://pubmed.ncbi.nlm.nih.gov/34032574
    > "The studies of head-mounted displays (HMDs) revealed that these devices could be useful in critical care medicine, particularly from an ergonomics point of view."
[12] https://pubmed.ncbi.nlm.nih.gov/16931660
    > "We were able to show a strong correlation between the use of a cognitive aid and the correct treatment of MH."
[13] https://pubmed.ncbi.nlm.nih.gov/24029855
    > "Ten studies using simulation suggested that technical performance improves with the use of cognitive aids in some anesthetic emergencies such as malignant hyperthermia, cardiopulmonary resuscitation, and airway management."
    > "However, in 3 of the simulator-based evaluations, participants had either no improvement or took longer to diagnose and treat and made more incorrect diagnoses."
[14] https://pubmed.ncbi.nlm.nih.gov/31033445
    > "Stressful situations during intraoperative emergencies have negative impact on human cognitive functions."
[15] https://pubmed.ncbi.nlm.nih.gov/27541721
    > "Emergency manuals (EMs), context-relevant sets of cognitive aids or crisis checklists, have been used in high-hazard industries for decades, although this is a nascent field in health care."
[16] https://pubmed.ncbi.nlm.nih.gov/7782663
    > "This monitor is mounted on a headband worn by the anesthesiologist. It projects a monochrome image of monitor data directly into one eye."
[17] https://pubmed.ncbi.nlm.nih.gov/23574136
    > "A simulation-based trial of surgical-crisis checklists"
[18] https://brilliant.xyz/products/halo
    > "The first Halo units are rolling off the production line now, with shipments beginning in early August."
    > "The device weighs just over than 40g and, at estimated normal use, can achieve all-day battery life. The device contains a color display, low-power optical sensor for AI inference, dual mics with audio activity detection, a low-power AI processor, and dual bone conduction speakers."
    > "Halo will begin shipping soon"
    > "Sale price  $399.00 USD  Regular price"
[19] https://docs.brilliant.xyz/halo/hardware
    > "640x480 global shutter color camera"
    > "Stereo bone conduction speakers"
    > "It is not verified for use where performance and accuracy would be critical to human health, safety or mission critical use."
    > "150mAh each, 300mAh total"
[20] https://www.evenrealities.com/smart-glasses
    > "Just 36 grams."
    > "Camera-free. By design."
    > "To prioritize your privacy and deliver a seamless display experience, Even G2 relies on its integrated microphone for information input rather than a camera."
    > "The built-in lithium battery of Even G2 lasts up to 2 days on a single charge, depending on usage."
    > "Patented screwless hinge"
    > "the charging case holds enough power for seven full charges."
[21] https://www.evenrealities.com/products/g2-a
    > "Personalize your Even G2 smart glasses."
[22] https://www.evenrealities.com/tech
    > "Screwless hinges opened and closed 40,000 times."
    > "Drop-tested from 2 metres."
    > "Dust proof. Certified IP65."
[23] https://mentra.glass
    > "MentraOS is an open-source operating system for smart glasses. It's the only smart glasses OS with a full SDK, app store, and support for multiple hardware platforms including Mentra Live, Even Realities, and Vuzix."
    > "Mentra Live gives enterprise teams and developers camera-enabled smart glasses for remote support, field operations, and AI workflows."
    > "Speakers, a microphone, and an HD camera on every worker's head"
[24] https://pubmed.ncbi.nlm.nih.gov/33973863
    > "In 100% (7/7) of the studies that evaluated gaze behavior, changes were found in gaze direction with HWDs."
    > "Change detection improvements were found in 67% (2/3) of the studies evaluating changes in the participants' ability to detect changes in vital signs."
