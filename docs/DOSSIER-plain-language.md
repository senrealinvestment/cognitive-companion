# Cognitive Companion — plain-language dossier

**Who this is for:** Co-investigator, co-founder, and anyone joining the core team who has **not** been in the planning chats.  
**How to read it:** Start at **The story so far**. Later sections zoom in on the same decisions. You should not need any other conversation to follow along.  
**Reading level:** Plain English. When a technical word appears, it is explained in the same sentence.  
**Last updated:** 2026-09-25

This dossier is a living document — update it as decisions land.

---

## The story so far

Cognitive Companion is a project to build an **ambient AI cognitive companion** for clinicians in **transplant ICU and critical care** (and related intensive care settings). “Ambient” means it listens in the background while people work. “Cognitive companion” means it tries to help the clinician **notice** important things — it does **not** give orders and it does **not** replace the clinician’s judgment.

Crisis Mirror was the early working name; the project is now branded Cognitive Companion.

### Where V1 ended and V2 began

An earlier version of the idea (**V1**) explored ambient listening with a more rigid “protocol card” style approach. That path is **retired**. The team is redesigning from scratch as **V2** for a real clinical application Sergio has in mind: a careful, advisory AI companion for high-stakes ICU work.

### Why the redesign was so detailed

The V2 redesign grew out of a long architecture discussion. The team had to choose:

- **Hardware** — which computers sit in a control room / closet and run the models  
- **Speech-to-text** — how room audio becomes text the system can understand  
- **Medical reasoning models** — which local models draft short advisory cues  
- **Privacy and regulatory rules** — what may never leave the room, and what VCU paperwork comes first  
- **Training approach** — how the system learns from labeled examples without updating itself at the bedside  

Those choices are written up in the architecture notes on **GitHub pull request (PR) #1**. This dossier restates them in everyday language.

### Decisions already locked

You will see each of these again below. Here is the spine of the plan:

1. **Dual-box hardware:** An **NVIDIA DGX Spark** (strong at fast speech work) plus a **Mac Studio with 512 GB of memory** (strong at larger “thinking” and local literature search). Two separate computers on a private network — they do **not** merge into one giant memory pool.  
2. **Local-first:** Bedside **decisions and nudges stay on those room computers**. Nothing is sent to the public cloud for deciding what to say in the moment.  
3. **Optional V2D cloud research lane:** Only for **deeper, on-demand** questions after a wake word or button — and only after a strict **local** check that the question is **not** patient-identifying. Details later.  
4. **Traffic-light nudge system:** Clinicians own the menu of what counts as a nudge (green / yellow / red). A database is the seed list.  
5. **Wizard-of-Oz first:** Before trusting hardware and models in the loop, run sims where the AI may log silently while a **human** decides what happens. Grade the AI’s judgment without anyone relying on it yet.  
6. **Lean Phase 0:** Start thin — architecture and engineering first; specialists only when their piece is needed.  
7. **VCU paperwork drafted (not finished until VCU says so):** Internal-only **not-human-subjects** path using **HRP-503b**, drafted for Phase 0.5. **Principal investigator (PI): Dr. Michael Kazior.** **Co-investigator: Dr. Sergio Navarrete.** Drafts live on **PR #4**.

### Who is on the team

- A **five-agent planning/build pod** covering, in everyday terms: **architecture**, **speech-to-text**, **clinical logic**, **regulatory and privacy**, and **coordination** (keeping the pieces aligned). Specialists stay scoped to their lane.  
- About **5–6 medical students** as early **category filters** — helping draft and review the nudge menu and related labeling, with clinicians remaining the authority.  
- **Investigators** named above for the VCU determination path.

### What is still open

Open risks and next actions are listed in the **action checklist** at the end. Examples: red-teaming the privacy filter before any cloud research, planning live calibration (not only sims), weekly student-batch review, advisory-only liability briefing, not hanging timelines on vendor deals, transcript reuse policy, picking the cloud provider only when implementing V2D, confirming the 512 GB Mac purchase still makes sense as models get smaller, and the engineering items (formal eval pipeline, vocabulary database on Mac Mini then migrate to Mac Studio, latency budget, failure modes, observability, and adapter contract tests).

---

## 1. What we build

Cognitive Companion listens with **audio only** (glasses and/or phone). The current design law is **no wearable camera**, because face-worn video creates serious privacy and consent problems.

What the clinician sees or hears from the system is an **advisory nudge** — a short suggestion meant to help attention. The system:

- **Never** writes medical orders  
- **Never** decides treatment  
- **Never** replaces the clinician  

**The clinician always decides.**

---

## 2. Why it matters

In a busy ICU, people can miss cues under load — not because they are careless, but because attention is scarce. Cognitive Companion’s job is to be a careful second set of ears: quiet most of the time, useful when something important may be missed, and easy to ignore when it is wrong.

