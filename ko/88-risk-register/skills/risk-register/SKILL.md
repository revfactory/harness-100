---
name: risk-register
description: "프로젝트 리스크 관리대장의 리스크식별, 확률·영향평가, 대응전략수립, 모니터링계획, 상태보고서를 에이전트 팀이 협업하여 한 번에 생성하는 풀 파이프라인. '리스크 관리', '리스크 등록부', '위험 관리대장', 'risk register', '리스크 매트릭스', '리스크 평가', '리스크 대응', '프로젝트 위험 관리', '리스크 모니터링', '리스크 보고서', 'EMV 분석', '리스크 히트맵' 등 프로젝트 리스크 관리 전반에 이 스킬을 사용한다. 단, 보험 계리, 금융 리스크(VaR/CVaR), 실시간 리스크 대시보드 시스템 구축, ERM(전사 리스크 관리) 소프트웨어 연동은 이 스킬의 범위가 아니다."
---

# Risk Register — 프로젝트 리스크 관리대장 풀 파이프라인

프로젝트 리스크의 식별→평가→대응→모니터링→보고를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| risk-identifier | `agents/risk-identifier.md` | 리스크 식별, RBS | general-purpose |
| assessment-analyst | `agents/assessment-analyst.md` | 확률·영향 평가, 매트릭스 | general-purpose |
| response-strategist | `agents/response-strategist.md` | 대응 전략, 비용-효과 | general-purpose |
| monitoring-planner | `agents/monitoring-planner.md` | KRI, 트리거, 모니터링 | general-purpose |
| report-writer | `agents/report-writer.md` | 대시보드, 통합 보고서 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **프로젝트 개요**: 명칭, 목표, 규모, 기간
    - **프로젝트 유형**: IT/건설/R&D/제조/서비스 등
    - **이해관계자**: 핵심 이해관계자와 기대사항
    - **제약 조건** (선택): 예산, 일정, 기술, 규제
    - **기존 자료** (선택): 기존 리스크 목록, 과거 교훈
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 해당 Phase를 조정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 리스크 식별 | identifier | 없음 | `_workspace/01_risk_identification.md` |
| 2 | 확률·영향 평가 | analyst | 작업 1 | `_workspace/02_risk_assessment.md` |
| 3 | 대응 전략 수립 | strategist | 작업 1, 2 | `_workspace/03_response_strategy.md` |
| 4 | 모니터링 계획 | planner | 작업 2, 3 | `_workspace/04_monitoring_plan.md` |
| 5 | 상태 보고서 | writer | 작업 1, 2, 3, 4 | `_workspace/05_status_report.md` |

**팀원 간 소통 흐름:**
- identifier 완료 → analyst에게 리스크 목록·RBS, strategist에게 오너·의존성 전달
- analyst 완료 → strategist에게 우선순위·EMV, planner에게 점수 기준 전달
- strategist 완료 → planner에게 트리거·성공지표, writer에게 대응 요약 전달
- planner 완료 → writer에게 모니터링 일정·KRI 전달
- writer는 모든 산출물을 교차 검증, 불일치 발견 시 해당 에이전트에 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. writer의 정합성 검증 결과를 반영한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "리스크 관리대장 전체 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "리스크 식별만 해줘" | **식별 모드** | identifier 단독 |
| "이 리스크 목록 평가해줘" (기존 목록) | **평가 모드** | analyst + strategist + writer |
| "리스크 대응 전략만 수립해줘" | **대응 모드** | strategist + writer |
| "리스크 현황 보고서 만들어줘" (기존 등록부) | **보고 모드** | writer 단독 |

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
| 프로젝트 정보 부족 | identifier가 산업별 일반 리스크 템플릿 제공, "[맞춤화 필요]" 명시 |
| 정량 데이터 없음 | analyst가 정성 평가로 대체, "[데이터 확보 후 재평가]" 표기 |
| 웹 검색 실패 | 일반 지식 기반 리스크 도출, 보고서에 "참조 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 누락 명시 |
| 정합성 불일치 | writer가 수정 요청 → 재작업 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "6개월짜리 사내 ERP 시스템 교체 프로젝트의 리스크 관리대장을 만들어줘. 예산 10억, 팀원 15명이야."
**기대 결과**:
- 식별: RBS 6개 카테고리, 리스크 20~30건, 연쇄 리스크 맵
- 평가: 5×5 매트릭스, EMV 산정, Critical 3~5건
- 대응: Critical은 회피/완화, 비용-효과 분석, 잔여 리스크
- 모니터링: KRI 10개+, 주간/월간 리뷰, 트리거 조건
- 보고서: 경영진 1페이지, 히트맵, Top 5 리스크

### 기존 자료 활용 흐름
**프롬프트**: "이 리스크 목록에 대해 대응 전략을 수립하고 보고서를 만들어줘" + 리스크 목록 파일
**기대 결과**:
- 기존 목록을 `_workspace/01_risk_identification.md`로 복사
- 평가 모드: analyst + strategist + writer 투입
- identifier는 건너뜀

### 에러 흐름
**프롬프트**: "리스크 관리대장 만들어줘, 프로젝트는 아직 기획 단계야"
**기대 결과**:
- identifier가 "[기획 단계]" 명시 후 일반적 프로젝트 리스크 + 기획 단계 특화 리스크 도출
- 정량 데이터 부족 → analyst가 정성 평가 중심으로 작업
- 보고서에 "기획 단계 — 상세화 시점에 재평가 필요" 권고

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| risk-scoring-matrix | `skills/risk-scoring-matrix/SKILL.md` | assessment-analyst | 5x5 매트릭스, RBS, EMV, 민감도 분석 |
| risk-response-patterns | `skills/risk-response-patterns/SKILL.md` | response-strategist, monitoring-planner | 4대 대응 전략, 대응 계획서, 모니터링 |
