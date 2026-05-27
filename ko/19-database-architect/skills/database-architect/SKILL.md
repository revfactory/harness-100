---
name: database-architect
description: "DB 설계 풀 파이프라인. 데이터 모델링→마이그레이션→인덱싱→쿼리 최적화→보안 검증을 에이전트 팀이 협업하여 수행한다. 'DB 설계해줘', '데이터베이스 모델링', '테이블 설계', 'ERD', '마이그레이션', '쿼리 최적화', '인덱스 설계', 'SQL 스키마', 'PostgreSQL 설계', 'MySQL 설계' 등 DB 설계 전반에 이 스킬을 사용한다. 기존 스키마가 있는 경우에도 최적화나 보안 감사를 지원한다. 단, 실제 DB 서버 설치/운영, 클라우드 인프라 프로비저닝, 모니터링 대시보드 구축은 이 스킬의 범위가 아니다."
---

# Database Architect — DB 설계 풀 파이프라인

DB의 모델링→마이그레이션→인덱싱→쿼리 최적화→보안 검증을 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| data-modeler | `agents/data-modeler.md` | ERD, 정규화, 관계 설계 | general-purpose |
| migration-manager | `agents/migration-manager.md` | DDL, 버전관리, 롤백 | general-purpose |
| performance-analyst | `agents/performance-analyst.md` | 인덱싱, 쿼리 최적화 | general-purpose |
| security-auditor | `agents/security-auditor.md` | 접근 제어, 암호화, 감사 | general-purpose |
| integration-reviewer | `agents/integration-reviewer.md` | 정합성, 운영 준비성 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **도메인**: 어떤 서비스의 DB인가
   - **DBMS**: PostgreSQL / MySQL / MongoDB / DynamoDB
   - **핵심 엔티티**: 주요 데이터 대상
   - **예상 규모** (선택): 데이터 건수, TPS
   - **기존 파일** (선택): 기존 스키마, ERD, SQL 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 데이터 모델링 | data-modeler | 없음 | `_workspace/01_data_model.md` |
| 2 | 마이그레이션 생성 | migration-manager | 작업 1 | `_workspace/02_migration.sql`, `02_migration_plan.md` |
| 3a | 성능 최적화 | performance-analyst | 작업 1, 2 | `_workspace/03_performance.md` |
| 3b | 보안 검증 | security-auditor | 작업 1, 2 | `_workspace/04_security.md` |
| 4 | 통합 리뷰 | integration-reviewer | 작업 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(성능)와 3b(보안)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- data-modeler 완료 → migration-manager에게 DDL 기반 전달, performance-analyst에게 액세스 패턴 전달, security-auditor에게 민감 데이터 전달
- migration-manager 완료 → performance-analyst에게 인덱스 DDL 전달, security-auditor에게 권한 DDL 전달
- performance-analyst ↔ security-auditor: 성능 최적화가 보안을 훼손하지 않는지 상호 검증
- integration-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "DB 설계해줘", "풀 설계" | **풀 파이프라인** | 5명 전원 |
| "ERD만 그려줘", "테이블 설계만" | **모델링 모드** | data-modeler + integration-reviewer |
| "이 스키마 최적화해줘" (기존 SQL) | **최적화 모드** | performance-analyst + integration-reviewer |
| "DB 보안 감사해줘" (기존 DB) | **보안 모드** | security-auditor + integration-reviewer |
| "이 스키마 리뷰해줘" | **리뷰 모드** | integration-reviewer 단독 |

**기존 파일 활용**: 사용자가 스키마, ERD 등을 제공하면 해당 단계를 건너뛴다.

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
| DBMS 미지정 | PostgreSQL을 기본으로, 다른 DBMS 호환 노트 추가 |
| 도메인 정보 부족 | 데이터 모델러가 일반 패턴으로 시작, 가정 사항 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 기존 스키마 파싱 실패 | 수동 분석 후 데이터 모델 재구성 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이커머스 플랫폼의 PostgreSQL DB를 설계해줘. 사용자, 상품, 주문, 결제, 리뷰 테이블이 필요해. 일 주문 10만 건 예상"
**기대 결과**:
- 모델: 5개 핵심 테이블 + 중간 테이블, 3NF 정규화, ERD
- 마이그레이션: 순차적 DDL + 롤백 스크립트 + 시드 데이터
- 성능: 인덱스 전략, 주요 쿼리 최적화, 파티셔닝 설계
- 보안: RBAC, PII 암호화, 감사 로깅, 백업 전략
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 SQL 스키마의 성능을 최적화해줘" + SQL 파일
**기대 결과**:
- 기존 스키마를 `_workspace/02_migration.sql`로 복사
- 최적화 모드: performance-analyst + integration-reviewer 투입
- data-modeler, migration-manager, security-auditor 건너뜀

### 에러 흐름
**프롬프트**: "DB 설계해줘, 블로그 플랫폼"
**기대 결과**:
- 규모/DBMS 미정 → data-modeler가 PostgreSQL + 블로그 표준 엔티티(Post, User, Comment, Tag) 추론
- 풀 파이프라인 모드로 실행
- 리뷰 보고서에 "요구사항 추론 기반 설계" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `normalization-patterns` | data-modeler | 1NF~BCNF 판별, 비정규화 전략, 도메인별 ERD 템플릿 |
| `query-optimization-catalog` | performance-analyst | 인덱스 전략, EXPLAIN 분석, N+1 해결, 파티셔닝 |
