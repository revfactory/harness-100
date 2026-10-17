---
name: api-security-checklist
description: "Web app API security checklist. Provides OWASP Top 10-based vulnerability checks, authentication/authorization patterns, input validation, Rate Limiting, CORS, CSRF, and SQL Injection defence as a backend-dev extension skill. Use for requests like 'API security', 'OWASP', 'auth implementation', 'SQL Injection', 'XSS defence', 'CORS configuration', 'security checklist', and other backend security design tasks. However, penetration testing or WAF configuration is outside this skill's scope."
---

# API Security Checklist — Web App API Security Checklist

An OWASP-based security checklist, authentication patterns, and defence code guide that the backend-dev agent uses during API development.

## Target Agent

`backend-dev` — Applies this skill's security checklist directly to API implementation.

## OWASP API Security Top 10 Check

| Rank | Vulnerability | Check Item | Defence |
|------|-------------|-----------|---------|
| A1 | **BOLA** (Broken Object Level Authorisation) | Can another user's resources be accessed? | Verify object ownership at every endpoint |
| A2 | **Broken Authentication** | Weak passwords, unlimited login attempts? | bcrypt hashing, Rate Limit, MFA |
| A3 | **Broken Object Property Level Authorisation** | Are fields that should be hidden exposed? | Filter fields via response DTOs |
| A4 | **Unrestricted Resource Consumption** | Can mass requests crash the server? | Rate Limiting, enforce pagination |
| A5 | **Broken Function Level Authorisation** | Can regular users call admin APIs? | RBAC middleware |
| A6 | **Server-Side Request Forgery (SSRF)** | Can external URL input access internal resources? | URL whitelist, block internal IPs |
| A7 | **Security Misconfiguration** | Debug mode exposed, default accounts? | Separate production config, inspect headers |
| A8 | **Lack of Protection from Automated Threats** | Can normal APIs be called in abnormal sequences? | State machine validation, server-side business rules |
| A9 | **Improper Asset Management** | Unused APIs, old versions exposed? | API inventory, version deprecation policy |
| A10 | **Unsafe Consumption of APIs** | Are external API responses blindly trusted? | Validate external responses, set timeouts |

## Authentication Patterns

### JWT-Based Authentication

| Item | Recommended Setting |
|------|-------------------|
| Access Token Expiry | 15-30 minutes |
| Refresh Token Expiry | 7-14 days |
| Algorithm | RS256 (asymmetric) or HS256 (symmetric) |
| Storage | httpOnly + secure + sameSite cookie |
| Payload | Minimal info only (userId, role) — no PII |
| Renewal Strategy | Silent Refresh or Rotation |

### Password Policy
- Minimum 8 characters, recommend uppercase + lowercase + numbers + special chars (show strength rather than enforce)
- bcrypt (cost factor 12+) or Argon2id
- Password history (prevent reuse of last 5)
- Temporary lock after 5 failed login attempts (15 min) or CAPTCHA

## Authorisation Patterns

### RBAC (Role-Based)
```
Role definitions: admin, manager, user, viewer
Permission mapping:
  admin    → *.* (full access)
  manager  → resource.create, resource.read, resource.update
  user     → resource.create (own), resource.read (own)
  viewer   → resource.read (public)
```

### Middleware Chain
```
Request → [Rate Limit] → [Auth: JWT verification] → [Authorization: role check] → [Input Validation] → Handler
```

## Input Validation Checklist

| Validation Item | Method | Tool |
|----------------|--------|------|
| **Type Validation** | Schema validation | Zod, Joi, class-validator |
| **Length Limits** | Min/max length | Schema min/max |
| **Pattern Matching** | Email, URL, phone | Regex + libraries |
| **Range Validation** | Number range, date range | min/max values |
| **Enumeration** | Allowed value list | enum type |
| **SQL Injection** | Parameterized queries | ORM (Prisma, TypeORM) |
| **XSS** | HTML escaping | DOMPurify (client), server escape |
| **Path Traversal** | Path normalisation | path.resolve + whitelist |
| **File Upload** | Type/size validation | MIME type + magic number verification |

## HTTP Security Headers

| Header | Value | Purpose |
|--------|-------|---------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Force HTTPS |
| `X-Content-Type-Options` | `nosniff` | Prevent MIME sniffing |
| `X-Frame-Options` | `DENY` or `SAMEORIGIN` | Prevent clickjacking |
| `Content-Security-Policy` | `default-src 'self'` | Prevent XSS |
| `X-XSS-Protection` | `0` (replaced by CSP) | Legacy |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Limit referrer info |
| `Permissions-Policy` | `camera=(), microphone=()` | Restrict browser features |

## CORS Configuration Guide

| Environment | Setting |
|------------|---------|
| Development | `origin: 'http://localhost:3000'` |
| Production | `origin: ['https://example.com']` — specify domains |
| Forbidden | `origin: '*'` + `credentials: true` — security risk |

Required settings:
- `methods`: Allow only necessary methods
- `allowedHeaders`: Only necessary headers
- `credentials`: Set to true only when cookies are needed
- `maxAge`: Preflight caching (86400 seconds)

## Rate Limiting Strategy

| Target | Limit | Implementation |
|--------|-------|---------------|
| Auth endpoints | 5 req/min/IP | IP-based |
| General API | 100 req/min/user | Token-based |
| File upload | 10 req/hour/user | Token-based |
| Unauthenticated API | 30 req/min/IP | IP-based |

### Response Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1609459200
Retry-After: 60 (on 429 response)
```

## Error Response Security

### Production Error Response Rules
- Never expose internal implementation details (stack traces, SQL queries)
- Use consistent error format
- Prevent enumeration attacks: On login failure, show "Email or password is incorrect" (don't reveal which one is wrong)

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input is invalid",
    "details": [
      {"field": "email", "message": "Please enter a valid email"}
    ]
  }
}
```

## Sensitive Data Handling

| Data Type | Storage | Transmission | Logging |
|----------|---------|-------------|---------|
| Passwords | bcrypt hash only | HTTPS only | Never |
| API Keys | Environment variables | Header (Authorisation) | Masked (first 4 chars only) |
| PII | Encrypted (AES-256) | HTTPS only | Masked |
| Credit Cards | Tokenized (delegate to payment provider) | Payment provider SDK | Never |
| Sessions/Tokens | httpOnly cookie | HTTPS only | Never |
