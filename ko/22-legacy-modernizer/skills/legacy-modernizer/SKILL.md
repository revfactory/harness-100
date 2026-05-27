---
name: legacy-modernizer
description: "레거시 코드베이스를 현대적 아키텍처로 전환하는 풀 파이프라인. 기술부채 분석, 리팩토링 전략 수립, 코드 마이그레이션, 회귀 테스트를 에이전트 팀이 협업하여 수행한다. '레거시 코드 현대화해줘', '리팩토링 전략 세워줘', '코드 마이그레이션', '기술부채 분석', '레거시 시스템 업그레이드', '프레임워크 전환', '코드 모더나이제이션', '리팩토링 계획' 등 레거시 코드 현대화 전반에 이 스킬을 사용한다. 기존 분석 보고서가 있어도 전략 수립이나 마이그레이션을 지원한다. 단, 실제 프로덕션 배포, CI/CD 파이프라인 실행, 인프라 프로비저닝은 이 스킬의 범위가 아니다."
---

# Legacy Modernizer — 레거시 코드 현대화 파이프라인

레거시 코드의 분석→리팩토링전략→마이그레이션→검증을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| legacy-analyzer | `agents/legacy-analyzer.md` | 기술부채 식별, 의존성 매핑, 복잡도 측정 | general-purpose |
| refactoring-strategist | `agents/refactoring-strategist.md` | 패턴 선정, 우선순위, 로드맵 | general-purpose |
| migration-engineer | `agents/migration-engineer.md` | 코드 변환, API 현대화, 프레임워크 전환 | general-purpose |
| regression-tester | `agents/regression-tester.md` | 동작 보존 검증, 성능 비교 | general-purpose |
| modernization-reviewer | `agents/modernization-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 코드/시스템**: 현대화할 코드베이스 또는 시스템 정보
    - **목표 아키텍처** (선택): 전환하고자 하는 기술 스택/패턴
    - **제약 조건** (선택): 다운타임 허용 범위, 예산, 기간
    - **기존 문서** (선택): 아키텍처 문서, 분석 보고서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 레거시 분석 | analyzer | 없음 | `_workspace/01_legacy_analysis.md` |
| 2 | 리팩토링 전략 수립 | strategist | 작업 1 | `_workspace/02_refactoring_strategy.md` |
| 3 | 마이그레이션 실행 계획 | engineer | 작업 1, 2 | `_workspace/03_migration_plan.md` |
| 4 | 회귀 테스트 | tester | 작업 1, 3 | `_workspace/04_test_report.md` |
| 5 | 최종 리뷰 | reviewer | 작업 1~4 | `_workspace/05_review_report.md` |

**팀원 간 소통 흐름:**
- analyzer 완료 → strategist에게 기술부채·핫스팟·의존성 전달, engineer에게 기술 스택·비즈니스 로직 전달, tester에게 현재 커버리지 전달
- strategist 완료 → engineer에게 로드맵·전환 매핑 전달, tester에게 Phase별 완료 기준 전달
- engineer 완료 → tester에게 Before/After·검증 포인트 전달
- tester 완료 → 회귀 발견 시 engineer에게 수정 요청
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "레거시 코드 현대화해줘", "풀 리팩토링" | **풀 파이프라인** | 5명 전원 |
| "기술부채 분석해줘", "코드 상태 진단" | **분석 모드** | analyzer + reviewer |
| "리팩토링 전략 세워줘" (기존 분석 있음) | **전략 모드** | strategist + reviewer |
| "이 코드 마이그레이션해줘" (전략 있음) | **마이그레이션 모드** | engineer + tester + reviewer |
| "마이그레이션 검증해줘" | **테스트 모드** | tester + reviewer |

**기존 파일 활용**: 사용자가 분석 보고서, 전략서 등을 제공하면 해당 단계는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 코드 접근 불가 | 사용자 제공 정보 기반 추론 분석, 보고서에 "제한된 접근" 명시 |
| 테스트 환경 없음 | 정적 분석과 코드 리뷰 기반 검증으로 대체 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 순환 의존성 해소 불가 | Anti-Corruption Layer 삽입으로 격리 후 점진적 해소 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "jQuery + Express.js 기반 레거시 웹앱을 React + NestJS로 현대화해줘"
**기대 결과**:
- 분석: jQuery 의존성 매핑, Express 라우트 구조 분석, 기술부채 인벤토리
- 전략: Strangler Fig 패턴, 프론트엔드 우선 전환 로드맵
- 마이그레이션: jQuery→React 컴포넌트 변환, Express→NestJS 컨트롤러 변환
- 테스트: DOM 조작 동작 보존, API 호환성, 성능 비교
- 리뷰: 전 항목 정합성 검증

### 기존 파일 활용 흐름
**프롬프트**: "이 분석 보고서 기반으로 리팩토링 전략만 세워줘" + 분석 보고서 첨부
**기대 결과**:
- 기존 보고서를 `_workspace/01_legacy_analysis.md`로 복사
- 전략 모드: strategist + reviewer만 투입
- analyzer는 건너뜀

### 에러 흐름
**프롬프트**: "이 코드 리팩토링해줘" (코드 조각만 제공, 전체 컨텍스트 없음)
**기대 결과**:
- 분석 모드로 시작, 제한된 정보로 추론 분석
- 보고서에 "부분 코드 기반 분석 — 전체 시스템 컨텍스트 미확인" 명시
- 추가 정보 필요 시 사용자에게 질문

## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| strangler-fig-patterns | `skills/strangler-fig-patterns/SKILL.md` | refactoring-strategist, migration-engineer | 점진적 마이그레이션 패턴(Strangler Fig, Branch by Abstraction, Parallel Run, ACL) 상세 구현 |
| dependency-analysis | `skills/dependency-analysis/SKILL.md` | legacy-analyzer, refactoring-strategist | 의존성 그래프 분석, 결합도/응집도 메트릭, 순환 의존성 탐지·해소 |
