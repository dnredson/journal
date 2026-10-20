# Screening rounds 06–10 (2026-10-20)

Five **separate operational batches** have been saved in `review_audit/assistant/`:

| Round | Original source block | Original source rows | Records |
|---|---|---|---:|
| 06 | 10 | 113–119 | 7 |
| 07 | 11 | 0–14 | 15 |
| 08 | 11 | 15–29 | 15 |
| 09 | 11 | 30–44 | 15 |
| 10 | 11 | 45–59 | 15 |
| **Total** | | | **67** |

All records received an **initial title/metadata screening label** only; `publication_status=UNVERIFIED` and `needs_full_text_review=YES`. Counts by provisional label: Core candidate 5, Adjacent candidate 9, topic exclusion provisional 4, uncertain 47, possible duplicate 2. **These are not final included-study or PRISMA figures.**

The title of original Block 10 row 119 concerns LLM judging of creative writing; original Block 11 row 30 concerns LLM-assisted testing of IoT software; original Block 11 row 58 concerns resource-efficient mixture-of-experts inference. These are useful follow-up full-text targets, not externally verified publication claims.

Known caveats:
- Only 7 indexed Block 10 records remain in the accessible per-record sheet; original Block 10 rows 120–193 are still unavailable individually. We moved to Block 11 rather than invent entries. Accordingly, do not interpret these operational rounds as a complete contiguous scan of original Block 10.
- Original Block 11 row 1 has the same extracted title as row 0 and row 39 has the same extracted title as row 38; study-level duplicate status must be established through DOI/title and SHA-1 reconciliation.
- The consolidated workbook itself was not accessible as raw bytes for independent parsing. These are indexed spreadsheet snippets, not independent full-text reading.
- Before sending to coauthors or a second AI, create blind copies excluding `provisional_label`. Future adjudication requires independently assessed evidence and publisher/venue verification.

**Total operationally triaged so far:** 180 source records (113 earlier plus 67 here). This is not yet equivalent to the first 180 consecutive items of the complete 2,662-record corpus and should not be reported as final scientific inclusion.
