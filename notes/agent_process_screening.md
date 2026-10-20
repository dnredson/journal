# Agent / Process / Trajectory Quality — evidence ledger and scope gate

**Status:** first narrative synthesis completed on 2026-10-20. This file records individual publication and relevance checks for the cited studies; it is **not** the final systematic screening result of the historical corpus (2,662 retrieved records). The source papers must still be reconciled against the 12 blocks by DOI/title/PDF hash before unique included-paper counts can be reported.

## Publication and inclusion decisions

The entries below represent **peer-reviewed original works**. Every publication claim was checked against a version-of-record venue; in particular, the arXiv page alone is not used to infer peer review.

| Cite key | Peer-reviewed version of record | Scope for LLM system quality | Agent/process dimension | Why it is used |
|---|---|---|---|---|
| `liu2024agentbench` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html) | **Core** — evaluates LLM agents | Mixed: outcomes and diagnosed failures; inspect full text for explicit trajectory metrics | Multi-environment agent evaluation |
| `zhou2024webarena` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4410c0711e9154a7a2d26f9b3816d1ef-Abstract-Conference.html) | **Core** — functional agent benchmark | **Not automatically Yes**: main reported metric is final goal-state correctness | Black-box task success counterexample |
| `drouin2024workarena` | [ICML 2024 / PMLR 235](https://proceedings.mlr.press/v235/drouin24a.html) | **Core** — enterprise browser-agent evaluation | **Not automatically Yes**: task success may be the primary construct | Operationally realistic interactive environments |
| `mialon2024gaia` | [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html) | **Core** — general-assistant capability/quality benchmark | **Not automatically Yes**: questions may require tools but score outcome only | Distinguish environment/tool requirements from measured process |
| `ma2024agentboard` | [NeurIPS 2024 Datasets & Benchmarks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html) | **Core** — agent evaluation framework | **Yes** — intermediate progress is explicitly measured | Progress-rate metric and visualization |
| `yang2024sweagent` | [NeurIPS 2024](https://proceedings.nips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html) | **Core** — interface design evaluated via agent performance | **Review** — interface intervention and behavior are analyzed; step-level validity not automatically established | Interface→outcome effect |
| `zhuge2025agentjudge` | [ICML 2025 / PMLR 267](https://proceedings.mlr.press/v267/zhuge25a.html) | **Core** — evaluator/method targets agents | **Yes** — intermediate tasks/hierarchical requirements assessed | Agentic judging and human-baseline comparison |
| `lu2025agentrewardbench` | [COLM 2025 accepted paper](https://colmweb.org/2025/AcceptedPapers.html); [peer-reviewed PDF](https://openreview.net/pdf?id=fQcUZMPIvu) | **Core**, primarily **evaluator reliability** | **Yes as evaluated object** (trajectory judgments); primary object is the evaluator | Expert annotation of 1,302 trajectories; assessment of 12 judges |

**Secondary study** — `nageshwaran2026agent`: [Artificial Intelligence Review 2026](https://doi.org/10.1007/s10462-026-11678-4). This is a peer-reviewed *survey* and belongs to the **secondary evidence track**, not to the primary empirical-study count; it can support related-work framing and research-gap interpretation.

## Screening rules (applied to the manuscript; final audit pending)

1. **Publication gate first:** journal or peer-reviewed conference/workshop version of record required for the primary academic corpus. An arXiv copy of an already peer-reviewed paper is **not** evidence for automatic exclusion.
2. **Core:** the primary contribution evaluates LLM or LLM-system quality, e.g., assistant success, agent execution, tool decisions, an evaluator's accuracy, reliability.
3. **Adjacent:** the LLM is mainly a means to evaluate an unrelated external object; keep in a separate context track if transferable, but **do not count as Core**.
4. **Exclude:** no substantive measurement or methodological contribution to LLM-system evaluation; papers primarily about agent architecture, application design or scheduling without measurement evidence do **not** become Core simply by using LLM agents.
5. **Preprint-only / publication unverified:** set `publication_status` to `preprint_only` or `needs_verification`. Do not silently promote to academic synthesis and do not erase files from the raw archive.
6. **Review vs original study:** peer-reviewed surveys can be cited as background/related work, but their referenced experiments are not counted again as independent empirical validations.
7. **Dimensions are not paper scope:** a study may be **Core** and measure only output or final task success (WebArena, GAIA); do **not** code `Agent/Process/Trajectory=Yes` merely because a task is agentic.
8. **Used/proposed/discussed** is an independent code. Tool libraries, evaluation frameworks and theoretical multi-dimensional indices do not necessarily provide empirically integrated quality measurement.

## Explicitly unresolved / future work

- The complete Block 1–9 master extraction and 10–12 files need to be reconciled; no defensible global count of `Core / Adjacent / Exclude` or peer-review-gated exclusions can be asserted now.
- Neither this evidence ledger nor a bibliography automatically removes paper PDFs from the raw archive. Keep excluded records with a reason code for reproducibility, and omit them from the **included-study denominator** after the final review.
- Only cited BibTeX records are printed by the standard manuscript bibliography command (unless `nocite` is deliberately introduced); the presence of a background citation is not equivalent to inclusion in the primary synthesis.
- For integration: outcome-only multi-step = candidate `Black-box end-to-end`; partial trajectory progress = `Cross-stage` only if explicit relations are examined; `Lifecycle-integrated` requires the stricter full codebook criteria.
- Record peer-review evidence URLs and any adjudication exception before manuscript freeze.
