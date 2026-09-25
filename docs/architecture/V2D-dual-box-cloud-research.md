# V2D — Dual-box + non-PHI cloud research lane

**V2D** = **Hybrid dual-box** (DGX Spark + Mac Studio over LAN) **plus** an optional **high-end cloud research** path for deeper literature / protocol / educational queries.

It is **not** a fourth full speech stack. Speech + System One + MedGemma cues stay on the local boxes (same shared spine as V2A / V2B / Hybrid). The cloud lane is **only** for clinician-triggered deep research after a **local** non-PHI gate.

## What V2D adds

| Piece | Where | Role |
|-------|--------|------|
| DGX Spark | On-prem | Speech (Parakeet + Nemotron-3) · NanoJev · NeMo T1/T3 · optional mid local research |
| Mac Studio | On-prem | MedGemma 27B · local RAG · **non-PHI classifier** · egress strip · HUD / panel |
| **Frontier cloud model (slot)** | Via **gateway only** | Swappable: a frontier cloud model with **zero-data-retention enterprise tier** (e.g. OpenAI or Anthropic), **selected at implementation time** |

## Hard rules (non-negotiable)

1. **Cloud never sees PHI.** Only questions the local system has classified as **non-PHI** (general medical knowledge, protocol lookups, educational queries).
2. **Strip identifiers before egress.** Patient names, MRNs, ages that identify, unit/bed, dates that identify, free-text that still contains identifiers — all removed on-box.
3. **Classify on the Mac Studio before egress.** The classifier runs **locally**; when in doubt → **keep on-box** (local RAG only). Conservative bias is required.
4. **Gateway with zero data retention.** Route through a gateway (e.g. **Vercel AI Gateway** or **Cloudflare**) so **API keys never live on the Spark or Mac**. The **cloud model is a swappable slot**: a frontier cloud model with **zero-data-retention enterprise tier** (e.g. OpenAI or Anthropic), **selected at implementation time** — not locked in the architecture. Boxes call the gateway; the gateway holds provider credentials.
5. **On-demand only.** Wake word or clinician button — **never automatic**. Same trigger contract as local deep research ("Hey Dr. Bellomo" placeholder / button).
6. **No continuous cloud decision stream.** System One (a–d), MedGemma cues, and the safety gate stay **local**. Cloud is research, not bedside routing.

## Flow (deep research only)

```
clinician wake/button
    → Mac Studio builds research question from room context
    → local non-PHI classifier (conservative)
         ├─ PHI / uncertain → local RAG only (never egress)
         └─ non-PHI → strip identifiers → gateway → **frontier cloud model (slot)**
              → optional curated evidence plugins (OE / UpToDate) if contracted
              → citations/panel back to clinician UI
```

Local RAG remains **primary** for anything that might touch the patient. Cloud is a **supplement** when the query is clearly general.

## Relationship to other variants

| Variant | Boxes | Deep research |
|---------|-------|----------------|
| **V2A** | Spark only | Local RAG (+ optional curated evidence later) |
| **V2B** | Mac only | Local RAG (+ optional curated evidence later) |
| **Hybrid** | Spark + Mac | Local RAG on Mac (+ optional curated evidence later) |
| **V2D** | Spark + Mac | Local RAG **+** gated non-PHI **frontier cloud model (slot)** via zero-retention gateway |

### Optional curated evidence (not defaults)

**OpenEvidence** and **UpToDate** (or similar) may be **plugged in behind** the frontier cloud model once **enterprise agreements** are in place. Neither is a default; neither is required for V2D. Treat them as optional evidence sources behind the same wake/button + non-PHI gate, not as the named cloud model.

## Open decisions specific to V2D

- Classifier model / ruleset ownership and eval (false-negative PHI leak = fail closed)
- Gateway choice (Vercel AI Gateway vs Cloudflare vs other) and logging policy (must be zero retention for prompts/completions)
- **Which frontier enterprise model fills the slot** (chosen at implementation; architecture stays provider-agnostic)
- Whether to add OpenEvidence / UpToDate (or neither) once contracts exist — **opt-in plugins, not defaults**
- Audit log of “egress denied” vs “egress allowed” without storing PHI

## See also

- [`V2-hybrid.md`](./V2-hybrid.md) — dual-box LAN split  
- [`V2-shared-layers.md`](./V2-shared-layers.md) — shared spine + deep research framing  
- [`V2-hardware-options.md`](./V2-hardware-options.md) — Spark / Mac / Hybrid table  
- [`crisis-mirror-architecture.html`](../../crisis-mirror-architecture.html) — diagram includes V2D cloud branch after classifier  
