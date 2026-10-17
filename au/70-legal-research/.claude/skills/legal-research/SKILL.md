---
name: legal-research
description: "Full legal research pipeline. An agent team collaborates to perform case search → legal doctrine analysis → opinion drafting → strategy formulation in one pass. Use this skill for all legal research tasks including 'legal research', 'case search', 'legal doctrine analysis', 'legal opinion', 'litigation strategy', 'legal issue analysis', 'legal review', 'dispute response strategy', 'legal risk analysis', 'legal advisory materials', etc. However, actual legal advice (attorney opinion letters), litigation/arbitration representation, direct integration with legal databases (comprehensive legal information systems), and notarization of legal documents are outside the scope of this skill."
---

# Legal Research — Legal Research Pipeline

Systematically performs case search, legal doctrine analysis, opinion drafting, and strategy formulation for legal issues.

## Execution Modes

**Agent Team** — 4 agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| case-searcher | `.claude/agents/case-searcher.md` | Case search, trend analysis | general-purpose |
| legal-analyst | `.claude/agents/legal-analyst.md` | Issue identification, legal doctrine analysis | general-purpose |
| opinion-writer | `.claude/agents/opinion-writer.md` | Legal opinion drafting | general-purpose |
| strategy-advisor | `.claude/agents/strategy-advisor.md` | Strategy formulation, risk assessment | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Legal Issue**: Specific legal question or dispute situation
    - **Facts**: Facts of the relevant case
    - **Relevant Legal Domain**: Civil, criminal, administrative, labor, intellectual property, etc.
    - **Client Position**: Plaintiff / defendant / victim / other
    - **Existing Materials** (optional): Contracts, evidence, prior opinions, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Output |
|------|------|------|------|--------|
| 1 | Case search | case-searcher | None | `_workspace/01_case_search.md` |
| 2 | Legal doctrine analysis | legal-analyst | Task 1 | `_workspace/02_legal_analysis.md` |
| 3 | Opinion drafting | opinion-writer | Tasks 1, 2 | `_workspace/03_legal_opinion.md` |
| 4 | Strategy formulation | strategy-advisor | Tasks 2, 3 | `_workspace/04_legal_strategy.md` |

**Inter-team Communication Flow:**
- case-searcher completes → delivers key cases and issue-by-issue classification to legal-analyst
- legal-analyst completes → delivers issue structure map and legal doctrine analysis to opinion-writer; delivers win probability assessment to strategy-advisor
- opinion-writer completes → delivers opinion conclusions and certainty level to strategy-advisor
- strategy-advisor cross-validates logical consistency across all outputs when drafting the final report

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify logical consistency across case search → legal doctrine → opinion → strategy
3. Report final summary to the user:
    - Case Search Report — `01_case_search.md`
    - Legal Doctrine Analysis Report — `02_legal_analysis.md`
    - Legal Opinion — `03_legal_opinion.md`
    - Strategy Formulation Report — `04_legal_strategy.md`

## Modes by Task Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------|----------|-------------|
| "Full legal research", "Comprehensive legal issue analysis" | **Full Pipeline** | All 4 agents |
| "Just find relevant cases" | **Case Search Mode** | case-searcher only |
| "Analyze the legal doctrine for this issue" | **Legal Doctrine Analysis Mode** | case-searcher + legal-analyst |
| "Just draft the legal opinion" (analysis already available) | **Opinion Mode** | opinion-writer |
| "Just formulate the litigation strategy" (opinion already available) | **Strategy Mode** | strategy-advisor |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Storing and sharing major deliverables |
| Message-based | SendMessage | Real-time delivery of key information, revision requests |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Web search failure | Case searcher proceeds with general legal knowledge, notes "case DB not queried" |
| Insufficient facts | Ask follow-up questions before proceeding; perform general analysis with minimal information |
| Agent failure | Retry once → if still failing, proceed without that deliverable; note omission in final report |
| Legal judgment uncertainty | Present multiple interpretations, note "professional legal counsel recommended" |
| Logical inconsistency between outputs | strategy-advisor identifies inconsistency and requests re-review |

## Test Scenarios

### Normal Flow
**Prompt**: "When a consumer suffers damages due to delayed delivery from an online shopping mall, please conduct legal research on the seller's liability for damages."
**Expected Results**:
- Case search: 5+ cases related to e-commerce delivery delay damages
- Legal doctrine analysis: Analysis of issues under breach of contract, Consumer Protection Act, and E-Commerce Act
- Opinion: IRAC structure, certainty level noted, disclaimer included
- Strategy: Comparison of litigation / mediation / negotiation options, cost-benefit analysis

### Partial Flow
**Prompt**: "Find cases related to dismissal under the Labor Standards Act."
**Expected Results**:
- Switches to Case Search Mode (case-searcher only)
- List of Supreme Court cases on unfair dismissal, classified by issue

### Error Flow
**Prompt**: "Let me know if there could be any legal issues — I can't share much detail."
**Expected Results**:
- Follow-up questions due to insufficient facts
- General analysis with minimal information, "recommend re-analysis once facts are supplemented"
- Disclaimer emphasized, "professional legal counsel required" noted

## Agent-Specific Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| case-searcher, legal-analyst | `case-analysis-framework` | IRAC framework, case analysis matrix |
| opinion-writer, strategy-advisor | `legal-writing-methodology` | Legal opinion structure, argumentation techniques, strategy frameworks |
