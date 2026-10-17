---
name: finding-classification
description: "Audit finding classification and reporting framework. Referenced by findings-analyst and recommendation-writer agents when systematically classifying findings and writing improvement recommendations. Used for 'finding classification', 'audit reporting', 'improvement recommendations' requests. Note: legal sanction decisions and disciplinary procedures are out of scope."
---

# Finding Classification — Finding Classification Framework

Enhances the finding classification and reporting capabilities of findings-analyst / recommendation-writer agents.

## Finding Rating System

### 4-Level Classification

| Rating | Name | Definition | Response Timeline |
|--------|------|-----------|-------------------|
| Critical | Critical | Risk of major loss/regulatory violation | Immediate (7 days) |
| High | High | Key control failure, recurring | 30 days |
| Medium | Medium | Partial control deficiency, improvement needed | 90 days |
| Low | Low | Efficiency improvement, best practice suggestion | 180 days |

### Classification Decision Tree

```
Q1: Financial impact exceeds $100K or regulatory violation?
├── YES → Critical
└── NO → Q2: Is the control failure recurring?
    ├── YES → High
    └── NO → Q3: Could it worsen without corrective action?
        ├── YES → Medium
        └── NO → Low
```

## Finding Report Structure

### Finding Card

```markdown
## Finding F-[Number]: [Title]

### Rating: [Critical/High/Medium/Low]

### Condition
[Current state discovered — facts only]

### Criteria
[Standard/regulation/policy that should apply]

### Cause
[Why the gap between criteria and condition occurred]

### Effect
[Current/potential impact — quantify where possible]

### Recommendation
[Specific improvement actions]

### Management Response
[Responsible department's response plan]
- Agreement: □ Agree □ Partially agree □ Disagree
- Corrective action: [Specific action]
- Owner: [Name/Title]
- Completion deadline: [YYYY-MM-DD]
```

## Root Cause Analysis

### Cause Categories

| Category | Description | Example |
|----------|-------------|---------|
| Policy/Procedure gap | Regulation missing or insufficient | Approval procedure not established |
| Personnel/Competency | Training or staffing deficiency | Owner not trained |
| System/Tools | IT control deficiency | Access rights management gaps |
| Supervision/Monitoring | Management review absence | Reconciliation not performed |
| Communication | Information transfer failure | Policy changes not shared |

## Recommendation Writing Rules

### SMART Recommendations

```
Bad example: "Controls should be strengthened"
Good example: "By June 2025, implement dual approval 
             for all expenditures exceeding $50,000, 
             and verify compliance through monthly reconciliation"
```

### Recommendation Priority Scoring

| Criteria | Weight |
|----------|--------|
| Risk reduction effect | 40% |
| Implementation ease | 25% |
| Cost efficiency | 20% |
| Urgency | 15% |

## Implementation Tracking Ledger

| Finding | Rating | Corrective Action | Owner | Deadline | Status | Verification Date |
|---------|--------|-------------------|-------|----------|--------|-------------------|
| F-01 | Critical | [Action] | [Name] | [Date] | In progress | - |
| F-02 | High | [Action] | [Name] | [Date] | Completed | [Date] |

### Status Definitions

| Status | Description |
|--------|-------------|
| Not started | Before corrective action begins |
| In progress | Corrective action underway |
| Completed | Correction done, awaiting verification |
| Verified | Auditor verification passed |
| Closed | Finalised |
| Overdue | Past deadline, incomplete |

## Quality Checklist

| Item | Criteria |
|------|----------|
| 4C structure | Condition, Criteria, Cause, Effect |
| Rating consistency | Decision tree applied |
| Quantification | Impact expressed in amounts/counts |
| SMART recommendations | Specific + Measurable + Time-bound |
| Management response | Agreement/disagreement recorded |
| Tracking | 5-stage status management |
