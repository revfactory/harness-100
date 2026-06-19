---
name: threat-modeling
description: "A guide to threat modeling methodologies such as STRIDE, DREAD, and Attack Tree, and to establishing threat identification, evaluation, and response strategies. Use this skill for system threat analysis, including 'STRIDE', 'DREAD', 'threat modeling', 'attack tree', 'attack surface', 'threat identification', 'security design', and similar requests. It enhances the threat analysis capabilities of security-consultant and pentest-reporter. However, actual penetration test execution and CVE scanning are out of scope for this skill."
---

# Threat Modeling — threat modeling methodology guide

A framework for systematically identifying and evaluating a system's security threats.

## STRIDE threat classification

| Threat | Description | Security property | Response pattern |
|------|------|----------|----------|
| **S**poofing | Identity spoofing | Authentication | MFA, certificates |
| **T**ampering | Data tampering | Integrity | HMAC, digital signatures, checksums |
| **R**epudiation | Repudiation of actions | Non-repudiation | Audit logs, timestamps |
| **I**nformation Disclosure | Information leakage | Confidentiality | Encryption, access control |
| **D**enial of Service | Denial of service | Availability | Rate Limiting, auto-scaling |
| **E**levation of Privilege | Privilege escalation | Authorization | RBAC, principle of least privilege |

## STRIDE application procedure

### Step 1: System decomposition (DFD creation)

```
┌────────┐    HTTPS     ┌──────────┐    SQL     ┌─────────┐
│ Browser │ ──────────→ │ Web App  │ ────────→ │   DB    │
│(external)   │ ←────────── │(Trust    │ ←──────── │(Trust   │
└────────┘             │ Boundary)│           │Boundary)│
                       └────┬─────┘           └─────────┘
                            │ REST API
                            ▼
                       ┌──────────┐
                       │ external PG  │
                       │(external)    │
                       └──────────┘

Threats arise at the Trust Boundary.
```

### Step 2: Per-element STRIDE analysis

```markdown
## Browser → Web App (HTTPS)
| Threat | Scenario | Risk level | Response |
|------|---------|--------|------|
| S | Session hijacking | High | HttpOnly, Secure cookies |
| T | Man-in-the-middle attack | High | TLS 1.3, HSTS |
| R | Anonymous requests | Medium | Request logging, require authentication |
| I | Eavesdropping in transit | High | TLS |
| D | DDoS | High | WAF, Rate Limiting |
| E | Admin API access | High | Role-based access control |
```

## DREAD risk evaluation

```
Rate each item 1~10:

D (Damage): scale of damage
R (Reproducibility): ease of reproduction
E (Exploitability): ease of attack
A (Affected Users): proportion of users affected
D (Discoverability): ease of discovery

risk level = (D + R + E + A + D) / 5

Grades:
├── 8~10: Critical (respond immediately)
├── 5~7: High (planned fix)
├── 3~4: Medium (monitoring)
└── 1~2: Low (accept)
```

### Example evaluation

```
Threat: SQL Injection in Login API
├── Damage: 9 (entire DB can be exfiltrated)
├── Reproducibility: 8 (automation tools exist)
├── Exploitability: 7 (many public PoCs)
├── Affected Users: 10 (all users)
├── Discoverability: 9 (found by automated scanners)
└── risk level: (9+8+7+10+9)/5 = 8.6 → Critical
```

## Attack Tree

```
Goal: gain administrator privileges
├── OR: authentication bypass
│   ├── AND: SQL Injection + weak password hash
│   ├── session hijacking
│   │   ├── OR: cookie theft via XSS
│   │   └── OR: network sniffing (HTTP)
│   └── default administrator account
├── OR: privilege escalation
│   ├── IDOR (direct call to admin API)
│   ├── JWT tampering (role field)
│   └── API Gateway bypass
└── OR: social engineering
    ├── administrator phishing
    └── insider collusion
```

## Attack surface analysis

### Web application attack surface

| Surface | Element | Check items |
|------|------|----------|
| **External API** | REST/GraphQL endpoints | Authentication, authorization, input validation |
| **Authentication** | Login, token, session | Brute force, session management |
| **File upload** | Profile, attachments | File type validation, path manipulation |
| **Third-party integration** | OAuth, Webhook, API | SSRF, token exposure |
| **Admin interface** | Admin panel, API | Access control, network segregation |
| **Data storage** | DB, cache, logs | Encryption, access control |

## Threat modeling report template

```markdown
# Threat modeling report

## System overview
- Architecture diagram (DFD)
- Trust boundary identification

## Threat list
| ID | STRIDE | Threat scenario | DREAD score | Current response | Residual risk |
|----|--------|-------------|-----------|----------|----------|
| T1 | S | Session hijacking | 7.2 | HttpOnly cookies | Medium |
| T2 | I | SQL Injection | 8.6 | Parameterized queries | Low |

## Attack surface summary
## Prioritized response plan
## Residual risk acceptance list
```
