---
name: api-designer
description: "REST/GraphQL API 설계·문서화·목업·테스트 풀 파이프라인. API 아키텍처 설계, OpenAPI/GraphQL 스키마 생성, 개발자 문서 작성, Mock 서버 및 테스트 설계를 에이전트 팀이 협업하여 수행한다. 'API 설계해줘', 'REST API', 'GraphQL API', 'API 문서화', 'API 스키마', 'OpenAPI', 'Swagger', 'API 테스트', 'API 목업', '엔드포인트 설계' 등 API 설계 전반에 이 스킬을 사용한다. 기존 API가 있는 경우에도 문서화나 테스트를 지원한다. 단, 실제 서버 구현(Express, FastAPI 등), API Gateway 배포, 모니터링 대시보드 구축은 이 스킬의 범위가 아니다."
---

# API Designer — API 설계·문서화·목업·테스트 파이프라인

API의 설계→스키마→문서→목업·테스트를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| api-architect | `agents/api-architect.md` | 리소스 모델링, 엔드포인트, 버전관리 | general-purpose |
| schema-validator | `agents/schema-validator.md` | OpenAPI/GraphQL 스키마, 타입 검증 | general-purpose |
| doc-writer | `agents/doc-writer.md` | 개발자 문서, 예시, 에러 레퍼런스 | general-purpose |
| mock-tester | `agents/mock-tester.md` | Mock 서버, 통합 테스트, 부하 시나리오 | general-purpose |
| review-auditor | `agents/review-auditor.md` | 보안, 일관성, 성능, 정합성 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **도메인**: 어떤 서비스의 API인가
   - **패러다임**: REST / GraphQL / 하이브리드
   - **주요 리소스**: 핵심 엔티티 목록
   - **인증 방식** (선택): OAuth, JWT, API Key
   - **기존 파일** (선택): 기존 스키마, 문서, 코드 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | API 설계 | api-architect | 없음 | `_workspace/01_api_design.md` |
| 2 | 스키마 생성·검증 | schema-validator | 작업 1 | `_workspace/02_schema.yaml`, `02_schema_validation.md` |
| 3a | API 문서 작성 | doc-writer | 작업 1, 2 | `_workspace/03_api_docs.md` |
| 3b | Mock 서버·테스트 | mock-tester | 작업 1, 2 | `_workspace/04_mock_tests.md` |
| 4 | API 리뷰 | review-auditor | 작업 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(문서)와 3b(테스트)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- api-architect 완료 → schema-validator에게 리소스 모델 전달, doc-writer에게 엔드포인트 전달, mock-tester에게 요청/응답 예시 전달
- schema-validator 완료 → doc-writer에게 스키마 전달, mock-tester에게 스키마 기반 예시 전달
- doc-writer ↔ mock-tester: 문서 예시와 Mock 응답 일치 여부 상호 검증
- review-auditor는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "API 설계해줘", "풀 설계" | **풀 파이프라인** | 5명 전원 |
| "API 문서만 작성해줘" (기존 API) | **문서 모드** | doc-writer + review-auditor |
| "이 OpenAPI 스키마 검증해줘" | **검증 모드** | schema-validator + review-auditor |
| "API 테스트 설계해줘" (기존 스키마) | **테스트 모드** | mock-tester + review-auditor |
| "이 API 설계 리뷰해줘" | **리뷰 모드** | review-auditor 단독 |

**기존 파일 활용**: 사용자가 스키마, 문서 등 기존 파일을 제공하면 해당 단계를 건너뛴다.

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
| 도메인 정보 부족 | API 아키텍트가 일반 CRUD 리소스로 시작, 확장 가능한 구조 설계 |
| REST vs GraphQL 미정 | REST를 기본으로, GraphQL 확장 방안 부록 제시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 기존 스키마 파싱 실패 | 수동으로 엔드포인트를 추출하여 작업 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이커머스 플랫폼의 REST API를 설계해줘. 상품, 주문, 사용자, 장바구니 리소스가 필요해"
**기대 결과**:
- API 설계: 4개 리소스, CRUD 엔드포인트, 관계 모델링, 인증 설계
- 스키마: OpenAPI 3.1 YAML, 모든 모델 타입 정의
- 문서: 빠른 시작 + 엔드포인트 레퍼런스 + 에러 코드
- 테스트: 리소스별 CRUD 테스트 + 인증 테스트 + 부하 시나리오
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 OpenAPI 스키마로 API 문서랑 테스트 만들어줘" + 스키마 파일
**기대 결과**:
- 기존 스키마를 `_workspace/02_schema.yaml`로 복사
- 문서 모드 + 테스트 모드 병합: doc-writer + mock-tester + review-auditor 투입
- api-architect, schema-validator 건너뜀

### 에러 흐름
**프롬프트**: "API 빨리 설계해줘, 블로그 플랫폼"
**기대 결과**:
- 도메인 정보 부족 → api-architect가 블로그 표준 리소스(Post, Comment, User, Tag) 추론
- 풀 파이프라인 모드로 실행
- 리뷰 보고서에 "도메인 요구사항 추론 기반 설계" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `rest-api-conventions` | api-architect | URL 네이밍, HTTP 상태 코드, 페이지네이션, 버전관리 |
| `api-error-design` | doc-writer, mock-tester | 에러 코드 체계, 에러 응답 구조, retry/fallback 전략 |
