---
name: rest-api-conventions
description: "REST API design conventions reference. An extension skill for api-architect that provides URL naming, HTTP method mapping, status code selection, pagination/filtering/sorting patterns, HATEOAS, and versioning strategies. Use when designing RESTful APIs involving 'REST conventions', 'URL design', 'HTTP status codes', 'pagination', 'API versioning', 'HATEOAS', etc. Note: GraphQL design and actual server implementation are outside the scope of this skill."
---

# REST API Conventions — RESTful API Design Conventions Reference

A reference of naming rules, status codes, and pagination patterns used by the api-architect agent when designing REST APIs.

## Target Agent

`api-architect` — Directly applies the conventions in this skill to API designs.

## URL Naming Rules

### Basic Principles
| Rule | Correct Example | Incorrect Example |
|------|----------------|-------------------|
| Plural nouns | `/users` | `/user`, `/getUsers` |
| Lowercase kebab-case | `/user-profiles` | `/userProfiles`, `/User_Profiles` |
| No verbs (use methods for CRUD) | `POST /orders` | `POST /createOrder` |
| Hierarchical relationships | `/users/{id}/orders` | `/getUserOrders` |
| No trailing slash | `/users` | `/users/` |
| No file extensions | `/users` (use Accept header) | `/users.json` |

### Resource URL Patterns

| Operation | Method | URL | Example |
|-----------|--------|-----|---------|
| List retrieval | GET | `/resources` | `GET /products` |
| Single retrieval | GET | `/resources/{id}` | `GET /products/123` |
| Create | POST | `/resources` | `POST /products` |
| Full update | PUT | `/resources/{id}` | `PUT /products/123` |
| Partial update | PATCH | `/resources/{id}` | `PATCH /products/123` |
| Delete | DELETE | `/resources/{id}` | `DELETE /products/123` |

### Relationship Resources
```
GET  /users/{userId}/orders           -- User's order list
GET  /users/{userId}/orders/{orderId} -- User's specific order
POST /users/{userId}/orders           -- Create order for user
```

### Non-CRUD Actions (RPC-Style Permitted)
```
POST /orders/{id}/cancel        -- Cancel order
POST /users/{id}/verify-email   -- Verify email
POST /reports/generate          -- Generate report
POST /cart/checkout             -- Proceed to checkout
```

## HTTP Status Code Selection Guide

### Success (2xx)
| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | GET, PUT, PATCH success |
| 201 | Created | POST resource creation success (include Location header) |
| 204 | No Content | DELETE success, no response body |

### Client Errors (4xx)
| Code | Meaning | When to Use |
|------|---------|-------------|
| 400 | Bad Request | Malformed request, validation failure |
| 401 | Unauthorized | Authentication required (missing/expired token) |
| 403 | Forbidden | Authenticated but not authorised |
| 404 | Not Found | Resource does not exist |
| 405 | Method Not Allowed | HTTP method not permitted |
| 409 | Conflict | Resource conflict (duplicate creation, etc.) |
| 422 | Unprocessable Entity | Format is correct but violates business rules |
| 429 | Too Many Requests | Rate limit exceeded |

### Server Errors (5xx)
| Code | Meaning | When to Use |
|------|---------|-------------|
| 500 | Internal Server Error | Unexpected server error |
| 502 | Bad Gateway | Upstream service error |
| 503 | Service Unavailable | Maintenance/overload (include Retry-After header) |

## Pagination Patterns

### Offset-Based (Traditional)
```
GET /products?page=2&limit=20

Response:
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
- Pros: Simple implementation, random page access
- Cons: Performance degradation with large datasets (OFFSET)

### Cursor-Based (Recommended)
```
GET /products?cursor=eyJpZCI6MTIzfQ&limit=20

Response:
{
  "data": [...],
  "pagination": {
    "nextCursor": "eyJpZCI6MTQzfQ",
    "hasMore": true
  }
}
```
- Pros: Excellent performance with large datasets, safe for real-time data
- Cons: No total count or random page access

### Selection Criteria
| Scenario | Recommendation |
|----------|---------------|
| Admin dashboard (page numbers needed) | Offset |
| Infinite scroll | Cursor |
| Real-time feed | Cursor |
| 1M+ records | Cursor |

## Filtering/Sorting/Search Patterns

### Filtering
```
GET /products?category=electronics&price_min=10000&price_max=50000&status=active
```

### Sorting
```
GET /products?sort=price&order=asc
GET /products?sort=-created_at,+name    (prefix style: - descending, + ascending)
```

### Search
```
GET /products?q=keyboard                (full-text search)
GET /products?name=keyboard             (specific field)
```

### Field Selection (Sparse Fieldsets)
```
GET /products?fields=id,name,price      (only needed fields)
```

## Error Response Standard Format

### RFC 7807 (Problem Details)
```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation Error",
  "status": 422,
  "detail": "The request data is invalid",
  "instance": "/products",
  "errors": [
    {
      "field": "price",
      "code": "INVALID_RANGE",
      "message": "Price must be greater than 0"
    }
  ]
}
```

## Versioning Strategies

| Strategy | Method | Pros | Cons |
|----------|--------|------|------|
| **URL Path** | `/v1/users` | Clear, simple routing | URL changes |
| **Header** | `Accept: application/vnd.api+json;version=1` | Clean URLs | Harder to debug |
| **Query** | `/users?version=1` | Can be optional | Complex caching |

**Recommended**: URL Path (`/v1/`) — Most intuitive and widely adopted

### Version Deprecation Policy
- New version released -> Maintain old version for 12 months
- Deprecation headers: `Deprecation: true`, `Sunset: 2025-12-31`
- Provide migration guide

## Response Envelope Pattern

### Single Resource Response
```json
{
  "data": { "id": 1, "name": "Product" },
  "meta": { "requestId": "abc-123" }
}
```

### List Response
```json
{
  "data": [{ "id": 1 }, { "id": 2 }],
  "pagination": { "page": 1, "limit": 20, "total": 150 },
  "meta": { "requestId": "abc-123" }
}
```

## Idempotency

| Method | Idempotent | Safe | Description |
|--------|-----------|------|-------------|
| GET | Yes | Yes | Returns the same result |
| PUT | Yes | No | Same data repeated yields the same result |
| DELETE | Yes | No | Re-deleting an already deleted resource returns 404 |
| PATCH | No | No | Can make relative changes (counter++) |
| POST | No | No | May create duplicates -> Idempotency-Key recommended |
