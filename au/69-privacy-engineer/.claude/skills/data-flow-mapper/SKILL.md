---
name: data-flow-mapper
description: "A data flow mapping tool that systematically maps personal information processing flows and identifies risk points. The 'pia-assessor' and 'process-architect' agents must utilise this skill's mapping methodology and risk point identification patterns when analysing data flows and designing protective measures. Use for 'data flow analysis', 'processing activity mapping', 'risk point identification', and similar tasks. Note that legal analysis or consent form drafting is outside the scope of this skill."
---

# Data Flow Mapper — Personal Information Data Flow Mapping Tool

Visualises the complete lifecycle of personal information — collection → processing → storage → transfer → destruction — and identifies risk points.

## Data Lifecycle Mapping Framework

### 6-Stage Lifecycle

```
Collection → Use → Storage → Sharing
    → Entrustment → Destruction

Checklist for each stage:
  Collection: items collected, collection channels, legal basis, consent method
  Use: processing purpose, processor, access permissions
  Storage: storage location, encryption, retention period
  Sharing: recipients, shared items, legal basis
  Entrustment: trustee, entrusted tasks, oversight and supervision
  Destruction: destruction timing, destruction method, destruction confirmation
```

### Record of Processing Activities (RoPA) Template

```
| Activity ID | Processing Purpose | Data Items | Data Subject | Legal Basis | Retention Period | Trustee | Cross-border Transfer |
|------------|-------------------|------------|--------------|-------------|-----------------|---------|----------------------|
| PA-001 | Member registration | Name, email, phone | Member | Consent | Upon withdrawal | - | - |
| PA-002 | Payment processing | Card number, account | Purchaser | Contract | 5 years | PG company | - |
| PA-003 | Marketing | Email, purchase history | Member | Consent (optional) | Upon consent withdrawal | Ad agency | AWS (USA) |
```

## Risk Point Identification Patterns

### High-Risk Data Flow Patterns

| Pattern ID | Pattern Name | Risk Description | Impact |
|-----------|-------------|-----------------|--------|
| DF-01 | Excessive collection | Collecting unnecessary items beyond the stated purpose | High |
| DF-02 | Use beyond purpose | Processing data for purposes other than the stated collection purpose | High |
| DF-03 | Insufficient encryption | Storing/transmitting sensitive information in plaintext | Critical |
| DF-04 | Undisclosed cross-border transfer | Missing notice/consent when using overseas servers | High |
| DF-05 | Unmanaged trustees | Absence of security management for entrusted vendors | High |
| DF-06 | Failure to destroy | Not destroying data after the retention period expires | Medium |
| DF-07 | No audit logs | Failure to record access/processing history | Medium |
| DF-08 | Excessive access privileges | Personal information accessible to unrelated personnel | High |

### Data Classification System

| Level | Data Type | Protection Level | Examples |
|-------|----------|-----------------|---------|
| Top Secret | Sensitive information | Separate consent + mandatory encryption | Health, beliefs, biometrics |
| Level 1 | Unique identifying information | Separate consent + mandatory encryption | National ID, passport, driver's license |
| Level 2 | General personal information | Consent + safety measures | Name, email, phone |
| Level 3 | Pseudonymized information | Safety measures | Pseudonymized data |
| Level 4 | Anonymized information | No restrictions | Statistical data |

## Data Flow Diagram Creation

### Text-Based DFD Notation

```
[Data Subject] ---(name, email)---> [Web Server]
[Web Server] ---(save to member DB)---> [RDS/MySQL]
[Web Server] ---(payment request)---> [PG Company API]
[RDS/MySQL] ---(backup)---> [S3 (Seoul Region)]
[RDS/MySQL] ---(analytics)---> [BigQuery (USA)] ⚠️ Cross-border transfer
[Batch Server] ---(marketing delivery)---> [Email Service] ⚠️ Entrustment
```

## Risk Assessment Scoring

```
Risk Score = Data_Sensitivity(1-5) × Processing_Scale(1-5) × Control_Absence(1-5)

Sensitivity: 5=Sensitive info  4=Unique identifier  3=General personal  2=Pseudonymized  1=Anonymized
Processing Scale: 5=1M+  4=100K+  3=10K+  2=1K+  1=Under 100
Control Absence: 5=No protective measures  4=Partial  3=Basic level  2=Good  1=Best-in-class

Risk Levels:
  75-125: 🔴 Immediate protective measures required
  40-74: 🟡 Improvement needed
  15-39: 🟢 Acceptable
  1-14: ⚪ Good
```

## References

- Based on GDPR Article 30 (RoPA) and Personal Information Protection Act Article 30
- Detailed mapping guide: see `references/data-flow-guide.md`
