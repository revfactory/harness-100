---
name: debate-simulator
description: "토론 시뮬레이션 종합 파이프라인. 주제분석→찬성논거→반대논거→교차심문→심판평가→종합보고서를 에이전트 팀이 협업하여 수행한다. '토론 시뮬레이션', '찬반 논거 만들어줘', '디베이트', '토론 준비', '논쟁 분석', '찬성 반대', '토론 주제 분석', '교차심문 연습', '토론 대회 준비' 등 토론 관련 전반에 이 스킬을 사용한다. 기존 논거나 토론 자료가 있으면 해당 단계를 보강한다. 단, 실시간 음성 토론 진행, 청중 투표 시스템 운영은 이 스킬의 범위가 아니다."
---

# Debate Simulator — 토론 시뮬레이션 종합 파이프라인

토론의 주제분석→찬성논거→반대논거→교차심문→심판평가→종합보고서를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 실제 토론을 시뮬레이션한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| topic-analyst | `agents/topic-analyst.md` | 주제 분석, 쟁점 구조화 | general-purpose |
| pro-debater | `agents/pro-debater.md` | 찬성 논거 구축 | general-purpose |
| con-debater | `agents/con-debater.md` | 반대 논거 구축 | general-purpose |
| judge | `agents/judge.md` | 논증 평가, 승패 판정 | general-purpose |
| rapporteur | `agents/rapporteur.md` | 종합 보고서 작성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **토론 논제**: 찬반으로 나뉠 수 있는 명확한 논제
    - **토론 목적** (선택): 교육/의사결정/대회준비/분석
    - **사용자 입장** (선택): 찬성/반대/중립
    - **토론 형식** (선택): 의회식/링컨-더글러스/자유토론
    - **기존 자료** (선택): 관련 보고서, 논문, 기사
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 주제 분석 | topic-analyst | 없음 | `_workspace/01_topic_analysis.md` |
| 2a | 찬성 논거 구축 | pro-debater | 작업 1 | `_workspace/02_pro_arguments.md` |
| 2b | 반대 논거 구축 | con-debater | 작업 1 | `_workspace/03_con_arguments.md` |
| 3 | 교차심문 | pro + con | 작업 2a, 2b | `_workspace/04_cross_examination.md` |
| 4 | 심판 평가 | judge | 작업 2a, 2b, 3 | `_workspace/05_judge_verdict.md` |
| 5 | 종합 보고서 | rapporteur | 전체 | `_workspace/06_final_report.md` |

작업 2a(찬성)와 2b(반대)는 **병렬 실행**한다. 단, 반대 측은 찬성 측 논거를 참조할 수 있으므로, 초기 논거는 독립적으로 구축 후 상호 반박 단계에서 교차한다.

**팀원 간 소통 흐름:**
- topic-analyst 완료 → pro-debater에게 찬성 유리 자료, con-debater에게 반대 유리 자료, judge에게 평가 기준 전달
- pro-debater + con-debater 완료 → 교차심문 시뮬레이션: 서로 질문·답변을 교환
- 교차심문 완료 → judge가 모든 논거+교차심문을 평가
- judge 완료 → rapporteur가 전체를 종합하여 보고서 작성

### Phase 3: 교차심문 시뮬레이션

오케스트레이터가 교차심문을 중재한다:
1. pro-debater의 교차심문 질문을 con-debater에게 전달
2. con-debater의 답변을 기록
3. con-debater의 교차심문 질문을 pro-debater에게 전달
4. pro-debater의 답변을 기록
5. 결과를 `_workspace/04_cross_examination.md`에 저장

### Phase 4: 통합 및 최종 보고

1. `_workspace/` 내 모든 파일을 확인한다
2. 종합 보고서의 균형성과 완성도를 검증한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "토론 시뮬레이션 해줘", "풀 디베이트" | **풀 시뮬레이션** | 5명 전원 |
| "주제 분석만", "쟁점 정리해줘" | **분석 모드** | topic-analyst 단독 |
| "찬반 논거만 만들어줘" | **논거 모드** | topic-analyst + pro + con |
| "이 주제로 찬성 논거 써줘" | **편측 모드** | topic-analyst + pro-debater |
| "이 토론 평가해줘" (기존 자료) | **평가 모드** | judge + rapporteur |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 교차심문 실시간 교환, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 논제가 불명확 | 사용자에게 구체화 요청, 또는 주제 분석가가 논제를 재구성 |
| 찬반 균형 불가 | 전제 조건 조정으로 논제 재구성 |
| 배경 자료 부족 | 유사 주제 사례 유추, "자료 제한" 명시 |
| 웹 검색 실패 | 일반 지식 기반 작업, 보고서에 명시 |
| 에이전트 실패 | 1회 재시도 → 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "'AI가 인간의 일자리를 대체하는 것은 사회적으로 바람직하다'라는 주제로 토론 시뮬레이션 해줘"
**기대 결과**:
- 주제 분석: 쟁점 3~4개 구조화, 배경 자료, 토론 형식
- 찬성: 3~5개 핵심 주장 + 근거 + 교차심문 질문
- 반대: 찬성 반박 + 독자적 주장 + 대안 제시
- 교차심문: 양측 3회씩 질의응답
- 심판: 100점 만점 채점 + 승패 판정 + 피드백
- 종합: 균형 잡힌 보고서 + 시사점

### 기존 파일 활용 흐름
**프롬프트**: "이 토론 자료를 기반으로 교차심문과 심판 평가만 해줘" + 찬반 논거 파일 첨부
**기대 결과**:
- 기존 자료를 `_workspace/02_pro_arguments.md`, `_workspace/03_con_arguments.md`로 복사
- topic-analyst, pro-debater, con-debater 건너뛰고 교차심문 + judge + rapporteur 투입

### 에러 흐름
**프롬프트**: "토론 시뮬레이션 해줘, 주제는 알아서 정해"
**기대 결과**:
- 논제 불명확 → topic-analyst가 시사 이슈 기반 3개 논제 제안 후 선택 요청
- 선택 후 풀 시뮬레이션 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| pro-debater, con-debater | `argumentation-framework` | Toulmin 논증 모델, 증거 피라미드, 반박 5-Type, 교차심문 설계 |
| judge, rapporteur | `logical-fallacy-detector` | 논리적 오류 4대 분류, 오류 감점 기준, 논증 건전성 루브릭 |
