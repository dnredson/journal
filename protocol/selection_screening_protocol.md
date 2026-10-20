# Corpus screening and reproducibility protocol (working draft)

Status: **prospective audit protocol; not a retrospective claim about searches already executed**. Companion to `sections/04_methodology.tex`. Updated 2026-10-20.

## Design and reporting standards
- Systematic Mapping Study (Petersen et al. 2015) + qualitative evidence synthesis.
- Report identification, screening, eligibility, and inclusion under PRISMA 2020 (Page et al. 2021).
- Report full reproducible search strings, databases, filters, last-run dates and deduplication under PRISMA-S (Rethlefsen et al. 2021).
- Do **not** infer that PRISMA adherence proves unbiased selection or classifier validity.

## Frozen historical baseline (not final included studies)
Historical 12-block retrieval: 2,662 records; 2,561 distinct PDF files by SHA-1; 60,858 pages. Preliminary relevance labels: Core 2,033; Adjacent 407; Exclude 222. A separate needs-review flag applies to 1,044 records, and must **not** be added to the relevance categories. Historical cutoff 2026-05-25. Temporal update starts 2026-05-26 (allow overlap for indexing lag, then deduplicate). These values must not be presented as a completed PRISMA flow.

## Search reconstruction and updates
For each of the 12 historical blocks, recover **actual** database, exact executed string, execution date, filters, export format, harvested IDs and number retrieved from logs. **Do not fabricate historical database names or query strings.** Search updates may adapt syntax to each database and log each adaptation verbatim. Candidate query families to test and document prospectively:

- General: ("large language model*" OR LLM OR "generative AI") AND (evaluat* OR assess* OR metric* OR benchmark* OR quality)
- Input: (LLM OR "large language model*") AND ("prompt sensitivity" OR "prompt quality" OR "prompt optimization" OR "instruction quality")
- Retrieval: ("retrieval augmented generation" OR RAG) AND (evaluat* OR faithfulness OR "context relevance" OR "retrieval quality")
- Outputs: (LLM OR "large language model*") AND (factuality OR hallucination OR correctness OR "response quality") AND evaluat*
- Interaction: (LLM OR chatbot*) AND (multi-turn OR dialogue OR conversation OR memory) AND evaluat*
- Agents: ("LLM agent*" OR "agentic AI") AND (benchmark* OR evaluat* OR trajectory OR "tool use")
- System: ("LLM serving" OR "LLM inference" OR "generative AI system*") AND (latency OR throughput OR cost OR energy OR reliability) AND evaluat*
- Judges: ("LLM-as-a-Judge" OR "LLM judge*" OR "multi-judge") AND (agreement OR calibration OR bias OR robustness OR reliability)
- Integrated: (LLM OR "large language model*" OR RAG OR agentic) AND ("end-to-end evaluation" OR "holistic evaluation" OR "cross-stage quality" OR "system-level quality")
- Reviews: (LLM OR "large language model*" OR RAG OR agentic) AND (survey OR "systematic review" OR "mapping study") AND evaluation

These are **proposed** search templates. Record precision/recall pilots and any changes; do not retrospectively attribute them to the original corpus.

## Selection stages and reason codes
1. Import with immutable source record ID; preserve source-specific search block/query/date.
2. Reconcile DOI/arXiv IDs, normalized title, venue, year, authors; PDF hash only catches file duplicates. Maintain canonical study ID and all versions.
3. Publication gate: `PR_JOURNAL`, `PR_CONFERENCE`, `PR_WORKSHOP_VERIFIED`, `PREPRINT_ONLY`, `THESIS`, `REPORT`, `BOOK_OR_CHAPTER_UNVERIFIED`, `GREY`, `STATUS_UNVERIFIED`. A preprint with verified peer-reviewed version is eligible via the latter.
4. Title/abstract screening: Core / Adjacent / Exclude / Insufficient-information, each with independently recorded peer-review status. Use uncertainty rather than forcing binary decisions.
5. Full-text eligibility: substantively evaluates quality of an LLM or LLM-based system or relevant evaluator; independent validation/contribution must be identifiable. Record one **primary** exclusion reason and optional secondary reasons.
6. Split primary empirical/method evidence from peer-reviewed secondary studies; never count a review's cited experiments as independent validations.
7. Verify extraction evidence (page, passage, method, dataset, protocol) and adjudicate disagreements.
8. Freeze counts only after the above steps; report identified records, deduplicated records, screening exclusions, sought/not retrieved, assessed full texts, full-text exclusion reasons, and included *studies* separately from *reports*.

Recommended primary full-text reason codes: `NO_PEER_REVIEW`, `OUT_OF_SCOPE`, `NOT_LLM_QUALITY_OBJECT`, `NO_SUBSTANTIVE_EVALUATION`, `DUPLICATE_VERSION`, `FULL_TEXT_UNAVAILABLE`, `INSUFFICIENT_PUBLISHING_EVIDENCE`. Use a distinct `UNCERTAIN_PENDING_ADJUDICATION` queue, not a rejection shortcut.

## Extraction columns
`study_id,source_record_id,search_block,source_database,query_exact,search_date,doi,arxiv_id,title,authors,year,venue,version_of_record_url,pdf_sha1,publication_status,peer_review_evidence_url,study_type,screen_ta_label,screen_fulltext_label,exclusion_reason_primary,exclusion_reason_other,quality_dimensions,input_object,context_object,output_object,interaction_object,agent_trajectory_object,operational_object,evaluator_reliability_object,methods,protocols,benchmarks,datasets,models,evaluator_models,integration_level,integration_evidence_status,evidence_page,evidence_excerpt,annotator,adjudicator,confidence,notes`.

Quality dimensions are independent multi-label variables. An architecture containing retrieval, prompts or an LLM judge is NOT sufficient evidence that retrieval quality, input quality or judge reliability was evaluated. Integration levels: None; Cross-stage; Black-box end-to-end; Lifecycle-integrated. Independently distinguish proposed/discussed/empirically used integration.

## Human calibration and automated triage
Preserve the manuscript's three reviewer batteries: 40 records/reviewer; 20 shared across all three, plus 20 unique each (80 unique records overall). Report sampling method and strata; require blinded first-pass human decisions, uncertainty labels and documented adjudication. Analyze Krippendorff alpha for appropriately comparable nominal fields and binary agreement for multi-label fields. Automated Ollama/RAG-assisted suggestions must remain separated from human labels, with prompt/model/version and evidence logged. Do not claim inter-rater reliability until actually calculated.

## Outstanding audit requirements
- Recover the original exact 12-block executed searches and database provenance.
- Execute and log the temporal update.
- Reconcile bibliographic duplicates not caught by PDF SHA-1.
- Independently verify archival/peer-review status and canonical versions.
- Manually adjudicate flagged cases and run the human calibration.
- Populate an actual PRISMA flow from audit logs and determine final N.
