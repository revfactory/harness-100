---
name: threat-modeling
description: "STRIDE, DREAD, Attack Tree etc. threat model methodologyand threat identification·evaluation· strategy count guide. 'STRIDE', 'DREAD', 'threat model', 'threat modelling', 'attack tree', 'attack surface', 'threat identification', 'security ' etc. system threat analysis  this  for. security-consultantand pentest-reporterof threat analysis  -ize. , actual penetration test executionthis CVE  this of scope ."
---

# Threat Modelling — threat model methodology guide

systemof security threat systematicas identificationand evaluationlower framework.

## STRIDE threat classification

| threat | people | security  |  pattern |
|------|------|----------|----------|
| **S**poofing |   | authentication | MFA, authentication |
| **T**ampering | data  | integrity | HMAC,  people,  |
| **R**epudiation |   |   | audit log,  |
| **I**nformation Disclosure | information  |  | encryption,   |
| **D**enial of Service | service rejection | availability | Rate Limiting, auto-scaling |
| **E**levation of Privilege | permission upper | authorisation | RBAC, minimum permission principle |

## STRIDE -basedfor procedure

### Step 1: system minutes (DFD )

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

Trust Boundary( )from threatthis .
```

### Step 2: per STRIDE analysis

```markdown
## Browser → Web App (HTTPS)
| threat |  | riskalso |  |
|------|---------|--------|------|
| S | session lowerthis |  | HttpOnly, Secure key |
| T | between attack |  | TLS 1.3, HSTS |
| R | people request | between | request as, authentication required |
| I | before  also |  | TLS |
| D | DDoS |  | WAF, Rate Limiting |
| E | administrator API  |  | role    |
```

## DREAD risk evaluation

```
each item 1~10 evaluation:

D (Damage):  
R (Reproducibility):  forthis
E (Exploitability): attack forthis
A (Affected Users): impact user ratio
D (Discoverability):  forthis

riskalso = (D + R + E + A + D) / 5

etc.:
├── 8~10: Critical (immediate )
├── 5~7: High (planthe modification)
├── 3~4: Medium (monitoring)
└── 1~2: Low (countfor)
```

### example evaluation

```
threat: SQL Injection in Login API
├── Damage: 9 (before DB  possible)
├── Reproducibility: 8 (automatic-ize also )
├── Exploitability: 7 (items PoC count)
├── Affected Users: 10 (before user)
├── Discoverability: 9 (automatic as )
└── riskalso: (9+8+7+10+9)/5 = 8.6 → Critical
```

## Attack Tree

```
target: administrator permission acquisition
├── OR: authentication 
│   ├── AND: SQL Injection +  password hash
│   ├── session lowerthis
│   │   ├── OR: XSSas key 
│   │   └── OR: network  (HTTP)
│   └──  administrator account
├── OR: permission upper
│   ├── IDOR (administrator API direct )
│   ├── JWT  (role )
│   └── API Gateway 
└── OR: 
    ├── administrator 
    └── internal 
```

## attack  analysis

###  this attack 

|  |  |  item |
|------|------|----------|
| **external API** | REST/GraphQL endpoint | authentication, authorisation,  verification |
| **authentication** | log, token, session | root, session  |
| **day as** | as, day | day type verification, as  |
| **3 integration** | OAuth, Webhook, API | SSRF, token  |
| ** interface** | Admin , API |  ,  separated |
| **data ** | DB, cache, log | encryption,   |

## threat model report template

```markdown
# threat model report

## system items
- architecture thisthe (DFD)
-   identification

## threat 
| ID | STRIDE | threat  | DREAD count | current  |  risk |
|----|--------|-------------|-----------|----------|----------|
| T1 | S | session lowerthis | 7.2 | HttpOnly key | between |
| T2 | I | SQL Injection | 8.6 | parameter-ize query |  |

## attack  
## priorityper  plan
##  risk countfor 
```
