---
name: hiring-pipeline
description: "hiring process JDwriting, sourcing, screening, interview design, assessment, offerto agent team to Korean creation Full pipeline. 'hiring', 'talent hiring', 'JD writing', 'job description', 'hiringposting', 'interview question', 'interview design', 'hiring process', 'sourcing strategy', 'screening', 'offer', 'hiring pipeline', 'hiring', 'talent secure' etc. hiring before skill usage. However, actual hiring platform(ATS) annual, grade whensystem etc.record, hiring totalapprox.from legal capability report, reference execution is outside this skill's scope."
---

# Hiring Pipeline — hiring process Full pipeline

hiring JDwriting→sourcing→screening→interview→assessment→offer An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| jd-writer | `.claude/agents/jd-writer.md` | job description, hiringposting | general-purpose |
| sourcing-specialist | `.claude/agents/sourcing-specialist.md` | channelstrategy, value | general-purpose |
| screening-expert | `.claude/agents/screening-expert.md` | fromassessment, task, screening | general-purpose |
| interview-designer | `.claude/agents/interview-designer.md` | structureinterview, question, evaluation form | general-purpose |
| offer-coordinator | `.claude/agents/offer-coordinator.md` | finalassessment, report, offer | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **degree**: hiringto do job, grade
 - ** information**: companypeople, team composition, document
 - **hiring condition**: , , grade scope
 - **grade**: hiring deadline, hiring personKRW
 - **existing material** (optional): existing JD, applicant current status
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. existing material `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | JD writing | writer | None | `_workspace/01_job_description.md` |
| 2 | sourcing strategy | sourcing | task 1 | `_workspace/02_sourcing_strategy.md` |
| 3 | screening design | screening | task 1 | `_workspace/03_screening_framework.md` |
| 4 | interview design | interview | task 1, 3 | `_workspace/04_interview_design.md` |
| 5 | assessment·offer | offer | task 1, 2, 3, 4 | `_workspace/05_evaluation_offer.md` |

task 2(sourcing) and 3(screening) ** execution**. task 1(JD) only dependency.

**teamKRW between flow:**
- writer complete → sourcingto target ·EVP, screeningto competency·assessmentstandard deliver
- sourcing complete → offerto market report level deliver
- screening complete → interviewto confirm needed competency deliver
- interview complete → offerto evaluation form structure·hiring recommendation standard deliver
- offer overall pipeline cross-verification, dayvalue findings when revision request (versus 2)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. offer consistency verify result reflected
3. Report the final summary to the user

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "hiring process overall designplease do" | **Full pipeline** | 5people beforeKRW |
| "JD only " | **JD mode** | writer |
| "interview question create it" | **interview mode** | writer + interview |
| " JD sourcing strategy " (existing JD) | **sourcing mode** | sourcing |
| "hiring screening standard create it" | **screening mode** | writer + screening |

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
| job information insufficient | writer tablelevel JD template + guide provide |
| grade information None | sourcing market value research, 3stage scope proposal |
| web search failure | day degree based JD/sourcing strategy, "[market data un-reflected]" specify |
| agent failure | Retry once -> proceed without that deliverable |
| consistency dayvalue | offer revision request → re-task (versus 2) |

## test scenario

### flow
**Prompt**: "when developmentspecialist 1people hiring . salary 8~100M, KRW possible, Korean plan hiringand ."
**expected result**:
- JD: when competency 5items, capabilityqualityperson hiringposting, assessment standard
- sourcing: LinkedIn Boolean , value template 3, channelby strategy
- screening: test + whensystem design task, before screening 5document
- interview: technical interview + document interview, STAR question 10items+
- offer: market value versus report, offer, negotiation guide

### departmentminute request flow
**Prompt**: " JD interview question only create it" + JD file
**expected result**:
- interview mode (writer + interview)
- existing JD based competency after structure interview question design
- writer competency standard plan only report

### error flow
**Prompt**: "hiring jobpersondegree "
**expected result**:
- writer work content/goal questionas job analysis whenwork
- company job 3items value proposal
- minimumKorean information plan JD writing after user confirm request

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| competency-model | `.claude/skills/competency-model/skill.md` | jd-writer, screening-expert | competency definition, level total, screening matrix |
| interview-scorecard | `.claude/skills/interview-scorecard/skill.md` | interview-designer | structure interview, BEI question , degree |
