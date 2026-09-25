# Phase 0.5 IRB / HRPP determination memo (advisory) — NHSR primary

**Project:** Crisis Mirror — Phase 0.5 Wizard-of-Oz (WoZ) sim  
**Source design:** `docs/architecture/V2-build-plan.md` (Phase 0.5), commit `a3bc50d` on `architect/v2-build-plan`  
**PI (draft):** Dr. Michael Kazior · **Co-I (draft):** Dr. Sergio Navarrete  
**Date:** 2026-09-25 (America/New_York)  
**Status:** Advisory analysis only — **not legal advice**; **final determination belongs to VCU HRPP / the VCU IRB**  
**Authoritative product decision:** Phase 0.5 is **INTERNAL ONLY** — no publication of cue-test results as research. Primary pathway = **not human subjects research (NHSR)** via **HRP-503b** in VIRBs.

---

## ★ If plans change — cannot retrospectively publish (read this first)

**Rule (non-optional):**

1. If Sergio / the team later wants to **publish** Phase 0.5 cue-test results, present them as research findings, or otherwise treat the activity as **generalizable research**, they must obtain **IRB review** (exempt, expedited, or full board, as VCU determines) **BEFORE any sessions that would be used for that research**.
2. Sessions conducted under an **NHSR / internal-only** determination **cannot be retrospectively published** (or otherwise repurposed) as human-subjects research under that NHSR letter.
3. Changing intent mid-stream means: **stop new sessions**, disclose the new design/intent to VCU HRPP, and obtain the applicable determination/approval **before** collecting any data intended for research/publication.

Put another way: NHSR for internal product go/no-go is a **use restriction**, not a shortcut to later papers. Plan publication → get IRB first → then run the research sessions.

---

## 1. What Phase 0.5 actually is (per the build plan + Sergio’s decision)

From V2-build-plan Phase 0.5 (follow the doc if it differs from informal summaries), **as constrained by the internal-only decision**:

- **Goal:** Before hardware purchase or model training, run **3–5 sim sessions** in which a **human hand-sends cues** to a display the team already has, to learn whether cues help, which categories matter, timing, and distraction — **for a local product go/no-go**, not for generalizable research publication.
- **Who:** Clinician **operator** (sim faculty or clinician) follows a **scripted cue sheet** (may send allowed free-text under wording rules); separate **observer/timekeeper** (does not send cues); engineer runs cue-sender tooling; Clinical Safety & Eval owns metrics/wording.
- **Measured (internal):** time to key actions; missed-action rate vs checklist; latency trigger→display; acted-on vs ignored; false/unhelpful rate in debrief; **short survey** on distraction/usefulness; debrief notes on timing.
- **Participants:** **Staff/volunteers in sim, never patients**. **No real patient data, QI/QA from institutional systems, or VCU institutional systems login.** Written informed consent / information sheet for sim volunteers covering **audio/video if any**, storage duration, who can access recordings, and withdrawal — framed for **internal product evaluation**, not research publication.
- **Outputs (internal):** seed gold nudges (ICU physician panel–approved), draft cue-category list, explicit go/no-go for Phases 1–4. **No publication of cue-test results as research** under this pathway.

**Framing for VCU:** Internal product evaluation / quality-improvement–style evaluation of a **prototype in simulation** — systematic local learning for this team’s go/no-go — **not** designed to develop or contribute to generalizable knowledge for external audiences.

---

## 2. Does the Common Rule apply at all?

**45 CFR 46** (the Common Rule, HHS) applies to research involving human subjects that is **conducted or supported by a Common Rule department/agency**, or that an institution elects to cover under its **Federalwide Assurance (FWA)** / institutional policy. Many universities apply Common Rule–aligned procedures to all human research regardless of funding.

- **Confirm with VCU HRPP:** whether this activity is covered by VCU’s FWA / institutional policy even if there is **no federal funding**, and which regulations VCU will apply.

Public VCU pages state that the VCU IRB oversees activities meeting the regulatory definitions of research involving a human subject, and that VCU is engaged when research is conducted by VCU faculty/staff/students in their university capacity (among other engagement criteria). Investigators may request an **official determination** (including NHSR) via VIRBs.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review/

---

## 3. Is it “research”? — 45 CFR 46.102(l) (primary NHSR question)

> **Research** means “a systematic investigation, including research development, testing, and evaluation, **designed to develop or contribute to generalizable knowledge**.”  
> https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102

Phase 0.5 is **systematic** (scripted sessions, predefined metrics, survey, debrief). Under Sergio’s **internal-only** decision, it is **not designed** to contribute to **generalizable knowledge** for publication or external scientific audiences — it is designed to answer a **local** product go/no-go for Crisis Mirror.

