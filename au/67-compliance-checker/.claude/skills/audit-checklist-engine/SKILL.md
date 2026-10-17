---
name: audit-checklist-engine
description: "A systematic checklist generation engine for compliance audits. The 'status-auditor' and 'remediation-planner' agents must use this skill's audit framework and checklist templates when conducting status assessments and developing remediation plans. Used for 'audit checklist', 'compliance inspection form', 'compliance status assessment', etc. Note: Law mapping or full orchestration is outside the scope of this skill."
---

# Audit Checklist Engine — Compliance Audit Checklist Generation Engine

Converts regulatory obligations into practical inspection items and quantitatively assesses compliance levels.

## Audit Framework: 5-Level Maturity Model

### Compliance Maturity Levels

| Level | Name | Description | Score |
|-------|------|-------------|-------|
| L1 | Unaware | Unaware that the obligation exists | 0 |
| L2 | Aware/Non-Compliant | Aware but no action taken | 25 |
| L3 | Partially Compliant | Some actions completed, deficiencies exist | 50 |
| L4 | Fully Compliant | Minimum legal requirements met | 75 |
| L5 | Best Practice | Industry-leading level of operation | 100 |

### Overall Compliance Rate Calculation

```
compliance_rate(%) = sum(item_maturity_score x weight) / sum(weight x 100) x 100

weight calculation:
  - Criminal punishment related: 5.0
  - Business suspension related: 4.0
  - High fines (100M+): 3.0
  - General fines: 2.0
  - Administrative guidance: 1.0

grades:
  A (90%+): Excellent — maintain
  B (70-89%): Good — improvement items exist
  C (50-69%): Insufficient — systematic improvement needed
  D (30-49%): Poor — urgent improvement needed
  F (under 30%): Critical — immediate correction required
```

## Domain-Specific Audit Checklist Templates

### Personal Data Protection Audit (20 items)

**Collection and Use (6 items)**
- [ ] Legal basis mapping (consent/law/contract) completed for each collection item
- [ ] Mandatory and optional consent separation implemented
- [ ] Consent withdrawal procedure provided and equally convenient
- [ ] Purpose limitation controls in place
- [ ] Separate consent for sensitive and unique identification information
- [ ] Legal guardian consent for minors under 14

**Technical Safeguards (5 items)**
- [ ] Access authority management (principle of least privilege)
- [ ] Access log retention and tamper prevention (6+ months)
- [ ] Personal data encryption (SSL/TLS in transit, encryption at rest)
- [ ] Backup and recovery system
- [ ] Physical safeguards (locks, access control)

**Administrative Safeguards (5 items)**
- [ ] Privacy policy published (website homepage)
- [ ] Internal management plan established and implemented
- [ ] Privacy protection training at least once per year
- [ ] Privacy officer designated and published
- [ ] Processor management and supervision

**Destruction (4 items)**
- [ ] Prompt destruction upon retention period expiration
- [ ] Destruction using irrecoverable methods
- [ ] Destruction records maintained
- [ ] Separate storage when other law retention obligations apply

### Labour Law Audit (15 items)

**Working Conditions (5 items)**
- [ ] Written employment contract issued
- [ ] Work rules prepared and filed (10+ employees)
- [ ] Statutory working hours compliance (52 hours per week)
- [ ] Minimum wage or above paid
- [ ] Annual paid leave granted and usage promoted

**Safety and Health (5 items)**
- [ ] Safety and health management system established (50+ employees)
- [ ] Risk assessment conducted
- [ ] Safety and health training conducted
- [ ] Industrial accident reporting
- [ ] Work environment measurement (hazardous factors)

**Other (5 items)**
- [ ] Workplace harassment prevention training
- [ ] Sexual harassment prevention training (annual)
- [ ] Mandatory employment of persons with disabilities (50+ employees)
- [ ] Four major social insurance enrollment
- [ ] Retirement benefit system established

## Audit Report Output Structure

```markdown
## Compliance Audit Report

**Target**: [Organization Name] | **Audit Domain**: [Domain] | **Audit Date**: [Date]
**Overall Compliance Rate**: [XX]% | **Grade**: [A/B/C/D/F]

### Results Summary by Domain
| Domain | Inspection Items | Compliant | Non-Compliant | Compliance Rate |
|--------|-----------------|-----------|---------------|----------------|
| Personal Data | 20 | 15 | 5 | 75% |

### Immediate Correction Required (Red)
1. [Item] — Current Status: [L?], Risk: [Violation sanctions]

### Improvement Recommended (Yellow)
1. [Item] — Current Status: [L?], Recommendation: [Action content]

### Best Practices (Green)
1. [Item] — L5 achieved
```

## Improvement Priority Calculation Formula

```
priority_score = risk_impact(1-25) x (1 - current_compliance_rate) x cost_efficiency(1-5)

cost_efficiency:
  5: No cost/immediately possible (document preparation, training)
  4: Low cost/short-term (within 1 month)
  3: Medium cost/mid-term (within 3 months)
  2: High cost/long-term (6+ months)
  1: Major investment/system implementation

order: highest score first = quickly, at low cost, eliminating major risk
```

## Notes

- Reference structure from ISMS-P, ISO 27001, SOC2 frameworks
- Detailed checklists: See `references/checklist-templates.md`
