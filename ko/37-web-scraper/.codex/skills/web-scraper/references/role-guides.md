# Role Guides

Use these role lenses while producing the web scraping package.

## Workspace Rule

All artifact paths are relative to the current work folder:

```text
_workspace/YYYY-MM-DD/NN-slug/
```

Choose `NN` by checking existing folders under the same date and using the next two-digit sequence. Do not write new artifacts directly under the root `_workspace/`.

## Target Analyst

Purpose: decide whether scraping is feasible, safe, and worth implementing.

Principles:

- Check robots.txt and identify disallowed paths and crawl-delay when available.
- Prefer official APIs, RSS/Atom, sitemap XML, public datasets, or exports.
- Identify rendering mode: SSR/static HTML, CSR/SPA, JSON API, hybrid.
- Map target fields to DOM selectors, JSON paths, or API endpoints.
- Evaluate legal/privacy risk conservatively.
- If the user asks to bypass access controls or member-only/paywalled restrictions, mark that scope as not allowed and propose authorized inputs or public alternatives.
- If the user asks to save full original text, decide and document whether rights allow full-text storage. If not, restrict output to metadata, short excerpts, summaries, and structured notes.

`01_target_analysis.md` should include:

```markdown
# 대상 사이트 분석 보고서

## 사이트 개요
- URL:
- 사이트 유형:
- 렌더링 방식:
- 기술 스택:

## robots.txt / 이용 조건 메모
- Crawl-delay:
- Disallow 경로:
- Sitemap:
- 준수 전략:

## 데이터 포인트 매핑
| 데이터 항목 | 위치(CSS/XPath/JSON path/API) | 데이터 타입 | 비고 |
|---|---|---|---|

## URL/API 패턴
- 목록 페이지:
- 상세 페이지:
- 페이지네이션:
- 예상 수집 규모:

## 리스크 평가
- 법적/약관 리스크:
- 개인정보 리스크:
- 기술 난이도:
- 차단 가능성:

## 권장 접근
## 전체 원문 저장 가능 여부
- 판단:
- 근거:
- 허용 산출물:
## 크롤러 개발자 전달 사항
## 파서 엔지니어 전달 사항
## 데이터 관리자 전달 사항
```

## Crawler Developer

Purpose: design and implement polite, robust collection code.

Principles:

- Read `01_target_analysis.md` first.
- Respect crawl-delay and implement rate limiting.
- Prefer HTTP clients for static/API sources; use browser automation only when rendering is genuinely required and allowed.
- Use timeouts, retry/backoff, circuit breaker logic, and structured logs.
- Preserve raw responses or fixtures for debugging.

`02_crawler_design.md` should include:

```markdown
# 크롤러 설계 문서

## 아키텍처
- 크롤링 방식:
- 기술 스택:
- 큐 전략:

## 요청 전략
- Rate limit:
- 동시 요청 수:
- User-Agent:
- 세션/쿠키:

## 크롤링 플로우
1. 시드 URL 투입
2. 목록/API 페이지 수집
3. 상세 URL 또는 레코드 추출
4. 상세 페이지/API 수집
5. 원본 데이터를 파서에 전달

## 재시도 전략
| HTTP 상태/오류 | 전략 | 최대 재시도 |
|---|---|---|

## 핵심 코드
## 파서 엔지니어 전달 사항
## 모니터 운영자 전달 사항
```

## Parser Engineer

Purpose: transform raw HTML/JSON into typed records.

Principles:

- Base parsing on `01_target_analysis.md` and sample raw responses.
- Prefer stable selectors: IDs, `data-*`, semantic classes, ARIA, then structural selectors.
- Define fallback selectors and expected value patterns.
- Normalize dates, numbers, prices, units, whitespace, and URLs.
- Keep invalid or failed raw samples for debugging.

`03_parser_logic.md` should include:

```markdown
# 파싱 로직 설계서

## 데이터 스키마
| 필드명 | 타입 | 필수 | 메인 선택자/경로 | 폴백 | 정규화 규칙 |
|---|---|---|---|---|---|

## 파싱 플로우
1. HTML/JSON 수신
2. 인코딩/형식 정규화
3. 필드 추출
4. 타입 변환
5. 검증
6. 구조화 데이터 출력

## 에지 케이스
## 검증 규칙
## 핵심 코드
## 데이터 관리자 전달 사항
```

## Data Manager

Purpose: store records reliably and make exports useful.

Principles:

- Use incremental updates by default.
- Separate raw data from cleaned data.
- Define unique keys and upsert behavior.
- Include transaction, backup, and recovery strategy.
- Choose storage according to scale and purpose.

Storage defaults:

| Condition | Storage | Why |
|---|---|---|
| Under 100k rows, simple local use | SQLite | zero-server, reliable |
| Flexible stream/archive | JSONL | append-friendly |
| Larger relational data | PostgreSQL | ACID and indexing |
| Analytical export | Parquet + DuckDB | efficient columnar analysis |

`04_data_storage.md` should include:

```markdown
# 데이터 저장 설계서

## 저장소 선택
## 스키마 설계
## 인덱스 전략
## 중복 제거 전략
## 증분 업데이트
## 품질 검증 쿼리
## 내보내기 형식
## 백업 및 복구
## 모니터 운영자 전달 사항
```

## Monitor Operator

Purpose: make the scraper maintainable after the first successful run.

Principles:

- Focus on early warning before total failure.
- Log as structured JSON.
- Detect selector drift using expected counts, required fields, and sample hashes.
- Schedule according to data freshness, server load, robots crawl-delay, and business need.
- Debounce repeated alerts.

`05_monitor_config.md` should include:

```markdown
# 모니터링 및 운영 설정

## 스케줄링
- 크롤링 주기:
- 스케줄러:
- 동시 실행 방지:

## 헬스체크
| 체크 항목 | 주기 | 방법 | 정상 기준 |
|---|---|---|---|

## 사이트 변경 감지
## 로깅 설계
## 알림 규칙
## 장애 대응 매뉴얼
## 운영 대시보드 설계
```
