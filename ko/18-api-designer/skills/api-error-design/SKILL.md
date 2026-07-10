---
name: api-error-design
description: "API 에러 설계 패턴. 에러 코드 체계, 에러 응답 구조, 클라이언트 친화적 에러 메시지, 에러 카탈로그 구축, retry/fallback 전략을 제공하는 doc-writer/mock-tester 확장 스킬. 'API 에러 설계', '에러 코드', '에러 응답', '에러 카탈로그', '에러 메시지', 'retry 전략' 등 API 에러 처리 체계 설계 시 사용한다. 단, 실제 에러 핸들링 코드 구현은 이 스킬의 범위가 아니다."
---

# API Error Design — API 에러 설계 패턴

doc-writer와 mock-tester 에이전트가 API 에러 문서화 및 테스트 설계 시 활용하는 에러 체계, 메시지 설계, 복구 전략 레퍼런스.

## 대상 에이전트

- `doc-writer` — 에러 레퍼런스 문서 작성에 적용
- `mock-tester` — 에러 시나리오 테스트 설계에 적용

## 에러 코드 체계 설계

### 계층적 에러 코드 구조
```
{도메인}_{카테고리}_{상세}

예시:
AUTH_TOKEN_EXPIRED        -- 인증 > 토큰 > 만료
ORDER_PAYMENT_DECLINED    -- 주문 > 결제 > 거절
USER_VALIDATION_EMAIL     -- 사용자 > 유효성 > 이메일
```

### 도메인별 에러 코드 카탈로그

#### 인증/인가 (AUTH)
| 코드 | HTTP | 메시지 | 클라이언트 액션 |
|------|------|--------|---------------|
| AUTH_REQUIRED | 401 | 인증이 필요합니다 | 로그인 페이지로 이동 |
| AUTH_TOKEN_EXPIRED | 401 | 토큰이 만료되었습니다 | 토큰 갱신 시도 |
| AUTH_TOKEN_INVALID | 401 | 유효하지 않은 토큰입니다 | 재로그인 |
| AUTH_FORBIDDEN | 403 | 이 작업에 대한 권한이 없습니다 | 권한 요청 안내 |
| AUTH_ACCOUNT_LOCKED | 403 | 계정이 잠겼습니다. 15분 후 재시도하세요 | 대기 타이머 표시 |
| AUTH_INVALID_CREDENTIALS | 401 | 이메일 또는 비밀번호가 올바르지 않습니다 | 재입력 유도 |

#### 유효성 검증 (VALIDATION)
| 코드 | HTTP | 메시지 | 필드별 상세 |
|------|------|--------|-----------|
| VALIDATION_REQUIRED | 422 | 필수 필드가 누락되었습니다 | `{field}` 필드는 필수입니다 |
| VALIDATION_FORMAT | 422 | 형식이 올바르지 않습니다 | 유효한 `{type}`을 입력하세요 |
| VALIDATION_RANGE | 422 | 범위를 벗어났습니다 | `{min}`~`{max}` 사이 값을 입력하세요 |
| VALIDATION_UNIQUE | 409 | 이미 사용 중인 값입니다 | 이 `{field}`는 이미 등록되어 있습니다 |
| VALIDATION_LENGTH | 422 | 길이 제한을 초과했습니다 | `{max}`자 이내로 입력하세요 |

#### 리소스 (RESOURCE)
| 코드 | HTTP | 메시지 |
|------|------|--------|
| RESOURCE_NOT_FOUND | 404 | 요청한 리소스를 찾을 수 없습니다 |
| RESOURCE_ALREADY_EXISTS | 409 | 이미 존재하는 리소스입니다 |
| RESOURCE_DELETED | 410 | 삭제된 리소스입니다 |
| RESOURCE_LOCKED | 423 | 리소스가 잠겨 있습니다 |

#### Rate Limit
| 코드 | HTTP | 메시지 |
|------|------|--------|
| RATE_LIMIT_EXCEEDED | 429 | 요청 한도를 초과했습니다. {retryAfter}초 후 재시도하세요 |

