# DRAFT — Phase 0.5 exemption / determination request (adapt for VIRBs)

**Disclaimer:** Advisory draft only — **not legal advice**. Adapt into VCU’s current public templates and submit via **VIRBs**. **Final determination belongs to VCU HRPP / the VCU IRB.** Do not start sessions until you have VCU’s determination/approval letter.

**How to use with VCU public templates (do not paste large template text into this public repo):**

| If VCU pathway is… | Primary public template to complete | URL index |
| --- | --- | --- |
| Official **NHSR / not human research** letter | **HRP-503b TEMPLATE NHSR** | https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/ |
| **Exempt** human subjects research | Protocol: **HRP-503** or SBS **HRP-503a**; consent/info: **HRP-502** or exempt information sheet per Investigator Manual | same URL |
| **Expedited** (fallback) | **HRP-503 / 503a** + **HRP-502** | same URL |

This draft **mirrors** common VCU protocol section order (Study Summary → Objectives → Background → Procedures → Population → Recruitment → Consent → Risks → Benefits → Data/Confidentiality → etc.) so content can be copied into HRP-503a fields. Section numbers below track **HRP-503a** style headings for convenience.

**Public process pages:**  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/getting-started/  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/types-of-irb-review/  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/virbs/

**Version:** DRAFT 0.1 · 2026-09-24 · Align footer with VCU version/date practice before upload.

---

## Protocol title

Crisis Mirror Phase 0.5: Wizard-of-Oz simulation study of advisory cue usefulness, timing, and distraction for ICU clinical teams (education / sim-lab only)

**Protocol / HM#:** [ASSIGNED BY VIRBs]  
**Version number/date:** [VERSION] / [DATE]

---

## Principal Investigator

- **Name:** Dr. Michael Kazior, [DEGREE(S)]  
- **Department:** [DEPARTMENT]  
- **Telephone:** [PHONE]  
- **Email:** [EMAIL]  

## Co-Investigator

- **Name:** Dr. Sergio Navarrete, [DEGREE(S)]  
- **Department:** [DEPARTMENT]  
- **Telephone:** [PHONE]  
- **Email:** [EMAIL]  
- **Role note:** Co-I is developing the Crisis Mirror product concept (see Conflicts of Interest).

## Other study personnel (placeholders)

- Clinician operator / cue-sender: [NAME / ROLE]  
- Observer / timekeeper: [NAME / ROLE]  
- Engineer (cue-sender tooling): [NAME / ROLE]  
- Clinical Safety & Eval metrics owner: [NAME / ROLE]  
- Person obtaining consent (must **not** be a supervisor of the enrollee; prefer PI or non-supervising designee): [NAME]

**Confirm with VCU HRPP:** PI eligibility for Dr. Kazior (permanent VCU/VCUHS employee per public Investigator Manual); CITI Human Subjects Protection current for all listed personnel; COI Investigator designations and AIRS disclosures.

---

## 1.0 Study summary

| Field | Content |
| --- | --- |
| Study design | Prospective, non-randomized Wizard-of-Oz simulation sessions; human operator hand-sends scripted (and limited free-text) advisory cues to an existing display while ICU-like teams complete education-only scenarios |
| Primary objective | Assess whether hand-sent advisory cues appear helpful vs distracting, and which cue categories / timings show repeated value |
| Secondary objectives | Measure timing/latency and action metrics; collect short survey and debrief notes; produce seed “gold nudge” examples and a draft cue-category list; inform go/no-go before hardware purchase |
| Intervention | Benign behavioral: display of short advisory cues during sim (no investigational device software in the loop; no drugs/devices under IDE) |
| IND/IDE | None — WoZ, no test article device/software driving cues |
| Study population | Adult staff/volunteers/faculty participating in sim (never patients) |
| Sample size | 3–5 consented sim sessions (exact headcount per session: [N PER SESSION PLACEHOLDER]) |
| Duration per participant | Approximately [DURATION PLACEHOLDER] per session including consent, sim, survey, debrief |
| Funding | [NONE / SOURCE PLACEHOLDER] — **confirm with VCU HRPP** re FWA/Common Rule coverage |

