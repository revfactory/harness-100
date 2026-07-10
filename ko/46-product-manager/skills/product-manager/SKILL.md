---
name: product-manager
description: "PM 업무의 로드맵, PRD, 유저스토리, 스프린트 계획, 회고를 에이전트 팀이 협업하여 한 번에 생성하는 풀 PM 파이프라인. 'PRD 작성해줘', '로드맵 만들어줘', '유저스토리 분해해줘', '스프린트 계획해줘', '제품 기획해줘', 'PM 업무 도와줘', '기능 명세서', '제품 요구사항', '백로그 정리', '스프린트 플래닝', 'OKR 설정', '제품 전략', '회고 템플릿' 등 PM 업무 전반에 이 스킬을 사용한다. 기존 PRD나 로드맵이 있는 경우에도 유저스토리 분해나 스프린트 계획을 지원한다. 단, 실제 Jira/Linear 티켓 생성, 디자인 목업 제작, 코드 개발, 이해관계자 미팅 진행은 이 스킬의 범위가 아니다."
---

# Product Manager — PM 업무 풀 파이프라인

로드맵→PRD→유저스토리→스프린트→회고를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| strategist | `agents/strategist.md` | 비전, 로드맵, OKR, 우선순위 | general-purpose |
| prd-writer | `agents/prd-writer.md` | 제품 요구사항 정의서 | general-purpose |
| story-writer | `agents/story-writer.md` | 유저스토리, AC, 스토리맵 | general-purpose |
| sprint-planner | `agents/sprint-planner.md` | 스프린트 계획, 용량, 회고 | general-purpose |
| pm-reviewer | `agents/pm-reviewer.md` | 정합성 검증, 실행 가능성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **제품/기능**: 계획하려는 제품 또는 기능
    - **목표**: 달성하려는 비즈니스/사용자 목표
    - **팀 정보** (선택): 팀 규모, 역할 구성, 벨로시티
    - **제약 조건** (선택): 기간, 기술 스택, 리소스
    - **기존 자산** (선택): 기존 PRD, 로드맵, 백로그
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 해당 단계를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 로드맵 수립 | strategist | 없음 | `_workspace/01_product_roadmap.md` |
| 2 | PRD 작성 | prd-writer | 작업 1 | `_workspace/02_prd.md` |
| 3 | 유저스토리 분해 | story-writer | 작업 1, 2 | `_workspace/03_user_stories.md` |
| 4 | 스프린트 계획 | sprint-planner | 작업 3 | `_workspace/04_sprint_plan.md` |
| 5 | PM 검증 | pm-reviewer | 작업 1~4 | `_workspace/05_review_report.md` |

**팀원 간 소통 흐름:**
- strategist 완료 → prd-writer에게 이니셔티브·OKR·성공지표 전달, story-writer에게 페르소나·유즈케이스 전달
- prd-writer 완료 → story-writer에게 요구사항·AC·범위 전달, sprint-planner에게 타임라인·의존성 전달
- story-writer 완료 → sprint-planner에게 스토리 목록·의존성·SP 합계 전달
- pm-reviewer는 모든 산출물 교차 검증. 🔴 필수 수정 발견 시 수정 요청 → 재작업 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "제품 기획해줘", "PM 업무 풀로" | **풀 파이프라인** | 5명 전원 |
| "로드맵만 만들어줘" | **전략 모드** | strategist + reviewer |
| "PRD 써줘" | **PRD 모드** | strategist + prd-writer + reviewer |
| "이 PRD로 유저스토리 만들어줘" (기존 PRD) | **스토리 모드** | story-writer + reviewer |
| "스프린트 계획 세워줘" (기존 스토리) | **스프린트 모드** | sprint-planner + reviewer |
| "이 계획 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 제품 정보 불충분 | 전략가가 일반적 제품 카테고리 3개 제안 후 선택 유도 |
| 팀 정보 부재 | 4~6인 표준 스크럼팀 기준으로 계획 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 검증 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "우리 SaaS 제품에 팀 협업 기능을 추가하려고 해. 제품 기획해줘"
**기대 결과**:
- 로드맵: 팀 협업 테마 OKR, Now/Next/Later 로드맵, RICE 우선순위
- PRD: 팀 협업 기능 명세, 사용자 플로우, AC, 비기능 요구사항
- 유저스토리: 15~25개 스토리, 스토리맵, 총 SP
- 스프린트: 3~4스프린트 계획, 용량, 리스크, 회고 템플릿
- 검증: 요구사항 추적 매트릭스 100% 커버

### 기존 파일 활용 흐름
**프롬프트**: "이 PRD로 유저스토리 분해하고 스프린트 계획 세워줘" + PRD 파일 첨부
**기대 결과**:
- 기존 PRD를 `02_prd.md`로 복사
- 스토리 모드 + 스프린트 모드 병합: story-writer + sprint-planner + reviewer 투입

### 에러 흐름
**프롬프트**: "새 기능 기획 좀 도와줘"
**기대 결과**:
- 제품/기능 불명확 → 전략가가 제품 컨텍스트 질문 후 진행
- 최소한의 정보로 전략 모드 시작, 점진적 확장

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| rice-prioritizer | `skills/rice-prioritizer/SKILL.md` | strategist, prd-writer | RICE 스코어 공식, Reach/Impact/Confidence/Effort 채점, 보완 프레임워크 |
| story-point-estimator | `skills/story-point-estimator/SKILL.md` | sprint-planner, story-writer | 피보나치 기준표, 복잡도 3차원 평가, 벨로시티 계산, 스토리 분해 기준 |
