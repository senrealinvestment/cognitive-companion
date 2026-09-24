# V2-HYBRID — Spark + Mac as networked services

Mac and Spark **cannot pool memory**. ConnectX-7 linking is **Spark↔Spark only**. Hybrid = **service split over LAN**.

## Example split
| Machine | Owns |
|---------|------|
| **DGX Spark** | Speech (Parakeet + Nemotron-3) · NanoJev · NeMo T1/T3 training · optional mid research |
| **Mac Studio** | MedGemma 27B · local research LLM + literature index · T2 training · HUD composition / clinician panel |

## Costs of hybrid
- LAN latency (chunk audio / RPC for decisions / RAG)  
- Auth + **TLS** between boxes  
- **Two OSes** to patch (DGX OS Arm + macOS)  
- Failover policy if one box dies  
- Still: no continuous **cloud** streaming for decisions  

## When to use
Want CUDA speech/train **and** Mac-scale RAG without forcing NanoJev onto MLX or NeMo onto Mac.

Shared product layers remain identical ([`V2-shared-layers.md`](./V2-shared-layers.md)).

## Local medical reasoning models
Catalog (benchmarks, licenses, Spark/Mac fit, shortlist): [`V2-local-medical-reasoning-models.md`](./V2-local-medical-reasoning-models.md).
