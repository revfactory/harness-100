---
name: public-speaking
description: "Full public speaking preparation pipeline where an agent team collaborates to produce speech scripts, presentation outlines, debate preparation, Q&A playbooks, and rehearsal guides. Use for "write a speech", "presentation prep", "debate preparation", "Q&A preparation", etc. Note: PowerPoint/Keynote file creation, live coaching, and real-time presentation are outside the scope of this skill."
---

# Public Speaking — comprehensive pipeline

 audienceanalysis→speechdocument→debatepreparation→Q&A→rehearsalguide An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| audience-analyst | `.claude/agents/audience-analyst.md` | audience file, emotion , message | general-purpose |
| speech-writer | `.claude/agents/speech-writer.md` | speechdocument/presentation versus, numbercompany, stage degreewhen | general-purpose |
| debate-preparer | `.claude/agents/debate-preparer.md` | , counterargument , gapdocument | general-purpose |
| qa-strategist | `.claude/agents/qa-strategist.md` | expected question, answer strategy, Q&A operations | general-purpose |
| rehearsal-coach | `.claude/agents/rehearsal-coach.md` | rehearsal plan, delivercapability, cross-verification | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **presentation type**: basisspeech/presentation/value/debate/interviewpresentation
 - **week**: presentation week and core message
 - **audience**: target audience nature
 - **time**: to do time
 - **context**: eventpeople, situation, by requirements
 - **existing material** (optional): before presentation material, , KRW
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | audience analysis | analyst | None | `_workspace/01_audience_analysis.md` |
| 2 | speechdocument writing | writer | task 1 | `_workspace/02_speech_script.md` |
| 3a | debate preparation | preparer | task 1, 2 | `_workspace/03_debate_prep.md` |
| 3b | Q&A strategy | strategist | task 1, 2 | `_workspace/04_qa_playbook.md` |
| 4 | rehearsal guide and verify | coach | task 3a, 3b | `_workspace/05_rehearsal_guide.md` |

task 3a(debate) and 3b(Q&A) ** execution**. task 1, 2 dependency.

**teamKRW between flow:**
- analyst complete → writerto audience file+emotion + deliver, preparerto audience also deliver, strategistto question direction deliver
- writer complete → preparerto core point+approx. point deliver, strategistto question point deliver
- preparer complete → strategistto counterargument list 
- coach all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - audience analysis — `01_audience_analysis.md`
 - speechdocument/presentation versus — `02_speech_script.md`
 - debate preparationfrom — `03_debate_prep.md`
 - Q&A — `04_qa_playbook.md`
 - rehearsal guide — `05_rehearsal_guide.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "presentation preparationplease do", "value overall preparation" | **Full pipeline** | 5people beforeKRW |
| "speechdocument only " | **speech mode** | analyst + writer + coach |
| " presentation material Q&A preparationplease do" (material provide) | **Q&A mode** | strategist + coach |
| "debate preparationplease do" | **debate mode** | analyst + preparer + coach |
| "rehearsal guide" (versus provide) | **rehearsal mode** | coach |

**existing file utilization**: user presentation material, versus etc. provide applicable stage case.

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| audience information None | event typefrom general audience file , "estimation based" specify |
| presentation type people | presentation basicas applied |
| web search failure | user provide information and day degree based task |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| debate needed | debate preparation , Q&A during |

## test scenario

### flow
**Prompt**: "next week technical from 'AI whenversus development' week 30minute basisspeech . audience developmentspecialist 500people."
**expected result**:
- audience analysis: developmentspecialist segment(week/when/), expected, , emotion 
- speechdocument: 30minute basisspeech versus + stage degreewhen + numbercompany technique
- debate preparation: AI versus etc. expected counterargument + 
- Q&A: 15items or more expected question + answer 
- rehearsal: D-7department schedule + delivercapability guide + consistency matrix confirm

### existing material utilization flow
**Prompt**: " presentation versusas Q&A preparation rehearsal guide create it" + versus file provide
**expected result**:
- audience analysis, speechdocument writing case
- versus `_workspace/02_speech_script.md` company
- strategist + coach deploy

### error flow
**Prompt**: "presentation preparationplease do, week un-"
**expected result**:
- week people userto presentation week/context confirm question
- answer basedas task progress
- verify report "week after final review needed" specify

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| rhetoric-patterns | `.claude/skills/rhetoric-patterns/skill.md` | speech-writer, debate-preparer | numbercompany pattern, structure, persuasion technique |
| audience-engagement | `.claude/skills/audience-engagement/skill.md` | audience-analyst, rehearsal-coach | audience analysis, strategy, management, communication |
