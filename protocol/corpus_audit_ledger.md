# Corpus audit execution ledger

This document describes **checks that must be run**, not checks already completed. The historical spreadsheet's indexed summary contains 12 blocks and 2,662 records, 2,561 unique PDF hashes, 2,033 Core / 407 Adjacent / 222 Exclude labels. Flags: needs-review 1,044, semantic-review 345, extraction-flag 597. Flags overlap categories and MUST NOT be added to exclusion counts.

## Evidence currently accessible
The consolidated file \`PQI_controle_classificacao_blocos_10_12.xlsx\` was located in Project files and its summary indexed, but the underlying workbook could not be materialized for row-wise analysis in this environment. Consequently, no per-record DOI/title check, venue verification, human eligibility adjudication, or final count has been executed here.

## Historical block audit table

| Block | Records | Unique PDF hashes | Core | Adjacent | Exclude | Needs review | Semantic review | Extraction flag |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 158 | 154 | 98 | 58 | 2 | 69 | 0 | 0 |
| 2 | 229 | 222 | 185 | 41 | 3 | 141 | 0 | 0 |
| 3 | 218 | 209 | 179 | 26 | 13 | 60 | 30 | 34 |
| 4 | 193 | 181 | 168 | 17 | 8 | 58 | 21 | 44 |
| 5 | 259 | 254 | 208 | 48 | 3 | 141 | 71 | 91 |
| 6 | 185 | 179 | 134 | 39 | 12 | 100 | 60 | 60 |
| 7 | 216 | 210 | 198 | 14 | 4 | 62 | 17 | 53 |
| 8 | 326 | 318 | 255 | 59 | 12 | 144 | 56 | 107 |
| 9 | 235 | 218 | 199 | 22 | 14 | 73 | 27 | 53 |
| 10 | 194 | 185 | 91 | 13 | 90 | 54 | 9 | 51 |
| 11 | 365 | 358 | 284 | 52 | 29 | 128 | 54 | 90 |
| 12 | 84 | 83 | 34 | 18 | 32 | 14 | 0 | 14 |
| **Reported total** | **2662** | **2561** | **2033** | **407** | **222** | **1044** | **345** | **597** |

Audit cross-check: the twelve per-block unique-file counts sum to **2,571**, whereas the consolidated global unique count is **2,561** (difference: **10**). This is compatible with files repeated across different blocks, but requires hash-level confirmation. Summed per-block unique hashes are not global unique-file counts. Compare global SHA-1 and metadata deduplication separately. The above per-block figures reflect the indexed spreadsheet summary and should be compared with source row data before publication.

## Validation checklist
- [ ] Recover exact source database, query string and search date for each original block.
- [ ] Export one row per retrieved record (stable source ID, title, DOI, arXiv ID, authors, year, venue, PDF hash, block, preliminary flags).
- [ ] Reconcile cross-block hashes, DOI normalization, title/author variants, and preprint vs version-of-record.
- [ ] Verify peer-reviewed publication status against venue or publisher; record source of verification.
- [ ] Audit all needs-review and extraction-flag records without confusing overlapping flags.
- [ ] Complete blind human screening and adjudication; report agreement.
- [ ] Run and timestamp temporal search update for publications after 2026-05-25.
- [ ] Freeze the study-level inclusion ledger and calculate PRISMA/PRISMA-S counts from source rows only.

## Publication safeguard
Never report the preliminary thematic labels as final included studies, and never subtract 2,662 - 2,561 to conclude there are only 101 duplicate *studies*. A PDF hash deduplicates byte-identical files; distinct PDFs can refer to the same publication.
