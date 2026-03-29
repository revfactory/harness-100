---
name: risk-register
description: "Full project risk management register pipeline. An agent team collaborates to generate all deliverables in a single run, covering risk identification, probability and impact assessment, response strategy development, monitoring planning, and status reporting. Use this skill for any project risk management need, including: 'risk management', 'risk register', 'risk log', 'risk matrix', 'risk assessment', 'risk response', 'project risk management', 'risk monitoring', 'risk report', 'EMV analysis', 'risk heat map'. Does not cover actuarial analysis, financial risk modeling (VaR/CVaR), real-time risk dashboard system development, or ERM (Enterprise Risk Management) software integration."
---

# Risk Register — Project Risk Management Register Full Pipeline

An agent team collaborates to generate all project risk management deliverables in a single run, covering identification → assessment → response → monitoring → reporting.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| risk-identifier | `.claude/agents/risk-identifier.md` | Risk identification, RBS | general-purpose |
| assessment-analyst | `.claude/agents/assessment-analyst.md` | Probability and impact assessment, matrix | general-purpose |
| response-strategist | `.claude/agents/response-strategist.md` | Response strategy, cost-benefit analysis | general-purpose |
| monitoring-planner | `.claude/agents/monitoring-planner.md` | KRIs, triggers, monitoring | general-purpose |
| report-writer | `.claude/agents/report-writer.md` | Dashboard, consolidated report | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Project overview**: Name, objectives, scale, duration
    - **Project type**: IT / Construction / R&D / Manufacturing / Services
    - **Stakeholders**: Key stakeholders and their expectations
    - **Constraints** (optional): Budget, schedule, technical, regulatory
    - **Existing materials** (optional): Prior risk lists, lessons learned
2. Create the `_workspace/` directory at the project root.
3. Organize the input and save to `_workspace/00_input.md`.
4. If existing materials are provided, copy them to `_workspace/` and adjust the relevant phases accordingly.
5. **Determine the execution mode** based on the scope of the request.

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|------------|
| 1 | Risk identification | identifier | None | `_workspace/01_risk_identification.md` |
| 2 | Probability and impact assessment | analyst | Task 1 | `_workspace/02_risk_assessment.md` |
| 3 | Response strategy development | strategist | Tasks 1, 2 | `_workspace/03_response_strategy.md` |
| 4 | Monitoring plan | planner | Tasks 2, 3 | `_workspace/04_monitoring_plan.md` |
| 5 | Status report | writer | Tasks 1, 2, 3, 4 | `_workspace/05_status_report.md` |

**Inter-agent communication flow:**
- identifier completes → delivers risk list and RBS to analyst; delivers owners and dependencies to strategist
- analyst completes → delivers prioritized list and EMV to strategist; delivers scoring criteria to planner
- strategist completes → delivers triggers and success metrics to planner; delivers response summary to writer
- planner completes → delivers monitoring schedule and KRIs to writer
- writer cross-verifies all deliverables; if inconsistency is found, requests revision from the relevant agent (maximum 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`.
2. Reflect writer's consistency verification results.
3. Report the final summary to the user.

## Mode by Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Create a full risk management register" | **Full Pipeline** | All 5 agents |
| "Identify risks only" | **Identification Mode** | identifier only |
| "Assess this risk list" (existing list provided) | **Assessment Mode** | analyst + strategist + writer |
| "Develop response strategies only" | **Response Mode** | strategist + writer |
| "Create a risk status report" (existing register provided) | **Reporting Mode** | writer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|---------|
| Insufficient project information | identifier provides industry-standard risk template; note "[Customization Required]" |
| No quantitative data | analyst uses qualitative assessment; note "[Recommend re-assessment once data is available]" |
| Web search fails | Derive risks from general knowledge; note "Reference Limited" in report |
| Agent failure | Retry once → if still failing, proceed without that deliverable; note the omission in final report |
| Consistency inconsistency | writer requests revision → rework (maximum 2 iterations) |

## Test Scenarios

### Normal Flow
**Prompt**: "Create a risk management register for a 6-month internal ERP system replacement project. Budget: KRW 1 billion, team: 15 members."
**Expected Results**:
- Identification: RBS with 6 categories, 20–30 risks, cascade risk map
- Assessment: 5×5 matrix, EMV calculated, 3–5 Critical risks
- Response: Avoid/mitigate for Critical risks, cost-benefit analysis, residual risks
- Monitoring: 10+ KRIs, weekly/monthly reviews, trigger conditions
- Report: 1-page executive summary, heat map, Top 5 risks

### Existing Materials Flow
**Prompt**: "Develop response strategies for this risk list and create a report" + risk list file
**Expected Results**:
- Copy existing list to `_workspace/01_risk_identification.md`
- Assessment Mode: deploy analyst + strategist + writer
- Skip identifier

### Error Flow
**Prompt**: "Create a risk register — the project is still in the planning stage."
**Expected Results**:
- identifier notes "[Planning Stage]" and derives general project risks + planning-stage-specific risks
- Insufficient quantitative data → analyst focuses on qualitative assessment
- Report recommends "Planning Stage — re-assess at detailed planning milestone"

## Agent Extension Skills

| Extension Skill | Path | Target Agents | Role |
|----------------|------|--------------|------|
| risk-scoring-matrix | `.claude/skills/risk-scoring-matrix/skill.md` | assessment-analyst | 5×5 matrix, RBS, EMV, sensitivity analysis |
| risk-response-patterns | `.claude/skills/risk-response-patterns/skill.md` | response-strategist, monitoring-planner | 4 response strategies, response plan template, monitoring |
