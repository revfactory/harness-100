# Investor Report Harness

Investor report generation: an agent team collaborates to produce financial performance analysis, KPI dashboard, market trends, strategy updates, and risk disclosures.

## Structure

```
.claude/
├── agents/
│   ├── financial-analyst.md     — Financial analysis (P&L, cash flow, key financial metrics)
│   ├── kpi-designer.md          — KPI dashboard (key metrics, trends, benchmarks)
│   ├── market-analyst.md        — Market trends (industry trends, competition, regulation)
│   ├── strategy-updater.md      — Strategy update (progress, roadmap, risk disclosure)
│   └── ir-reviewer.md           — Cross-validation (financial ↔ KPI ↔ market ↔ strategy consistency)
├── skills/
│   ├── investor-report/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── financial-ratio-analyzer/
│   │   └── skill.md             — Financial ratio deep analysis (DuPont, SaaS metrics, 5 ratio categories)
│   ├── kpi-benchmark-engine/
│   │   └── skill.md             — KPI benchmarking (industry benchmarks, SMART-R, pyramid)
│   └── ir-narrative-builder/
│       └── skill.md             — IR narrative construction (Equity Story, investor-specific tone, EBITDA Bridge)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/investor-report` skill or make a natural language request such as "Create an investor report."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_financial_analysis.md` — Financial performance analysis report
- `02_kpi_dashboard.md` — KPI dashboard
- `03_market_trends.md` — Market trends report
- `04_strategy_update.md` — Strategy update and risk disclosure
- `05_review_report.md` — Review report
- `06_investor_report_final.md` — Final integrated report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 36 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
