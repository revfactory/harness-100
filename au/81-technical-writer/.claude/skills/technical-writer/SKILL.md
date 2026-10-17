---
name: technical-writer
description: "technical document agent team to specialistqualityas writing pipeline. 'technical document writingplease do', 'API document', ' document', 'user guide', 'developmentspecialist document', 'README writing', ' create it', 'operations ', 'technical blog', 'document', 'documentation', 'technical peopletaxfrom' etc. technical document writing before skill usage. existing code existing document case also review and improvement degreeKRW. However, code writing, test execution, CI/CD building, actual document deployment is outside this skill's scope."
---

# Technical Writer — technical document writing pipeline

structuredesign→→diagram→review→versionmanagement An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| info-architect | `.claude/agents/info-architect.md` | structure design, reader analysis, table of contents | general-purpose |
| doc-writer | `.claude/agents/doc-writer.md` | body text writing, code example, | general-purpose |
| diagram-maker | `.claude/agents/diagram-maker.md` | Mermaid diagram, wheneach material | general-purpose |
| tech-reviewer | `.claude/agents/tech-reviewer.md` | accuracy, completeness, consistency verify | general-purpose |
| version-controller | `.claude/agents/version-controller.md` | data, change capability, deployment | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **document week**: regarding documentperson
 - **document type** (optional): API//guide//operations
 - **target reader** (optional): role, technical level
 - **reference material** (optional): code, existing document, 
 - **existing file** (optional): existing document plan, structureplan
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | structure design | architect | None | `_workspace/01_doc_structure.md` |
| 2a | body text | writer | task 1 | `_workspace/02_doc_draft.md` |
| 2b | diagram writing | diagram | task 1 | `_workspace/03_diagrams.md` |
| 3 | technical review | reviewer | task 2a, 2b | `_workspace/04_review_report.md` |
| 4 | version management | version | task 1~3 | `_workspace/05_version_meta.md` |

task 2a(body text) and 2b(diagram) ** execution**. task 1(structure) only dependency when whenworkto do number .

**teamKRW between flow:**
- architect complete → writerto table of contents·content strategy, diagramto diagram requirement, versionto data deliver
- writer ↔ diagram: position, caption 
- reviewer body text+diagram cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)
- version review result reflectedto final data 

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. review reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - document structure — `01_doc_structure.md`
 - document body text — `02_doc_draft.md`
 - diagram — `03_diagrams.md`
 - review report — `04_review_report.md`
 - version — `05_version_meta.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "technical document overall writing" | **Full pipeline** | 5people beforeKRW |
| "document structure only " | **design mode** | architect + reviewer |
| " contentas document " (structure ) | ** mode** | writer + diagram + reviewer |
| " document diagram addition" | **diagram mode** | diagram + reviewer |
| " document reviewplease do" | **review mode** | reviewer |
| " document please do" (existing version) | ** mode** | writer + reviewer + version |

**existing file utilisation**: existing document, code, provide applicable stage case existing material basedas task.

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
| document week/scope people | reader·purpose afterreport present, optional also |
| technical taxdepartmentmatters insufficient | [confirm needed] , review when verify |
| code example verify impossible | "verify needed" tablewhen, readerto test |
| agent failure | Retry once -> proceed without that deliverable, note the gap in the review report |
| reviewfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |

## test scenario

### flow
**Prompt**: " team API documentplease do. target external developmentspecialist, REST API 5items endpoint ."
**expected result**:
- structure: API reference type, external developmentspecialist target reader analysis, endpointby section design
- body text: authentication, endpoint 5items detailed, error code, example code
- diagram: authentication when, process flowchart
- review: technical accuracy·completeness verify
- version: v1.0.0, Published status

### existing file utilisation flow
**Prompt**: " document structure existing, body text writingplease do" + structure file department
**expected result**:
- mode: writer + diagram + reviewer deploy
- architect case, existing structure based task

### error flow
**Prompt**: "technical document , week versus whensystem before"
**expected result**:
- scope versus → architect document minute proposal ( overview, API, operations guide etc.)
- reader people → withindepartment developmentspecialist/external developmentspecialist/operationsteam afterreport present
- priority documentdepartment task

## agentby extension skill

each agent specialistnature person skill:

| extension skill | | target agent | role |
|----------|------|-------------|------|
| diagram-patterns | `.claude/skills/diagram-patterns/skill.md` | diagram-maker | Mermaid diagram pattern library (, when, flowchart, ER, status diagram) |
| api-doc-standards | `.claude/skills/api-doc-standards/skill.md` | doc-writer | REST API document writing tablelevel (endpoint template, error code, degree, authentication) |
| code-example-patterns | `.claude/skills/code-example-patterns/skill.md` | doc-writer | code example pattern (5stage structure, by style, composition) |
