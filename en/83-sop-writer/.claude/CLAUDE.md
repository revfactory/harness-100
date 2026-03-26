# SOP Writer Harness

A harness where an agent team collaborates to produce Standard Operating Procedure (SOP) deliverables — process analysis, procedure documentation, checklists, training materials, and version control.

## Structure

```
.claude/
├── agents/
│   ├── process-analyst.md      — Process analysis (current workflow analysis, bottleneck identification)
│   ├── procedure-writer.md     — Procedure documentation (step-by-step procedures, decision branches)
│   ├── checklist-designer.md   — Checklist design (execution checklists, quality gates)
│   ├── training-developer.md   — Training material creation (learning guides, assessment items)
│   └── version-controller.md   — Version control and cross-verification (change history, consistency check)
├── skills/
│   ├── sop-writer/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── process-mapping/
│   │   └── skill.md           — Process mapping methodology (for process-analyst)
│   └── checklist-design/
│       └── skill.md           — Checklist design principles (for checklist-designer)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/sop-writer` skill, or make a natural language request such as "Create an SOP for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_process_analysis.md` — Process analysis results
- `02_procedure_document.md` — Standard procedure document
- `03_checklists.md` — Checklist set
- `04_training_materials.md` — Training materials
- `05_version_control.md` — Version control and verification report
