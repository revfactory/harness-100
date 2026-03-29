---
name: personal-finance
description: "A pipeline where an agent team collaborates to comprehensively design personal financial management. Use this skill for requests like 'help me manage my finances', 'organize my budget', 'how to save money', 'how to invest', 'tax savings tips', 'year-end tax optimization', 'retirement planning', 'create a budget', 'savings plan', 'wealth building', 'asset management', 'financial planning', and other personal finance needs. Supports starting from analysis when existing household budget data is available. However, actual financial transaction execution, securities trading, and tax filing services are outside the scope of this skill."
---

# Personal Finance — Personal Financial Management Comprehensive Pipeline

An agent team collaborates to generate income/expense analysis, budget design, investment strategy, tax optimization, and retirement planning all at once.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| financial-analyst | `.claude/agents/financial-analyst.md` | Income/expense analysis, financial health diagnosis | general-purpose |
| budget-planner | `.claude/agents/budget-planner.md` | Budget design, savings plan | general-purpose |
| investment-advisor | `.claude/agents/investment-advisor.md` | Asset allocation, portfolio design | general-purpose |
| tax-strategist | `.claude/agents/tax-strategist.md` | Tax optimization strategy, retirement planning | general-purpose |
| finance-reviewer | `.claude/agents/finance-reviewer.md` | Cross-verification, figure consistency confirmation | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Income Information**: Monthly income, income type (employment/business/freelance)
    - **Expense Information** (optional): Monthly expense breakdown or approximate scale
    - **Assets and Liabilities** (optional): Current assets, loan status
    - **Financial Goals** (optional): Savings, investment, home purchase, retirement, etc.
    - **Existing Files** (optional): Budget data, existing financial plans, etc.
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|--------------|-------------|
| 1 | Income/expense analysis | analyst | None | `_workspace/01_financial_analysis.md` |
| 2 | Budget design | planner | Task 1 | `_workspace/02_budget_plan.md` |
| 3a | Investment strategy | advisor | Tasks 1, 2 | `_workspace/03_investment_strategy.md` |
| 3b | Tax optimization / retirement design | strategist | Tasks 1, 2 | `_workspace/04_tax_strategy.md` |
| 4 | Comprehensive review | reviewer | Tasks 1–3 | `_workspace/05_review_report.md` |

Tasks 3a (investment) and 3b (tax) run **in parallel**. Both depend only on Task 2 (budget) so they can start simultaneously.

**Inter-team Communication Flow:**
- analyst completes → delivers expense structure and reduction opportunities to planner, investable amount and risk profile to advisor, income structure and tax burden to strategist
- planner completes → delivers investable monthly amount to advisor, savings and investment plan to strategist
- advisor ↔ strategist: mutually share tax-advantaged product utilization status
- finance-reviewer cross-validates all deliverables. If 🔴 Must Fix, sends revision request → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Comprehensive financial planning" | **Full Pipeline** | All 5 |
| "Just create a budget" | **Budget Mode** | analyst + planner + reviewer |
| "How should I invest" | **Investment Mode** | analyst + advisor + reviewer |
| "Tell me how to save on taxes" | **Tax Mode** | analyst + strategist + reviewer |
| "Help me plan for retirement" | **Retirement Mode** | analyst + strategist + reviewer |
| "Analyze this budget" | **Analysis Mode** | analyst + reviewer |

**Existing file utilization**: If budget data or existing budget tables are provided, skip the corresponding phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{number}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Financial data not provided | Simulate with average household data, mark as "sample data" |
| Web search failure | Apply general interest/tax rate standards, note "data limitation" |
| Investable amount is 0 | Switch to emergency fund + debt repayment priority strategy |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note omission in review |
| 🔴 found in review | Send revision request → rework → re-validate (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm a salaried worker earning 4,000,000 KRW/month and need comprehensive financial guidance. Monthly rent is 700,000 KRW and I'm barely saving anything."
**Expected Results**:
- Analysis: Diagnose expense structure relative to 4,000,000 KRW income, flag low savings rate
- Budget: 50/30/20-based budget table, minimum monthly savings goal of 800,000 KRW
- Investment: Stable beginner-friendly portfolio, pension savings prioritized
- Tax: Year-end tax optimization, pension savings tax credit utilization
- Review: Figure cross-verification, feasibility confirmation

### Existing File Utilization Flow
**Prompt**: "Build an investment strategy from this budget data" + budget file attached
**Expected Results**:
- Use budget as `_workspace/01_financial_analysis.md` base data
- Investment mode: analyst (data organization) + advisor + reviewer deployed

### Error Flow
**Prompt**: "I want to save money — where do I start?"
**Expected Results**:
- Insufficient financial data → analyst asks basic questions or simulates with average data
- Unclear goal → planner proposes stage-by-stage goals: emergency fund → mid-term → long-term
- Review report notes "accuracy improves with actual data input"

## Agent Extension Skills

| Agent | Extension Skill | Purpose |
|-------|----------------|---------|
| investment-advisor, tax-strategist | `compound-interest-simulator` | Compound interest calculation, asset growth projection, retirement planning |
| financial-analyst, finance-reviewer | `financial-ratio-analyzer` | Financial ratio analysis, health diagnosis, scoring |
