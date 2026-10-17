---
name: api-error-design
description: "API error design patterns. An extension skill for doc-writer/mock-tester that provides error code systems, error response structures, client-friendly error messages, error catalog construction, and retry/fallback strategies. Use when designing API error handling systems involving 'API error design', 'error codes', 'error responses', 'error catalogs', 'error messages', 'retry strategies', etc. Note: actual error handling code implementation is outside the scope of this skill."
---

# API Error Design — API Error Design Patterns

A reference for error systems, message design, and recovery strategies used by the doc-writer and mock-tester agents when designing API error documentation and tests.

## Target Agents

- `doc-writer` — Applied when writing error reference documentation
- `mock-tester` — Applied when designing error scenario tests

## Error Code System Design

### Hierarchical Error Code Structure
```
{DOMAIN}_{CATEGORY}_{DETAIL}

Examples:
AUTH_TOKEN_EXPIRED        -- Authentication > Token > Expired
ORDER_PAYMENT_DECLINED    -- Order > Payment > Declined
USER_VALIDATION_EMAIL     -- User > Validation > Email
```

### Error Code Catalog by Domain

#### Authentication/Authorization (AUTH)
| Code | HTTP | Message | Client Action |
|------|------|---------|---------------|
| AUTH_REQUIRED | 401 | Authentication is required | Redirect to login page |
| AUTH_TOKEN_EXPIRED | 401 | Token has expired | Attempt token refresh |
| AUTH_TOKEN_INVALID | 401 | Invalid token | Re-authenticate |
| AUTH_FORBIDDEN | 403 | You do not have permission for this action | Guide user to request permissions |
| AUTH_ACCOUNT_LOCKED | 403 | Account is locked. Please retry after 15 minutes | Display wait timer |
| AUTH_INVALID_CREDENTIALS | 401 | Invalid email or password | Prompt re-entry |

#### Validation (VALIDATION)
| Code | HTTP | Message | Field-Level Detail |
|------|------|---------|-------------------|
| VALIDATION_REQUIRED | 422 | Required field is missing | The `{field}` field is required |
| VALIDATION_FORMAT | 422 | Invalid format | Please enter a valid `{type}` |
| VALIDATION_RANGE | 422 | Value is out of range | Please enter a value between `{min}` and `{max}` |
| VALIDATION_UNIQUE | 409 | Value is already in use | This `{field}` is already registered |
| VALIDATION_LENGTH | 422 | Length limit exceeded | Please enter no more than `{max}` characters |

#### Resource (RESOURCE)
| Code | HTTP | Message |
|------|------|---------|
| RESOURCE_NOT_FOUND | 404 | The requested resource was not found |
| RESOURCE_ALREADY_EXISTS | 409 | Resource already exists |
| RESOURCE_DELETED | 410 | Resource has been deleted |
| RESOURCE_LOCKED | 423 | Resource is locked |

#### Rate Limit
| Code | HTTP | Message |
|------|------|---------|
| RATE_LIMIT_EXCEEDED | 429 | Request limit exceeded. Please retry after {retryAfter} seconds |

#### Server (SERVER)
| Code | HTTP | Message |
|------|------|---------|
| SERVER_INTERNAL | 500 | A server error occurred. Please retry shortly |
| SERVER_MAINTENANCE | 503 | Service is under maintenance |
| SERVER_UPSTREAM | 502 | Failed to connect to an external service |

## Error Response Structure Standard

### Basic Structure
```json
{
  "error": {
    "code": "AUTH_TOKEN_EXPIRED",
    "message": "Token has expired",
    "detail": "The access token has expired. Please refresh using your refresh token.",
    "timestamp": "2025-03-15T09:30:00Z",
    "requestId": "req_abc123def456",
    "path": "/api/v1/users/me"
  }
}
```

### Validation Error (Per-Field)
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input values are invalid",
    "errors": [
      {
        "field": "email",
        "code": "VALIDATION_FORMAT",
        "message": "Please enter a valid email address",
        "value": "invalid-email"
      },
      {
        "field": "password",
        "code": "VALIDATION_LENGTH",
        "message": "Password must be at least 8 characters",
        "constraint": { "min": 8 }
      }
    ]
  }
}
```

## Error Message Writing Principles

### Three Elements of a Good Error Message
1. **What went wrong** — Describe the problem
2. **Why it went wrong** — Explain the cause or constraint
3. **How to fix it** — Provide a specific action

### Do / Don't

| Don't | Do |
|-------|---|
| "Error occurred" | "Failed to create the order" |
| "Invalid input" | "Price must be a number greater than 0" |
| "Server error: NullPointerException at..." | "A server error occurred. Please retry shortly" |
| "Access denied" | "You do not have permission to modify this order. Please contact an administrator" |
| "Duplicate key constraint violation" | "This email is already registered" |

### Multilingual Error Message Structure
```json
{
  "error": {
    "code": "VALIDATION_REQUIRED",
    "message": "Required field is missing",
    "messageKey": "error.validation.required",
    "params": { "field": "email" }
  }
}
```

## Retry/Fallback Strategy

### Retry Eligibility

| HTTP Status | Retryable? | Strategy |
|-------------|-----------|----------|
| 408 | Yes | Retry immediately |
| 429 | Yes | Wait per Retry-After header |
| 500 | Yes (conditional) | Exponential backoff |
| 502, 503, 504 | Yes | Exponential backoff |
| 400, 401, 403, 404 | No | Client-side fix required |
| 409, 422 | No | Input correction required |

### Exponential Backoff
```
wait_time = min(baseDelay * 2^attempt + jitter, maxDelay)

Example: baseDelay=1s, maxDelay=30s
Attempt 1: 1s + random(0~500ms)
Attempt 2: 2s + random(0~500ms)
Attempt 3: 4s + random(0~500ms)
Attempt 4: 8s + random(0~500ms)
Maximum 3-5 attempts
```

## Error Test Scenario Matrix

| Category | Test Case | Expected Code |
|----------|-----------|---------------|
| No authentication | Request without Authorisation header | 401 |
| Expired token | Request with expired JWT | 401 |
| No permission | Access another user's resource | 403 |
| Non-existent ID | Query with random UUID | 404 |
| Missing required field | Remove required field from body | 422 |
| Invalid format | "abc" in email field | 422 |
| Duplicate creation | POST same data twice | 409 |
| Bulk requests | Exceed Rate Limit | 429 |
| Malformed JSON | Send `{invalid json` | 400 |
| Empty body | Content-Length: 0 | 400 |
