# Conversation & Interaction Quality — evidence provenance and coding notes

Status: **first representative qualitative synthesis**, not the final coded distribution of the full corpus. Manuscript target: `sections/06_quality_dimensions.tex`.

| BibTeX key | Verified peer-reviewed version | Evidence relevant to this subsection | Boundary |
|---|---|---|---|
| `kwan2024mteval` | [EMNLP 2024](https://aclanthology.org/2024.emnlp-main.1124/) | MT-Eval: recollection, expansion, refinement and follow-up; 1,170 paired single-/multi-turn questions; distance to relevant information and error propagation | Paired outcomes demonstrate turn effects, not necessarily exact internal failure cause |
| `deshpande2025multichallenge` | [Findings ACL 2025](https://aclanthology.org/2025.findings-acl.958/) | MultiChallenge: four realistic conversation challenges, instance rubrics, LLM judge and human comparison; best reported model 41.4% | Results bound to challenge distribution and model versions; judge agreement is separate evidence |
| `tian2025cmteval` | [Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.992/) | Chinese multi-turn speech acts/user personas: 596 dialogues, 4,431 turns | Generalization beyond language, user-persona and scenario design needs independent evidence |
| `maharana2024locomo` | [ACL 2024 Long Papers](https://aclanthology.org/2024.acl-long.747/) | LoCoMo: very long-term memory, temporal/causal relationships; roughly 600 turns/16k tokens on average over up to 32 sessions | Memory question-answering outcome ≠ retrieval-stage attribution |
| `wu2025longmemeval` | [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html) | LongMemEval: 500 questions; extraction, multi-session/temporal reasoning, updates, abstention; indexing/retrieval/reading decomposition | Evidence for memory-stage optimization, not automatically all lifecycle dimensions |
| `wang2024mint` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8a0d3ae989a382ce6e50312bc35bf7e1-Abstract-Conference.html) | MINT: multistep use of tools and natural-language feedback in interactive tasks | Tools are present; tool-use quality requires explicit evidence; feedback simulated by GPT-4 |
| `yao2025taubench` | [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html) | tau-bench: retail/airline dynamic agent-user conversations; end database state against gold goal; pass^k repeatability | Verifiable end-state is not a trace-level safety/efficiency validation |
| `zhou2024sotopia` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/b3075b88e583a0e98d8b24338a613060-Abstract-Conference.html) | SOTOPIA: simulated open-ended social interactions and SOTOPIA-Eval | Ecological validity of simulation and reliability of scoring warrant separate assessment |

### Relationship to already cited literature

The existing `zheng2023mtbench` citation in Output Quality is also conversation-relevant (two-turn MT-Bench, preferences, judge agreement/bias). The Conversation Quality subsection does **not** cite it again as a new primary record. A study can have multiple coded dimensions while remaining a single deduplicated bibliographic study.

### Screening and coding reminders

1. Several independent single-turn questions are not necessarily **interaction evaluation**. Require actual cross-turn dependence, state continuity or interactive feedback.
2. Long context is not identical to long-term interactive memory. Preserve separate labels for context retrieval, conversational state, memory update and turn-level action.
3. Count a study under Agent/Process/Trajectory only when quality of actions/plans/tools/process is explicitly evaluated; simply exposing tools is not enough.
4. A final goal-state check after several turns is **black-box end-to-end** unless process contributions are explicitly decomposed; repeated success is an additional stability measure.
5. When an LLM judge or simulated user is employed, separately code the target and the presence/absence of reliability/validity evidence for the simulator or judge.
6. MultiChallenge compares LLM judge results with experienced human raters; this supports limited meta-evaluation coding, not unqualified trustworthiness.
7. LongMemEval is a **subsystem-level stage-aware counterexample** (indexing→retrieval→reading); do not claim no prior cross-stage conversation studies.
8. Papers cited here were validated via the official ACL Anthology or ICLR proceedings. Their membership and duplicate hashes in historical blocks **remain unreconciled**.
9. Report no field prevalence, reliability coefficients of our annotators or final integration distributions until human-validated extraction.

### Editorial caution: 30-page target

There are now four dimension-specific qualitative comparison tables; consider a concise two-page evidence matrix for all six dimensions plus supplemental tables later. Do not cut detailed conceptual contrasts that justify RQ3/RQ4 to preserve an arbitrary table count.