**Ancillary reviews (check HRP-309; confirm with VCU HRPP):** This Phase 0.5 design excludes real patient data, QI/QA content, and VCU institutional systems per the V2 build plan. Still confirm whether **sim facility**, **department**, **DMS**, or other ancillary reviews apply to the chosen pathway. Public VIRBs guidance: department-head ancillary review is required for many **new** submissions but **excludes NHSR and exemption determination requests** — confirm current rule for your submission type.  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/virbs/

---

## 2.0 Objectives / aims

1. Estimate whether WoZ advisory cues are rated net helpful and non-harmful (no cue-caused wrong action / harmful distraction) across 3–5 sessions.  
2. Characterize cue categories, timing, acted-on vs ignored rates, and distraction/usefulness via survey and debrief.  
3. Generate panel-reviewable seed gold nudges and a draft cue-category list to support a hardware go/no-go decision.

---

## 3.0 Background (brief)

Crisis Mirror is an advisory ambient-AI **concept** for ICU clinical teams. Phase 0.5 tests cue **human factors** in simulation **before** purchasing edge hardware or training models, using a human “wizard” instead of automated software (see `docs/architecture/V2-build-plan.md`). No live patients; education/sim only.

---

## 4.0 Study endpoints

- Primary (descriptive): participant survey ratings of usefulness/distraction; debrief judgment that cues helped vs harmed.  
- Process: time to key actions; missed-action rate vs checklist; latency trigger→display; acted-on vs ignored; false/unhelpful cue rate.  
- Deliverables: seed gold nudges; draft cue-category list; go/no-go recommendation.

---

## 5.0 Study intervention

Human operator sends short advisory text cues (scripted sheet; limited free-text under wording rules: advisory language, HUD-length discipline per Clinical Safety & Eval). Display is an existing laptop/phone/monitor—**not** investigational Crisis Mirror runtime. No EMR write; no real patient data.

---

## 6.0 Procedures involved (session flow)

1. **Pre-session:** Confirm VCU determination/approval letter on file; verify CITI/COI; prepare scripted cue sheet, checklist, survey, recording gear (if used).  
2. **Recruitment / consent:** Eligible adults receive study information; written informed consent (and recording release if A/V) **before** any recording or research procedures. Consent obtained by [PI or non-supervising designee — NAME].  
3. **Orientation:** Role assignments (team, operator, observer, engineer); reminder that participation is voluntary and **not** a performance review.  
4. **Sim scenario:** Education-only manikin/standardized scenario from Phase 0 scenario set ([SCENARIO IDS]). Operator sends cues per script; observer times key actions; engineer supports tooling only.  
5. **Metrics capture:** Observer records timing/missed actions/latency/acted-on vs ignored on paper or local encrypted form ([TOOL PLACEHOLDER]).  
6. **Debrief:** Structured discussion of false/unhelpful cues and timing; notes captured without employer identifiers beyond study ID.  
7. **Survey:** Short distraction/usefulness survey.  
8. **Close:** Remind withdrawal rights; storage/destruction summary; thank participants.  
9. **After session:** Coding/de-identification per Data Management; optional panel review of seed gold nudges (use de-identified materials unless additional consent obtained).

**Audio/video (if any):** Describe exactly what is recorded (room audio, video of bay, screen capture of cue display, etc.), who operates recording, and that faces/voices are identifiable. If no A/V: state “no audio/video recording.”

---

## 7.0 Data / specimen banking

No biospecimens. Optional later use of de-identified clips or transcripts for AI training **only** with separate opt-in on the recording release — default is research analysis only. **Confirm with VCU HRPP** before any model-training secondary use.

---

## 8.0 Sharing results with subjects

Aggregate/de-identified summaries may be shared with participants on request: [YES/NO PLACEHOLDER]. Individual performance scores will **not** be shared with employers or used for employment evaluation.

---

## 9.0 Study timelines

- Consent to end of debrief: ~[DURATION]  
- Overall accrual: [START DATE]–[END DATE] (3–5 sessions)  
- Analysis complete: [DATE PLACEHOLDER]

---

