# V2 Hardware Options — Mac Studio vs DGX Spark vs Hybrid vs V2D

## OPEN DECISION (read first)
**Single box vs dual box?** Does **Spark replace or complement** the Mac?  
Recommendation to debate: **Hybrid complements** — Spark owns CUDA speech + NanoJev + NeMo training; Mac owns MedGemma 27B + large local research RAG. **V2D** = Hybrid **plus** a gated non-PHI cloud research lane (see [`V2D-dual-box-cloud-research.md`](./V2D-dual-box-cloud-research.md)). Or pick **one** stack (V2A or V2B) for Phase 1 sim simplicity.

---

## Verified DGX Spark (Sergio’s claims checked)

| Claim | Verdict | Source |
|-------|---------|--------|
| GB10 Grace Blackwell | **Correct** | [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/), [docs hardware](https://docs.nvidia.com/dgx/dgx-spark/hardware.html) |
| 128 GB unified LPDDR5X | **Correct** | same |
| Memory bandwidth ~273 GB/s | **Correct** (273 GB/s) | NVIDIA hardware overview |
| Up to 1 PFLOP FP4 | **Marketing = sparse FP4**; not dense FP4 | NVIDIA site / datasheets (footnote sparsity) |
| Models ~200B local; two units ~405B | **Vendor claim** (quantized); dual via **ConnectX-7** | NVIDIA datasheet |
| ConnectX linking | Spark↔Spark (NVIDIA also markets up to **4** Sparks for larger models) — **not** Mac↔Spark memory pool | NVIDIA product page |
| Size ~150×150×50 mm, 1.2 kg | **Correct** (150×150×50.5 mm) | NVIDIA specs |
| Price ~$4,000–4,700 | **Correct band** (~$3,999–$4,699; moved with DRAM supply) | [NVIDIA marketplace](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/), channel reports |
| DGX OS (Linux), full CUDA | **Correct** | docs |
| Power ~140–180 W with fans | **Mostly correct**: GB10 **TDP 140 W**; **240 W** external PSU; system components share remaining budget | NVIDIA hardware docs |

### Bandwidth vs Mac Studio
| | DGX Spark | Mac Studio M3 Ultra |
|--|-----------|---------------------|
| Unified memory | **128 GB** | **up to 512 GB** (new Store often **256 GB max** as of Mar 2026) |
| Bandwidth | **273 GB/s** | **819 GB/s** (~3× Spark) |
| Decode implication | Bandwidth-limited large-model decode | Better for large dense decode on one box |

Sources: NVIDIA Spark hardware; [Apple M3 Ultra / Mac Studio specs](https://support.apple.com/en-us/122211) (819 GB/s).

### Mac Studio power / noise (not silent)
- Max continuous power rating **480 W** ([Apple specs](https://www.apple.com/mac-studio/specs/))  
- Apple table: M3 Ultra 512 GB config **idle 9 W / max 270 W** wall ([Apple Support 102027](https://support.apple.com/en-us/102027))  
- Acoustic: **~7 dB** operator position idle/wireless web ([Apple Support AU 122211](https://support.apple.com/en-au/122211)) — **has fans**; quiet, **not literally silent**. Heavy LLM load reviews still report low fan noise.

---

## Comparison table — Mac 512 vs Spark vs both

| Dimension | **V2B Mac Studio (target 512 GB)** | **V2A DGX Spark** | **Hybrid (both)** | **V2D (Hybrid + cloud research)** |
|-------|------------------------------------|-------------------|-------------------|----------------------------------|
| Memory | 512 GB (procure used/stock if new max 256) | 128 GB | Separate pools — **cannot merge** | Same as Hybrid + cloud lane |
| Bandwidth | 819 GB/s | 273 GB/s | LAN between boxes | Same + gateway RTT for research |
| Stack | MLX / CoreML / MPS | **Full CUDA** + DGX OS | Service split over LAN | Hybrid + **gateway** cloud research |
| System One | **Laya** default | **NanoJev** native | Both, by service | Same (always local) |
| NeMo / V2A train | Awkward | **Native** | Spark does T1/T3 CUDA | Same as Hybrid |
| MedGemma 27B | Comfortable (+ RAG + research) | **Fits** (~14–54 GB) with speech | Prefer Mac for 27B+RAG | Same; Mac runs **non-PHI classifier** |
| Largest practical research | 70B–120B easy; 671B MoE Q4 possible but crowded | Mid: **70B 4-bit ~40 GB** + speech; dual-Spark 405B **slow** | Mac for big RAG; Spark for CUDA jobs | Local RAG **+** enterprise cloud (non-PHI only) |
| Decode speed | 27B 4-bit ~15–28 tok/s class (M3 Max proxies); measure Ultra | e.g. community: 70B NVFP4 ~5 tok/s; 120B ~27; dual 405B INT4 ~**1.8 tok/s** | LAN adds ms–tens of ms | Cloud research latency separate (opt-in) |
| Price | ~$9.5k launch 512 GB; used much higher; new often 256 GB | ~$4.0–4.7k | Sum + networking | Hybrid + gateway/API spend |
| Power | Idle ~9 W; max ~270 W (512 GB table); rated 480 W | SoC 140 W TDP; 240 W PSU | Both on UPS | Same |
| Size / noise | Desktop; fans, quiet | 1.2 kg SFF; fans | Two boxes | Same |
| OS / IT | macOS | DGX OS Linux Arm | **Two OSes** to patch | + gateway / enterprise cloud policy |

Decode cites: Level1Techs Spark first impressions table (community; treat as indicative).

---

## Is 128 GB enough? (Spark budget)

| Resident | Est. |
|----------|------|
| Parakeet + Nemotron-3 diar | ~1–2 GB |
| NanoJev 0.6B | ~1–2 GB |
| MedGemma **4B** 4-bit | ~3–5 GB |
| MedGemma **27B** 4-bit + KV | ~20–40 GB |
| Research 70B 4-bit | ~40–45 GB |
| gpt-oss-120b / Qwen3-235B-A22B MoE 4-bit | **fits memory-wise on paper** for weights alone on 128 GB if carefully quantized; **KV + concurrent speech + 27B compete** — usually **not** all at once |
| Training headroom | LoRA OK; full FT crowded |

**Conclusion:** One Spark handles **live stack + mid-size research** (e.g. speech + NanoJev + MedGemma 27B **or** 70B research, not every giant at once). Second Spark for >~120–200B class; dual-Spark 405B decode is **bandwidth/network limited and slow** (~low single-digit tok/s in community 405B run). **For large local literature research, Mac 512 is the better tool.**

---

## Power / noise / hospital suitability
**Neither is medical-grade (not IEC 60601).** Place in **sim control room / server closet**, not patient vicinity. Biomed electrical safety check, hospital IT approval, UPS, thermal. Sim lab: straightforward.

---

## Comparison caveat (full-stack V2A vs V2B)
Multiple variables differ (box, System One, ASR, training stack). **Outcome differences cannot be attributed to the speech layer alone.**  
**Recommendation:** run a **controlled speech bake-off** (both ASR stacks on the **same** box) before claiming speech superiority.

---

## OPEN DECISIONS
1. Single box (V2A **or** V2B) vs **hybrid dual box** vs **V2D** (Hybrid + gated cloud research)  
2. Does Spark **replace or complement** Mac?  
3. Mac 512 used vs 256 new vs wait  
4. Dual-Spark for 405B worth it given slow decode?  
5. V2D: gateway (Vercel AI Gateway vs Cloudflare), classifier eval, enterprise cloud model pick  
6. Plus prior: wake-word, OE BAA, corpus rights, gold nudges, Sortformer vs Nemotron-3 on Mac, etc.
