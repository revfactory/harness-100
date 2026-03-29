---
name: api-doc-standards
description: "API documentation standards and pattern library. The standard that the doc-writer agent references when writing REST/GraphQL/gRPC API documentation. Use when 'API documentation standards' or 'writing an API reference' is requested. Automatic OpenAPI Spec generation and API test execution are outside this skill's scope."
---

# API Doc Standards — API Documentation Writing Standards

Specifications and patterns that standardize the API documentation quality of the doc-writer agent.

## Required Sections for REST API Documentation

```
1. Overview — API purpose, target users, base URL
2. Authentication — Authentication method, token acquisition / refresh
3. Common conventions — Request/response format, pagination, error codes
4. Endpoint reference — CRUD per resource
5. Error handling — Error code table, troubleshooting
6. Change history — Changes per version
```

## Endpoint Documentation Template

```markdown
## POST /api/v1/users

Creates a new user.

### Request

**Headers**
| Header | Value | Required |
|--------|-------|----------|
| Authorization | Bearer {token} | Yes |
| Content-Type | application/json | Yes |

**Body**
| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| email | string | Yes | Email address | RFC 5322, 254 characters |
| name | string | Yes | Full name | 2–50 characters |
| role | string | No | Role | admin/user/viewer, default: user |

### Response

**Success (201 Created)**
{ "id": "usr_abc123", "email": "...", "name": "..." }

**Error**
| Status | Code | Description |
|--------|------|-------------|
| 400 | INVALID_EMAIL | Invalid email format |
| 409 | DUPLICATE_EMAIL | Email already in use |
| 422 | VALIDATION_ERROR | Validation error |
```

## Standard Error Response Format

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource could not be found.",
    "details": [{ "field": "user_id", "reason": "Does not exist" }],
    "request_id": "req_xyz789"
  }
}
```

## HTTP Status Code Mapping

| Range | Meaning | Codes Used |
|-------|---------|------------|
| 2xx | Success | 200, 201, 204 |
| 4xx | Client error | 400, 401, 403, 404, 409, 422, 429 |
| 5xx | Server error | 500, 502, 503 |

## Pagination Documentation Standards

### Cursor-Based (Recommended)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| limit | integer | 20 | Number of items (1–100) |
| cursor | string | - | Next page cursor |

Response metadata: `has_more`, `next_cursor`

### Offset-Based

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number |
| per_page | integer | 20 | Items per page |
| sort | string | created_at | Sort field |
| order | string | desc | Sort direction |

## Authentication Section Standard

```markdown
## Authentication
All API requests require a Bearer token.

### Obtain token: POST /auth/token
### Use token: Authorization: Bearer {access_token}
### Refresh token: POST /auth/refresh (when expired)

| Status Code | Cause | Action |
|-------------|-------|--------|
| 401 | Token missing / expired | Reissue token |
| 403 | Insufficient permissions | Check role |
```

## Rate Limiting Documentation Standard

| Plan | Limit | Unit |
|------|-------|------|
| Free | 100 | Per minute |
| Pro | 1,000 | Per minute |
| Enterprise | 10,000 | Per minute |

Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
When exceeded: 429 + `Retry-After` header

## Versioning Documentation Standard

- URL path versioning: `/api/v1/`, `/api/v2/`
- Backward compatible: Adding new fields / endpoints / optional parameters
- Breaking change: Removing fields, restructuring, adding required parameters → new version required
- Deprecation notice: Minimum 6 months in advance

## Documentation Quality Checklist

| Item | Standard |
|------|----------|
| Examples | Request + response + error for every endpoint |
| Types | string, integer, boolean, array, object |
| Required / optional | Indicated for all parameters |
| Constraints | Length, allowed values, pattern |
| Authentication | Required permissions per endpoint |
| SDK examples | cURL + at least 1 language |
| Change history | Date + change + impact scope |
