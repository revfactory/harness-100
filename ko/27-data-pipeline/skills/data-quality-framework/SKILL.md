---
name: data-quality-framework
description: "데이터 품질 차원(정확성, 완전성, 적시성, 일관성 등)별 검증 규칙 설계와 Great Expectations, dbt tests 등의 도구 활용 가이드. '데이터 품질', '검증 규칙', 'Great Expectations', 'dbt test', '데이터 프로파일링', '이상 탐지', '데이터 계약' 등 데이터 품질 관리 시 이 스킬을 사용한다. data-quality-manager의 품질 검증 역량을 강화한다. 단, 파이프라인 스케줄링이나 전체 아키텍처 설계는 이 스킬의 범위가 아니다."
---

# Data Quality Framework — 데이터 품질 프레임워크 가이드

데이터 품질을 체계적으로 정의, 측정, 모니터링하는 프레임워크.

## 데이터 품질 6차원

| 차원 | 정의 | 측정 방법 | 임계값 예시 |
|------|------|----------|-----------|
| **정확성** (Accuracy) | 현실을 올바르게 반영 | 소스 대조, 비즈니스 규칙 검증 | 정확도 > 99.9% |
| **완전성** (Completeness) | 필수 데이터 존재 | NULL 비율, 필수 필드 충족 | NULL < 1% |
| **적시성** (Timeliness) | 기대 시간 내 도착 | 지연시간, 데이터 신선도 | 지연 < 30분 |
| **일관성** (Consistency) | 시스템 간 일치 | 교차 검증, 참조 무결성 | 불일치 = 0 |
| **유일성** (Uniqueness) | 중복 없음 | 중복 행/키 비율 | 중복 = 0% |
| **유효성** (Validity) | 포맷/범위 준수 | 정규식, 범위 체크 | 유효율 > 99% |

## 검증 규칙 설계 패턴

### P0 (필수 — 실패 시 파이프라인 중단)

```yaml
rules:
  - name: pk_uniqueness
    type: uniqueness
    column: order_id
    threshold: 0  # 중복 0건

  - name: not_null_critical
    type: completeness
    columns: [order_id, customer_id, total_amount]
    max_null_rate: 0

  - name: row_count_sanity
    type: volume
    min_rows: 1000  # 일일 최소 주문 수
    max_deviation: 0.5  # 전일 대비 50% 이상 변동 시 경고

  - name: referential_integrity
    type: consistency
    source: orders.customer_id
    reference: customers.id
    match_rate: 1.0
```

### P1 (중요 — 경고 후 진행)

```yaml
rules:
  - name: email_format
    type: validity
    column: email
    pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    threshold: 0.99

  - name: amount_range
    type: accuracy
    column: total_amount
    min: 0
    max: 100000000  # 1억 초과 주문은 의심

  - name: freshness
    type: timeliness
    column: created_at
    max_age_hours: 24
```

## Great Expectations 구현

```python
import great_expectations as gx

# 기대 정의
suite = context.add_expectation_suite("orders_quality")

# 완전성
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
)

# 유일성
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeUnique(column="order_id")
)

# 유효성
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="total_amount", min_value=0, max_value=100000000
    )
)

# 볼륨
suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(
        min_value=1000, max_value=1000000
    )
)
```

## dbt Tests 구현

```yaml
# schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('customers')
              field: id
      - name: total_amount
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 100000000
    tests:
      - dbt_utils.recency:
          datepart: hour
          field: created_at
          interval: 24
```

## 데이터 프로파일링 체크리스트

```
컬럼별 프로파일:
├── 타입: 실제 타입 vs 선언 타입
├── 기수성(Cardinality): 고유값 수
├── NULL 비율: 결측 패턴
├── 분포: 히스토그램, 왜도, 첨도
├── 이상치: IQR 기반 아웃라이어
├── 패턴: 날짜, 이메일, 전화번호 등 정규식 일치율
└── 의존성: 함수적 종속 관계

테이블별 프로파일:
├── 행 수: 기대 범위 vs 실제
├── 중복률: 전체 행 중 중복
├── 참조 무결성: FK 위반 건수
└── 시간 분포: 레코드 생성 시간 패턴
```

## 이상 탐지 기법

| 기법 | 적용 | 공식/방법 |
|------|------|----------|
| Z-Score | 정규분포 데이터 | \|x - μ\| / σ > 3 |
| IQR | 비정규분포 | x < Q1-1.5*IQR or x > Q3+1.5*IQR |
| 이동평균 | 시계열 볼륨 | 7일 이동평균 대비 2σ 이탈 |
| 전일 대비 | 일일 적재 | \|today - yesterday\| / yesterday > 0.5 |

## 데이터 계약 (Data Contract)

```yaml
# data-contract.yml
name: orders
version: "2.0.0"
owner: order-team
description: "주문 데이터 계약"

schema:
  - name: order_id
    type: string
    required: true
    unique: true
  - name: total_amount
    type: decimal(10,2)
    required: true
    min: 0

sla:
  freshness: 1h
  availability: 99.9%

quality:
  completeness: 99.9%
  accuracy: 99.99%
```
