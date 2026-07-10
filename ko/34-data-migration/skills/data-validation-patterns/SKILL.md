---
name: data-validation-patterns
description: "마이그레이션 데이터 검증 패턴: 행 수 비교, 체크섬, 샘플링 검증, FK 무결성, 비즈니스 규칙 검증 쿼리 설계 가이드. '데이터 검증', '마이그레이션 검증', '체크섬', '행 수 비교', '무결성 검증', '회귀 테스트', 'Go/No-Go 체크리스트' 등 마이그레이션 데이터 정합성 검증 시 이 스킬을 사용한다. validation-engineer의 검증 설계 역량을 강화한다. 단, 스키마 매핑이나 롤백 계획은 이 스킬의 범위가 아니다."
---

# Data Validation Patterns — 마이그레이션 검증 패턴 가이드

마이그레이션 전후 데이터 정합성을 검증하는 체계적 패턴과 쿼리 모음.

## 검증 계층 모델

```
Level 5: 비즈니스 규칙 검증  ← 도메인 특화 규칙
Level 4: 교차 참조 검증      ← 테이블 간 관계
Level 3: 데이터 값 검증      ← 변환 정확성
Level 2: 스키마 검증         ← 구조 일치
Level 1: 건수 검증           ← 행/열 수 일치
```

## Level 1: 건수 검증

```sql
-- 소스
SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM source.orders
UNION ALL
SELECT 'customers', COUNT(*) FROM source.customers
UNION ALL
SELECT 'products', COUNT(*) FROM source.products;

-- 타깃 (동일 쿼리)
SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM target.orders
UNION ALL ...;

-- 차이 비교
SELECT s.table_name,
       s.row_count AS source_count,
       t.row_count AS target_count,
       s.row_count - t.row_count AS diff,
       CASE WHEN s.row_count = t.row_count THEN 'PASS' ELSE 'FAIL' END AS status
FROM source_counts s JOIN target_counts t ON s.table_name = t.table_name;
```

## Level 2: 스키마 검증

```sql
-- 컬럼 수 비교
SELECT s.table_name,
       s.col_count AS source_cols,
       t.col_count AS target_cols,
       CASE WHEN s.col_count = t.col_count THEN 'PASS' ELSE 'CHECK' END
FROM (SELECT table_name, COUNT(*) col_count
      FROM source_information_schema.columns GROUP BY table_name) s
JOIN (SELECT table_name, COUNT(*) col_count
      FROM target_information_schema.columns GROUP BY table_name) t
ON s.table_name = t.table_name;

-- NULL 제약 비교
-- PK/FK 제약 비교
-- 인덱스 비교
```

## Level 3: 데이터 값 검증

### 체크섬 비교

```sql
-- 행 단위 체크섬 (PostgreSQL)
SELECT id, md5(ROW(order_id, customer_id, total_amount, created_at)::text) AS row_hash
FROM orders;

-- 테이블 전체 체크섬
SELECT md5(string_agg(row_hash, '' ORDER BY id)) AS table_hash
FROM (
    SELECT id, md5(ROW(*)::text) AS row_hash FROM orders
) t;

-- MySQL 체크섬
CHECKSUM TABLE orders;
```

### 샘플링 검증

```python
def sample_validation(source_conn, target_conn, table, pk_col, sample_size=1000):
    """무작위 샘플 N건을 행 단위로 비교"""
    # 1. PK 무작위 추출
    pks = source_conn.execute(
        f"SELECT {pk_col} FROM {table} ORDER BY RANDOM() LIMIT {sample_size}"
    ).fetchall()

    mismatches = []
    for pk in pks:
        source_row = source_conn.execute(
            f"SELECT * FROM {table} WHERE {pk_col} = %s", (pk,)
        ).fetchone()
        target_row = target_conn.execute(
            f"SELECT * FROM {table} WHERE {pk_col} = %s", (pk,)
        ).fetchone()

        if not rows_equal(source_row, target_row):
            mismatches.append({
                'pk': pk, 'source': source_row, 'target': target_row,
                'diff_columns': find_diff_columns(source_row, target_row)
            })

    return {
        'table': table,
        'sample_size': sample_size,
        'mismatches': len(mismatches),
        'match_rate': (sample_size - len(mismatches)) / sample_size,
        'details': mismatches[:10]  # 상위 10건만
    }
```

