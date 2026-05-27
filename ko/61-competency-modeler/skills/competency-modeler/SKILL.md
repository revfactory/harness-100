---
name: competency-modeler
description: "역량 모델링 종합 파이프라인. 직무분석→역량사전작성→평가루브릭설계→개발계획수립→역량매트릭스를 에이전트 팀이 협업하여 수행한다. '역량 모델 만들어줘', '직무 분석', '역량 사전', '평가 루브릭', '역량 개발 계획', '역량 매트릭스', 'competency model', 'KSA 분석', '직무기술서', '행동지표', '역량 평가' 등 역량 모델링 전반에 이 스킬을 사용한다. 기존 직무기술서나 역량 데이터가 있으면 해당 단계를 보강한다. 단, 실제 인사 시스템(SAP HR, Workday) 연동, 급여 체계 설계, 법률적 인사 자문은 이 스킬의 범위가 아니다."
---

# Competency Modeler — 역량 모델링 종합 파이프라인

직무분석→역량사전→평가루브릭→개발계획→역량매트릭스를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 4명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| job-analyst | `agents/job-analyst.md` | 직무 분석, KSA 도출 | general-purpose |
| competency-architect | `agents/competency-architect.md` | 역량 정의, 행동지표, 수준 체계 | general-purpose |
| rubric-designer | `agents/rubric-designer.md` | 평가 기준, 채점표, 평가 도구 | general-purpose |
| development-planner | `agents/development-planner.md` | 개발 계획, 학습 경로, 매트릭스 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 직무**: 역량 모델을 구축할 직무명
    - **조직 정보** (선택): 산업, 규모, 조직 문화
    - **목적** (선택): 채용/평가/개발/승진/조직 설계
    - **직급 범위** (선택): 특정 직급 또는 전 직급
    - **기존 자료** (선택): 기존 직무기술서, 역량 체계
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 해당 Phase를 조정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 직무 분석 | job-analyst | 없음 | `_workspace/01_job_analysis.md` |
| 2 | 역량사전 작성 | competency-architect | 작업 1 | `_workspace/02_competency_dictionary.md` |
| 3 | 평가 루브릭 설계 | rubric-designer | 작업 1, 2 | `_workspace/03_assessment_rubric.md` |
| 4a | 개발 계획 수립 | development-planner | 작업 1, 2, 3 | `_workspace/04_development_plan.md` |
| 4b | 역량 매트릭스 | development-planner | 작업 1, 2, 3 | `_workspace/05_competency_matrix.md` |

**팀원 간 소통 흐름:**
- job-analyst 완료 → competency-architect에게 KSA 매핑·과업 가중치 전달, rubric-designer에게 과업별 성과 기준 전달
- competency-architect 완료 → rubric-designer에게 역량 정의·행동지표·수준 체계 전달, development-planner에게 역량 목록·수준 체계 전달
- rubric-designer 완료 → development-planner에게 평가 결과 해석 가이드·갭 분석 프레임 전달
- development-planner는 모든 정보를 종합하여 개발 계획과 매트릭스를 작성한다

### Phase 3: 통합 및 최종 보고

1. `_workspace/` 내 모든 파일을 확인한다
2. 직무 분석→역량 사전→루브릭→개발 계획의 일관성을 검증한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "역량 모델 전체", "풀 모델링" | **풀 파이프라인** | 4명 전원 |
| "직무 분석만", "JD 작성해줘" | **직무분석 모드** | job-analyst 단독 |
| "역량 사전 만들어줘" | **역량사전 모드** | job-analyst + competency-architect |
| "평가 루브릭 설계해줘" | **루브릭 모드** | rubric-designer 단독 (기존 역량 사전 활용) |
| "역량 개발 계획 세워줘" | **개발계획 모드** | development-planner 단독 (기존 역량 데이터 활용) |
| "역량 매트릭스 만들어줘" | **매트릭스 모드** | development-planner 단독 |

**기존 데이터 활용**: 사용자가 기존 직무기술서, 역량 체계 등을 제공하면 해당 단계를 건너뛰거나 보강한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 직무 정보 부족 | 웹 검색으로 유사 직무 JD 수집, 사용자에게 추가 정보 요청 |
| 산업 특수성 높음 | NCS/O*NET 표준 참조, 산업 전문 용어 사전 활용 |
| 조직 정보 미제공 | 일반적인 중견기업 기준으로 작업, 커스터마이징 가이드 제공 |
| 복수 직무 요청 | 핵심 직무 1개 우선 처리, 나머지는 매트릭스에서 프레임 제공 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "IT기업 백엔드 개발자 직무의 역량 모델을 만들어줘. 주니어~시니어까지 포함해줘."
**기대 결과**:
- 직무 분석: 백엔드 개발자의 과업 분석, KSA 도출, NCS 매핑
- 역량 사전: 10~12개 역량(기술역량+공통역량), 5단계 수준별 행동지표
- 평가 루브릭: BARS 기반 채점표, BEI 질문, SJT 문항
- 개발 계획: 주니어→시니어 성장 경로, 70:20:10 개발 활동
- 역량 매트릭스: 직급별 요구 수준 매핑

### 부분 요청 흐름
**프롬프트**: "우리 회사 영업직 직무기술서 작성해줘, 중견 제조업이야"
**기대 결과**:
- 직무분석 모드 (job-analyst 단독)
- 제조업 영업직 직무기술서 + KSA 도출

### 기존 데이터 활용 흐름
**프롬프트**: "이 역량 사전에 맞는 평가 루브릭 만들어줘" + 기존 역량 사전 파일
**기대 결과**:
- 루브릭 모드 (rubric-designer 단독)
- 기존 역량 사전 기반 BARS 채점표 + 평가 도구

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| rubric-designer | `bars-assessment` | BARS 5단계 설계, BEI 질문(STAR-L), SJT 문항, 평가 방법 비교 |
| job-analyst, competency-architect | `ksa-taxonomy` | KSA-O 프레임워크, NCS/O*NET 매핑, 역량 수준 5단계, 직무기술서 표준 |
