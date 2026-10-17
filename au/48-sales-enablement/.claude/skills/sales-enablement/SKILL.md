---
name: sales-enablement
description: "A full B2B sales enablement pipeline. An agent team collaborates to produce customer analysis, customised proposals, presentations, and follow-up plans. Use this skill for 'create a sales proposal,' 'analyse a customer,' 'write a proposal,' 'build a sales presentation,' 'follow-up plan,' 'sales materials,' 'sales strategy,' 'customer proposal,' and 'B2B proposal' — across the full spectrum of sales enablement. It also supports supplementing and extending existing customer analyses or proposals. Note: CRM system implementation, real-time pipeline dashboards, contract legal review, and actual email sending are outside the scope of this skill."
---

# Sales Enablement — Full Sales Enablement Pipeline

An agent team collaborates to generate the full B2B sales pipeline in one pass: Customer Analysis → Proposal → Presentation → Follow-up.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| customer-analyst | `.claude/agents/customer-analyst.md` | Customer profiling, needs, DMU analysis | general-purpose |
| proposal-writer | `.claude/agents/proposal-writer.md` | Customised proposal, ROI, pricing design | general-purpose |
| presenter | `.claude/agents/presenter.md` | Presentation storyline, slide structure | general-purpose |
| followup-manager | `.claude/agents/followup-manager.md` | Follow-up schedule, objection handling, negotiation | general-purpose |
| sales-reviewer | `.claude/agents/sales-reviewer.md` | Cross-verification, consistency checking | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
    - **Customer Info**: Customer company name, industry, size, contact person
    - **Our Info**: Product/service, strengths, price range
    - **Sales Situation**: Deal stage, competitive landscape, timeline
    - **Existing Materials** (optional): Customer analysis, existing proposals, etc.
2. Create the `_workspace/` directory at the project root
3. Organise input and save as `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding phase

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Customer analysis | customer-analyst | None | `_workspace/01_customer_analysis.md` |
| 2 | Proposal writing | proposal-writer | Task 1 | `_workspace/02_proposal.md` |
| 3a | Presentation design | presenter | Tasks 1, 2 | `_workspace/03_presentation.md` |
| 3b | Follow-up planning | followup-manager | Tasks 1, 2 | `_workspace/04_followup_plan.md` |
| 4 | Sales review | sales-reviewer | Tasks 1, 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (Presentation) and 3b (Follow-up) execute **in parallel**. Both depend on Tasks 1 (Customer Analysis) and 2 (Proposal), so they start simultaneously after the proposal is complete.

**Inter-agent communication flow:**
- customer-analyst completes → sends pain points and BANT assessment to proposal-writer
- proposal-writer completes → sends value proposition and ROI to presenter; sends pricing and objections to followup-manager
- presenter completes → sends Q&A predictions to followup-manager
- sales-reviewer cross-verifies all deliverables. When RED Must Fix items are found, sends revision requests to the relevant agent → rework → re-verify (up to 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Create a full sales package" | **Full Pipeline** | All 5 agents |
| "Just write a proposal" | **Proposal Mode** | customer-analyst + proposal-writer + reviewer |
| "Build a sales presentation" (proposal exists) | **Presentation Mode** | presenter + reviewer |
| "Plan a follow-up strategy" | **Follow-up Mode** | followup-manager + reviewer |
| "Review this proposal" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient customer info | Build a hypothesis-based profile using industry/size, tag with "HYPOTHESIS-BASED" |
| Insufficient product info | Draft using a general B2B solution framework, tag with "PRODUCT INFO NEEDED" |
| Web search failure | Proceed with general knowledge, tag with "DATA LIMITED" |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the review report |
| RED found in review | Send revision request to the relevant agent → rework → re-verify (up to 2 iterations) |

## Test Scenarios

### Normal Flow
**Prompt**: "We want to propose our cloud security solution to Acme Corp. It's a $500K annual contract, and the CISO is the decision-maker. They currently use Competitor P's solution."
**Expected Result**:
- Customer Analysis: Profile based on Acme Corp's public info + DMU mapping
- Proposal: Cloud security-specific value proposition + differentiators vs. Competitor P + 3-tier ROI
- Presentation: CISO-perspective messaging emphasis, security ROI visualisation
- Follow-up: Reflects enterprise decision cycle (4-8 weeks), 5+ objection responses

### Existing File Flow
**Prompt**: "I have this customer analysis. Just create the proposal and presentation from it." + attached file
**Expected Result**:
- Copy existing analysis to `_workspace/01_customer_analysis.md`
- Skip customer-analyst; deploy proposal-writer + presenter + reviewer

### Error Flow
**Prompt**: "Create a sales proposal. The customer is a mid-sized company."
**Expected Result**:
- Insufficient customer info → Ask follow-up questions about industry/product
- If only minimal info is provided, generate a general mid-market framework proposal
- Tag with "CUSTOMER CUSTOMISATION NEEDED"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| roi-calculator | `.claude/skills/roi-calculator/skill.md` | proposal-writer, presenter | ROI/TCO/Payback formulas, value quantification framework, 3-stage presentation |
| objection-handler | `.claude/skills/objection-handler/skill.md` | followup-manager, proposal-writer | BANT+C objection classification, LAER response framework, severity assessment, negotiation strategy |
