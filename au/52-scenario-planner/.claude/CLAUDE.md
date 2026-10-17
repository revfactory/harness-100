# Scenario Planner Harness

An agent team harness that defines key variables in uncertain environments, constructs a scenario matrix, and develops impact analysis and response strategies.

## Structure

```
.claude/
├── agents/
│   ├── variable-analyst.md       — Key variable identification and uncertainty assessment
│   ├── scenario-designer.md      — Scenario matrix design and scenario narrative writing
│   ├── impact-assessor.md        — Per-scenario impact analysis and quantitative/qualitative assessment
│   ├── strategy-architect.md     — Response strategy development and decision-making framework design
│   └── integration-reviewer.md   — Cross-validation, logical consistency verification, final document integration
├── skills/
│   ├── scenario-planner/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── steep-framework/
│   │   └── skill.md              — STEEP macro-environment analysis (6 dimension scanning, uncertainty-impact matrix)
│   ├── scenario-narrative-engine/
│   │   └── skill.md              — Scenario narrative construction (2x2 matrix, timeline, early warning signals)
│   └── decision-trigger-mapper/
│       └── skill.md              — Decision trigger map (real options, strategy portfolio, execution roadmap)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/scenario-planner` skill or make a natural language request such as "Run a scenario analysis" or "Plan future scenarios."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_variable_analysis.md` — Key variable analysis report
- `02_scenario_matrix.md` — Scenario matrix and narratives
- `03_impact_assessment.md` — Impact analysis report
- `04_response_strategy.md` — Response strategy document
- `05_decision_document.md` — Integrated decision document
- `06_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 23 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
