# Wedding Planner Harness

A harness where an agent team collaborates to produce comprehensive wedding preparation deliverables: timeline design, budget management table, vendor comparison table, checklist, and invitation wording.

## Structure

```
.claude/
├── agents/
│   ├── timeline-designer.md   — Timeline design (D-day countdown, monthly tasks)
│   ├── budget-controller.md   — Budget management (category allocation, tracking, cost reduction)
│   ├── vendor-analyst.md      — Vendor comparison (wedding hall, studio/dress/makeup, honeymoon research)
│   ├── checklist-builder.md   — Checklist + invitation wording (task list, wording drafts)
│   └── wedding-reviewer.md    — Cross-verification (timeline↔budget↔vendor↔checklist consistency)
├── skills/
│   ├── wedding-planner/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── vendor-negotiation-guide/
│   │   └── skill.md           — Wedding vendor comparison and negotiation guide (for vendor-analyst)
│   └── wedding-budget-optimizer/
│       └── skill.md           — Wedding budget optimization (for budget-controller)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/wedding-planner` skill, or make a natural language request such as "help me plan my wedding."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_timeline.md` — Wedding preparation timeline
- `02_budget.md` — Budget management table
- `03_vendor_comparison.md` — Vendor comparison table
- `04_checklist_invitation.md` — Checklist + invitation wording
- `05_review_report.md` — Review report
