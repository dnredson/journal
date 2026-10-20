# Operational / System Quality — evidence provenance and coding safeguards

Status: **first critical qualitative synthesis**, not full-corpus prevalence analysis. Source: sections/06_quality_dimensions.tex, Operational and System Quality subsection.

| BibTeX key | Peer-reviewed version | What the study evaluates | Caveat |
|---|---|---|---|
| kwon2023vllm | [ACM SOSP 2023](https://doi.org/10.1145/3600006.3613165) | KV-cache fragmentation, batching, serving throughput at comparable latency; reported 2–4x throughput | Serving improvement is not independent semantic-quality evidence |
| agrawal2024sarathi | [USENIX OSDI 2024](https://www.usenix.org/conference/osdi24/presentation/agrawal) | Prefill/decoding scheduling, throughput-tail-latency tradeoff, capacity | Stages are serving *phases*, not all quality lifecycle dimensions |
| zhong2024distserve | [USENIX OSDI 2024](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) | TTFT and TPOT SLO constrained goodput; >90% compliance in reported experiments | Meeting latency SLO does not demonstrate uptime or availability |
| patel2024splitwise | [ISCA 2024 / Microsoft Research](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) | Throughput, resource specialization, power/cost tradeoffs | Phase-specific performance does not guarantee answer equivalence |
| zheng2024sglang | [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html) | LLM program runtimes, KV reuse, constrained decoding, application throughput; up to 6.4x | Task workloads are diverse, but runtime benchmark is not correctness evaluation |
| poddar2025energy | [NAACL 2025](https://aclanthology.org/2025.naacl-long.632/) | Inference energy vs output length, response time, prompt/model/batching choices | Energy efficiency and response quality must be coded separately |
| stojkovic2025dynamollm | [IEEE HPCA 2025](https://doi.org/10.1109/HPCA61900.2025.00102) | Energy/carbon/cost minimization subject to latency SLOs; reported 52% mean energy, 38% carbon, 61% cost improvements | Depends on hardware/workload/carbon modeling and experimental scope |

**Screening distinction:** all seven are peer-reviewed and directly measure properties of *LLM inference systems*; therefore they are defensible candidate **Core** articles under our definition, rather than Adjacent merely because their methods concern systems architecture. Their inclusion in the historical archive, duplicate identity, and final extraction confidence still require reconciliation. Operational quality labels require actual measurements, not mere suggestions for cheaper inference.

Additional cross-cutting distinctions:
- raw throughput vs **SLO-constrained goodput**; averages vs tail latency;
- TTFT vs TPOT vs end-to-end application latency;
- operational **reliability** (latency-satisfaction statistics) vs **availability** (up-time/service continuity);
- energy estimates vs measured power; per-query cost vs total cloud expense;
- deployment efficiency vs content correctness; batch and quantization changes may have quality implications, but those implications need actual measurements.

Privacy, safety and observability are in the broader operational taxonomy but were **not empirically established by this selected serving-focused sample**. Do not claim the full literature neglects these until the final Core corpus is coded.

**Separate review methodology change:** systematic mapping-study guidance, PRISMA 2020, and PRISMA-S citations have been added to sections/04_methodology.tex and notes/review_protocol_prisma.md. This is a protocol/reporting framework, not evidence that all screening and independent validation are complete.

**30-page budget:** this adds a sixth comparison table to the manuscript. Before layout freeze, consolidate representative tables or move detailed comparison rows into supplementary material.
