---
name: crisis-communication
description: "crisis situation occurrence when situationidentify, messagestrategy, press release, Q&A, monitoringto agent team to integration crisis package Korean creation Full pipeline. 'crisis response', 'crisis communication', 'press release writing', 'crisismanagement', 'crisis management', 'grade response', ' response', 'basisspecialist preparation', 'official document', 'crisis strategy', 'companydocument writing', ' response', 'data response', 'companycase company response' etc. crisis situation communication before skill usage. crisis type degree also crisis response framework provide. However, actual rate specialistdocument, insurance , company/company versus, actualtime SNS monitoring API annual is outside this skill's scope."
---

# Crisis Communication — crisis Full pipeline

crisis situation situationidentify→messagestrategy→press release→Q&A→monitoring An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| situation-analyst | `.claude/agents/situation-analyst.md` | companyactualtotal, stakeholder, crisisetc.grade | general-purpose |
| message-strategist | `.claude/agents/message-strategist.md` | coremessage, tone, channelstrategy | general-purpose |
| press-release-writer | `.claude/agents/press-release-writer.md` | press release, officialdocument, withindepartmentdegree | general-purpose |
| qa-preparer | `.claude/agents/qa-preparer.md` | expectedquestion, answerguide, when | general-purpose |
| media-monitor | `.claude/agents/media-monitor.md` | tracking, 2gapcrisisdegree, judgment | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **crisis situation**: day occurrence
 - ** information**: people, scale, 
 - **current status**: press coverage department, withindepartment persondegree timing, initial response department
 - **constraint condition** (optional): legal issue, matters, time constraint
 - **existing document** (optional): existing press release, withindepartment report etc.
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. existing document `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request ( "task scaleby mode" reference)

### Phase 2: team composition and execution

team compositionand task to do. task between dependency total next and :

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | situation analysis | analyst | None | `_workspace/01_situation_analysis.md` |
| 2 | message strategy | strategist | task 1 | `_workspace/02_message_strategy.md` |
| 3a | press release writing | writer | task 1, 2 | `_workspace/03_press_release.md` |
| 3b | Q&A preparation | preparer | task 1, 2 | `_workspace/04_qa_briefing.md` |
| 4 | monitoring plan | monitor | task 1, 2, 3a, 3b | `_workspace/05_monitoring_plan.md` |

task 3a(press release) and 3b(Q&A) ** execution**. task 2(messagestrategy) only dependency when whenworkto do number .

**teamKRW between flow:**
- analyst complete → strategistto crisisetc.grade·stakeholder· deliver
- strategist complete → writerto coremessage·tone·No-Go Phrases deliver, preparerto stakeholderby message deliver
- writer complete → preparerto official documentplan deliver (Q&A consistency secure)
- preparer complete → monitorto expected question pattern deliver
- monitor all deliverable cross-verificationto message consistency, scenario, inspection

### Phase 3: integration and final deliverable

 verify result basedas final deliverable organisation:

1. `_workspace/` Verify all files in the directory
2. message consistency issue findings applicable agent revision request (versus 2)
3. Report the final summary to the user:
 - situation analysis report — `01_situation_analysis.md`
 - message strategyfrom — `02_message_strategy.md`
 - press release/document — `03_press_release.md`
 - Q&A when — `04_qa_briefing.md`
 - monitoring plan — `05_monitoring_plan.md`

## task scaleby mode

user request scope according to deploy agent :

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "crisis response overall preparationplease do", "Full package" | **Full pipeline** | 5people beforeKRW |
| "press release only " | **press release mode** | analyst + strategist + writer |
| "basisspecialist Q&A preparationplease do" | **Q&A mode** | analyst + strategist + preparer |
| "crisis situation analysis only please do" | **analysis mode** | analyst |
| " press release reviewplease do" (existing file) | **review mode** | strategist + monitor |

**existing file utilisation**: user existing press release, withindepartment report etc. provide, applicable file `_workspace/` qualityKorean position companyand applicable stage case.

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
| crisis information insufficient | analyst scenario basedas task, "[information limitation]" specify |
| web search failure | company crisis type day patternas versus, report " un-confirm" specify |
| legal judgment needed | ⚖️ tablebasis after ratereview needed matters by also organisation, reportnumberquality version |
| agent failure | Retry once -> proceed without that deliverable, final reporting specify |
| message day findings | applicable agent revision request → re-task (versus 2) |

## test scenario

### flow
**Prompt**: " company from client itemspersoninformation 5 only case . press coverage before withindepartmentfrom 30minute before findings. crisis response communication overall preparationplease do."
**expected result**:
- situation analysis: data crisisetc.grade Critical , itemspersoninformationreport risk, stakeholder 6items or more
- message strategy: 3C core message, response, No-Go Phrases 5items or more
- press release: + press release + CEO fromKorean
- Q&A: categoryby expected question 20items or more, question response
- monitoring: channelby , standard, crisis judgment standard

### departmentminute request flow
**Prompt**: "withinday basisspecialistperson Q&A only grade preparationplease do. situation ."
**expected result**:
- Q&A mode beforeexchange (analyst + strategist + preparer)
- question (planbeforenature, report, scope, cause, re-degree)
- versusperson 1-degree + degree document

### error flow
**Prompt**: "crisis response preparationplease do, situation SNSfrom "
**expected result**:
- analyst "[information limitation]" specify after SNS crisis type scenario 3items present
- each scenarioby core message preparation
- i.e.when provide

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| stakeholder-mapping | `.claude/skills/stakeholder-mapping/skill.md` | situation-analyst, message-strategist | stakeholder mapping, crisis etc.grade, timeline |
| media-response-templates | `.claude/skills/media-response-templates/skill.md` | press-release-writer, qa-preparer | press release template, Q&A ABT structure, prohibited tablecurrent |
