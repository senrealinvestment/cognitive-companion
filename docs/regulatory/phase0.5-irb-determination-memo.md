# Phase 0.5 IRB determination memo (advisory)

**Project:** Crisis Mirror — Phase 0.5 Wizard-of-Oz (WoZ) sim  
**Source design:** `docs/architecture/V2-build-plan.md` (Phase 0.5), commit `a3bc50d` on `architect/v2-build-plan`  
**PI (draft):** Dr. Michael Kazior · **Co-I (draft):** Dr. Sergio Navarrete  
**Date:** 2026-09-24 (America/New_York)  
**Status:** Advisory analysis only — **not legal advice**; **final determination belongs to VCU HRPP / the VCU IRB**

---

## 1. What Phase 0.5 actually is (per the build plan)

From V2-build-plan Phase 0.5 (follow the doc if it differs from informal summaries):

- **Goal:** Before hardware purchase or model training, run **3–5 sim sessions** in which a **human hand-sends cues** to a display the team already has, to learn whether cues help, which categories matter, timing, and distraction.
- **Who:** Clinician **operator** (sim faculty or clinician) follows a **scripted cue sheet** (may send allowed free-text under wording rules); separate **observer/timekeeper** (does not send cues); engineer runs cue-sender tooling; Clinical Safety & Eval owns metrics/wording.
- **Measured:** time to key actions; missed-action rate vs checklist; latency trigger→display; acted-on vs ignored; false/unhelpful rate in debrief; **short survey** on distraction/usefulness; debrief notes on timing.
- **Consent:** **Written informed consent** from every sim participant (including operator and faculty), covering **audio/video if any**, storage duration, who can access recordings, and withdrawal. Participants are **staff/volunteers in sim, never patients**. **No real patient data, QI/QA, or VCU institutional systems.** IRB review vs exemption is **open** and must be settled before session 1.
- **Outputs:** seed gold nudges (ICU physician panel–approved), draft cue-category list, explicit go/no-go for Phases 1–4.

**Discrepancy note vs informal study summary:** The build plan does **not** state an intent to publish Phase 0.5 results; it frames product learning and a hardware go/no-go. Audio/video is **conditional** (“if any”), not mandatory. Publication intent, if added later, is a factor that should be disclosed to VCU HRPP (see §4).

---

## 2. Does the Common Rule apply at all?

**45 CFR 46** (the Common Rule, HHS) applies to research involving human subjects that is **conducted or supported by a Common Rule department/agency**, or that an institution elects to cover under its **Federalwide Assurance (FWA)** / institutional policy. Many universities apply Common Rule–aligned procedures to all human research regardless of funding.

- **Confirm with VCU HRPP:** whether this activity is covered by VCU’s FWA / institutional policy even if there is **no federal funding**, and which regulations VCU will apply.

Public VCU pages state that the VCU IRB oversees activities meeting the regulatory definitions of research involving a human subject, and that VCU is engaged when research is conducted by VCU faculty/staff/students in their university capacity (among other engagement criteria).  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review/

---

## 3. Is it “research”? — 45 CFR 46.102(l)

> **Research** means “a systematic investigation, including research development, testing, and evaluation, **designed to develop or contribute to generalizable knowledge**.”  
> https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102

Phase 0.5 is clearly **systematic** (scripted sessions, predefined metrics, survey, debrief). The open question is **design for generalizable knowledge** vs purely local product/process learning.

**OHRP Quality Improvement FAQs** (still useful framing; note FAQ cites older subsection letters):

- Pure QI limited to implementing a practice and collecting data for clinical/practical/administrative purposes is often **not** “research.”  
- **Intent to publish alone does not make** an activity research; conversely, research can exist without publication plans.  
- Projects that also collect information to establish scientific evidence of how well an intervention works **may** be research.  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/quality-improvement-activities/index.html

**Application:** If Phase 0.5 is designed **only** to decide Crisis Mirror’s local go/no-go (and not to produce findings meant to apply beyond this product/team), a **not human subjects research / non-research** argument is possible—but VCU still offers an official determination path. If the team **designs** the work to answer general questions about cue usefulness, distraction, timing categories, etc., for audiences beyond the product team (including later papers), it meets **research**.

**VCU OneTRAC (public):** Research vs QI hinges on design for generalizable knowledge; publishing QI does not automatically convert QI to research.  
https://onetrac.vcu.edu/research-vs-qi/

---

## 4. Are there “human subjects”? — 45 CFR 46.102(e)(1)

> **Human subject** means a living individual about whom an investigator conducting research:  
> (i) obtains information or biospecimens through **intervention or interaction**, and uses/studies/analyzes it; **or**  
> (ii) obtains, uses, studies, analyzes, or generates **identifiable private information** or identifiable biospecimens.  
> https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102

