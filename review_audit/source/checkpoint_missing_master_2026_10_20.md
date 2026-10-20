# Corpus availability checkpoint — 2026-10-20

## What was verified in this iteration

- Searched available Project/Library files for the complete PQI individual-record corpus; the only relevant source is `PQI_controle_classificacao_blocos_10_12.xlsx`.
- The other similarly named `consolidated_results_v2.xlsx` and `consolidated_results_v3.xlsx` contain experiment summaries, **not** the 2,662-record PQI screening corpus.
- Checked the root of the connected `dnredson/journal` GitHub repository: it contains the manuscript, `protocol/` and `review_audit/`, **not** the original 2,662-row bibliography or original PDF archive.
- Historic Block 12 rows 0–83 were already registered in operational rounds 17–25. There are no new indexed Block 12 rows to screen.
- Unavailable per-record rows: historic blocks 1–9 (all), block 10 rows 120–193 (74), block 11 rows 121–364 (244). Even existing indexed rows have mostly title-level evidence only.

## Decision

**Do not invent rounds 26–30.** Source metadata for the next five independent batches is absent. Further automation from abstracts or filenames alone would be an unsupported claim of full scientific review.

## Inputs needed

1. Master spreadsheet/CSV: 2,662 source records, source order, original block, filename, title, abstract, DOI, venue, author/year, provenance and PDF SHA-1.
2. Source PDFs for at least all candidate and uncertain studies.
3. Original search block query logs (database, Boolean string, date and export file).
4. Coauthor IDs and external AI model details when independent validation is commissioned.

## Planned continuation

Once full source rows are accessible:
- Reconcile study IDs, source duplicates and version-of-record.
- Freeze fifty source-order batches and create their blinded reviewer copies.
- Release rounds 26–30 as **separate evidence-backed CSVs**; track whether each record received metadata, abstract or full-text review.
- Keep original automated labels and assistant decisions hidden from independent coauthors/AI until adjudication.
- Record eligibility and PRISMA counts only from adjudicated study-level data.

**Current count:** 325 source records provisionally logged in operational rounds 1–25. No new documents were reviewed in this checkpoint.
