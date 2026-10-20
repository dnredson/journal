# Recovery of the original PQI screening corpus — 2026-10-20

**FOUND:** The user's supplied Google Drive folder contains all twelve original `pqi_screening_BlocoN.csv` files, matching JSONL files, and archives `Bloco1.zip` through `Bloco12.zip` plus supplemental ZIP parts. The 12 CSV files were read directly with the Google Drive connector.

## Verified source-row counts
| Historical block | Original rows | Recovered GitHub file |
|---|---:|---|
| 1 | 158 | [block_01_source.csv](original_screening/block_01_source.csv) |
| 2 | 229 | [block_02_source.csv](original_screening/block_02_source.csv) |
| 3 | 218 | [block_03_source.csv](original_screening/block_03_source.csv) |
| 4 | 193 | [block_04_source.csv](original_screening/block_04_source.csv) |
| 5 | 259 | [block_05_source.csv](original_screening/block_05_source.csv) |
| 6 | 185 | [block_06_source.csv](original_screening/block_06_source.csv) |
| 7 | 216 | [block_07_source.csv](original_screening/block_07_source.csv) |
| 8 | 326 | [block_08_source.csv](original_screening/block_08_source.csv) |
| 9 | 235 | [block_09_source.csv](original_screening/block_09_source.csv) |
| 10 | 194 | [block_10_source.csv](original_screening/block_10_source.csv) |
| 11 | 365 | [block_11_source.csv](original_screening/block_11_source.csv) |
| 12 | 84 | [block_12_source.csv](original_screening/block_12_source.csv) |
| **Total** | **2662** | **All 12 files committed** |

Each CSV has 11 fields: prior source-row identifier, original block, row position, PDF filename, SHA-1, title, abstract, publication signal, historical label, previous manual-review flag, and original Drive source file ID. All records retain original provenance. Their historical classifications are **machine-generated source data**, not validated scientific decisions.

These files constitute the full **recoverable bibliographic source master in 12 independently versioned partitions**. The materialized single-file `corpus_master_2662.csv` and fifty reviewer-blind input batches can be generated reproducibly by running:

```bash
python review_audit/tools/build_master_from_recovered.py
```

This generation utility is committed but **its outputs have not been executed or uploaded to GitHub in this session**. A local checkout with Python 3 is required for that step. The tool asserts all 2,662 records and creates 50 batches (38×53 + 12×54), preserving source order. Historic labels stay in the master and are omitted from blind inputs.

Next checks: compare global SHA-1 counts against historical 2,561 unique PDF hashes, reconcile bibliographic versions, verify peer-reviewed status, and perform full-text study-level eligibility checks. The historical `corpus_master_partial_325.csv` should be treated as an earlier partial recovery, superseded by these twelve original CSV sources.
