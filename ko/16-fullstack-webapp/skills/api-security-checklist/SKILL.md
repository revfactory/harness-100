---
name: api-security-checklist
description: "웹앱 API 보안 체크리스트. OWASP Top 10 기반 취약점 점검, 인증/인가 패턴, 입력 검증, Rate Limiting, CORS, CSRF, SQL Injection 방어를 제공하는 backend-dev 확장 스킬. 'API 보안', 'OWASP', '인증 구현', 'SQL Injection', 'XSS 방어', 'CORS 설정', '보안 체크리스트' 등 백엔드 보안 설계 시 사용한다. 단, 침투 테스트 수행이나 WAF 구성은 이 스킬의 범위가 아니다."
---

# API Security Checklist — 웹앱 API 보안 체크리스트

backend-dev 에이전트가 API 개발 시 활용하는 OWASP 기반 보안 체크리스트, 인증 패턴, 방어 코드 가이드.

## 대상 에이전트

`backend-dev` — 이 스킬의 보안 체크리스트를 API 구현에 직접 적용한다.

## OWASP API Security Top 10 점검

| 순위 | 취약점 | 점검 항목 | 방어 |
|------|--------|----------|------|
| A1 | **BOLA** (객체 수준 인가 결함) | 다른 사용자의 리소스 접근 가능? | 모든 엔드포인트에서 객체 소유권 검증 |
| A2 | **인증 결함** | 약한 비밀번호, 무제한 로그인 시도? | bcrypt 해싱, Rate Limit, MFA |
| A3 | **객체 속성 수준 인가** | 숨겨야 할 필드 노출? | 응답 DTO로 필드 필터링 |
| A4 | **무제한 리소스 소비** | 대량 요청으로 서버 마비? | Rate Limiting, 페이지네이션 강제 |
| A5 | **기능 수준 인가 결함** | 관리자 API를 일반 유저가 호출? | RBAC 미들웨어 |
| A6 | **서버 사이드 요청 위조 (SSRF)** | 외부 URL 입력으로 내부 접근? | URL 화이트리스트, 내부 IP 차단 |
| A7 | **보안 설정 오류** | 디버그 모드 노출, 기본 계정? | 프로덕션 설정 분리, 헤더 점검 |
| A8 | **비즈니스 흐름 결함** | 정상 API를 비정상 순서로 호출? | 상태 머신 검증, 비즈니스 규칙 서버측 |
| A9 | **취약 자산 관리** | 미사용 API, 구버전 노출? | API 인벤토리, 버전 폐기 정책 |
| A10 | **안전하지 않은 API 소비** | 외부 API 응답 무조건 신뢰? | 외부 응답 검증, 타임아웃 설정 |

## 인증 (Authentication) 패턴

### JWT 기반 인증

| 항목 | 권장 설정 |
|------|----------|
| Access Token 만료 | 15~30분 |
| Refresh Token 만료 | 7~14일 |
| 알고리즘 | RS256 (비대칭) 또는 HS256 (대칭) |
| 저장소 | httpOnly + secure + sameSite cookie |
| Payload | 최소 정보만 (userId, role) — PII 금지 |
| 갱신 전략 | Silent Refresh 또는 Rotation |

### 비밀번호 정책
- 최소 8자, 대소문자+숫자+특수문자 권장 (강제보다 강도 표시)
- bcrypt (cost factor 12+) 또는 Argon2id
- 비밀번호 히스토리 (최근 5개 재사용 금지)
- 로그인 실패 5회 시 임시 잠금 (15분) 또는 CAPTCHA

## 인가 (Authorization) 패턴

### RBAC (역할 기반)
```
역할 정의: admin, manager, user, viewer
권한 매핑:
  admin    → *.* (전체)
  manager  → resource.create, resource.read, resource.update
  user     → resource.create (own), resource.read (own)
  viewer   → resource.read (public)
```

