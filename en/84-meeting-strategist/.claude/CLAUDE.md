# Meeting Strategist Harness

A harness where an agent team collaborates to produce a complete meeting strategy document set, covering agenda structure design, background research, decision-making frameworks, meeting record templates, and follow-up plans.

## Structure

```
.claude/
├── agents/
│   ├── agenda-architect.md        — Agenda design (meeting purpose, structure, time allocation)
│   ├── background-researcher.md   — Background research (relevant data, stakeholder analysis)
│   ├── framework-designer.md      — Decision-making framework (evaluation criteria, option assessment)
│   ├── template-builder.md        — Document templates (meeting minutes, reporting forms)
│   └── followup-planner.md        — Follow-up plan and cross-validation (execution tracking, QA)
├── skills/
│   ├── meeting-strategist/
│   │   └── skill.md               — Orchestrator (team coordination, workflow, error handling)
│   ├── decision-frameworks/
│   │   └── skill.md               — Decision-making framework library (framework-designer extension)
│   └── facilitation-techniques/
│       └── skill.md               — Facilitation techniques (agenda-architect extension)
└── CLAUDE.md                      — This file
```

## Usage

Trigger the `/meeting-strategist` skill, or make a natural language request such as "prepare meeting materials" or "create a meeting agenda."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_agenda_design.md` — Agenda structure design document
- `02_background_brief.md` — Background research brief
- `03_decision_framework.md` — Decision-making framework
- `04_meeting_templates.md` — Meeting minutes and reporting templates
- `05_followup_plan.md` — Follow-up plan and validation report
