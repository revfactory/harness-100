---
name: test-automation
description: "테스트 자동화 풀 파이프라인. 전략 수립, 단위/통합 테스트 작성, CI 통합, 커버리지 분석을 에이전트 팀이 협업하여 수행한다. '테스트 자동화해줘', '테스트 코드 작성해줘', '단위 테스트 만들어줘', '통합 테스트 작성', '테스트 커버리지 분석', '테스트 전략 세워줘', 'CI에 테스트 연동해줘', '테스트 피라미드 설계' 등 테스트 자동화 전반에 이 스킬을 사용한다. 기존 테스트가 있어도 커버리지 분석이나 개선을 지원한다. 단, E2E/UI 테스트 실행, 브라우저 자동화 실행, 부하 테스트 실행은 이 스킬의 범위가 아니다."
---

# Test Automation — 테스트 자동화 파이프라인

테스트 전략수립→테스트작성→CI통합→커버리지분석을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| test-strategist | `agents/test-strategist.md` | 테스트 피라미드, 도구, CI 설계 | general-purpose |
| unit-tester | `agents/unit-tester.md` | 단위 테스트 작성, 모킹 | general-purpose |
| integration-tester | `agents/integration-tester.md` | API/DB/외부 서비스 테스트 | general-purpose |
| coverage-analyst | `agents/coverage-analyst.md` | 커버리지 갭 분석, 개선 계획 | general-purpose |
| qa-reviewer | `agents/qa-reviewer.md` | 교차 검증, 테스트 품질 평가 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 코드**: 테스트할 코드베이스 또는 모듈
    - **기술 스택** (선택): 언어, 프레임워크, 기존 테스트 도구
    - **제약 조건** (선택): 커버리지 목표, CI 플랫폼, 시간 제한
    - **기존 테스트** (선택): 이미 작성된 테스트 코드
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 테스트 전략 수립 | strategist | 없음 | `_workspace/01_test_strategy.md` |
| 2a | 단위 테스트 작성 | unit-tester | 작업 1 | `_workspace/02_unit_tests.md` |
| 2b | 통합 테스트 작성 | integration-tester | 작업 1 | `_workspace/03_integration_tests.md` |
| 3 | 커버리지 분석 | coverage-analyst | 작업 1, 2a, 2b | `_workspace/04_coverage_report.md` |
| 4 | 최종 리뷰 | qa-reviewer | 작업 1~3 | `_workspace/05_review_report.md` |

작업 2a(단위)와 2b(통합)는 **병렬 실행** 가능하다.

**팀원 간 소통 흐름:**
- strategist 완료 → unit-tester에게 테스트 범위·모킹 전략 전달, integration-tester에게 통합 테스트 범위·환경 전략 전달
- unit-tester 완료 → integration-tester에게 모킹 인터페이스 목록 공유, coverage-analyst에게 테스트 목록 전달
- integration-tester 완료 → coverage-analyst에게 통합 테스트 목록 전달
- coverage-analyst 완료 → 갭 발견 시 unit-tester/integration-tester에게 추가 테스트 요청
- qa-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "테스트 자동화해줘", "풀 테스트" | **풀 파이프라인** | 5명 전원 |
| "단위 테스트만 작성해줘" | **단위 테스트 모드** | strategist + unit-tester + reviewer |
| "통합 테스트만 작성해줘" | **통합 테스트 모드** | strategist + integration-tester + reviewer |
| "커버리지 분석해줘" | **커버리지 모드** | coverage-analyst + reviewer |
| "테스트 전략만 세워줘" | **전략 모드** | strategist + reviewer |

**기존 파일 활용**: 사용자가 기존 테스트 코드, 커버리지 보고서 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 코드 접근 불가 | 사용자 설명 기반 일반적 테스트 작성, 보고서에 "추정 기반" 명시 |
| 테스트 프레임워크 미설치 | 설치 가이드 포함하여 테스트 코드 제공 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 커버리지 도구 실행 불가 | 정적 분석 기반 추정 커버리지로 대체 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "NestJS로 만든 REST API에 테스트 자동화를 적용해줘. 현재 테스트가 하나도 없어"
**기대 결과**:
- 전략: Jest + Supertest 선정, 리스크 기반 우선순위, CI(GitHub Actions) 설계
- 단위: 서비스 클래스 테스트, Repository 모킹, DTO 검증
- 통합: API 엔드포인트 테스트, Testcontainers로 PostgreSQL 연동
- 커버리지: 모듈별 갭 분석, P0/P1 추가 테스트 제안
- 리뷰: 전 항목 정합성 검증

### 기존 파일 활용 흐름
**프롬프트**: "기존 테스트 커버리지가 40%인데 80%까지 올리고 싶어" + 코드/테스트 첨부
**기대 결과**:
- 커버리지 모드로 시작, 현재 갭 분석
- 리스크 기반 우선순위로 추가 테스트 계획 수립
- 단계별 개선 로드맵 (40% → 60% → 80%)

### 에러 흐름
**프롬프트**: "이 함수 테스트 코드 써줘" (함수 하나만 제공)
**기대 결과**:
- 단위 테스트 모드로 전환
- 해당 함수의 경계값, 정상/비정상 케이스 테스트 작성
- 전략 없이도 기본 AAA 패턴으로 즉시 테스트 제공


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| test-design-patterns | `skills/test-design-patterns/SKILL.md` | test-strategist, unit-tester | 경계값 분석, 동등 분할, 상태 전이, 페어와이즈, 리스크 기반 우선순위 |
| mocking-strategy | `skills/mocking-strategy/SKILL.md` | unit-tester, integration-tester | Mock/Stub/Spy/Fake 선택, 계층별 모킹, 안티패턴 방지 |
