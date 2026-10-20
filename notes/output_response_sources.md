# Output & Response Quality — sources, boundaries and pending checks

Status: first **critical narrative synthesis** with a purposive representative sample. Not a census of the screened academic corpus; do not infer frequencies or inclusion counts. Article: `sections/06_quality_dimensions.tex`, subsection `Output and Response Quality`.

## Verified peer-reviewed works

| BibTeX key | Academic publication (version of record) | Evaluation construct and methodological role | Reading note |
|---|---|---|---|
| `zhang2020bertscore` | ICLR 2020, https://openreview.net/forum?id=SkeHuCVFDr | Embedding-based **reference similarity** | Semantic match is not independent fact verification |
| `lin2022truthfulqa` | ACL 2022, https://aclanthology.org/2022.acl-long.229/ | Truthfulness under misconception-focused prompts | Not general helpfulness/faithfulness measure |
| `min2023factscore` | EMNLP 2023, https://aclanthology.org/2023.emnlp-main.741/ | Atomized **fact support**; evaluates long-form generations | Verifier retrieval ≠ generation-system retrieval; verification-source accuracy matters |
| `zha2023alignscore` | ACL 2023, https://aclanthology.org/2023.acl-long.634/ | Learned source–output **factual consistency** | A source may be wrong, even if text is consistent with it |
| `adlakha2024correctness` | TACL 2024, https://aclanthology.org/2024.tacl-1.38/ | Separates **correctness**, **faithfulness** and abstention in QA; human evaluation | Useful cross-stage QA/context/output boundary; does not collapse criteria |
| `manakul2023selfcheckgpt` | EMNLP 2023, https://aclanthology.org/2023.emnlp-main.557/ | Self-consistency as hallucination **indicator** | Consistent samples can still repeat incorrect claims |
| `liu2023geval` | EMNLP 2023, https://aclanthology.org/2023.emnlp-main.153/ | Structured LLM-as-a-Judge for NLG; human-alignment analysis | Judge is a method and only a meta-evaluation target when bias/agreement are measured |
| `zheng2023mtbench` | NeurIPS 2023 Datasets & Benchmarks, https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html | LLM judges vs human preference; position/verbosity/self-enhancement bias | Also conversation / meta-evaluation; avoid double-counting across categories |
| `gu2024dingo` | AAAI 2024, https://doi.org/10.1609/aaai.v38i16.29768 | Fine-grained **instruction compliance** evaluation | Fixed instructions as stimulus ≠ assessed prompt quality |
| `jimenez2024swebench` | ICLR 2024, https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html | Executable **task-resolution success** for software patches | Black-box correctness alone does not establish trajectory/tool safety |
| `liang2023helm` | TMLR 2023, https://mlanthology.org/tmlr/2023/liang2023tmlr-holistic/ | Seven metrics across standardized model scenarios | Multi-metric ≠ stage-aware lifecycle integration |

## Eligibility caveat

The original IFEval work (Zhou et al., 2023, arXiv:2311.07911) was **not** placed in the primary academic references here because this pass did not verify a peer-reviewed version of record. The manuscript instead uses peer-reviewed DINGO (AAAI 2024) for instruction-following coverage. If a version of record is later verified, revisit eligibility before citation.

## Classification implications

- Correctness relative to a user question, faithfulness relative to retrieved evidence, and independent truthfulness differ.
- Lexical/semantic similarity is a **method family**, not a quality guarantee.
- Judging via GPT does **not** entail judge reliability. Compare separate observed evidence about evaluator agreement or bias.
- Semantic-output metrics, preference votes, source-grounding measures, execution tests, and abstention should not be averaged into a universal score without construct definition and a defensible aggregation rule.
- A benchmark measuring success across a multi-step workflow can be black-box end-to-end without any process attribution.
- HELM's multi-metric approach is an important novelty competitor. Do **not** claim prior work lacks multidimensional evaluation.
- Do not cite a survey as independent confirmation of the empirical results it merely synthesizes.
- These eleven works are **not yet reconciled** for deduplication against the 12 historical blocks; they are not new additions to the declared 2,662 retrieval total unless they are verified as such.

## Editorial and reproduction notes

Three dimension-specific tables now appear in `sections/06_quality_dimensions.tex`. Before manuscript freeze, consider compressing these into a consolidated table or moving detailed rows to a supplementary appendix to preserve the ~30-page working budget. The current text is qualitative and should be reconciled against the human-validated coding and final peer-review gate before final gap/prevalence statements.
