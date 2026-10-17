---
name: regulation-knowledge-base
description: "A structured knowledge base of key regulatory laws. The 'law-mapper' and 'gap-analyst' agents must use this skill's law database and mapping methodology when identifying applicable laws by industry and mapping obligations. Used for 'applicable law verification', 'regulatory mapping', 'obligation extraction', etc. Note: Full compliance orchestration or remediation planning is outside the scope of this skill."
---

# Regulation Knowledge Base — Structured Regulatory Law Knowledge Base

Systematically maps applicable laws, obligations, and penalty criteria by industry sector.

## Industry-Specific Key Applicable Law Matrix

### IT/Online Services

| Law | Application Condition | Key Obligations | Violation Sanctions |
|-----|----------------------|----------------|-------------------|
| Personal Information Protection Act | When processing personal data | Consent for collection, privacy policy disclosure, safety measures | Fines up to 50M, 3% of revenue |
| Information and Communications Network Act | When providing online services | Technical safeguards, breach incident reporting | Fines up to 30M |
| E-Commerce Act | When selling goods/services | Right of withdrawal, labeling/advertising, payment | Fines up to 100M |
| Location Information Act | When collecting location data | Location service business registration, consent | Fines up to 50M |
| Electronic Financial Transactions Act | When providing payment services | E-finance business registration, security | Fines up to 50M |

### Finance

| Law | Application Condition | Key Obligations |
|-----|----------------------|----------------|
| Capital Markets Act | Financial investment business | Authorisation, business conduct regulation, disclosure |
| Banking Act | Banking business | Authorisation, soundness regulation, BIS |
| Insurance Business Act | Insurance business | License, solvency, solicitation regulation |
| Specialised Credit Finance Act | Cards/Leasing/Installments | Registration, interest rate limits |
| Specific Financial Information Act | Virtual assets | Reporting, AML/KYC |

### Healthcare

| Law | Application Condition | Key Obligations |
|-----|----------------------|----------------|
| Medical Service Act | Medical practice | Medical facility establishment, practitioner licensing |
| Pharmaceutical Affairs Act | Drug handling | Authorisation, GMP, distribution management |
| Medical Devices Act | Medical devices | Manufacturing/import authorisation, clinical trials |
| Bioethics Act | Human-derived material research | IRB review, consent |

### Manufacturing/Distribution

| Law | Application Condition | Key Obligations |
|-----|----------------------|----------------|
| Occupational Safety and Health Act | Workplace operation | Safety and health management system, risk assessment |
| Chemical Substances Control Act | Chemical handling | Hazardous chemical business permit |
| Food Sanitation Act | Food manufacturing/sales | Business permit, HACCP |
| Framework Act on Product Safety | Product distribution | Safety certification, recall |

## Organisation Size-Based Law Application Branches

### By Number of Employees

| Scale | Additional Applicable Laws/Obligations |
|-------|---------------------------------------|
| 5+ employees | Full application of Labour Standards Act, work rules |
| 10+ employees | Obligation to report work rules |
| 30+ employees | Act on Employment Promotion for Persons with Disabilities (mandatory employment) |
| 50+ employees | Occupational safety and health committee, safety and health manager |
| 100+ employees | Employment impact assessment, workplace childcare facility |
| 300+ employees | Large business group disclosure, ESG |
| 1000+ employees | Serious Accidents Punishment Act immediate application |

## Obligation Structuring Template

```
[Obligation ID]: REG-{law_code}-{clause_number}
[Law]: {Law Name} Article {X}
[Obligation Type]: Permit/License | Registration | Reporting | Action | Record | Training
[Obligation Content]: {Specific obligation details}
[Compliance Cycle]: Ongoing | Annually | Quarterly | Upon occurrence
[Supervisory Authority]: {Regulatory body}
[Violation Sanction]: {Fines/Penalties/Administrative action}
[Evidence Documents]: {Compliance documentation}
```

## Risk Impact Assessment

```
impact = probability(1-5) x severity(1-5)

severity criteria:
  5: Criminal punishment, business suspension
  4: Fine 100M+, corrective order
  3: Fine up to 50M, warning
  2: Fine up to 10M, improvement recommendation
  1: Administrative guidance, voluntary correction

impact grades:
  20-25: Immediate response (Red)
  12-19: Early response (Orange)
  6-11: Planned response (Yellow)
  1-5: Monitoring (Green)
```

## Notes

- Must verify latest information according to law amendment cycles
- Detailed law explanations: See `references/regulation-details.md`
