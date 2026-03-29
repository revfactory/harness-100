---
name: technical-writer
description: "A pipeline where an agent team collaborates to professionally produce technical documentation. Use this skill for all technical writing topics: 'write technical documentation', 'API documentation', 'architecture document', 'user guide', 'developer documentation', 'write a README', 'create a tutorial', 'operations manual', 'technical blog', 'documentation', and 'technical specification'. Supports review and improvement of existing code or documents as well. Source code writing, test execution, CI/CD setup, and actual document hosting deployment are outside this skill's scope."
---

# Technical Writer — Technical Documentation Pipeline

An agent team collaborates to generate structure design, body text, diagrams, review, and version management all at once.

## Execution Mode

**Agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| info-architect | `.claude/agents/info-architect.md` | Structure design, audience analysis, table of contents | general-purpose |
| doc-writer | `.claude/agents/doc-writer.md` | Body text writing, code examples, tutorials | general-purpose |
| diagram-maker | `.claude/agents/diagram-maker.md` | Mermaid diagrams, visual materials | general-purpose |
| tech-reviewer | `.claude/agents/tech-reviewer.md` | Accuracy, completeness, consistency verification | general-purpose |
| version-controller | `.claude/agents/version-controller.md` | Metadata, change history, deployment | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Document topic**: What is the document about?
    - **Document type** (optional): API / tutorial / guide / architecture / operations
    - **Target audience** (optional): Role, technical level
    - **Reference materials** (optional): Source code, existing documents, specs
    - **Existing files** (optional): Existing document draft, structure outline
2. Create the `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Responsible | Dependency | Deliverable |
|-------|------|-------------|------------|-------------|
| 1 | Structure design | architect | None | `_workspace/01_doc_structure.md` |
| 2a | Body text writing | writer | Task 1 | `_workspace/02_doc_draft.md` |
| 2b | Diagram creation | diagram | Task 1 | `_workspace/03_diagrams.md` |
| 3 | Technical review | reviewer | Tasks 2a, 2b | `_workspace/04_review_report.md` |
| 4 | Version management | version | Tasks 1–3 | `_workspace/05_version_meta.md` |

Tasks 2a (body text) and 2b (diagrams) are **executed in parallel**. Both depend only on Task 1 (structure), so they can start simultaneously.

**Inter-team communication flow:**
- architect completes → delivers table of contents and content strategy to writer, diagram requirements to diagram, and metadata to version
- writer ↔ diagram: coordinate insertion positions and captions
- reviewer cross-verifies body text + diagrams. When a 🔴 required fix is found, request revision from the relevant agent → rework → re-verify (up to 2 rounds)
- version incorporates review results and finalizes metadata

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 required fixes from the review report have been addressed
3. Report the final summary to the user:
    - Document structure — `01_doc_structure.md`
    - Document body text — `02_doc_draft.md`
    - Diagrams — `03_diagrams.md`
    - Review report — `04_review_report.md`
    - Version metadata — `05_version_meta.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------------|----------------|-----------------|
| "Write the full technical documentation" | **Full pipeline** | All 5 agents |
| "Just design the document structure" | **Design mode** | architect + reviewer |
| "Write the document with this content" (structure provided) | **Writing mode** | writer + diagram + reviewer |
| "Add diagrams to this document" | **Diagram mode** | diagram + reviewer |
| "Review this document" | **Review mode** | reviewer only |
| "Update this document" (existing version) | **Update mode** | writer + reviewer + version |

**Using existing files**: If existing documents, code, or specs are provided, skip the corresponding step or work from the existing materials.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|------------|----------|
| Document topic / scope unclear | Present audience and purpose candidates; prompt a selection |
| Insufficient technical details | Insert [Verification Needed] tag; validate during review |
| Code example cannot be verified | Mark "Verification Required"; advise the reader to test |
| Agent failure | Retry once → if it fails, proceed without that deliverable and note the gap in the review report |
| 🔴 finding in review | Request revision from the relevant agent → rework → re-verify (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Document our team's payment API. The audience is external developers, and there are 5 REST API endpoints."
**Expected result**:
- Structure: API reference type; audience analysis targeting external developers; endpoint-based section design
- Body text: Authentication, 5 endpoints in detail, error codes, example code
- Diagrams: Authentication flow sequence diagram, payment process flowchart
- Review: Technical accuracy and completeness verified
- Version: v1.0.0, Published status

### Existing File Utilization Flow
**Prompt**: "The document structure is already in place — please write the body text" + structure file attached
**Expected result**:
- Writing mode: writer + diagram + reviewer deployed
- architect skipped; work based on existing structure

### Error Flow
**Prompt**: "Write technical documentation — the topic is roughly our entire system"
**Expected result**:
- Scope too broad → architect proposes document separation (architecture overview, API, operations guide, etc.)
- Audience unclear → present candidates: internal developers / external developers / operations team
- Work on the highest-priority document first

## Extension Skills by Agent

Domain-specific skills that enhance each agent's expertise:

| Extension Skill | Path | Target Agent | Role |
|-----------------|------|-------------|------|
| diagram-patterns | `.claude/skills/diagram-patterns/skill.md` | diagram-maker | Mermaid diagram pattern library (architecture, sequence, flowchart, ER, state diagrams) |
| api-doc-standards | `.claude/skills/api-doc-standards/skill.md` | doc-writer | REST API documentation standards (endpoint templates, error codes, pagination, authentication) |
| code-example-patterns | `.claude/skills/code-example-patterns/skill.md` | doc-writer | Code example patterns (5-step structure, per-language styles, tutorial composition) |
