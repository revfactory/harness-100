---
name: decision-trigger-mapper
description: "A specialised skill for designing decision trigger maps and strategy option portfolios within scenario response strategies. Used by the strategy-architect agent when converting robust/hedge/option strategies into concrete execution plans. Automatically applied in contexts such as 'decision triggers', 'strategy options', 'execution roadmap', 'trigger map', 'hedge strategy'. However, actual project management tool (Jira, Asana) integration and budget execution approval are outside the scope of this skill."
---

# Decision Trigger Mapper — Decision Trigger Map Design Tool

A specialised skill that enhances the strategy execution design capabilities of the strategy-architect agent.

## Target Agent

- **strategy-architect** — Response strategy development, decision trigger design

## Strategy Type Classification System

### 3-Tier Strategy Portfolio

| Type | Definition | Execution Condition | Investment Level |
|------|-----------|--------------------|----|
| **Robust Strategy** | Valid across all scenarios | Execute immediately | Full investment |
| **Hedge Strategy** | Valid across most scenarios | Start early, adjust direction | Medium investment |
| **Option Strategy** | Valid only in specific scenarios | Execute when trigger fires | Minimum investment (secure option) |

### Strategy Type Decision Tree

```
Is this strategy valuable across all 4 scenarios?
+-- YES → Robust Strategy (Core)
|         → Execute immediately, concentrate resources
+-- NO
    +-- Valuable in 2-3 scenarios?
    |   +-- YES → Hedge Strategy (Hedge)
    |   |         → Initial investment, design for pivot
    |   +-- NO → Valuable in only 1?
    |       +-- YES & high impact → Option Strategy (Option)
    |       |                     → Minimum investment, await trigger
    |       +-- YES & low impact → Defer
    +-- Uncertain in any scenario → Requires re-analysis
```

## Decision Trigger Map Design

### Trigger Card Template

```markdown
### Trigger #N: [Trigger Name]

**Related Strategy**: [Which option strategy does it activate]
**Related Scenario**: [Which scenario transition triggers it]

| Item | Content |
|------|---------|
| Observable Metric | [What to monitor] |
| Data Source | [Where to collect data] |
| Threshold | [At what level does it fire] |
| Confirmation Period | [How long must it persist to confirm trigger] |
| Response Action | [Specifically what to do] |
| Decision Owner | [Who makes the decision] |
| Required Resources | [Budget/people/time needed] |
| Withdrawal Condition | [When to deactivate the trigger] |
```

### Trigger Types

| Type | Description | Example |
|------|-----------|---------|
| Redline Trigger | Immediate action if crossed | Market share < 15% |
| Cumulative Trigger | Act when multiple signals accumulate | 3+ warning signals fire simultaneously |
| Time Trigger | Evaluate at specific points | Quarterly strategy review |
| Event Trigger | Act upon specific event occurrence | Competitor M&A announcement |

## Real Options Thinking Framework

Design strategic options using financial option analogies:

| Financial Option | Strategic Option Equivalent | Example |
|-----------------|---------------------------|---------|
| Call Option (right to buy) | Growth Option | New market entry preparation (small-scale test) |
| Put Option (right to sell) | Shrink/Exit Option | Business unit divestiture conditions defined |
| Straddle | Both-direction Option | Prepare for both scenario outcomes |
| Premium | Option maintenance cost | Pilot project costs |
| Strike Price | Trigger threshold | Market size attainment benchmark |
| Expiration | Decision deadline | Strategy review timing |

### Option Value Assessment Criteria

| Criterion | Question | High = Higher Option Value |
|-----------|---------|---------------------------|
| Uncertainty | Is uncertainty high in this area? | More uncertain → higher option value |
| Irreversibility | Is it irreversible once executed? | More irreversible → higher option value |
| Learning Potential | Will more information become available over time? | More learnable → higher option value |
| Option Cost | Is the option maintenance cost manageable? | Lower cost → easier to execute |

## Execution Roadmap Integration

### Action Classification by Time Horizon

| Time Horizon | Action Type | Budget Share |
|-------------|------------|-------------|
| Immediate (0-3 months) | Launch robust strategies + build monitoring system | 50% |
| Short-term (3-12 months) | Initial hedge strategy execution + secure options | 30% |
| Medium-term (1-3 years) | Trigger-based option exercise/abandonment | 15% |
| Long-term (3-5 years) | Strategy portfolio reassessment | 5% |

### Strategy Review Cadence

```
Quarterly Review: Monitor triggers → evaluate signals → decide option exercise
Semi-Annual Review: Revalidate scenario validity → add new variables → update matrix
Annual Review: Full scenario refresh → rebuild strategy portfolio
```
