---
name: academic-paper
description: "학술 논문 작성의 연구설계, 실험, 분석, 집필, 투고준비를 에이전트 팀이 협업하여 한 번에 생성하는 풀 연구 파이프라인. '학술 논문 써줘', '연구 논문 작성', '논문 쓰기 도와줘', '연구 설계해줘', '통계 분석해줘', '저널 투고 준비', '논문 집필', '연구 방법론 설계', '가설 검증', '학술 글쓰기' 등 학술 연구 논문 작성 전반에 이 스킬을 사용한다. 기존 데이터나 초고가 있는 경우에도 분석/리라이팅/투고 준비를 지원한다. 단, 실제 데이터 수집 실행, IRB 공식 제출, 저널 시스템 로그인 및 업로드, 실제 통계 소프트웨어 실행은 이 스킬의 범위가 아니다."
---

# Academic Paper — 학술 논문 작성 풀 파이프라인

학술 논문의 연구설계→실험→분석→집필→투고준비를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| research-designer | `agents/research-designer.md` | 연구 질문, 가설, 방법론, 선행연구 | general-purpose |
| experiment-manager | `agents/experiment-manager.md` | 실험 프로토콜, 데이터 수집 계획 | general-purpose |
| statistical-analyst | `agents/statistical-analyst.md` | 통계 분석, 코드 생성, 시각화 | general-purpose |
| paper-writer | `agents/paper-writer.md` | IMRaD 구조 집필, 인용 관리 | general-purpose |
| submission-preparer | `agents/submission-preparer.md` | 저널 선정, 포맷팅, 커버레터 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **연구 주제**: 연구 분야, 핵심 키워드
    - **연구 수준** (선택): 학부/석사/박사/교수 수준
    - **타깃 저널** (선택): 저널명, IF 범위
    - **기존 자료** (선택): 데이터, 초고, 선행연구 목록
    - **제약 조건** (선택): 마감일, 분량, 특이사항
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 연구 설계 | designer | 없음 | `_workspace/01_research_design.md` |
| 2 | 실험 프로토콜 | experiment | 작업 1 | `_workspace/02_experiment_protocol.md` |
| 3 | 통계 분석 | analyst | 작업 1, 2 | `_workspace/03_analysis_report.md` |
| 4 | 논문 집필 | writer | 작업 1, 2, 3 | `_workspace/04_manuscript.md` |
| 5 | 투고 준비 | preparer | 작업 1, 4 | `_workspace/05_submission_package.md` |
| 6 | 통합 리뷰 | 오케스트레이터 | 전체 | `_workspace/06_review_report.md` |

**팀원 간 소통 흐름:**
- designer 완료 → experiment에게 변수·표본 전달, analyst에게 가설·분석 방향 전달, writer에게 이론적 배경 전달, preparer에게 연구 분야 전달
- experiment 완료 → analyst에게 데이터 구조 전달, writer에게 Methods 자료 전달
- analyst 완료 → writer에게 Results 자료(APA 형식 + Table/Figure) 전달, preparer에게 분석 코드 전달
- writer 완료 → preparer에게 완성 원고 전달
- 오케스트레이터가 전체 일관성(가설↔분석↔결과↔논의)을 교차 검증

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일의 정합성을 확인한다
2. 가설-분석-결과-논의의 논리적 일관성을 검증한다
3. 통합 리뷰 보고서를 생성한다
4. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "논문 써줘", "연구 논문 작성" | **풀 파이프라인** | 5명 전원 |
| "연구 설계만 해줘" | **설계 모드** | designer 단독 |
| "이 데이터 분석해줘" + 데이터 | **분석 모드** | analyst + writer |
| "논문 초고 다듬어줘" + 초고 | **리라이팅 모드** | writer + preparer |
| "투고 준비해줘" + 원고 | **투고 모드** | preparer 단독 |
| "이 연구 설계로 나머지 진행해줘" + 설계서 | **후속 모드** | experiment → analyst → writer → preparer |

**기존 파일 활용**: 사용자가 데이터, 초고, 설계서 등을 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 선행연구 검색 실패 | 사용자 제공 참고문헌 중심으로 작업, "제한적 문헌 검토" 명시 |
| 연구 주제 모호 | 세부 주제 3개 제안 후 사용자 선택 요청 |
| 데이터 부재 | 분석 전략과 코드만 제공, "데이터 수집 후 실행" 안내 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 가설-결과 불일치 | 논문작성자가 Discussion에서 설명, 사후 분석(post-hoc) 제안 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "소셜 미디어 사용 시간이 대학생의 학업 성취도에 미치는 영향을 연구하는 논문을 써줘. 설문조사 기반으로"
**기대 결과**:
- 설계: 횡단적 조사 설계, SNS 사용 시간(IV) → GPA(DV), 통제변수 포함
- 프로토콜: 설문지(기존 척도 활용), 온라인 수집 절차
- 분석: 다중회귀분석 코드(R/Python), APA 형식 결과
- 원고: IMRaD 완전 구조, 선행연구 인용
- 투고: SSCI 저널 3개 추천, 커버레터

### 기존 파일 활용 흐름
**프롬프트**: "이 데이터로 논문 분석이랑 집필해줘" + CSV 데이터 첨부
**기대 결과**:
- 데이터에서 변수 구조를 파악하여 분석 전략 수립
- designer를 가볍게 투입하여 연구 프레임 역추출
- analyst → writer → preparer 순서로 진행

### 에러 흐름
**프롬프트**: "논문 써줘, 주제는 아직 안 정했어"
**기대 결과**:
- designer가 사용자의 관심 분야를 질문하거나
- 최근 트렌드 기반 연구 주제 3개를 제안
- 리뷰 보고서에 "주제 미확정 — 예시 기반 진행" 명시

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| research-methodology | `skills/research-methodology/SKILL.md` | research-designer, statistical-analyst | 연구 설계, 표본, 통계 분석, 윤리 |
| citation-standards | `skills/citation-standards/SKILL.md` | paper-writer, submission-preparer | APA/IEEE/Chicago 인용, IMRaD, 투고 준비 |
