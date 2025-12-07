<!--
Sync Impact Report:
Version change: 0.0.0 -> 1.0.0 (MAJOR: Initial version)
Modified principles: None (New principles added)
Added sections: Key Standards and Constraints, Success Criteria and Project Goals
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/*.md: ⚠ pending
Follow-up TODOs: None
-->
# AI-Native Book Creation with Integrated RAG Chatbot Constitution

## Core Principles

### I. Clarity and Correctness
All technical explanations MUST be clear, concise, and factually correct.

### II. AI-Assisted Drafting Alignment
AI-assisted drafting MUST align with developer-friendly writing standards, prioritizing readability and practical utility.

### III. Consistency
All content, code, and documentation MUST maintain consistency in structure, tone, terminology, and formatting across the project.

### IV. Reproducibility
All code examples and instructions MUST be reproducible and run as written without errors or ambiguity.

### V. Security and Data-Privacy Awareness
The RAG design MUST incorporate robust security measures and adhere strictly to data privacy best practices.

## Key Standards and Constraints

### Key Standards
*   Book framework: Docusaurus v3
*   Deployment: GitHub Pages using CI/CD
*   Chatbot stack: OpenAI Agents/ChatKit SDKs + FastAPI + Neon Postgres + Qdrant Cloud
*   Source of truth: project specification + generated book content
*   Code samples validated and tested before inclusion
*   All architectural diagrams MUST be AI-generated and reviewed

### Constraints
*   Book MUST contain at least 8–12 chapters
*   RAG chatbot MUST answer questions only from book content and selected text
*   Free-tier limits MUST be respected for Neon, Qdrant, and GitHub Pages
*   All configurations MUST be open source in a public GitHub repository

## Success Criteria and Project Goals

*   Docusaurus book deployed live on GitHub Pages
*   Fully functional embedded RAG chatbot with accurate, citation-based responses
*   Smooth user experience: fast retrieval, correct sources, clear UI
*   All instructions reproducible by another developer using the repo
*   Project meets Spec-Driven standards and passes verification in all phases

## Governance
This constitution supersedes all other practices. Amendments require thorough documentation, explicit approval from stakeholders, and a clear migration plan. Compliance reviews are expected at regular intervals to ensure ongoing adherence to these principles and standards.

**Version**: 1.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05