---
name: query-optimization-patterns
description: "SQL/NoSQL 쿼리 최적화 패턴, 실행 계획 분석, 인덱스 전략, N+1 문제 해결 등 데이터베이스 성능 최적화 가이드. '쿼리 최적화', '실행 계획', 'EXPLAIN', '인덱스 설계', 'N+1 문제', '느린 쿼리', 'slow query', 'DB 성능' 등 데이터베이스 쿼리 성능 개선 시 이 스킬을 사용한다. bottleneck-analyst와 optimization-engineer의 DB 성능 분석 역량을 강화한다. 단, 전체 시스템 프로파일링이나 벤치마크 실행은 이 스킬의 범위가 아니다."
---

# Query Optimization Patterns — 쿼리 최적화 패턴 가이드

데이터베이스 쿼리 성능을 체계적으로 분석하고 최적화하는 방법론.

## 실행 계획 분석

### PostgreSQL EXPLAIN 읽기

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.created_at > '2024-01-01'
ORDER BY o.total_amount DESC
LIMIT 10;
```

### 핵심 지표 해석

| 지표 | 의미 | 위험 신호 |
|------|------|----------|
| **Seq Scan** | 전체 테이블 스캔 | 큰 테이블에서 발생 시 |
| **Nested Loop** | 행 단위 조인 | 외부 테이블이 클 때 |
| **Hash Join** | 해시 기반 조인 | work_mem 초과 시 디스크 사용 |
| **Sort** | 정렬 | 메모리 초과 시 외부 정렬 |
| **Bitmap Heap Scan** | 인덱스 → 테이블 접근 | lossy 비트맵 시 성능 저하 |
| **actual time** | 실제 소요 시간 | 첫 행 vs 전체 행 차이 |
| **rows** | estimated vs actual 차이 | 10배 이상 차이 → 통계 갱신 |

### 위험 패턴 탐지

```
❌ Seq Scan on large_table (rows=10000000)
   → 인덱스 추가 필요

❌ Sort Method: external merge (Disk: 256MB)
   → work_mem 증가 또는 인덱스 정렬

❌ Nested Loop (actual rows=1000000)
   → Hash Join 또는 Merge Join으로 전환

❌ estimated=100 actual=100000
   → ANALYZE 실행하여 통계 갱신
```

## 인덱스 전략

### 인덱스 유형별 사용

| 인덱스 유형 | 적합한 경우 | 부적합한 경우 |
|------------|-----------|-------------|
| B-Tree (기본) | 등호, 범위, 정렬 | 배열, JSON, 전문 검색 |
| Hash | 등호 비교만 | 범위 쿼리 |
| GIN | 배열, JSONB, 전문 검색 | 단순 등호/범위 |
| GiST | 지리공간, 범위 타입 | 단순 스칼라 |
| BRIN | 물리적으로 정렬된 데이터 | 랜덤 분포 |

### 복합 인덱스 설계 원칙

```sql
-- 왼쪽 접두사 규칙 (Leftmost Prefix)
CREATE INDEX idx_orders ON orders(status, created_at, customer_id);

-- 이 인덱스가 커버하는 쿼리:
✅ WHERE status = 'PAID'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01' AND customer_id = 123
❌ WHERE created_at > '2024-01-01'  (status 누락)
❌ WHERE customer_id = 123          (status, created_at 누락)

-- 컬럼 순서 결정 기준:
-- 1. 등호 조건 컬럼 먼저 (선택도 높은 것)
-- 2. 범위 조건 컬럼 다음
-- 3. ORDER BY 컬럼 마지막
```

### 커버링 인덱스

```sql
-- 테이블 접근 없이 인덱스만으로 쿼리 완료
CREATE INDEX idx_covering ON orders(status, created_at) INCLUDE (total_amount);

SELECT total_amount FROM orders
WHERE status = 'PAID' AND created_at > '2024-01-01';
-- Index Only Scan 발생 → 힙 접근 불필요
```

## N+1 문제 해결

### 문제 진단

```python
# N+1 패턴 (느림!)
orders = Order.objects.filter(status="PAID")  # 쿼리 1
for order in orders:
    print(order.customer.name)  # 쿼리 N (주문 수만큼)
# 총 쿼리: 1 + N

# Eager Loading으로 해결
orders = Order.objects.filter(status="PAID").select_related("customer")  # 쿼리 1 (JOIN)
# 또는
orders = Order.objects.filter(status="PAID").prefetch_related("items")  # 쿼리 2 (IN)
```

### ORM별 해결

| ORM | N+1 해결 | 방법 |
|-----|---------|------|
| Django | `select_related` / `prefetch_related` | FK JOIN / Reverse IN |
| SQLAlchemy | `joinedload` / `subqueryload` | JOIN / 서브쿼리 |
| TypeORM | `relations` / `@JoinColumn` | eager/lazy 설정 |
| Prisma | `include` | 자동 배치 |
| JPA | `@EntityGraph` / `JOIN FETCH` | JPQL/Criteria |

## 페이지네이션 최적화

| 방식 | SQL | 성능 | 적합 |
|------|-----|------|------|
| OFFSET | `LIMIT 20 OFFSET 10000` | O(N) — 느림 | 소규모, 초반 페이지 |
| Keyset | `WHERE id > 1000 LIMIT 20` | O(1) — 빠름 | 대규모, 무한 스크롤 |
| Cursor | 암호화된 keyset | O(1) | API, 클라이언트용 |

```sql
-- OFFSET (10000번째부터 → 10000행 스캔 후 버림)
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;

-- Keyset (즉시 해당 위치로)
SELECT * FROM orders WHERE id > 10000 ORDER BY id LIMIT 20;
```

## 쿼리 안티패턴

| 안티패턴 | 문제 | 해결 |
|---------|------|------|
| `SELECT *` | 불필요한 컬럼 전송 | 필요한 컬럼만 명시 |
| `WHERE func(column)` | 인덱스 사용 불가 | 변환을 상수 쪽으로 이동 |
| `LIKE '%keyword%'` | 풀스캔 | 전문 검색 인덱스(GIN) |
| 서브쿼리 IN (대량) | 느린 실행 | JOIN으로 전환 |
| 암시적 타입 변환 | 인덱스 무효화 | 타입 일치 |

## 쿼리 최적화 체크리스트

- [ ] EXPLAIN ANALYZE 실행하여 실행 계획 확인
- [ ] Seq Scan이 의도적인지 확인 (소량 데이터는 OK)
- [ ] estimated vs actual rows 차이 확인
- [ ] 필요한 인덱스 존재 여부
- [ ] N+1 쿼리 패턴 없는지 확인
- [ ] 페이지네이션이 keyset 기반인지 확인
- [ ] 불필요한 ORDER BY / DISTINCT 제거
- [ ] 트랜잭션 범위가 최소한인지 확인
