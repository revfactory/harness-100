---
name: normalization-patterns
description: "데이터베이스 정규화/비정규화 패턴 라이브러리. 1NF~BCNF 판별 기준, 함수 종속성 분석, 정규화 단계별 변환 절차, 전략적 비정규화 패턴, 공통 도메인 ERD 템플릿을 제공하는 data-modeler 확장 스킬. '정규화', '비정규화', 'ERD 패턴', '함수 종속성', '테이블 분리', '관계 설계' 등 데이터 모델링 시 사용한다. 단, DDL 생성이나 쿼리 최적화는 이 스킬의 범위가 아니다."
---

# Normalization Patterns — 정규화/비정규화 패턴 라이브러리

data-modeler 에이전트가 데이터 모델링 시 활용하는 정규화 규칙, 비정규화 전략, 도메인별 ERD 패턴.

## 대상 에이전트

`data-modeler` — 이 스킬의 정규화 규칙과 ERD 패턴을 데이터 모델 설계에 직접 적용한다.

## 정규화 단계 판별 & 변환

### 1NF (제1정규형)
**규칙**: 모든 컬럼은 원자값(atomic value)이어야 한다.

| 위반 패턴 | 문제 | 해결 |
|----------|------|------|
| 다중값 컬럼 | `tags = "java,python,go"` | 별도 테이블 분리 (M:N) |
| 반복 그룹 | `phone1, phone2, phone3` | 별도 테이블 분리 (1:N) |
| 복합값 | `address = "서울시 강남구 역삼동"` | 시/구/동 컬럼 분리 |

### 2NF (제2정규형)
**전제**: 1NF 만족
**규칙**: 부분 함수 종속성 제거 — 복합 기본키의 일부에만 종속되는 컬럼 분리.

| 위반 예 | 종속 관계 | 해결 |
|--------|----------|------|
| `주문상세(주문ID, 상품ID, 상품명, 수량)` | 상품명 → 상품ID에만 종속 | 상품 테이블 분리 |

### 3NF (제3정규형)
**전제**: 2NF 만족
**규칙**: 이행적 함수 종속성 제거 — 기본키가 아닌 컬럼이 다른 비키 컬럼을 결정하면 안 됨.

| 위반 예 | 종속 관계 | 해결 |
|--------|----------|------|
| `직원(ID, 부서ID, 부서명, 부서장)` | 부서명, 부서장 → 부서ID 종속 (이행적) | 부서 테이블 분리 |

### BCNF (보이스-코드 정규형)
**규칙**: 모든 결정자(determinant)가 후보키여야 한다.

| 위반 예 | 문제 | 해결 |
|--------|------|------|
| `수강(학생, 과목, 교수)` 여기서 교수→과목 | 교수가 결정자이지만 후보키 아님 | 교수-과목 테이블 분리 |

## 정규화 결정 흐름도

```
데이터 분석
  ├─ 원자값 위반? → 1NF 변환
  ├─ 복합키 & 부분 종속? → 2NF 변환
  ├─ 이행적 종속? → 3NF 변환
  ├─ 비후보키 결정자? → BCNF 변환
  └─ 성능 요구사항 → 전략적 비정규화 검토
```

## 전략적 비정규화 패턴

### 언제 비정규화하는가?
- 읽기 >> 쓰기 비율이 높을 때
- JOIN이 5개 이상 필요한 빈번한 쿼리
- 실시간 집계/통계가 필요할 때
- 대시보드/리포트 전용 데이터

### 비정규화 패턴 카탈로그

