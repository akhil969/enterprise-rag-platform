# Project Roadmap

This roadmap is split into PRs so each merge is a self-contained, reviewable unit of work.
Rough phase durations are carried over from the original project spec (8–10 weeks total);
adjust freely as you go.

| PR | Phase | Deliverables | Est. Duration |
|----|-------|--------------|----------------|
| **PR #1** | Foundation | Repo setup, README, architecture diagrams, requirements doc, roadmap, Docker skeleton | Week 1 |
| **PR #2** | Basic RAG | PDF upload endpoint, chunking, embeddings, vector search (Qdrant) | Week 2 |
| **PR #3** | Advanced Retrieval | Hybrid search (vector + BM25), metadata filters, citation engine | Week 3 |
| **PR #4** | Conversational RAG | Chat history, memory management, session handling | Week 4 |
| **PR #5** | Airflow Integration | Automated ingestion DAGs, scheduled updates, retry handling | Week 5 |
| **PR #6** | Agentic RAG | Query router, multi-source retrieval, dynamic tool selection | Weeks 6–7 |
| **PR #7** | Evaluation Framework | Hallucination detection, faithfulness metrics, retrieval metrics | Week 8 |
| **PR #8** | Production Readiness | Auth (JWT/OAuth), RBAC, monitoring, structured logging, CI/CD | Weeks 9–10 |

## Notes on working this way

- Each PR should be small enough to review in one sitting — resist merging multiple phases together.
- Open PR #2 from a new branch (e.g. `feature/basic-rag`) once PR #1 is merged into `main`.
- Use PR descriptions to link back to the relevant section of `requirements.md`.
- Tag PRs with milestones in GitHub (`Phase 1`, `Phase 2`, ...) to keep the roadmap visible on the repo itself.

## Expected Outcomes (end state)

- Automatic ingestion of enterprise knowledge from multiple sources
- Accurate, hybrid semantic + keyword retrieval
- Citation-backed, explainable answers
- Persistent conversational memory
- Secure, role-based multi-user access
- A repo that demonstrates production-grade AI engineering practice end-to-end
