---
name: api-doc-standards
description: "API 문서 작성 표준 및 패턴 라이브러리. doc-writer 에이전트가 REST/GraphQL/gRPC API 문서를 작성할 때 참조하는 표준. 'API 문서 표준', 'API 레퍼런스 작성' 요청 시 사용. 단, OpenAPI Spec 자동 생성이나 API 테스트 실행은 범위 밖."
---

# API Doc Standards — API 문서 작성 표준

doc-writer 에이전트의 API 문서 품질을 표준화하는 규격과 패턴.

## REST API 문서 필수 섹션

```
1. 개요 — API 목적, 대상 사용자, 기본 URL
2. 인증 — 인증 방식, 토큰 획득/갱신
3. 공통 규격 — 요청/응답 포맷, 페이지네이션, 에러 코드
4. 엔드포인트 레퍼런스 — 리소스별 CRUD
5. 에러 처리 — 에러 코드 테이블, 트러블슈팅
6. 변경 이력 — 버전별 변경사항
```

## 엔드포인트 문서 템플릿

```markdown
## POST /api/v1/users

사용자를 생성합니다.

### 요청

**헤더**
| 헤더 | 값 | 필수 |
|------|-----|------|
| Authorization | Bearer {token} | O |
| Content-Type | application/json | O |

**본문**
| 필드 | 타입 | 필수 | 설명 | 제약조건 |
|------|------|------|------|---------|
| email | string | O | 이메일 | RFC 5322, 254자 |
| name | string | O | 이름 | 2~50자 |
| role | string | X | 역할 | admin/user/viewer, 기본: user |

### 응답

**성공 (201 Created)**
{ "id": "usr_abc123", "email": "...", "name": "..." }

**에러**
| 상태 | 코드 | 설명 |
|------|------|------|
| 400 | INVALID_EMAIL | 이메일 형식 오류 |
| 409 | DUPLICATE_EMAIL | 중복 이메일 |
| 422 | VALIDATION_ERROR | 유효성 오류 |
```

## 에러 응답 표준 형식

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "요청한 리소스를 찾을 수 없습니다.",
    "details": [{ "field": "user_id", "reason": "존재하지 않음" }],
    "request_id": "req_xyz789"
  }
}
```

## HTTP 상태 코드 매핑

| 범위 | 의미 | 사용 코드 |
|------|------|----------|
| 2xx | 성공 | 200, 201, 204 |
| 4xx | 클라이언트 에러 | 400, 401, 403, 404, 409, 422, 429 |
| 5xx | 서버 에러 | 500, 502, 503 |

## 페이지네이션 문서 표준

### 커서 기반 (권장)

| 파라미터 | 타입 | 기본값 | 설명 |
|---------|------|-------|------|
| limit | integer | 20 | 항목 수 (1~100) |
| cursor | string | - | 다음 페이지 커서 |

응답 메타: `has_more`, `next_cursor`

### 오프셋 기반

| 파라미터 | 타입 | 기본값 | 설명 |
|---------|------|-------|------|
| page | integer | 1 | 페이지 번호 |
| per_page | integer | 20 | 항목 수 |
| sort | string | created_at | 정렬 기준 |
| order | string | desc | 정렬 방향 |

## 인증 섹션 표준

```markdown
## 인증
모든 API 요청에 Bearer 토큰 필요.

### 토큰 획득: POST /auth/token
### 토큰 사용: Authorization: Bearer {access_token}
### 토큰 갱신: POST /auth/refresh (만료 시)

| 상태 코드 | 원인 | 조치 |
|----------|------|------|
| 401 | 토큰 누락/만료 | 재발급 |
| 403 | 권한 부족 | 역할 확인 |
```

## Rate Limiting 문서 표준

| 플랜 | 제한 | 단위 |
|------|------|------|
| Free | 100 | 분당 |
| Pro | 1,000 | 분당 |
| Enterprise | 10,000 | 분당 |

응답 헤더: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
초과 시: 429 + `Retry-After` 헤더

## 버저닝 문서 표준

- URL 경로 버전: `/api/v1/`, `/api/v2/`
- 하위 호환: 새 필드/엔드포인트/옵션 파라미터 추가
- 호환 불가: 필드 삭제, 구조 변경, 필수 파라미터 추가 → 새 버전 필요
- 폐기 예고: 최소 6개월 전

## 문서 품질 체크리스트

| 항목 | 기준 |
|------|------|
| 예시 | 모든 엔드포인트에 요청+응답+에러 |
| 타입 | string, integer, boolean, array, object |
| 필수/선택 | 모든 파라미터에 표시 |
| 제약조건 | 길이, 허용 값, 패턴 |
| 인증 | 엔드포인트별 필요 권한 |
| SDK 예제 | cURL + 1개 이상 언어 |
| 변경 이력 | 날짜 + 변경 + 영향 범위 |
