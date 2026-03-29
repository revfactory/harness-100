---
name: threat-modeling
description: "A guide to threat modeling methodologies (STRIDE, DREAD, Attack Tree, etc.) and strategies for identifying, evaluating, and responding to threats. Use this skill for system threat analysis involving 'STRIDE', 'DREAD', 'threat modeling', 'attack tree', 'attack surface', 'threat identification', 'security design', and similar topics. Enhances the threat analysis capabilities of security-consultant and pentest-reporter. Note: actual penetration test execution and CVE scanning are outside the scope of this skill."
---

# Threat Modeling — Threat Modeling Methodology Guide

A framework for systematically identifying and evaluating security threats in a system.

## STRIDE Threat Classification

| Threat | Description | Security Property | Response Pattern |
|--------|-------------|------------------|-----------------|
| **S**poofing | Identity impersonation | Authentication | MFA, certificates |
| **T**ampering | Data modification | Integrity | HMAC, digital signatures, checksums |
| **R**epudiation | Denial of actions | Non-repudiation | Audit logs, timestamps |
| **I**nformation Disclosure | Information leakage | Confidentiality | Encryption, access control |
| **D**enial of Service | Service disruption | Availability | Rate limiting, auto-scaling |
| **E**levation of Privilege | Privilege escalation | Authorization | RBAC, principle of least privilege |

## STRIDE Application Procedure

### Step 1: System Decomposition (DFD Construction)

```
┌────────┐    HTTPS     ┌──────────┐    SQL     ┌─────────┐
│ Browser │ ──────────→ │ Web App  │ ────────→ │   DB    │
│(external)│ ←────────── │(Trust    │ ←──────── │(Trust   │
└────────┘             │ Boundary)│           │Boundary)│
                       └────┬─────┘           └─────────┘
                            │ REST API
                            ▼
                       ┌──────────┐
                       │ External │
                       │   PG     │
                       │(external)│
                       └──────────┘

Threats originate at Trust Boundaries.
```

### Step 2: Per-Component STRIDE Analysis

```markdown
## Browser → Web App (HTTPS)
| Threat | Scenario | Risk Level | Response |
|--------|----------|-----------|----------|
| S | Session hijacking | High | HttpOnly, Secure cookies |
| T | Man-in-the-middle attack | High | TLS 1.3, HSTS |
| R | Anonymous requests | Medium | Request logging, mandatory authentication |
| I | Eavesdropping in transit | High | TLS |
| D | DDoS | High | WAF, Rate Limiting |
| E | Admin API access | High | Role-based access control |
```

## DREAD Risk Assessment

```
Score each item 1–10:

D (Damage): Extent of damage
R (Reproducibility): Ease of reproduction
E (Exploitability): Ease of exploitation
A (Affected Users): Proportion of impacted users
D (Discoverability): Ease of discovery

Risk Score = (D + R + E + A + D) / 5

Ratings:
├── 8–10: Critical (respond immediately)
├── 5–7: High (planned fix)
├── 3–4: Medium (monitor)
└── 1–2: Low (accept)
```

### Example Assessment

```
Threat: SQL Injection in Login API
├── Damage: 9 (full DB exfiltration possible)
├── Reproducibility: 8 (automated tooling available)
├── Exploitability: 7 (multiple public PoCs exist)
├── Affected Users: 10 (all users)
├── Discoverability: 9 (detectable by automated scanners)
└── Risk Score: (9+8+7+10+9)/5 = 8.6 → Critical
```

## Attack Tree

```
Goal: Gain administrator privileges
├── OR: Authentication bypass
│   ├── AND: SQL Injection + weak password hash
│   ├── Session hijacking
│   │   ├── OR: Cookie theft via XSS
│   │   └── OR: Network sniffing (HTTP)
│   └── Default administrator account
├── OR: Privilege escalation
│   ├── IDOR (direct admin API call)
│   ├── JWT tampering (role field)
│   └── API Gateway bypass
└── OR: Social engineering
    ├── Administrator phishing
    └── Insider collusion
```

## Attack Surface Analysis

### Web Application Attack Surface

| Surface | Components | Review Items |
|---------|-----------|-------------|
| **External API** | REST/GraphQL endpoints | Authentication, authorization, input validation |
| **Authentication** | Login, tokens, sessions | Brute force, session management |
| **File upload** | Profile pictures, attachments | File type validation, path traversal |
| **Third-party integrations** | OAuth, Webhook, API | SSRF, token exposure |
| **Administrative interfaces** | Admin panel, API | Access control, network segmentation |
| **Data storage** | DB, cache, logs | Encryption, access control |

## Threat Modeling Report Template

```markdown
# Threat Modeling Report

## System Overview
- Architecture diagram (DFD)
- Trust boundary identification

## Threat List
| ID | STRIDE | Threat Scenario | DREAD Score | Current Response | Residual Risk |
|----|--------|----------------|-------------|-----------------|--------------|
| T1 | S | Session hijacking | 7.2 | HttpOnly cookies | Medium |
| T2 | I | SQL Injection | 8.6 | Parameterized queries | Low |

## Attack Surface Summary
## Prioritized Response Plan
## Accepted Residual Risk List
```
