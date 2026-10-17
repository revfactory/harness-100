---
name: compliance-checker
description: "A full compliance verification pipeline. An agent team collaborates to perform law mapping, status audit, gap analysis, and remediation planning in a single pass. Use this skill for contexts such as 'check regulatory compliance', 'compliance check', 'legal compliance status', 'run gap analysis', 'regulatory response plan', 'legal risk analysis', 'compliance audit', 'regulatory inspection', 'compliance status assessment', and other compliance verification tasks. Note: Actual legal counsel (attorney opinions), litigation representation, administrative filings/submissions, and direct integration with legal databases (case law search systems) are outside the scope of this skill."
---

# Compliance Checker — Compliance Verification Pipeline

Systematically diagnoses an organisation's law and regulation compliance status, analyses gaps, and develops actionable remediation plans.

## Execution Mode

**Agent Team** — 4 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| law-mapper | `.claude/agents/law-mapper.md` | Law identification, clause mapping, obligation extraction | general-purpose |
| status-auditor | `.claude/agents/status-auditor.md` | Status investigation, evidence collection, compliance assessment | general-purpose |
| gap-analyst | `.claude/agents/gap-analyst.md` | Gap identification, risk calculation, priority derivation | general-purpose |
| remediation-planner | `.claude/agents/remediation-planner.md` | Corrective actions, scheduling, monitoring framework | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Target Organization/Service**: Business type and scale of the audit target
    - **Industry/Sector**: Finance, IT, Healthcare, Manufacturing, Education, etc.
    - **Regulatory Domain** (optional): Personal data, finance, labour, environment, etc.
    - **Existing Materials** (optional): Policy documents, compliance reports, org charts, etc.
    - **Focus Areas** (optional): Specific law or specific domain
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing materials are available, copy to `_workspace/` and utilise for the relevant phase
5. Determine the **execution mode** based on the requested scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Law Mapping | law-mapper | None | `_workspace/01_law_mapping.md` |
| 2 | Status Audit | status-auditor | Task 1 | `_workspace/02_status_audit.md` |
| 3 | Gap Analysis | gap-analyst | Tasks 1, 2 | `_workspace/03_gap_analysis.md` |
| 4 | Remediation Plan | remediation-planner | Tasks 1, 2, 3 | `_workspace/04_remediation_plan.md` |

**Inter-agent Communication Flow:**
- law-mapper completes -> Delivers obligation checklist to status-auditor, mapping original to gap-analyst
- status-auditor completes -> Delivers compliance status to gap-analyst, existing infrastructure info to remediation-planner
- gap-analyst completes -> Delivers priority matrix and root cause analysis to remediation-planner
- remediation-planner cross-verifies logical consistency across all deliverables when writing the final report

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that the remediation plan's comprehensive opinion is consistent with law mapping, status audit, and gap analysis
3. Report the final summary to the user:
    - Law Mapping Report — `01_law_mapping.md`
    - Status Audit Report — `02_status_audit.md`
    - Gap Analysis Report — `03_gap_analysis.md`
    - Remediation Plan — `04_remediation_plan.md`

## Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Full compliance check", "Full compliance audit" | **Full Pipeline** | All 4 agents |
| "Tell me which laws apply" | **Law Mapping Mode** | law-mapper only |
| "Just assess current compliance status" (existing mapping available) | **Status Audit Mode** | status-auditor |
| "Just do gap analysis" (mapping + status available) | **Gap Analysis Mode** | gap-analyst |
| "Just create a remediation plan" (gap analysis results available) | **Remediation Plan Mode** | remediation-planner |

**Using Existing Files**: If the user provides existing law mapping, status audit, or other materials, copy them to the appropriate numbered position in `_workspace/` and skip that phase's agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time delivery of key information, revision requests |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Law analyst works based on general knowledge, notes "latest amendments unverified" |
| Insufficient target organisation info | Assume-based audit using general organisation standards, note "assumption-based" |
| Agent failure | Retry once -> if failed, proceed without that deliverable, note omission in final report |
| Uncertain law applicability | Conservatively include, note "professional legal consultation recommended" |
| Gap analysis and status audit inconsistency | remediation-planner identifies inconsistency, applies conservative judgment |

## Test Scenarios

### Normal Flow
**Prompt**: "Run a full check on our online shopping mall's Personal Information Protection Act compliance."
**Expected Results**:
- Law Mapping: Maps applicable laws including Personal Information Protection Act, E-Commerce Act, Information and Communications Network Act
- Status Audit: Compliance status for each obligation including personal data collection, use, provision, destruction
- Gap Analysis: Risk grade for each non-compliant item, 5x5 risk matrix
- Remediation Plan: Short/mid/long-term roadmap, monitoring KPIs

### Partial Flow
**Prompt**: "List the labor-related laws applicable to our company. We're a 50-person IT company."
**Expected Results**:
- Switches to law mapping mode (law-mapper only)
- Lists applicable laws including Labour Standards Act, Occupational Safety and Health Act, Equal Employment Act
- Maps obligations by clause

### Error Flow
**Prompt**: "Check our regulatory compliance, we're a financial company but I don't know the details."
**Expected Results**:
- Full pipeline execution, comprehensively maps financial industry regulations
- Status audit assumes general financial company standards, notes "assumption-based audit"
- Final report includes "recommend re-running gap analysis upon actual status verification"

## Agent Extension Skills

| Agent | Extension Skill | Purpose |
|-------|----------------|---------|
| law-mapper, gap-analyst | `regulation-knowledge-base` | Industry-specific applicable law DB, obligation mapping |
| status-auditor, remediation-planner | `audit-checklist-engine` | Audit checklist generation, compliance maturity assessment |
