---
name: web-scraper
description: "Use this skill for safe and compliant web scraping, crawler development, site data collection, web crawling systems, parser design, structured data extraction, scraper monitoring, and scraping feasibility analysis. It produces target analysis, crawler design, parser logic, data storage plan, monitoring config, and runnable source code under _workspace/YYYY-MM-DD/NN-slug/. Use it for requests like 웹 스크래핑 만들어줘, 크롤러 개발해줘, 사이트 데이터 수집, 웹 크롤링 시스템, 스크래퍼 구축, 사이트 파싱, and 웹 데이터 추출. Do not use it for unauthorized access, CAPTCHA solving, login bypass, aggressive anti-bot circumvention, personal-data harvesting, streaming data pipelines, browser test automation, or website performance monitoring."
---

# Web Scraper

대상 URL, 샘플 파일, 기존 크롤러 코드를 바탕으로 안전하고 유지보수 가능한 웹 스크래핑 패키지를 만든다. 사용자가 다른 언어를 요청하지 않으면 한국어로 작업한다.

## 사용법

다음과 같은 요청에 이 스킬을 사용한다:

- "웹 스크래핑 시스템 만들어줘"
- "이 사이트에서 상품명과 가격을 수집하는 크롤러 만들어줘"
- "이 사이트 스크래핑 가능한지 먼저 분석해줘"
- "기존 크롤러 코드에 파서와 모니터링을 추가해줘"

작업을 시작하면 먼저 출력 폴더를 정한다. 모든 산출물은 `_workspace/날짜/순번-작업명/` 하위에 저장한다.

예:

```text
_workspace/2026-05-16/01-news-price-scraper/
├── 00_input.md
├── 01_target_analysis.md
├── 02_crawler_design.md
├── 03_parser_logic.md
├── 04_data_storage.md
├── 05_monitor_config.md
└── src/
```

폴더명 규칙:

- 날짜는 현재 날짜의 `YYYY-MM-DD` 형식을 사용한다.
- 순번은 같은 날짜 폴더 안의 기존 작업 폴더를 확인한 뒤 `01`, `02`, `03`처럼 두 자리로 증가시킨다.
- 작업명은 URL/주제에서 만든 짧은 영문 slug를 사용한다. 예: `naver-news`, `product-price`, `job-postings`.
- 이후 문서에서 `_workspace/`라고 쓰인 경로는 이 작업 폴더를 기준으로 해석한다.

## Safety Boundary

- Prefer official APIs, RSS/Atom feeds, sitemap data, open data portals, and documented exports before scraping HTML.
- Respect robots.txt, site terms, rate limits, authentication boundaries, and privacy constraints.
- Do not provide CAPTCHA solving, credential bypass, paywall bypass, stealth evasion, or instructions to defeat access controls.
- If a site blocks scraping or disallows the target path, document the finding and propose compliant alternatives.
- For public security or anti-bot analysis, stay passive and defensive unless the user provides explicit authorization.

## 차단/회원 전용 콘텐츠 처리

사용자가 "우회해서라도", "가능한 모든 방법", "로그인/Paywall/CAPTCHA를 넘어", "403을 뚫고"처럼 접근 제한 회피를 요청하면 해당 우회 방법은 제공하거나 구현하지 않는다. 대신 다음 순서로 전환한다:

1. 접근 제한의 근거를 기록한다: HTTP 상태, robots.txt, 로그인/회원 전용 표시, CAPTCHA/challenge 여부.
2. 공개적으로 허용된 대체 소스를 찾는다: 공식 API, RSS/Atom, sitemap, 공개 데이터셋, export/download, 작성자 제공 자료.
3. 사용자가 합법적으로 접근 권한이 있는 경우, 사용자가 직접 제공한 HTML/Markdown/PDF/export 파일을 입력으로 받아 파싱한다.
4. 본문 전체를 저장할 수 없는 저작권 콘텐츠는 메타데이터, 짧은 허용 범위의 발췌, 요약, 구조화 메모만 저장한다.
5. 결과 문서에 "우회하지 않았음"과 남은 한계를 명시한다.

## 전체 원문 저장 조건

전체 원문 저장은 기본 동작이 아니다. 다음 중 하나가 명확할 때만 `full_text.md` 또는 `source.html`을 만든다:

- 사용자가 본인 소유 콘텐츠라고 명시했다.
- 사용자가 합법적으로 접근 권한이 있는 HTML/Markdown/PDF/export 파일을 직접 제공했다.
- 대상 콘텐츠가 공개 라이선스, 공공 데이터, 퍼블릭 도메인, 또는 명시적 재배포 허용 조건을 가진다.
- 작성자/발행자의 저장·재사용 허가가 확인되었다.

위 조건이 확인되지 않은 일반 웹 글, 블로그, 뉴스, Medium/멤버십 글 등은 원문 전체를 저장하지 않는다. 이 경우 `article.md`, `public_preview.md`, `summary.md`, `metadata.json`처럼 메타데이터, 제한된 미리보기, 요약, 구조화 메모만 저장한다.

전체 원문 저장이 허용되는 경우에도 다음을 함께 저장한다:

