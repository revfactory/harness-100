---
name: hiring-pipeline
description: "Full pipeline where an agent team collaborates to produce all hiring process deliverables — JD writing, sourcing, screening, interview design, evaluation, and offer — at once. Use this skill for all recruitment-related requests: 'hire someone', 'talent acquisition', 'write a JD', 'job description', 'job posting', 'interview questions', 'interview design', 'hiring process', 'sourcing strategy', 'screening', 'offer letter', 'hiring pipeline', 'recruiting', etc. Out of scope: ATS platform integration, payroll system enrollment, legal enforceability of employment contracts, and conducting reference checks."
---

# Hiring Pipeline — Full Recruitment Process Pipeline

An agent team collaborates to produce all deliverables — JD writing → sourcing → screening → interview → evaluation → offer — in a single workflow.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| jd-writer | `.claude/agents/jd-writer.md` | Job description, job posting | general-purpose |
| sourcing-specialist | `.claude/agents/sourcing-specialist.md` | Channel strategy, outreach | general-purpose |
| screening-expert | `.claude/agents/screening-expert.md` | Resume evaluation, take-home task, screening | general-purpose |
| interview-designer | `.claude/agents/interview-designer.md` | Structured interview, questions, scorecard | general-purpose |
| offer-coordinator | `.claude/agents/offer-coordinator.md` | Final evaluation, compensation, offer | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Position**: Role and level to hire for
    - **Company Information**: Company name, team structure, culture
    - **Hiring Conditions**: Employment type, work arrangement, salary range
    - **Urgency**: Hiring deadline, number of openings
    - **Existing Materials** (optional): Current JD, applicant status
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing materials are available, copy to `_workspace/` and adjust the relevant Phase accordingly
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|-----------|------------|
| 1 | JD writing | writer | None | `_workspace/01_job_description.md` |
| 2 | Sourcing strategy | sourcing | Task 1 | `_workspace/02_sourcing_strategy.md` |
| 3 | Screening design | screening | Task 1 | `_workspace/03_screening_framework.md` |
| 4 | Interview design | interview | Tasks 1, 3 | `_workspace/04_interview_design.md` |
| 5 | Evaluation and offer | offer | Tasks 1, 2, 3, 4 | `_workspace/05_evaluation_offer.md` |

Tasks 2 (sourcing) and 3 (screening) run **in parallel** — both depend only on Task 1 (JD).

**Inter-team communication flow:**
- writer complete → send target profile and EVP to sourcing; send competencies and criteria to screening
- sourcing complete → send market compensation levels to offer
- screening complete → send competencies requiring deeper evaluation to interview
- interview complete → send scorecard structure and hiring recommendation criteria to offer
- offer cross-verifies the entire pipeline; requests revisions on discrepancies (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Reflect offer coordinator's consistency verification results
3. Report the final summary to the user

## Mode by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------------|----------------|----------------|
| "Design the full hiring process" | **Full Pipeline** | All 5 agents |
| "Just write the JD" | **JD Mode** | writer only |
| "Create interview questions" | **Interview Mode** | writer + interview |
| "Build a sourcing strategy for this JD" (existing JD) | **Sourcing Mode** | sourcing only |
| "Create a screening framework" | **Screening Mode** | writer + screening |

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
| Insufficient job information | writer provides standard JD template + customization guide |
| No compensation information | sourcing researches market benchmarks and proposes a 3-tier range |
| Web search failure | Use general knowledge for JD / sourcing strategy; mark "[Market data not reflected]" |
| Agent failure | Retry once → if still failing, proceed without that deliverable |
| Consistency discrepancy | offer requests revision → rework (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "I need to hire 1 senior backend engineer. Salary range KRW 80M–100M, remote work available, want to hire within a month."
**Expected results**:
- JD: 5 senior backend competencies, compelling job posting, evaluation criteria
- Sourcing: LinkedIn Boolean queries, 3 outreach templates, channel-by-channel strategy
- Screening: Coding test + system design task, 5 phone screening questions
- Interview: Technical interview (live coding) + culture interview, 10+ STAR questions
- Offer: Compensation benchmarked against market, offer letter, negotiation guide

### Partial Request Flow
**Prompt**: "Create interview questions for this JD" + JD file
**Expected results**:
- Interview Mode (writer + interview)
- Extract competencies from existing JD and design structured interview questions
- writer supplements only the competency criteria draft

### Error Flow
**Prompt**: "I need to hire someone but I'm not sure what the role is"
**Expected results**:
- writer begins job analysis by asking about tasks and goals
- Proposes benchmarks for 3 similar roles
- Writes a draft JD with minimal information and asks user to confirm

## Per-Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|-----------------|------|-------------|------|
| competency-model | `.claude/skills/competency-model/skill.md` | jd-writer, screening-expert | Competency definitions, proficiency levels, screening matrix |
| interview-scorecard | `.claude/skills/interview-scorecard/skill.md` | interview-designer | Structured interview design, BEI question bank, bias prevention |
