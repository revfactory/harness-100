---
name: data-pipeline
description: "데이터 파이프라인의 수집, 변환, 적재, 품질검증, 모니터링을 에이전트 팀이 협업하여 설계·구현하는 풀 파이프라인. '데이터 파이프라인 설계해줘', 'ETL 파이프라인 구축', '데이터 수집 자동화', '데이터 웨어하우스 파이프라인', 'ELT 설계', '배치 파이프라인', '스트리밍 파이프라인', 'Airflow DAG 만들어줘', 'dbt 모델 설계', '데이터 품질 검증 체계' 등 데이터 파이프라인 설계·구축 전반에 이 스킬을 사용한다. 기존 파이프라인의 품질 검증이나 모니터링만 필요한 경우에도 지원한다. 단, 실시간 스트리밍 엔진(Flink/Spark Streaming) 직접 실행, 클라우드 인프라 프로비저닝, 데이터베이스 관리자(DBA) 업무는 이 스킬의 범위가 아니다."
---

# Data Pipeline — 데이터 파이프라인 설계·구현

데이터 파이프라인의 수집→변환→적재→품질검증→모니터링을 에이전트 팀이 협업하여 한 번에 설계·구현한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| etl-architect | `agents/etl-architect.md` | 소스분석, 스키마설계, 파이프라인구조 | general-purpose |
| data-quality-manager | `agents/data-quality-manager.md` | 검증규칙, 프로파일링, 이상탐지 | general-purpose |
| scheduler-engineer | `agents/scheduler-engineer.md` | DAG설계, 의존관계, 재시도전략 | general-purpose |
| monitoring-specialist | `agents/monitoring-specialist.md` | 메트릭, 알림, 대시보드, SLA | general-purpose |
| pipeline-reviewer | `agents/pipeline-reviewer.md` | 교차검증, 정합성, 운영준비도 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **데이터 소스**: 원천 시스템(DB, API, 파일, 스트리밍)
    - **타깃 시스템**: 데이터 웨어하우스, 데이터 레이크, 분석 플랫폼
    - **비즈니스 요구**: 리포팅 주기, SLA, 데이터 신선도
    - **기술 제약** (선택): 클라우드 벤더, 기존 스택, 예산
    - **기존 파일** (선택): 사용자가 제공한 스키마, 쿼리, 설정 파일
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | ETL 아키텍처 설계 | etl-architect | 없음 | `_workspace/01_etl_architecture.md` |
| 2a | 데이터 품질 계획 | data-quality-manager | 작업 1 | `_workspace/02_data_quality_plan.md` |
| 2b | 스케줄링 설정 | scheduler-engineer | 작업 1 | `_workspace/03_scheduler_config.md` |
| 3 | 모니터링 설정 | monitoring-specialist | 작업 1, 2a, 2b | `_workspace/04_monitoring_setup.md` |
| 4 | 파이프라인 리뷰 | pipeline-reviewer | 작업 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(품질)와 2b(스케줄링)는 **병렬 실행**한다. 둘 다 작업 1(아키텍처)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- etl-architect 완료 → quality-manager에게 스키마·비즈니스 규칙 전달, scheduler에게 의존관계·리소스 요구량 전달, monitoring에게 핵심 메트릭 전달
- quality-manager 완료 → scheduler에게 검증 작업 삽입 위치·중단 조건 전달, monitoring에게 품질 메트릭·SLA 전달
- scheduler 완료 → monitoring에게 DAG 실행 메트릭 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - ETL 아키텍처 — `01_etl_architecture.md`
    - 품질 관리 계획 — `02_data_quality_plan.md`
    - 스케줄링 설정 — `03_scheduler_config.md`
    - 모니터링 설정 — `04_monitoring_setup.md`
    - 리뷰 보고서 — `05_review_report.md`
    - 파이프라인 코드 — `pipeline_code/`

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "데이터 파이프라인 설계해줘", "ETL 전체 구축" | **풀 파이프라인** | 5명 전원 |
| "데이터 품질 검증 체계 만들어줘" | **품질 모드** | etl-architect + quality-manager + reviewer |
| "Airflow DAG 설계해줘" | **스케줄 모드** | etl-architect + scheduler + reviewer |
| "파이프라인 모니터링 대시보드 구성해줘" | **모니터링 모드** | monitoring + reviewer |
| "이 파이프라인 리뷰해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 스키마, DAG 코드 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

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
| 소스 접속 정보 부재 | 아키텍트가 placeholder 기반 템플릿으로 진행, 산출물에 "접속 정보 미입력" 명시 |
| 기술 스택 불명 | AWS/GCP/Azure 3대 클라우드별 옵션 병기, 사용자 선택 유도 |
| 볼륨 정보 부재 | 소(일 1만건)·중(일 100만건)·대(일 1억건) 3단계 아키텍처 제시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "PostgreSQL 주문 데이터를 BigQuery 데이터 웨어하우스로 적재하는 일일 배치 파이프라인을 설계해줘. Airflow 기반으로."
**기대 결과**:
- ETL 아키텍처: PostgreSQL CDC/증분 로드 전략, Raw→Staging→Curated→Analytics 4레이어
- 품질 계획: 주문 데이터 특성 기반 P0/P1/P2 검증 규칙, 매출 집계 cross-check
- 스케줄링: Airflow DAG 코드(extract→stage→curate→analytics→quality_check), 재시도 정책
- 모니터링: 일일 적재 건수, 지연시간, 품질 점수 대시보드
- 리뷰: 전항목 정합성 매트릭스

### 기존 파일 활용 흐름
**프롬프트**: "이 dbt 모델 파일들에 대해 데이터 품질 검증과 모니터링을 설계해줘" + dbt 모델 파일 첨부
**기대 결과**:
- 기존 dbt 모델을 `_workspace/`에 복사
- 품질 모드 + 모니터링 모드 병합: quality-manager + monitoring + reviewer 투입
- etl-architect, scheduler는 건너뜀

### 에러 흐름
**프롬프트**: "데이터 파이프라인 빨리 설계해줘, 소스는 여러 개인데 아직 정확히 모름"
**기대 결과**:
- 아키텍트가 일반적인 멀티소스 파이프라인 템플릿으로 진행
- 소스별 커넥터 placeholder 포함, 볼륨별 3단계 옵션 제시
- 리뷰 보고서에 "소스 정보 미확정 — 확정 후 재설계 필요" 명시


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| data-quality-framework | `skills/data-quality-framework/SKILL.md` | data-quality-manager | 품질 6차원, Great Expectations, dbt tests, 데이터 계약 |
| dag-orchestration-patterns | `skills/dag-orchestration-patterns/SKILL.md` | scheduler-engineer | Airflow DAG 패턴, 멱등성, 재시도, 백필, 의존관계 |
