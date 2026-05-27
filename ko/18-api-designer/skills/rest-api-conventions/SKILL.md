---
name: rest-api-conventions
description: "REST API 설계 컨벤션 레퍼런스. URL 네이밍, HTTP 메서드 매핑, 상태 코드 선택, 페이지네이션/필터링/정렬 패턴, HATEOAS, 버전관리 전략을 제공하는 api-architect 확장 스킬. 'REST 컨벤션', 'URL 설계', 'HTTP 상태 코드', '페이지네이션', 'API 버전관리', 'HATEOAS' 등 RESTful API 설계 시 사용한다. 단, GraphQL 설계나 실제 서버 구현은 이 스킬의 범위가 아니다."
---

# REST API Conventions — RESTful API 설계 컨벤션 레퍼런스

api-architect 에이전트가 REST API 설계 시 활용하는 네이밍 규칙, 상태 코드, 페이지네이션 패턴 레퍼런스.

## 대상 에이전트

`api-architect` — 이 스킬의 컨벤션을 API 설계에 직접 적용한다.

## URL 네이밍 규칙

### 기본 원칙
| 규칙 | 올바른 예 | 잘못된 예 |
|------|----------|----------|
| 복수형 명사 | `/users` | `/user`, `/getUsers` |
| 소문자 kebab-case | `/user-profiles` | `/userProfiles`, `/User_Profiles` |
| 동사 금지 (CRUD는 메서드로) | `POST /orders` | `POST /createOrder` |
| 계층적 관계 | `/users/{id}/orders` | `/getUserOrders` |
| 슬래시 끝 금지 | `/users` | `/users/` |
| 파일 확장자 금지 | `/users` (Accept 헤더) | `/users.json` |

### 리소스 URL 패턴

| 작업 | 메서드 | URL | 예시 |
|------|--------|-----|------|
| 목록 조회 | GET | `/resources` | `GET /products` |
| 단건 조회 | GET | `/resources/{id}` | `GET /products/123` |
| 생성 | POST | `/resources` | `POST /products` |
| 전체 수정 | PUT | `/resources/{id}` | `PUT /products/123` |
| 부분 수정 | PATCH | `/resources/{id}` | `PATCH /products/123` |
| 삭제 | DELETE | `/resources/{id}` | `DELETE /products/123` |

### 관계 리소스
```
GET  /users/{userId}/orders           -- 사용자의 주문 목록
GET  /users/{userId}/orders/{orderId} -- 사용자의 특정 주문
POST /users/{userId}/orders           -- 사용자의 주문 생성
```

### 비-CRUD 액션 (RPC 스타일 허용)
```
POST /orders/{id}/cancel        -- 주문 취소
POST /users/{id}/verify-email   -- 이메일 인증
POST /reports/generate          -- 보고서 생성
POST /cart/checkout             -- 결제 진행
```

## HTTP 상태 코드 선택 가이드

### 성공 (2xx)
| 코드 | 의미 | 사용 시점 |
|------|------|----------|
| 200 | OK | GET, PUT, PATCH 성공 |
| 201 | Created | POST 리소스 생성 성공 (Location 헤더 포함) |
| 204 | No Content | DELETE 성공, 응답 바디 없음 |

### 클라이언트 에러 (4xx)
| 코드 | 의미 | 사용 시점 |
|------|------|----------|
| 400 | Bad Request | 요청 형식 오류, 유효성 검증 실패 |
| 401 | Unauthorized | 인증 필요 (토큰 없음/만료) |
| 403 | Forbidden | 인증됨, 권한 없음 |
| 404 | Not Found | 리소스 존재하지 않음 |
| 405 | Method Not Allowed | 허용되지 않은 HTTP 메서드 |
| 409 | Conflict | 리소스 충돌 (중복 생성 등) |
| 422 | Unprocessable Entity | 형식은 맞지만 비즈니스 규칙 위반 |
| 429 | Too Many Requests | Rate Limit 초과 |

### 서버 에러 (5xx)
| 코드 | 의미 | 사용 시점 |
|------|------|----------|
| 500 | Internal Server Error | 예상치 못한 서버 오류 |
| 502 | Bad Gateway | 업스트림 서비스 오류 |
| 503 | Service Unavailable | 점검/과부하 (Retry-After 헤더) |

## 페이지네이션 패턴

### 오프셋 기반 (전통적)
```
GET /products?page=2&limit=20

응답:
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8
  }
}
```
- 장점: 구현 간단, 임의 페이지 접근
- 단점: 대량 데이터에서 성능 저하 (OFFSET)

### 커서 기반 (권장)
```
GET /products?cursor=eyJpZCI6MTIzfQ&limit=20

응답:
{
  "data": [...],
  "pagination": {
    "nextCursor": "eyJpZCI6MTQzfQ",
    "hasMore": true
  }
}
```
- 장점: 대량 데이터 성능 우수, 실시간 데이터에 안전
- 단점: 총 개수/임의 페이지 접근 불가

### 선택 기준
| 상황 | 추천 |
|------|------|
| 관리자 대시보드 (페이지 번호 필요) | 오프셋 |
| 무한 스크롤 | 커서 |
| 실시간 피드 | 커서 |
| 데이터 100만 건+ | 커서 |

## 필터링/정렬/검색 패턴

### 필터링
```
GET /products?category=electronics&price_min=10000&price_max=50000&status=active
```

### 정렬
```
GET /products?sort=price&order=asc
GET /products?sort=-created_at,+name    (prefix 방식: -내림, +오름)
```

### 검색
```
GET /products?q=키보드                  (전체 검색)
GET /products?name=키보드               (특정 필드)
```

### 필드 선택 (Sparse Fieldsets)
```
GET /products?fields=id,name,price      (필요한 필드만)
```

## 에러 응답 표준 형식

### RFC 7807 (Problem Details)
```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "요청 데이터가 유효하지 않습니다",
  "instance": "/products",
  "errors": [
    {
      "field": "price",
      "code": "INVALID_RANGE",
      "message": "가격은 0보다 커야 합니다"
    }
  ]
}
```

## 버전관리 전략

| 전략 | 방법 | 장점 | 단점 |
|------|------|------|------|
| **URL Path** | `/v1/users` | 명확, 라우팅 간단 | URL 변경 |
| **Header** | `Accept: application/vnd.api+json;version=1` | URL 깔끔 | 디버깅 어려움 |
| **Query** | `/users?version=1` | 옵셔널 가능 | 캐싱 복잡 |

**권장**: URL Path (`/v1/`) — 가장 직관적이고 널리 채택

### 버전 폐기 정책
- 새 버전 출시 → 구 버전 12개월 유지
- Deprecation 헤더: `Deprecation: true`, `Sunset: 2025-12-31`
- 마이그레이션 가이드 제공

## 응답 Envelope 패턴

### 단건 응답
```json
{
  "data": { "id": 1, "name": "Product" },
  "meta": { "requestId": "abc-123" }
}
```

### 목록 응답
```json
{
  "data": [{ "id": 1 }, { "id": 2 }],
  "pagination": { "page": 1, "limit": 20, "total": 150 },
  "meta": { "requestId": "abc-123" }
}
```

## 멱등성 (Idempotency)

| 메서드 | 멱등 | 안전 | 설명 |
|--------|------|------|------|
| GET | O | O | 동일 결과 반환 |
| PUT | O | X | 같은 데이터로 반복 시 동일 결과 |
| DELETE | O | X | 이미 삭제된 리소스 재삭제 시 404 |
| PATCH | X | X | 상대적 변경 가능 (counter++) |
| POST | X | X | 중복 생성 가능 → Idempotency-Key 권장 |
