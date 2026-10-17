# Financial Modeler Harness

A harness where an agent team collaborates to produce the full financial modelling lifecycle: revenue model, cost structure, scenario analysis, and valuation.

## Structure

```
.claude/
├── agents/
│   ├── revenue-modeler.md       — Revenue Modeler (revenue structure, growth model, unit price analysis)
│   ├── cost-analyst.md          — Cost Analyst (fixed costs, variable costs, break-even)
│   ├── scenario-planner.md      — Scenario Planner (sensitivity analysis, Monte Carlo)
│   ├── valuation-expert.md      — Valuation Expert (DCF, multiples, comparable analysis)
│   └── model-reviewer.md        — Model Reviewer (revenue-cost-scenario-valuation consistency)
├── skills/
│   ├── financial-modeler/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── sensitivity-analysis/
│   │   └── skill.md             — Sensitivity Analysis (tornado, spider, data tables)
│   ├── unit-economics/
│   │   └── skill.md             — Unit Economics (CAC, LTV, payback period)
│   └── dcf-valuation/
│       └── skill.md             — DCF Valuation (WACC, terminal value, scenarios)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/financial-modeler` skill, or make a natural language request such as "Build a financial model."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_revenue_model.md` — Revenue model
- `02_cost_structure.md` — Cost structure
- `03_scenario_analysis.md` — Scenario analysis results
- `04_valuation.md` — Valuation report
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 41 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
