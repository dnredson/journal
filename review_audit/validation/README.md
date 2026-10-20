# Independent cross-validation

Human reviewer A and B each submit an independent file in `human/`. A third author may adjudicate disagreements. External AI writes `ai/` independently, without seeing assistant/human labels.

Recommended columns: `record_id,reviewer_id,screening_phase,decision,primary_reason,dimensions,methods,integration_level,evidence_reference,confidence,comments,review_date`.

Decisions: `INCLUDE_CORE`, `ADJACENT`, `EXCLUDE`, `UNCERTAIN`; publication status is coded separately (`VERIFIED_PEER_REVIEWED`, `PREPRINT_ONLY`, `THESIS`, `OTHER_GREY`, `UNKNOWN`). Do not force uncertain records to exclusion.

Primary-human consensus is independent of AI votes. Measure nominal human agreement (e.g. Cohen kappa for two raters) and multilabel binary agreement by dimension; report agreement on an adjudicated set for the AI separately. Blind first, compare later.
