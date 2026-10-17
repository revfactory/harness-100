---
name: procurement-docs
description: "A procurement document set generation pipeline. An agent team collaborates to produce requirements definitions, vendor comparisons, evaluation criteria, contract terms, and acceptance criteria. Use this skill for 'create procurement documents', 'vendor comparison', 'procurement specifications', 'evaluation criteria', 'acceptance criteria', 'procurement documents', 'bid evaluation', 'RFP creation', 'vendor selection', and similar procurement/sourcing document topics. Actual ordering, contract execution, payment processing, and asset registration are out of scope."
---

# Procurement Docs — Procurement Document Set Generation Pipeline

Generates procurement requirements, vendor comparisons, evaluation criteria, contract term reviews, and acceptance criteria through agent team collaboration.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| requirements-definer | `.claude/agents/requirements-definer.md` | Specifications, quantity, delivery, budget | general-purpose |
| vendor-comparator | `.claude/agents/vendor-comparator.md` | Candidate research, comparison tables, SWOT | general-purpose |
| evaluation-designer | `.claude/agents/evaluation-designer.md` | Scoring, weighting, evaluation process | general-purpose |
| contract-reviewer | `.claude/agents/contract-reviewer.md` | Clauses, risks, SLA, negotiation | general-purpose |
| acceptance-builder | `.claude/agents/acceptance-builder.md` | Inspection items, testing, pass criteria | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Procurement target**: Goods, software, services, construction, etc.
    - **Procurement context**: New introduction, replacement, expansion, etc.
    - **Budget**: Budget range or limit
    - **Timeline**: Desired delivery date, project schedule
    - **Vendor candidates** (optional): Vendors already under consideration
    - **Existing documents** (optional): Existing specifications, contract drafts
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Requirements definition | definer | None | `_workspace/01_requirements_spec.md` |
| 2 | Vendor comparison | comparator | Task 1 | `_workspace/02_vendor_comparison.md` |
| 3a | Evaluation criteria | evaluator | Tasks 1, 2 | `_workspace/03_evaluation_criteria.md` |
| 3b | Contract review | contract | Tasks 1, 2 | `_workspace/04_contract_review.md` |
| 4 | Acceptance criteria | acceptance | Tasks 1, 3b | `_workspace/05_acceptance_criteria.md` |

Tasks 3a (evaluation) and 3b (contract) run **in parallel**.

**Inter-team communication flow:**
- definer completes → sends requirements/budget to comparator, priorities/criteria to evaluator, delivery/support terms to contract, must-have requirements/criteria to acceptance
- comparator completes → sends vendor info/comparison items to evaluator, license/clause highlights to contract
- contract completes → sends acceptance conditions/warranty to acceptance
- Orchestrator performs final cross-document consistency validation

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] All must-have requirements are reflected in acceptance criteria
    - [ ] Evaluation criteria weight totals equal 100%
    - [ ] Contract terms align with requirements/acceptance criteria
    - [ ] Vendor comparison items map to requirements
3. Generate procurement summary report at `_workspace/06_procurement_summary.md`
4. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|----------------|-----------------|
| "Create complete procurement documents" | **Full Pipeline** | All 5 |
| "Just write the requirements spec" | **Spec Mode** | definer solo |
| "Just compare vendors" | **Comparison Mode** | definer + comparator |
| "Just create evaluation criteria" | **Evaluation Mode** | definer + evaluator |
| "Review this contract" | **Review Mode** | contract solo |
| "Just create acceptance criteria" | **Acceptance Mode** | definer + acceptance |

## Data Transfer Protocol

| Strategy | Method | Usage |
|----------|--------|-------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Unclear procurement target | definer presents clarifying question list, works from answers |
| Insufficient vendor info | comparator provides RFI template when web search fails, requests user direct input |
| Budget undetermined | Estimate budget range based on market prices, proceed after user confirmation |
| Legal review needed | contract tags with "[Legal review needed]", warns cannot replace legal counsel |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note in report |

## Test Scenarios

### Normal Flow
**Prompt**: "Create a procurement document set for cloud server hosting services. Budget is $500K/year and I want to compare AWS, Azure, and GCP."
**Expected Results**:
- Spec: Compute/storage/network requirements, SLA requirements
- Comparison: 3-provider feature/price/support comparison, TCO analysis, SWOT
- Evaluation: Technical 40% / Price 30% / Support 20% / Reliability 10% scoring
- Contract: SLA clauses, data sovereignty, termination terms, negotiation points
- Acceptance: Infrastructure deployment acceptance, performance testing, SLA compliance verification

### Existing File Flow
**Prompt**: "I already have a spec. Just create vendor comparison and evaluation criteria." + spec file
**Expected Results**:
- Existing spec copied to `_workspace/01_requirements_spec.md`
- Comparison + evaluation mode: comparator + evaluator deployed
- Vendor comparison and evaluation criteria generated from spec

### Error Flow
**Prompt**: "I need to buy something but don't know what, maybe work laptops?"
**Expected Results**:
- definer presents clarifying questions (use case, number of users, performance needs, etc.)
- Requirements derived from user responses
- Market price range presented if budget is undetermined
- Report notes "Requirements confirmation needed"

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|--------------|------|
| vendor-scoring | `.claude/skills/vendor-scoring/skill.md` | vendor-comparator, evaluation-designer | Vendor evaluation scorecard, pricing formulas, reference checks |
| contract-checklist | `.claude/skills/contract-checklist/skill.md` | contract-reviewer, acceptance-builder | Contract 10 key clauses, SLA design, acceptance criteria |
