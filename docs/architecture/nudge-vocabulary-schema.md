# Nudge vocabulary — paper schema (future database)

**What this is:** A plain-language design for the database that will one day replace the Excel spreadsheet (`nudge-category-vocabulary.xlsx`).  
**Who this is for:** Engineers and clinicians who need a shared picture of tables and fields before anyone writes code.  
**Reading level:** High-school plain English.

> **Do not build this database until the Mac Studio is on hand; this schema is the design to implement then.**
>
> Until then, keep using the spreadsheet as the seed list. This document is the plan on paper only.

This schema supports the traffic-light nudge system described in `docs/DOSSIER-plain-language.md` (see **The story so far** and **Nudge system**).

---

## Why a database later

The spreadsheet is fine for early drafts. A real product needs:

- **Versioning** — what the menu looked like on a given day  
- **Provenance** — who tagged what, and when  
- **Review trail** — who approved a change, and what they said  

That is what these tables are for.

---

## Color meanings (same as the dossier)

When a field says **priority_tier**, use these meanings (do not invent new ones):

| Value | Plain meaning |
|-------|----------------|
| **green** | Extremely important — escalate (**nudge now**) |
| **yellow** | Worth paying attention to (**watch**) |
| **red** | Less important — monitor only (**stay quiet**) |

---

## Table: `categories`

One row per nudge category (the “menu items” clinicians own).

| Field | Type (plain) | Meaning |
|-------|--------------|---------|
| `id` | unique id | Stable key for this category |
| `organ_system` | short text | Which organ tab it belongs to (for example: Neuro, Cardiac, Emergencies) |
| `name` | short text | Human-readable category name |
| `trigger_pattern_plain_text` | longer text | In everyday words: what room talk or situation should fire this category |
| `priority_tier` | one of: `red`, `yellow`, `green` | Traffic-light priority (see table above) |
| `auto_escalate` | true / false | If true, short-circuit to **green** (nudge now) when this pattern is detected |
| `status` | one of: `draft`, `reviewed`, `approved` | How far this row has gone through clinician review |
| `created_by` | id → `clinicians` (or student tagger) | Who first wrote this row |
| `reviewed_by` | id → `clinicians` (optional until reviewed) | Who last reviewed it |
| `created_at` | date-time | When it was created |
| `updated_at` | date-time | When it last changed |

---

## Table: `tagged_examples`

One row per labeled example — a piece of transcript or a mock scenario marked with a category tag. This is how students and clinicians teach the system offline.

| Field | Type (plain) | Meaning |
|-------|--------------|---------|
| `id` | unique id | Stable key for this example |
| `category_id` | id → `categories` | Which category this tag points to |
| `source` | text | Either a `transcript_id` (real/sim audio turned into text) **or** a `mock_scenario_id` (made-up teaching case) — store which kind and the id |
| `student_tagger_id` | id → person | Who applied the student-level tag (often one of the ~5–6 medical student filters) |
| `tag` | short text | The label applied (usually the category name or code) |
| `confidence` | number or low/medium/high | How sure the tagger was |
| `notes` | longer text (optional) | Free-form comments |
| `tagged_at` | date-time | When the tag was applied |

**Note on `source`:** On paper, treat it as “one of two kinds of pointer.” In a real database you may use two optional fields (`transcript_id`, `mock_scenario_id`) with a rule that exactly one is filled. Either shape is fine as long as provenance is clear.

---

## Table: `clinicians`

People who create, review, or approve vocabulary (investigators, panel members, assigned reviewers).

| Field | Type (plain) | Meaning |
|-------|--------------|---------|
| `id` | unique id | Stable key for this person |
| `name` | text | Display name |
| `role` | short text | For example: PI, co-investigator, panel reviewer, student tagger |

Student taggers may live in this same table with `role = student tagger`, or in a separate people table later. Keep one place for “who did this” so provenance stays simple.

---

## Table: `review_log`

An append-only history of clinician (or assigned reviewer) decisions on tagged examples. Do not overwrite old rows — add a new row when someone reviews again.

| Field | Type (plain) | Meaning |
|-------|--------------|---------|
| `id` | unique id | Stable key for this review event |
| `example_id` | id → `tagged_examples` | Which example was reviewed |
| `reviewer_id` | id → `clinicians` | Who reviewed it |
| `decision` | short text | For example: approve / reject / needs edit / escalate to panel |
| `comment` | longer text (optional) | Why they decided that |
| `reviewed_at` | date-time | When the review happened |

---

## How the tables connect (plain picture)

1. A **clinician** (or student) drafts a **category**.  
2. Students (and later clinicians) add **tagged examples** that point at that category.  
3. A reviewer writes a **review_log** row for each example they check.  
4. When a category is ready, its `status` moves from `draft` → `reviewed` → `approved`.

No bedside system should invent new categories on its own. Humans own the menu; the database only stores what they agreed.

---

## What this schema deliberately does *not* include yet

Keep out of scope until you implement on the Mac Studio:

- Exact database product (SQLite, Postgres, etc.)  
- API endpoints or UI screens  
- Encryption / backup details (those belong in a security design when hardware exists)  
- Automatic promotion of student tags to “approved” without a clinician review

---

## Related files

| File | Role |
|------|------|
| `docs/architecture/nudge-category-vocabulary.xlsx` | Current seed spreadsheet (use now) |
| `docs/DOSSIER-plain-language.md` | Plain-language project dossier + action checklist |
| This file | Paper schema for the future database |

---

**Reminder:** Do not build this database until the Mac Studio is on hand; this schema is the design to implement then.
