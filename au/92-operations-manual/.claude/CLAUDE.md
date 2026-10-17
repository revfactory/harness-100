# Operations Manual Harness

An automated operations manual generation harness. An agent team collaborates to analyse existing documents/code and generate process flowcharts, step-by-step manuals, FAQs, and training materials.

## Structure

```
.claude/
├── agents/
│   ├── document-analyst.md    — Existing document/code analysis (structure mapping, process extraction, glossary)
│   ├── flowchart-designer.md  — Process flowchart design (Mermaid diagrams, branching logic)
│   ├── manual-writer.md       — Step-by-step manual writing (procedures, screenshot guides, checklists)
│   ├── faq-builder.md         — FAQ and troubleshooting guide creation
│   └── training-producer.md   — Training material production (quizzes, hands-on exercises, summary cards)
├── skills/
│   ├── operations-manual/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── flowchart-standards/
│   │   └── skill.md           — Process flowchart standards (flowchart-designer extension)
│   └── knowledge-base-design/
│       └── skill.md           — Knowledge base design guide (faq-builder extension)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/operations-manual` skill, or make a natural language request such as "Create an operations manual."

## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — User input and analysis targets
- `01_document_analysis.md` — Existing document/code analysis results
- `02_process_flowcharts.md` — Process flowcharts (Mermaid)
- `03_step_by_step_manual.md` — Step-by-step operations manual
- `04_faq_troubleshooting.md` — FAQ and troubleshooting guide
- `05_training_materials.md` — Training materials package
- `06_review_report.md` — Integrated review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 24 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
