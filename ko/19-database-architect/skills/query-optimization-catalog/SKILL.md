---
name: query-optimization-catalog
description: "SQL 쿼리 최적화 카탈로그. 인덱스 전략(B-Tree/Hash/GIN/GiST), 실행 계획 분석, N+1 문제 해결, 파티셔닝 전략, 슬로우 쿼리 패턴별 최적화 기법을 제공하는 performance-analyst 확장 스킬. '쿼리 최적화', '인덱스 설계', '실행 계획', 'N+1 문제', '파티셔닝', '슬로우 쿼리' 등 DB 성능 분석 시 사용한다. 단, 데이터 모델링이나 보안 설정은 이 스킬의 범위가 아니다."
---

# Query Optimization Catalog — SQL 쿼리 최적화 카탈로그

performance-analyst 에이전트가 성능 최적화 시 활용하는 인덱스 전략, 실행 계획 분석, 쿼리 안티패턴 해결 레퍼런스.

## 대상 에이전트

`performance-analyst` — 이 스킬의 최적화 기법을 성능 분석과 인덱스 설계에 직접 적용한다.

## 인덱스 전략

### 인덱스 유형별 선택 가이드

| 인덱스 유형 | 적합 쿼리 | DBMS | 특징 |
|-----------|----------|------|------|
| **B-Tree** | `=`, `<`, `>`, `BETWEEN`, `ORDER BY` | 전체 | 범용, 기본값 |
| **Hash** | `=` 동등 비교만 | PostgreSQL, MySQL | 범위 검색 불가 |
| **GIN** | 배열, JSONB, 전문검색 | PostgreSQL | 다중값 인덱싱 |
| **GiST** | 공간(geometry), 범위 | PostgreSQL | PostGIS, 범위 타입 |
| **BRIN** | 시계열, 자연 정렬 데이터 | PostgreSQL | 매우 작은 크기 |
| **Fulltext** | 전문검색 | MySQL, PostgreSQL | LIKE '%word%' 대체 |

### 복합 인덱스 설계 원칙

#### 왼쪽 접두사 규칙 (Leftmost Prefix)
```sql
INDEX idx_abc ON table(a, b, c)

-- 활용 가능:
WHERE a = 1                          -- O (a만)
WHERE a = 1 AND b = 2               -- O (a, b)
WHERE a = 1 AND b = 2 AND c = 3     -- O (전체)
WHERE a = 1 AND c = 3               -- 부분 (a만, c 건너뜀)

-- 활용 불가:
WHERE b = 2                          -- X (a 누락)
WHERE c = 3                          -- X (a, b 누락)
```

#### 컬럼 순서 결정 규칙
1. **WHERE 등호(=) 조건** 컬럼 먼저
2. **정렬(ORDER BY)** 컬럼 다음
3. **범위(<, >, BETWEEN)** 컬럼 마지막
4. **카디널리티** 높은 것 먼저 (단, 규칙 1~3 우선)

### 커버링 인덱스
인덱스만으로 쿼리 결과를 반환 (테이블 접근 불필요).

```sql
-- 커버링 인덱스
CREATE INDEX idx_covering ON orders(user_id, status, created_at);

-- 이 쿼리는 인덱스만으로 응답 (Index Only Scan)
SELECT status, created_at FROM orders WHERE user_id = 123;
```

### 인덱스 생성/삭제 판단

| 상황 | 인덱스 추가? | 이유 |
|------|-----------|------|
| WHERE 절에 자주 사용되는 컬럼 | O | 검색 속도 향상 |
| JOIN ON 절의 FK 컬럼 | O | JOIN 성능 |
| ORDER BY 자주 사용되는 컬럼 | O | 정렬 회피 |
| 매우 낮은 카디널리티 (boolean 등) | X | 효과 미미 |
| 자주 UPDATE되는 컬럼 | 신중히 | 쓰기 성능 저하 |
| 작은 테이블 (1만 행 미만) | X | 풀스캔이 더 빠름 |

## 슬로우 쿼리 안티패턴 & 해결

### 1. N+1 문제
```sql
-- 안티패턴: 루프에서 개별 쿼리
SELECT * FROM users;
-- 각 user마다:
SELECT * FROM orders WHERE user_id = ?;  -- N번 반복!

-- 해결: JOIN 또는 IN
SELECT u.*, o.* FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 또는 배치 로딩
SELECT * FROM orders WHERE user_id IN (1, 2, 3, ...);
```

### 2. SELECT *
```sql
-- 안티패턴
SELECT * FROM products WHERE category = 'electronics';

-- 해결: 필요한 컬럼만
SELECT id, name, price FROM products WHERE category = 'electronics';
-- 커버링 인덱스 활용 가능
```