**OHRP Quality Improvement FAQs** (framing; note FAQ cites older subsection letters):

- Pure QI limited to implementing a practice and collecting data for clinical/practical/administrative purposes is often **not** “research.”  
- **Intent to publish alone does not make** an activity research; conversely, research can exist without publication plans.  
- Projects that also collect information to establish scientific evidence of how well an intervention works **may** be research.  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/quality-improvement-activities/index.html

**Application under current decision:** Design for **local** Crisis Mirror go/no-go / prototype evaluation in sim supports an **NHSR / not human research** request. If the team later redesigns the work to answer general questions for papers or external audiences, that is **research** — see the ★ box above.

**VCU OneTRAC (public):** Research vs QI hinges on design for generalizable knowledge; publishing QI does not automatically convert QI to research — but **publishing as research after NHSR sessions is not available under the NHSR letter**.  
https://onetrac.vcu.edu/research-vs-qi/

---

## 4. Are there “human subjects”? — 45 CFR 46.102(e)(1)

> **Human subject** means a living individual about whom an investigator conducting research:  
> (i) obtains information or biospecimens through **intervention or interaction**, and uses/studies/analyzes it; **or**  
> (ii) obtains, uses, studies, analyzes, or generates **identifiable private information** or identifiable biospecimens.  
> https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102

If VCU agrees the activity is **not research**, the human-subjects definition does not trigger IRB review as human subjects research. Practically, Phase 0.5 still involves **interaction** with living staff/volunteers and may involve identifiable A/V — which is why **official NHSR determination** (not casual self-labeling) and ethical consent/information practices for sim volunteers remain recommended.

**OHRP decision charts (2018 Requirements):** Chart 01 (is it human subjects research?).  
https://www.hhs.gov/ohrp/regulations-and-policy/decision-charts-2018/index.html

---

## 5. Pathway options — PRIMARY first, then alternates only if plans change

### A. PRIMARY — Not human subjects research (NHSR) / non-research  **← current decision**

**Request:** Official **NHSR / not human research** determination letter via VIRBs by completing and uploading **HRP-503b TEMPLATE NHSR**, before any Phase 0.5 sessions begin.

**Rationale under current decision:** Activity is designed as **internal product go/no-go / quality-improvement–style evaluation of a prototype in sim**, not as generalizable research intended for publication. Build-plan outputs (seed gold nudges, cue-category list, hardware go/no-go) are **local product** deliverables.

**VCU public process:**

- Investigators are responsible for deciding whether IRB review is needed, but **may submit for an official determination**; for NHSR, upload **HRP-503b**. The review decision is sent in a letter to the PI.  
  https://research.vcu.edu/integrity-and-compliance/hrpp-irb/activities-requiring-irb-review/
- Submit in **VIRBs** (VCU IRB system).  
  https://research.vcu.edu/integrity-and-compliance/hrpp-irb/virbs/
- Template index: https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/
- Per HRP-503b notes (public template): IRB will not make NHSR determinations **after** the activity has begun — **submit before session 1**.

**Strong recommendation:** Obtain the **official HRPP/IRB NHSR letter BEFORE session 1**. Do **not** self-determine casually even when the internal-only framing is clear. **VCU HRPP / the VCU IRB decides.**

**Dept-head ancillary (public VIRBs page):** Department-head approval is required for all new submissions **except NHSR and exemption determination requests** (also required for external IRB reliance and HUD). Confirm current VIRBs config for your submission.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/virbs/

### B. Alternate — Exempt — 45 CFR 46.104(d)(2) and/or (d)(3)  **← only if plans change to research**

Use **only if** the team decides Phase 0.5 (or a successor protocol) **is** human subjects research (e.g., publication / generalizable design). Then VCU must determine exemption; investigators do **not** self-exempt.

**§46.104(d)(2)** — research that **only** includes interactions involving educational tests, **surveys**, **interviews**, or **observation of public behavior** (including visual or auditory recording), if (i)/(ii)/(iii) is met (including limited IRB review under **§46.111(a)(7)** when identity can be ascertained and disclosure could affect reputation/employability).  
**§46.104(d)(3)** — **benign behavioral interventions** with adults who **prospectively agree**, plus information collection, under analogous conditions.

https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.104  
https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.111  

**VCU-specific:** Even if research is exempt, **“at VCU the determination of exemption must be made by the IRB.”** VCU is **not** implementing exemption categories **7 and 8**.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/types-of-irb-review/

### C. Alternate — Expedited review (63 FR 60364)