### 집계 비교

```sql
-- 수치 컬럼 집계 비교
SELECT
    COUNT(*) AS cnt,
    SUM(total_amount) AS sum_amount,
    AVG(total_amount) AS avg_amount,
    MIN(total_amount) AS min_amount,
    MAX(total_amount) AS max_amount,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM orders
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

## Level 4: 교차 참조 검증

```sql
-- FK 무결성: orders.customer_id가 customers.id에 존재하는가?
SELECT o.order_id, o.customer_id
FROM target.orders o
LEFT JOIN target.customers c ON o.customer_id = c.id
WHERE c.id IS NULL;
-- 결과가 0행이어야 통과

-- 역방향: 주문이 있는 고객이 모두 존재하는가?
SELECT DISTINCT o.customer_id
FROM source.orders o
WHERE o.customer_id NOT IN (SELECT id FROM target.customers);
```

## Level 5: 비즈니스 규칙 검증

```sql
-- 규칙 1: 주문 총액 = 주문항목 합계
SELECT o.order_id, o.total_amount, SUM(oi.price * oi.quantity) AS calc_total,
       ABS(o.total_amount - SUM(oi.price * oi.quantity)) AS diff
FROM target.orders o
JOIN target.order_items oi ON o.id = oi.order_id
GROUP BY o.order_id, o.total_amount
HAVING ABS(o.total_amount - SUM(oi.price * oi.quantity)) > 0.01;

-- 규칙 2: 상태 전이 유효성
SELECT * FROM target.orders
WHERE status = 'SHIPPED' AND paid_at IS NULL;
-- 결제 없이 배송은 불가 → 0행이어야 함

-- 규칙 3: 날짜 순서
SELECT * FROM target.orders
WHERE created_at > paid_at OR paid_at > shipped_at;
-- 생성 > 결제 > 배송 순서 위반 → 0행이어야 함
```

## Go/No-Go 체크리스트

```markdown
## 마이그레이션 Go/No-Go 판정

### 필수 통과 (전부 PASS여야 Go)
- [ ] L1: 전체 테이블 행 수 100% 일치
- [ ] L2: 스키마 구조 일치 (컬럼 수, 타입, 제약)
- [ ] L3: 체크섬 100% 일치 (또는 샘플 99.99%)
- [ ] L4: FK 무결성 위반 0건
- [ ] L5: 핵심 비즈니스 규칙 위반 0건

### 경고 허용 (문서화 후 Go 가능)
- [ ] 날짜/시간 밀리초 차이 (타임존 변환 시)
- [ ] 문자열 트레일링 공백 차이
- [ ] 소수점 끝자리 반올림 차이

### 자동 판정
전체 PASS → ✅ Go
필수 1건 이상 FAIL → ❌ No-Go
경고만 있음 → ⚠️ 조건부 Go (승인 필요)
```

## 검증 자동화 프레임워크

```python
class MigrationValidator:
    def __init__(self, source, target, tables):
        self.source = source
        self.target = target
        self.tables = tables
        self.results = []

    def run_all(self):
        for table in self.tables:
            self.results.append({
                'table': table,
                'row_count': self.check_row_count(table),
                'checksum': self.check_checksum(table),
                'fk_integrity': self.check_fk(table),
                'business_rules': self.check_rules(table),
            })
        return self.generate_report()

    def verdict(self):
        failed = [r for r in self.results if not r['all_pass']]
        return "GO" if not failed else "NO-GO"
```
