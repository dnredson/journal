# PQI survey — independent validation workspace

Status: **in progress**. This directory is the canonical review workspace. Other legacy `protocol/` documents remain as historical context, not as the validation dataset.

## Directory conventions
- `source/`: source inventory and provenance; **historical automated labels are not reviewer input**.
- `batches/`: 50 stable screening batches, once the complete 2,662-row source table is obtained. Partition by deterministic `source_order` (38 batches of 53 and 12 of 54). Never silently reorder rows after IDs are minted.
- `assistant/`: initial coding and evidence, with all conclusions marked provisional until independently adjudicated.
- `validation/human/`: individual human reviewers' blinded decisions; one file per reviewer per batch.
- `validation/ai/`: independent second AI's predictions; model/prompt/version recorded.
- `adjudication/`: disagreements, reasons, resolution, and final consensus records.
- `reports/`: PRISMA and agreement statistics generated **only** from reconciled decisions.

## Workflow
1. Recover complete source rows and bibliographic identifiers.
2. Mint stable study and record IDs. One paper can have multiple source records or PDFs.
3. Produce a blind input CSV for each batch (bibliographic facts and abstract; no old class labels, assistant or other reviewer judgments).
4. Initial assistant classification must distinguish title/abstract screening from full-text eligibility; store source pages and citations.
5. Coauthors and second AI read the same blind data independently; AI runs must document model, system prompt hash, timestamp, and decoding configuration.
6. Adjudicate disagreements. Verify publication status and version of record; maintain reasons, and never assume a preprint is peer reviewed.
7. Compute human–human agreement separately from human–AI comparison; count a study only once.
8. Finalize PRISMA stage counts from the actual selection ledger; no final N before that.

**Current limitation:** project-indexed historical workbook is readable in excerpts but its raw file could not be materialized, and it only exposes individual records for original blocks 10–12. The 50 batch files cannot responsibly be populated before full master-row access. An initial seven-record pilot from original block 10 is archived in `assistant/`.
