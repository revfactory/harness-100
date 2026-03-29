# Event Organizer Harness

Event planning and operations: a harness where an agent team collaborates to produce deliverables covering concept → venue → program → promotion → execution → post-event evaluation.

## Structure

```
.claude/
├── agents/
│   ├── concept-planner.md        — Concept planning (theme, goals, target audience, budget)
│   ├── logistics-manager.md      — Logistics (venue, flow, equipment, catering)
│   ├── program-designer.md       — Program design (timetable, speakers, content)
│   ├── promotion-lead.md         — Promotion (channel strategy, content, registration management)
│   └── evaluation-analyst.md     — Post-event evaluation (KPI, survey, report, lessons learned)
├── skills/
│   ├── event-organizer/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── budget-planning/
│   │   └── skill.md              — Event budget planning (concept-planner extension)
│   └── venue-evaluation/
│       └── skill.md              — Venue evaluation scorecard (logistics-manager extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/event-organizer` skill, or make a natural language request such as "plan an event for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_concept_plan.md` — Concept plan
- `02_logistics_plan.md` — Logistics plan
- `03_program_design.md` — Program design document
- `04_promotion_plan.md` — Promotion plan
- `05_evaluation_framework.md` — Evaluation framework
