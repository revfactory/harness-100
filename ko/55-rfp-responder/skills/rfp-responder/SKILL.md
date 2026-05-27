---
name: rfp-responder
description: "RFI/RFP 응답서 작성 풀 파이프라인. 요구사항 분석→역량 매칭→기술 제안→가격 제안→차별화 전략을 에이전트 팀이 협업하여 생성한다. 'RFP 응답', '제안서 작성', 'RFP 분석', '입찰 제안', '기술 제안서', '가격 제안', '공공 입찰', '제안요청서 응답', 'SI 제안서', 'IT 프로젝트 입찰' 등 RFP/RFI 응답 전반에 이 스킬을 사용한다. 기존 제안서 검토도 지원한다. 단, 나라장터/조달청 시스템 직접 접속, 실시간 입찰가 조회, 전자 입찰 참여는 이 스킬의 범위가 아니다."
---

# RFP Responder — RFI/RFP 응답서 작성 풀 파이프라인

요구사항 분석→역량 매칭→기술 제안→가격 제안→차별화 전략을 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| requirement-analyst | `agents/requirement-analyst.md` | RFP 해부, 요구사항 분류, 평가 기준 분석 | general-purpose |
| capability-matcher | `agents/capability-matcher.md` | 실적 매칭, 인력 구성, 기술 역량 매핑 | general-purpose |
| technical-proposer | `agents/technical-proposer.md` | 방법론, 아키텍처, 일정, 품질 관리 | general-purpose |
| pricing-strategist | `agents/pricing-strategist.md` | 원가 산정, 가격 전략, 경쟁 포지셔닝 | general-purpose |
| proposal-reviewer | `agents/proposal-reviewer.md` | 정합성, 차별화, 완성도 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **RFP 문서**: 제안요청서 파일 또는 핵심 내용
    - **자사 정보**: 회사 개요, 핵심 역량, 수행 실적
    - **투입 가능 자원**: 인력, 기술, 파트너
    - **경쟁 정보** (선택): 예상 경쟁사, 강약점
    - **기존 파일** (선택): 이전 제안서, 회사 소개서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 요구사항 분석 | requirement-analyst | 없음 | `_workspace/01_requirement_analysis.md` |
| 2 | 역량 매칭 | capability-matcher | 작업 1 | `_workspace/02_capability_matrix.md` |
| 3a | 기술 제안서 | technical-proposer | 작업 1, 2 | `_workspace/03_technical_proposal.md` |
| 3b | 가격 제안서 | pricing-strategist | 작업 1, 2 | `_workspace/04_pricing_proposal.md` |
| 4 | 통합 리뷰 | proposal-reviewer | 작업 1~3 | `_workspace/05_differentiation_strategy.md`, `_workspace/06_review_report.md` |

작업 3a(기술 제안)와 3b(가격 제안)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- requirement-analyst 완료 → capability-matcher에게 요구사항·평가기준 전달
- capability-matcher 완료 → technical-proposer에게 실적·인력·차별화 전달, pricing-strategist에게 인력 구성·비용 전달
- technical-proposer → pricing-strategist에게 추진 일정·공수 전달 (상호 참조)
- proposal-reviewer는 모든 산출물을 교차 검증. 🔴 발견 시 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "RFP 응답서 풀로 작성해줘" | **풀 파이프라인** | 5명 전원 |
| "이 RFP 분석만 해줘" | **분석 모드** | requirement-analyst 단독 |
| "기술 제안서만 써줘" | **기술 제안 모드** | requirement-analyst + technical-proposer + reviewer |
| "가격만 산정해줘" | **가격 모드** | pricing-strategist + reviewer |
| "이 제안서 검토해줘" | **리뷰 모드** | proposal-reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| RFP 문서 미제공 | 사업명으로 나라장터 웹 검색, 실패 시 사용자에게 요청 |
| 자사 정보 부족 | 최소한의 정보로 골격 작성, [확인 필요] 표시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 요구사항 누락 발견 | 기술 제안 작성자에게 즉시 보완 요청 |
| 정합성 불일치 | 관련 에이전트에 통일 기준값 제시 후 수정 요청 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 RFP에 대한 제안서를 작성해줘. 우리 회사는 클라우드 MSP 중견기업이고, 공공 SI 실적 20건 이상이야." + RFP 파일 첨부
**기대 결과**:
- 요구사항 분석: 전체 요구사항 매트릭스, 평가 기준 해부, Win 전략
- 역량 매칭: 실적 매핑 + 투입 인력 구성 + 차별화 3개
- 기술 제안서: 방법론, 아키텍처, WBS, 품질관리, RTM
- 가격 제안서: 비목별 원가 + 가격 시뮬레이션 3개 시나리오
- 차별화 전략서 + 리뷰 보고서

### 기존 파일 활용 흐름
**프롬프트**: "이 RFP의 가격만 산정해줘. 투입 인력은 여기 있어." + 인력 구성표 첨부
**기대 결과**:
- 가격 모드: pricing-strategist + reviewer 투입
- 인력 구성표를 기반으로 인건비 산출
- 가격 평가 방식에 따른 최적 투찰가 제안

### 에러 흐름
**프롬프트**: "SI 프로젝트 제안서 써줘, RFP는 아직 없어"
**기대 결과**:
- RFP 미제공 알림 + 일반적 SI 제안서 골격 작성
- 사업 유형별 표준 구성 제안
- RFP 입수 후 재실행 안내

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| capability-matcher, proposal-reviewer | `win-theme-builder` | Win Theme 도출, Ghost Team 분석, 제안서 관통 전략 |
| pricing-strategist | `pricing-calculator` | SW 사업 원가 산정, FP/MM 추정, 투찰 전략 시뮬레이션 |
