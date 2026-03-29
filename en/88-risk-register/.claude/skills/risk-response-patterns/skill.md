---
name: risk-response-patterns
description: "Risk response strategy pattern library. Referenced by the response-strategist and monitoring-planner agents when developing risk response plans. Use for requests involving 'risk response', 'mitigation strategy', or 'response plan'. Does not cover insurance product design or legal risk advisory."
---

# Risk Response Patterns — Risk Response Strategy Patterns

Enhances the response plan development capabilities of the response-strategist and monitoring-planner agents.

## Four Core Response Strategies (Threats)

| Strategy | Description | When to Use | Cost |
|----------|-------------|-------------|------|
| **Avoid** | Eliminate the risk cause | Score ≥ 16, elimination feasible | High |
| **Transfer** | Shift responsibility to a third party | Financial impact, insufficient expertise | Medium |
| **Mitigate** | Reduce probability or impact | Most risks | Medium |
| **Accept** | Tolerate the risk | Score ≤ 4, or cost > benefit | Low |

### Detailed Patterns by Strategy

#### Avoid

```
Patterns:
- Scope reduction: Exclude high-risk features
- Technology substitution: Replace with a proven technology
- Schedule extension: Allocate sufficient time
- Vendor change: Switch to a more reliable supplier

Example:
  Risk: "Stability of new Technology A is unverified"
  Avoid: "Replace with proven Technology B; accept feature limitations"
  Cost: +₩30M in development cost, 20% feature reduction
```

#### Transfer

```
Patterns:
- Insurance: Cover disaster or accident risks
- Outsourcing: Delegate areas requiring specialist expertise
- Contractual: Include penalty / incentive clauses
- Warranty: Require vendor performance guarantees

Example:
  Risk: "Penalty exposure due to delivery delay"
  Transfer: "Link subcontractor contract to delivery-date penalty clause"
  Cost: 5% increase in contract unit price
```

#### Mitigate

```
Probability Reduction Patterns:
- Upfront validation (PoC, Pilot)
- Training and education
- Review and inspection processes
- Redundancy and backup

Impact Reduction Patterns:
- Secure reserve resources
- Prepare alternative approaches
- Phased implementation (incremental delivery)
- Enhanced monitoring

Example:
  Risk: "Key staff attrition" (Probability 3, Impact 5 = Score 15)
  Mitigate: "Knowledge-sharing sessions + designate backup personnel"
  Residual: Probability 3, Impact 3 = Score 9 (🟡)
```

#### Accept

```
Active Acceptance:
- Allocate contingency reserve
- Develop contingency plan (Plan B)
- Set trigger + define response procedure

Passive Acceptance:
- Handle if and when the risk occurs (Score ≤ 4)
- Response cost is not justified relative to the risk value
```

## Risk Response Plan Template

```markdown
## Risk R01: [Risk Name]

### Current Assessment
- Probability: [N] / Impact: [N] / Score: [N×N] / Grade: [color]

### Response Strategy: [Avoid / Transfer / Mitigate / Accept]

### Response Actions
| # | Action | Owner | Deadline | Cost | Status |
|---|--------|-------|----------|------|--------|
| 1 | [Specific action] | [Name] | [Date] | [Amount] | In Progress |
| 2 | [Specific action] | [Name] | [Date] | [Amount] | Not Started |

### Residual Risk
- Post-response Probability: [N] / Impact: [N] / Score: [N×N]

### Trigger / Early Warning
- KRI: [Indicator] > [Threshold] → Activate
- Monitoring Frequency: [Weekly / Monthly]

### Contingency Plan (Plan B)
- [Fallback if primary response fails]
```

## Risk Monitoring Dashboard

### Risk Heat Map (Current vs. Target)

```
Current Status:
🔴 Extreme: 2 items (R01, R05)
🟠 High:    3 items (R02, R07, R09)
🟡 Medium:  5 items
🟢 Low:     8 items

Post-Response Target:
🔴 Extreme: 0 items
🟠 High:    1 item (R05)
🟡 Medium:  4 items
🟢 Low:     13 items
```

### Trend Tracking

| Risk | Previous Period | Current Period | Trend | Reason |
|------|----------------|---------------|-------|--------|
| R01 | 🔴 20 | 🟠 12 | ↓ Improved | Mitigation actions effective |
| R05 | 🟠 15 | 🔴 16 | ↑ Deteriorated | New issue identified |

## Quality Checklist

| Item | Criterion |
|------|-----------|
| Response Strategy | Explicitly selected from the 4 core strategies |
| Action Specificity | Owner + deadline + cost specified |
| Residual Risk | Re-assessed score after response applied |
| Triggers | KRI + threshold defined |
| Plan B | Contingency plan provided for Extreme/High risks |
| Cost-Benefit | Response cost < risk EMV |
