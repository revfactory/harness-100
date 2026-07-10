---
name: thesis-advisor
description: "논문 작성 종합 지원 파이프라인. 주제선정→문헌조사→방법론설계→집필→교정을 에이전트 팀이 협업하여 수행한다. '논문 도와줘', '연구 주제 잡아줘', '문헌 검토', '방법론 설계', '논문 써줘', '논문 교정', '학위 논문', '학술지 투고', '연구 설계', 'literature review' 등 학술 논문 작성 전반에 이 스킬을 사용한다. 기존 원고나 문헌 목록이 있으면 해당 단계를 보강한다. 단, 실제 데이터 수집·분석 실행, 통계 소프트웨어 조작, 학술지 투고 시스템 조작은 이 스킬의 범위가 아니다."
---

# Thesis Advisor — 논문 작성 종합 지원 파이프라인

논문의 주제선정→문헌조사→방법론→집필→교정을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| topic-explorer | `agents/topic-explorer.md` | 주제 탐색, 연구질문 수립 | general-purpose |
| literature-analyst | `agents/literature-analyst.md` | 문헌 조사, 비판적 검토 | general-purpose |
| methodology-expert | `agents/methodology-expert.md` | 연구설계, 분석방법 선정 | general-purpose |
| writing-coach | `agents/writing-coach.md` | 논문 구조 설계, 초고 작성 | general-purpose |
| proofreader | `agents/proofreader.md` | 교정, 형식 검증, 일관성 검토 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **학문 분야**: 전공, 세부 분야
    - **논문 유형**: 석사/박사/학술지/학부 졸업논문
    - **관심 주제** (선택): 구체적 주제 또는 키워드
    - **지도교수 연구 분야** (선택): 연구실 방향성
    - **기존 자료** (선택): 기존 원고, 문헌 목록, 데이터
    - **마감일** (선택): 제출 기한
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 해당 Phase를 조정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 주제 탐색·선정 | topic-explorer | 없음 | `_workspace/01_topic_proposal.md` |
| 2 | 문헌 조사·검토 | literature-analyst | 작업 1 | `_workspace/02_literature_review.md` |
| 3 | 방법론 설계 | methodology-expert | 작업 1, 2 | `_workspace/03_methodology_design.md` |
| 4 | 논문 초고 작성 | writing-coach | 작업 1, 2, 3 | `_workspace/04_draft_manuscript.md` |
| 5 | 교정·검증 | proofreader | 작업 4 | `_workspace/05_proofread_report.md` |

**팀원 간 소통 흐름:**
- topic-explorer 완료 → literature-analyst에게 연구질문·키워드 전달, methodology-expert에게 가설·변수 전달
- literature-analyst 완료 → methodology-expert에게 선행연구 방법론 동향 전달, writing-coach에게 문헌 검토 내용 전달
- methodology-expert 완료 → writing-coach에게 방법론 설계 전문 전달
- writing-coach 완료 → proofreader에게 초고 전문 전달
- proofreader 완료 → 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 보고

1. `_workspace/` 내 모든 파일을 확인한다
2. 교정 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "논문 처음부터 끝까지", "풀 지원" | **풀 파이프라인** | 5명 전원 |
| "연구 주제 잡아줘" | **주제 탐색 모드** | topic-explorer 단독 |
| "문헌 검토 해줘" | **문헌 검토 모드** | topic-explorer + literature-analyst |
| "방법론 설계해줘" | **방법론 모드** | methodology-expert 단독 (기존 RQ 활용) |
| "논문 써줘", "초고 작성" | **집필 모드** | writing-coach + proofreader |
| "논문 교정해줘" (기존 원고) | **교정 모드** | proofreader 단독 |

**기존 자료 활용**: 사용자가 기존 원고, 문헌 목록 등을 제공하면 해당 단계를 건너뛰거나 보강한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 학술 DB 검색 실패 | 웹 검색으로 대체, 보고서에 "검색 제한" 명시 |
| 분야 특정 불가 | 사용자에게 분야 좁히기 질문, 관심사 기반 추론 |
| 기존 원고 형식 불명확 | 일반적 학위 논문 형식 적용 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 교정에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "교육학 석사 논문을 쓰려고 해. 플립러닝이 학습 동기에 미치는 영향에 관심이 있어."
**기대 결과**:
- 주제 제안: 플립러닝×학습동기 관련 연구 갭 발견, RQ 3~5개, 후보 주제 비교
- 문헌 검토: 플립러닝·학습동기 선행연구 20편+, 이론적 프레임워크
- 방법론: 준실험 설계 또는 설문 조사, 표본·도구·분석 방법
- 초고: 석사 논문 구조(6장), 서론~연구방법까지 완성
- 교정: 형식·문체·일관성 검증

### 기존 파일 활용 흐름
**프롬프트**: "이 원고 교정해줘" + 논문 파일 첨부
**기대 결과**:
- 교정 모드 (proofreader 단독)
- 문법·형식·일관성 검증 보고서

### 에러 흐름
**프롬프트**: "논문 주제 추천해줘, 분야는 아직 안 정했어"
**기대 결과**:
- 관심사·강점 파악 질문으로 분야를 좁힌 후 주제 탐색 모드로 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| methodology-expert | `research-methodology` | 연구 설계 매트릭스, 표본 크기 산출, 타당도·신뢰도, 분석 방법 선택 |
| writing-coach, proofreader | `academic-writing-style` | 논문 장별 구조, 학술 문체 규칙, APA 인용, 교정 체크리스트 |
