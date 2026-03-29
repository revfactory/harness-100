---
name: diagram-patterns
description: "Mermaid diagram pattern library. A collection of verified patterns that the diagram-maker agent references when creating diagrams for technical documentation. Use when 'diagram pattern', 'Mermaid template', or 'architecture diagram pattern' is requested. Actual image rendering and design tool operations are outside this skill's scope."
---

# Diagram Patterns — Mermaid Diagram Pattern Library

A collection of verified patterns that improve the diagram quality of the diagram-maker agent.

## Architecture Diagram Patterns

### Pattern 1: Layered Architecture

```mermaid
graph TD
    subgraph Presentation["Presentation Layer"]
        UI[Web UI]
        API_GW[API Gateway]
    end
    subgraph Business["Business Layer"]
        SVC1[Service A]
        SVC2[Service B]
    end
    subgraph Data["Data Layer"]
        DB[(Database)]
        CACHE[(Cache)]
    end
    UI --> API_GW
    API_GW --> SVC1 & SVC2
    SVC1 --> DB
    SVC2 --> CACHE --> DB
```

**When to use**: Monolithic or layer-separated systems
**Core rules**: Use subgraph to delineate layers; use TD direction; keep to 3–4 nodes per layer

### Pattern 2: Microservices Communication

```mermaid
graph LR
    CLIENT --> GW[API Gateway]
    GW --> AUTH[Auth]
    GW --> USER[User]
    GW --> ORDER[Order]
    ORDER --> PAYMENT[Payment]
    ORDER -.->|event| MQ[Message Queue]
    MQ -.-> NOTIFY[Notification]
    style MQ fill:#f9f,stroke:#333
```

**Core rules**: Synchronous = solid line, asynchronous = dashed line, highlight message queue with color

### Pattern 3: Cloud Infrastructure Topology

```mermaid
graph TD
    subgraph VPC["VPC (10.0.0.0/16)"]
        subgraph Public["Public Subnet"]
            ALB[ALB]
            NAT[NAT GW]
        end
        subgraph Private["Private Subnet"]
            ECS[ECS]
            RDS[(RDS)]
        end
    end
    INTERNET((Internet)) --> ALB --> ECS --> RDS
```

**Core rules**: Nested subgraph = network boundary; circle node = external

## Sequence Diagram Patterns

### Pattern 4: API Call (Happy Path + Error)

```mermaid
sequenceDiagram
    actor User
    participant FE as Frontend
    participant API as API Server
    participant DB as Database
    User->>FE: Request
    FE->>API: POST /resource
    API->>DB: INSERT
    alt Success
        DB-->>API: OK
        API-->>FE: 201
    else Failure
        DB-->>API: Error
        API-->>FE: 500
    end
```

**Core rules**: alt/else branching; request = solid line, response = dashed line

### Pattern 5: OAuth 2.0 Authentication Flow

```mermaid
sequenceDiagram
    Client->>Auth: 1. Authentication request
    Auth-->>Client: 2. Access + Refresh Token
    Client->>Resource: 3. API request (Bearer)
    Resource->>Auth: 4. Token validation
    Auth-->>Resource: 5. Valid
    Resource-->>Client: 6. Response
    Note over Client,Auth: On token expiry
    Client->>Auth: 7. Refresh
    Auth-->>Client: 8. New Token
```

## Flowchart Patterns

### Pattern 6: Decision Flow

```mermaid
flowchart TD
    START([Start]) --> CHECK{Condition check}
    CHECK -->|A| PA[Process A]
    CHECK -->|B| PB[Process B]
    PA & PB --> VALIDATE{Validate}
    VALIDATE -->|Pass| DONE([Done])
    VALIDATE -->|Fail| RETRY{Retry?}
    RETRY -->|Yes| CHECK
    RETRY -->|No| ERROR([Error])
```

**Core rules**: Diamond = decision; rounded rectangle = start/end; loop = circular arrow

### Pattern 7: CI/CD Pipeline

```mermaid
flowchart LR
    COMMIT --> BUILD --> TEST --> SCAN --> STAGING --> APPROVE{Approve}
    APPROVE -->|Yes| PROD[Deploy]
    APPROVE -->|No| ROLLBACK
    style PROD fill:#2d5
    style ROLLBACK fill:#d52
```

## ER Diagram Patterns

### Pattern 8: Data Model

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER_ITEM }o--|| PRODUCT : "refers to"
    USER { int id PK; string email UK; string name }
    ORDER { int id PK; int user_id FK; string status }
```

## State Diagram Patterns

### Pattern 9: State Transition

```mermaid
stateDiagram-v2
    [*] --> Received
    Received --> AwaitingPayment: Confirmed
    AwaitingPayment --> PaymentComplete: Success
    AwaitingPayment --> Cancelled: Failed
    PaymentComplete --> Shipping: Dispatched
    Shipping --> Completed: Received
    Completed --> [*]
    Cancelled --> [*]
```

## Diagram Quality Checklist

| Item | Standard |
|------|----------|
| Node count | 10 or fewer |
| Labels | 3–5 words |
| Arrow crossings | 0 |
| Legend / caption | Included in all diagrams |
| Colors | Only for meaningful differentiation; maximum 3 colors |
| subgraph depth | Maximum 2 levels |

## Anti-Patterns

| Anti-Pattern | Solution |
|-------------|----------|
| Spaghetti (arrow crossings) | Rearrange nodes, split into subgraphs |
| Excessive detail | Unify abstraction level |
| Unlabeled arrows | Add verb-form labels to all relationships |
| Inconsistent node shapes | Standardize by type |
