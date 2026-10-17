---
name: onboarding-system
description: "A full pipeline where an agent team collaborates to generate onboarding checklists, training, mentor assignments, and 30-60-90 day plans for new hires all at once. Use this skill for 'onboarding', 'new hire', 'new employee training', 'onboarding checklist', 'mentor assignment', '30-60-90', 'onboarding program', 'new employee orientation', 'onboarding process', 'first day', 'new employee adaptation', and similar new hire onboarding topics. Applicable to full-time, contract, intern, and remote new hires. Note: actual HR system (SAP, Workday) integration, payroll/tax processing, legal review of employment contracts, and security system access provisioning are out of scope."
---

# Onboarding System — New Hire Onboarding Full Pipeline

Generates new hire onboarding checklists, training, mentor assignments, and 30-60-90 day plans through agent team collaboration in a single pass.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| onboarding-architect | `.claude/agents/onboarding-architect.md` | Checklists, schedules, stakeholders | general-purpose |
| training-builder | `.claude/agents/training-builder.md` | Curriculum, learning materials, quizzes | general-purpose |
| mentor-matcher | `.claude/agents/mentor-matcher.md` | Mentor/buddy assignment, guides | general-purpose |
| milestone-tracker | `.claude/agents/milestone-tracker.md` | 30-60-90 goals, feedback | general-purpose |
| experience-reviewer | `.claude/agents/experience-reviewer.md` | Consistency, overload, report | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **New hire info**: Role, level, employment type
    - **Organisation info**: Team size, work arrangement (office/remote/hybrid)
    - **Start date**: First day
    - **Special requirements** (optional): Remote start, international hire, experienced/entry-level
    - **Existing materials** (optional): Existing onboarding docs, training materials
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing materials are provided, copy to `_workspace/` and adjust the relevant Phase
5. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Onboarding checklist | architect | None | `_workspace/01_onboarding_checklist.md` |
| 2a | Training program | builder | Task 1 | `_workspace/02_training_program.md` |
| 2b | Mentor guide | matcher | Task 1 | `_workspace/03_mentor_guide.md` |
| 3 | 30-60-90 plan | tracker | Tasks 1, 2a, 2b | `_workspace/04_30_60_90_plan.md` |
| 4 | Experience review | reviewer | Tasks 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (training) and 2b (mentor) run **in parallel**. Both depend only on Task 1 (checklist).

**Inter-team communication flow:**
- architect completes → sends learning goals/system list to builder, role definitions to matcher
- builder + matcher share mutually → agree on mentor training responsibility areas
- builder + matcher complete → send training completion criteria and mentoring milestones to tracker
- tracker completes → sends 30-60-90 goals and feedback framework to reviewer
- reviewer cross-validates all deliverables; requests corrections for inconsistencies/overload (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Incorporate reviewer's consistency validation and overload analysis results
3. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|----------------|-----------------|
| "Create a complete onboarding program" | **Full Pipeline** | All 5 |
| "Just the onboarding checklist" | **Checklist Mode** | architect solo |
| "Just create a 30-60-90 plan" | **Milestone Mode** | architect + tracker |
| "Just design a mentor program" | **Mentor Mode** | matcher solo |
| "Just create a training curriculum" | **Training Mode** | architect + builder |

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
| Insufficient role information | architect provides standard templates by job category |
| Unknown organisation size | 3 versions: small (~20), medium (~100), large (100+) |
| Remote new hire | Include remote alternative activities for all items |
| Agent failure | 1 retry → proceed without that deliverable if still failing |
| Overload detected | reviewer requests activity redistribution → readjust (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Create an onboarding program for a senior frontend developer. 20-person team, remote work, starting the 1st of next month."
**Expected Results**:
- Checklist: Pre-boarding D-7 through Day 1 through 90 days, remote setup included
- Training: Tech stack training + codebase onboarding + security training
- Mentor: Senior technical mentor + culture buddy, remote pairing guide
- 30-60-90: Codebase understanding → PR contributions → feature lead
- Review: Activity volume analysis by period, no overload confirmed

### Partial Request Flow
**Prompt**: "Just quickly create an intern onboarding checklist"
**Expected Results**:
- Checklist mode (architect solo)
- Intern-specific checklist (shorter duration, project-focused)
- Single concise deliverable

### Error Flow
**Prompt**: "Create an onboarding program, I don't know the role, just make it generic"
**Expected Results**:
- architect designs a common program for 5 job categories (engineering/product/sales/marketing/operations)
- Role-specific customisation points marked as "[Role-specific additions needed]"
- Curriculum focused on common training (company overview, culture, tools)

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|--------------|------|
| learning-path-design | `.claude/skills/learning-path-design/skill.md` | training-builder, onboarding-architect | 30-60-90 day learning paths, ADDIE, Kirkpatrick assessment |
| buddy-program-guide | `.claude/skills/buddy-program-guide/skill.md` | mentor-matcher | Buddy matching criteria, activity guides, GROW mentoring |
