---
name: contract-analyzer
description: "A pipeline where an agent team performs contract analysis, drafting, review, and risk assessment. Use this skill for contexts such as 'review the contract', 'contract analysis', 'draft a contract', 'contract risk assessment', 'contract review', 'clause modification', 'contract comparison', 'NDA review', 'service agreement', 'lease agreement', 'employment contract', 'license agreement', and other contract management tasks. Note: Providing legal counsel, conducting litigation, notarization, and court document preparation are outside the scope of this skill."
---

# Contract Analyser — Contract Analysis, Drafting, and Review Pipeline

An agent team collaborates to perform clause analysis, drafting/revision, risk assessment, comparison review, and comprehensive opinion.

> Warning: This pipeline does not replace professional legal advice.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| clause-analyst | `.claude/agents/clause-analyst.md` | Clause structure, interpretation, essential clause verification | general-purpose |
| clause-drafter | `.claude/agents/clause-drafter.md` | Clause drafting, amendment proposals | general-purpose |
| risk-assessor | `.claude/agents/risk-assessor.md` | Legal and business risk assessment | general-purpose |
| comparison-reviewer | `.claude/agents/comparison-reviewer.md` | Standard/previous version comparison, negotiation points | general-purpose |
| contract-coordinator | `.claude/agents/contract-coordinator.md` | Comprehensive opinion, consistency verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Contract Text**: The contract to analyse (file or text)
    - **Contract Type**: Sale/Service/Lease/NDA/Employment/License, etc.
    - **Party Position**: User's position as Party A or Party B
    - **Special Concerns** (optional): Specific clauses, risks, comparison targets
    - **Comparison Target** (optional): Standard template, previous version
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If contract text is available, copy to `_workspace/original_contract.md`
5. Determine the **execution mode** based on the requested scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Clause Analysis | clause-analyst | None | `_workspace/01_clause_analysis.md` |
| 2a | Risk Assessment | risk-assessor | Task 1 | `_workspace/03_risk_assessment.md` |
| 2b | Comparison Review | comparison-reviewer | Task 1 | `_workspace/04_comparison_report.md` |
| 3 | Clause Drafting/Revision | clause-drafter | Tasks 1, 2a, 2b | `_workspace/02_draft_clauses.md` |
| 4 | Comprehensive Opinion | contract-coordinator | Tasks 1, 2a, 2b, 3 | `_workspace/05_final_opinion.md` |

Tasks 2a (Risk) and 2b (Comparison) are executed **in parallel**.

**Inter-agent Communication Flow:**
- clause-analyst completes -> Delivers risk clauses to risk-assessor, structural info to comparison-reviewer
- risk-assessor + comparison-reviewer complete -> Deliver modification requirements to clause-drafter
- clause-drafter completes -> contract-coordinator comprehensively verifies all deliverables
- contract-coordinator: If Red inconsistencies found, requests revision from relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that all Red required actions in the comprehensive opinion are reflected in the amendments
3. Report the final summary to the user:
    - Clause Analysis Report — `01_clause_analysis.md`
    - Amendments — `02_draft_clauses.md`
    - Risk Assessment — `03_risk_assessment.md`
    - Comparison Review — `04_comparison_report.md`
    - Comprehensive Opinion — `05_final_opinion.md`

## Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Review this contract", "Full analysis" | **Full Analysis** | All 5 agents |
| "Draft a contract", "Write a contract" | **Drafting Mode** | clause-drafter + risk-assessor + contract-coordinator |
| "Just assess the risk" | **Risk Mode** | clause-analyst + risk-assessor |
| "Compare with previous version" | **Comparison Mode** | clause-analyst + comparison-reviewer |
| "Modify this clause" | **Amendment Mode** | clause-drafter only |

**Using Existing Files**: If comparison targets (standard, previous version) are provided, comparison-reviewer utilises them.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time delivery of key information, revision requests |
| Web Browsing | WebSearch/WebFetch | Standard templates, related laws, case law research |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No contract text | Switch to drafting mode based on standard template for the contract type |
| Party position unclear | Analyse from both Party A and Party B perspectives, request position confirmation from user |
| Governing law unclear | Default analysis based on domestic law, note possibility of other applicable laws |
| Web search failure | Work based on general legal knowledge, note "latest case law unverified" |
| Agent failure | Retry once -> if failed, proceed without that deliverable, note omission in report |

## Test Scenarios

### Normal Flow
**Prompt**: "Review this software development service contract. We are Party B (the contractor)." + contract file provided
**Expected Results**:
- Clause Analysis: Full structure map, clause-by-clause legal and practical analysis, essential clause check
- Risk Assessment: Risks from Party B's perspective, disadvantageous clause identification, mitigation strategies
- Comparison Review: Differences from software development standard contract
- Amendments: Revised wording for disadvantageous clauses, additional protective clauses
- Comprehensive Opinion: Signing feasibility, required modification list, checklist

### New Drafting Flow
**Prompt**: "Draft a freelance design service contract. I am Party A."
**Expected Results**:
- Drafting Mode: clause-drafter creates standard service contract draft
- risk-assessor checks risks of the drafted document
- contract-coordinator performs final verification

### Error Flow
**Prompt**: "Check if this contract is okay" + English NDA provided
**Expected Results**:
- English NDA analysis, key terms annotated in both languages
- Analysis based on domestic law, with explanation of common law practice differences
- Governing law verification recommendation included in comprehensive opinion

## Agent Extension Skills

| Agent | Extension Skill | Purpose |
|-------|----------------|---------|
| risk-assessor, clause-analyst | `clause-risk-database` | Risk clause pattern DB, risk scoring algorithm |
| clause-drafter, comparison-reviewer | `negotiation-playbook` | Negotiation strategy framework, amendment wording templates |
