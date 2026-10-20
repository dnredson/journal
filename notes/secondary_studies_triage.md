# First-pass triage of surveys and reviews

Status: working note for novelty positioning; not a final inclusion table.

## A. Closest prior surveys — use directly in the novelty comparison

These are the strongest direct comparators for the manuscript and are already cited in `sections/03_prior_surveys.tex`.

1. **Yehudai et al. (2026), A Survey on Evaluation of LLM-based Agents** — agent evaluation; capabilities, benchmarks, frameworks/tools.
2. **Kehkashan et al. (2026), From benchmarks to deployment: a comprehensive review of agentic AI evaluation** — agentic evaluation; trajectory, deployment, safety/cost gaps.
3. **Nageshwaran et al. (2026), Large language model agent evaluation and benchmarking: a systematic survey, meta-taxonomy, and critical research roadmap** — systematic agent-evaluation mapping; what/how/where and validity.
4. **Knollmeyer et al. (2026), Evaluating Retrieval Augmented Generation: A Comprehensive Review of Evaluation Dimensions, Question Types, and Application** — RAG evaluation; dimensions, metrics, evaluator types, datasets, retrieval-generation links.
5. **Wu et al. (2026), Retrieval-augmented generation for natural language processing: a survey** — broad RAG architecture/application survey with evaluation and deployment sections.
6. **Nadăş (2026), Large language models as judges...** — LLM-as-a-Judge techniques and judge-quality issues.

Working novelty position: these surveys are deep but specialized by **system class** (agents/RAG) or **evaluation mechanism** (LLM judges). Our survey treats those as parts of one lifecycle-wide quality-assessment problem and explicitly codes integration across stages.

## B. Relevant secondary studies — evidence for individual dimensions

These should be retained as dimension-specific background/evidence if they pass the publication-status gate.

- **Assessing RAG: A Comprehensive Review of Evaluation Frameworks** — RAG evaluation frameworks; context/retrieval, output and operational concerns.
- **Large Language Models and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability and Defensive Strategies** — output/security and deployment concerns.
- **Transforming IoT Security through Large Language Models: A Comprehensive Systematic Review and Future Directions** — domain review combining task quality, resource constraints and security.
- **ChatEMT: large language model framework for energy-efficient machine tools — review, paradigm and perspectives** — context/output/operational quality in a manufacturing domain.
- **A Systematic Review of Intelligent Agents, Language Models, and Recurrent Neural Networks in Industrial Maintenance** — domain-specific agent/context/output evidence.
- **LLM-Enabled Cyber-Physical Systems Survey: Research Opportunities and Challenges** — CPS deployment and output-quality concerns.
- **Agentic AI in Action: A Review of Architectures, Communication, and Coordination in Intelligent Multi-Agent Systems** — agent/process, communication and operational concerns.
- **A Review of Multi-Agent AI Systems for Biological and Clinical Data Analysis** — multi-agent evaluation in a domain-specific setting.
- **A Systematic Survey of Automatic Prompt Optimization Techniques** — Input/Specification dimension.
- **A Systematic Review of Prompt Injection Attacks on Large Language Models: Trends, Taxonomy...** — Input/Specification + safety/security cross-cutting concern.
- **Prompting for LLM Security and RAG: A Survey from Zero-Shot to Automatic Prompt Optimization and Prompt-Injection Defenses** — input/context/security.
- **A Review of Large Language Models for Energy Systems: Applications, Challenges and Future Prospects** — domain-specific output/system-quality evidence.
- **A systematic review of the limitations of large language models in generating healthcare content** — domain-specific output quality.
- **The use of Large Language Models and other Generative AI tools to support decision-making in cancer care: a mapping review** — domain-specific LLM use/evaluation.
- **Large Language Models in Multi Criteria Decision Making: A Systematic Review, Taxonomy, and Future Research Agenda** — domain/task-oriented LLM review.

These are not direct substitutes for our survey because their organizing scope is a technique, risk class, application domain, or subsystem.

## C. Adjacent secondary studies

Useful mainly for context or specific operational/agent issues; not primary novelty baselines.

- **Agent-Based Hybrid AI Models and Technologies: A Systematic Literature Review**.
- **AI Agents Meet Blockchain: A Survey on Secure and Scalable Collaboration for Multi-Agents**.
- **Understanding AI Agents—A Data-Driven Literature Review**.
- **Is Collaboration Worth It? A Decision-Oriented Survey in Multi-Agent Systems**.
- **A Review on Agent-to-Agent Protocol: Concept, State-of-the-art, Challenges and Future Directions**.
- **Future AI Tools LLM and Frameworks**.

The last two require special care because the available versions may be preprint/non-archival; they should not enter the primary academic evidence until peer review is verified.

## D. Obvious study-type false positives found in the historical classification

The first pass found records labelled `survey_review` that are not actually secondary studies. These should be corrected during the study-type audit.

- **A Multi-Stage Self-Review Framework for Translating Natural Language into Neo4j Cypher Queries** — empirical/framework study; “self-review” is part of the method, not a literature review.
- **AI-Driven Monitoring and Knowledge Graphs for Generative AI Applications** — empirical/benchmarking work.
- **Evaluating GPT-4o as a Cyberattack Simulator: Perspectives on AI and Human Decision-Making** — empirical evaluation, not a survey.
- **Mammal Review...** — journal/title lexical collision and outside LLM scope.
- **Comparative Study of the Working of Various AI Classifiers for Identifying Ragas of Indian Classical Music** — genuine systematic review, but outside LLM-system quality scope.

This confirms that study type must be audited from title/abstract/full text rather than inferred from words such as “review” or inherited labels.

## E. Publication-status caution

The primary manuscript should compare itself primarily with confirmed peer-reviewed secondary studies. TechRxiv, SSRN, arXiv-only and other preprint-only surveys may be used in a supplementary/grey-literature track but must not be counted as peer-reviewed evidence unless a version of record is verified.

## Remaining audit

The current pass covers the secondary-study candidates identifiable in the accessible classified Blocks 10–12 material, the explicitly uploaded survey/review candidates, and the 2026 update set. The earlier Blocks 1–9 need the same study-type re-audit once the consolidated 1–9 master classification is available again in readable form; do not claim the current list is the final exhaustive secondary-study inventory until that pass is completed.
