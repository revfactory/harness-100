# Crisis Communication Harness

crisis situation occurrence when situationidentify→messagestrategy→press release→Q&A→monitoringto agent team to integration crisis package creation .

## structure

```
.claude/
├── agents/
│ ├── situation-analyst.md — situation analysis (companyactualtotal, stakeholder, crisisetc.grade)
│ ├── message-strategist.md — message strategy (coremessage, tone, channelstrategy)
│ ├── press-release-writer.md — press release writing (officialdocument, timeline)
│ ├── qa-preparer.md — Q&A preparation (expectedquestion, answerguide, when)
│ └── media-monitor.md — media monitoring (tracking, riskdegree, afterwithinresponse)
├── skills/
│ ├── crisis-communication/
│ │ └── skill.md — Orchestrator (team , workflow, error handling)
│ ├── stakeholder-mapping/
│ │ └── skill.md — stakeholder mapping framework (situation-analyst extension)
│ └── media-response-templates/
│ └── skill.md — media response template (press-release-writer extension)
└── CLAUDE.md — file
```

## usage

`/crisis-communication` skill , "crisis response communication preparationplease do" specialistannual request.

## deliverable

all deliverable `_workspace/` save:
- `00_input.md` — user input organisation
- `01_situation_analysis.md` — situation analysis report
- `02_message_strategy.md` — message strategyfrom
- `03_press_release.md` — press release/official document
- `04_qa_briefing.md` — Q&A when
- `05_monitoring_plan.md` — monitoring plan and afterwithin response guide

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 8 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