### 미들웨어 체인
```
요청 → [Rate Limit] → [인증: JWT 검증] → [인가: 역할 확인] → [입력 검증] → 핸들러
```

## 입력 검증 체크리스트

| 검증 항목 | 방법 | 도구 |
|----------|------|------|
| **타입 검증** | 스키마 검증 | Zod, Joi, class-validator |
| **길이 제한** | 최소/최대 길이 | 스키마에 min/max |
| **패턴 매칭** | 이메일, URL, 전화번호 | 정규식 + 라이브러리 |
| **범위 검증** | 숫자 범위, 날짜 범위 | min/max 값 |
| **열거형** | 허용된 값 목록 | enum 타입 |
| **SQL Injection** | 파라미터화 쿼리 | ORM (Prisma, TypeORM) |
| **XSS** | HTML 이스케이핑 | DOMPurify (클라이언트), 서버 이스케이프 |
| **Path Traversal** | 경로 정규화 | path.resolve + 화이트리스트 |
| **파일 업로드** | 타입/크기 검증 | MIME 타입 + 매직넘버 검증 |

## HTTP 보안 헤더

| 헤더 | 값 | 목적 |
|------|---|------|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | HTTPS 강제 |
| `X-Content-Type-Options` | `nosniff` | MIME 스니핑 방지 |
| `X-Frame-Options` | `DENY` 또는 `SAMEORIGIN` | 클릭재킹 방지 |
| `Content-Security-Policy` | `default-src 'self'` | XSS 방지 |
| `X-XSS-Protection` | `0` (CSP로 대체) | 레거시 |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 리퍼러 정보 제한 |
| `Permissions-Policy` | `camera=(), microphone=()` | 브라우저 기능 제한 |

## CORS 설정 가이드

| 환경 | 설정 |
|------|------|
| 개발 | `origin: 'http://localhost:3000'` |
| 프로덕션 | `origin: ['https://example.com']` — 도메인 명시 |
| 금지 | `origin: '*'` + `credentials: true` — 보안 위험 |

필수 설정:
- `methods`: 필요한 메서드만 허용
- `allowedHeaders`: 필요한 헤더만
- `credentials`: 쿠키 필요 시에만 true
- `maxAge`: 프리플라이트 캐싱 (86400초)

## Rate Limiting 전략

| 대상 | 제한 | 구현 |
|------|------|------|
| 인증 엔드포인트 | 5회/분/IP | IP 기반 |
| API 일반 | 100회/분/사용자 | 토큰 기반 |
| 파일 업로드 | 10회/시간/사용자 | 토큰 기반 |
| 비인증 API | 30회/분/IP | IP 기반 |

### 응답 헤더
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1609459200
Retry-After: 60 (429 응답 시)
```

## 에러 응답 보안

### 프로덕션 에러 응답 규칙
- 내부 구현 세부사항 절대 노출 금지 (스택 트레이스, SQL 쿼리)
- 일관된 에러 형식 사용
- 열거 공격 방지: 로그인 실패 시 "이메일 또는 비밀번호가 올바르지 않습니다" (어느 것이 틀렸는지 X)

### 에러 응답 형식
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "입력값이 올바르지 않습니다",
    "details": [
      {"field": "email", "message": "유효한 이메일을 입력하세요"}
    ]
  }
}
```

## 민감 데이터 처리

| 데이터 유형 | 저장 | 전송 | 로깅 |
|-----------|------|------|------|
| 비밀번호 | bcrypt 해시만 | HTTPS only | 절대 금지 |
| API Key | 환경변수 | 헤더 (Authorization) | 마스킹 (앞4자리만) |
| 개인정보 (PII) | 암호화 (AES-256) | HTTPS only | 마스킹 |
| 신용카드 | 토큰화 (PG사 위임) | PG사 SDK | 절대 금지 |
| 세션/토큰 | httpOnly cookie | HTTPS only | 절대 금지 |
