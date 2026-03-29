---
name: tax-calculator
description: "A full pipeline where an agent team collaborates to handle the entire process of tax calculation and tax-saving strategy development. Use this skill for requests related to tax calculation, tax savings, and tax filing such as: 'calculate my taxes', 'year-end tax settlement simulation', 'how much will my comprehensive income tax be', 'tax-saving methods', 'tax credit optimization', 'pension savings tax credit', 'business income tax', 'freelancer taxes', 'capital gains tax calculation', 'effective tax rate analysis'. If existing tax documents are available, it supports analysis and optimization. However, replacing certified tax accountant or CPA work, acting as a tax agent or filing on behalf of clients, and representing tax appeals or adjudications are outside the scope of this skill."
---

# Tax Calculator — Full Tax Calculation & Tax-Saving Strategy Pipeline

An agent team collaborates to produce income analysis → deduction optimization → tax calculation → tax-saving simulation → filing preparation in one pass.

## Execution Modes

**Agent Team** — 4 agents communicate directly via SendMessage and cross-validate each other.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| income-analyst | `.claude/agents/income-analyst.md` | Income classification, taxable income calculation | general-purpose |
| deduction-optimizer | `.claude/agents/deduction-optimizer.md` | Income deduction & tax credit optimization | general-purpose |
| tax-engine | `.claude/agents/tax-engine.md` | Tax calculation, payable/refund amount | general-purpose |
| strategy-advisor | `.claude/agents/strategy-advisor.md` | Tax-saving simulation, filing preparation | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Income information**: Employment income (gross salary), business income, financial income, miscellaneous income
    - **Family composition**: Spouse, dependents (for personal exemptions)
    - **Deduction items** (optional): Insurance premiums, medical expenses, education costs, donations, pension savings, etc.
    - **Pre-paid tax** (optional): Withheld tax at source, interim prepayment
    - **Tax year**: Attribution year
2. Create a `_workspace/` directory in the project root
3. Organize input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Income analysis | analyst | None | `_workspace/01_income_analysis.md` |
| 2 | Deduction optimization | optimizer | Task 1 | `_workspace/02_deduction_optimization.md` |
| 3 | Tax calculation | engine | Tasks 1, 2 | `_workspace/03_tax_calculation.md` |
| 4 | Tax strategy + filing prep | advisor | Tasks 1, 2, 3 | `_workspace/04_tax_strategy.md`, `_workspace/05_filing_preparation.md` |

This workflow is **sequential** — each step depends on the previous one.

**Inter-agent communication flow:**
- analyst completes → passes comprehensive income amount & tax bracket to optimizer, passes taxable income basis to engine
- optimizer completes → passes deduction totals to engine, passes unused deduction items to advisor
- engine completes → passes final tax amount, effective tax rate & tax bracket analysis to advisor
- advisor synthesizes all results to build tax-saving strategies + filing guide

### Phase 3: Integration and Final Outputs

1. Review all files in `_workspace/`
2. Validate consistency of calculated figures (accuracy of the income → deduction → tax chain)
3. Report final summary to user:
    - Income analysis — `01_income_analysis.md`
    - Deduction optimization — `02_deduction_optimization.md`
    - Tax calculation statement — `03_tax_calculation.md`
    - Tax-saving strategy — `04_tax_strategy.md`
    - Filing preparation — `05_filing_preparation.md`

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Engaged |
|----------------|----------|-------------|
| "Calculate all my taxes and show me how to save" | **Full Pipeline** | All 4 agents |
| "How much tax on an annual salary of 50M KRW?" | **Quick Calculation Mode** | analyst + engine |
| "Optimize my deduction items" | **Deduction Mode** | analyst + optimizer |
| "Just tell me how to save on taxes" | **Strategy Mode** | advisor (uses existing tax info) |
| "What do I need to prepare for year-end settlement?" | **Filing Prep Mode** | advisor solo |

**Using existing files**: If the user provides an existing withholding tax receipt or similar, extract that data and incorporate it into `_workspace/`.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share primary outputs |
| Message-based | SendMessage | Real-time delivery of key information, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

Filename convention: `{order}_{agent}_{output}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient income information | Calculate with information provided, note "additional income verification required" |
| Unclear tax year | Apply latest tax law, note "attribution year verification required" |
| Calculated figure mismatch | Request re-validation of prior step (max 2 times) |
| Agent failure | 1 retry → if still failing, proceed without that output and note the omission in the report |
| Complex tax structure | Note "tax accountant consultation recommended" + provide basic analysis only |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm a salaried worker earning 70M KRW annually, with 1 spouse and 2 children. I contributed 4M KRW to pension savings and spent 20M KRW on credit cards. Calculate my taxes and show me how to save."
**Expected Result**:
- Income analysis: Gross salary 70M KRW → employment income deduction → net employment income calculated
- Deduction optimization: Personal exemptions (4 people), pension savings tax credit, credit card deduction, etc. — optimal combination
- Tax calculation: Full process from taxable income → calculated tax → final tax → payable/refund amount
- Tax-saving strategy: IRP additional contribution, medical expense deduction utilization, etc. — 3+ simulations
- Filing preparation: Required documentation checklist, HomeTax filing guide

### Existing File Flow
**Prompt**: "This is last year's withholding tax receipt — analyze it for me" + file attachment
**Expected Result**:
- Extract income, deduction, and tax data from the withholding tax receipt
- Analyze current deduction status + identify additional tax-saving opportunities

### Error Flow
**Prompt**: "I'm a freelancer with annual revenue of 100M KRW — how much tax do I owe?"
**Expected Result**:
- Classify as business income, apply expense ratio (simplified expense ratio / standard expense ratio)
- Simulate tax differences based on expense documentation method
- Explain differences based on business registration status
- Provide information on regional health insurance premium burden

## Per-Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| deduction-optimizer | `deduction-optimizer-engine` | Deduction limit tables, optimization algorithm, credit card allocation |
| tax-engine, strategy-advisor | `tax-bracket-simulator` | Tax bracket analysis, tax simulation, marginal tax rate calculation |
