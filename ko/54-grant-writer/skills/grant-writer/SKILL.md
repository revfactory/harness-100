---
name: grant-writer
description: "보조금/지원사업 신청 풀 파이프라인. 공고 분석→사업계획서 작성→예산 편성→규정 준수 검증→제출 체크리스트를 에이전트 팀이 협업하여 생성한다. '보조금 신청', '지원사업 사업계획서', '정부 지원금', '보조금 신청서', '사업계획서 작성', '예산 편성', '지원사업 준비', 'R&D 과제 신청', '창업 지원사업', '소상공인 지원' 등 보조금/지원사업 신청 전반에 이 스킬을 사용한다. 기존 사업계획서 검토도 지원한다. 단, 실제 온라인 시스템 접속 및 제출, 증빙 서류 발급, 심사위원 대면 발표 코칭은 이 스킬의 범위가 아니다."
---

# Grant Writer — 보조금/지원사업 신청 풀 파이프라인

공고 분석→사업계획서→예산 편성→규정 준수 검증→제출 체크리스트를 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| announcement-analyst | `agents/announcement-analyst.md` | 공고 분석, 평가 기준 해부, 핵심 키워드 | general-purpose |
| plan-writer | `agents/plan-writer.md` | 사업계획서 작성, 기술성/사업성/수행역량 | general-purpose |
| budget-designer | `agents/budget-designer.md` | 예산 편성, 비목 산정, 정산 가이드 | general-purpose |
| compliance-checker | `agents/compliance-checker.md` | 규정 준수, 배점 최적화, 자격 검증 | general-purpose |
| submission-verifier | `agents/submission-verifier.md` | 서류 완비, 형식 점검, 제출 체크리스트 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **공고 정보**: 공고문, 사업명, 주관 기관 (공고문 파일 또는 URL)
    - **신청자 정보**: 기업/기관명, 업종, 규모, 핵심 기술/제품
    - **사업 아이디어**: 신청하려는 사업의 개요
    - **기존 자료** (선택): 기존 사업계획서, 재무제표, 이력서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 공고 분석 | announcement-analyst | 없음 | `_workspace/01_announcement_analysis.md` |
| 2a | 사업계획서 작성 | plan-writer | 작업 1 | `_workspace/02_business_plan.md` |
| 2b | 예산 편성 | budget-designer | 작업 1, 2a | `_workspace/03_budget_plan.md` |
| 3 | 규정 준수 검증 | compliance-checker | 작업 1, 2a, 2b | `_workspace/04_compliance_report.md` |
| 4 | 제출 검증 | submission-verifier | 작업 1~3 | `_workspace/05_submission_checklist.md` |

**팀원 간 소통 흐름:**
- announcement-analyst 완료 → plan-writer에게 평가 기준·키워드·전략 전달, budget-designer에게 예산 규정 전달
- plan-writer 완료 → budget-designer에게 추진 계획·필요 자원 전달
- compliance-checker는 사업계획서+예산서를 교차 검증. 🔴 탈락 위험 발견 시 해당 에이전트에게 수정 요청 (최대 2회)
- submission-verifier는 모든 서류의 완결성을 최종 검증

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 규정 준수 보고서의 🔴 항목이 모두 해결되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "지원사업 신청 풀로 준비해줘" | **풀 파이프라인** | 5명 전원 |
| "이 공고 분석해줘" | **공고 분석 모드** | announcement-analyst 단독 |
| "사업계획서만 작성해줘" | **계획서 모드** | announcement-analyst + plan-writer + compliance-checker |
| "예산만 편성해줘" | **예산 모드** | budget-designer + compliance-checker |
| "이 사업계획서 검토해줘" | **검토 모드** | compliance-checker + submission-verifier |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 공고문 미제공 | 사업명으로 웹 검색하여 공고문 확보 시도, 실패 시 사용자에게 요청 |
| 사업 정보 부족 | 산업/기술 기반 일반 골격 작성 후 [확인 필요] 표시 |
| 자격 미충족 발견 | 대안(컨소시엄, 공동 신청, 요건 보완) 가능 여부 분석 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 누락 명시 |
| 규정 위반 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "중소기업 기술개발사업에 AI 기반 품질검사 솔루션으로 신청하려고 해. 공고문은 여기 있어." + 공고문 첨부
**기대 결과**:
- 공고 분석: 자격 요건 체크, 평가 기준 해부(배점별), 핵심 키워드 10개+, 정책 정렬 분석
- 사업계획서: 기술성/사업성/수행역량 체계적 서술, 평가 기준 반영, 데이터 기반 근거
- 예산서: 비목별 세부 내역 + 산출 근거, 규정 비율 준수
- 규정 준수: 자격 검증, 배점 최적화 제안, 예상 점수
- 제출 체크리스트: 서류 목록, 형식 요건, 제출 가이드

### 기존 파일 활용 흐름
**프롬프트**: "이 사업계획서를 검토하고 개선점을 알려줘" + 기존 사업계획서 첨부
**기대 결과**:
- 검토 모드: compliance-checker + submission-verifier 투입
- 개선 사항을 🔴/🟡/🟢 등급으로 분류
- 배점 최적화 로드맵 제공

### 에러 흐름
**프롬프트**: "소상공인 지원사업 신청하고 싶은데 뭘 준비해야 해?"
**기대 결과**:
- 공고 미제공 → 웹 검색으로 최신 소상공인 지원사업 공고 탐색
- 여러 사업 후보 제시 후 사용자 선택 요청
- 선택 후 풀 파이프라인 실행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| compliance-checker, plan-writer | `scoring-optimizer` | 배점 해부, 고배점 서술 전략, 탈락 위험 체크리스트, 가점 획득 가이드 |
| budget-designer | `budget-rule-engine` | 비목별 상한 규정, 인건비 단가표, 산출 근거 템플릿, 정산 대비 |
