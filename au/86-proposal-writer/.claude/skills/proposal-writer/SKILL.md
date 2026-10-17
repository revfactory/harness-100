---
name: proposal-writer
description: "proposal agent team to clientanalysis→solutiondesign→price→differentiation→specialistpersonto Korean creation Full pipeline. 'proposal create it', 'proposal writing', 'RFP response', ' proposal', 'technical proposal', 'company proposal', 'project proposal', ' proposal', 'service proposal', 'solution proposal' etc. proposal writing before skill usage. existing client analysis solution design price·differentiation·integration writing degreeKRW. However, actual whensystem etc.record, beforespecialisttotalapprox., quality proposal person/person is outside this skill's scope."
---

# Proposal Writer — proposal writing Full pipeline

proposal clientanalysis→solutiondesign→price→differentiation→specialistperson An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| client-analyst | `.claude/agents/client-analyst.md` | client , decision-makingstructure, competitionsituation | general-purpose |
| solution-architect | `.claude/agents/solution-architect.md` | solution composition, implementation plan, WBS | general-purpose |
| pricing-strategist | `.claude/agents/pricing-strategist.md` | KRW, price model, ROI | general-purpose |
| differentiator | `.claude/agents/differentiator.md` | USP, competitionadvantage, Win Theme | general-purpose |
| proposal-designer | `.claude/agents/proposal-designer.md` | integration composition, specialistperson, cross-verification | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **client**: clientcompanypeople, , scale
 - **proposal target**: /service/project
 - **RFP** (optional): RFP/RFI document
 - **competition situation** (optional): competitor
 - **existing material** (optional): before proposal, company itemsfrom, results material
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | client analysis | analyst | None | `_workspace/01_client_analysis.md` |
| 2a | solution design | architect | task 1 | `_workspace/02_solution_design.md` |
| 2b | differentiation strategy | differentiator | task 1 | `_workspace/04_differentiation.md` |
| 3 | price strategy | strategist | task 1, 2a | `_workspace/03_pricing_model.md` |
| 4 | proposal integration and verify | designer | task 2a, 2b, 3 | `_workspace/05_final_proposal.md` |

task 2a(solution) and 2b(differentiation) ** execution**. task 1(clientanalysis) only dependency.

**teamKRW between flow:**
- analyst complete → architectto requirements+technicalenvironment deliver, differentiatorto competitionanalysis+company deliver, strategistto budget+priceinformation deliver
- architect complete → strategistto KRW element deliver, differentiatorto technical gapbypoint deliver
- differentiator complete → strategistto value message deliver
- strategist complete → designerto price strategyfrom deliver
- designer all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - client analysis — `01_client_analysis.md`
 - solution design — `02_solution_design.md`
 - price strategy — `03_pricing_model.md`
 - differentiation strategy — `04_differentiation.md`
 - final proposal — `05_final_proposal.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "proposal create it", "RFP response" | **Full pipeline** | 5people beforeKRW |
| " RFP solution designplease do" | **solution mode** | analyst + architect + designer |
| "price only " (solution provide) | **price mode** | strategist + designer |
| " proposal differentiation point reportplease do" | **differentiation mode** | differentiator + designer |
| " proposal reviewplease do" | **review mode** | designer |

**existing file utilisation**: user RFP, existing proposal, company itemsfrom provide applicable content reflected.

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| client information insufficient | /scalefrom file , userto core information question |
| RFP None | user inputfrom requirements , proposal structure applied |
| specialistcompany information None | userto strength/results question, minimum information differentiation composition |
| web search failure | user provide material based task, "external data un-secure" specify |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |

## test scenario

### flow
**Prompt**: "Acompany ERP whensystem proposal create it. duringbasis sales 50000M scale. competitor SAP ."
**expected result**:
- client analysis: Acompany , Pain Point, decision-making structure, SAP/ competition analysis
- solution: ERP , composition, implementation schedule, WBS
- price: KRW analysis, 3degree price option, ROI(investment number duration)
- differentiation: Win Theme 3items, SAP/ versus advantage matrix
- proposal: integration proposal + specialistperson guide + consistency matrix confirm

### RFP based flow
**Prompt**: " RFP proposal create it" + RFP file provide
**expected result**:
- RFP requirements itemby minute → responsetable writing
- all requirements regarding solution mapping
- RFP assessment standard proposal structure

### error flow
**Prompt**: "proposal create it"
**expected result**:
- client/proposal target people → userto confirm question
- answer basedas task progress
- verify report "client information estimation based — confirm after revision needed" specify

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| roi-calculator | `.claude/skills/roi-calculator/skill.md` | pricing-strategist, solution-architect | ROI/TCO/NPV/IRR calculation, scenario analysis |
| win-theme-builder | `.claude/skills/win-theme-builder/skill.md` | differentiator, client-analyst | Win Theme building, competition positioning, Ghost strategy |