That is why the traffic-light system and Wizard-of-Oz grading exist: we want proof that the companion is **helpful and not noisy** before anyone depends on it.

---

## 3. Status

**Decided / in motion**

- **Hardware path:** Dual-box — **NVIDIA DGX Spark** plus **Mac Studio (512 GB target)**.  
- **Regulatory:** VCU **not-human-subjects** path drafted for Phase 0.5 — adapt into **HRP-503b**. Activity is **internal only** (product go/no-go; **no** publishing cue-test results as research). **PI: Dr. Michael Kazior**; **co-investigator: Dr. Sergio Navarrete**. Drafts on **PR #4**. Final determination belongs to VCU HRPP / IRB — do not start sessions until you have their letter.  
- **Build order:** **Wizard-of-Oz** before buying/committing to full local-model and hardware integration. “Wizard of Oz” is named after the movie where a hidden person runs a grand machine: here the AI can run **silently** in the background during sim sessions and log every nudge it *would* have given, while a **human** (the “wizard”) actually decides what happens — so no patient is ever affected by the model’s output. We grade the model’s judgment without anyone relying on it yet. **Lean Phase 0** — architecture and engineering first; specialists only for their pieces.  
- **V1 retired:** Old protocol / card-style flow is out. Current work is **V2** (local decision routing + local medical cue drafting; **no** cloud model deciding bedside nudges).

**Still open (examples)** — see also the checklist:

- Exact wake-word engine and permission questions for any tribute placeholder phrase  
- Which frontier cloud model fills the optional V2D research slot (chosen at implementation)  
- Whether OpenEvidence / UpToDate contracts happen (optional; not on the critical path)  
- How well the non-PHI / de-identification check works before any cloud research egress  
- Gold-nudge authors and sim consent details (see regulatory drafts on PR #4)

---

## 4. Architecture (plain)

Imagine two powerful computers in a **sim control room or closet** — not marketed as bedside medical devices.

1. Glasses or a phone send audio over an **encrypted local network** (a private, protected link inside the facility/lab) to those computers.  
2. **DGX Spark** focuses on **speech**: turning sound into text and related speech jobs, plus training work that needs NVIDIA’s CUDA tools.  
3. **Mac Studio** focuses on **thinking** for the live advisory path: drafting short cue text with a local medical model (the working baseline discussed is **MedGemma 27B**), local literature search when needed, and — for V2D — the privacy gate before any optional cloud research.  
4. **Nothing goes to the cloud for bedside decisions.** Choosing whether to nudge, and what to say in the moment, stays on the local boxes.

**Shared product spine (same idea on both boxes):** clean up / de-identify what must stay local → a small local “System One” router that decides salience and urgency → draft a short cue → a safety/wording gate → show a brief heads-up on glasses or phone → later, humans label whether it helped (for offline training only — **no self-updating at the bedside**).

### Optional add-on: V2D cloud research lane

V2D means: keep the dual-box local system, and add a **cloud research** option that is **not** used for automatic bedside decisions.

Rules:

- Only after a **wake word or button** (on-demand). **Never automatic.**  
- Before anything leaves the room: a **strict local non-PHI check** on the Mac (“PHI” means patient-identifying information). When in doubt, **stay local**. Strip identifiers.  
- Use a **zero-retention gateway** so API keys never sit on the Spark or Mac, and prompts/answers are not kept by the pipe.  
- The cloud model is a **swappable slot**: a frontier model with zero-data-retention enterprise terms, **chosen at implementation** (people mention examples like OpenAI or Anthropic — the architecture does **not** lock a vendor).  
- **OpenEvidence** and **UpToDate** may plug in later **only if** enterprise agreements exist. **Neither is a default.**

Details for engineers: `docs/architecture/` on **PR #1**, especially `V2D-dual-box-cloud-research.md`.

---

## 5. Nudge system

Nudges use a **traffic-light** framing clinicians can edit:

| Color | Plain meaning |
|-------|----------------|
| **Green** | Extremely important — escalate (**nudge now**) |
| **Yellow** | Worth paying attention to (**watch**) |
| **Red** | Less important — monitor only (**stay quiet**) |

**Clinicians own the category menu.** The seed list is a database with organ-system tabs (Neuro, Cardiac, Pulmonary, GI, Hepatology, Renal, Heme, Infectious Disease, Endocrine, Musculoskeletal) plus an **Emergencies** tab whose jump-off reference is the **Stanford Emergency Manual** (also called the Stanford Guide).

**Auto-escalate:** Some diagnoses or patterns can be marked to **short-circuit** the normal light — jump straight to green when detected, like an ambulance through a red light.

That database is a **seed training / labeling set**, not finished clinical doctrine. Panel review replaces placeholders. Medical students may help filter drafts; clinicians approve.

File: `docs/architecture/nudge-category-vocabulary.xlsx` (on the same V2 branch as this dossier).

**Vocabulary database plan:** The seed list is the versioned, provenance-tracked database that tracks who tagged what and when (schema: `docs/architecture/nudge-vocabulary-schema.md`). **Build and populate it now on Sergio’s existing Mac Mini** (prototype / dev). When the **Mac Studio** arrives, **migrate the same schema and data** there as **production** (see the action checklist).

---

## 6. Team

- **Five-agent Cognitive Companion pod** (planning/build roles in plain words): architecture, speech-to-text, clinical logic, regulatory and privacy, and coordination. Keep specialists paused or narrow until their piece is needed (lean Phase 0).  
- **About 5–6 medical students** as early filters on categories and labeling batches.  
- **Investigators:** Dr. Michael Kazior (PI for the VCU determination path); Dr. Sergio Navarrete (co-investigator / co-founder).

---

## 7. Doc index (where to click)

*(If you are on GitHub’s `main` branch you may not see `docs/` yet — switch the branch dropdown to `v2-speech-layer-ab`.)*

| What | Where |
|------|--------|
| Architecture notes + diagram (hardware stacks, shared spine, V2D) | **PR #1** — `docs/architecture/` · `cognitive-companion-architecture.html` · `assets/cognitive-companion-architecture.png` |
| V2D cloud research addendum | `docs/architecture/V2D-dual-box-cloud-research.md` |
| Nudge category vocabulary spreadsheet | `docs/architecture/nudge-category-vocabulary.xlsx` |
| Nudge vocabulary **schema** (Mac Mini prototype → Mac Studio production) | `docs/architecture/nudge-vocabulary-schema.md` |
| IRB / NHSR Phase 0.5 drafts (HRP-503b path) | **PR #4** — `docs/regulatory/` |
| This dossier | `docs/DOSSIER-plain-language.md` |

Direct dossier link on the V2 branch:  
https://github.com/senrealinvestment/cognitive-companion/blob/v2-speech-layer-ab/docs/DOSSIER-plain-language.md

---

## 8. Action checklist

*(Copy answers into the `Response:` lines.)*

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

### Engineering (must become systems, not promises)

- [ ] Build a **formal evaluation pipeline** — continuous-integration (CI) harness, fixed test set, and scoreboard — **before any model training**. “Every update must pass eval” is currently a promise, not a system.  
  Response: ___

- [ ] Build and populate the **versioned, provenance-tracked database** (who tagged what, when) that is the nudge-category seed list. Schema: `docs/architecture/nudge-vocabulary-schema.md`. **Build and populate now on Sergio’s existing Mac Mini** (prototype / dev). When the **Mac Studio** arrives, **migrate the same schema and data** to it as **production**.  
  Response: ___

- [ ] Define a **hard latency budget** for speech-to-cue (for example: 500 ms vs 2 seconds) as a written **spec**, not something discovered after purchase.  
  Response: ___

- [ ] Define **failure modes and graceful degradation**: Spark drop, network hiccup, low classifier confidence — **suppress cues rather than guess**, and alert a human.  
  Response: ___

- [ ] Add **observability**: health checks, an audit log of every emitted cue with timestamp, and an alert when the system goes quiet.  
  Response: ___

- [ ] Write **contract tests** for the `SystemOneClient` adapter so swapping models cannot silently break behavior.  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

- [ ] Additional item: ___  
  Response: ___

---

## 9. Wizard-of-Oz grading rubric

**Draft for clinician review — not final.**

“Wizard of Oz” here means the same thing as in the movie: a hidden person is running the show. In our sims the AI stays **silent**, logging every nudge it *would* have given, while a **human wizard** actually decides what happens — so the model never affects a patient. We are grading its judgment before anyone relies on it.

In that **silent phase**, the model does **not** speak to the clinician. It still **logs every moment it would have nudged**.

Each log line should capture, in plain fields:

- **When** (timestamp)
- **What it heard** (short transcript snippet or note)
- **What category** it would have chosen
- **How sure** it was (confidence)

After each sim session, a clinician reviews those logs and answers **three simple questions** per logged call:

1. **Should it have spoken at all?** Yes / No  
2. **If yes, was the category right?** Yes / No  
3. **Was the timing right?** Too early / Just right / Too late  

That is the whole grade for one call. No long forms. Stack enough sessions and you can see whether the system is too chatty, wrong-category, or late — before it ever talks in the room.

Use this rubric to train and calibrate; replace or tighten it once the clinical panel signs off.

---

This dossier is a living document — update it as decisions land.