- `source_rights.md`: 저장 근거, 라이선스/허가, 출처 URL, 접근 날짜
- `full_text.md`: 정제된 전체 텍스트
- `source.html`: 사용자가 제공했거나 저장 허용이 확인된 경우에만 원본 HTML

## Output Contract

Create or update these files under the current work folder, not directly under the root `_workspace/`. The work folder must follow `_workspace/YYYY-MM-DD/NN-slug/`.

- `00_input.md`: normalized target, desired data, purpose, scale, constraints, source files
- `01_target_analysis.md`: site structure, robots/ToS notes, URL/API patterns, risk assessment
- `02_crawler_design.md`: crawler architecture, request strategy, retry/backoff, implementation notes
- `03_parser_logic.md`: schema, selectors, parsing/normalization logic, validation rules
- `04_data_storage.md`: storage choice, schema, upsert/deduplication, export and backup plan
- `05_monitor_config.md`: schedule, health checks, selector-change detection, logging, alerts
- `source_rights.md`: rights/license basis when full text is requested
- `full_text.md`: full cleaned text only when the full-text storage conditions are met
- `src/`: runnable source code when implementation is requested and feasible

If a step cannot be executed because of access restrictions, missing dependencies, or policy limits, still create the relevant design artifact and mark the limitation clearly.

## Workflow

1. Parse the request.
   - Extract target URL/site, desired data fields, purpose, volume, frequency, output format, tech stack constraints, and legal/compliance constraints.
   - If only a URL is supplied, produce analysis first and list feasible data candidates before implementing a crawler.
   - If the user requests full original text, first determine whether the full-text storage conditions are met. If not, produce metadata/preview/summary instead.
2. Prepare the dated work folder.
   - Create `_workspace/YYYY-MM-DD/` if it does not exist.
   - Inspect existing folders under that date and choose the next two-digit sequence.
   - Create `_workspace/YYYY-MM-DD/NN-slug/` and treat it as the current work folder.
   - Save the normalized brief to `00_input.md` inside that folder.
   - Create `src/` inside that folder when code is requested.
   - Copy or summarize existing crawler/parser files into the workspace when provided.
3. Analyze before coding.
   - Review robots.txt and known public alternatives.
   - Identify rendering mode: static HTML, JSON API, SPA, hybrid.
   - Map target fields to URL patterns, API paths, DOM selectors, or JSON paths.
   - Assess legal risk, technical difficulty, rate limits, and data privacy concerns.
   - Record the full-text rights decision in `source_rights.md` whenever full text is requested.
   - If the request asks for bypassing access controls, switch to the blocked-content workflow above and do not implement bypass tactics.
4. Choose the production mode.
   - Analysis mode: `01_target_analysis.md` only, plus recommendations.
   - Crawler mode: analysis plus `02_crawler_design.md` and crawler code.
   - Parser mode: parser logic and tests/fixtures from supplied HTML or JSON.
   - Storage mode: schema, deduplication, export, and backup plan.
   - Monitoring mode: schedule, health checks, logging, alerts, and selector drift detection.
   - Full pipeline: all artifacts and runnable source code where feasible.
5. Implement conservatively.
   - Use the repo's existing language and tooling when present.
   - For a new small scraper on this Windows harness, Node.js standard library is a safe fallback when Python is unavailable.
   - Add rate limiting, backoff, timeouts, structured logs, and raw-response preservation.
   - Include fixture-based tests when possible instead of depending only on live site access.
6. Verify before completion.
   - Confirm promised artifacts exist.
   - Run the available test or lint command.
   - If live access is blocked, treat that as a valid result and verify with fixtures or saved samples.

## Codex Collaboration Rules

- Do not rely on legacy harness commands, hooks, browser-only fetch tools, or custom message-passing APIs.
- Use normal Codex file editing and verification.
- Use Codex subagents only when the user explicitly asks for subagents/delegation/parallel agent work; otherwise perform the role passes yourself using the role guides.
- Keep durable outputs in the dated `_workspace/YYYY-MM-DD/NN-slug/` work folder, not only in chat.
- Do not invent live-site findings. If you did not fetch or inspect the target in the current task, label conclusions as assumptions.

## Role Passes

Read [role-guides.md](references/role-guides.md) when detailed artifact templates are needed.

- Target analyst: site structure, robots/ToS notes, APIs, URL patterns, risk.
- Crawler developer: request flow, rate limiting, retries, sessions, implementation.
- Parser engineer: CSS/XPath/JSON paths, normalization, validation, fixtures.
- Data manager: schema, deduplication, incremental updates, exports, backup.
- Monitor operator: scheduling, health checks, selector drift, logs, alerts.

## Specialist References

Load these only when needed:

- [anti-bot-and-compliance.md](references/anti-bot-and-compliance.md): defensive anti-bot assessment, rate limit design, compliant alternatives, legal risk checklist.
- [selector-patterns.md](references/selector-patterns.md): selector priority, CSS/XPath recipes, robustness scoring, drift detection, data cleaning.

## Completion Report

End with:

- Created/updated artifact paths.
- Verification command and result.
- Any access/compliance limitation.
- Suggested next executable step, such as supplying sample HTML, approving a public URL fetch, or running the generated scraper.
