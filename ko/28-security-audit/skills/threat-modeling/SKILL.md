---
name: threat-modeling
description: "STRIDE, DREAD, Attack Tree 등 위협 모델링 방법론과 위협 식별·평가·대응 전략 수립 가이드. 'STRIDE', 'DREAD', '위협 모델링', 'threat modeling', '공격 트리', 'attack surface', '위협 식별', '보안 설계' 등 시스템 위협 분석 시 이 스킬을 사용한다. security-consultant와 pentest-reporter의 위협 분석 역량을 강화한다. 단, 실제 침투 테스트 실행이나 CVE 스캐닝은 이 스킬의 범위가 아니다."
---

# Threat Modeling — 위협 모델링 방법론 가이드

시스템의 보안 위협을 체계적으로 식별하고 평가하는 프레임워크.

## STRIDE 위협 분류

| 위협 | 설명 | 보안 속성 | 대응 패턴 |
|------|------|----------|----------|
| **S**poofing | 신원 위장 | 인증 | MFA, 인증서 |
| **T**ampering | 데이터 변조 | 무결성 | HMAC, 디지털 서명, 체크섬 |
| **R**epudiation | 행위 부인 | 부인 방지 | 감사 로그, 타임스탬프 |
| **I**nformation Disclosure | 정보 누출 | 기밀성 | 암호화, 접근 제어 |
| **D**enial of Service | 서비스 거부 | 가용성 | Rate Limiting, 오토스케일링 |
| **E**levation of Privilege | 권한 상승 | 인가 | RBAC, 최소 권한 원칙 |

## STRIDE 적용 절차

### Step 1: 시스템 분해 (DFD 작성)

```
┌────────┐    HTTPS     ┌──────────┐    SQL     ┌─────────┐
│ Browser │ ──────────→ │ Web App  │ ────────→ │   DB    │
│(외부)   │ ←────────── │(Trust    │ ←──────── │(Trust   │
└────────┘             │ Boundary)│           │Boundary)│
                       └────┬─────┘           └─────────┘
                            │ REST API
                            ▼
                       ┌──────────┐
                       │ 외부 PG  │
                       │(외부)    │
                       └──────────┘

Trust Boundary(신뢰 경계)에서 위협이 발생한다.
```

### Step 2: 요소별 STRIDE 분석

```markdown
## Browser → Web App (HTTPS)
| 위협 | 시나리오 | 위험도 | 대응 |
|------|---------|--------|------|
| S | 세션 하이재킹 | 높음 | HttpOnly, Secure 쿠키 |
| T | 중간자 공격 | 높음 | TLS 1.3, HSTS |
| R | 익명 요청 | 중간 | 요청 로깅, 인증 필수 |
| I | 전송 중 도청 | 높음 | TLS |
| D | DDoS | 높음 | WAF, Rate Limiting |
| E | 관리자 API 접근 | 높음 | 역할 기반 접근 제어 |
```

## DREAD 위험 평가

```
각 항목 1~10점 평가:

D (Damage): 피해 규모
R (Reproducibility): 재현 용이성
E (Exploitability): 공격 용이성
A (Affected Users): 영향 사용자 비율
D (Discoverability): 발견 용이성

위험도 = (D + R + E + A + D) / 5

등급:
├── 8~10: Critical (즉시 대응)
├── 5~7: High (계획된 수정)
├── 3~4: Medium (모니터링)
└── 1~2: Low (수용)
```

### 예시 평가

```
위협: SQL Injection in Login API
├── Damage: 9 (전체 DB 탈취 가능)
├── Reproducibility: 8 (자동화 도구 존재)
├── Exploitability: 7 (공개 PoC 다수)
├── Affected Users: 10 (전체 사용자)
├── Discoverability: 9 (자동 스캐너로 발견)
└── 위험도: (9+8+7+10+9)/5 = 8.6 → Critical
```

## Attack Tree

```
목표: 관리자 권한 획득
├── OR: 인증 우회
│   ├── AND: SQL Injection + 약한 비밀번호 해시
│   ├── 세션 하이재킹
│   │   ├── OR: XSS로 쿠키 탈취
│   │   └── OR: 네트워크 스니핑 (HTTP)
│   └── 디폴트 관리자 계정
├── OR: 권한 상승
│   ├── IDOR (관리자 API 직접 호출)
│   ├── JWT 변조 (role 필드)
│   └── API Gateway 우회
└── OR: 사회공학
    ├── 관리자 피싱
    └── 내부자 공모
```

## 공격 표면 분석

### 웹 애플리케이션 공격 표면

| 표면 | 요소 | 점검 항목 |
|------|------|----------|
| **외부 API** | REST/GraphQL 엔드포인트 | 인증, 인가, 입력 검증 |
| **인증** | 로그인, 토큰, 세션 | 브루트포스, 세션 관리 |
| **파일 업로드** | 프로필, 첨부파일 | 파일 유형 검증, 경로 조작 |
| **제3자 연동** | OAuth, Webhook, API | SSRF, 토큰 노출 |
| **관리 인터페이스** | Admin 패널, API | 접근 제어, 망 분리 |
| **데이터 저장** | DB, 캐시, 로그 | 암호화, 접근 제어 |

## 위협 모델링 보고서 템플릿

```markdown
# 위협 모델링 보고서

## 시스템 개요
- 아키텍처 다이어그램 (DFD)
- 신뢰 경계 식별

## 위협 목록
| ID | STRIDE | 위협 시나리오 | DREAD 점수 | 현재 대응 | 잔여 위험 |
|----|--------|-------------|-----------|----------|----------|
| T1 | S | 세션 하이재킹 | 7.2 | HttpOnly 쿠키 | 중간 |
| T2 | I | SQL Injection | 8.6 | 파라미터화 쿼리 | 낮음 |

## 공격 표면 요약
## 우선순위별 대응 계획
## 잔여 위험 수용 목록
```
