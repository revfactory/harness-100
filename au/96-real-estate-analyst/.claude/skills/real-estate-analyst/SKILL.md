---
name: real-estate-analyst
description: "Real estate investment analysis pipeline. An agent team collaborates to produce market research, location analysis, profitability analysis, risk assessment, and investment reports. Use this skill for requests such as 'analyse this real estate', 'apartment investment analysis', 'studio apartment yield', 'real estate market research', 'location analysis', 'real estate investment report', 'buy vs lease', 'reconstruction investment analysis', 'commercial property yield analysis', and other general real estate investment analysis tasks. Actual purchase contracts, brokerage services, interior design, and property management are outside the scope of this skill."
---

# Real Estate Analyst — Real Estate Investment Analysis Pipeline

An agent team collaborates to produce market research, location analysis, profitability analysis, risk assessment, and investment reports.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| market-researcher | `.claude/agents/market-researcher.md` | Macroeconomics, regional markets, price trends | general-purpose |
| location-analyst | `.claude/agents/location-analyst.md` | Transit, school districts, commercial areas, development catalysts | general-purpose |
| profitability-analyst | `.claude/agents/profitability-analyst.md` | Rental yield, IRR, cash flow | general-purpose |
| risk-assessor | `.claude/agents/risk-assessor.md` | Regulatory, market, liquidity risks | general-purpose |
| report-writer | `.claude/agents/report-writer.md` | Comprehensive investment report, investment opinion | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Analysis Target**: Specific property (address, listing) or area/type
    - **Investment Objective**: Owner-occupancy / rental income / capital gains / mixed
    - **Budget**: Equity, financing plan
    - **Investment Horizon**: Short-term (1-2 years) / Medium-term (3-5 years) / Long-term (5+ years)
    - **Constraints** (optional): Specific requirements (school district, transit, area, etc.)
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it as `_workspace/00_input.md`
4. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Market Research | researcher | None | `_workspace/01_market_research.md` |
| 1b | Location Analysis | location | None | `_workspace/02_location_analysis.md` |
| 2 | Profitability Analysis | profitability | Tasks 1a, 1b | `_workspace/03_profitability_analysis.md` |
| 3 | Risk Assessment | risk | Tasks 1a, 1b, 2 | `_workspace/04_risk_assessment.md` |
| 4 | Investment Report | writer | Tasks 1a, 1b, 2, 3 | `_workspace/05_investment_report.md` |

Tasks 1a (Market Research) and 1b (Location Analysis) run **in parallel**.

**Inter-Agent Communication Flow:**
- researcher + location complete in parallel -> deliver price, interest rate, and location data to profitability
- researcher -> deliver policy and market risk data to risk
- location -> deliver development catalyst uncertainties and environmental risks to risk
- profitability completes -> deliver leverage and cash flow risk data to risk
- risk completes -> deliver overall risk rating and stress test results to writer
- writer synthesizes all results into the investment report

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] Do the market research price data and the profitability analysis purchase price match?
    - [ ] Is the location score accurately reflected in the report?
    - [ ] Do the risk assessment scenarios align with the profitability analysis scenarios?
    - [ ] Is the investment opinion supported by the analysis results?
3. If discrepancies are found, request corrections from the relevant agent (up to 2 times)
4. Present the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|-----------------|
| "Run a full real estate investment analysis" | **Full Pipeline** | All 5 agents |
| "Just do market research for this area" | **Market Mode** | researcher only |
| "Just analyse this apartment's location" | **Location Mode** | location only |
| "Just calculate the yield" | **Yield Mode** | profitability only |
| "Just assess the investment risks" | **Risk Mode** | researcher + risk |
| "Compare these two properties" | **Comparison Mode** | All 5 agents x 2 properties compared |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-Based | `_workspace/` directory | Store and share main deliverables |
| Message-Based | SendMessage | Real-time key information delivery, correction requests |
| Task-Based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Market data retrieval failure | Work with most recent available data, note the reference date |
| Insufficient property details | Analyse using regional averages, request property specifics from user |
| Tax/legal judgment required | Note "Professional consultation recommended", estimate using standard criteria |
| Unable to form investment opinion | Issue "Hold (additional data needed)" opinion, list required data |
| Agent failure | Retry once -> if still fails, proceed without that deliverable, note in report |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm considering investing in an apartment in Mapo-gu, Ahyeon-dong, Seoul. My budget is $300K equity and $400K in loans. I plan to hold for 3-5 years for both rental income and capital gains."
**Expected Results**:
- Market Research: Mapo-gu sale/lease trends, supply outlook, interest rate environment
- Location Analysis: Ahyeon New Town transit (Line 2, Gyeongui-Jungang Line), school districts, commercial areas, development catalysts
- Profitability: Cap Rate, IRR, optimistic/neutral/pessimistic scenarios, leverage effect
- Risk: Interest rate increase risk, oversupply risk, stress tests
- Report: Executive Summary, investment opinion (Buy/Hold/Avoid), checklist

### Comparative Analysis Flow
**Prompt**: "Which is better, a studio in Gangnam or an apartment in Mapo?"
**Expected Results**:
- Full pipeline analysis for each property
- Comparison table: location score, yield, risk rating side-by-side
- Recommendation by investment objective: Property A for rental income, Property B for capital gains

### Error Flow
**Prompt**: "Is real estate investment a good idea?"
**Expected Results**:
- No specific property/area provided, so only macro market analysis is performed
- Prompt user for specifics: area, budget, objectives
- Provide a general real estate investment checklist

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|-------------|------|
| cap-rate-calculator | `.claude/skills/cap-rate-calculator/skill.md` | profitability-analyst | Cap Rate, Cash-on-Cash, DCF, scenario analysis |
| location-scoring | `.claude/skills/location-scoring/skill.md` | location-analyst | Location scorecard, commercial area analysis, future value |
