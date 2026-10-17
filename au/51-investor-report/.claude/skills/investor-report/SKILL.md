---
name: investor-report
description: "A full pipeline that systematizes investor reports into financial performance analysis, KPI dashboard, market trends, strategy updates, and risk disclosures. Use this skill for requests like 'create an investor report', 'IR report', 'quarterly report', 'shareholder report', 'earnings report', 'investor update', 'KPI dashboard', 'financial analysis report', 'business report', 'management performance', and other investor communication needs. Also supports analysis and report generation when existing financial data or KPIs are available. However, accounting audits, statutory disclosure documents, securities filings, and stock issuance operations are outside the scope of this skill."
---

# Investor Report — Investor Report Full Pipeline

An agent team collaborates to generate financial, KPI, market, strategy, and risk sections all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| financial-analyst | `.claude/agents/financial-analyst.md` | P&L, cash flow, financial metrics | general-purpose |
| kpi-designer | `.claude/agents/kpi-designer.md` | KPI selection, trends, benchmarks | general-purpose |
| market-analyst | `.claude/agents/market-analyst.md` | Industry trends, competition, regulation | general-purpose |
| strategy-updater | `.claude/agents/strategy-updater.md` | Strategy progress, roadmap, risk, integration | general-purpose |
| ir-reviewer | `.claude/agents/ir-reviewer.md` | Cross-validation, numerical consistency | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Company Information**: Company name, industry, stage (startup/growth/public)
    - **Reporting Period**: Quarterly/semi-annual/annual, target period
    - **Financial Data**: P&L, cash flow, KPIs, etc. (file or text)
    - **Strategy Information** (optional): Existing strategy, initiative progress
    - **Target Investors**: VC/PE/public shareholders/creditors
2. Create `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Financial Analysis | financial-analyst | None | `_workspace/01_financial_analysis.md` |
| 1b | Market Trends | market-analyst | None | `_workspace/03_market_trends.md` |
| 2 | KPI Dashboard | kpi-designer | Task 1a | `_workspace/02_kpi_dashboard.md` |
| 3 | Strategy + Risk + Integration | strategy-updater | Tasks 1a, 1b, 2 | `_workspace/04_strategy_update.md`, `_workspace/06_investor_report_final.md` |
| 4 | IR Review | ir-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (Financial) and 1b (Market) are **executed in parallel**.

**Inter-team Communication Flow:**
- financial-analyst completes → delivers financial KPI data to kpi-designer, requests revenue variance factor analysis from market-analyst
- market-analyst completes → delivers benchmark data to kpi-designer, delivers implications to strategy-updater
- kpi-designer completes → delivers KPI achievement status to strategy-updater
- strategy-updater completes → delivers all documents + final integrated report to ir-reviewer
- ir-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final integrated report (`06_investor_report_final.md`) to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Create an investor report", "Full IR report" | **Full Pipeline** | All 5 |
| "Just do the financial analysis" | **Financial Mode** | financial-analyst + reviewer |
| "Create a KPI dashboard" | **KPI Mode** | kpi-designer + reviewer |
| "Write a market trends report" | **Market Mode** | market-analyst + reviewer |
| "Review this report" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Incomplete financial data | Perform analysis with available data, specify missing items |
| Web search failure | Work from general market knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Numerical discrepancy | Unify using financial analyst as the source of truth |

## Test Scenarios

### Normal Flow
**Prompt**: "Create a Q4 2024 investor report for a Series B SaaS startup. ARR $6M, revenue growth 120% YoY, NRR 115%, 60 employees. Primary investor is ABC Venture Capital."
**Expected Results**:
- Financial: SaaS-specific P&L analysis, ARR/MRR trends, cash runway
- KPI: SaaS core metrics (ARR, NRR, CAC, LTV, Rule of 40) dashboard
- Market: SaaS market trends, competitive developments
- Strategy: Growth strategy update, hiring plan, risk disclosure
- Integration: VC-targeted investor report final version

### Existing File Utilisation Flow
**Prompt**: "Create an investor report with this financial data" + Excel/CSV data attached
**Expected Results**:
- Financial analyst analyses based on financial data (file reference)
- Remaining agents execute normally
- Integrated report completed

### Error Flow
**Prompt**: "Create an investor report, revenue is $3.7M"
**Expected Results**:
- Insufficient financial data → request additional info (costs, growth rate, KPIs)
- If only minimal info provided, generate a general report framework
- Tag as "update needed after data supplementation"

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Agent | Extension Skill | Role |
|-------|----------------|------|
| financial-analyst | `financial-ratio-analyzer` | DuPont analysis, SaaS metrics, 5 financial ratio categories |
| kpi-designer | `kpi-benchmark-engine` | Industry KPI benchmarks, SMART-R selection framework, pyramid structure |
| strategy-updater, ir-reviewer | `ir-narrative-builder` | Equity Story 5 stages, investor-type-specific narrative tone, EBITDA Bridge |
