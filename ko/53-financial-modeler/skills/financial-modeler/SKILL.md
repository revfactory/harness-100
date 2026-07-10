---
name: financial-modeler
description: "재무 모델링 풀 파이프라인. 수익 모델→비용 구조→시나리오 분석→밸류에이션을 에이전트 팀이 협업하여 생성한다. '재무 모델 만들어줘', '매출 예측', '비용 분석', '밸류에이션', '기업 가치 평가', 'DCF 분석', '투자 모델', '수익 모델링', '손익 분석', '재무 전망' 등 재무 모델링 전반에 이 스킬을 사용한다. 기존 재무 데이터가 있는 경우에도 부분 분석을 지원한다. 단, 실제 회계 시스템 연동, ERP 데이터 추출, 세무 신고서 작성, 실시간 주가 분석은 이 스킬의 범위가 아니다."
---

# Financial Modeler — 재무 모델링 풀 파이프라인

수익 모델→비용 구조→시나리오 분석→밸류에이션을 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| revenue-modeler | `agents/revenue-modeler.md` | 수익원 정의, 매출 예측, 단위 경제학 | general-purpose |
| cost-analyst | `agents/cost-analyst.md` | 비용 분류, 손익분기 분석, 마진 분석 | general-purpose |
| scenario-planner | `agents/scenario-planner.md` | Bear/Base/Bull 시나리오, 민감도 분석 | general-purpose |
| valuation-expert | `agents/valuation-expert.md` | DCF, 멀티플, 비교 기업, 투자 수익 분석 | general-purpose |
| model-reviewer | `agents/model-reviewer.md` | 수식 정합성, 가정 일관성, 통합 요약 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **사업 정보**: 업종, 사업 모델, 제품/서비스, 현재 단계(아이디어/MVP/PMF/스케일업)
    - **재무 데이터** (선택): 현재 매출, 비용, 투자 금액 등
    - **분석 목적**: 투자 유치, 내부 계획, M&A, 사업 타당성 검증 등
    - **기존 파일** (선택): 기존 재무 모델, 사업계획서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 수익 모델 | revenue-modeler | 없음 | `_workspace/01_revenue_model.md` |
| 1b | 비용 구조 | cost-analyst | 작업 1a | `_workspace/02_cost_structure.md` |
| 2 | 시나리오 분석 | scenario-planner | 작업 1a, 1b | `_workspace/03_scenario_analysis.md` |
| 3 | 밸류에이션 | valuation-expert | 작업 2 | `_workspace/04_valuation_report.md` |
| 4 | 통합 리뷰 | model-reviewer | 작업 1~3 | `_workspace/05_financial_summary.md`, `_workspace/06_review_report.md` |

**팀원 간 소통 흐름:**
- revenue-modeler 완료 → cost-analyst에게 수익원 구조·매출 규모 전달, scenario-planner에게 핵심 가정 전달
- cost-analyst 완료 → scenario-planner에게 고정비/변동비 구조 전달
- scenario-planner 완료 → valuation-expert에게 시나리오별 재무제표·확률 가중 예측 전달
- model-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "재무 모델 풀로 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "매출 예측만 해줘" | **수익 모드** | revenue-modeler + reviewer |
| "비용 분석해줘" | **비용 모드** | cost-analyst + reviewer |
| "밸류에이션만 해줘" (기존 재무 데이터 있음) | **밸류에이션 모드** | valuation-expert + reviewer |
| "이 재무 모델 검토해줘" | **리뷰 모드** | model-reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 시장 데이터 부족 | 유사 산업 벤치마크 적용, "추정치" 명시 |
| 사업 모델 불명확 | 3가지 수익 모델 유형 제안 후 사용자 선택 요청 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 수치 불일치 발견 | 원본 추적 후 올바른 수치로 수정, 수정 이력 문서화 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "B2B SaaS 스타트업 재무 모델 만들어줘. 월 구독료 5만원, 현재 고객 50개사, 연 30% 성장 목표. 시리즈 A 투자 유치용이야."
**기대 결과**:
- 수익 모델: SaaS 수익 구조 (MRR/ARR), 고객 코호트, 이탈률 반영, LTV/CAC
- 비용 구조: 클라우드 인프라, 개발팀 인건비, 영업비, BEP 분석
- 시나리오: Bear(15%)/Base(30%)/Bull(50%) 성장률 시나리오, 민감도 분석
- 밸류에이션: DCF + PSR 멀티플 + 비교 기업 3개 이상
- 통합 요약: 투자자 보고용 Executive Summary

### 기존 파일 활용 흐름
**프롬프트**: "이 매출 데이터로 밸류에이션만 해줘" + 재무 데이터 첨부
**기대 결과**:
- 기존 데이터를 `_workspace/`에 매핑
- valuation-expert + model-reviewer만 투입
- 데이터 부족 부분은 가정으로 보완

### 에러 흐름
**프롬프트**: "새로운 사업 아이디어인데 재무 모델 만들어줘. 아직 매출은 없어."
**기대 결과**:
- 사업 모델 유형 제안 후 확인
- 매출 추정은 Bottom-up 중심 (TAM/SAM/SOM + 고객 단위)
- Bear 시나리오에서 자금 소진 분석 강조
- 밸류에이션은 벤처 캐피탈 방법론 우선 적용

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| valuation-expert | `dcf-valuation` | WACC 산정, FCFF 추정, 터미널 밸류, 멀티플 교차검증 |
| scenario-planner | `sensitivity-analysis` | 토네이도 차트, 2-Way 테이블, Bear/Base/Bull 시나리오, 브레이크이븐 |
| revenue-modeler | `unit-economics` | LTV/CAC, 공헌이익 3-Layer, 코호트 분석, Bottom-up 매출 추정 |
