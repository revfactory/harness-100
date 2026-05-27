---
name: distributed-patterns
description: "분산 시스템 핵심 패턴(Saga, CQRS, Circuit Breaker, 이벤트 소싱 등)의 구현 가이드와 선택 매트릭스. '분산 트랜잭션', 'Saga 패턴', 'CQRS', '서킷 브레이커', '이벤트 소싱', '분산 패턴', '보상 트랜잭션', '최종 일관성' 등 분산 시스템 패턴 적용 시 이 스킬을 사용한다. communication-designer와 service-architect의 분산 시스템 설계 역량을 강화한다. 단, 인프라 구축이나 모니터링 설정은 이 스킬의 범위가 아니다."
---

# Distributed Patterns — 분산 시스템 핵심 패턴 가이드

마이크로서비스 간 통신, 데이터 일관성, 장애 대응을 위한 패턴 구현 상세.

## 1. Saga 패턴

### Choreography vs Orchestration 선택

| 기준 | Choreography | Orchestration |
|------|-------------|---------------|
| 서비스 수 | 2~4개 | 5개 이상 |
| 흐름 복잡도 | 선형 | 분기/조건부 |
| 결합도 | 이벤트 기반 느슨한 결합 | 오케스트레이터에 집중 |
| 가시성 | 흐름 추적 어려움 | 중앙에서 상태 관리 |
| 실패 처리 | 각 서비스 자체 보상 | 오케스트레이터가 보상 조율 |

### Orchestration Saga 구현

```
주문 Saga:
T1: 주문 생성 ──→ C1: 주문 취소
T2: 재고 차감 ──→ C2: 재고 복원
T3: 결제 처리 ──→ C3: 결제 환불
T4: 배송 요청 ──→ C4: 배송 취소

실패 시나리오 (T3 실패):
T1 → T2 → T3(실패) → C2(재고 복원) → C1(주문 취소)
```

### Saga 상태 머신

```
STARTED → INVENTORY_RESERVED → PAYMENT_PROCESSED → SHIPPING_REQUESTED → COMPLETED
    ↓           ↓                    ↓                    ↓
 FAILED → COMPENSATING_INVENTORY → COMPENSATING_PAYMENT → COMPENSATING_SHIPPING
                                                              ↓
                                                         COMPENSATED
```

## 2. CQRS (Command Query Responsibility Segregation)

```
┌──────────┐     Command     ┌───────────────┐
│  Client   │ ──────────────→│ Write Model   │──→ Event Store
│           │                │ (정규화 DB)    │
│           │     Query      ┌───────────────┐
│           │ ←──────────── │ Read Model    │←── Projection
│           │                │ (비정규화 뷰)  │
└──────────┘                └───────────────┘
```

**적용 기준:**

| 적용해야 할 때 | 적용하면 안 될 때 |
|--------------|----------------|
| 읽기/쓰기 부하 비대칭 (100:1) | 단순 CRUD 앱 |
| 읽기 모델과 쓰기 모델이 매우 다름 | 읽기/쓰기 모델이 거의 동일 |
| 복잡한 도메인 로직 + 다양한 뷰 | 최종 일관성 허용 불가 |
| 이벤트 소싱과 함께 사용 | 팀 규모가 작음 (< 3명) |

## 3. Circuit Breaker

### 상태 전이

```
CLOSED ──(실패율 > 임계값)──→ OPEN
   ↑                            │
   │                        (타임아웃 후)
   │                            ↓
   └──(성공)── HALF_OPEN ──(실패)──→ OPEN
```

### 설정 가이드

| 파라미터 | 권장값 | 설명 |
|---------|-------|------|
| failureRateThreshold | 50% | OPEN 전환 실패율 |
| slowCallRateThreshold | 80% | 느린 호출 비율 임계 |
| slowCallDurationThreshold | 3s | 느린 호출 기준 |
| waitDurationInOpenState | 30s | HALF_OPEN 전환 대기 |
| slidingWindowSize | 100 | 측정 윈도우 크기 |
| minimumNumberOfCalls | 10 | 최소 호출 수 |

### Fallback 전략

| 전략 | 적용 | 예시 |
|------|------|------|
| 캐시 응답 | 읽기 API | 마지막 성공 응답 반환 |
| 기본값 | 비핵심 기능 | 추천 목록 대신 인기 상품 |
| 대체 서비스 | 결제 | 주 PG 장애 시 보조 PG |
| 큐잉 | 비동기 가능 | 주문을 큐에 저장 후 처리 |
| 에러 응답 | 핵심 기능 | 명확한 오류 메시지 |

## 4. Event Sourcing

```
전통 방식: 현재 상태만 저장
  Account { balance: 750 }

이벤트 소싱: 모든 변경 이력 저장
  1. AccountOpened  { id: A1 }
  2. MoneyDeposited { amount: 1000 }
  3. MoneyWithdrawn { amount: 250 }
  → 현재 상태 재구성: balance = 0 + 1000 - 250 = 750
```

**스냅샷 전략:**

| 전략 | 조건 | 장점 |
|------|------|------|
| 이벤트 수 기반 | N개마다 스냅샷 | 예측 가능한 성능 |
| 시간 기반 | N분마다 스냅샷 | 일정한 복구 시간 |
| 온디맨드 | 읽기 시 캐시 미스 | 저장 공간 절약 |

## 5. API Gateway 패턴

| 패턴 | 설명 | 적용 |
|------|------|------|
| **API Composition** | 여러 서비스 응답 합성 | BFF (Backend for Frontend) |
| **Rate Limiting** | 요청 속도 제한 | Token Bucket / Sliding Window |
| **Request Routing** | 경로 기반 라우팅 | /api/v1/orders → order-service |
| **Protocol Translation** | 프로토콜 변환 | REST → gRPC, WebSocket → HTTP |

## 패턴 조합 레시피

### 이커머스 주문 처리
```
Saga(Orchestration) + Event Sourcing + CQRS
├── 주문 Saga: 재고→결제→배송 조율
├── 각 서비스: 이벤트 소싱으로 감사 추적
└── 주문 조회: CQRS Read Model로 빠른 조회
```

### 실시간 채팅
```
Event-Driven + Circuit Breaker + API Gateway
├── 메시지: 이벤트 스트리밍 (Kafka)
├── 부가 기능: Circuit Breaker (번역, 필터링)
└── 클라이언트: WebSocket Gateway
```

## CAP 정리 실무 적용

```
              일관성 (Consistency)
                    /\
                   /  \
              CP  /    \ CA
                 /      \
                /________\
    가용성(A) ────────── 분단허용(P)
                  AP

실무 선택:
- CP: 결제, 재고 (정확성 최우선)
- AP: 상품 조회, 추천 (가용성 최우선)
- CA: 단일 노드 DB (분산 아님)
```
