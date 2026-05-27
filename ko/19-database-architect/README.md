# Database Architect Harness

DB 설계의 모델링→마이그레이션→인덱싱→쿼리 최적화를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── data-modeler.md         — 데이터 모델링 (ERD, 정규화, 비정규화, 관계 설계)
│   ├── migration-manager.md    — 마이그레이션 관리 (DDL, 버전관리, 롤백)
│   ├── performance-analyst.md  — 성능 분석 (인덱싱, 쿼리 최적화, 실행 계획)
│   ├── security-auditor.md     — 보안 검증 (접근 제어, 암호화, 감사 로깅)
│   └── integration-reviewer.md — 통합 리뷰 (정합성, 일관성, 운영 준비성)
├── skills/
│   ├── database-architect/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── normalization-patterns/
│   │   └── SKILL.md             — 데이터모델러 확장 (1NF~BCNF, 비정규화 전략, ERD 템플릿)
│   └── query-optimization-catalog/
│       └── SKILL.md             — 성능분석가 확장 (인덱스 전략, EXPLAIN 분석, N+1, 파티셔닝)
└── README.md                    — 이 파일
```

## 사용법

`/database-architect` 스킬을 트리거하거나, "DB 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_data_model.md` — 데이터 모델 설계 문서
- `02_migration.sql` — 마이그레이션 SQL 스크립트
- `02_migration_plan.md` — 마이그레이션 계획서
- `03_performance.md` — 성능 최적화 보고서
- `04_security.md` — 보안 검증 보고서
- `05_review_report.md` — 통합 리뷰 보고서
