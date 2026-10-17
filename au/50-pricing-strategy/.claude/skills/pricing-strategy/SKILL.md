---
name: pricing-strategy
description: "A full pipeline that systematizes product/service pricing strategy through cost analysis, competitive pricing, value-based pricing, and simulation. Use this skill for requests like 'build a pricing strategy', 'set the price', 'pricing strategy', 'cost analysis', 'competitive pricing research', 'pricing simulation', 'pricing model design', 'create a pricing plan', 'SaaS pricing', 'subscription model design', and other pricing strategy needs. Also supports analysis and optimisation when existing cost data or pricing information is available. However, accounting ledger preparation, tax calculations, payment system development, and real-time dynamic pricing engine construction are outside the scope of this skill."
---

# Pricing Strategy — Pricing Strategy Full Pipeline

An agent team collaborates to derive optimal pricing through cost, competitive, value, and simulation analysis.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| cost-analyst | `.claude/agents/cost-analyst.md` | Cost structure, BEP, margin | general-purpose |
| competitive-analyst | `.claude/agents/competitive-analyst.md` | Competitive pricing, positioning | general-purpose |
| value-assessor | `.claude/agents/value-assessor.md` | Value-based pricing, WTP, segments | general-purpose |
| pricing-simulator | `.claude/agents/pricing-simulator.md` | Scenarios, elasticity, P&L | general-purpose |
| pricing-reviewer | `.claude/agents/pricing-reviewer.md` | Cross-validation, numerical consistency | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Product/Service Information**: Type, features, target customers
    - **Cost Data** (optional): Known cost items
    - **Competitive Information** (optional): Known competitors, prices
    - **Objectives**: Revenue targets, market share targets, margin targets
2. Create `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Cost Analysis | cost-analyst | None | `_workspace/01_cost_analysis.md` |
| 1b | Competitive Pricing Analysis | competitive-analyst | None | `_workspace/02_competitive_pricing.md` |
| 2 | Value-Based Pricing | value-assessor | Tasks 1a, 1b | `_workspace/03_value_pricing.md` |
| 3 | Pricing Simulation | pricing-simulator | Tasks 1a, 1b, 2 | `_workspace/04_pricing_simulation.md` |
| 4 | Pricing Review | pricing-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (Cost) and 1b (Competitive) are **executed in parallel**. Both can start simultaneously as they have no initial dependencies.

**Inter-team Communication Flow:**
- cost-analyst completes → delivers price floor to competitive-analyst, delivers cost structure to value-assessor
- competitive-analyst completes → delivers competitive price range to value-assessor
- value-assessor completes → delivers WTP and pricing model recommendations to pricing-simulator
- pricing-simulator completes → delivers all documents to pricing-reviewer
- pricing-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Build a pricing strategy", "Full pricing analysis" | **Full Pipeline** | All 5 |
| "Just do a cost analysis" | **Cost Mode** | cost-analyst + reviewer |
| "Research competitive pricing" | **Competitive Mode** | competitive-analyst + reviewer |
| "Run a pricing simulation" (with data) | **Simulation Mode** | pricing-simulator + reviewer |
| "Review this pricing strategy" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient cost data | Estimate based on industry benchmarks, tag as "estimates" |
| Competitor pricing undisclosed | Estimate using industry average range, tag as "undisclosed pricing" |
| Web search failure | Work from general knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Numerical contradiction found | Request numerical reconciliation from all related agents |

## Test Scenarios

### Normal Flow
**Prompt**: "I need to set the price for a B2B SaaS project management tool. Server costs are $15K/month, dev team labour is $230K/month. Competitors are Asana and Monday.com. Target ARR of $7.5M within 1 year."
**Expected Results**:
- Cost: SaaS cost structure analysis, per-user unit cost, BEP
- Competitive: Asana/Monday pricing structure research, feature-price comparison
- Value: PM tool value drivers (time savings, collaboration efficiency), segment WTP
- Simulation: 3 scenario P&L, path to $7.5M ARR
- Review: All figures cross-validated

### Existing File Utilisation Flow
**Prompt**: "I've already done the cost analysis. Just do competitive analysis and pricing decision" + cost file attached
**Expected Results**:
- Copy cost file to `_workspace/01_cost_analysis.md`
- Skip cost-analyst and deploy competitive-analyst + value-assessor + simulator + reviewer

### Error Flow
**Prompt**: "Set the price for our app"
**Expected Results**:
- Insufficient product info → ask follow-up questions about product type/target/features
- If only minimal info provided, present an industry-average-based price range
- Include note: "More precise analysis possible with additional data"

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agents | Role |
|-------|------|---------------|------|
| psm-analyzer | `.claude/skills/psm-analyzer/skill.md` | value-assessor, pricing-simulator | Van Westendorp PSM 4 questions, intersection derivation, Gabor-Granger supplement, segment analysis |
| price-elasticity-calculator | `.claude/skills/price-elasticity-calculator/skill.md` | pricing-simulator, competitive-analyst | PED/XED formulas, optimal price derivation, scenario simulation, price increase strategy |
