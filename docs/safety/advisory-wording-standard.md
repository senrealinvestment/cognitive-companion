# Advisory wording standard — Crisis Mirror cues (v0.1)

**Status:** Draft for clinician / sim-faculty review. Not merged policy.  
**Owner:** Clinical Safety & Evaluation  
**Scope:** Spoken and glanceable (HUD) cue text delivered by Crisis Mirror in **simulation-lab** use. Advisory only; the clinician decides.  
**Aligned to:** `docs/architecture/V2-shared-layers.md` (PR #1 / `v2-speech-layer-ab` @ d0d101f) — cue ≤8 words, gate + wording check, MedGemma-generated cue path, fail-closed ethos via silence / vetted fallback.

---

## 1. Purpose

This standard defines **how** Crisis Mirror may speak to a clinical team so that every delivered cue remains:

1. **Suggestive, not directive** — cognitive forcing, not orders.
2. **Short enough** for HUD glance and optional earcon / TTS without stealing working memory mid-crisis.
3. **Honest about uncertainty** — never fake certainty.
4. **Compatible with a deterministic safety gate** — see companion doc [`safety-gate-rules.md`](./safety-gate-rules.md).

It does **not** define the gold-nudge training schema (owned by Clinical Models Lead), the gate I/O interface or cue pipeline schema (owned by CC Architect), or FDA device / non-device determination (owned by CC Regulatory & Privacy).

---

## 2. Assumed interface (explicit — Architect owns the real contract)

Clinical Safety & Evaluation **does not** own the wire schema. The rules below assume the following until the Architect publishes the authoritative contract. **Every assumption is marked; reconcile before implementation.**

| ID | Assumption | Why we need it | Owner to reconcile |
|----|------------|----------------|--------------------|
| A1 | A cue candidate arrives at the wording gate as structured text (at least `cue_text_spoken` and/or `cue_text_hud`) plus metadata: `scenario_family` (or equivalent), `confidence` ∈ [0,1], `modality` ∈ {hud, spoken, both}, optional `earcon_id`, optional `source` ∈ {medgemma, vetted_label, deep_research_summary}. | Gate must lint words and route fallback. | CC Architect |
| A2 | Pipeline order on fast path is roughly: speech → System One (salience/category/urgency) → MedGemma cue draft → **wording/safety gate** → HUD (± tone). Deep research is clinician opt-in and may produce a longer panel; any HUD one-liner still passes this wording standard. | Matches V2 shared layers wording. | CC Architect |
| A3 | Gate outcomes the Architect will honor include at least: `deliver` (possibly after rewrite), `fallback_vetted_label`, `suppress` (silence). Exact enum names are Architect-owned. | Fail-closed behavior. | CC Architect |
| A4 | HUD hard budget is **≤8 words** (product spine / architecture diagram). Spoken cue may be slightly longer (see §5) but should share the same semantic content. | Length lint. | CC Architect / product |
| A5 | Confidence is a numeric score available **before** delivery; thresholding is a gate rule, not a wording rule. | Uncertainty handling. | CC Architect / System One |
| A6 | A vetted-label catalog exists (static, faculty-approved strings keyed by scenario family / urgency). Schema of that catalog is **not** defined here. | Fallback path. | Sim faculty + Architect |
| A7 | No automatic EMR write, no dosing order entry, no actuator control from cues. | Out of scope for wording but assumed product law. | Product / Architect |

If any of A1–A7 is wrong, update this doc and the gate rules in the same PR cycle — do not silently reinterpret.

---

## 3. Grammatical framing (required)

Every cue must use **one** of these frames (or a close variant that still fails the banned-list in §4):

| Frame | Pattern | Intent |
|-------|---------|--------|
| Suggestive | `Consider …` | Soft cognitive force |
| Interrogative check | `Check …?` / `Confirm …?` | Prompt verification without ordering |
| Observational | `Noted: …` | Surface a salient observation; clinician interprets |
| Differential nudge | `Diff includes …` / `Also consider …` | Widen, not close, the differential |
| Reference (checklist only) | `Ref: [vetted checklist item] — consider` | Quote a pre-approved cognitive aid; still suggestive |

**Default voice:** second-person team-facing, present tense, no patient name/MRN/identifiers in the cue string.

### 3.1 Required semantic elements

A delivered cue should encode **both**:

1. **Observation or trigger context** (what was noticed / which concern family), and  
2. **Suggestion or check** (what to consider next),

without collapsing into a single imperative order.

Acceptable compression for HUD (≤8 words) may fold both into one short phrase, e.g. `Noted: rising EtCO2 — check MH?` (7 words).

### 3.2 Dosing and orders

- **Banned:** generating novel drug doses, rates, concentrations, or “give / start / push / order …” language.
- **Allowed only as reference:** quoting a **faculty-vetted** checklist / emergency-manual line, explicitly framed as reference, e.g. `Ref: MH card — consider dantrolene path` — never as `Give dantrolene 2.5 mg/kg now`.
- If MedGemma drafts a dose, the gate **must** fail that draft (fallback or suppress). Gold-nudge / training policy for dosing refusal is owned by Clinical Models Lead; this standard only bans delivery.

---

## 4. Banned language (fail the wording lint)

### 4.1 Banned imperative / directive verbs and openings

Case-insensitive whole-word / phrase match (non-exhaustive starter list; extend via gate config YAML):

`give`, `administer`, `push`, `bolus`, `start`, `stop`, `discontinue`, `order`, `prescribe`, `intubate now`, `call a code`, `you must`, `you should`, `do not skip`, `immediately do`, `proceed to`, `perform`, `insert`, `remove the`, `increase the drip`, `decrease the drip`, `titrate to`, `shock`, `defibrillate`, `cardiovert now`

**Note:** Observational mentions of actions already underway (`Noted: epi given`) are allowed only when clearly descriptive of past/observed state, not instructing the team. Prefer `Noted: epi already given` over any form that could be heard as an order.

### 4.2 Banned certainty / authority phrases

`definitely`, `certainly`, `obviously`, `this is`, `diagnosis is`, `patient has`, `rule out complete`, `ignore other causes`, `guaranteed`, `always`, `never miss`, `must be`, `proven`, `confirmed diagnosis`, `the correct next step is`, `I recommend you`, `Crisis Mirror recommends`, `AI recommends`

### 4.3 Banned automation-bias amplifiers

`trust this`, `follow the cue`, `override your plan`, `do what I say`, `skip assessment`, `no need to think`, single-option closers like `only treat as X`

### 4.4 Allowed pattern library (positive examples of shape)

- `Consider anaphylaxis — check airway?`
- `Check EtCO2 trend?`
- `Noted: refractory hypotension`
- `Diff includes PEA causes`
- `Also consider transfusion reaction`
- `Ref: airway card — review steps`

---

## 5. Length and modality limits

Aligned to product spine (**HUD ≤8 words**). Spoken limits below are **estimates** for working-memory load in crisis; validate in sim with faculty.

| Modality | Hard limit (v0.1) | Soft target | Notes |
|----------|-------------------|-------------|-------|
| **HUD / glanceable** | **≤8 words** | 4–7 words | Architecture diagram / V2 shared layers. No scrolling. |
| **Spoken / TTS** (if used) | **≤14 words** (**estimate**) | ≤10 words | Prefer same content as HUD; do not add orders in speech that HUD omitted. |
| **Earcon-only** | n/a text | — | Tone without text still needs a logged silent/label reason if it replaces a failed cue. |
| **Deep-research panel** | Not a crisis HUD cue | Citations required (Architect / deep-research path) | Any HUD one-liner distilled from deep research **still** obeys this standard. |

**Word count rule:** whitespace-separated tokens; hyphenated clinical terms count as one word (`EtCO2`, `PEA`). Punctuation does not add words.

---

## 6. Confidence and uncertainty handling

| Confidence band (assumed `confidence` ∈ [0,1]) | Wording expectation | Delivery expectation (see gate rules) |
|-----------------------------------------------|---------------------|----------------------------------------|
| High (e.g. ≥ threshold T_high) | Suggestive / check / noted OK | May deliver if all other gates pass |
| Mid | Prefer interrogative (`Check …?`) or `Diff includes …` | Deliver only if wording + consistency pass |
| Low / abstain | Do **not** invent hedge spam (`maybe possibly perhaps…`); prefer silence or vetted soft label | **Suppress** or **fallback_vetted_label** |

Numeric thresholds are owned by gate config (`safety-gate-rules.md`), not hard-coded here. Wording must not overclaim relative to confidence (e.g. no `Noted: anaphylaxis` at low confidence — use `Consider anaphylaxis?` or suppress).

---

## 7. Examples — good vs bad (sim crises)

Examples are **educational illustrations** for sim faculty review. They are not a clinical protocol pack and must not be treated as standing orders.

### 7.1 Suspected anaphylaxis (perioperative / ICU exposure)

| | Cue | Verdict |
|---|-----|---------|
| Bad | `Give epi 0.3 mg IM now` | Imperative + novel dose |
| Bad | `This is anaphylaxis` | False certainty |
| Good | `Consider anaphylaxis — check exposure?` | Suggestive + check |
| Good | `Noted: bronchospasm + hypotension` | Observational |

### 7.2 Malignant hyperthermia concern

| | Cue | Verdict |
|---|-----|---------|
| Bad | `Start dantrolene 2.5 mg/kg` | Dose order |
| Bad | `Definitely MH — treat now` | Certainty + directive |
| Good | `Check rising EtCO2 — MH?` | Interrogative |
| Good | `Ref: MH card — review steps` | Vetted reference frame |

### 7.3 Refractory hypotension (undifferentiated)

| | Cue | Verdict |
|---|-----|---------|
| Bad | `You must give fluids and pressors` | Stacked orders |
| Bad | `Ignore bleed — it's sepsis` | Narrowing + authority |
| Good | `Noted: refractory hypotension` | Observational |
| Good | `Diff includes bleed, pump, obstructive` | Widens differential (8 words) |

### 7.4 Airway risk

| | Cue | Verdict |
|---|-----|---------|
| Bad | `Intubate immediately` | Directive |
| Good | `Check airway patency?` | Interrogative |
| Good | `Consider difficult airway cart` | Suggestive |

---

## 8. Regulatory framing note (short — defer to CC Regulatory & Privacy)

This wording standard is designed to **support advisory framing** (suggestions / checks / observations; no orders). **It does not by itself establish Non-Device CDS status** under the 21st Century Cures Act §3060 / FD&C Act §520(o)(1)(E) four-criterion test, and it is **not** a regulatory determination.

Verified citations for Regulatory to use (do not treat this section as the analysis):

1. **FDA**, *Clinical Decision Support Software — Guidance for Industry and Food and Drug Administration Staff*, final guidance issued **September 28, 2022** (interprets the four Non-Device CDS criteria). FDA guidance index: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software · PDF commonly at https://www.fda.gov/media/109618/download (note: that media URL currently serves the **January 29, 2026** superseding edition; Reg & Privacy should pin the edition used in their memo).
2. **21st Century Cures Act** §3060(a), adding FD&C Act §520(o)(1)(E) Non-Device CDS criteria (all four must be met). Summary of the four criteria as restated in secondary analyses of the Sept 2022 guidance (Goodwin, 17 Oct 2022): https://www.goodwinlaw.com/en/insights/publications/2022/10/10_17-fda-issues-final-clinical-decision

**Honest pointer for Regulatory (not a determination):** Secondary analyses of the Sept 2022 guidance describe FDA’s interpretation that software intended to support **time-critical** decision-making, or to provide a specific directive output, faces serious pressure under **Criterion 3** and **Criterion 4** (independent review of the basis). Crisis Mirror’s **ambient, time-pressured ICU crisis cues** are therefore assumed **sim-only research** until Regulatory completes review — this standard only keeps language advisory.

**Owner of the full analysis:** CC Regulatory & Privacy. Sim-lab first remains product law (`README.md` / V2 shared layers).

---

## 9. Relationship to other owners

| Artifact | Owner |
|----------|-------|
| Cue pipeline schema, SystemOneClient, gate I/O types | CC Architect |
| Safety gate **rules** + wording lint | Clinical Safety & Evaluation (this pod) |
| Gold-nudge **data schema** (points at this rubric) | Clinical Models Lead |
| FDA / privacy / non-device CDS memo | CC Regulatory & Privacy |
| Faculty approval of vetted labels / scenario packs | Sim faculty + Sergio |

---

## 10. Change control

- Version bumps require clinician or sim-faculty review before any non-draft merge.
- Banned-list and length limits may tighten without loosening without faculty sign-off.
- Nothing in this file authorizes bedside clinical deployment.

---

## 11. Verified sources used in this doc

| Source | Year | URL |
|--------|------|-----|
| FDA CDS Software guidance landing page (current edition noted Jan 2026; Sept 2022 final historically issued) | 2022 / 2026 | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software |
| Goodwin summary of FDA Sept 28, 2022 CDS final guidance (four criteria; time-critical / Criterion 3–4 discussion) | 2022 | https://www.goodwinlaw.com/en/insights/publications/2022/10/10_17-fda-issues-final-clinical-decision |
| Crisis Mirror V2 shared layers (cue ≤8 words; gate + wording check; advisory-only) | 2026 | `docs/architecture/V2-shared-layers.md` @ d0d101f |
