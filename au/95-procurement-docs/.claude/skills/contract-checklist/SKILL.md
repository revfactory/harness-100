---
name: contract-checklist
description: "Procurement contract review checklist. Referenced by contract-reviewer and acceptance-builder agents when reviewing contract terms and establishing acceptance criteria. Used for 'contract review', 'contract terms', 'acceptance criteria' requests. Note: legal counsel and contract notarization are out of scope."
---

# Contract Checklist — Procurement Contract Review Checklist

Enhances the contract review capabilities of contract-reviewer / acceptance-builder agents.

## Contract Review Essential Items

### Key Clause Checklist

| Clause | Verification Points | Risk Level |
|--------|-------------------|------------|
| Scope | Scope clarity, exclusions | High |
| Price | Fixed/variable, exchange rate, taxes | High |
| Delivery | Milestones, delay penalties | High |
| Quality | Acceptance criteria, SLA, warranty | High |
| Intellectual Property (IP) | Ownership, license, assignment | High |
| Confidentiality (NDA) | Scope, duration, breach penalties | Medium |
| Termination | Grounds, notice period, settlement | Medium |
| Liability Limitation | Damages cap, indemnification | Medium |
| Dispute Resolution | Arbitration/litigation, jurisdiction | Low |
| Force Majeure | Definition, notification, indemnification | Low |

### Price Clause Details

```
Verification items:
- [ ] Total contract amount specified
- [ ] Payment terms (advance/milestone/balance ratios)
- [ ] Payment timing (N days after delivery)
- [ ] Additional cost trigger conditions
- [ ] Price index clause (long-term contracts)
- [ ] Exchange rate fluctuation handling (international)
- [ ] Tax liability assignment
- [ ] Late payment interest rate
```

### SLA Clause Details

| SLA Item | Measurement Criteria | Non-compliance Action |
|----------|---------------------|----------------------|
| Availability | Monthly 99.9% | Credit refund |
| Response time | P1: 15 min, P2: 1 hour | Penalty |
| Resolution time | P1: 4 hours, P2: 8 hours | Escalation |
| Reporting | Monthly SLA report | Warning if not submitted |

## Acceptance Criteria Design

### Acceptance Process Steps

```
1. Establish acceptance plan (before delivery)
2. Confirm deliverable receipt
3. Functional/performance testing
4. Defect classification (Critical/Major/Minor)
5. Correction request (with deadline)
6. Re-inspection
7. Issue acceptance completion certificate
8. Authorize payment
```

### Acceptance Criteria Template

| Inspection Item | Criteria | Method | Pass Condition |
|----------------|----------|--------|----------------|
| Functional completeness | 100% requirements implemented | Checklist | Must-have 100%, Optional 80% |
| Performance | Response time ≤2s | Load test | P95 criteria met |
| Security | OWASP Top 10 addressed | Vulnerability scan | 0 Critical findings |
| Documentation | Manuals, API docs | Document review | 90%+ completeness |
| Training | Operator training complete | Training completion | 100% completion rate |

### Defect Classification

| Level | Definition | Handling |
|-------|-----------|----------|
| Critical | Core functionality unusable | Correction required, acceptance held |
| Major | Key functionality limited | Correction required, conditional acceptance |
| Minor | Minor issue | Next iteration fix, acceptance proceeds |

## Negotiation Points Guide

| Buyer-favorable | Vendor-favorable | Compromise |
|----------------|-----------------|------------|
| Delay penalties | Penalty waiver | Grace period |
| Fixed price | Variable price | Price index cap |
| Unlimited liability | Liability cap | N times contract value |
| Exclusive license | Non-exclusive | Use-restricted license |

## Quality Checklist

| Item | Criteria |
|------|----------|
| Key clauses | All 10 clauses reviewed |
| Risks | High-risk items legally reviewed |
| SLA | Measurement criteria + non-compliance actions |
| Acceptance | Items + criteria + methods specified |
| Defect classification | 3-level definition |
| Termination | Grounds + notice + settlement specified |
