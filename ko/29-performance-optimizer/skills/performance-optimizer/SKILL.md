---
name: performance-optimizer
description: "애플리케이션 성능 최적화를 프로파일링, 병목 분석, 최적화 구현, 벤치마크 검증까지 에이전트 팀이 협업하여 수행하는 풀 파이프라인. '성능 최적화해줘', '느린 API 개선', '쿼리 최적화', '응답시간 줄여줘', '성능 프로파일링', '병목 분석', '벤치마크 테스트', '로딩 속도 개선', 'P95 응답시간 줄이기', '처리량 늘리기' 등 성능 개선 전반에 이 스킬을 사용한다. 특정 쿼리 최적화나 프로파일링만 필요한 경우에도 지원한다. 단, 인프라 프로비저닝 직접 실행, 로드밸런서 설정, CDN 구성 직접 배포는 이 스킬의 범위가 아니다."
---

# Performance Optimizer — 성능 최적화 풀 파이프라인

애플리케이션의 프로파일링→병목분석→최적화→벤치마크를 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| profiler | `agents/profiler.md` | CPU, 메모리, I/O, 네트워크 프로파일링 | general-purpose |
| bottleneck-analyst | `agents/bottleneck-analyst.md` | 핫스팟 식별, 근본원인, 영향산정 | general-purpose |
| optimization-engineer | `agents/optimization-engineer.md` | 코드/쿼리/아키텍처 최적화 | general-purpose |
| benchmark-manager | `agents/benchmark-manager.md` | 테스트설계, 실행, 비교분석 | general-purpose |
| perf-reviewer | `agents/perf-reviewer.md` | 교차검증, 회귀방지, 최종보고서 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **최적화 대상**: 코드, API, 쿼리, 시스템 전체
    - **성능 목표**: 응답시간, 처리량, 메모리 사용량 등 구체적 수치
    - **기술 스택**: 언어, 프레임워크, DB, 인프라
    - **현재 문제** (선택): 구체적 증상, 에러 로그, 사용자 불만
    - **기존 파일** (선택): 프로파일링 결과, 실행 계획, 코드
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 프로파일링 | profiler | 없음 | `_workspace/01_profiling_report.md` |
| 2 | 병목 분석 | bottleneck-analyst | 작업 1 | `_workspace/02_bottleneck_analysis.md` |
| 3 | 최적화 구현 | optimization-engineer | 작업 2 | `_workspace/03_optimization_plan.md` |
| 4 | 벤치마크 검증 | benchmark-manager | 작업 1, 3 | `_workspace/04_benchmark_results.md` |
| 5 | 성능 리뷰 | perf-reviewer | 작업 1~4 | `_workspace/05_review_report.md` |

**팀원 간 소통 흐름:**
- profiler 완료 → analyst에게 핫스팟·자원 패턴 전달, benchmark에게 baseline 수치 전달
- analyst 완료 → engineer에게 병목 우선순위·근본원인 전달, benchmark에게 성능 예산 전달
- engineer 완료 → benchmark에게 최적화 코드·기대 수치 전달
- benchmark 완료 → reviewer에게 비교 분석 결과 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 프로파일링 — `01_profiling_report.md`
    - 병목 분석 — `02_bottleneck_analysis.md`
    - 최적화 계획 — `03_optimization_plan.md`
    - 벤치마크 — `04_benchmark_results.md`
    - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "성능 전체 최적화해줘" | **풀 파이프라인** | 5명 전원 |
| "이 코드 프로파일링해줘" | **프로파일링 모드** | profiler + reviewer |
| "이 쿼리 최적화해줘" | **쿼리 최적화 모드** | profiler + analyst + engineer + reviewer |
| "벤치마크 테스트 설계해줘" | **벤치마크 모드** | benchmark + reviewer |
| "이 최적화 결과 검증해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 프로파일링 도구 실행 불가 | 코드 정적 분석으로 대체, 도구 설정 가이드 제공 |
| 실행 환경 부재 | 벤치마크 스크립트 + 실행 가이드 제공, 예상 결과 시뮬레이션 |
| 성능 목표 미정 | 업계 표준(P95 < 200ms, 에러율 < 1%) 기반 목표 제안 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "Django REST API의 응답시간이 P95 기준 2초인데, 500ms 이하로 줄이고 싶어. 코드 분석하고 최적화해줘."
**기대 결과**:
- 프로파일링: Django 미들웨어, ORM 쿼리, 직렬화 과정 분석, N+1 쿼리 탐지
- 병목분석: DB 쿼리가 전체 응답시간의 70% 차지 → ORM N+1 + 인덱스 미비 진단
- 최적화: select_related/prefetch_related 적용, 인덱스 추가, 쿼리셋 캐싱
- 벤치마크: k6 스크립트로 전후 비교, P95 2s → 400ms 검증
- 리뷰: 정합성 확인, 회귀 위험 평가

### 기존 파일 활용 흐름
**프롬프트**: "이 프로파일링 결과를 분석하고 최적화 방안 제시해줘" + flame graph 첨부
**기대 결과**:
- 기존 프로파일링 데이터를 `_workspace/01_profiling_report.md`로 활용
- profiler 건너뛰고 analyst + engineer + benchmark + reviewer 투입

### 에러 흐름
**프롬프트**: "사이트가 느린데 뭐가 문제인지 모르겠어"
**기대 결과**:
- 코드 정적 분석 기반 프로파일링 수행
- 일반적 성능 안티패턴 체크리스트 적용
- "상세 프로파일링 도구 적용 권장" 명시


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| query-optimization-patterns | `skills/query-optimization-patterns/SKILL.md` | bottleneck-analyst, optimization-engineer | 실행 계획 분석, 인덱스 설계, N+1 해결, 페이지네이션 |
| caching-strategy-selector | `skills/caching-strategy-selector/SKILL.md` | optimization-engineer | Cache Aside/Write Through/Behind, 무효화, 스탬피드 방지 |
