# Reconstructed PQI corpus — checkpoint 2026-10-20

A **325-source-record partial master** has been reconstructed from the independently saved screening CSVs (318 records) and the seven-row historical pilot. It is available at `corpus_master_partial_325.csv`. Rows contain source block/row, partial title, known PDF SHA-1, screening provenance, and a **provisional** label. IDs `PQI-REC-*` identify only the partial reconstruction and must not be treated as the final original corpus source IDs.

The prior two intermediate ledgers (`partial_ledger_01.csv`, `partial_ledger_02.csv`) preserve the original CSV record and header for reversible reconstruction. Source labels were **not independently audited**. Rows may represent duplicate PDFs or multiple versions of one study; 325 is not a unique-study count.

The original 12 ZIPs could not be found among accessible Project/Library files, and none is committed to `dnredson/journal`. The indexed Excel `PQI_controle_classificacao_blocos_10_12.xlsx` holds historic totals for all 2,662 records but only partial individual rows (blocks 10–12). The source PDFs themselves are not automatically available from their names in that workbook. Therefore **2,337 source rows remain un-reconstructed**, and no 2,662-row detailed sheet can be honestly generated from existing source data.

The local ZIP reconstructor is `review_audit/tools/rebuild_corpus.py`. Once archives are available, run it from the Git checkout with `--zips` pointing at the directory containing `Bloco*.zip`. It enumerates every PDF in those archives and computes its SHA-1, producing `corpus_master_from_zips.csv`. This requires a subsequent **study-level** DOI/title/version deduplication and full-text verification; file hashes alone are insufficient.

Do not send the initial labels to blinded coauthors or another AI. Create a stripped source file with bibliographic metadata only when preparing independent validation.
