---
name: clause-risk-database
description: "A risk clause database that systematically identifies and grades risk patterns in contract clauses. The 'risk-assessor' and 'clause-analyst' agents must use this skill's pattern DB and scoring methodology when evaluating clause-level risk in contracts. Used for clause-level risk assessment tasks such as 'risk clause analysis', 'disadvantageous clause identification', 'risk scoring', etc. Note: Overall contract orchestration or contract drafting itself is outside the scope of this skill."
---

# Clause Risk Database — Risk Clause Pattern DB and Scoring Engine

A specialised knowledge base that identifies risk patterns in contract clauses and calculates quantitative risk scores.

## Risk Clause Pattern Classification System

### Tier 1: Critical Risk (80-100 points)

| Pattern ID | Pattern Name | Description | Representative Wording |
|-----------|-------------|-------------|----------------------|
| C-01 | Unlimited Liability | Full liability without cap | "shall indemnify all damages" |
| C-02 | Unilateral Termination | Only the counterparty can terminate unconditionally | "Party A may terminate immediately without cause" |
| C-03 | Blanket Indemnification | Complete exemption of counterparty's liability | "Party A shall not be liable under any circumstances" |
| C-04 | Unlimited IP Transfer | Transfer of all IP without consideration | "All rights to deliverables shall vest in Party A" |
| C-05 | Excessive Non-Compete | Non-compete with excessive scope in duration, geography, and range | "Prohibited from working in the same industry for 2 years" |

### Tier 2: High Risk (60-79 points)

| Pattern ID | Pattern Name | Description | Representative Wording |
|-----------|-------------|-------------|----------------------|
| H-01 | Auto-Renewal Trap | Excessive notice period + automatic renewal | "Auto-renews for 1 year without 60-day prior notice" |
| H-02 | Excessive Delay Penalties | Delay penalty rate exceeding market standard | "1% of contract amount per day of delay" |
| H-03 | Infinite Acceptance Loop | No limit on acceptance review count/duration | "Revisions shall continue until Party A is satisfied" |
| H-04 | One-Sided Confidentiality | Confidentiality obligation imposed on one party only | "Party B shall not disclose the contents of this contract" |
| H-05 | Unfavorable Jurisdiction | Exclusive jurisdiction at counterparty's location | "Court at Party A's headquarters location" |

### Tier 3: Medium Risk (40-59 points)

| Pattern ID | Pattern Name | Description |
|-----------|-------------|-------------|
| M-01 | Delayed Payment | Payment terms exceeding 60 days after acceptance |
| M-02 | Unlimited Change Requests | Lack of cost adjustment provisions for scope changes |
| M-03 | Unclear Completion Criteria | Ambiguous completion/acceptance standards |
| M-04 | Excessive Warranty Period | Warranty period exceeding industry standard |
| M-05 | Unspecified Governing Law | Unclear governing law in international transactions |

### Tier 4: Low Risk (20-39 points)

| Pattern ID | Pattern Name | Description |
|-----------|-------------|-------------|
| L-01 | Insufficient Notice Provisions | Absence of written/email notification rules |
| L-02 | No Assignment Restriction | Absence of restrictions on transfer of contractual rights/obligations |
| L-03 | Missing Force Majeure | Absence of force majeure exemption clause |

## Risk Scoring Algorithm

### Individual Clause Score Calculation

```
clause_score = base_score(pattern) x position_weight x contract_size_weight x industry_weight

position_weight:
  - Party A (advantaged side): 0.5
  - Party B (disadvantaged side): 1.5
  - Neutral/Unknown: 1.0

contract_size_weight:
  - Under 100M: 0.8
  - 100M-1B: 1.0
  - 1B-10B: 1.3
  - Over 10B: 1.5

industry_weight:
  - IT/Software Development: 1.2 (IP risk)
  - Construction: 1.3 (delay penalties, warranty)
  - Finance: 1.4 (regulatory risk)
  - General Services: 1.0
```

### Overall Risk Grade

```
overall_score = sum(weighted_clause_scores) / total_clause_count

Grades:
  S Grade (Immediate Correction): Overall 80+ or 1+ Critical clauses
  A Grade (Correction Recommended): Overall 60-79
  B Grade (Caution): Overall 40-59
  C Grade (Satisfactory): Overall 20-39
  D Grade (Excellent): Overall under 20
```

## Required Checkpoints by Contract Type

### Software Development Services

| Essential Clause | Risk if Missing | Recommended Standard |
|-----------------|----------------|---------------------|
| IP Ownership | IP dispute | Joint ownership or license |
| Source Code Delivery | Vendor lock-in | Escrow or direct delivery |
| Change Management (CR) | Scope creep | CR process specified |
| Acceptance Criteria/Period | Infinite revisions | Within 2 rounds, 14-day deadline |

### Lease Agreement

| Essential Clause | Risk if Missing | Recommended Standard |
|-----------------|----------------|---------------------|
| Deposit Return Conditions | Non-return | Within 30 days after vacating |
| Restoration Scope | Excessive restoration costs | Exclude normal wear and tear |
| Early Termination Terms | Penalty disputes | 3 months prior notice |

### NDA (Non-Disclosure Agreement)

| Essential Clause | Risk if Missing | Recommended Standard |
|-----------------|----------------|---------------------|
| Confidential Information Definition | Scope dispute | Marking/labeling approach |
| Duration | Infinite obligation | 2-3 years |
| Exceptions | Excessive restrictions | Public info, independent development, court orders |

## Risk Report Output Format

```markdown
## Contract Risk Scorecard

**Contract Type**: [Type]  |  **Party Position**: [A/B]  |  **Overall Grade**: [S/A/B/C/D]

| # | Clause | Pattern | Grade | Score | Modification Recommendation |
|---|--------|---------|-------|-------|-----------------------------|
| 1 | Article X | C-01 | Critical | 95 | Liability cap required |
```

## Notes

- Based on contract law practices; common law contracts require separate pattern application
- Detailed patterns: See `references/clause-patterns-detail.md`
