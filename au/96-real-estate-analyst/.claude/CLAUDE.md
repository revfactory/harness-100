# Real Estate Analyst Harness

A real estate analysis harness. An agent team collaborates to produce market research, location analysis, profitability analysis, risk assessment, and investment reports.

## Structure

```
.claude/
├── agents/
│   ├── market-researcher.md      — Market research (macroeconomics, regional market, supply/demand)
│   ├── location-analyst.md       — Location analysis (transit, schools, commercial district, development potential)
│   ├── profitability-analyst.md  — Profitability analysis (rental yield, cash flow, IRR)
│   ├── risk-assessor.md          — Risk assessment (regulatory, market, liquidity risk)
│   └── report-writer.md          — Investment report (overall judgment, investment opinion)
├── skills/
│   ├── real-estate-analyst/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── cap-rate-calculator/
│   │   └── skill.md              — Yield calculator (profitability-analyst extension)
│   └── location-scoring/
│       └── skill.md              — Location evaluation scorecard (location-analyst extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/real-estate-analyst` skill, or make a natural language request such as "Analyse this real estate property."

## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Analysis target and investment conditions
- `01_market_research.md` — Market research report
- `02_location_analysis.md` — Location analysis report
- `03_profitability_analysis.md` — Profitability analysis report
- `04_risk_assessment.md` — Risk assessment report
- `05_investment_report.md` — Comprehensive investment report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 24 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
