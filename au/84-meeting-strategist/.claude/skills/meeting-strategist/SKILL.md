---
name: meeting-strategist
description: "meeting strategy document agent team to agenda itemstructuredesign→backgroundmaterialresearch→decision-makingframework→meetingrecordtemplate→to Korean creation Full pipeline. 'meeting preparationplease do', 'meeting agenda item create it', 'un- preparation material', 'meeting strategy', 'decision-making meeting design', 'company agenda item', 'project meeting', 'team un- preparation', ' design' etc. meeting preparation before skill usage. existing agenda item backgroundmaterial·framework·template writing degreeKRW. However, actual meeting progress(meeting whensystem operations), meetingactual exampleapprox., attendee schedule is outside this skill's scope."
---

# Meeting Strategist — meeting strategy document Full pipeline

meeting strategy document agenda itemstructuredesign→backgroundmaterialresearch→decision-makingframework→meetingrecordtemplate→ An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| agenda-architect | `.claude/agents/agenda-architect.md` | agenda item structure, time allocation, attendee role | general-purpose |
| background-researcher | `.claude/agents/background-researcher.md` | background data, stakeholder, case research | general-purpose |
| framework-designer | `.claude/agents/framework-designer.md` | judgment standard, option matrix, method | general-purpose |
| template-builder | `.claude/agents/template-builder.md` | meetingrecord, basisrecorddegree, trackingtable template | general-purpose |
| followup-planner | `.claude/agents/followup-planner.md` | execution tracking, cross-verification | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **meeting type**: basisreporting/decision-making/person/problem//
 - **meeting purpose**: natureandspecialist specific goal
 - **attendee**: personKRW, role, grade
 - **time**: example time
 - **existing material** (optional): before meetingrecord, agenda item plan, related report
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | agenda item structure design | architect | None | `_workspace/01_agenda_design.md` |
| 2a | background material research | researcher | task 1 | `_workspace/02_background_brief.md` |
| 2b | decision-making framework | designer | task 1 | `_workspace/03_decision_framework.md` |
| 3 | document template creation | builder | task 1, 2b | `_workspace/04_meeting_templates.md` |
| 4 | and verify | planner | task 2a, 2b, 3 | `_workspace/05_followup_plan.md` |

task 2a(backgroundresearch) and 2b(framework) ** execution**. task 1(agenda item) only dependency.

**teamKRW between flow:**
- architect complete → researcherto needed background material list deliver, designerto decision-making agenda item+initial option deliver
- researcher complete → designerto data+constraintcondition deliver, builderto companybefore information deliver
- designer complete → builderto basisrecord +table deliver
- planner all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - agenda item designfrom — `01_agenda_design.md`
 - background material — `02_background_brief.md`
 - decision-making framework — `03_decision_framework.md`
 - meeting document template — `04_meeting_templates.md`
 - — `05_followup_plan.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "meeting preparationplease do", "meeting strategy document overall" | **Full pipeline** | 5people beforeKRW |
| "agenda item only " | **agenda item mode** | architect + planner |
| " agenda itemas backgroundmaterial researchplease do" (agenda item provide) | **research mode** | researcher + planner |
| "decision-making framework" | **framework mode** | designer + planner |
| "meetingrecord template only create it" | **template mode** | builder |

**existing file utilisation**: user agenda item, before meetingrecord etc. provide applicable stage case.

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| meeting purpose people | userto meeting type and goal confirm question |
| attendee information None | role(facilitator/frombasis/attendee) design |
| web search failure | user provide material and day degree based task, "external data un-secure" specify |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |

## test scenario

### flow
**Prompt**: "next week management meeting preparationplease do. 2025year basis company plan purpose, 3items agenda item : company decision, personcapability KRW plan, budget allocation. attendee CEO, CFO, COO, company, HR company. 2time meeting."
**expected result**:
- agenda item design: 3items agenda item time allocation, progress method, nature standard
- background material: each agenda itemby data, stakeholder analysis, value
- framework: 3items agenda item assessment standard, option matrix, RAPID
- template: meetingrecord, decision basisrecorddegree, trackingtable
- : execution plan + consistency matrix beforeitem confirm

### existing agenda item utilisation flow
**Prompt**: " agenda itemas meeting backgroundmaterial framework create it" + agenda item file provide
**expected result**:
- agenda item design case
- providedone agenda item `_workspace/01_agenda_design.md` company
- researcher + designer + builder + planner deploy

### error flow
**Prompt**: "team meeting preparationplease do"
**expected result**:
- meeting purpose and agenda item people userto confirm question
- answer basedas task progress
- verify report "user input based estimation — agenda item needed" specify

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| decision-frameworks | `.claude/skills/decision-frameworks/skill.md` | framework-designer | DACI, during matrix, expected analysis, method |
| facilitation-techniques | `.claude/skills/facilitation-techniques/skill.md` | agenda-architect, followup-planner | facilitation technique, time management, pattern |