#### 서버 (SERVER)
| 코드 | HTTP | 메시지 |
|------|------|--------|
| SERVER_INTERNAL | 500 | 서버 오류가 발생했습니다. 잠시 후 재시도하세요 |
| SERVER_MAINTENANCE | 503 | 서비스 점검 중입니다 |
| SERVER_UPSTREAM | 502 | 외부 서비스 연결에 실패했습니다 |

## 에러 응답 구조 표준

### 기본 구조
```json
{
  "error": {
    "code": "AUTH_TOKEN_EXPIRED",
    "message": "토큰이 만료되었습니다",
    "detail": "access token의 유효기간이 지났습니다. refresh token으로 갱신하세요.",
    "timestamp": "2025-03-15T09:30:00Z",
    "requestId": "req_abc123def456",
    "path": "/api/v1/users/me"
  }
}
```

### 유효성 검증 에러 (필드별)
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "입력값이 올바르지 않습니다",
    "errors": [
      {
        "field": "email",
        "code": "VALIDATION_FORMAT",
        "message": "유효한 이메일 주소를 입력하세요",
        "value": "invalid-email"
      },
      {
        "field": "password",
        "code": "VALIDATION_LENGTH",
        "message": "비밀번호는 8자 이상이어야 합니다",
        "constraint": { "min": 8 }
      }
    ]
  }
}
```

## 에러 메시지 작성 원칙

### 좋은 에러 메시지의 3요소
1. **무엇이 잘못됐는가** — 문제 설명
2. **왜 잘못됐는가** — 원인/제약 조건
3. **어떻게 해결하는가** — 구체적 액션

### Do / Don't

| Don't | Do |
|-------|---|
| "Error occurred" | "주문 생성에 실패했습니다" |
| "Invalid input" | "가격은 0보다 큰 숫자여야 합니다" |
| "Server error: NullPointerException at..." | "서버 오류가 발생했습니다. 잠시 후 재시도하세요" |
| "Access denied" | "이 주문을 수정할 권한이 없습니다. 관리자에게 문의하세요" |
| "Duplicate key constraint violation" | "이 이메일은 이미 등록되어 있습니다" |

### 다국어 에러 메시지 구조
```json
{
  "error": {
    "code": "VALIDATION_REQUIRED",
    "message": "필수 필드가 누락되었습니다",
    "messageKey": "error.validation.required",
    "params": { "field": "email" }
  }
}
```

## Retry/Fallback 전략

### Retry 가능 여부 판단

| HTTP 상태 | Retry 가능? | 전략 |
|----------|-----------|------|
| 408 | O | 즉시 재시도 |
| 429 | O | Retry-After 헤더 대기 후 |
| 500 | O (조건부) | 지수 백오프 |
| 502, 503, 504 | O | 지수 백오프 |
| 400, 401, 403, 404 | X | 클라이언트 수정 필요 |
| 409, 422 | X | 입력값 수정 필요 |

### 지수 백오프 (Exponential Backoff)
```
대기시간 = min(baseDelay * 2^attempt + jitter, maxDelay)

예시: baseDelay=1초, maxDelay=30초
시도 1: 1초 + 랜덤(0~500ms)
시도 2: 2초 + 랜덤(0~500ms)
시도 3: 4초 + 랜덤(0~500ms)
시도 4: 8초 + 랜덤(0~500ms)
최대 3~5회 시도
```

## 에러 테스트 시나리오 매트릭스

| 카테고리 | 테스트 케이스 | 기대 코드 |
|---------|------------|----------|
| 인증 없음 | Authorization 헤더 없이 요청 | 401 |
| 만료 토큰 | 만료된 JWT로 요청 | 401 |
| 권한 없음 | 다른 사용자 리소스 접근 | 403 |
| 존재하지 않는 ID | 랜덤 UUID로 조회 | 404 |
| 필수 필드 누락 | body에서 필수 필드 제거 | 422 |
| 잘못된 형식 | 이메일 필드에 "abc" | 422 |
| 중복 생성 | 같은 데이터로 POST 2회 | 409 |
| 대량 요청 | Rate Limit 초과 | 429 |
| 잘못된 JSON | `{invalid json` 전송 | 400 |
| 빈 바디 | Content-Length: 0 | 400 |
