Cross-Repo AutoFix Multi-Agent


Project Vision
In large-scale microservice architectures, breaking changes to the underlying common library often cause dozens of downstream repositories to fail. This project achieves full automation from "change analysis" to "end-to-end remediation" and then to "closed-loop verification" through multi-agent collaboration.

Addressing core pain points
Eliminate the cost of manual retrieval: Utilize Graph RAG technology to accurately locate affected cross-repository code blocks.
Solving the long chain of inference challenges: Planner Agent generates remediation strategies that span multiple dependency levels.
Automated verification loop: Through the Reviewer Agent and the reflection mechanism of unit tests, ensure that the fix PR is 100% usable.

Core technology stack
Multi-agent orchestration: Four-role collaboration based on long-chain reasoning.
Self-reflection mechanism: After the reviewer discovers an error, it provides feedback to the coder for multiple rounds of iterative correction.


Quick Start
1. Configure `config.yaml`.
2. Run `python run_workflow.py` to start the simulated repair process.
