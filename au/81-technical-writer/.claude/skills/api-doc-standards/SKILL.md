---
name: api-doc-standards
description: "API document writing tablelevel and pattern library. doc-writer agent REST/GraphQL/gRPC API document writingto do when reference tablelevel. 'API document tablelevel', 'API reference writing' request when usage. However, OpenAPI Spec specialist creation API test execution scope outside."
---

# API Doc Standards — API document writing tablelevel

doc-writer agent API document quality tablelevel and pattern.

## REST API document required section

```
1. overview — API purpose, target user, basic URL
2. authentication — authentication method, /
3. — request/ format, degree, error code
4. endpoint reference — by CRUD
5. error processing — error code , 
6. change capability — versionby changematters
```

## endpoint document template

```markdown
## POST /api/v1/users

user creation.

### request

****
| | | required |
|------|-----|------|
| Authorization | Bearer {token} | O |
| Content-Type | application/json | O |

**body text**
| | type | required | description | constraintcondition |
|------|------|------|------|---------|
| email | string | O | email | RFC 5322, 254specialist |
| name | string | O | name | 2~50specialist |
| role | string | X | role | admin/user/viewer, basic: user |

### 

**nature (201 Created)**
{ "id": "usr_abc123", "email": "...", "name": "..." }

**error**
| status | code | description |
|------|------|------|
| 400 | INVALID_EMAIL | email |
| 409 | DUPLICATE_EMAIL | during email |
| 422 | VALIDATION_ERROR | nature |
```

## error tablelevel 

```json
{
 "error": {
 "code": "RESOURCE_NOT_FOUND",
 "message": "requestKorean number .",
 "details": [{ "field": "user_id", "reason": "re-degree " }],
 "request_id": "req_xyz789"
 }
}
```

## HTTP status code mapping

| scope | un- | usage code |
|------|------|----------|
| 2xx | nature | 200, 201, 204 |
| 4xx | error | 400, 401, 403, 404, 409, 422, 429 |
| 5xx | from error | 500, 502, 503 |

## degree document tablelevel

### from based (recommended)

| un- | type | basic | description |
|---------|------|-------|------|
| limit | integer | 20 | item number (1~100) |
| cursor | string | - | next degree from |

 : `has_more`, `next_cursor`

### based

| un- | type | basic | description |
|---------|------|-------|------|
| page | integer | 1 | degree |
| per_page | integer | 20 | item number |
| sort | string | created_at | standard |
| order | string | desc | direction |

## authentication section tablelevel

```markdown
## authentication
all API request Bearer needed.

### : POST /auth/token
### usage: Authorization: Bearer {access_token}
### : POST /auth/refresh ( when)

| status code | cause | action |
|----------|------|------|
| 401 | / | re-grade |
| 403 | authority insufficient | role confirm |
```

## Rate Limiting document tablelevel

| | limitation | |
|------|------|------|
| Free | 100 | minute |
| Pro | 1,000 | minute |
| Enterprise | 10,000 | minute |

 : `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
exceeding when: 429 + `Retry-After` 

## document tablelevel

- URL version: `/api/v1/`, `/api/v2/`
- exchange: /endpoint/option un- addition
- exchange impossible: deletion, structure change, required un- addition → version needed
- basis example: minimum 6months before

## document quality checklist

| item | standard |
|------|------|
| examplewhen | all endpoint request++error |
| type | string, integer, boolean, array, object |
| required/optional | all un- tablewhen |
| constraintcondition | , , pattern |
| authentication | endpointby needed authority |
| SDK example | cURL + 1items or more |
| change capability | date + change + impact scope |
