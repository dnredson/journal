# Context & Retrieval Quality — evidence and scope audit

Status: first **qualitative draft**, not a census or the final coded synthesis.
Article target: `sections/06_quality_dimensions.tex` (Context and Retrieval Quality subsection).

## Peer-reviewed works used

| BibTeX key | Version of record | Claim/evidence used | Classification caution |
|---|---|---|---|
| `es2024ragas` | [EACL 2024 System Demonstrations](https://aclanthology.org/2024.eacl-demo.16/) | Reference-free evaluation of RAG context and generation dimensions | Metric suite ≠ experimentally established causal attribution |
| `saadfalcon2024ares` | [NAACL 2024 Long Papers](https://aclanthology.org/2024.naacl-long.20/) | Context relevance, answer faithfulness, answer relevance; synthetic supervision + small human-labelled set, PPI | Evaluator calibration is substantive; dimensions still require interpretation |
| `ru2024ragchecker` | [NeurIPS 2024 Datasets & Benchmarks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/27245589131d17368cccdfa990cbf16e-Abstract-Datasets_and_Benchmarks_Track.html) | Fine-grained retrieval and generation diagnosis, eight RAG systems, human meta-evaluation | Diagnostic labels do not automatically constitute causal experimental interventions |
| `cho2026graphene` | [RSC Advances 2026](https://doi.org/10.1039/D5RA09726F) | Compared RAGAS, BERTScore, LLM-as-a-Judge and human experts on 20 graphene-synthesis questions | Domain-specific evaluation; do not generalize evaluator superiority or score scales |
| `neloy2026metarag` | [Canadian AI 2026 / PMLR 318](https://proceedings.mlr.press/v318/neloy26a.html) | Twenty RAG evaluators on 200 shared samples; median pairwise Pearson r=0.21 | Substantial disagreement may indicate different measured constructs, not all raters wrong |
| `knollmeyer2026rag` | [SN Computer Science 2026](https://doi.org/10.1007/s42979-026-05134-x) | Systematic secondary synthesis of 12 RAG-evaluation studies, proposed framework | Secondary-study evidence; conceptual integration ≠ empirical validation |
| `wu2026ragsurvey` | [Artificial Intelligence Review 2026](https://doi.org/10.1007/s10462-026-11605-7) | RAG retrieval, generation, end-to-end robustness and operational efficiency taxonomy | A strong prior RAG-specific survey; novelty must not be overstated |
| `garcialopez2026reliabilityrag` | [Computers 2026](https://doi.org/10.3390/computers15090564) | Reliability-aware RAG architecture proposes joint reliability assessment | Mark **proposed** unless paper-specific execution evidence validates design |

## Eligibility and provenance

These are publisher/proceedings-verified peer-reviewed versions of record. The current passage is a **purposive narrative starting point** using known project papers and bibliographically checked research. It must not imply that all eight works have been de-duplicated against the original 12 blocks. The temporal update includes papers published after the May 25, 2026 historical cutoff.

**Important boundary test:** the influential `RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems` (Friel et al., arXiv:2407.11005) appeared as **preprint-only** in the bibliographic verification performed here. It is **not** added to the peer-reviewed academic-study synthesis or counted as a primary study. Neloy and Islam's peer-reviewed meta-analysis does use RAGBench examples, which is allowed: use of a preprint-origin dataset does not change the publication status of the peer-reviewed meta-analysis or of the underlying dataset.

## Rules for the final coding round

- Merely **using** a retriever or RAG = not sufficient for `Context/Retrieval Quality=Yes`.
- Answer correctness without retrieval evidence = can be **black-box pipeline evaluation**, not retrieval-quality measurement.
- Context relevance, context sufficiency/coverage, answer faithfulness and answer correctness are not synonyms.
- Side-by-side retrieval and output metrics ≠ directly measuring their **relationship**.
- LLM judges are an **evaluation method**; judge quality is a **meta-level target** only when reliability, bias, calibration, consistency or agreement is explicitly measured.
- For reviews/conceptual papers, record `used/proposed/discussed` rather than inferring empirical integration from taxonomy breadth.
- Do **not** claim RAG literature lacks cross-stage links, diagnostic tools, operational topics or judge validation: there is clear prior art in all these areas.
- Do not infer counts or prevalence until the peer-review gate and blind human validation are complete.

## Editorial issue

The comparison table is illustrative. Later decide whether to consolidate dimension-specific tables into one master table to keep the manuscript near the 30-page budget; references alone may require more space than estimated.
