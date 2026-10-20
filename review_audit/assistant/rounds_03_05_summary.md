# Operational rounds 03–05 — 2026-10-20

Three independent title/metadata-screening batches were added:

- `round03_block10_rows_068_082.csv`: 15 source records.
- `round04_block10_rows_083_097.csv`: 15 source records.
- `round05_block10_rows_098_112.csv`: 15 source records.

These are **operational mini-batches**, NOT three of the planned canonical 50 partitions of all 2,662 records. All belong to **historical source Block 10**. Do not add these counts to original source block totals.

## Counts (not final eligibility)
| Batch | Core candidates | Adjacent | Uncertain | Exclude | Exact file duplicate | Potential study duplicate | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Round 03 | 6 | 0 | 2 | 7 | 0 | 0 | 15 |
| Round 04 | 6 | 0 | 3 | 4 | 1 | 1 | 15 |
| Round 05 | 2 | 1 | 3 | 9 | 0 | 0 | 15 |
| **Total** | **14** | **1** | **8** | **20** | **1** | **1** | **45** |

## Duplicate audit
- Rows 83 and 84, *An Iterative Self-Correcting Agentic RAG System*: identical SHA-1 `62eb450867c738f552f4720c68e67fd2147145e1`; one PDF duplicated, retain both source provenance records.
- Rows 88 and 89, *High-Performance Durable LLM Observability at Scale...*: same extracted title, **different** SHA-1 (`809fcb7758d3e8ea848df63e9f05693d243fc2f7` vs `a54881ebf8d2414fcf25f50b3fdaa03c39d5c334`); probable bibliographic/version duplicate requiring verification, not an identical-file duplicate.

## Limits and actions
The indexed spreadsheet supplied titles, source filenames and hashes; independent full-PDF verification and exhaustive venue review have **not** been completed for these 45 records. Screening is provisional. Title-only exclusions should be checked against the full record where ambiguous. Peer-review verification is pending across retained candidates; an original master's thesis is not peer-reviewed primary evidence by itself.

For external validation, blind reviewers must receive neutral source metadata, **not** the assistant-coded CSV. The original corpus's 50 stable batches still require the full master-table export.
