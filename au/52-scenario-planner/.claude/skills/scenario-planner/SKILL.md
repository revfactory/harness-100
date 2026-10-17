---
name: scenario-planner
description: "A scenario planning full pipeline. An agent team collaborates to generate key variable definition, scenario matrix construction, impact analysis, response strategy, and decision documents. Use this skill for requests like 'scenario analysis', 'future scenarios', 'scenario planning', 'strategic scenarios', 'uncertainty analysis', 'plan scenarios for me', 'scenario matrix', 'response strategy development', 'decision support', and other scenario-based strategic planning needs. Also supports partial pipelines when existing analysis materials are available. However, real-time data collection system construction, enterprise risk management (ERM) software integration, and Monte Carlo simulation code execution are outside the scope of this skill."
---

# Scenario Planner — Scenario Planning Full Pipeline

An agent team collaborates to generate key variable definition, scenario matrix, impact analysis, response strategy, and decision documents.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| variable-analyst | `.claude/agents/variable-analyst.md` | Key variable identification, STEEP analysis, scenario axis determination | general-purpose |
| scenario-designer | `.claude/agents/scenario-designer.md` | 2x2 matrix, scenario narratives, early warning signals | general-purpose |
| impact-assessor | `.claude/agents/impact-assessor.md` | Per-scenario impact analysis, risk-opportunity mapping | general-purpose |
| strategy-architect | `.claude/agents/strategy-architect.md` | Robust/hedge/option strategies, decision triggers | general-purpose |
| integration-reviewer | `.claude/agents/integration-reviewer.md` | Cross-validation, consistency verification, integrated document editing | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Decision Topic**: The strategic question subject to scenario analysis
    - **Time Horizon**: Analysis target period (default 3-5 years if unspecified)
    - **Analysis Scope**: Industry, region, organizational scope
    - **Existing Materials** (optional): Analysis reports, data provided by user
2. Create `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on request scope (see "Execution Modes by Request Scale" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies:

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1 | Key Variable Analysis | variable-analyst | None | `_workspace/01_variable_analysis.md` |
| 2 | Scenario Matrix | scenario-designer | Task 1 | `_workspace/02_scenario_matrix.md` |
| 3 | Impact Analysis | impact-assessor | Tasks 1, 2 | `_workspace/03_impact_assessment.md` |
| 4 | Response Strategy | strategy-architect | Tasks 2, 3 | `_workspace/04_response_strategy.md` |
| 5 | Integration Review + Decision Document | integration-reviewer | Tasks 1-4 | `_workspace/05_decision_document.md`, `_workspace/06_review_report.md` |

**Inter-team Communication Flow:**
- variable-analyst completes → delivers scenario axes, extreme values, predetermined trends to scenario-designer
- scenario-designer completes → delivers 4 scenario narratives, metrics, early warning signals to impact-assessor
- impact-assessor completes → delivers common impacts, key risks/opportunities, vulnerable areas to strategy-architect
- integration-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

Based on the reviewer's report, finalise all deliverables:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user:
    - Key Variable Analysis Report — `01_variable_analysis.md`
    - Scenario Matrix — `02_scenario_matrix.md`
    - Impact Analysis Report — `03_impact_assessment.md`
    - Response Strategy Document — `04_response_strategy.md`
    - Integrated Decision Document — `05_decision_document.md`
    - Review Report — `06_review_report.md`

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Full scenario analysis", "Scenario planning" | **Full Pipeline** | All 5 |
| "Just analyse the key variables" | **Variable Analysis Mode** | variable-analyst + reviewer |
| "Design a scenario matrix" | **Matrix Mode** | variable-analyst + scenario-designer + reviewer |
| "Analyse impact for this scenario" | **Impact Mode** | impact-assessor + reviewer |
| "Develop response strategies" | **Strategy Mode** | strategy-architect + reviewer |
| "Review this scenario plan" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient topic information | Ask follow-up questions about industry, scope, time horizon |
| Web search failure | Work from general knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Logical contradiction between deliverables | Request reconciliation from all related agents, resolve root cause |

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agents | Role |
|-------|------|---------------|------|
| steep-framework | `.claude/skills/steep-framework/skill.md` | variable-analyst | STEEP 6-dimension scanning, uncertainty-impact matrix, trend classification |
| scenario-narrative-engine | `.claude/skills/scenario-narrative-engine/skill.md` | scenario-designer | 2x2 matrix construction, timeline development, early warning signal design |
| decision-trigger-mapper | `.claude/skills/decision-trigger-mapper/skill.md` | strategy-architect | Real options thinking, strategy portfolio, trigger card design, execution roadmap |
