# Data Pipeline Harness

데이터 파이프라인의 수집→변환→적재→품질검증→모니터링을 에이전트 팀이 협업하여 설계·구현하는 하네스.

## 구조

```

├── agents/
│   ├── etl-architect.md        — ETL 아키텍처 설계 (소스분석, 스키마설계, 파이프라인구조)
│   ├── data-quality-manager.md  — 데이터 품질 관리 (검증규칙, 프로파일링, 이상탐지)
│   ├── scheduler-engineer.md    — 스케줄링 엔지니어 (DAG설계, 의존관계, 재시도전략)
│   ├── monitoring-specialist.md — 모니터링 전문가 (메트릭, 알림, 대시보드, SLA)
│   └── pipeline-reviewer.md     — 파이프라인 리뷰어 (교차검증, 정합성, 운영준비도)
├── skills/
│   ├── data-pipeline/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── data-quality-framework/
│   │   └── SKILL.md              — 데이터 품질 프레임워크 가이드
│   └── dag-orchestration-patterns/
│       └── SKILL.md              — 파이프라인 오케스트레이션 패턴 가이드
└── README.md                    — 이 파일
```

## 사용법

`/data-pipeline` 스킬을 트리거하거나, "데이터 파이프라인 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_etl_architecture.md` — ETL 아키텍처 설계서
- `02_data_quality_plan.md` — 데이터 품질 관리 계획
- `03_scheduler_config.md` — 스케줄링 설정 및 DAG 정의
- `04_monitoring_setup.md` — 모니터링 대시보드 및 알림 설정
- `05_review_report.md` — 리뷰 보고서
- `pipeline_code/` — 파이프라인 구현 코드