If treated as research and not exempt: **minimal risk** research may fit **expedited category 6** (voice/video/digital/image recordings) and/or **category 7** (surveys/behavior/human-factors/program evaluation-type methods).  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/categories-of-research-expedited-review-procedure-1998/index.html

### D. Full board

Unlikely for this minimal-risk adult sim **unless** the IRB finds greater than minimal risk or other issues that remove expedited/exempt eligibility — relevant only if the activity is research.

---

## 6. FDA 21 CFR 50 / 56 / 812

Phase 0.5 WoZ uses a **human** cue-sender and existing display—**no Crisis Mirror software/device as a test article in the loop**. Under FDA device IDE definitions, an **investigation** evaluates safety/effectiveness of a **device** (**21 CFR 812.3**).  
https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812/subpart-A/section-812.3

**Practical reading for Phase 0.5:** not an FDA-regulated clinical investigation of a device. **Confirm with VCU HRPP / regulatory counsel** if any claim of device evaluation creeps in.

**Important transition:** Once **real Crisis Mirror software** drives cues (or the study evaluates safety/effectiveness of a device/software function), the activity may become an FDA-regulated clinical investigation. Plan a **fresh** determination before software-in-the-loop studies — and if that work is research intended for publication, use the IRB research pathway from the start (see ★ box).

---

## 7. Employee / clinician participants and coercion

Participants may be staff, faculty, volunteers, or trainees. Belmont **Respect for Persons** requires voluntary participation free of **coercion** and **undue influence**.  
https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html  

OHRP Informed Consent FAQs: employees as subjects raise the same concerns as students. Consent must be sought under circumstances that minimize coercion/undue influence (**45 CFR 46.116**).  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/informed-consent/index.html  

**Practice recommendation (ethical / OHRP-aligned; confirm with VCU HRPP):** Supervisors should **not** recruit or obtain consent from their own direct reports. **Co-I Dr. Sergio Navarrete is developing the Crisis Mirror concept**—disclose that conflict; he should **not** be the person obtaining consent from staff he supervises. Prefer PI or a non-supervising team member for recruitment/consent. This recommendation applies even under NHSR (ethical sim practice).

---

## 8. Identifiability of voice, video, and faces

Voice and facial images are typically **readily identifiable**. Under the **NHSR / internal-only** path, recordings (if any) are for **internal product evaluation** (and, only if separately opted in, internal system-training uses) — **not** for publications/presentations as research deliverables. Deleting after coding, or recording only non-identifiable metrics, reduces risk.

**Note:** Detailed “A/V consent cannot be waived” language in VCU’s public **HRP-103 Investigator Manual** appears in the **VA research appendix**—treat as **VA-specific**, not automatic VCU-wide rule for non-VA activities.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/

---

## 9. Most-likely answer under the current decision (reasoned)

**Primary (current decision):** Request an official **NHSR / not human research** determination via **HRP-503b** in VIRBs, because Phase 0.5 is framed as **internal product go/no-go / QI-style prototype evaluation in sim**, **not** generalizable research intended for publication. **Obtain the letter before session 1.** Do not self-determine casually. **VCU HRPP / IRB decides.**

**If plans change to publication / generalizable research:** Stop; obtain IRB review (likely exempt **46.104(d)(2)** and/or **(d)(3)** with limited IRB review under **46.111(a)(7)** if identifiable recordings/linkable performance data are retained, or expedited categories **6**/**7** if exemption is denied) **before** any sessions that would be used for research. **Cannot retrospectively publish** NHSR/internal sessions as research.

**FDA:** Unlikely for Phase 0.5 WoZ as designed; reassess before software-in-the-loop.

---

## 10. What would change the answer

| Change | Likely effect |
| --- | --- |
| Keep **internal-only** go/no-go design; no publication as research | Supports **NHSR primary** (still get official letter) |
| Clear **publication / generalizable** design | Leaves NHSR; requires **IRB research review before those sessions**; cannot retrofit old NHSR sessions |
| Identifiable A/V **kept** for internal eval only | Still compatible with NHSR request if not research; tighten access/retention; no publication-clip use |
| Recordings **deleted after coding** | Lower confidentiality risk under any pathway |
| **Real patient data** or real-case PHI in audio | HIPAA + not Phase 0.5 as designed |
| **Crisis Mirror software** drives cues / device evaluation | Possible FDA clinical investigation; fresh determination |
| Individual clinician scores **shareable with employers** | Reputation/employability risk — avoid under any pathway |

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
15. https://research.vcu.edu/integrity-and-compliance/hrpp-irb/virbs/  
16. https://onetrac.vcu.edu/research-vs-qi/  
17. `docs/architecture/V2-build-plan.md` (Phase 0.5)

*End of memo.*
