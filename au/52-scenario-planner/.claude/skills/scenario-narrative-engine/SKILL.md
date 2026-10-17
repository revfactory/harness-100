---
name: scenario-narrative-engine
description: "A specialised skill for vividly constructing each scenario's narrative and designing timelines and early warning signals during scenario design. Used by the scenario-designer agent when narrativizing 2x2 matrix-based scenarios. Automatically applied in contexts such as 'scenario narrative', 'scenario story', 'timeline', 'early warning signals', 'early warning'. However, fictional novel writing or movie screenplay creation are outside the scope of this skill."
---

# Scenario Narrative Engine — Scenario Narrative Construction Tool

A specialised skill that enhances the scenario narrative construction capabilities of the scenario-designer agent.

## Target Agent

- **scenario-designer** — 2x2 matrix scenario narrativization, timeline design

## 2x2 Scenario Matrix Construction Method

### Basic Structure

```
                    Axis A: [Variable] High
                         |
   Scenario 2            |           Scenario 1
   [Scenario Name]       |           [Scenario Name]
   "Narrative subtitle"  |           "Narrative subtitle"
                         |
Axis B: Low ─────────────┼──────────────── Axis B: High
                         |
   Scenario 3            |           Scenario 4
   [Scenario Name]       |           [Scenario Name]
   "Narrative subtitle"  |           "Narrative subtitle"
                         |
                    Axis A: [Variable] Low
```

### Scenario Naming Rules

| Principle | Good Example | Bad Example |
|-----------|-------------|-------------|
| Use intuitive metaphor | "Silicon Spring" | "Scenario A" |
| Evoke emotion/imagery | "Digital Ice Age" | "Tech Slowdown" |
| 2-4 words | "Quiet Revolution" | "Technology Regulation Strengthening and Market Contraction Scenario" |
| Value-neutral | "Fork in the Road" | "Worst Case" |

## Scenario Narrative Writing Template

Each scenario is described with the following structure:

### 1. Core Premise (1 paragraph)
- Why this combination of extreme values on both axes emerged
- Root Cause

### 2. Development Timeline (yearly key events)

```markdown
### Timeline

| Timepoint | Event | Signal | Impact |
|-----------|-------|--------|--------|
| Y+1 | [Trigger event] | [Observable indicator] | [Primary impact] |
| Y+2 | [Chain reaction] | [Strengthening/weakening signal] | [Industry change] |
| Y+3 | [Structural transformation] | [New normal signal] | [Paradigm shift] |
| Y+5 | [Stabilization/new equilibrium] | [Settlement indicators] | [Long-term structure] |
```

### 3. Key Characteristics (5 items)
- Market structure
- Technology environment
- Regulatory framework
- Competitive dynamics
- Consumer/user behaviour

### 4. Winners and Losers
- Player types that thrive in this scenario
- Player types that decline in this scenario

### 5. Early Warning Signals (3-5 items)
- Observable indicators that signal entry into this scenario

## Early Warning Signal Design Framework

### Signal Type Classification

| Type | Definition | Example | Monitoring Frequency |
|------|-----------|---------|---------------------|
| Leading indicator | Appears before change | Patent filing surge | Quarterly |
| Concurrent indicator | Appears with change | Market share shift | Monthly |
| Weak signal | Subtle but meaningful change | Startup investment direction shift | Quarterly |
| Wild card | Unexpected shock | Regulatory reversal, tech breakthrough | Continuous |

### Signal Design Principles

1. **Observable**: Must be trackable with publicly available data
2. **Measurable**: Define quantitative thresholds
3. **Sufficient Lead Time**: Leading indicators that allow response time
4. **Uniqueness**: Exclusive signals specific to a particular scenario

### Signal Card Template

```markdown
#### Early Warning Signal #N

- **Signal Name**: [Clear name]
- **Related Scenario**: [Which scenario]
- **Data Source**: [Where to observe]
- **Threshold**: [At what level to trigger alert]
- **Monitoring Frequency**: [How often to check]
- **Response Action**: [What to do when this signal occurs]
```

## Cross-Scenario Analysis

### Common Element Matrix

| Element | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 | Common? |
|---------|-----------|-----------|-----------|-----------|---------|
| Element A | O | O | O | O | Predetermined trend |
| Element B | O | X | O | X | Axis A dependent |
| Element C | O | O | X | X | Axis B dependent |

### Robust Strategy Identification

Actions valid across all 4 scenarios = **Robust strategy** (execute unconditionally)
Actions valid in 2-3 scenarios = **Hedge strategy** (conditional execution)
Actions valid in only 1 scenario = **Option** (execute after signal confirmation)
