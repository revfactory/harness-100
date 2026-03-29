---
name: event-organizer
description: "Full pipeline where an agent team collaborates to produce event concept planning, venue and logistics, program design, promotion, execution plan, and post-event evaluation all at once. Use this skill for all event planning and operations requests — 'plan an event', 'prepare a conference', 'design a seminar', 'set up a workshop', 'networking event', 'exhibition planning', 'festival planning', 'event program', 'event promotion', 'event checklist', 'event budget', etc. Applicable to all scales from small team gatherings to large conferences. Out of scope: actual venue booking, payment processing, real-time live streaming operations, and physical print production."
---

# Event Organizer — Full Event Planning and Operations Pipeline

An agent team collaborates to produce all deliverables — concept → venue → program → promotion → execution → post-event evaluation — in a single workflow.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| concept-planner | `.claude/agents/concept-planner.md` | Concept, goals, target audience, budget | general-purpose |
| logistics-manager | `.claude/agents/logistics-manager.md` | Venue, flow, equipment, safety | general-purpose |
| program-designer | `.claude/agents/program-designer.md` | Timetable, sessions, speakers | general-purpose |
| promotion-lead | `.claude/agents/promotion-lead.md` | Channel strategy, promotional content, registration | general-purpose |
| evaluation-analyst | `.claude/agents/evaluation-analyst.md` | KPI, survey, ROI, lessons learned | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Event Purpose**: What the event is for
    - **Event Type**: Conference / Seminar / Workshop / Networking / Exhibition / Festival / etc.
    - **Scale**: Expected number of attendees
    - **Budget** (optional): Total budget or per-person budget
    - **Date / Venue** (optional): Confirmed or preferred conditions
    - **Constraints** (optional): Special requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing materials are available, copy to `_workspace/` and adjust the relevant Phase accordingly
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|-----------|------------|
| 1 | Concept planning | planner | None | `_workspace/01_concept_plan.md` |
| 2a | Logistics | logistics | Task 1 | `_workspace/02_logistics_plan.md` |
| 2b | Program design | designer | Task 1 | `_workspace/03_program_design.md` |
| 3 | Promotion plan | promotion | Tasks 1, 2a, 2b | `_workspace/04_promotion_plan.md` |
| 4 | Evaluation framework | analyst | Tasks 1, 2a, 2b, 3 | `_workspace/05_evaluation_framework.md` |

Tasks 2a (logistics) and 2b (program) run **in parallel** — both depend only on Task 1 (concept).

**Inter-team communication flow:**
- planner complete → send scale/budget/format to logistics; send theme/target/message to designer
- logistics + designer share outputs → verify space ↔ program consistency
- logistics + designer complete → send venue and program information to promotion
- promotion complete → send promotion KPIs to analyst
- analyst cross-verifies all deliverables; requests revisions on discrepancies (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Reflect analyst's consistency verification results
3. Report the final summary to the user

## Mode by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------------|----------------|----------------|
| "Plan the full event" | **Full Pipeline** | All 5 agents |
| "Design the program only" | **Program Mode** | planner + designer |
| "Just the event promotion strategy" | **Promotion Mode** | planner + promotion |
| "Just create the event checklist" | **Checklist Mode** | logistics only |
| "Create the post-event evaluation report" (after event) | **Evaluation Mode** | analyst only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key information transfer and revision requests |
| Task-based | TaskCreate / TaskUpdate | Progress tracking and dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|------------|---------|
| Insufficient event information | planner provides type-specific default templates; marks "[Needs elaboration]" |
| Budget undecided | Provide scenarios for 3 scales (small / medium / large) |
| Venue undecided | logistics provides requirements checklist and selection criteria |
| Agent failure | Retry once → if still failing, proceed without that deliverable |
| Consistency discrepancy | analyst requests revision → rework (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Plan an AI technology conference for 200 attendees. Budget is KRW 50 million, in Seoul, next month."
**Expected results**:
- Concept: AI conference theme/slogan, SMART goals, budget allocation
- Logistics: Seoul 200-person venue requirements, flow design, D-day timeline
- Program: Keynote + 5–6 sessions, speaker profiles, MC cue sheet
- Promotion: D-60 timeline, social media series, email sequence
- Evaluation: KPI measurement system, survey, ROI analysis framework

### Partial Request Flow
**Prompt**: "Just build the program for a half-day team workshop next week. 20 people."
**Expected results**:
- Program Mode (planner + designer)
- Half-day workshop timetable, icebreakers, interactive activities
- Concise deliverables tailored for small-scale event

### Error Flow
**Prompt**: "Plan an event — nothing has been decided yet."
**Expected results**:
- planner proposes 5 event types (by purpose)
- Provides scale / budget / duration guidelines for each type
- Proceeds to full pipeline after user selection

## Per-Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|-----------------|------|-------------|------|
| budget-planning | `.claude/skills/budget-planning/skill.md` | concept-planner, logistics-manager | Budget categories, calculation templates, sponsorship guide |
| venue-evaluation | `.claude/skills/venue-evaluation/skill.md` | logistics-manager | Venue evaluation scorecard, site visit checklist, contract review |
