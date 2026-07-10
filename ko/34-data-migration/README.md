# Data Migration Harness

데이터 마이그레이션: 소스분석→스키마매핑→변환스크립트생성→검증쿼리→롤백계획을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── source-analyst.md    — 소스 분석 (스키마 역공학, 데이터 프로파일링, 의존성 매핑)
│   ├── schema-mapper.md     — 스키마 매핑 (필드 매핑, 타입 변환, 비즈니스 규칙 정의)
│   ├── script-developer.md  — 변환 스크립트 (ETL 코드, 증분 처리, 성능 최적화)
│   ├── validation-engineer.md — 검증 엔지니어 (검증 쿼리, 데이터 정합성, 회귀 테스트)
│   └── rollback-planner.md  — 롤백 계획 (백업 전략, 롤백 스크립트, 비상 절차)
├── skills/
│   ├── data-migration/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── type-mapping-encyclopedia/
│   │   └── SKILL.md              — 데이터 타입 매핑 백과사전
│   └── data-validation-patterns/
│       └── SKILL.md              — 마이그레이션 검증 패턴 가이드
└── README.md                — 이 파일
```

## 사용법

`/data-migration` 스킬을 트리거하거나, "데이터 마이그레이션 계획 세워줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 마이그레이션 요구사항
- `01_source_analysis.md` — 소스 시스템 분석 보고서
- `02_schema_mapping.md` — 스키마 매핑 명세서
- `03_migration_scripts/` — 변환 스크립트 디렉토리
- `04_validation_suite.md` — 검증 쿼리 및 테스트 스위트
- `05_rollback_plan.md` — 롤백 및 비상 대응 계획
