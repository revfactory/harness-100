---
name: research-assistant
description: "학술 연구 보조를 에이전트 팀이 체계적으로 수행하는 파이프라인. '논문 조사해줘', '문헌 리뷰', '연구 자료 정리', 'literature review', '학술 리서치', '참고문헌 정리', '선행 연구 분석', '연구 동향 파악', '문헌 검색', '학술 메모 정리' 등 학술 연구 보조 전반에 이 스킬을 사용한다. 단, 실험 수행, 통계 분석 실행, 논문 최종 집필, 학술지 투고는 이 스킬의 범위가 아니다."
---

# Research Assistant — 학술 연구 보조 파이프라인

문헌 검색→메모 작성→비평·종합→참고문헌 관리를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| literature-searcher | `agents/literature-searcher.md` | 문헌 검색·관련성 필터링 | general-purpose |
| note-taker | `agents/note-taker.md` | 구조화된 읽기 메모 작성 | general-purpose |
| critic-synthesizer | `agents/critic-synthesizer.md` | 비판적 분석·테마 종합 | general-purpose |
| reference-manager | `agents/reference-manager.md` | 서지 정보·인용 형식 관리 | general-purpose |
| research-coordinator | `agents/research-coordinator.md` | 품질 검증·최종 정리 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **연구 주제/질문**: 무엇을 조사하는가
    - **연구 목적** (선택): 논문 작성, 발표, 보고서 등
    - **인용 형식** (선택): APA, MLA, Chicago 등 (기본: APA 7th)
    - **범위 제한** (선택): 기간, 언어, 분야, 문헌 수
    - **기존 자료** (선택): 이미 수집한 논문, 메모
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 문헌 검색 | literature-searcher | 없음 | `_workspace/01_literature_search.md` |
| 2a | 읽기 메모 | note-taker | 작업 1 | `_workspace/02_reading_notes.md` |
| 2b | 참고문헌 초안 | reference-manager | 작업 1 | `_workspace/04_bibliography.md` (초안) |
| 3 | 비평·종합 | critic-synthesizer | 작업 2a | `_workspace/03_critical_synthesis.md` |
| 4 | 참고문헌 최종화 | reference-manager | 작업 3 | `_workspace/04_bibliography.md` (최종) |
| 5 | 연구 조율·검증 | research-coordinator | 작업 2a, 3, 4 | `_workspace/05_research_summary.md` |

작업 2a(메모)와 2b(참고문헌 초안)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- literature-searcher 완료 → note-taker에게 문헌 목록·우선순위, reference-manager에게 서지 정보 전달
- note-taker 완료 → critic-synthesizer에게 메모·연결점 전달
- critic-synthesizer 완료 → reference-manager에게 인용 목록 전달
- research-coordinator는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 연구 조율 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 문헌 검색 결과 — `01_literature_search.md`
    - 읽기 메모 — `02_reading_notes.md`
    - 비평·종합 — `03_critical_synthesis.md`
    - 참고문헌 — `04_bibliography.md`
    - 연구 보고서 — `05_research_summary.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "문헌 리뷰 해줘", "선행 연구 분석" | **풀 파이프라인** | 5명 전원 |
| "논문 검색만 해줘" | **검색 모드** | literature-searcher + reference-manager |
| "이 논문들 정리해줘" (기존 문헌 제공) | **메모 모드** | note-taker + critic-synthesizer + reference-manager |
| "참고문헌 형식 바꿔줘" | **서지 모드** | reference-manager 단독 |
| "이 문헌들 종합 분석해줘" | **종합 모드** | critic-synthesizer + research-coordinator |

**기존 파일 활용**: 사용자가 논문 목록이나 메모를 제공하면, `_workspace/`에 복사하고 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 웹 탐색 | WebSearch/WebFetch | 학술 자료 검색·수집 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 알려진 주요 학술지·저자 기반 추천, "검색 제한" 명시 |
| 논문 전문 접근 불가 | 초록 기반으로 작업, "전문 미확인" 표시 |
| 문헌 수 부족 | 인접 분야로 확대 검색, "예비 종합" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 누락 명시 |
| 인용 형식 불명 | APA 7th를 기본 적용, 사용자에게 확인 요청 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "'대규모 언어 모델의 환각(hallucination) 완화 기법'에 대한 문헌 리뷰를 해줘. APA 형식으로."
**기대 결과**:
- 문헌 검색: 10편 이상, Boolean 검색식 기록, 핵심/보조/배경 분류
- 읽기 메모: 문헌별 구조화 메모, 방법론 분석, 핵심 인용 추출
- 비평·종합: 테마별 종합, 연구 갭 식별, 시간적 발전 궤적
- 참고문헌: APA 7th 형식, 본문 인용 가이드, BibTeX
- 연구 보고서: 정합성 매트릭스 전항목 확인

### 기존 자료 활용 흐름
**프롬프트**: "이 5편의 논문을 정리하고 종합 분석해줘" + 논문 목록 제공
**기대 결과**:
- 문헌 검색 건너뛰기, 제공된 논문 목록을 `01_literature_search.md`로 정리
- note-taker + critic-synthesizer + reference-manager 중심 작업

### 에러 흐름
**프롬프트**: "양자 컴퓨팅과 머신러닝의 교차점 논문 찾아줘"
**기대 결과**:
- 검색 모드로 전환
- 웹 검색으로 관련 논문 탐색
- 검색 결과가 제한적이면 인접 분야 확대 + "예비 검색" 명시

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| literature-searcher, critic-synthesizer | `systematic-review-protocol` | PRISMA 흐름도, PICO 검색식, Boolean 전략, 문헌 품질 평가, 테마 종합 |
| reference-manager | `citation-formatter` | APA/MLA/Chicago 형식, BibTeX 변환, 한국어 문헌 규칙, 인용 품질 체크 |
