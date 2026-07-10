---
name: diagram-patterns
description: "Mermaid 다이어그램 패턴 라이브러리. diagram-maker 에이전트가 기술 문서용 다이어그램을 작성할 때 참조하는 검증된 패턴 모음. '다이어그램 패턴', 'Mermaid 템플릿', '아키텍처 다이어그램 패턴' 요청 시 사용. 단, 실제 이미지 렌더링이나 디자인 도구 조작은 범위 밖."
---

# Diagram Patterns — Mermaid 다이어그램 패턴 라이브러리

diagram-maker 에이전트의 다이어그램 품질을 높이는 검증된 패턴 모음.

## 아키텍처 다이어그램 패턴

### 패턴 1: 계층형 아키텍처 (Layered Architecture)

```mermaid
graph TD
    subgraph Presentation["프레젠테이션 계층"]
        UI[웹 UI]
        API_GW[API Gateway]
    end
    subgraph Business["비즈니스 계층"]
        SVC1[서비스 A]
        SVC2[서비스 B]
    end
    subgraph Data["데이터 계층"]
        DB[(데이터베이스)]
        CACHE[(캐시)]
    end
    UI --> API_GW
    API_GW --> SVC1 & SVC2
    SVC1 --> DB
    SVC2 --> CACHE --> DB
```

**사용 시점**: 모놀리식/계층 분리 시스템
**핵심 규칙**: subgraph로 계층 구분, TD 방향, 계층당 3-4 노드 이내

### 패턴 2: 마이크로서비스 통신

```mermaid
graph LR
    CLIENT --> GW[API Gateway]
    GW --> AUTH[인증]
    GW --> USER[사용자]
    GW --> ORDER[주문]
    ORDER --> PAYMENT[결제]
    ORDER -.->|이벤트| MQ[메시지 큐]
    MQ -.-> NOTIFY[알림]
    style MQ fill:#f9f,stroke:#333
```

**핵심 규칙**: 동기=실선, 비동기=점선, 메시지 큐 색상 강조

### 패턴 3: 클라우드 인프라 토폴로지

```mermaid
graph TD
    subgraph VPC["VPC (10.0.0.0/16)"]
        subgraph Public["퍼블릭 서브넷"]
            ALB[ALB]
            NAT[NAT GW]
        end
        subgraph Private["프라이빗 서브넷"]
            ECS[ECS]
            RDS[(RDS)]
        end
    end
    INTERNET((인터넷)) --> ALB --> ECS --> RDS
```

**핵심 규칙**: 중첩 subgraph=네트워크 경계, 원형 노드=외부

## 시퀀스 다이어그램 패턴

### 패턴 4: API 호출 (Happy Path + Error)

```mermaid
sequenceDiagram
    actor User
    participant FE as 프론트엔드
    participant API as API 서버
    participant DB as 데이터베이스
    User->>FE: 요청
    FE->>API: POST /resource
    API->>DB: INSERT
    alt 성공
        DB-->>API: OK
        API-->>FE: 201
    else 실패
        DB-->>API: Error
        API-->>FE: 500
    end
```

**핵심 규칙**: alt/else 분기, 요청=실선, 응답=점선

### 패턴 5: OAuth 2.0 인증 흐름

```mermaid
sequenceDiagram
    Client->>Auth: 1. 인증 요청
    Auth-->>Client: 2. Access + Refresh Token
    Client->>Resource: 3. API 요청 (Bearer)
    Resource->>Auth: 4. 토큰 검증
    Auth-->>Resource: 5. 유효
    Resource-->>Client: 6. 응답
    Note over Client,Auth: 토큰 만료 시
    Client->>Auth: 7. Refresh
    Auth-->>Client: 8. 새 Token
```

## 플로차트 패턴

### 패턴 6: 의사결정 흐름도

```mermaid
flowchart TD
    START([시작]) --> CHECK{조건 확인}
    CHECK -->|A| PA[처리 A]
    CHECK -->|B| PB[처리 B]
    PA & PB --> VALIDATE{검증}
    VALIDATE -->|통과| DONE([완료])
    VALIDATE -->|실패| RETRY{재시도?}
    RETRY -->|예| CHECK
    RETRY -->|아니오| ERROR([에러])
```

**핵심 규칙**: 다이아몬드=판단, 둥근 사각형=시작/종료, 루프=순환 화살표

### 패턴 7: CI/CD 파이프라인

```mermaid
flowchart LR
    COMMIT --> BUILD --> TEST --> SCAN --> STAGING --> APPROVE{승인}
    APPROVE -->|O| PROD[배포]
    APPROVE -->|X| ROLLBACK
    style PROD fill:#2d5
    style ROLLBACK fill:#d52
```

## ER 다이어그램 패턴

### 패턴 8: 데이터 모델

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER_ITEM }o--|| PRODUCT : "refers to"
    USER { int id PK; string email UK; string name }
    ORDER { int id PK; int user_id FK; string status }
```

## 상태 다이어그램 패턴

### 패턴 9: 상태 전이

```mermaid
stateDiagram-v2
    [*] --> 접수
    접수 --> 결제대기: 확인
    결제대기 --> 결제완료: 성공
    결제대기 --> 취소: 실패
    결제완료 --> 배송중: 출고
    배송중 --> 완료: 수령
    완료 --> [*]
    취소 --> [*]
```

## 다이어그램 품질 체크리스트

| 항목 | 기준 |
|------|------|
| 노드 수 | 10개 이내 |
| 레이블 | 3~5단어 |
| 화살표 교차 | 0개 |
| 범례/캡션 | 모든 다이어그램에 포함 |
| 색상 | 의미 있는 구분에만, 최대 3색 |
| subgraph 깊이 | 최대 2단계 |

## 안티패턴

| 안티패턴 | 해결책 |
|---------|--------|
| 스파게티 (화살표 교차) | 노드 재배치, subgraph 분리 |
| 과도한 세부사항 | 추상화 수준 통일 |
| 레이블 없는 화살표 | 모든 관계에 동사형 레이블 |
| 일관성 없는 노드 모양 | 유형별 통일 |
