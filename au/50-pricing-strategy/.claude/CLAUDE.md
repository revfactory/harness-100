# Pricing Strategy Harness

Develop a pricing strategy: an agent team collaborates to produce cost analysis, competitive pricing, value-based pricing, and simulations.

## Structure

```
.claude/
├── agents/
│   ├── cost-analyst.md          — Cost analysis (direct/indirect costs, BEP, margin structure)
│   ├── competitive-analyst.md   — Competitive pricing analysis (market positioning, price benchmarking)
│   ├── value-assessor.md        — Value-based pricing (WTP, value drivers, segments)
│   ├── pricing-simulator.md     — Pricing simulation (scenarios, elasticity, P&L impact)
│   └── pricing-reviewer.md      — Cross-validation (cost ↔ competitive ↔ value ↔ simulation consistency)
├── skills/
│   ├── pricing-strategy/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── psm-analyzer/
│   │   └── skill.md             — PSM analysis (Van Westendorp, optimal price, segments)
│   └── price-elasticity-calculator/
│       └── skill.md             — Price elasticity (PED/XED, optimal price, simulation)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/pricing-strategy` skill or make a natural language request such as "Build me a pricing strategy."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_cost_analysis.md` — Cost analysis report
- `02_competitive_pricing.md` — Competitive pricing analysis report
- `03_value_pricing.md` — Value-based pricing analysis report
- `04_pricing_simulation.md` — Pricing simulation report
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 26 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
