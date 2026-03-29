# Technical Writer Harness

A harness where an agent team collaborates to produce technical documentation deliverables: structure design, writing, diagrams, review, and version management.

## Structure

```
.claude/
├── agents/
│   ├── info-architect.md      — Information design (structure design, table of contents, audience analysis)
│   ├── doc-writer.md          — Writer (body text, code examples, tutorials)
│   ├── diagram-maker.md       — Diagram creation (Mermaid, visual materials)
│   ├── tech-reviewer.md       — Technical reviewer (accuracy, completeness, consistency verification)
│   └── version-controller.md  — Version management (change history, metadata, deployment)
├── skills/
│   ├── technical-writer/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── diagram-patterns/
│   │   └── skill.md           — Mermaid diagram pattern library (extension for diagram-maker)
│   ├── api-doc-standards/
│   │   └── skill.md           — API documentation standards (extension for doc-writer)
│   └── code-example-patterns/
│       └── skill.md           — Code example pattern library (extension for doc-writer)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/technical-writer` skill, or make a natural language request such as "write technical documentation for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_doc_structure.md` — Document structure design
- `02_doc_draft.md` — Document body text draft
- `03_diagrams.md` — Diagram collection
- `04_review_report.md` — Technical review report
- `05_version_meta.md` — Version management metadata
