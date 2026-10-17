---
name: risk-register
description: "project risk managementversus riskidentification, probability·impactassessment, responsestrategyestablish, monitoringplan, statusreport agent team to Korean creation Full pipeline. 'risk management', 'risk etc.recorddepartment', 'risk managementversus', 'risk register', 'risk matrix', 'risk assessment', 'risk response', 'project risk management', 'risk monitoring', 'risk report', 'EMV analysis', 'risk ' etc. project risk management before skill usage. However, insurance total, risk(VaR/CVaR), actualtime risk dashboard whensystem building, ERM(beforecompany risk management) annual is outside this skill's scope."
---

# Risk Register — project risk managementversus Full pipeline

project risk identification→assessment→response→monitoring→reporting An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| risk-identifier | `.claude/agents/risk-identifier.md` | risk identification, RBS | general-purpose |
| assessment-analyst | `.claude/agents/assessment-analyst.md` | probability·impact assessment, matrix | general-purpose |
| response-strategist | `.claude/agents/response-strategist.md` | response strategy, cost- and | general-purpose |
| monitoring-planner | `.claude/agents/monitoring-planner.md` | KRI, , monitoring | general-purpose |
| report-writer | `.claude/agents/report-writer.md` | dashboard, integration report | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **project overview**: people, goal, scale, duration
 - **project type**: IT/case/R&D//service etc.
 - **stakeholder**: core stakeholder and expectedmatters
 - **constraint condition** (optional): budget, schedule, technical, 
 - **existing material** (optional): existing risk list, 
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. existing material `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | risk identification | identifier | None | `_workspace/01_risk_identification.md` |
| 2 | probability·impact assessment | analyst | task 1 | `_workspace/02_risk_assessment.md` |
| 3 | response strategy establish | strategist | task 1, 2 | `_workspace/03_response_strategy.md` |
| 4 | monitoring plan | planner | task 2, 3 | `_workspace/04_monitoring_plan.md` |
| 5 | status report | writer | task 1, 2, 3, 4 | `_workspace/05_status_report.md` |

**teamKRW between flow:**
- identifier complete → analystto risk list·RBS, strategistto ·dependencynature deliver
- analyst complete → strategistto priority·EMV, plannerto score standard deliver
- strategist complete → plannerto ·natureindicator, writerto response summary deliver
- planner complete → writerto monitoring schedule·KRI deliver
- writer all deliverable cross-verification, dayvalue findings when applicable agent revision request (versus 2)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. writer consistency verify result reflected
3. Report the final summary to the user

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "risk managementversus overall create it" | **Full pipeline** | 5people beforeKRW |
| "risk identification only please do" | **identification mode** | identifier |
| " risk list assessmentplease do" (existing list) | **assessment mode** | analyst + strategist + writer |
| "risk response strategy only establishplease do" | **response mode** | strategist + writer |
| "risk status report create it" (existing etc.recorddepartment) | **reporting mode** | writer |

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| project information insufficient | identifier by day risk template provide, "[ needed]" specify |
| data None | analyst nature assessment versus, "[data secure after re-assessment]" tablebasis |
| web search failure | day degree based risk derive, report "reference limitation" specify |
| agent failure | Retry once -> proceed without that deliverable, report specify |
| consistency dayvalue | writer revision request → re-task (versus 2) |

## test scenario

### flow
**Prompt**: "6months companywithin ERP whensystem project risk managementversus create it. budget 1000M, teamKRW 15people."
**expected result**:
- identification: RBS 6items category, risk 20~30case, annual risk 
- assessment: 5×5 matrix, EMV , Critical 3~5case
- response: Critical avoidance/mitigation, cost- and analysis, residual risk
- monitoring: KRI 10items+, weekbetween/monthbetween review, condition
- report: management 1degree, , Top 5 risk

### existing material utilisation flow
**Prompt**: " risk list regarding response strategy establishand report create it" + risk list file
**expected result**:
- existing list `_workspace/01_risk_identification.md` company
- assessment mode: analyst + strategist + writer deploy
- identifier case

### error flow
**Prompt**: "risk managementversus create it, project basis stage"
**expected result**:
- identifier "[basis stage]" specify after general project risk + basis stage risk derive
- data insufficient → analyst nature assessment duringas task
- report "basis stage — detailed timing re-assessment needed" 

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| risk-scoring-matrix | `.claude/skills/risk-scoring-matrix/skill.md` | assessment-analyst | 5x5 matrix, RBS, EMV, also analysis |
| risk-response-patterns | `.claude/skills/risk-response-patterns/skill.md` | response-strategist, monitoring-planner | 4versus response strategy, response planfrom, monitoring |
