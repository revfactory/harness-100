---
name: api-client-generator
description: "API 클라이언트 SDK를 자동 생성하는 풀 파이프라인. API 스펙(OpenAPI/GraphQL/gRPC) 파싱, 타입 생성, 클라이언트 코드, 테스트, 사용 문서를 에이전트 팀이 협업하여 생성한다. 'API 클라이언트 만들어줘', 'SDK 생성', 'OpenAPI에서 클라이언트', 'API 래퍼', 'REST 클라이언트', 'GraphQL 클라이언트', 'API 타입 생성', 'Swagger에서 SDK' 등 API 클라이언트 SDK 생성 전반에 이 스킬을 사용한다. 단, API 서버 구현, API 게이트웨이 설정, API 모니터링 대시보드 구축은 이 스킬의 범위가 아니다."
---

# API Client Generator — SDK 생성 풀 파이프라인

API 스펙 파싱→타입 생성→클라이언트 코드→테스트→문서를 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| spec-parser | `agents/spec-parser.md` | API 스펙 분석, 엔드포인트 추출 | general-purpose |
| type-generator | `agents/type-generator.md` | 타입 정의 생성 | general-purpose |
| sdk-developer | `agents/sdk-developer.md` | 클라이언트 SDK 코드 개발 | general-purpose |
| test-engineer | `agents/test-engineer.md` | 테스트 코드 작성 | general-purpose |
| doc-writer | `agents/doc-writer.md` | 사용 문서 작성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **API 스펙**: 파일 경로/URL, 스펙 포맷(OpenAPI/GraphQL/gRPC)
    - **타깃 언어**: TypeScript, Python, Go, Java 등
    - **SDK 이름**: 패키지/모듈명
    - **설정** (선택): 인증 방식 우선순위, 네이밍 컨벤션, 추가 기능
2. `_workspace/` 디렉토리와 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. API 스펙 파일을 `_workspace/`에 복사한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 스펙 분석 | spec-parser | 없음 | `01_spec_analysis.md` |
| 2 | 타입 생성 | type-generator | 작업 1 | `02_types/` |
| 3 | SDK 개발 | sdk-developer | 작업 1, 2 | `03_client/` |
| 4a | 테스트 작성 | test-engineer | 작업 2, 3 | `04_tests/` |
| 4b | 문서 작성 | doc-writer | 작업 1, 3 | `05_docs/` |

작업 4a(테스트)와 4b(문서)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- spec-parser 완료 → type-generator에게 모델 상세 전달, sdk-developer에게 엔드포인트 그룹핑 전달
- type-generator 완료 → sdk-developer에게 타입 임포트 정보 전달, test-engineer에게 팩토리 데이터 전달
- sdk-developer 완료 → test-engineer에게 공개 API 목록 전달, doc-writer에게 사용 예시 전달
- test-engineer/doc-writer → 코드/문서 불일치 발견 시 sdk-developer에게 수정 요청

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 코드-타입-테스트-문서 간 정합성을 최종 검증한다
3. 빌드/테스트 실행 명령어와 함께 최종 요약을 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "SDK 전체 생성", "풀 클라이언트" | **풀 파이프라인** | 5명 전원 |
| "타입만 생성해줘" | **타입 모드** | spec-parser + type-generator |
| "클라이언트 코드만" | **코드 모드** | spec-parser + type-generator + sdk-developer |
| "테스트만 작성" (기존 SDK 있음) | **테스트 모드** | test-engineer 단독 |
| "문서만 작성" (기존 SDK 있음) | **문서 모드** | doc-writer 단독 |
| "스펙 분석만" | **분석 모드** | spec-parser 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 코드, 타입, 테스트, 문서 |
| 메시지 기반 | SendMessage | 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 스펙 파싱 실패 | 문법 오류 위치 보고, 파싱 가능 부분만 진행 |
| 불완전한 스펙 | 타입 추론으로 보완, "추론됨" 표시 |
| 순환 참조 | lazy reference 패턴 자동 적용 |
| 비표준 인증 | 커스텀 인터셉터 확장 포인트 제공 |
| 에이전트 실패 | 1회 재시도 후 해당 산출물 없이 진행 |
| 코드-문서 불일치 | doc-writer/test-engineer가 sdk-developer에게 수정 요청 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 OpenAPI 3.1 스펙으로 TypeScript SDK를 만들어줘"
**기대 결과**:
- 스펙 분석: 엔드포인트 그룹핑, 모델 목록, 인증 방식 식별
- 타입: TypeScript interface/type, enum, 유니온 타입, 직렬화 헬퍼
- SDK: 리소스 기반 클라이언트 클래스, 인증, 페이지네이션, 재시도
- 테스트: 리소스별 단위 테스트, 인증 통합 테스트, 목 서버
- 문서: README, 빠른 시작, API 레퍼런스, 코드 예제

### 기존 파일 활용 흐름
**프롬프트**: "이 Swagger 파일에서 Python 타입만 뽑아줘"
**기대 결과**:
- spec-parser가 스키마 분석
- type-generator가 Python dataclass/Pydantic 모델 생성
- sdk-developer, test-engineer, doc-writer는 미투입

### 에러 흐름
**프롬프트**: "이 API의 SDK를 만들어줘" (불완전한 스펙, 응답 타입 미정의 다수)
**기대 결과**:
- spec-parser가 불완전한 부분을 목록화하여 보고
- type-generator가 추론 가능한 범위에서 타입 생성, "추론됨" 주석 추가
- sdk-developer가 런타임 타입 체크 레이어를 추가
- doc-writer가 "알려진 제한사항" 섹션에 미정의 응답 목록 기록


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| openapi-spec-patterns | `skills/openapi-spec-patterns/SKILL.md` | spec-parser | 엔드포인트 그룹핑, 인증 매핑, 페이지네이션/에러 패턴, GraphQL/gRPC |
| sdk-design-patterns | `skills/sdk-design-patterns/SKILL.md` | sdk-developer | 빌더 패턴, 인터셉터 체인, 재시도, 타입 안전, 페이지네이션 래퍼 |
