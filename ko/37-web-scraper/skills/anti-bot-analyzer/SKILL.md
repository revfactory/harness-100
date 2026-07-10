---
name: anti-bot-analyzer
description: "웹사이트의 안티봇 방어 메커니즘을 분석하고 합법적 우회 전략을 수립하는 스킬. '안티봇 분석해줘', '봇 차단 우회', 'Cloudflare 대응', '캡차 감지', 'rate limit 확인' 등 안티봇 분석 시 사용한다. 단, 불법적 우회 도구 개발, CAPTCHA 자동 풀이 서비스, 개인정보 침해 스크래핑은 이 스킬의 범위가 아니다."
---

# Anti-Bot Analyzer — 안티봇 방어 분석 + 합법적 대응

target-analyst와 crawler-developer의 안티봇 분석 역량을 강화하는 스킬.

## 대상 에이전트

- **target-analyst** — 대상 사이트의 방어 수준을 사전 평가
- **crawler-developer** — 분석 결과 기반 합법적 크롤러 전략 수립

## 안티봇 방어 계층 분류

### Level 1: 기본 방어 (난이도: 하)
| 방어 | 감지 방법 | 대응 전략 |
|------|----------|----------|
| robots.txt | `GET /robots.txt` | 규칙 준수 (Crawl-delay, Disallow) |
| User-Agent 필터 | 403/429 응답 | 실제 브라우저 UA 헤더 설정 |
| Referer 검사 | 빈 Referer 시 차단 | 적절한 Referer 헤더 설정 |
| IP Rate Limit | 짧은 간격 시 429 | `time.sleep()` + 랜덤 지연 |

### Level 2: 중급 방어 (난이도: 중)
| 방어 | 감지 방법 | 대응 전략 |
|------|----------|----------|
| 쿠키 기반 세션 | Set-Cookie 추적 | `requests.Session()` 유지 |
| JavaScript 렌더링 필수 | 빈 HTML body | Playwright/Puppeteer 사용 |
| 동적 토큰 (CSRF) | hidden input | 토큰 추출 후 요청에 포함 |
| API 인증 | 401 응답 | 공개 API 키 분석 |

### Level 3: 고급 방어 (난이도: 상)
| 방어 | 감지 방법 | 대응 전략 |
|------|----------|----------|
| Cloudflare | `cf-` 쿠키, challenge 페이지 | 합법적 API 탐색 |
| Akamai Bot Manager | `_abck` 쿠키 | 공식 API/RSS 대안 탐색 |
| 브라우저 핑거프린팅 | navigator/WebGL 검사 | 스텔스 플러그인 |
| reCAPTCHA/hCaptcha | `g-recaptcha` DOM | API 대안 사용 |
| TLS 핑거프린팅 (JA3) | 비표준 TLS 차단 | curl_cffi |

## 방어 수준 자동 감지 플로우

```
1. HTTP 요청 (UA 없음)
   ├── 200 OK → Level 0 (방어 없음)
   └── 403/503 → UA 필터 의심

2. HTTP 요청 (Chrome UA)
   ├── 200 + 데이터 → Level 1
   ├── 200 + 빈 body → JS 렌더링 필요 (Level 2)
   └── 403/503 → Level 2+

3. 응답 헤더 분석
   ├── server: cloudflare → Cloudflare
   ├── x-akamai-* → Akamai
   └── set-cookie: __cf_bm → CF Bot Management

4. HTML 분석
   ├── <script src="captcha"> → CAPTCHA
   └── API 엔드포인트 탐색 (XHR/fetch)

5. 최종: Level 0~3 + 방어 목록 출력
```

## Rate Limit 설계 공식

```python
base_delay = max(robots_crawl_delay, response_time * 5, 1.0)
actual_delay = base_delay + random.uniform(0, base_delay * 0.5)

# 429 시 지수 백오프
backoff_delay = base_delay * (2 ** retry_count)
max_backoff = 300  # 최대 5분

# 업무시간 배려
if is_business_hours(target_tz):
    actual_delay *= 2
```

## robots.txt 분석 체크리스트

```
1. Crawl-delay → base_delay 반영
2. Sitemap URL → 크롤링 대상 수집
3. Disallow 패턴 → URL 필터 적용
4. Allow 예외 → 허용 경로 명시
5. 특정 UA 규칙 → 커스텀 UA 전략
```

## 합법적 대안 탐색 순서

```
1. 공식 API → 최우선
2. RSS/Atom 피드 → /feed, /rss
3. Sitemap XML → URL 목록
4. Open Data / 공공 API → data.go.kr
5. 제휴/파트너 API
6. 웹 아카이브 → web.archive.org
```

## 법적 리스크 체크리스트

| 항목 | 리스크 |
|------|--------|
| robots.txt 준수 | 필수 |
| 이용약관 스크래핑 금지 조항 | 높음 |
| 개인정보 미수집 | 필수 |
| 저작권 확인 | 높음 |
| 서버 부하 미과중 | 필수 |
| 로그인 미사용 | 중간 |
| 데이터 용도 (분석 vs 재판매) | 높음 |

## 보고서 템플릿

```markdown
## 안티봇 분석 보고서
### 대상: [URL]
### 방어 수준: Level [0-3]
### 감지된 방어 메커니즘
| 방어 유형 | 상세 | 대응 가능 |
### robots.txt 분석
### 권장 전략
### 합법적 대안
### 법적 리스크 평가: [낮음/중간/높음]
```