### 3. 함수 사용으로 인덱스 무효화
```sql
-- 안티패턴: 인덱스 컬럼에 함수 적용
WHERE YEAR(created_at) = 2025

-- 해결: 범위 조건으로 변환
WHERE created_at >= '2025-01-01' AND created_at < '2026-01-01'
```

### 4. OR 조건의 인덱스 무효화
```sql
-- 안티패턴
WHERE status = 'active' OR category = 'books'

-- 해결: UNION ALL
SELECT * FROM products WHERE status = 'active'
UNION ALL
SELECT * FROM products WHERE category = 'books' AND status != 'active'
```

### 5. 서브쿼리 vs JOIN
```sql
-- 안티패턴: 상관 서브쿼리
SELECT * FROM orders o
WHERE o.total > (SELECT AVG(total) FROM orders WHERE user_id = o.user_id);

-- 해결: JOIN + 집계
SELECT o.* FROM orders o
JOIN (SELECT user_id, AVG(total) as avg_total FROM orders GROUP BY user_id) a
ON o.user_id = a.user_id
WHERE o.total > a.avg_total;
```

### 6. OFFSET 페이지네이션
```sql
-- 안티패턴: 깊은 OFFSET
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 100000;

-- 해결: 커서 기반 (Keyset)
SELECT * FROM products WHERE id > 100000 ORDER BY id LIMIT 20;
```

### 7. 대량 IN 절
```sql
-- 안티패턴: 수천 개 ID
WHERE id IN (1, 2, 3, ..., 10000)

-- 해결: 임시 테이블 또는 JOIN
-- PostgreSQL: VALUES 또는 ANY(ARRAY[...])
-- 범용: 배치 처리 (500개씩)
```

## EXPLAIN 분석 가이드 (PostgreSQL)

### 실행 계획 읽기
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 123 AND status = 'completed';
```

### 주요 노드 유형

| 노드 | 의미 | 성능 |
|------|------|------|
| Seq Scan | 전체 테이블 스캔 | 느림 (대량 데이터) |
| Index Scan | 인덱스 + 테이블 접근 | 보통 |
| Index Only Scan | 인덱스만으로 응답 | 빠름 |
| Bitmap Index Scan | 비트맵으로 인덱스 스캔 | 보통 |
| Nested Loop | 중첩 루프 조인 | 소량 데이터에 적합 |
| Hash Join | 해시 테이블 조인 | 대량 동등 조인 |
| Merge Join | 정렬 병합 조인 | 대량 정렬 데이터 |
| Sort | 정렬 연산 | 메모리/디스크 주의 |

### 경고 신호
- `Seq Scan` on 대형 테이블 → 인덱스 필요
- `Sort` with `external merge Disk` → work_mem 부족
- `actual rows` >> `estimated rows` → 통계 오래됨 (ANALYZE 필요)
- `Nested Loop` with 대형 테이블 → Hash Join 유도

## 파티셔닝 전략

### 파티셔닝 필요 신호
- 테이블 크기 > 수억 행
- 시계열 데이터 (로그, 이벤트, 메트릭)
- 오래된 데이터 주기적 삭제/아카이빙
- 특정 기간 쿼리가 대부분

### 파티셔닝 유형

| 유형 | 분할 기준 | 적합 | 예시 |
|------|----------|------|------|
| **Range** | 값 범위 | 시계열 | 월별/연별 파티션 |
| **List** | 값 목록 | 카테고리 | 지역별, 상태별 |
| **Hash** | 해시값 | 균등 분산 | user_id % N |

### Range 파티셔닝 예시 (PostgreSQL)
```sql
CREATE TABLE events (
  id BIGINT,
  event_time TIMESTAMPTZ,
  data JSONB
) PARTITION BY RANGE (event_time);

CREATE TABLE events_2025_q1 PARTITION OF events
  FOR VALUES FROM ('2025-01-01') TO ('2025-04-01');
```

## 캐싱 전략

| 레벨 | 도구 | 적합 데이터 | TTL |
|------|------|-----------|-----|
| **쿼리 캐시** | Redis/Memcached | 자주 읽히는 조회 결과 | 30초~5분 |
| **ORM 캐시** | Prisma/TypeORM 캐시 | 엔티티 단위 | 1~5분 |
| **집계 캐시** | Materialized View | 통계/대시보드 | 1시간+ |
| **CDN 캐시** | CloudFront/CloudFlare | 정적 API 응답 | 5~60분 |

### 캐시 무효화 전략
- **TTL 기반**: 만료 시간 후 자동 갱신
- **이벤트 기반**: 데이터 변경 시 즉시 삭제
- **Write-Through**: 쓰기 시 캐시도 함께 갱신
- **Cache-Aside**: 읽기 시 캐시 없으면 DB 조회 후 캐시 저장
