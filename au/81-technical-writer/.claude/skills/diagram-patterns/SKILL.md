---
name: diagram-patterns
description: "Mermaid diagram pattern library. diagram-maker agent technical document diagram writingto do when reference verifydone pattern . 'diagram pattern', 'Mermaid template', ' diagram pattern' request when usage. However, actual un-degree specialistperson tool work scope outside."
---

# Diagram Patterns — Mermaid diagram pattern library

diagram-maker agent diagram quality verifydone pattern .

## diagram pattern

### pattern 1: total (Layered Architecture)

```mermaid
graph TD
 subgraph Presentation["presentation total"]
 UI[web UI]
 API_GW[API Gateway]
 end
 subgraph Business[" total"]
 SVC1[service A]
 SVC2[service B]
 end
 subgraph Data["data total"]
 DB[(data)]
 CACHE[(when)]
 end
 UI --> API_GW
 API_GW --> SVC1 & SVC2
 SVC1 --> DB
 SVC2 --> CACHE --> DB
```

**usage timing**: /total minute whensystem
**core rule**: subgraph total minute, TD direction, total 3-4 within

### pattern 2: service communication

```mermaid
graph LR
 CLIENT --> GW[API Gateway]
 GW --> AUTH[authentication]
 GW --> USER[user]
 GW --> ORDER[weekdocument]
 ORDER --> PAYMENT
 ORDER -.->|event| MQ[message ]
 MQ -.-> NOTIFY
 style MQ fill:#f9f,stroke:#333
```

**core rule**: basis=actual, basis=point, message 

### pattern 3: person degree

```mermaid
graph TD
 subgraph VPC["VPC (10.0.0.0/16)"]
 subgraph Public[" from"]
 ALB[ALB]
 NAT[NAT GW]
 end
 subgraph Private[" from"]
 ECS[ECS]
 RDS[(RDS)]
 end
 end
 INTERNET((person)) --> ALB --> ECS --> RDS
```

**core rule**: during subgraph= total, KRW =external

## when diagram pattern

### pattern 4: API (Happy Path + Error)

```mermaid
sequenceDiagram
 actor User
 participant FE as 
 participant API as API from
 participant DB as data
 User->>FE: request
 FE->>API: POST /resource
 API->>DB: INSERT
 alt nature
 DB-->>API: OK
 API-->>FE: 201
 else failure
 DB-->>API: Error
 API-->>FE: 500
 end
```

**core rule**: alt/else minutebasis, request=actual, =point

### pattern 5: OAuth 2.0 authentication flow

```mermaid
sequenceDiagram
 Client->>Auth: 1. authentication request
 Auth-->>Client: 2. Access + Refresh Token
 Client->>Resource: 3. API request (Bearer)
 Resource->>Auth: 4. verify
 Auth-->>Resource: 5. 
 Resource-->>Client: 6. 
 Note over Client,Auth: when
 Client->>Auth: 7. Refresh
 Auth-->>Client: 8. Token
```

## flowchart pattern

### pattern 6: decision-making flow

```mermaid
flowchart TD
 START([whenwork]) --> CHECK{condition confirm}
 CHECK -->|A| PA[processing A]
 CHECK -->|B| PB[processing B]
 PA & PB --> VALIDATE{verify}
 VALIDATE -->|| DONE([complete])
 VALIDATE -->|failure| RETRY{re-when?}
 RETRY -->|example| CHECK
 RETRY -->|| ERROR([error])
```

**core rule**: =However, companyeach=whenwork/, =exchange table

### pattern 7: CI/CD pipeline

```mermaid
flowchart LR
 COMMIT --> BUILD --> TEST --> SCAN --> STAGING --> APPROVE{person}
 APPROVE -->|O| PROD[deployment]
 APPROVE -->|X| ROLLBACK
 style PROD fill:#2d5
 style ROLLBACK fill:#d52
```

## ER diagram pattern

### pattern 8: data model

```mermaid
erDiagram
 USER ||--o{ ORDER : places
 ORDER ||--|{ ORDER_ITEM : contains
 ORDER_ITEM }o--|| PRODUCT : "refers to"
 USER { int id PK; string email UK; string name }
 ORDER { int id PK; int user_id FK; string status }
```

## status diagram pattern

### pattern 9: status before

```mermaid
stateDiagram-v2
 [*] --> number
 number --> versusbasis: confirm
 versusbasis --> complete: nature
 versusbasis --> : failure
 complete --> during: 
 during --> complete: number
 complete --> [*]
 --> [*]
```

## diagram quality checklist

| item | standard |
|------|------|
| number | 10items within |
| | 3~5 |
| table gap | 0items |
| /caption | all diagram included |
| | un- minute, versus 3 |
| subgraph | versus 2stage |

## planpattern

| planpattern | |
|---------|--------|
| (table gap) | re-arrangement, subgraph minute |
| Korean taxdepartmentmatters | level day |
| table | all total company |
| consistency | typeby day |
