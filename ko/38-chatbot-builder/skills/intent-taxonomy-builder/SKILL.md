---
name: intent-taxonomy-builder
description: "챗봇의 의도(Intent) 분류 체계를 체계적으로 설계하는 방법론. '의도 분류 설계', 'intent 체계', 'NLU 의도 목록', '엔티티 사전', '슬롯 설계' 등 챗봇 의도 분류 체계 설계 시 사용한다. 단, 실제 NLU 모델 학습, 클라우드 NLU 서비스 배포는 이 스킬의 범위가 아니다."
---

# Intent Taxonomy Builder — 의도 분류 체계 설계 방법론

nlu-developer와 conversation-designer의 의도 분류 설계를 강화하는 스킬.

## 대상 에이전트

- **nlu-developer** — 의도/엔티티/슬롯 체계를 설계할 때 사용
- **conversation-designer** — 대화 시나리오와 의도를 매핑할 때 사용

## 의도 분류 체계 설계 프레임워크

### 1단계: 도메인 의도 수집

```
사용자 발화 수집 → 그룹핑 → 의도 후보 도출

수집 소스:
- 기존 FAQ 문서
- CS 문의 로그
- 경쟁사 챗봇 분석
- 사용자 인터뷰/설문
- 도메인 전문가 브레인스토밍
```

### 2단계: 의도 계층 구조

```
Level 0 (도메인)
├── Level 1 (카테고리)
│   ├── Level 2 (세부 의도)
│   └── Level 2
└── Level 1
    └── Level 2

예시 (이커머스):
commerce
├── order (주문)
│   ├── order.place — "주문하고 싶어요"
│   ├── order.status — "주문 상태 확인"
│   ├── order.cancel — "주문 취소해줘"
│   └── order.modify — "주문 변경하고 싶어요"
├── product (상품)
│   ├── product.search — "이런 상품 있어요?"
│   ├── product.detail — "이 상품 상세 정보"
│   └── product.compare — "두 상품 비교해줘"
├── payment (결제)
│   ├── payment.method — "결제 방법 알려줘"
│   ├── payment.refund — "환불 요청"
│   └── payment.receipt — "영수증 발급"
└── general (일반)
    ├── general.greeting — "안녕하세요"
    ├── general.goodbye — "감사합니다"
    └── general.fallback — (미인식)
```

### 3단계: 의도 품질 체크리스트

| 기준 | 설명 | 통과 조건 |
|------|------|----------|
| 상호배타성 | 의도 간 중복 없음 | 발화 1개 = 의도 1개 |
| 완전성 | 모든 사용자 시나리오 커버 | fallback < 10% |
| 균형성 | 의도당 학습 데이터 균등 | 최소 20개 발화/의도 |
| 명확성 | 이름만으로 목적 파악 | `verb.noun` 형식 |
| 적정 개수 | 관리 가능 범위 | 20~50개 (소규모), 50~150개 (대규모) |

## 엔티티 설계 방법론

### 엔티티 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| 시스템 엔티티 | 플랫폼 내장 | @sys.date, @sys.number, @sys.email |
| 사전 엔티티 | 도메인 고정 목록 | 메뉴명, 사이즈, 색상 |
| 패턴 엔티티 | 정규식 기반 | 주문번호(`ORD-\d{8}`), 전화번호 |
| 복합 엔티티 | 엔티티 조합 | 주소(시+구+동), 날짜범위 |

### 엔티티-슬롯 매핑

```
의도: order.place
필수 슬롯:
  - product_name (@product) — "아메리카노"
  - quantity (@sys.number) — "두 잔"
선택 슬롯:
  - size (@size) — "톨 사이즈"
  - option (@option) — "얼음 적게"
  - takeout (@boolean) — "포장이요"

슬롯 미충족 시 → 프롬프트:
  - product_name 누락: "어떤 메뉴를 주문하시겠어요?"
  - quantity 누락: "몇 개 주문하시겠어요?"
```

## 학습 데이터 생성 가이드

### 발화 변형 패턴

```
원본: "주문 취소하고 싶어요"

변형 전략:
1. 어미 변형: "취소해주세요", "취소할래요", "취소 부탁드립니다"
2. 표현 대체: "주문 철회", "주문 취소", "주문 안 할래요"
3. 문맥 추가: "방금 주문한 거 취소", "아까 시킨 것 취소"
4. 오타/축약: "주문취소", "취소여", "캔슬"
5. 간접 표현: "주문한 거 안 받고 싶어요", "그냥 안 살래요"
6. 엔티티 포함: "ORD-12345678 취소해줘"
```

### 발화 수 가이드

| 의도 복잡도 | 최소 발화 수 | 권장 발화 수 |
|-----------|------------|------------|
| 단순 (인사/작별) | 10 | 20 |
| 보통 (조회/확인) | 20 | 50 |
| 복잡 (주문/변경) | 30 | 80 |
| 혼동 가능 (유사 의도) | 50 | 100+ |

## 의도 혼동 매트릭스 분석

```
높은 혼동 쌍 예시:
- order.cancel ↔ payment.refund (취소 vs 환불)
- product.search ↔ product.detail (검색 vs 상세)
- order.modify ↔ order.cancel (변경 vs 취소)

해결 전략:
1. 차별화 발화 추가 (각 의도의 고유 키워드 강화)
2. 의도 합병 (구분 불필요시)
3. 컨텍스트 의존 분리 (대화 상태 기반)
4. 확인 질문 ("취소를 원하시나요, 환불을 원하시나요?")
```

## 산출물 템플릿

```yaml
intent_taxonomy:
  - intent: order.place
    description: "새 주문 접수"
    examples:
      - "아메리카노 두 잔 주문할게요"
      - "이거 주문하고 싶어요"
    required_slots:
      - name: product_name
        entity: "@product"
        prompt: "어떤 메뉴를 주문하시겠어요?"
    optional_slots:
      - name: quantity
        entity: "@sys.number"
        default: 1
    responses:
      success: "{product_name} {quantity}개 주문 접수되었습니다."
      slot_missing: "주문할 메뉴를 말씀해 주세요."
```
