---
name: gov-funding-plan
description: "정부지원사업 사업계획서의 공고요건 분석, 기술성·사업성 작성, 예산 편성, 증빙 준비, 제출 검증을 에이전트 팀이 협업하여 한 번에 생성하는 풀 파이프라인. '정부지원사업 사업계획서 써줘', '정부과제 지원', 'R&D 사업계획서', 'TIPS 사업계획서', '창업성장기술개발 사업계획서', '정부 R&D 예산 편성', '공고 분석해줘', '기술성 파트 작성', '사업성 파트 작성', '정부과제 예산', '중기부 과제 지원' 등 정부지원사업 사업계획서 작성 전반에 이 스킬을 사용한다. 기존 기술 계획이나 사업 계획이 있는 경우에도 예산 편성이나 검증을 지원한다. 단, 실제 온라인 시스템 제출, 법인 서류 발급, 회계 처리, 특허 출원은 이 스킬의 범위가 아니다."
---

# Gov Funding Plan — 정부지원사업 사업계획서 풀 파이프라인

공고요건분석→기술성·사업성작성→예산편성→증빙준비→제출검증을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| announcement-analyst | `agents/announcement-analyst.md` | 공고 요건 분석, 평가 기준 | general-purpose |
| tech-writer | `agents/tech-writer.md` | 기술성 파트 작성 | general-purpose |
| biz-writer | `agents/biz-writer.md` | 사업성 파트 작성 | general-purpose |
| budget-planner | `agents/budget-planner.md` | 예산 편성, 증빙 가이드 | general-purpose |
| submission-reviewer | `agents/submission-reviewer.md` | 교차 검증, 제출 준비 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **공고문**: 지원하려는 정부지원사업 공고 내용 (URL 또는 텍스트)
    - **기업 정보**: 업종, 업력, 매출, 인력, 보유 기술
    - **개발 과제**: 개발하려는 기술/제품/서비스
    - **기존 자산** (선택): 기존 사업계획서, 기술 문서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 해당 단계를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 공고 요건 분석 | announcement-analyst | 없음 | `_workspace/01_announcement_analysis.md` |
| 2a | 기술성 작성 | tech-writer | 작업 1 | `_workspace/02_tech_proposal.md` |
| 2b | 사업성 작성 | biz-writer | 작업 1 | `_workspace/03_biz_proposal.md` |
| 3 | 예산 편성 | budget-planner | 작업 1, 2a, 2b | `_workspace/04_budget_plan.md` |
| 4 | 제출 검증 | submission-reviewer | 작업 1~3 | `_workspace/05_review_report.md` |

작업 2a(기술성)와 2b(사업성)는 **병렬 실행**한다. 둘 다 작업 1(공고 분석)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- announcement-analyst 완료 → tech-writer에게 기술성 평가 기준·배점·키워드 전달, biz-writer에게 사업성 평가 기준·정책 키워드 전달, budget-planner에게 예산 제한 전달
- tech-writer 완료 → biz-writer에게 기술 차별화 포인트 전달, budget-planner에게 인력·장비 소요 전달
- biz-writer 완료 → budget-planner에게 사업화 투자 계획 전달
- submission-reviewer는 모든 산출물 교차 검증. 🔴 필수 수정 발견 시 수정 요청 → 재작업 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "사업계획서 써줘", "정부과제 지원" | **풀 파이프라인** | 5명 전원 |
| "기술성만 써줘" | **기술성 모드** | announcement-analyst + tech-writer + reviewer |
| "사업성만 써줘" | **사업성 모드** | announcement-analyst + biz-writer + reviewer |
| "예산만 편성해줘" | **예산 모드** | announcement-analyst + budget-planner + reviewer |
| "이 사업계획서 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 공고문 미제공 | 대표적 정부 R&D 사업(TIPS, 창업성장기술개발 등) 일반 양식 기반으로 작성 |
| 기업 정보 부족 | 역할별 필요 역량만 기술, [기입필요] 표시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 검증 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "TIPS 사업에 AI 기반 물류 최적화 솔루션으로 지원하려고 해. 사업계획서 써줘"
**기대 결과**:
- 공고 분석: TIPS 평가 기준, 배점, 제출 서류 체크리스트
- 기술성: AI/물류 기술 개발 목표, 차별성, 추진 체계
- 사업성: 물류 시장 규모, 사업화 전략, 매출 계획
- 예산: 2억원 규모 비목별 편성, 증빙 가이드
- 검증: 전 항목 정합성 확인, 예상 점수

### 기존 파일 활용 흐름
**프롬프트**: "이 기술 계획서로 예산만 편성해줘" + 기술 문서 첨부
**기대 결과**:
- 기존 문서를 `02_tech_proposal.md`로 복사
- 예산 모드: announcement-analyst + budget-planner + reviewer 투입

### 에러 흐름
**프롬프트**: "정부과제 써줘, 어떤 사업이 좋을지 모르겠어"
**기대 결과**:
- 기업 정보와 기술 분야 확인 후 적합한 정부지원사업 3개 추천
- 사용자 선택 후 풀 파이프라인 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| budget-standard-checker | `skills/budget-standard-checker/SKILL.md` | budget-planner, submission-reviewer | 비목별 편성 기준, 인건비/장비/간접비 규정, 사업별 특이사항 |
| scoring-optimizer | `skills/scoring-optimizer/SKILL.md` | tech-writer, biz-writer, submission-reviewer | 평가 항목별 고득점 전략, 감점 방지, 키워드 분석, 발표 평가 대비 |
