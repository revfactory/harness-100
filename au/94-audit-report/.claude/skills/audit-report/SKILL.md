---
name: audit-report
description: "An internal audit report generation pipeline. An agent team collaborates to produce everything from audit scope design through checklists, findings, improvement recommendations, and tracking ledgers. Use this skill for 'create audit report', 'internal audit preparation', 'create audit checklist', 'organise audit findings', 'corrective action plan', 'audit tracking ledger', 'compliance audit', 'operational audit report', and similar internal audit topics. External financial audits, tax investigations, and litigation-related audits are out of scope."
---

# Audit Report — Internal Audit Report Generation Pipeline

Generates audit scope design, checklists, findings analysis, improvement recommendations, and implementation tracking ledgers through agent team collaboration.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| scope-designer | `.claude/agents/scope-designer.md` | Audit scope, criteria, plan design | general-purpose |
| checklist-builder | `.claude/agents/checklist-builder.md` | Control items, test procedures, evidence | general-purpose |
| findings-analyst | `.claude/agents/findings-analyst.md` | Finding 4C analysis, root cause | general-purpose |
| recommendation-writer | `.claude/agents/recommendation-writer.md` | Corrective actions, implementation plans, priorities | general-purpose |
| tracking-manager | `.claude/agents/tracking-manager.md` | Tracking ledger, escalation, closure | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Audit target**: Department, process, system, project
    - **Audit type**: Regular/Special/Follow-up
    - **Audit context**: Regulation changes, incidents, scheduled review
    - **Applicable criteria** (optional): Related laws, policies, industry standards
    - **Existing materials** (optional): Previous audit results, existing checklists
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing materials are provided, copy to `_workspace/` and determine whether to skip the relevant phase
5. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Audit scope design | scope | None | `_workspace/01_audit_scope.md` |
| 2 | Checklist creation | checklist | Task 1 | `_workspace/02_audit_checklist.md` |
| 3 | Findings analysis | findings | Tasks 1, 2 | `_workspace/03_audit_findings.md` |
| 4 | Recommendations | recommendation | Task 3 | `_workspace/04_recommendations.md` |
| 5 | Tracking ledger | tracking | Tasks 3, 4 | `_workspace/05_tracking_ledger.md` |

This workflow is **sequential by default**. Audit processes have strong step-by-step dependencies, limiting parallelization opportunities.

**Inter-team communication flow:**
- scope completes → sends audit criteria/risk assessment to checklist, criteria/rating framework to findings
- checklist completes → sends checklist result framework to findings
- findings completes → sends findings/root causes to recommendation, finding IDs/ratings to tracking
- recommendation completes → sends recommendations/implementation plans/deadlines to tracking
- tracking integrates all information to generate the tracking ledger

### Phase 3: Comprehensive Report Generation

The orchestrator generates the final comprehensive audit report:

1. Verify all files in `_workspace/`
2. Generate comprehensive report at `_workspace/06_final_report.md`:
    - Executive summary (1 page)
    - Audit scope and methodology
    - Findings summary and detail
    - Recommendation summary
    - Implementation tracking plan
3. Cross-validation:
    - [ ] Every finding has a corresponding recommendation
    - [ ] Every recommendation has an implementation deadline and owner
    - [ ] The tracking ledger includes all findings
    - [ ] Risk ratings are consistently applied
4. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|----------------|-----------------|
| "Create a complete internal audit report" | **Full Pipeline** | All 5 |
| "Just create an audit checklist" | **Checklist Mode** | scope + checklist |
| "Write recommendations for these findings" | **Recommendation Mode** | findings + recommendation |
| "Just create an audit tracking ledger" | **Tracking Mode** | tracking solo |
| "Follow-up on previous audit" | **Follow-up Mode** | scope (reduced) + findings + tracking |

**Leveraging existing materials**: When the user provides existing checklists, findings, etc., copy to `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Usage |
|----------|--------|-------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Unclear audit criteria | Apply COSO framework as default, request criteria confirmation from user |
| Insufficient audit target info | Present interview question list to user, work from answers |
| No findings | Write report with "conforming" conclusion, include preventive improvement suggestions |
| Insufficient evidence | Record as provisional findings, establish additional evidence collection plan |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note in report |

## Test Scenarios

### Normal Flow
**Prompt**: "Create an IT department information security internal audit report. Audit access control, change management, and backup areas based on ISO 27001."
**Expected Results**:
- Scope: ISO 27001-based 3 areas, risk assessment, audit schedule
- Checklist: 15-25 control items per area, test procedures, evidence requirements
- Findings: 4C framework, root cause analysis, impact assessment
- Recommendations: SMART-based corrective actions, priority matrix
- Tracking ledger: All findings tracked, escalation procedures, closure criteria

### Existing File Flow
**Prompt**: "Create improvement recommendations and tracking ledger from this findings list" + findings file
**Expected Results**:
- Existing findings copied to `_workspace/03_audit_findings.md`
- Recommendation mode: recommendation + tracking deployed
- Recommendations and tracking ledger generated from findings

### Error Flow
**Prompt**: "Do a company-wide internal audit, I don't know what to look at"
**Expected Results**:
- scope suggests general internal control areas (financial, IT, operations, compliance)
- Requests user to select priorities
- Proceeds with reduced scope on selected areas
- Report includes "Future comprehensive audit roadmap"

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|--------------|------|
| internal-control-framework | `.claude/skills/internal-control-framework/skill.md` | scope-designer, checklist-builder | COSO framework, risk-based audit, control testing |
| finding-classification | `.claude/skills/finding-classification/skill.md` | findings-analyst, recommendation-writer | 4-level findings, 4C reporting, root cause, implementation tracking |
