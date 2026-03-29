---
name: decision-frameworks
description: "Decision-making framework library. Referenced by the framework-designer agent when designing decision structures for meetings. Use when 'decision matrix', 'DACI', or 'option evaluation' is requested. Note: building actual voting systems or decision automation tools is outside this skill's scope."
---

# Decision Frameworks — Decision-Making Framework Library

A collection of frameworks that strengthen the framework-designer agent's ability to design decision structures for meetings.

## Framework Mapping by Decision Type

| Decision Type | Complexity | Recommended Framework | Suitable Meeting |
|--------------|------------|----------------------|-----------------|
| Binary choice | Low | Pros and cons table | 10-min stand-up |
| Multiple option selection | Medium | Weighted scoring matrix | 30-min decision session |
| Strategic direction | High | DACI + scenario analysis | 60-min strategy meeting |
| Resource allocation | High | Priority matrix | Quarterly planning |
| Risk judgment | High | Expected value analysis | Executive briefing |

## DACI Framework

| Role | Description | Count |
|------|-------------|-------|
| **D**river | Leads the decision-making process | 1 person |
| **A**pprover | Gives final approval | 1 person |
| **C**ontributor | Provides input and information | N people |
| **I**nformed | Receives notification of the outcome | N people |

### DACI Document Template

```markdown
## Decision: [Title]
- Deadline: 2025-01-31
- Driver: [name / title]
- Approver: [name / title]
- Contributors: [name list]
- Informed: [name list]

### Background
[Why this decision is needed]

### Options
| Option | Description | Pros | Cons | Cost | Timeline |
|--------|-------------|------|------|------|----------|
| A | ... | ... | ... | ... | ... |
| B | ... | ... | ... | ... | ... |

### Recommendation
[Driver's recommendation and rationale]

### Decision
[Approver's final decision] — Date: ____
```

## Weighted Scoring Matrix

### Design Procedure

```
1. Define evaluation criteria (5–7 criteria)
2. Assign weights (total = 100%)
3. Score each option per criterion on a 1–5 scale
4. Weighted score = raw score × weight
5. Compare totals → select highest-scoring option
```

### Template

| Criterion | Weight | Option A | Option B | Option C |
|-----------|--------|---------|---------|---------|
| Cost efficiency | 30% | 4 (1.2) | 3 (0.9) | 5 (1.5) |
| Implementation difficulty | 25% | 3 (0.75) | 5 (1.25) | 2 (0.5) |
| Strategic fit | 25% | 5 (1.25) | 3 (0.75) | 4 (1.0) |
| Risk | 20% | 4 (0.8) | 4 (0.8) | 3 (0.6) |
| **Total** | **100%** | **4.0** | **3.7** | **3.6** |

## 2×2 Priority Matrix

### Eisenhower Matrix

```
              Urgency
          High         Low
  ┌───────────┬───────────┐
  │  DO NOW   │  SCHEDULE │
Im│  Act now  │  Plan it  │
po├───────────┼───────────┤
rt│  DELEGATE │  ELIMINATE│
  │  Hand off │  Remove   │
  └───────────┴───────────┘
```

### Impact-Effort Matrix

| | Low Effort | High Effort |
|---|-----------|------------|
| **High Impact** | Quick Win (do immediately) | Major Project (plan carefully) |
| **Low Impact** | Fill-in (do when available) | Thankless Task (eliminate) |

## Expected Value Analysis

```
Expected Value = Σ (Outcome × Probability)

Option A:
  Success (70%): +$500K → $350K
  Failure (30%): -$200K → -$60K
  Expected Value: +$290K

Option B:
  Success (90%): +$200K → $180K
  Failure (10%): -$50K → -$5K
  Expected Value: +$175K

→ By expected value, select Option A
→ However, if risk tolerance is low, select Option B (consider maximum loss)
```

## Consensus Methods

| Method | Description | Best For |
|--------|-------------|---------|
| Fist of Five | Show 1–5 fingers simultaneously | Quick consensus check |
| Dot Voting | Each person distributes sticker votes | Narrowing down many options |
| Roman Voting | 👍/👎/✊ simultaneously | Simple approve/reject |
| Gradients of Agreement | 8-level agreement spectrum | Surfacing nuanced differences |
| Decision Sprint | Time-boxed discussion + vote | Time-constrained decisions |

## Quality Checklist

| Item | Standard |
|------|---------|
| Role definition | DACI or equivalent roles assigned |
| Evaluation criteria | 5–7 pre-agreed criteria |
| Number of options | 2–5 (pre-filter if more) |
| Data basis | Quantitative basis for each option |
| Consensus method | Pre-agreed voting/consensus approach |
| Deadline | Decision deadline explicitly stated |
