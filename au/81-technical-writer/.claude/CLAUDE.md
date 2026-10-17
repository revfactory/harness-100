# Technical Writer Harness

technical document writing structuredesign→→diagram→review→versionmanagement A harness where an agent team collaborates to produce deliverables.

## structure

```
.claude/
├── agents/
│ ├── info-architect.md — information design (structure design, table of contents, reader analysis)
│ ├── doc-writer.md — specialist (body text writing, code example, )
│ ├── diagram-maker.md — diagram writing (Mermaid, wheneach material)
│ ├── tech-reviewer.md — technical reviewer (accuracy, completeness, consistency verify)
│ └── version-controller.md — version management (change capability, data, deployment)
├── skills/
│ ├── technical-writer/
│ │ └── skill.md — Orchestrator (team , workflow, error handling)
│ ├── diagram-patterns/
│ │ └── skill.md — Mermaid diagram pattern library (diagram-maker extension)
│ ├── api-doc-standards/
│ │ └── skill.md — API document writing tablelevel (doc-writer extension)
│ └── code-example-patterns/
│ └── skill.md — code example pattern library (doc-writer extension)
└── CLAUDE.md — file
```

## usage

`/technical-writer` skill , "technical document writingplease do" specialistannual request.

## deliverable

all deliverable `_workspace/` save:
- `00_input.md` — user input organisation
- `01_doc_structure.md` — document structure designfrom
- `02_doc_draft.md` — document body text plan
- `03_diagrams.md` — diagram 
- `04_review_report.md` — technical review report
- `05_version_meta.md` — version management data

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 9 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