Phase 0.5 involves **interaction** (consent, sim participation, survey, debrief) and, if A/V is kept, **identifiable** face/voice information. Clinician performance in sim can be **private** in the sense that participants may reasonably expect it not to be publicized as an individual evaluation. Manikin-only clinical content is not a living patient subject; **staff/volunteer participants are**.

**OHRP decision charts (2018 Requirements):** Chart 01 (is it human subjects research?) and Chart 02 (exemption eligibility).  
https://www.hhs.gov/ohrp/regulations-and-policy/decision-charts-2018/index.html

---

## 5. Pathway options (most likely → less likely)

### A. Not human subjects research (NHSR) / non-research

**Possible only if** VCU agrees the activity is **not** designed to contribute to generalizable knowledge (e.g., strictly internal product evaluation) **or** otherwise fails the research definition. Build-plan framing (go/no-go, no stated publication) supports raising this question; **do not self-certify if a determination letter is needed**.

At VCU (public): investigators are responsible for deciding whether IRB review is needed, but may submit for an **official determination**; for NHSR, upload **HRP-503b TEMPLATE NHSR** in VIRBs. The IRB will not make NHSR determinations **after** the activity has begun (per HRP-503b notes extracted from the public template).  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review/  
Template index: https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/

### B. Exempt — 45 CFR 46.104(d)(2) and/or (d)(3)  **← most likely if treated as research**

**§46.104(d)(2)** — research that **only** includes interactions involving educational tests, **surveys**, **interviews**, or **observation of public behavior** (including visual or auditory recording), if one of (i)/(ii)/(iii) is met:

- (i) identity cannot readily be ascertained; **or**  
- (ii) disclosure outside the research would **not** reasonably risk criminal/civil liability or damage financial standing, **employability**, educational advancement, or **reputation**; **or**  
- (iii) identity **can** be ascertained **and** an IRB conducts **limited IRB review** under **§46.111(a)(7)** (privacy/confidentiality provisions).  

https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104  
https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.111

**§46.104(d)(3)** — **benign behavioral interventions** with adults who **prospectively agree**, plus information collection (verbal/written/audiovisual), meeting (A)/(B)/(C) analogous to above. Interventions must be brief, harmless, painless, not physically invasive, not likely to have significant lasting adverse impact, and not expected to be offensive/embarrassing. Examples in the rule (games, puzzles under noise, allocating cash) are illustrative. WoZ **cue display during a sim** can often be argued as a brief behavioral intervention in an adult education/sim setting—**confirm with VCU HRPP** whether they accept (d)(3) for this design or prefer (d)(2) for survey/observation components.

**Identifiability / harm angle:** Identifiable **voice/video/faces** of clinicians, plus timing/missed-action metrics, could reasonably implicate **reputation or employability** if disclosed outside research → **(d)(2)(iii)** or **(d)(3)(i)(C)** limited IRB review is the cautious fit unless recordings are never identifiable or are destroyed after coding and identity cannot be ascertained.

**VCU-specific:** Even if research is exempt, **“at VCU the determination of exemption must be made by the IRB.”** Investigators do **not** independently finalize exemption. VCU is **not** implementing exemption categories **7 and 8**.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/types-of-irb-review/  
OHRP recommends institutions not let investigators self-determine exemption (conflict of interest).  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/exempt-research-determination/index.html

### C. Expedited review (63 FR 60364)

If not exempt (e.g., intervention framed outside (d)(3), or IRB declines exemption): **minimal risk** research may fit **expedited category 6** (voice/video/digital/image recordings for research) and/or **category 7** (surveys/behavior/human-factors/program evaluation-type methods).  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/categories-of-research-expedited-review-procedure-1998/index.html  
Source: 63 FR 60364 (Nov. 9, 1998).

### D. Full board

Unlikely for this minimal-risk adult sim **unless** the IRB finds greater than minimal risk, inadequate confidentiality protections for identifiable performance recordings, coercive recruitment of subordinates, or other issues that remove expedited/exempt eligibility.

---

## 6. FDA 21 CFR 50 / 56 / 812

Phase 0.5 WoZ uses a **human** cue-sender and existing display—**no Crisis Mirror software/device as a test article in the loop**. Under FDA device IDE definitions, an **investigation** evaluates safety/effectiveness of a **device** (**21 CFR 812.3**).  
https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812/subpart-A/section-812.3

**Practical reading for Phase 0.5:** not an FDA-regulated clinical investigation of a device. **Confirm with VCU HRPP / regulatory counsel** if any claim of device evaluation creeps in.

