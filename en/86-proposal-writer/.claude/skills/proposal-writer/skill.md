---
name: proposal-writer
description: "Full pipeline skill where an agent team collaborates to produce a complete proposal — from client analysis through solution design, pricing, differentiation, and document design — in a single run. Use this skill for all proposal writing needs: 'create a proposal', 'write a proposal', 'RFP response', 'sales proposal', 'technical proposal', 'business proposal', 'project proposal', 'bid proposal', 'service proposal', 'solution proposal', etc. If existing client analysis or solution design is available, the skill supports pricing, differentiation, and integration writing. Note: actual bid system registration, e-contracting, and physical proposal printing/binding are outside this skill's scope."
---

# Proposal Writer — Proposal Writing Full Pipeline

An agent team collaborates to produce a complete proposal in a single run: client analysis → solution design → pricing → differentiation → document design.

## Execution Mode

**Agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| client-analyst | `.claude/agents/client-analyst.md` | Client needs, decision-making structure, competitive landscape | general-purpose |
| solution-architect | `.claude/agents/solution-architect.md` | Solution composition, implementation plan, WBS | general-purpose |
| pricing-strategist | `.claude/agents/pricing-strategist.md` | Cost analysis, pricing model, ROI | general-purpose |
| differentiator | `.claude/agents/differentiator.md` | USP, competitive advantage, Win Themes | general-purpose |
| proposal-designer | `.claude/agents/proposal-designer.md` | Integration, design, cross-validation | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Client**: client company name, industry, scale
    - **Proposal target**: product / service / project
    - **RFP** (optional): RFP/RFI document
    - **Competitive situation** (optional): known competitors
    - **Existing materials** (optional): previous proposals, company profile, track record
2. Create the `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Client analysis | analyst | None | `_workspace/01_client_analysis.md` |
| 2a | Solution design | architect | Task 1 | `_workspace/02_solution_design.md` |
| 2b | Differentiation strategy | differentiator | Task 1 | `_workspace/04_differentiation.md` |
| 3 | Pricing strategy | strategist | Tasks 1, 2a | `_workspace/03_pricing_model.md` |
| 4 | Proposal integration and validation | designer | Tasks 2a, 2b, 3 | `_workspace/05_final_proposal.md` |

Tasks 2a (solution) and 2b (differentiation) run **in parallel** — both depend only on Task 1 (client analysis).

**Inter-team communication flow:**
- analyst complete → forward requirements + technical environment to architect; forward competitive analysis + interests to differentiator; forward budget + pricing information to strategist
- architect complete → forward cost components to strategist; forward technical differentiators to differentiator
- differentiator complete → forward value messaging to strategist
- strategist complete → forward pricing strategy document to designer
- designer cross-validates all deliverables. When 🔴 required revisions are found, request rework from the relevant agent → rework → re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in the `_workspace/` directory
2. Confirm that all 🔴 required revisions from the validation report have been addressed
3. Report the final summary to the user:
    - Client analysis — `01_client_analysis.md`
    - Solution design — `02_solution_design.md`
    - Pricing strategy — `03_pricing_model.md`
    - Differentiation strategy — `04_differentiation.md`
    - Final proposal — `05_final_proposal.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Create a proposal", "RFP response" | **Full pipeline** | All 5 agents |
| "Design a solution for this RFP" | **Solution mode** | analyst + architect + designer |
| "Just produce the pricing" (solution provided) | **Pricing mode** | strategist + designer |
| "Strengthen the differentiation of this proposal" | **Differentiation mode** | differentiator + designer |
| "Review this proposal" | **Review mode** | designer only |

**Using existing files**: If the user provides an RFP, existing proposal, or company profile, reflect that content in the work.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|------------|----------|
| Insufficient client information | Infer profile from industry/scale; ask user for key information |
| No RFP | Extract requirements from user input; apply general proposal structure |
| No company information | Ask user about strengths/track record; build differentiation from minimum information |
| Web search failure | Work from user-provided materials; note "External data not obtained" |
| Agent failure | Retry once → if still failing, proceed without that deliverable |
| 🔴 found in validation | Request revision from relevant agent → rework → re-verify (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Create an ERP system proposal for Company A. They are a mid-size manufacturer with $50M in revenue. Competitors are SAP and Douzone."
**Expected output**:
- Client analysis: Company A business overview, Pain Points, decision-making structure, SAP/Douzone competitive analysis
- Solution: ERP architecture, module composition, implementation schedule, WBS
- Pricing: cost analysis, 3 pricing options, ROI (payback period)
- Differentiation: 3 Win Themes, competitive advantage matrix vs. SAP/Douzone
- Proposal: integrated proposal + design guide + consistency matrix confirmed

### RFP-Based Flow
**Prompt**: "Create a proposal for this RFP" + RFP file provided
**Expected output**:
- Decompose RFP requirements item by item → build response table
- Map all requirements to solution components
- Structure proposal around RFP evaluation criteria

### Error Flow
**Prompt**: "Make me a proposal"
**Expected output**:
- Client and proposal target are unclear → ask user for confirmation
- Proceed with work based on the answer
- Note in validation report: "Client information based on estimates — confirmation and revision required"

## Extension Skills by Agent

| Extension Skill | Path | Target Agent | Role |
|----------------|------|-------------|------|
| roi-calculator | `.claude/skills/roi-calculator/skill.md` | pricing-strategist, solution-architect | ROI / TCO / NPV / IRR calculation, scenario analysis |
| win-theme-builder | `.claude/skills/win-theme-builder/skill.md` | differentiator, client-analyst | Win Theme development, competitive positioning, Ghost strategy |
