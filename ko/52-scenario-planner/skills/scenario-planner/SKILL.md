---
name: scenario-planner
description: "시나리오 기획 풀 파이프라인. 핵심 변수 정의→시나리오 매트릭스 구성→영향 분석→대응 전략→의사결정 문서를 에이전트 팀이 협업하여 생성한다. '시나리오 분석', '미래 시나리오', '시나리오 플래닝', '전략 시나리오', '불확실성 분석', '시나리오 기획해줘', '시나리오 매트릭스', '대응 전략 수립', '의사결정 지원' 등 시나리오 기반 전략 기획 전반에 이 스킬을 사용한다. 기존 분석 자료가 있는 경우에도 부분 파이프라인을 지원한다. 단, 실시간 데이터 수집 시스템 구축, 전사적 리스크 관리(ERM) 소프트웨어 연동, 몬테카를로 시뮬레이션 코드 실행은 이 스킬의 범위가 아니다."
---

# Scenario Planner — 시나리오 기획 풀 파이프라인

핵심 변수 정의→시나리오 매트릭스→영향 분석→대응 전략→의사결정 문서를 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| variable-analyst | `agents/variable-analyst.md` | 핵심 변수 식별, STEEP 분석, 시나리오 축 결정 | general-purpose |
| scenario-designer | `agents/scenario-designer.md` | 2x2 매트릭스, 시나리오 서사, 조기 경보 신호 | general-purpose |
| impact-assessor | `agents/impact-assessor.md` | 시나리오별 영향 분석, 리스크-기회 매핑 | general-purpose |
| strategy-architect | `agents/strategy-architect.md` | 로버스트/헤지/옵션 전략, 의사결정 트리거 | general-purpose |
| integration-reviewer | `agents/integration-reviewer.md` | 교차 검증, 정합성 확인, 통합 문서 편집 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **의사결정 주제**: 시나리오 분석의 대상이 되는 전략적 질문
    - **시간 지평**: 분석 대상 기간 (미지정 시 3~5년 기본)
    - **분석 범위**: 산업, 지역, 조직 범위
    - **기존 자료** (선택): 사용자가 제공한 분석 보고서, 데이터 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 핵심 변수 분석 | variable-analyst | 없음 | `_workspace/01_variable_analysis.md` |
| 2 | 시나리오 매트릭스 | scenario-designer | 작업 1 | `_workspace/02_scenario_matrix.md` |
| 3 | 영향 분석 | impact-assessor | 작업 1, 2 | `_workspace/03_impact_assessment.md` |
| 4 | 대응 전략 수립 | strategy-architect | 작업 2, 3 | `_workspace/04_response_strategy.md` |
| 5 | 통합 리뷰 + 의사결정 문서 | integration-reviewer | 작업 1~4 | `_workspace/05_decision_document.md`, `_workspace/06_review_report.md` |

**팀원 간 소통 흐름:**
- variable-analyst 완료 → scenario-designer에게 시나리오 축·극단값·확정 트렌드 전달
- scenario-designer 완료 → impact-assessor에게 4개 시나리오 서사·지표·조기 경보 신호 전달
- impact-assessor 완료 → strategy-architect에게 공통 영향·핵심 리스크/기회·취약 영역 전달
- integration-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 핵심 변수 분석서 — `01_variable_analysis.md`
    - 시나리오 매트릭스 — `02_scenario_matrix.md`
    - 영향 분석 보고서 — `03_impact_assessment.md`
    - 대응 전략서 — `04_response_strategy.md`
    - 통합 의사결정 문서 — `05_decision_document.md`
    - 리뷰 보고서 — `06_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "시나리오 분석 풀로 해줘", "시나리오 기획" | **풀 파이프라인** | 5명 전원 |
| "핵심 변수만 분석해줘" | **변수 분석 모드** | variable-analyst + reviewer |
| "이 변수로 시나리오 매트릭스 만들어줘" | **매트릭스 모드** | scenario-designer + reviewer |
| "이 시나리오들의 영향 분석해줘" | **영향 분석 모드** | impact-assessor + strategy-architect + reviewer |
| "대응 전략만 수립해줘" | **전략 모드** | strategy-architect + reviewer |

**기존 파일 활용**: 사용자가 기존 분석 자료를 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물명}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 변수분석가가 일반 지식 기반으로 작업, 보고서에 "데이터 제한" 명시 |
| 사용자 정보 부족 | 산업/주제 기반 일반 STEEP 분석 수행, 추가 정보 요청 사항 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 시나리오 간 논리 모순 | scenario-designer에게 전제 조정 요청, 조정 사유 문서화 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "2025~2030년 한국 전기차 배터리 산업의 시나리오를 기획해줘. 우리 회사는 2차전지 소재 중견기업이야."
**기대 결과**:
- 변수 분석: STEEP 기반 20개+ 변수, 불확실성-영향력 매트릭스, 핵심 축 2개 선정
- 시나리오 매트릭스: 2x2 매트릭스, 4개 시나리오 서사 (타임라인 포함), 조기 경보 신호
- 영향 분석: 6개 차원 히트맵, 리스크/기회 매핑, 크로스 시나리오 비교
- 대응 전략: 로버스트/헤지/옵션 전략, 의사결정 트리거 맵, 실행 로드맵
- 통합 문서: Executive Summary + 경영진 보고용 요약

### 기존 파일 활용 흐름
**프롬프트**: "이 산업 분석 보고서를 기반으로 시나리오 매트릭스와 대응 전략만 만들어줘" + 분석 파일 첨부
**기대 결과**:
- 기존 분석을 `_workspace/01_variable_analysis.md`로 매핑
- variable-analyst 건너뛰고 scenario-designer부터 실행
- 필요 시 기존 분석에서 핵심 축을 추출

### 에러 흐름
**프롬프트**: "AI 산업 시나리오 분석해줘"
**기대 결과**:
- 범위가 넓으므로 변수분석가가 범위 좁히기 제안 (예: "생성형 AI의 기업 채택" 등)
- 시간 지평 미지정 → 3~5년 기본 적용
- 웹 검색으로 최신 트렌드 반영 시도

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| variable-analyst | `steep-framework` | STEEP 6대 차원 스캐닝, 불확실성-영향력 매트릭스, 시나리오 축 선정 |
| scenario-designer | `scenario-narrative-engine` | 2x2 매트릭스 서사화, 타임라인 설계, 조기 경보 신호 |
| strategy-architect | `decision-trigger-mapper` | 의사결정 트리거 맵, 리얼옵션 사고, 전략 포트폴리오(로버스트/헤지/옵션) |
