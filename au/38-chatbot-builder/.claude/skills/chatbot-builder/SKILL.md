---
name: chatbot-builder
description: "Full pipeline where an agent team collaborates to build a chatbot system. Use this skill for requests like 'build me a chatbot', 'conversational bot development', 'customer service bot', 'FAQ chatbot', 'KakaoTalk chatbot', 'Slack bot', 'auto-response system', 'conversational AI', 'chatbot design', and other chatbot construction tasks. Also supports design-only mode when only conversation design is needed. Note: voice assistants (Alexa/Google Home), real-time voice call bots, and video chatbots are outside the scope of this skill."
---

# Chatbot Builder — Chatbot Construction Pipeline

An agent team collaborates to build a chatbot through persona design > conversation design > NLU > integration > testing.

## Execution Mode

**Agent Team** — Five agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| persona-architect | `.claude/agents/persona-architect.md` | Bot persona design | general-purpose |
| conversation-designer | `.claude/agents/conversation-designer.md` | Conversation scenario design | general-purpose |
| nlu-developer | `.claude/agents/nlu-developer.md` | NLU pipeline implementation | general-purpose |
| integration-engineer | `.claude/agents/integration-engineer.md` | Channel integration, deployment | general-purpose |
| dialog-tester | `.claude/agents/dialog-tester.md` | Quality verification, testing | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Chatbot purpose**: Customer service/FAQ/reservations/orders/consultation, etc.
    - **Target users**: Age, digital literacy, expectation level
    - **Integration channels**: Slack/KakaoTalk/Telegram/Web/multi-channel
    - **Domain knowledge**: Business rules, FAQ list, product information, etc.
    - **Constraints** (optional): Technology stack, response time requirements
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request (see "Execution Modes by Request Scope" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Persona design | persona | None | `_workspace/01_persona_spec.md` |
| 2 | Conversation design | designer | Task 1 | `_workspace/02_conversation_design.md` |
| 3a | NLU implementation | nlu-dev | Task 2 | `_workspace/03_nlu_config.md` + `src/` |
| 3b | Integration design | integrator | Task 2 | `_workspace/04_integration_spec.md` + `src/` |
| 4 | Testing | tester | Tasks 3a, 3b | `_workspace/05_test_report.md` |

Tasks 3a (NLU) and 3b (integration) run **in parallel**.

**Inter-agent communication flow:**
- persona completes > passes tone and manner guide to designer, passes domain keywords to nlu-dev
- designer completes > passes intent/entity catalog to nlu-dev, passes external integration flows to integrator
- nlu-dev completes > passes NLU interface to integrator, passes test data to tester
- integrator completes > passes test environment info to tester
- tester cross-validates all deliverables. On CRITICAL findings, requests corrections from the relevant agent > rework > re-verification (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Finalise deliverables based on the tester's report:

1. Verify all files in `_workspace/` and `src/` code
2. Confirm that all CRITICAL findings have been resolved
3. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build me a chatbot", "full build" | **Full pipeline** | All 5 agents |
| "Just do the conversation design", "write scenarios" | **Design mode** | persona + designer |
| "Just develop the NLU" (design complete) | **NLU mode** | nlu-dev + tester |
| "Integrate chatbot with KakaoTalk" (implementation complete) | **Integration mode** | integrator + tester |
| "Test the chatbot" (implementation complete) | **Test mode** | tester only |

**Reusing existing files**: If the user provides an existing conversation design document or NLU configuration, copy those files to `_workspace/` and skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents and configuration sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Code-based | `_workspace/src/` | Executable source code |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient domain knowledge | Request additional FAQ list/business information from user, supplement with web search |
| Channel API changes | Verify latest API documentation via WebFetch, then update integration code |
| NLU accuracy below threshold | Augment training data > redesign prompts > strengthen fallback, in that order |
| Agent failure | Retry once > if still failing, proceed without that deliverable and note in report |

## Test Scenarios

### Normal Flow
**Prompt**: "Build a KakaoTalk chatbot for cafe order processing. It should support menu browsing, ordering, and payment guidance"
**Expected result**:
- Persona: Bright, friendly cafe staff character, formal tone, active emoji usage
- Conversation design: Menu browsing/ordering/payment guidance/business hours intents, slots (menu name/quantity/options)
- NLU: LLM prompt-based intent classification, menu name entity dictionary construction
- Integration: KakaoTalk chatbot API integration, card-type messages for menu display
- Testing: Order flow happy path, fallback for unavailable menu items, multi-turn ordering

### Existing File Reuse Flow
**Prompt**: "I have this conversation design document; implement the NLU and integrate it with KakaoTalk" + design document attached
**Expected result**:
- Copy existing design document to `_workspace/02_conversation_design.md`
- Skip persona and designer; deploy nlu-dev + integrator + tester
- Implement NLU based on existing intent/entity catalog

### Error Flow
**Prompt**: "Build me a chatbot" (purpose, channel unclear)
**Expected result**:
- persona proposes a generic persona and requests purpose confirmation from user
- Proceed with remaining pipeline after purpose is confirmed
- Note in report: "Channel undetermined — web widget applied as default"

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| intent-taxonomy-builder | `.claude/skills/intent-taxonomy-builder/skill.md` | nlu-developer, conversation-designer | Intent taxonomy design, entity-slot mapping, training data generation, confusion matrix |
| conversation-flow-validator | `.claude/skills/conversation-flow-validator/skill.md` | dialog-tester, conversation-designer | Dialog flow defect detection, Happy/Sad/Edge testing, fallback hierarchy, quality metrics |
