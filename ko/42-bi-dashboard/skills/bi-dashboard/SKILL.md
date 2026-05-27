---
name: bi-dashboard
description: "BI 대시보드의 데이터 웨어하우스 설계, KPI 정의, 시각화, 자동 보고를 에이전트 팀이 협업하여 한 번에 생성하는 풀 파이프라인. 'BI 대시보드 만들어줘', '대시보드 설계', 'KPI 정의해줘', '경영진 보고 대시보드', '데이터 시각화 설계', '보고서 자동화', '데이터 웨어하우스 설계', 'KPI 트리 만들어줘', '매출 대시보드', '성과 지표 체계' 등 BI 대시보드 구축 전반에 이 스킬을 사용한다. 기존 데이터 모델이나 KPI 목록이 있는 경우에도 시각화나 보고서 자동화를 지원한다. 단, 실제 BI 도구(Tableau/PowerBI/Looker) 직접 조작, 데이터베이스 인스턴스 생성, 실시간 데이터 파이프라인 운영은 이 스킬의 범위가 아니다."
---

# BI Dashboard — 데이터 분석 대시보드 풀 파이프라인

데이터 웨어하우스 설계→KPI 정의→시각화→자동 보고를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| data-engineer | `agents/data-engineer.md` | 웨어하우스 설계, ETL, 데이터 모델링 | general-purpose |
| kpi-designer | `agents/kpi-designer.md` | 지표 정의, 계산 로직, 목표치 설정 | general-purpose |
| dashboard-builder | `agents/dashboard-builder.md` | 시각화 설계, 레이아웃, 인터랙션 | general-purpose |
| report-automator | `agents/report-automator.md` | 정기 보고, 알림 설정, 배포 | general-purpose |
| bi-reviewer | `agents/bi-reviewer.md` | 정합성 검증, 데이터 흐름 QA | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **비즈니스 도메인**: 이커머스/SaaS/제조/금융/교육 등
    - **데이터 소스**: 보유 중인 DB, API, 파일 정보
    - **핵심 질문**: 대시보드로 답하고 싶은 비즈니스 질문
    - **사용자 계층**: 경영진/팀장/실무자 등 대시보드 사용자
    - **기존 자산** (선택): 기존 KPI, 데이터 모델, 보고서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 데이터 웨어하우스 설계 | data-engineer | 없음 | `_workspace/01_data_warehouse_design.md` |
| 2 | KPI 정의 | kpi-designer | 작업 1 | `_workspace/02_kpi_definition.md` |
| 3a | 대시보드 시각화 설계 | dashboard-builder | 작업 1, 2 | `_workspace/03_dashboard_spec.md` |
| 3b | 보고서 자동화 설정 | report-automator | 작업 2 | `_workspace/04_report_automation.md` |
| 4 | BI 검증 | bi-reviewer | 작업 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(대시보드)와 3b(보고서)는 **병렬 실행**한다. 둘 다 작업 2(KPI)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- data-engineer 완료 → kpi-designer에게 Measure/Dimension 목록 전달
- kpi-designer 완료 → dashboard-builder에게 KPI 우선순위·드릴다운 전달, report-automator에게 보고 주기·임계값 전달
- dashboard-builder 완료 → report-automator에게 스냅샷 캡처 방식 전달
- bi-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

검증자의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 데이터 웨어하우스 설계서 — `01_data_warehouse_design.md`
    - KPI 정의서 — `02_kpi_definition.md`
    - 대시보드 명세 — `03_dashboard_spec.md`
    - 자동 보고 설정서 — `04_report_automation.md`
    - 검증 보고서 — `05_review_report.md`

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "BI 대시보드 만들어줘", "풀 대시보드 설계" | **풀 파이프라인** | 5명 전원 |
| "KPI만 정의해줘" | **KPI 모드** | data-engineer + kpi-designer + reviewer |
| "이 KPI로 대시보드 설계해줘" (기존 KPI) | **시각화 모드** | dashboard-builder + reviewer |
| "보고서 자동화 설정해줘" | **보고서 모드** | report-automator + reviewer |
| "이 대시보드 설계 검토해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 KPI 목록, 데이터 모델 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물명}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 데이터 소스 정보 부재 | 도메인별 표준 스키마로 설계, 커스터마이징 포인트 명시 |
| 비즈니스 목표 불명확 | 도메인별 표준 KPI 프레임워크 제안 후 선택 유도 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 검증 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이커머스 쇼핑몰의 매출·고객·재고 관리 BI 대시보드를 설계해줘"
**기대 결과**:
- 데이터 모델: 이커머스 Star Schema (fact_orders, dim_product, dim_customer, dim_date)
- KPI: 구매 퍼널(방문→장바구니→결제), 매출, 객단가, 재구매율, 재고회전율
- 대시보드: Executive Summary + Sales + Customer + Inventory 4탭
- 보고서: 일일 매출요약, 주간 팀리포트, 월간 경영보고
- 검증: 전 구간 정합성 매트릭스 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 KPI 목록으로 대시보드 레이아웃 설계해줘" + KPI 파일 첨부
**기대 결과**:
- 기존 KPI를 `_workspace/02_kpi_definition.md`로 복사
- 시각화 모드: dashboard-builder + reviewer 투입
- data-engineer, kpi-designer는 건너뜀

### 에러 흐름
**프롬프트**: "우리 회사 대시보드 하나 만들어줘"
**기대 결과**:
- 도메인/데이터 소스 불명 → 일반적인 비즈니스 도메인 3개 제안 후 선택 유도
- 선택 후 해당 도메인 표준 스키마 기반으로 풀 파이프라인 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| kpi-tree-builder | `skills/kpi-tree-builder/SKILL.md` | kpi-designer, dashboard-builder | KPI 트리 분해 방법론, 도메인별 템플릿, 임계값 설정, 드릴다운 설계 |
| chart-selector | `skills/chart-selector/SKILL.md` | dashboard-builder, kpi-designer | 차트 유형 의사결정 트리, 차트별 규칙, 색상 팔레트, 레이아웃 원칙 |
