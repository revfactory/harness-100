---
name: operations-manual
description: "An automated operations manual generation pipeline. An agent team collaborates to analyse existing documents and code to produce process flowcharts, step-by-step manuals, FAQs, and training materials. Use this skill for 'create operations manual', 'write SOP', 'auto-generate SOP', 'process documentation', 'manual writing', 'create work guide', 'procedure automation', 'create training materials', and similar process documentation topics. Code review, technical document translation, and marketing content creation are out of scope."
---

# Operations Manual — Automated Operations Manual Generation Pipeline

Analyses existing documents, code, and wikis to produce process flowcharts, step-by-step manuals, FAQs, and training materials through agent team collaboration.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| document-analyst | `.claude/agents/document-analyst.md` | Existing document/code analysis, process extraction | general-purpose |
| flowchart-designer | `.claude/agents/flowchart-designer.md` | Mermaid flowcharts, RACI matrix | general-purpose |
| manual-writer | `.claude/agents/manual-writer.md` | Step-by-step procedures, checklists | general-purpose |
| faq-builder | `.claude/agents/faq-builder.md` | FAQ, troubleshooting, escalation | general-purpose |
| training-producer | `.claude/agents/training-producer.md` | Quizzes, hands-on exercises, summary cards | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Target processes**: Scope of work/systems to document
    - **Source materials**: Existing document paths, code repositories, wiki URLs
    - **Target audience**: New hires/experienced staff/managers — manual users
    - **Constraints** (optional): Specific format requirements, existing manual templates
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If an existing manual is provided, copy to `_workspace/` and switch to update mode
5. Determine the **execution mode** based on the request scope (see "Execution Modes by Scope" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Document/code analysis | analyst | None | `_workspace/01_document_analysis.md` |
| 2 | Process flowcharts | designer | Task 1 | `_workspace/02_process_flowcharts.md` |
| 3a | Step-by-step manual | writer | Tasks 1, 2 | `_workspace/03_step_by_step_manual.md` |
| 3b | FAQ/troubleshooting | faq | Tasks 1, 2 | `_workspace/04_faq_troubleshooting.md` |
| 4 | Training materials | producer | Tasks 3a, 3b | `_workspace/05_training_materials.md` |

Tasks 3a (manual) and 3b (FAQ) run **in parallel**. Both depend only on Tasks 1 and 2, so they can start simultaneously.

**Inter-team communication flow:**
- analyst completes → sends process inventory/branching conditions to designer, raw procedure data/glossary to writer, gap analysis/tacit knowledge to faq
- designer completes → sends flowcharts/RACI to writer, exception flows to faq, Level 0 map to producer
- writer/faq complete → sends manual structure and key FAQ items to producer
- producer generates training materials from all deliverables and performs final consistency validation between manual and training materials

### Phase 3: Integration and Final Deliverables

The orchestrator performs final integration validation:

1. Verify all files in `_workspace/`
2. Cross-validation checklist:
    - [ ] All flowchart processes are described as procedures in the manual
    - [ ] All manual exception situations are reflected in the FAQ
    - [ ] All glossary terms are used consistently in the manual
    - [ ] Quiz content in training materials matches the manual
3. Request corrections from the relevant agent if discrepancies are found (up to 2 rounds)
4. Save validation results to `_workspace/06_review_report.md`
5. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|----------------|-----------------|
| "Create a complete operations manual" | **Full Pipeline** | All 5 |
| "Analyse this code's processes" | **Analysis Mode** | analyst + designer |
| "Add FAQ to this procedure doc" (existing file) | **FAQ Mode** | faq + producer |
| "Update the existing manual" | **Update Mode** | analyst (changes only) + writer + faq |
| "Just create training materials" (existing manual) | **Training Mode** | producer solo |

**Leveraging existing files**: When the user provides existing manuals, procedures, or flowcharts, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent's phase.

## Data Transfer Protocol

| Strategy | Method | Usage |
|----------|--------|-------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{ext}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Source file inaccessible | analyst works with accessible sources only, lists "unanalyzed sources" in report |
| Process extraction impossible | Present interview questions for key processes to user, work from answers |
| Document contradictions | Prioritise code-based behaviour, record contradictions in gap analysis |
| Mermaid rendering limitations | Split complex diagrams into sub-processes, supplement with text descriptions |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note omission in review report |

## Test Scenarios

### Normal Flow
**Prompt**: "Create a deployment process manual for our team. Sources include deploy.sh, CI config files, and existing wiki docs."
**Expected Results**:
- Analysis report: 3 sources analysed, process inventory, glossary
- Flowcharts: Deployment process Levels 0-1, including rollback exception flows
- Manual: Pre/during/post deployment step-by-step procedures, checklists
- FAQ: Deployment failure troubleshooting, rollback decision tree
- Training materials: Deployment hands-on exercise for new developers

### Existing File Flow
**Prompt**: "Based on this procedure doc, just add FAQ and training materials" + existing manual file
**Expected Results**:
- Existing manual copied to `_workspace/03_step_by_step_manual.md`
- FAQ mode: faq extracts exception situations from the manual to create FAQs
- producer generates training materials based on the manual

### Error Flow
**Prompt**: "Create a customer service process manual, there are no docs, I'll explain verbally"
**Expected Results**:
- analyst extracts processes from user description (interview mode)
- Report specifies "Based on verbal description — field verification required"
- All deliverables include "[Verification needed]" tags

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|--------------|------|
| flowchart-standards | `.claude/skills/flowchart-standards/skill.md` | flowchart-designer | Flowchart notation, process patterns, complexity management |
| knowledge-base-design | `.claude/skills/knowledge-base-design/skill.md` | faq-builder, manual-writer | FAQ design, troubleshooting diagnostic trees, knowledge lifecycle |
