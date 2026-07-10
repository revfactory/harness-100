---
name: proposal-writer
description: "제안서를 에이전트 팀이 협업하여 고객분석→솔루션설계→가격→차별화→디자인까지 한 번에 생성하는 풀 파이프라인. '제안서 만들어줘', '제안서 작성', 'RFP 대응', '영업 제안서', '기술 제안서', '사업 제안서', '프로젝트 제안서', '입찰 제안서', '서비스 제안', '솔루션 제안' 등 제안서 작성 전반에 이 스킬을 사용한다. 기존 고객 분석이나 솔루션 설계가 있으면 가격·차별화·통합 작성을 지원한다. 단, 실제 입찰 시스템 등록, 전자계약, 물리적 제안서 인쇄/바인딩은 이 스킬의 범위가 아니다."
---

# Proposal Writer — 제안서 작성 풀 파이프라인

제안서의 고객분석→솔루션설계→가격→차별화→디자인을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| client-analyst | `agents/client-analyst.md` | 고객 니즈, 의사결정구조, 경쟁상황 | general-purpose |
| solution-architect | `agents/solution-architect.md` | 솔루션 구성, 구현 계획, WBS | general-purpose |
| pricing-strategist | `agents/pricing-strategist.md` | 원가, 가격 모델, ROI | general-purpose |
| differentiator | `agents/differentiator.md` | USP, 경쟁우위, Win Theme | general-purpose |
| proposal-designer | `agents/proposal-designer.md` | 통합 구성, 디자인, 교차 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **고객**: 고객사명, 산업, 규모
    - **제안 대상**: 제품/서비스/프로젝트
    - **RFP** (선택): RFP/RFI 문서
    - **경쟁 상황** (선택): 알려진 경쟁사
    - **기존 자료** (선택): 이전 제안서, 회사 소개서, 실적 자료
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 고객 분석 | analyst | 없음 | `_workspace/01_client_analysis.md` |
| 2a | 솔루션 설계 | architect | 작업 1 | `_workspace/02_solution_design.md` |
| 2b | 차별화 전략 | differentiator | 작업 1 | `_workspace/04_differentiation.md` |
| 3 | 가격 전략 | strategist | 작업 1, 2a | `_workspace/03_pricing_model.md` |
| 4 | 제안서 통합 및 검증 | designer | 작업 2a, 2b, 3 | `_workspace/05_final_proposal.md` |

작업 2a(솔루션)와 2b(차별화)는 **병렬 실행**한다. 둘 다 작업 1(고객분석)에만 의존한다.

**팀원 간 소통 흐름:**
- analyst 완료 → architect에게 요구사항+기술환경 전달, differentiator에게 경쟁분석+관심사 전달, strategist에게 예산+가격정보 전달
- architect 완료 → strategist에게 원가 요소 전달, differentiator에게 기술 차별점 전달
- differentiator 완료 → strategist에게 가치 메시지 전달
- strategist 완료 → designer에게 가격 전략서 전달
- designer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 고객 분석 — `01_client_analysis.md`
    - 솔루션 설계 — `02_solution_design.md`
    - 가격 전략 — `03_pricing_model.md`
    - 차별화 전략 — `04_differentiation.md`
    - 최종 제안서 — `05_final_proposal.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "제안서 만들어줘", "RFP 대응" | **풀 파이프라인** | 5명 전원 |
| "이 RFP에 맞는 솔루션 설계해줘" | **솔루션 모드** | analyst + architect + designer |
| "가격만 뽑아줘" (솔루션 제공) | **가격 모드** | strategist + designer |
| "이 제안서 차별화 포인트 보강해줘" | **차별화 모드** | differentiator + designer |
| "이 제안서 검토해줘" | **검토 모드** | designer 단독 |

**기존 파일 활용**: 사용자가 RFP, 기존 제안서, 회사 소개서를 제공하면 해당 내용을 반영한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 고객 정보 부족 | 산업/규모에서 프로파일 추론, 사용자에게 핵심 정보 질문 |
| RFP 없음 | 사용자 입력에서 요구사항 추출, 범용 제안서 구조 적용 |
| 자사 정보 없음 | 사용자에게 강점/실적 질문, 최소 정보로 차별화 구성 |
| 웹 검색 실패 | 사용자 제공 자료 기반 작업, "외부 데이터 미확보" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "A사에 ERP 시스템 도입 제안서를 만들어줘. 제조업 중견기업이고 매출 500억 규모야. 경쟁사는 SAP이랑 더존이야."
**기대 결과**:
- 고객 분석: A사 비즈니스 이해, Pain Point, 의사결정 구조, SAP/더존 경쟁 분석
- 솔루션: ERP 아키텍처, 모듈 구성, 구현 일정, WBS
- 가격: 원가 분석, 3가지 가격 옵션, ROI(투자 회수 기간)
- 차별화: Win Theme 3개, SAP/더존 대비 우위 매트릭스
- 제안서: 통합 제안서 + 디자인 가이드 + 정합성 매트릭스 확인

### RFP 기반 흐름
**프롬프트**: "이 RFP에 맞는 제안서 만들어줘" + RFP 파일 제공
**기대 결과**:
- RFP 요구사항 항목별 분해 → 대응표 작성
- 모든 요구사항에 대한 솔루션 매핑
- RFP 평가 기준에 맞춘 제안서 구조

### 에러 흐름
**프롬프트**: "제안서 하나 만들어줘"
**기대 결과**:
- 고객/제안 대상 불명확 → 사용자에게 확인 질문
- 답변 기반으로 작업 진행
- 검증 보고서에 "고객 정보 추정 기반 — 확인 후 수정 필요" 명시

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| roi-calculator | `skills/roi-calculator/SKILL.md` | pricing-strategist, solution-architect | ROI/TCO/NPV/IRR 산출, 시나리오 분석 |
| win-theme-builder | `skills/win-theme-builder/SKILL.md` | differentiator, client-analyst | Win Theme 구축, 경쟁 포지셔닝, Ghost 전략 |