| 패턴 | 설명 | 적합 상황 | 트레이드오프 |
|------|------|----------|-----------|
| **파생 컬럼** | 계산값 저장 (`total_price`) | 빈번한 합계 조회 | 갱신 시 동기화 필요 |
| **중복 컬럼** | FK 대상의 자주 쓰는 컬럼 복사 | JOIN 회피 | 데이터 불일치 위험 |
| **사전 조인 테이블** | 조인 결과를 물리 테이블로 | 리포트/대시보드 | 저장 공간, 갱신 복잡 |
| **히스토리 스냅샷** | 시점 데이터 보존 (`order_address`) | 주문 시점 주소 보관 | 저장 공간 |
| **카운터 컬럼** | `likes_count`, `comments_count` | 실시간 카운트 표시 | 동시성 처리 |
| **JSON/JSONB** | 구조화되지 않은 확장 데이터 | 설정, 메타데이터 | 인덱싱 제한 |

## 공통 도메인 ERD 패턴

### 이커머스
```
users ──1:N──> orders ──1:N──> order_items
  │                                 │
  └──1:N──> addresses          products
  └──1:N──> reviews ──N:1──────┘
                               │
products ──N:M──> categories (via product_categories)
products ──1:N──> product_images
products ──1:N──> product_variants
```

핵심 테이블:
- `users` (id, email, name, password_hash, created_at)
- `products` (id, name, description, base_price, status)
- `orders` (id, user_id, status, total, shipping_address_snapshot)
- `order_items` (id, order_id, product_id, variant_id, quantity, unit_price)

### SaaS 멀티테넌트
```
tenants ──1:N──> users ──N:M──> roles (via user_roles)
   │                              │
   └──1:N──> subscriptions    permissions ──N:M──> roles
   └──1:N──> [도메인 테이블] (tenant_id FK)
```

핵심: 모든 비즈니스 테이블에 `tenant_id` 포함, RLS(Row Level Security) 적용

### 소셜 네트워크
```
users ──N:M──> users (via follows: follower_id, following_id)
  │
  └──1:N──> posts ──1:N──> comments
  │              └──N:M──> tags (via post_tags)
  │              └──1:N──> likes (user_id + post_id UNIQUE)
  └──1:N──> messages (sender_id, receiver_id)
```

### CMS/블로그
```
users ──1:N──> posts ──N:M──> tags (via post_tags)
                 │
                 └──1:N──> comments (self-referencing: parent_id)
                 └──1:N──> media
                 └──1:1──> post_meta (SEO, OG 등)
```

## 관계 패턴

### 1:1 관계
- 큰 테이블 분할 (자주 쓰는 컬럼 vs 가끔 쓰는 컬럼)
- 선택적 확장 (`user` + `user_profile`)
- 구현: FK + UNIQUE 제약

### 1:N 관계
- 가장 흔한 관계
- 자기참조: 카테고리 트리, 댓글 스레드 (`parent_id`)
- 구현: 자식 테이블에 FK

### M:N 관계
- 중간 테이블(junction table) 필수
- 중간 테이블에 추가 속성 가능 (`created_at`, `role`, `quantity`)
- 네이밍: `{table1}_{table2}` 또는 의미 있는 이름 (`enrollments`)

## 공통 컬럼 패턴

### 기본 타임스탬프
모든 테이블에 포함:
- `id` — UUID 또는 BIGINT AUTO_INCREMENT
- `created_at` — TIMESTAMPTZ DEFAULT NOW()
- `updated_at` — TIMESTAMPTZ, 트리거로 자동 갱신

### Soft Delete
- `deleted_at` — TIMESTAMPTZ NULL (NULL이면 미삭제)
- 모든 쿼리에 `WHERE deleted_at IS NULL` 조건
- 복원 가능, 감사 로그 역할

### 상태 관리
- `status` — ENUM 또는 VARCHAR
- 상태 전이 규칙 문서화 필수 (어떤 상태에서 어떤 상태로?)
- 이력이 필요하면 별도 `status_history` 테이블

### 다국어
- 전략 1: 컬럼 확장 (`name_ko`, `name_en`, `name_ja`)
- 전략 2: 번역 테이블 (`product_translations`: product_id, locale, name, description)
- 전략 2 권장 (언어 추가 시 스키마 변경 불필요)
