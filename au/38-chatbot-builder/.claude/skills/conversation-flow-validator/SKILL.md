---
name: conversation-flow-validator
description: "Methodology for validating chatbot conversation flow completeness, cycles, and dead ends. Use this skill for 'conversation flow validation', 'scenario testing', 'edge case checking', 'fallback verification', 'multi-turn testing', and other dialog quality verification tasks. Note: conducting actual user testing and building A/B testing infrastructure are outside the scope of this skill."
---

# Conversation Flow Validator — Dialog Flow Validation Methodology

A skill that enhances dialog quality verification for the dialog-tester and conversation-designer.

## Target Agents

- **dialog-tester** — Systematically validates conversation scenarios
- **conversation-designer** — Proactively discovers flow defects during the design phase

## Conversation Flow Graph Analysis

### Node Types

```
[START] → Entry point
[BOT] → Bot utterance node
[USER] → User input expectation node
[ACTION] → Backend API call
[CONDITION] → Branching condition
[END] → Exit point
[FALLBACK] → Unrecognized input handling
[HANDOFF] → Human agent handoff
```

### Defect Type Detection

| Defect | Description | Severity | Detection Method |
|--------|------------|----------|-----------------|
| Dead end | Conversation reaches a dead end | P0 | Search for terminal nodes without END |
| Infinite loop | Infinite cycling through the same nodes | P0 | Cycle detection (DFS) |
| Unreachable | Cannot be reached via any path | P1 | BFS from START for unreached nodes |
| Fallback black hole | No recovery path from fallback | P0 | Verify valid transitions after fallback |
| Slot leakage | Proceeds without collecting required slots | P0 | Track slot fulfillment conditions |
| Context loss | Prior information not retained in multi-turn | P1 | Track session variables |

## Test Scenario Generation Framework

### Happy Path (Normal Flow)

```
Purpose: Validate the most common usage flow

Structure:
1. Greeting > Express intent > Provide slots > Confirm > Complete

Example (Cafe order):
USER: "Hello"
BOT: "Hello! How can I help you?"
USER: "I'd like to order two Americanos"
BOT: "Two Americanos, correct? Please choose a size."
USER: "Tall"
BOT: "Two tall Americanos, total $9.00. Would you like to place the order?"
USER: "Yes"
BOT: "Your order has been placed! Thank you."
```

### Sad Path (Failure Flow)

```
Purpose: Validate recovery capabilities in error situations

Scenario types:
1. Ordering unavailable item > Suggest similar items
2. Out of stock > Suggest alternatives or direct to another location
3. API failure > Retry or connect to agent
4. Payment failure > Suggest alternative payment methods
```

### Edge Case (Boundary Cases)

```
1. Intent switch: Suddenly asking "What are your hours?" mid-order
   > Preserve current context, respond, then guide back

2. Multiple intents: "Place an order and send me the receipt too"
   > Sequential processing or compound handling

3. Ambiguous expression: "One more of that"
   > Reference previous context or ask clarifying question

4. Negative confirmation: Repeated questions after "No"
   > Offer alternatives after maximum 2 attempts

5. Empty input / special characters only / emojis only
   > Safe fallback response
```

## Multi-Turn Verification Checklist

```
[ ] Is context maintained in conversations of 3+ turns?
[ ] Can the user modify previously provided information?
[ ] Is there an alternative path after a "No" response?
[ ] Can the original flow be resumed after an intent switch?
[ ] Is there appropriate guidance after session timeout?
[ ] Is escalation triggered after 3 repetitions of the same question?
[ ] When modifying a slot, are other already-collected slots preserved?
```

## Fallback Strategy Hierarchy

```
Level 1: Re-input request
  "I'm sorry, I didn't understand that. Could you please say it again?"
  > Allowed once

Level 2: Suggest options
  "Which of the following would you like? 1. Order 2. View menu 3. Other"
  > On 2nd unrecognized input

Level 3: Human agent handoff
  "Let me connect you with an agent for more accurate assistance."
  > On 3rd unrecognized input or user request
```

## Quality Metrics

| Metric | Formula | Threshold |
|--------|---------|-----------|
| Intent recognition rate | Correct recognitions / total utterances | >= 85% |
| Task completion rate | Successful completions / started tasks | >= 70% |
| Fallback rate | Fallback count / total turns | <= 15% |
| Average turn count | Total turns / completed sessions | Task-specific baseline +/- 2 |
| Escalation rate | Agent handoffs / total sessions | <= 20% |

## Validation Report Template

```markdown
## Conversation Flow Validation Report

### Test Summary
- Happy Path: N/M passed
- Sad Path: N/M passed
- Edge Case: N/M passed

### Defects Found
| # | Type | Scenario | Severity | Remediation |

### Fallback Analysis
- Fallback rate: N%
- Key unrecognized utterances: [list]

### Metrics
| Metric | Result | Threshold | Verdict |
```
