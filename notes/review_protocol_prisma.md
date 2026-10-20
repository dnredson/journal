# Survey selection protocol — SMS / PRISMA 2020 / PRISMA-S

Status: **working protocol and audit plan**. This is not a claim that final screening was completed.

## Study design

The review is a **Systematic Mapping Study** following Petersen, Vakkalanka and Kuzniarz (2015, DOI 10.1016/j.infsof.2015.03.007), with evidence-based narrative synthesis. Mapping is appropriate for classifying a broad field across dimensions, methods, and research gaps. We follow **PRISMA 2020** (Page et al. 2021, DOI 10.1136/bmj.n71) for transparent reporting of identification, screening, eligibility and inclusion and **PRISMA-S** (Rethlefsen et al. 2021, DOI 10.1186/s13643-020-01542-z) for reporting exact searches. PRISMA and PRISMA-S are *reporting guidelines*, not methods that themselves conduct the review.

## Known retrieval data

Historical cutoff: **25 May 2026**. The original archive recorded **2,662 records**, **2,561 globally distinct PDF SHA-1 hashes** and **60,858 pages** across twelve blocks.

| Block | Documented broad topic | Records | Distinct PDF hashes in block |
|---|---|---:|---:|
| B1 | Prompt quality/optimization | 158 | 154 |
| B2 | Answer quality | 229 | 222 |
| B3 | LLM-as-a-Judge/reliability | 218 | 209 |
| B4 | Sensitivity/robustness | 193 | 181 |
| B5 | Surveys and reviews | 259 | 254 |
| B6 | Decomposition | 185 | 179 |
| B7 | Multi-agent | 216 | 210 |
| B8 | Cost/latency | 326 | 318 |
| B9 | Frameworks/benchmarks | 235 | 218 |
| B10 | Evaluation tools | 194 | 185 |
| B11 | Domain-specific studies | 365 | 358 |
| B12 | Agent-to-Agent interoperability | 84 | 83 |
| **Total** | | **2,662** | **2,561 globally distinct PDFs** |

Prior automated screen: **Core 2,033; Adjacent 407; Exclude 222; Needs Review 1,044**. These are **provisional, pre-peer-review-gate classifications**, NOT final accepted academic studies and not PRISMA inclusion counts. Distinct PDF hashes are not necessarily distinct *studies*. Differing versions and uploads can have different hashes; per-block PDF counts should not be added to obtain the global count.

## Search strings, keywords, dates, and databases

The **exact executed queries, platforms, execution dates, per-query export logs, and limits are not currently verified**. Do not invent them. Prior conversations mentioned Google Scholar and complementary publisher searches, but full platform-by-block provenance needs the original scripts, search logs, saved exports or metadata.

Proposed **keyword families for reconstructing/documenting** the searches (not claims about historical literal queries):
- LLM terms: large language model, LLM, foundation model, generative AI.
- Evaluation terms: evaluation, assessment, benchmark, metric, quality, reliability, validation.
- Lifecycle: prompt, instruction, specification; retrieval, RAG, grounding; response, factuality, hallucination; dialogue, memory, multi-turn; agent, tool, trajectory, planning; latency, throughput, cost, energy, availability.
- Evaluation reliability: LLM-as-a-Judge, evaluator, calibration, agreement, bias, multi-judge.
- Integration: end-to-end, lifecycle, holistic, cross-stage, integrated.

**Illustrative only, not necessarily executed:** 
("large language model" OR LLM OR "generative AI") AND (evaluat* OR benchmark* OR metric* OR quality) AND (prompt OR retrieval OR trajectory OR latency OR "end-to-end").

The definitive search log should capture: query ID, block, database, platform, exact query, time/date, date range, language, fields, limits, records exported, export path, and notes. Include temporal-update searches beginning May 26 2026 and any separately logged supplementary discovery.

## Reproducible selection flow

1. **Identify** source records in historical blocks, temporal update, snowballing and other sources; preserve IDs, source query and retrieval date.
2. **Deduplicate at study level**, not only by PDF hash. Use DOI, normalized title/authors/year, venue, version links, and hash; retain peer-reviewed version of record as canonical when available.
3. **Verify publication status** independently of topic relevance: peer-reviewed journal/conference/workshop; preprint-only; grey literature; uncertain; non-archival. A preprint with a verified peer-reviewed publication remains eligible as the canonical journal/conference record.
4. **Screen title/abstract** for LLM-system evaluation: Core, Adjacent or Exclude; uncertain cases require full-text review.
5. **Assess full text and extract evidence** for actual measurement of a quality dimension, evaluator validation, multi-stage relations, and whether a method is used/proposed/discussed. Architecture alone does not imply an evaluated property.
6. **Finalize inclusion** of *unique peer-reviewed Core studies* for the primary evidence map; keep surveys in the secondary-study track, Adjacent separately and practice/grey evidence outside the primary denominator.

**Exclusive primary exclusion reason codes** (secondary flags permitted): duplicate study/version; no peer-reviewed version; unresolved publication status; not LLM-based evaluation; external domain object only; no substantive LLM-quality evaluation; ineligible publication format; full text unavailable/insufficient; other with recorded rationale. Do not count one record in two mutually exclusive exclusion boxes. Duplicates removed before screening should not recur among full-text exclusions.

**Peer-review is a gate, not a quality score.** A peer-reviewed paper can still be excluded for topical irrelevance. A technically relevant preprint without confirmed peer-review may be recorded as grey literature but must not enter the primary academic synthesis denominator. A review can be cited as related work without being counted as another empirical experiment.

## Extraction schema

For every candidate, maintain study ID, source record IDs, PDF hash, DOI, bibliographic version/venue, publication status and evidence URL; source blocks, queries and duplicate linkages; screening decision, primary exclusion reason, reviewers, disagreement/adjudication, confidence, supporting page quotes; study type, Core/Adjacent/Exclude; evaluation object; six lifecycle dimensions and evaluator meta-evaluation; methods/protocols; integration category and used/proposed/discussed; experimental regimes and operational measures.

Human calibration was designed as three 40-paper review batteries, with 20 shared papers and 20 unique per battery (80 distinct overall). Do **not** state that all raters completed these, nor invent Krippendorff alpha or agreement estimates. Report results only after verified independent decisions and adjudication.

## PRISMA stage-count ledger: placeholders, not results

| Stage | Confirmed or TBD |
|---|---|
| Historical records retrieved | 2,662 |
| Temporal-update/supplementary records | TBD |
| Duplicate *studies* removed | TBD |
| Records screened title/abstract | TBD |
| Records excluded at initial screen | TBD |
| Full texts sought / not retrieved | TBD / TBD |
| Full texts assessed for eligibility | TBD |
| Full texts excluded by exclusive reason | TBD |
| Unique peer-reviewed Core studies included | **TBD** |
| Surveys/secondary, Adjacent, tools/grey | Report separately |

The chart should balance only after reconciliation of records/reports/studies. **Never use 2,033 preliminary Core labels as the final study count.**

## 30-page manuscript plan

Use approximately 2–3 pages for the core methodological narrative, one adapted PRISMA diagram, and a compact inclusion-criteria table. Put all original search strings, database dates, raw decision ledger, publication verification, full paper-level classification and validation details in online supplementary materials. Do not claim prospective registration or blinded double screening if not actually performed.

**Next action:** recover master cross-block dataset and original search/exports, reconcile DOI/title/hash study identities, apply publication and relevance gates, adjudicate ambiguous records, then calculate the defensible final number.
