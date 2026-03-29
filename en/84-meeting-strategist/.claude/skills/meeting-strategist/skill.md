---
name: meeting-strategist
description: "Full pipeline skill where an agent team collaborates to produce a complete meeting strategy document set — from agenda structure design through background research, decision-making frameworks, meeting record templates, and follow-up plans — in a single run. Use this skill for all meeting preparation needs: 'prepare meeting materials', 'create a meeting agenda', 'meeting prep docs', 'meeting strategy', 'decision meeting design', 'board agenda', 'project kickoff meeting', 'team meeting prep', 'workshop design', etc. If an existing agenda is provided, the skill supports background research, framework design, and template creation. Note: actual meeting facilitation (running a video conferencing system), room booking, and attendee scheduling are outside this skill's scope."
---

# Meeting Strategist — Meeting Strategy Document Full Pipeline

An agent team collaborates to produce a complete meeting strategy document set in a single run: agenda structure design → background research → decision-making framework → meeting record templates → follow-up plan.

## Execution Mode

**Agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| agenda-architect | `.claude/agents/agenda-architect.md` | Agenda structure, time allocation, attendee roles | general-purpose |
| background-researcher | `.claude/agents/background-researcher.md` | Background data, stakeholder analysis, case research | general-purpose |
| framework-designer | `.claude/agents/framework-designer.md` | Evaluation criteria, option matrix, consensus methods | general-purpose |
| template-builder | `.claude/agents/template-builder.md` | Meeting minutes, decision records, action item tracker templates | general-purpose |
| followup-planner | `.claude/agents/followup-planner.md` | Execution tracking, cross-validation | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Meeting type**: regular reporting / decision-making / brainstorming / problem-solving / kickoff / retrospective
    - **Meeting purpose**: specific goal to be achieved
    - **Attendees**: headcount, roles, seniority
    - **Duration**: planned meeting length
    - **Existing materials** (optional): previous meeting minutes, agenda draft, related reports
2. Create the `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Agenda structure design | architect | None | `_workspace/01_agenda_design.md` |
| 2a | Background research | researcher | Task 1 | `_workspace/02_background_brief.md` |
| 2b | Decision-making framework | designer | Task 1 | `_workspace/03_decision_framework.md` |
| 3 | Document template creation | builder | Tasks 1, 2b | `_workspace/04_meeting_templates.md` |
| 4 | Follow-up plan and validation | planner | Tasks 2a, 2b, 3 | `_workspace/05_followup_plan.md` |

Tasks 2a (background research) and 2b (framework) run **in parallel** — both depend only on Task 1 (agenda).

**Inter-team communication flow:**
- architect complete → forward required background material list to researcher; forward decision items + initial options to designer
- researcher complete → forward data + constraints to designer; forward pre-meeting context to builder
- designer complete → forward recording forms + voting forms to builder
- planner cross-validates all deliverables. When 🔴 required revisions are found, request rework from the relevant agent → rework → re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in the `_workspace/` directory
2. Confirm that all 🔴 required revisions from the validation report have been addressed
3. Report the final summary to the user:
    - Agenda design document — `01_agenda_design.md`
    - Background brief — `02_background_brief.md`
    - Decision-making framework — `03_decision_framework.md`
    - Meeting document templates — `04_meeting_templates.md`
    - Follow-up plan — `05_followup_plan.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Prepare meeting materials", "full meeting strategy document" | **Full pipeline** | All 5 agents |
| "Just draft the agenda" | **Agenda mode** | architect + planner |
| "Research background for this agenda" (agenda provided) | **Research mode** | researcher + planner |
| "Decision-making framework only" | **Framework mode** | designer + planner |
| "Just create a meeting minutes template" | **Template mode** | builder only |

**Using existing files**: If the user provides an agenda, previous meeting minutes, or other materials, skip the corresponding phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|------------|----------|
| Meeting purpose unclear | Ask user to confirm meeting type and goal |
| No attendee information | Design with generic roles (facilitator / secretary / attendee) |
| Web search failure | Work from user-provided materials and general knowledge; note "External data not obtained" |
| Agent failure | Retry once → if still failing, proceed without that deliverable |
| 🔴 found in validation | Request revision from relevant agent → rework → re-verify (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Prepare next week's executive meeting. The purpose is to finalize the 2025 H2 business plan, with 3 agenda items: new business entry decision, headcount plan, and marketing budget allocation. Attendees are CEO, CFO, COO, Marketing Director, and HR Director. It's a 2-hour meeting."
**Expected output**:
- Agenda design: time allocation, facilitation method, and success criteria for 3 agenda items
- Background brief: data, stakeholder analysis, and benchmarks for each item
- Framework: evaluation criteria, option matrix, and RAPID for 3 decision items
- Templates: meeting minutes, decision record, action item tracker
- Follow-up: execution plan + all consistency matrix items confirmed

### Existing Agenda Flow
**Prompt**: "Create background materials and a decision framework for this agenda" + agenda file provided
**Expected output**:
- Skip agenda design phase
- Copy provided agenda to `_workspace/01_agenda_design.md`
- Deploy researcher + designer + builder + planner

### Error Flow
**Prompt**: "Prepare a team meeting"
**Expected output**:
- Meeting purpose and agenda items are unclear → ask user for confirmation
- Proceed with work based on the answer
- Note in validation report: "Estimated from user input — agenda confirmation required"

## Extension Skills by Agent

| Extension Skill | Path | Target Agent | Role |
|----------------|------|-------------|------|
| decision-frameworks | `.claude/skills/decision-frameworks/skill.md` | framework-designer | DACI, weighted matrix, expected value analysis, consensus methods |
| facilitation-techniques | `.claude/skills/facilitation-techniques/skill.md` | agenda-architect, followup-planner | Facilitation techniques, time management, retrospective patterns |