**Important transition:** Once **real Crisis Mirror software** drives cues (or the study evaluates safety/effectiveness of a device/software function), the activity may become an FDA-regulated clinical investigation. FDA’s IRB exemptions (**21 CFR 56.104**) are narrow (mostly historical / emergency use / taste-food); **Common Rule §46.104 exemptions generally do not cover FDA-regulated clinical investigations** (except overlapping taste/food-type cases). Plan a **fresh** determination before software-in-the-loop studies.

---

## 7. Employee / trainee participants and coercion

Participants may be staff, faculty, volunteers, or trainees. Belmont **Respect for Persons** requires voluntary participation free of **coercion** and **undue influence**.  
https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html  

OHRP Informed Consent FAQs: employees as subjects raise the same concerns as students—participation/refusal may be perceived to affect evaluations or advancement; employers are authority figures. Consent must be sought under circumstances that minimize coercion/undue influence (**45 CFR 46.116**).  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/informed-consent/index.html  

**Practice recommendation (ethical / OHRP-aligned; confirm with VCU HRPP):** Supervisors should **not** recruit or obtain consent from their own direct reports. **Co-I Dr. Sergio Navarrete is developing the Crisis Mirror concept**—disclose that conflict; he should **not** be the person obtaining consent from staff he supervises. Prefer PI or a non-supervising team member for recruitment/consent.

---

## 8. Identifiability of voice, video, and faces

Voice and facial images are typically **readily identifiable**. Retention of identifiable A/V → confidentiality risk and possible limited IRB review path under exemption (d)(2)(iii)/(d)(3)(i)(C). Deleting after coding, or recording only non-identifiable metrics, changes the analysis.

**Note:** Detailed “A/V consent cannot be waived” language in VCU’s public **HRP-103 Investigator Manual** appears in the **VA research appendix**—treat as **VA-specific**, not automatic VCU-wide rule for non-VA studies. For non-VA VCU research, public **HRP-503a** still expects protocols to describe audio/video/photographs as procedures; build plan already requires written consent covering A/V if any.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/

---

## 9. Most-likely answer (reasoned)

**Most likely:** Phase 0.5 will be treated as **human subjects research** eligible for **exemption under 45 CFR 46.104(d)(2)** (survey + observation/recording components) and/or **(d)(3)** (benign behavioral WoZ intervention with prospective adult agreement), **with limited IRB review** under **46.111(a)(7)** if identifiable recordings or linkable performance data are retained **and** disclosure could affect reputation/employability.  

**Alternate if VCU finds no generalizable-knowledge design:** official **NHSR / not human research** determination via **HRP-503b** (still submit if a letter is needed).  

**Fallback if exemption denied:** **expedited** categories **6** and **7**.  

**At VCU:** the **IRB/HRPP makes** exempt and NHSR official determinations—**do not self-determine exemption**. Submit in **VIRBs** before session 1.

---

## 10. What would change the answer

| Change | Likely effect |
| --- | --- |
| Identifiable A/V **kept** long-term / shared | Stronger need for limited IRB review or expedited; higher confidentiality scrutiny |
| Recordings **deleted after coding**; coded data not re-identifiable | May support (d)(2)(i) or (d)(3)(i)(A) |
| **Real patient data** or real-case PHI in audio | HIPAA + not Phase 0.5 as designed; stops exemption simplicity |
| Recordings of **simulated patients/actors** | Still human subjects if living actors; consent them too |
| Clear **publication / generalizable** design | Reinforces “research” |
| Purely local product go/no-go, no generalize | Supports NHSR/non-research argument |
| **Federal funding** / FWA-triggered coverage | Clarifies Common Rule applicability |
| **Crisis Mirror software** drives cues / device evaluation | Possible FDA clinical investigation; §46.104 exemptions generally unavailable |
| Individual clinician scores **shareable with employers** | Reputation/employability risk; may block (d)(2)(ii)/(d)(3)(i)(B); needs strong separation from performance review |

---

## 11. Sources fetched for this memo

1. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102  
2. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104  
3. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.111  
4. https://www.hhs.gov/ohrp/regulations-and-policy/decision-charts-2018/index.html  
5. https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/exempt-research-determination/index.html  
6. https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/quality-improvement-activities/index.html  
7. https://www.hhs.gov/ohrp/regulations-and-policy/guidance/categories-of-research-expedited-review-procedure-1998/index.html  
8. https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/informed-consent/index.html  
9. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html  
10. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812/subpart-A/section-812.3  
11. https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-56/subpart-A/section-56.104  
12. https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review/  
13. https://research.vcu.edu/integrity-and-compliance/hrpp-irb/types-of-irb-review/  
14. https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/  
15. https://onetrac.vcu.edu/research-vs-qi/  
16. `docs/architecture/V2-build-plan.md` (Phase 0.5)

*End of memo.*
