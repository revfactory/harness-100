---
name: internal-control-framework
description: "Internal control framework guide. Referenced by scope-designer and checklist-builder agents when designing audit scope and control items. Used for 'COSO', 'internal controls', 'control testing' requests. Note: external audit representation and legal opinion preparation are out of scope."
---

# Internal Control Framework

Enhances the audit design capabilities of scope-designer / checklist-builder agents.

## COSO Internal Control Framework

### 5 Components

| Component | Description | Audit Points |
|-----------|-------------|-------------|
| Control Environment | Organizational culture, ethics, competence | Code of ethics, segregation of duties, training |
| Risk Assessment | Identification/analysis of risks to objectives | Risk assessment process, documentation |
| Control Activities | Policies/procedures responding to risks | Approvals, verification, physical controls |
| Information/Communication | Timely delivery of necessary information | Reporting structure, IT controls |
| Monitoring | Continuous evaluation of control effectiveness | Self-assessments, internal audit |

### Control Types

| Type | Description | Examples |
|------|-------------|---------|
| Preventive | Block before occurrence | Approval procedures, access restrictions, training |
| Detective | Discover after occurrence | Audit logs, reconciliation, anomaly detection |
| Corrective | Rectify after discovery | Corrective actions, rollback, recovery |

### Control Testing Methods

| Method | Description | Best For |
|--------|-------------|----------|
| Inquiry | Interview the owner | Initial understanding, process mapping |
| Observation | Observe actual execution | Field control verification |
| Inspection | Review documents/records | Evidence verification, approval records |
| Reperformance | Execute the control procedure | Direct verification of control effectiveness |

## Audit Scope Design Framework

### Risk-Based Audit Approach

```
1. Identify audit target processes
2. Assess inherent risk (amount, complexity, change)
3. Assess control risk (control design, operating effectiveness)
4. Residual risk = Inherent risk × Control risk
5. Prioritize audit by highest residual risk
```

### Audit Scope Definition Template

```markdown
## Audit Scope

### In-Scope
- Period: [YYYY-MM-DD to YYYY-MM-DD]
- Target: [Department/Process/System]
- Criteria: [Regulations/Policies/Laws]

### Out-of-Scope
- [Excluded items and rationale]

### Audit Criteria
| Criteria | Source |
|----------|--------|
| [Criteria 1] | [Internal policy/Law] |
| [Criteria 2] | [Industry standard] |
```

## Checklist Design Patterns

### Control Item Card

```markdown
## Control Item: [ID]-[Item Name]

- Category: [COSO component]
- Type: [Preventive/Detective/Corrective]
- Owner: [Department/Role]
- Frequency: [Daily/Weekly/Monthly/Quarterly/Annual]

### Control Description
[Specific control activity description]

### Test Procedure
1. [Test step 1]
2. [Test step 2]
3. [Verification criteria]

### Evidence
- [Required evidence list]

### Determination Criteria
- Effective: [Criteria]
- Partially effective: [Criteria]
- Ineffective: [Criteria]
```

## Quality Checklist

| Item | Criteria |
|------|----------|
| COSO coverage | 5 components reviewed |
| Risk-based | Residual risk-based prioritisation |
| Control types | Preventive/detective/corrective balance |
| Test methods | 2+ methods per item |
| Evidence | Required evidence specified per test |
| Determination | 3-level determination criteria |
