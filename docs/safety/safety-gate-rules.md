# Safety gate rules — Crisis Mirror cue delivery (v0.1)

**Status:** Draft for clinician / sim-faculty review. Not merged policy.  
**Owner:** Clinical Safety & Evaluation (gate **rules** only)  
**Does not own:** Gate I/O TypeScript/Python contracts, SystemOneClient adapter, cue pipeline schema — those are **CC Architect**.  
**Aligned to:** `docs/architecture/V2-shared-layers.md` (PR #1 / `v2-speech-layer-ab` @ d0d101f): MedGemma cue → **gate + wording check** → HUD; labels offline; no bedside self-update.  
**Companion:** [`advisory-wording-standard.md`](./advisory-wording-standard.md)

---

## 1. Design law

> **Fail closed.** When uncertain, inconsistent, poorly worded, or over-rate: **silence** or a **pre-vetted static label** — never invent a “better” free-form cue after a failed check.

This matches the product’s advisory-only spine and human-factors evidence that low-value alerts drive desensitization (see §8 citations).

---

## 2. Assumed interface (explicit — not authoritative)

Clinical Safety specifies **predicates**. The Architect owns names, types, and transport. Until reconciled, rules assume:

| ID | Assumed input field | Use in rules |
|----|---------------------|--------------|
| I1 | `request_id` (opaque) | Logging correlation |
| I2 | `session_id`, `revision` | Ordering / dedupe |
| I3 | `cue_text_hud` (string, may be empty) | Wording lint + length |
| I4 | `cue_text_spoken` (string, optional) | Wording lint + length |
| I5 | `confidence` ∈ [0,1] | Threshold |
| I6 | `scenario_family` or System One category (e.g. airway / circulation / metabolic / other) | Consistency + vetted-label key |
| I7 | `urgency` or equivalent (optional enum) | Timing / rate limits |
| I8 | `source` ∈ {medgemma, vetted_label, deep_research_summary, other} | Whether generation lint applies |
| I9 | `knowledge_hit` / structured claims (optional) | Hallucination / contraindication check against vetted set |
| I10 | `timestamps` (cue_ready_at, last_delivered_at, …) | Rate limit / timing |

| ID | Assumed output | Meaning |
|----|----------------|---------|
| O1 | `outcome: deliver` | Pass; deliver `cue_text_*` (or Architect-normalized form) |
| O2 | `outcome: fallback_vetted_label` | Replace with faculty-approved static string for family/urgency |
| O3 | `outcome: suppress` | Silence; no HUD/spoken crisis cue |
| O4 | `reasons: string[]` | Bounded policy codes only (never free-text model excuses) |
| O5 | `gate_latency_ms` | Observability |

**Prior art (non-binding):** `companion-next` Jev gate on branch `feat/companion-next-jev-gate-slice-2` already fail-closes to `silence` with bounded reason codes. Reuse the *ethos*, not the wire types, unless Architect adopts them.

List every drift from I*/O* in the Architect reconciliation checklist (PR description).

---

## 3. Deterministic check pipeline (ordered)

Run **all** checks that are cheap enough to always run; collect **every** failing reason code (no silent short-circuit that drops codes), then decide:

1. If any **hard-fail** code ∈ fail-closed set → `suppress` (or `fallback_vetted_label` only when §5 says fallback is safe).  
2. Else if only **soft** wording failures with a mapped vetted label → `fallback_vetted_label`.  
3. Else → `deliver`.

### Stage A — Schema / presence (Architect-validated; rule intent)

- Missing both HUD and spoken text → `suppress` / `reason: empty_cue`
- Unknown `scenario_family` when required → `suppress` / `unknown_family`
- Non-finite or out-of-range `confidence` → `suppress` / `invalid_confidence`

### Stage B — Wording lint (this standard)

Against [`advisory-wording-standard.md`](./advisory-wording-standard.md):

| Check | Fail code | Default action |
|-------|-----------|----------------|
| HUD word count > 8 | `hud_too_long` | fallback or suppress |
| Spoken word count > 14 (**estimate** limit) | `spoken_too_long` | fallback or suppress |
| Banned imperative/directive hit | `banned_imperative` | **suppress** (do not “soften” with regex rewrite in v0.1) |
| Banned certainty / authority hit | `banned_certainty` | **suppress** |
| Novel dosing pattern (number + unit + drug-like token) | `dosing_order` | **suppress** |
| Missing suggestive/interrogative/observational frame | `missing_advisory_frame` | fallback if label exists else suppress |
| Spoken adds clinical content absent from HUD | `speech_hud_mismatch` | suppress spoken or full suppress |

**v0.1 policy:** no automatic LLM rewrite after fail. Humans fix gold nudges offline; live path is deliver / fallback / suppress only.

### Stage C — Scenario / state consistency

| Check | Fail code | Default action |
|-------|-----------|----------------|
| Cue family ≠ System One selected family | `family_mismatch` | suppress |
| Cue asserts a specific diagnosis while family is `other` / unclear | `over_specific` | fallback or suppress |
| Deep-research one-liner without clinician opt-in flag | `deep_without_opt_in` | suppress |
| Duplicate of last delivered cue within refractory window | `duplicate_refractory` | suppress |

### Stage D — Contraindication / hallucination vs vetted knowledge

Assume a **vetted knowledge set** (checklists, emergency-manual items, faculty YAML) — not an open web browse mid-cue.

| Check | Fail code | Default action |
|-------|-----------|----------------|
| Cue claim not entailed by knowledge set ∪ transcript evidence | `unsupported_claim` | suppress |
| Cue conflicts with vetted contraindication rule for active context | `contraindication` | **suppress** |
| Citation-required path (deep) without citation IDs | `missing_citation` | suppress HUD distillation |

If knowledge set is unavailable → **fail closed** (`knowledge_unavailable` → suppress), do not skip Stage D.

### Stage E — Confidence threshold

Configurable `min_confidence_deliver` (starter **estimate:** `0.70`) and `min_confidence_fallback` (starter **estimate:** `0.50`):

- `confidence < min_confidence_fallback` → `suppress` / `confidence_below_fallback`
- `min_confidence_fallback ≤ confidence < min_confidence_deliver` → only `fallback_vetted_label` if mapped, else suppress
- else → continue

Exact numbers are **estimates** until sim calibration; label them as such in dashboards.

### Stage F — Rate limiting / alarm-fatigue suppression

Starter policy (**estimates** — tune in sim):

| Knob | Starter value (estimate) | Purpose |
|------|--------------------------|---------|
| `min_seconds_between_cues_same_session` | 45 | Refractory period |
| `max_cues_per_rolling_10_min` | 4 | Cap chatter |
| `max_cues_per_scenario_activation` | 3 | Per crisis episode |
| `suppress_if_team_verbalized_same_concern` | true (when detectable) | Avoid nagging |

Fail codes: `rate_limit_refractory`, `rate_limit_burst`, `rate_limit_scenario_cap`.

Human-factors rationale: Joint Commission SEA 50 and AHRQ PSNet alert-fatigue primer — excess low-value alerts desensitize (§8).

### Stage G — Timing rules

| Rule | Fail / hold code | Notes |
|------|------------------|-------|
| Cue ready but ASR/System One latency already exceeded fast-path budget | `stale_cue` | Prefer suppress over late wrong nudge; fast-path budget in V2 docs is **&lt;1–2 s estimate** end-to-end — Architect measures |
| Cue would interrupt during declared sterile/critical procedure window (sim flag) | `timing_hold` | Hold → suppress if window ends without refresh |
| Deep-research panel latency | n/a for auto HUD | Deep path is opt-in; do not auto-escalate to spoken crisis cue |

---

## 4. Decision table (summary)

| Condition | Outcome |
|-----------|---------|
| Hard safety fail (dosing, contraindication, banned imperative/certainty, knowledge unavailable, invalid confidence) | `suppress` |
| Soft length/frame fail **and** vetted label mapped | `fallback_vetted_label` |
| Soft fail **and** no label | `suppress` |
| Rate / refractory / duplicate / stale | `suppress` |
| All stages pass | `deliver` |

**Never:** deliver a second MedGemma sample after failure; never “best effort” partial banned phrase stripping in v0.1.

---

## 5. Vetted-label fallback behavior

1. Look up `vetted_labels[scenario_family][urgency_or_default]`.  
2. If found: deliver **exact** faculty string (already compliant with wording standard). Log `outcome=fallback_vetted_label`, `label_id`, original draft hash.  
3. If not found: `suppress`.  
4. Fallbacks **count toward rate limits** (they still consume attention).  
5. Label library changes require sim-faculty approval; not hot-edited by the model.

Gold-nudge **training schema** that teaches models toward these labels is owned by Clinical Models Lead (points at the wording rubric) — not defined here.

---

## 6. Logging requirements (every cue attempt)

Log a structured record (field names illustrative):

```text
request_id, session_id, revision,
outcome, reasons[],
source, scenario_family, confidence,
cue_text_hud_draft, cue_text_spoken_draft,
cue_text_delivered (nullable), label_id (nullable),
stage_fail_bitmap or per-stage pass/fail,
gate_latency_ms, policy_config_version,
timestamp
```

Rules:

- Retain drafts **and** delivered text for eval (helpful / accurate labels offline per ONEPAGER loop).
- No silent drops: attempts that suppress must still log.
- PHI: follow camera-free / audio policy owned by Regulatory & Privacy; this gate must not add identifiers into cue strings.
- Config version pin enables replay when banned lists change.

---

## 7. Failure modes that must fail closed

| Failure | Required behavior |
|---------|-------------------|
| Gate process crash / timeout | No cue (`suppress` equivalent); surface soft “companion unavailable” only if Architect defines a non-clinical status glyph |
| Knowledge set load failure | `suppress` |
| Wording linter unavailable | `suppress` (do not deliver unchecked generative text) |
| Ambiguous family tie / low confidence | `suppress` or vetted soft label only |
| Conflicting checks | `suppress` |
| Architect interface mismatch / unknown field | `suppress` + eng alert — do not guess |

---

## 8. Human-factors and cognitive-aid citations (verified)

| # | Source | Year | Why it informs these rules | URL |
|---|--------|------|----------------------------|-----|
| 1 | The Joint Commission, *Sentinel Event Alert* Issue 50: Medical device alarm safety in hospitals | 2013 (Apr 8) | Alarm fatigue / desensitization; excess alarms harm response | https://www.jointcommission.org/en-us/knowledge-library/newsletters/sentinel-event-alert/issue-50 · PDF mirror often cited: https://www.jointcommission.org/-/media/tjc/documents/resources/patient-safety-topics/sentinel-event/sea_50_alarms_4_26_16.pdf · AHRQ PSNet issue page: https://psnet.ahrq.gov/issue/medical-device-alarm-safety-hospitals |
| 2 | AHRQ PSNet Primer: *Alert Fatigue* | 2019 (last reviewed 2024 per page) | Low-value alerts → override/ignore; tier severity; reduce inconsequential alerts | https://psnet.ahrq.gov/primer/alert-fatigue |
| 3 | Arriaga AF et al., *Simulation-Based Trial of Surgical-Crisis Checklists*, N Engl J Med | 2013 | Crisis checklists in sim cut missed lifesaving steps (6% vs 23%); supports **vetted** cognitive aids over memory alone — not unconstrained generation | https://doi.org/10.1056/NEJMsa1204720 · https://pubmed.ncbi.nlm.nih.gov/23323901/ |
| 4 | Stanford Medicine, *Emergency Manual* (perioperative cognitive aids / crisis checklists) | ongoing (manual site) | Faculty-vetted emergency manuals as point-of-care cognitive aids; model for vetted-label content | https://emergencymanual.stanford.edu/ |

These sources justify: **rate limits**, **prefer vetted labels**, **silence over junk cues**, and **checklist-shaped reference framing** in the wording standard.

---

## 9. Machine-readable sketch (config + banned phrases)

Illustrative only — Architect may relocate paths / keys. Policy version must bump when this changes.

```yaml
# docs/safety/gate-config.v0.1.yaml  (sketch — not yet wired)
schema_version: "0.1"
policy_id: crisis-mirror-safety-gate
fail_closed: true
allow_llm_rewrite_on_fail: false

assumed_outcomes:
  - deliver
  - fallback_vetted_label
  - suppress

thresholds:
  # ESTIMATES — calibrate in sim; do not treat as validated clinical params
  min_confidence_deliver: 0.70
  min_confidence_fallback: 0.50

length:
  hud_max_words: 8
  spoken_max_words: 14  # estimate

rate_limit:
  min_seconds_between_cues_same_session: 45  # estimate
  max_cues_per_rolling_10_min: 4             # estimate
  max_cues_per_scenario_activation: 3        # estimate

timing:
  stale_cue_suppress: true
  # end_to_end_fast_path_ms target documented as <1000–2000 estimate in V2 shared layers

wording:
  standard_ref: docs/safety/advisory-wording-standard.md
  require_advisory_frame: true
  banned_phrases:
    - "give "
    - "administer"
    - "push "
    - "bolus"
    - "you must"
    - "you should"
    - "this is "
    - "diagnosis is"
    - "definitely"
    - "certainly"
    - "start dantrolene"
    - "give epi"
    - "intubate now"
    - "order "
    - "prescribe"
    - "AI recommends"
    - "Crisis Mirror recommends"
    - "trust this"
    - "the correct next step is"
  banned_regex:
    - '(?i)\\b\\d+(\\.\\d+)?\\s*(mg|mcg|µg|g|ml|mL|units?)(/kg)?\\b'
  allowed_frame_prefixes:
    - "Consider "
    - "Check "
    - "Confirm "
    - "Noted:"
    - "Diff includes "
    - "Also consider "
    - "Ref:"

fallback:
  on:
    - hud_too_long
    - spoken_too_long
    - missing_advisory_frame
  never_on:
    - banned_imperative
    - banned_certainty
    - dosing_order
    - contraindication
    - unsupported_claim
    - knowledge_unavailable
    - invalid_confidence

logging:
  required_fields:
    - request_id
    - outcome
    - reasons
    - confidence
    - scenario_family
    - cue_text_hud_draft
    - cue_text_delivered
    - label_id
    - policy_config_version
    - gate_latency_ms
```

```json
{
  "policy_id": "crisis-mirror-safety-gate",
  "schema_version": "0.1",
  "fail_closed": true,
  "banned_phrases": [
    "give ",
    "administer",
    "you must",
    "this is ",
    "definitely",
    "AI recommends",
    "intubate now"
  ],
  "outcomes": ["deliver", "fallback_vetted_label", "suppress"]
}
```

---

## 10. Open decisions for Sergio / sim faculty (with options)

### D1 — Generative MedGemma cue vs vetted-label-first

| Option | Tradeoff |
|--------|----------|
| **A. Generative + gate** (current V2 lean) | Flexible coverage; higher hallucinated-order risk; needs strong lint + fallback |
| **B. Vetted labels only in crisis HUD** | Strongest safety / Arriaga-aligned; less novel phrasing; catalog ownership heavy |
| **C. Hybrid:** labels for high-urgency; generative only for mid-urgency differentials | Complexity; clearest rate-limit story |

### D2 — After wording fail: suppress vs fallback vs (later) constrained rewrite

| Option | Tradeoff |
|--------|----------|
| **A. Suppress only** | Safest attention profile; more silence |
| **B. Fallback to vetted label** (v0.1 default when mapped) | Preserves cognitive aid value; still spends an alert token |
| **C. Deterministic template fill** (no LLM) | Middle ground; Architect effort; still not free-form |

### D3 — Confidence thresholds

| Option | Tradeoff |
|--------|----------|
| **A. Conservative** (e.g. deliver ≥0.85) | Fewer cues; more missed forces (**estimate**) |
| **B. Starter mid** (0.70 / 0.50 as in sketch) | Balance until labeled sim data exists |
| **C. Family-specific thresholds** | Better fit; more tuning + eval burden |

### D4 — Who approves vetted labels / scenario pack

| Option | Tradeoff |
|--------|----------|
| **A. Sim faculty committee** | Legitimacy; slower |
| **B. Sergio + one faculty champion** | Speed; bus factor |
| **C. Per-ICU specialty reviewers** | Best clinical fit; coordination cost |

---

## 11. Change control

- Draft PR only; **do not merge** without Sergio or his engineer + clinician/sim-faculty review.
- Rule tightening allowed; loosening banned lists or raising rate caps needs faculty sign-off.
- Architect interface changes must update §2 assumptions in the same change set.

---

*Crisis Mirror · Clinical Safety & Evaluation · sim-lab advisory cues only · not a medical device determination*