## 10.0 Inclusion / exclusion (subject population)

**Inclusion:** Adults (≥18) who are staff, faculty, or volunteers able to participate in an ICU-style education sim; able to consent in English [or language arrangements: PLACEHOLDER]; available for one session.

**Exclusion:** Patients or anyone receiving clinical care in the scenario; anyone under supervisory pressure who cannot freely decline; anyone the consenting person directly supervises if that person is obtaining consent; [OTHER PLACEHOLDER].

**Vulnerable populations:** Employees/trainees may perceive pressure—mitigations in Recruitment and Consent. No children, prisoners, or decisionally impaired adults targeted.

---

## 11.0 Local number of subjects

Approximately [TOTAL PARTICIPANTS] across 3–5 sessions (confirm headcount).

---

## 12.0 Recruitment methods

- [EMAIL LIST / SIM CENTER BULLETIN / VOLUNTEER CALL — PLACEHOLDER], posted/sent by someone **without** grading/employment authority over invitees when feasible.  
- Clear statement: voluntary; refusal/withdrawal will not affect job, evaluations, grades, or clinical privileges.  
- **Co-I (product developer) and any supervisor must not recruit or consent their own direct reports.**  
- No cold-calling patients; no use of VCUHS clinical systems for recruitment (per Phase 0.5 build-plan constraint).

Attach recruitment text as a separate document with version/date footer.

---

## 13.0 Withdrawal of subjects

Participants may stop at any time without penalty. On withdrawal: stop further data collection; ask preference for already-collected identifiable recordings (destroy vs retain coded data only) — **confirm allowable options with VCU HRPP**; document the choice.

---

## 14.0 Risks to subjects

- **Confidentiality breach** of identifiable A/V or performance notes (reputation/employability concern).  
- **Performance-evaluation anxiety** if participants fear scores will reach supervisors.  
- **Simulation stress** (crisis scenario cognitive load)—similar to ordinary sim education.  
- Minimal physical risk (standard sim environment hazards only).

**Mitigations:** encrypted local storage; no cloud upload of A/V by default; limited access list; no employer sharing; non-supervisor consent; clear voluntariness language; option to decline A/V while still participating in non-recorded metrics if feasible ([CONFIRM]); destroy or tightly control identifiable media.

---

## 15.0 Potential benefits

No direct clinical benefit. Possible indirect benefit: reflection on teamwork/cues. Societal/scientific benefit limited to improved design of advisory cues for future sim/education research.

---

## 16.0 Data management and confidentiality

- **What is stored:** consent forms; survey responses; timing sheets; debrief notes; optional A/V and transcripts.  
- **Identifiers:** study ID map stored separately from coded analytic files.  
- **Access:** PI, Co-I, [LIST]; need-to-know only.  
- **Storage:** encrypted local drive / institution-approved storage — **no consumer cloud** for identifiable A/V ([CONFIRM APPROVED PLATFORM WITH VCU HRPP / IT]).  
- **Coding:** remove names from transcripts where feasible; blur faces if clips used in presentations **and** participant opted in.  
- **Retention / destruction:** identifiable A/V retained until [DATE or DURATION PLACEHOLDER], then securely deleted; coded analytic data retained [DURATION] per VCU research data policy — **confirm with VCU HRPP**.  
- **HIPAA:** No PHI / no real patient data in Phase 0.5 as designed. If any PHI inadvertently captured, stop, isolate, and **confirm with VCU HRPP / privacy**.

---

## 17.0 Privacy provisions

Private consent conversation; do not discuss individual performance in open nursing-station style settings; badge presence of recording when A/V used.

---

## 18.0 Compensation for research-related injury

Minimal risk educational sim — [STANDARD VCU LANGUAGE FROM HRP-502 IF REQUIRED; PLACEHOLDER]. Not a clinical trial of a drug/device.

---

## 19.0 Economic burden

No expected costs to participants other than time. Parking/time compensation: [NONE / AMOUNT PLACEHOLDER].

---

## 20.0 Consent process

