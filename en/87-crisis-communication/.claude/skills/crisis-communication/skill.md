---
name: crisis-communication
description: "Full crisis communication pipeline. When a crisis occurs, an agent team collaborates to generate an integrated crisis package — covering situation assessment, message strategy, press release, Q&A, and monitoring — in a single run. Use this skill for any organizational crisis communication need, including: 'crisis response', 'crisis communication', 'press release writing', 'crisis management', 'emergency response', 'media response', 'press conference preparation', 'official statement', 'crisis communication strategy', 'apology drafting', 'product recall response', 'data breach response', 'incident response'. Provides a universal crisis response framework even when the crisis type is not yet specified. Does not cover actual legal counsel, insurance claims, civil or criminal litigation representation, or real-time social media monitoring API integration."
---

# Crisis Communication — Crisis Communication Full Pipeline

When a crisis occurs, an agent team collaborates to generate all deliverables in a single run, covering situation assessment → message strategy → press release → Q&A → monitoring.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| situation-analyst | `.claude/agents/situation-analyst.md` | Facts, stakeholders, crisis grade | general-purpose |
| message-strategist | `.claude/agents/message-strategist.md` | Core messages, tone, channel strategy | general-purpose |
| press-release-writer | `.claude/agents/press-release-writer.md` | Press release, official statements, internal notices | general-purpose |
| qa-preparer | `.claude/agents/qa-preparer.md` | Anticipated questions, answer guide, briefing sheet | general-purpose |
| media-monitor | `.claude/agents/media-monitor.md` | Sentiment tracking, secondary crisis detection, resolution criteria | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Crisis situation**: What happened
    - **Organization information**: Name, size, industry
    - **Current status**: Whether media has reported, when internally discovered, whether initial response has occurred
    - **Constraints** (optional): Legal issues, regulatory considerations, time constraints
    - **Existing documents** (optional): Prior press releases, internal reports
2. Create the `_workspace/` directory at the project root.
3. Organize the input and save to `_workspace/00_input.md`.
4. If existing documents are provided, copy them to `_workspace/` and adjust the relevant phases accordingly.
5. **Determine the execution mode** based on the scope of the request (see "Mode by Scope" below).

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|------------|
| 1 | Situation analysis | analyst | None | `_workspace/01_situation_analysis.md` |
| 2 | Message strategy | strategist | Task 1 | `_workspace/02_message_strategy.md` |
| 3a | Press release writing | writer | Tasks 1, 2 | `_workspace/03_press_release.md` |
| 3b | Q&A preparation | preparer | Tasks 1, 2 | `_workspace/04_qa_briefing.md` |
| 4 | Monitoring plan | monitor | Tasks 1, 2, 3a, 3b | `_workspace/05_monitoring_plan.md` |

Tasks 3a (press release) and 3b (Q&A) are executed **in parallel**. Both depend only on Task 2 (message strategy) and can begin simultaneously.

**Inter-agent communication flow:**
- analyst completes → delivers crisis grade, stakeholder analysis, and facts to strategist
- strategist completes → delivers core messages, tone, and No-Go Phrases to writer; delivers stakeholder-specific messages to preparer
- writer completes → delivers final copy to preparer (for Q&A consistency)
- preparer completes → delivers anticipated question patterns to monitor
- monitor cross-verifies all deliverables for message consistency, missing scenarios, and timing conflicts

### Phase 3: Integration and Final Deliverables

Finalize deliverables based on the monitor's verification results:

1. Verify all files in `_workspace/`.
2. If message consistency issues are found, request revisions from the relevant agent (maximum 2 iterations).
3. Report the final summary to the user:
    - Situation Analysis Report — `01_situation_analysis.md`
    - Message Strategy Document — `02_message_strategy.md`
    - Press Release / Official Statement — `03_press_release.md`
    - Q&A Briefing Sheet — `04_qa_briefing.md`
    - Monitoring Plan — `05_monitoring_plan.md`

## Mode by Scope

Adjust the agents deployed based on the scope of the user's request:

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Prepare full crisis response package" | **Full Pipeline** | All 5 agents |
| "Write the press release only" | **Press Release Mode** | analyst + strategist + writer |
| "Prepare Q&A for the press conference" | **Q&A Mode** | analyst + strategist + preparer |
| "Analyze the crisis situation only" | **Analysis Mode** | analyst only |
| "Review this press release" (existing file) | **Review Mode** | strategist + monitor |

**Using existing files**: If the user provides an existing press release or internal report, copy the file to the appropriate location in `_workspace/` and skip the corresponding phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|---------|
| Insufficient crisis information | analyst works from assumption-based scenarios; note "[Information Limited]" |
| Web search fails | Replace with general patterns for the relevant crisis type; note "Precedent unconfirmed" in report |
| Legal judgment required | Mark ⚖️ and compile legal review items separately; provide conservative version in parallel |
| Agent failure | Retry once → if still failing, proceed without that deliverable; note the omission in the final report |
| Message inconsistency found | Request revision from relevant agent → rework (maximum 2 iterations) |

## Test Scenarios

### Normal Flow
**Prompt**: "50,000 customer records were leaked from our app. It hasn't been reported yet, and we discovered it internally 30 minutes ago. Prepare the full crisis communication response."
**Expected Results**:
- Situation analysis: Data breach rated Critical, Personal Data Protection Act violation risk identified, 6+ stakeholder groups
- Message strategy: 3C core messages, Golden Hour response plan, 5+ No-Go Phrases
- Press release: Holding statement + full press release + CEO letter
- Q&A: 20+ anticipated questions by category, trap question responses
- Monitoring: Channel-specific keywords, alert thresholds, crisis resolution criteria

### Partial Request Flow
**Prompt**: "We have a press conference tomorrow and urgently need Q&A only. The situation is a product recall."
**Expected Results**:
- Switch to Q&A Mode (analyst + strategist + preparer)
- Recall-specific questions (safety, compensation, recall scope, cause, preventive measures)
- Spokesperson one-page card + bridge phrases

### Error Flow
**Prompt**: "Prepare a crisis response — I'm not sure of the details, but there's an uproar on social media."
**Expected Results**:
- analyst notes "[Information Limited]" and presents 3 social media crisis type assumption scenarios
- Prepares core message variations for each scenario
- Provides a general-purpose holding statement immediately

## Agent Extension Skills

| Extension Skill | Path | Target Agents | Role |
|----------------|------|--------------|------|
| stakeholder-mapping | `.claude/skills/stakeholder-mapping/skill.md` | situation-analyst, message-strategist | Stakeholder mapping, crisis grading, timeline |
| media-response-templates | `.claude/skills/media-response-templates/skill.md` | press-release-writer, qa-preparer | Press release templates, Q&A ABT structure, prohibited expressions |
