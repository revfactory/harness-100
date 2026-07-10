---
name: pricing-strategy
description: "제품/서비스의 가격 전략을 원가 분석, 경쟁 가격, 가치 기반 가격, 시뮬레이션으로 체계화하는 풀 파이프라인. '가격 전략 세워줘', '가격 책정해줘', '프라이싱 전략', '원가 분석', '경쟁 가격 조사', '가격 시뮬레이션', '가격 모델 설계', '요금제 만들어줘', 'SaaS 가격', '구독 모델 설계' 등 가격 전략 수립 전반에 이 스킬을 사용한다. 기존 원가 데이터나 가격 정보가 있는 경우에도 분석·최적화를 지원한다. 단, 회계 장부 작성, 세금 계산, 결제 시스템 개발, 실시간 동적 가격 엔진 구축은 이 스킬의 범위가 아니다."
---

# Pricing Strategy — 가격 전략 풀 파이프라인

제품/서비스의 원가→경쟁→가치→시뮬레이션을 에이전트 팀이 협업하여 최적 가격을 도출한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| cost-analyst | `agents/cost-analyst.md` | 원가 구조, BEP, 마진 | general-purpose |
| competitive-analyst | `agents/competitive-analyst.md` | 경쟁 가격, 포지셔닝 | general-purpose |
| value-assessor | `agents/value-assessor.md` | 가치 기반 가격, WTP, 세그먼트 | general-purpose |
| pricing-simulator | `agents/pricing-simulator.md` | 시나리오, 탄력성, P&L | general-purpose |
| pricing-reviewer | `agents/pricing-reviewer.md` | 교차 검증, 수치 정합성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **제품/서비스 정보**: 유형, 기능, 타깃 고객
    - **원가 데이터** (선택): 알고 있는 비용 항목
    - **경쟁 정보** (선택): 알고 있는 경쟁사, 가격
    - **목표**: 매출 목표, 시장 점유율 목표, 마진 목표
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 원가 분석 | cost-analyst | 없음 | `_workspace/01_cost_analysis.md` |
| 1b | 경쟁 가격 분석 | competitive-analyst | 없음 | `_workspace/02_competitive_pricing.md` |
| 2 | 가치 기반 가격 | value-assessor | 작업 1a, 1b | `_workspace/03_value_pricing.md` |
| 3 | 가격 시뮬레이션 | pricing-simulator | 작업 1a, 1b, 2 | `_workspace/04_pricing_simulation.md` |
| 4 | 가격 리뷰 | pricing-reviewer | 작업 1a,1b,2,3 | `_workspace/05_review_report.md` |

작업 1a(원가)와 1b(경쟁)는 **병렬 실행**한다. 둘 다 초기 의존 관계가 없으므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- cost-analyst 완료 → competitive-analyst에게 가격 하한선 전달, value-assessor에게 원가 구조 전달
- competitive-analyst 완료 → value-assessor에게 경쟁 가격 범위 전달
- value-assessor 완료 → pricing-simulator에게 WTP, 가격 모델 권고 전달
- pricing-simulator 완료 → pricing-reviewer에게 모든 문서 전달
- pricing-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "가격 전략 세워줘", "프라이싱 풀분석" | **풀 파이프라인** | 5명 전원 |
| "원가 분석만 해줘" | **원가 모드** | cost-analyst + reviewer |
| "경쟁 가격 조사해줘" | **경쟁 모드** | competitive-analyst + reviewer |
| "가격 시뮬레이션 돌려줘" (데이터 있음) | **시뮬레이션 모드** | pricing-simulator + reviewer |
| "이 가격 전략 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 원가 데이터 부족 | 산업 벤치마크 기반 추정, "추정치" 태그 명시 |
| 경쟁사 가격 비공개 | 업계 평균 범위로 추정, "비공개 가격" 태그 |
| 웹 검색 실패 | 일반 지식 기반 작업, "데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 수치 모순 발견 | 관련 에이전트 전원에게 수치 조정 협의 요청 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "B2B SaaS 프로젝트 관리 도구의 가격을 정해야 해. 서버 비용 월 200만원, 개발팀 인건비 월 3000만원이고, 경쟁사는 Asana, Monday.com이야. 1년 내 ARR 10억 목표"
**기대 결과**:
- 원가: SaaS 원가 구조 분석, 사용자당 단위 원가, BEP
- 경쟁: Asana/Monday 가격 체계 조사, 기능-가격 비교
- 가치: PM 도구의 가치 드라이버(시간 절약, 협업 효율), 세그먼트별 WTP
- 시뮬레이션: 3개 시나리오 P&L, ARR 10억 달성 경로
- 리뷰: 모든 수치 교차 검증

### 기존 파일 활용 흐름
**프롬프트**: "원가 분석은 했어. 경쟁 분석이랑 가격 결정만 해줘" + 원가 파일 첨부
**기대 결과**:
- 원가 파일을 `_workspace/01_cost_analysis.md`로 복사
- cost-analyst 건너뛰고 competitive-analyst + value-assessor + simulator + reviewer 투입

### 에러 흐름
**프롬프트**: "우리 앱 가격 정해줘"
**기대 결과**:
- 제품 정보 부족 → 제품 유형/타깃/기능 추가 질문
- 최소 정보만 제공 시 산업 평균 기반 가격 범위 제시
- "데이터 보완 시 정밀 분석 가능" 안내

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| psm-analyzer | `skills/psm-analyzer/SKILL.md` | value-assessor, pricing-simulator | Van Westendorp PSM 4대 질문, 교차점 도출, Gabor-Granger 보완, 세그먼트 분석 |
| price-elasticity-calculator | `skills/price-elasticity-calculator/SKILL.md` | pricing-simulator, competitive-analyst | PED/XED 공식, 최적 가격 도출, 시나리오 시뮬레이션, 가격 인상 전략 |
