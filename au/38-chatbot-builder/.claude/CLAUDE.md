# Chatbot Builder Harness

Chatbot construction: a harness where an agent team collaborates to perform intent analysis, conversation design, NLU development, integration, and testing.

## Structure

```
.claude/
├── agents/
│   ├── conversation-designer.md — Conversation design (scenarios, flows, fallback strategies)
│   ├── nlu-developer.md         — NLU development (intent classification, entity extraction, context management)
│   ├── integration-engineer.md  — Integration engineer (channel integration, API, backend)
│   ├── dialog-tester.md         — Dialog tester (scenario testing, edge cases, quality verification)
│   └── persona-architect.md     — Persona design (bot personality, tone, brand alignment)
├── skills/
│   ├── chatbot-builder/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── intent-taxonomy-builder/
│   │   └── skill.md             — Intent taxonomy (entities, slots, training data)
│   └── conversation-flow-validator/
│       └── skill.md             — Conversation flow validation (defect detection, testing, metrics)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/chatbot-builder` skill or make a natural language request such as "Build me a chatbot."

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input summary
- `01_persona_spec.md` — Bot persona specification
- `02_conversation_design.md` — Conversation design document
- `03_nlu_config.md` — NLU configuration and training data
- `04_integration_spec.md` — Integration specification
- `05_test_report.md` — Test report
- `src/` — Chatbot source code

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 5 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
