# Crisis Mirror — plain-language dossier

**Audience:** Co-investigator and co-founder (and anyone joining the core team).  
**Reading level:** Plain English.  
**Last updated:** 2026-09-25

This dossier is a living document — update it as decisions land.

---

## 1. What we build

Crisis Mirror is an **ambient AI cognitive companion** for ICU clinicians.

- Glasses and/or a phone **listen** to the room (audio only; **no camera** in the current design).
- The system offers **advisory nudges** — short suggestions meant to help the clinician notice something.
- It **never** writes orders, never replaces judgment, and never decides for the clinician.
- The clinician always decides.

---

## 2. Why

In a busy ICU, people can miss cues under load — not because they are careless, but because attention is scarce.

Crisis Mirror’s job is to be a careful second set of ears: quiet most of the time, useful when something important is likely being missed, and easy to ignore when it is wrong.

---

## 3. Status (as of this writing)

**Decided / in motion**

- **Hardware path:** Dual-box — **NVIDIA DGX Spark** plus **Mac Studio (512 GB target)**.
- **Regulatory:** VCU **not-human-subjects** path drafted for Phase 0.5 — adapt into **HRP-503b** (NHSR). Activity is **internal only** (product go/no-go; **no** publishing cue-test results as research). Named **PI: Dr. Michael Kazior**; **co-investigator: Dr. Sergio Navarrete**. Drafts live on **PR #4** (not a final VCU determination until HRPP/IRB issues one).
- **Build order:** **Wizard-of-Oz** (human sends cues) **before** buying/committing to full local models and hardware integration. **Lean Phase 0** — Architect + engineer first; specialists only for their pieces.
- **V1 retired:** Old protocol / Stanford-card style flow is out. Current work is **V2** (local System One + MedGemma cues; no cloud “Jev” deciding).

**Still open (examples)**

- Exact wake-word engine and family/estate permission for the tribute placeholder phrase.
- Which frontier cloud model fills the optional V2D research **slot** (chosen at implementation).
- Whether OpenEvidence / UpToDate deals happen (optional; not on the critical path).
- Classifier evaluation for any future non-PHI cloud egress.
- Final gold-nudge authors and sim consent details (see regulatory drafts).

---

## 4. Architecture (plain)

Think of two powerful computers in a **sim control room / closet**, not at the bedside as medical devices.

1. Glasses or phone send audio over an **encrypted local network** to those computers.
2. **DGX Spark** focuses on **speech** (who spoke / what was said) and CUDA-friendly training jobs.
3. **Mac Studio** focuses on **thinking** for the live advisory path (including MedGemma-style cue text and local literature search when needed).
4. **Nothing goes to the cloud for bedside decisions.** Routing and nudges stay on the local boxes.

**Optional add-on: V2D cloud research lane**

- Only for **on-demand deep research** after a **wake word or button**.
- **Never automatic.**
- Before anything leaves the room: a **strict local non-PHI check** on the Mac (when in doubt, **stay local**), and patient identifiers stripped.
- Traffic goes through a **zero-retention gateway** (keys stay off the boxes).
- The cloud model is a **swappable slot**: a frontier model with zero-data-retention enterprise terms, **chosen at implementation** (examples people mention: OpenAI or Anthropic — not locked in).
- **OpenEvidence** and **UpToDate** may plug in later **only if** enterprise agreements exist. **Neither is a default.**

Details: `docs/architecture/` on **PR #1**, especially the V2D addendum.

---

## 5. Nudge system

Nudges use a **traffic-light** framing clinicians can edit:

| Color | Plain meaning |
|-------|----------------|
| **Green** | Extremely important — escalate (**nudge now**) |
| **Yellow** | Worth paying attention to (**watch**) |
| **Red** | Less important — monitor only (**stay quiet**) |

**Clinicians own the category menu.** The seed list is a spreadsheet with organ-system tabs (Neuro, Cardiac, Pulmonary, GI, Hepatology, Renal, Heme, Infectious Disease, Endocrine, Musculoskeletal) plus an **Emergencies** tab whose jump-off is the **Stanford Emergency Manual (Stanford Guide)**.

**Auto-escalate:** some diagnoses/patterns can be marked to **short-circuit** the normal light — jump straight to green, like an ambulance through a red light — when that pattern is detected.

That spreadsheet is a **seed training / labeling set**, not finished clinical doctrine. Panel review replaces placeholders.

File: `docs/architecture/nudge-category-vocabulary.xlsx`

---

## 6. Team

- **Cognitive Companion Pod (five agents):** Architect, Speech Engineer, Clinical Models Lead, Clinical Safety & Eval, Regulatory & Privacy — coordinated for build/plan work; specialists stay scoped to their pieces.
- **Human clinical layer:** About **5–6 medical students** as filters / helpers on vocabulary, labeling, and review batches (exact roster and schedule still operational).
- **Investigators:** Dr. Michael Kazior (PI for the VCU determination path); Dr. Sergio Navarrete (co-investigator / co-founder).

---

## 7. Doc index (where to click)

| What | Where |
|------|--------|
| Architecture notes + diagram (V2A / V2B / Hybrid / V2D) | **PR #1** — `docs/architecture/` · `crisis-mirror-architecture.html` · `assets/crisis-mirror-architecture.png` |
| V2D cloud research addendum | `docs/architecture/V2D-dual-box-cloud-research.md` (on PR #1 branch) |
| Nudge category vocabulary spreadsheet | `docs/architecture/nudge-category-vocabulary.xlsx` |
| IRB / NHSR Phase 0.5 drafts (HRP-503b path) | **PR #4** — `docs/regulatory/` (e.g. `phase0.5-nhsr-determination-request-DRAFT.md`, process + consent drafts) |
| This dossier | `docs/DOSSIER-plain-language.md` |

---

## 8. Action checklist

Copy answers into the `Response:` lines. Check boxes when done.

- [ ] Red-team the **de-ID / non-PHI classifier** before any real clinical data could hit a cloud research lane.  
  Response: ___

- [ ] Plan **live calibration** (real workflow stress), not only sim-lab sessions.  
  Response: ___

- [ ] Set a **weekly student-batch review** with a named assigned reviewer.  
  Response: ___

- [ ] Brief **risk management** on advisory-only liability (what we claim vs what we never claim).  
  Response: ___

- [ ] Do **not** put project timelines on OpenEvidence / UpToDate deals.  
  Response: ___

- [ ] Confirm **transcript secondary-use** policy (what may be stored, labeled, or reused).  
  Response: ___

- [ ] Decide the **cloud provider for the V2D slot at implementation** (architecture stays swappable).  
  Response: ___

- [ ] Confirm **Mac Studio 512 GB** procurement still makes sense given model distillation / size trends.  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

---

This dossier is a living document — update it as decisions land.
