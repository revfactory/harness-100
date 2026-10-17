---
name: financial-modeler
description: "A financial modelling full pipeline. An agent team collaborates to generate revenue model, cost structure, scenario analysis, and valuation. Use this skill for requests like 'build a financial model', 'revenue forecast', 'cost analysis', 'valuation', 'enterprise valuation', 'DCF analysis', 'investment model', 'revenue modelling', 'P&L analysis', 'financial projection', and other financial modelling needs. Also supports partial analysis when existing financial data is available. However, actual accounting system integration, ERP data extraction, tax return preparation, and real-time stock price analysis are outside the scope of this skill."
---

# Financial Modeler — Financial Modelling Full Pipeline

An agent team collaborates to generate revenue model, cost structure, scenario analysis, and valuation.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| revenue-modeler | `.claude/agents/revenue-modeler.md` | Revenue stream definition, revenue forecast, unit economics | general-purpose |
| cost-analyst | `.claude/agents/cost-analyst.md` | Cost classification, break-even analysis, margin analysis | general-purpose |
| scenario-planner | `.claude/agents/scenario-planner.md` | Bear/Base/Bull scenarios, sensitivity analysis | general-purpose |
| valuation-expert | `.claude/agents/valuation-expert.md` | DCF, multiples, comparable companies, investment return analysis | general-purpose |
| model-reviewer | `.claude/agents/model-reviewer.md` | Formula accuracy, assumption consistency, integrated summary | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Business Information**: Industry, business model, product/service, current stage (idea/MVP/PMF/scale-up)
    - **Financial Data** (optional): Current revenue, costs, investment amounts, etc.
    - **Analysis Purpose**: Fundraising, internal planning, M&A, business feasibility validation, etc.
    - **Existing Files** (optional): Existing financial models, business plans, etc.
2. Create `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Revenue Model | revenue-modeler | None | `_workspace/01_revenue_model.md` |
| 1b | Cost Structure | cost-analyst | Task 1a | `_workspace/02_cost_structure.md` |
| 2 | Scenario Analysis | scenario-planner | Tasks 1a, 1b | `_workspace/03_scenario_analysis.md` |
| 3 | Valuation | valuation-expert | Task 2 | `_workspace/04_valuation_report.md` |
| 4 | Integration Review | model-reviewer | Tasks 1-3 | `_workspace/05_financial_summary.md`, `_workspace/06_review_report.md` |

**Inter-team Communication Flow:**
- revenue-modeler completes → delivers revenue stream structure and revenue scale to cost-analyst, delivers key assumptions to scenario-planner
- cost-analyst completes → delivers fixed/variable cost structure to scenario-planner
- scenario-planner completes → delivers per-scenario financial statements and probability-weighted forecasts to valuation-expert
- model-reviewer cross-validates all deliverables. If 🔴 Must Fix, sends revision request (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Build a full financial model" | **Full Pipeline** | All 5 |
| "Just do revenue forecasting" | **Revenue Mode** | revenue-modeler + reviewer |
| "Analyse costs" | **Cost Mode** | cost-analyst + reviewer |
| "Just do valuation" (with existing financial data) | **Valuation Mode** | valuation-expert + reviewer |
| "Review this financial model" | **Review Mode** | model-reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient market data | Apply similar industry benchmarks, tag as "estimates" |
| Unclear business model | Propose 3 revenue model types, request user selection |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note omission in review |
| Numerical discrepancy found | Trace to original, correct figures, document revision history |
| 🔴 found in review | Send revision request → rework → re-validate (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "Build a financial model for a B2B SaaS startup. Monthly subscription $50, currently 50 enterprise customers, targeting 30% annual growth. For Series A fundraising."
**Expected Results**:
- Revenue Model: SaaS revenue structure (MRR/ARR), customer cohort, churn reflected, LTV/CAC
- Cost Structure: Cloud infrastructure, dev team labour, sales costs, BEP analysis
- Scenarios: Bear(15%)/Base(30%)/Bull(50%) growth rate scenarios, sensitivity analysis
- Valuation: DCF + PSR multiples + 3+ comparable companies
- Integrated Summary: Investor-ready Executive Summary

### Existing File Utilisation Flow
**Prompt**: "Just do valuation with this revenue data" + financial data attached
**Expected Results**:
- Map existing data to `_workspace/`
- Deploy only valuation-expert + model-reviewer
- Supplement data gaps with assumptions

### Error Flow
**Prompt**: "I have a new business idea, build me a financial model. No revenue yet."
**Expected Results**:
- Propose business model types, then confirm
- Revenue estimation focused on bottom-up (TAM/SAM/SOM + per-customer)
- Emphasise cash burn analysis in Bear scenario
- Prioritise venture capital methodology for valuation

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Agent | Extension Skill | Role |
|-------|----------------|------|
| valuation-expert | `dcf-valuation` | WACC calculation, FCFF estimation, terminal value, multiples cross-validation |
| scenario-planner | `sensitivity-analysis` | Tornado chart, 2-way table, Bear/Base/Bull scenarios, break-even |
| revenue-modeler | `unit-economics` | LTV/CAC, 3-layer contribution margin, cohort analysis, bottom-up revenue estimation |
