---
name: data-migration
description: "데이터 마이그레이션의 소스 분석, 스키마 매핑, 변환 스크립트 생성, 검증 쿼리 설계, 롤백 계획을 에이전트 팀이 협업하여 수행하는 풀 마이그레이션 파이프라인. '데이터 마이그레이션', 'DB 이관', '데이터 이전', '스키마 변환', '데이터베이스 이관 계획', 'ETL 스크립트', '데이터 이행', 'DB 마이그레이션 검증', '시스템 전환' 등 데이터 마이그레이션 전반에 이 스킬을 사용한다. 단, 실시간 CDC 스트리밍 구축, 클라우드 인프라 프로비저닝, 애플리케이션 코드 마이그레이션은 이 스킬의 범위가 아니다."
---

# Data Migration — 데이터 마이그레이션 풀 파이프라인

소스분석→스키마매핑→변환스크립트→검증쿼리→롤백계획을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| source-analyst | `agents/source-analyst.md` | 소스 분석, 데이터 프로파일링 | general-purpose |
| schema-mapper | `agents/schema-mapper.md` | 스키마 매핑, 변환 규칙 설계 | general-purpose |
| script-developer | `agents/script-developer.md` | ETL 스크립트, 성능 최적화 | general-purpose |
| validation-engineer | `agents/validation-engineer.md` | 검증 쿼리, 정합성 테스트 | general-purpose |
| rollback-planner | `agents/rollback-planner.md` | 롤백 계획, 비상 대응 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **소스 시스템**: DBMS 종류, 버전, 접속 정보, 스키마 범위
    - **타깃 시스템**: DBMS 종류, 버전, 기존 스키마 유무
    - **마이그레이션 범위**: 전체/부분, 대상 테이블, 데이터 기간
    - **제약 조건**: 다운타임 허용 시간, 성능 요구사항, 일정
2. `_workspace/` 디렉토리와 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 소스 분석 | source-analyst | 없음 | `01_source_analysis.md` |
| 2 | 스키마 매핑 | schema-mapper | 작업 1 | `02_schema_mapping.md` |
| 3a | 변환 스크립트 | script-developer | 작업 2 | `03_migration_scripts/` |
| 3b | 검증 스위트 | validation-engineer | 작업 1, 2 | `04_validation_suite.md` |
| 4 | 롤백 계획 | rollback-planner | 작업 1, 2, 3a, 3b | `05_rollback_plan.md` |

작업 3a(스크립트)와 3b(검증)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- source-analyst 완료 → schema-mapper에게 소스 스키마 전달, script-developer에게 볼륨·순서 전달, validation-engineer에게 무결성 규칙 전달
- schema-mapper 완료 → script-developer에게 매핑 명세 전달, validation-engineer에게 변환 규칙 전달, rollback-planner에게 역매핑 가능 여부 전달
- script-developer 완료 → rollback-planner에게 트랜잭션 경계 전달
- validation-engineer 완료 → rollback-planner에게 롤백 트리거 조건 전달
- rollback-planner는 전체 계획을 수립하고 위험 항목을 각 에이전트에 피드백

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 산출물을 확인한다
2. 산출물 간 정합성을 검증한다 (매핑↔스크립트, 검증↔매핑, 롤백↔스크립트)
3. 최종 마이그레이션 실행 체크리스트를 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "마이그레이션 전체 계획" | **풀 파이프라인** | 5명 전원 |
| "소스 DB 분석만" | **분석 모드** | source-analyst 단독 |
| "스키마 매핑만 해줘" | **매핑 모드** | source-analyst + schema-mapper |
| "ETL 스크립트만 생성" | **스크립트 모드** | script-developer (매핑 전제) |
| "검증 쿼리만 만들어줘" | **검증 모드** | validation-engineer (매핑 전제) |
| "롤백 계획만 세워줘" | **롤백 모드** | rollback-planner (전체 분석 전제) |

**기존 파일 활용**: 사용자가 기존 DDL, ERD, 스키마 매핑 문서 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 산출물 문서 |
| 스크립트 기반 | `_workspace/03_migration_scripts/` | 실행 가능한 코드 |
| 메시지 기반 | SendMessage | 핵심 정보 전달, 피드백 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| DB 접속 불가 | DDL/ERD 문서 기반 분석으로 대체 |
| 타깃 스키마 미정 | 소스 기반 추천 타깃 스키마 자동 생성 |
| 호환 불가 타입 | 중간 타입 경유 2단계 변환 제안 |
| 대용량 테이블(>1억행) | 파티션 단위 마이그레이션 전략 |
| 에이전트 실패 | 1회 재시도 후 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "MySQL 5.7에서 PostgreSQL 16으로 전자상거래 DB를 마이그레이션하는 계획을 세워줘"
**기대 결과**:
- 소스 분석: MySQL 스키마 역공학, 데이터 프로파일링, 의존성 그래프
- 스키마 매핑: MySQL→PostgreSQL 타입 매핑, 자동증가→시퀀스 변환, 문자셋 처리
- 스크립트: Python ETL 코드, 배치 처리, 인덱스 관리 SQL
- 검증: 행 수, 체크섬, FK 무결성, 변환 정확성 쿼리
- 롤백: 백업 전략, Go/No-Go 기준, 단계별 롤백 절차

### 기존 파일 활용 흐름
**프롬프트**: "이 DDL 파일로 타깃 PostgreSQL 매핑만 해줘"
**기대 결과**:
- DDL 파싱으로 source-analyst가 스키마 분석
- schema-mapper가 PostgreSQL 타깃 매핑 생성
- script-developer, validation-engineer, rollback-planner는 미투입

### 에러 흐름
**프롬프트**: "Oracle에서 MongoDB로 마이그레이션해줘" (RDBMS→NoSQL)
**기대 결과**:
- source-analyst가 관계형 구조 분석
- schema-mapper가 RDBMS→Document 모델 변환 전략 제시 (정규화 해제, 임베딩 vs 참조)
- 비가역 변환 다수 발생 → rollback-planner가 아카이브 보존 전략 수립


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| type-mapping-encyclopedia | `skills/type-mapping-encyclopedia/SKILL.md` | schema-mapper | MySQL/Oracle/PostgreSQL 타입 매핑, RDBMS→NoSQL, 문자셋 변환 |
| data-validation-patterns | `skills/data-validation-patterns/SKILL.md` | validation-engineer | 5단계 검증(건수→스키마→값→참조→비즈니스), Go/No-Go 체크리스트 |
