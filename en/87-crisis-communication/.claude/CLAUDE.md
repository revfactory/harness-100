# Crisis Communication Harness

When a crisis occurs, an agent team collaborates to produce an integrated crisis communication package covering situation assessment, message strategy, press release, Q&A, and monitoring.

## Structure

```
.claude/
├── agents/
│   ├── situation-analyst.md      — Situation analysis (facts, stakeholders, crisis grade)
│   ├── message-strategist.md     — Message strategy (core messages, tone, channel strategy)
│   ├── press-release-writer.md   — Press release writing (official statements, timeline)
│   ├── qa-preparer.md            — Q&A preparation (anticipated questions, answer guide, briefing sheet)
│   └── media-monitor.md          — Media monitoring (public sentiment tracking, risk detection, follow-up response)
├── skills/
│   ├── crisis-communication/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── stakeholder-mapping/
│   │   └── skill.md              — Stakeholder mapping framework (situation-analyst extension)
│   └── media-response-templates/
│       └── skill.md              — Media response templates (press-release-writer extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/crisis-communication` skill, or make a natural-language request such as "Prepare a crisis response communication plan."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Structured user input
- `01_situation_analysis.md` — Situation analysis report
- `02_message_strategy.md` — Message strategy document
- `03_press_release.md` — Press release / official statement
- `04_qa_briefing.md` — Q&A briefing sheet
- `05_monitoring_plan.md` — Monitoring plan and follow-up response guide