- Prospective written informed consent before participation (build plan requirement), using language aligned to **HRP-502** structure or, if VCU determines **exempt with interactions**, at least the abbreviated information elements in the public Investigator Manual (research; procedures; voluntary; investigator contact)—**confirm with VCU HRPP** which form they want.  
- Separate **recording release** with tiered opt-ins (research analysis; publications/presentations; AI-model training; education).  
- Time for questions; copy of signed form to participant.  
- Consent obtained by [NAME] who does **not** supervise the participant.

Public exempt abbreviated-consent expectations are summarized on VCU Getting Started / Investigator Manual materials via:  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/getting-started/  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/hrpp-policies-and-guidance/

---

## 21.0 Documentation of consent

Signed paper or VCU-approved eConsent (REDCap/DocuSign per VCU guidance) — **confirm with VCU HRPP**. Store with study records.

---

## 22.0 Setting

[SIM LAB / CLASSROOM BAY NAME AND ADDRESS PLACEHOLDER] — education space only; no live ICU patient care. Facility permission: [PLACEHOLDER — confirm with VCU HRPP / sim center].

---

## 23.0 Resources available

Qualified PI oversight; trained operator/observer; engineering support for cue-sender UI; Clinical Safety & Eval wording rules; secure storage.

---

## 24.0 Multi-site research

Single site: VCU / [SITE PLACEHOLDER]. No external IRB reliance planned.

---

## 25.0 HIPAA waiver

Not applicable — no PHI intended.

---

## Requested regulatory pathway and justification

**Primary request:** Determination that the activity is **exempt** under **45 CFR 46.104(d)(2)** and/or **(d)(3)**, with **limited IRB review** under **46.111(a)(7)** if identifiable recordings/linkable performance data are retained.

**Justification (short):** Adult volunteers in education sim; survey + observation (± A/V) and/or brief benign behavioral cue intervention with prospective agreement; minimal risk; no FDA test article in Phase 0.5 WoZ; confidentiality plan addresses employability/reputation risks.

**Alternate request:** If VCU finds the activity is **not** designed to contribute to generalizable knowledge, issue an **NHSR / not human research** determination (complete **HRP-503b** instead/in addition as instructed).

**Fallback:** Expedited review under OHRP 1998 categories **6** and **7**.

**VCU rule acknowledgment:** Exemption determination must be made by the VCU IRB (investigators do not self-exempt).  
https://research.vcu.edu/integrity-and-compliance/hrpp-irb/types-of-irb-review/

---

## Compensation

[NONE / $X / REFRESHMENTS — PLACEHOLDER]. Describe in protocol and consent per VCU payment guidance if any payment is offered.  
https://procurement.vcu.edu/i-want-to/pay-an-individual/compensate-a-research-participant/

---

## Conflicts of interest

**Disclose:** Co-Investigator Dr. Sergio Navarrete is developing the Crisis Mirror product concept and may have intellectual/commercial interests in study outcomes.  

**Management (proposed; confirm with VCU COI / HRPP):** Disclose in VIRBs/AIRS as required; Co-I will not obtain consent from subordinates; primary oversight and consent by PI Dr. Michael Kazior or a non-conflicted designee; analytic emphasis on pre-specified metrics; no individual scores to employers.  

COI program: https://research.vcu.edu/integrity-and-compliance/integrity-and-ethics/conflicts-of-interest-in-research/

---

## Publication plan

[NONE AT THIS TIME / INTENDED SUBMISSION TO ___ — PLACEHOLDER]. Build plan emphasizes product go/no-go; if publication is planned, state that clearly for VCU HRPP (generalizable-knowledge factor). OHRP: intent to publish alone does not define research.  
https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/quality-improvement-activities/index.html

---

## Attachments checklist (typical)

- This protocol content pasted into HRP-503 / 503a or HRP-503b as applicable  
- Consent + recording release (adapted from companion draft; final on HRP-502 or exempt info sheet)  
- Recruitment message  
- Survey instrument  
- Cue-sheet example / wording rules summary (no proprietary secrets required)  
- PI CV; Co-I CV if requested  
- CITI linked via matching email in VIRBs  

**Confirm with VCU HRPP** before submission that the file set matches current VIRBs requirements for exempt vs NHSR vs expedited.
