# Anti-Bot And Compliance

Use this for passive, defensive assessment and compliant collection design.

## Non-Negotiable Boundary

Do not build or explain CAPTCHA solving, credential bypass, paywall bypass, stealth evasion, or aggressive fingerprint spoofing. If a site presents hard anti-bot controls, propose official APIs, feeds, partnerships, exports, or reduced manual workflows.

## Blocked-Content Request Handling

If the user asks to bypass access controls, collect member-only/paywalled text, evade 403/429, solve CAPTCHA, reuse login sessions without a clear authorized export, rotate identities to avoid rate limits, or "use every possible method" to get blocked content:

- Refuse the bypass portion directly.
- Do not add bypass steps to generated code, plans, skills, or runbooks.
- Preserve the useful goal by offering compliant paths:
  - official API or developer portal
  - RSS/Atom or sitemap
  - user-provided HTML/Markdown/PDF/export file from an account they are authorized to use
  - author/publisher permission
  - public preview metadata and summary
  - manual clipping/import workflow with attribution
- Document the blocked status and the exact safe next input needed.
- For copyrighted articles, avoid storing the full article text unless the user provides a lawful source and explicitly asks to process it; prefer metadata, short excerpts, summary, and structured notes.

## Full-Text Storage Policy

Full text is allowed only when the rights basis is clear:

- user-owned content
- user-provided HTML/Markdown/PDF/export from an account or source they are authorized to use
- public domain, open license, public dataset, or explicit redistribution permission
- documented author/publisher permission

When full text is allowed, save:

- `source_rights.md`: rights basis, source URL, license/permission note, access date
- `full_text.md`: cleaned full text
- `source.html`: original HTML only if user-provided or explicitly permitted

When full text is not allowed, save only:

- metadata
- short excerpts within allowed limits
- summaries
- structured notes
- links and citation/provenance

## Defense Levels

| Level | Defense | Detection | Compliant Response |
|---|---|---|---|
| 0 | No obvious defense | normal 200 responses | polite rate limiting |
| 1 | robots, UA checks, referer checks, rate limit | robots.txt, 403/429 | comply with robots, identify client, slow down |
| 2 | cookies, JS rendering, CSRF, public API auth | Set-Cookie, empty body, hidden tokens, 401 | session handling if allowed, official API, browser rendering only if permitted |
| 3 | Cloudflare/Akamai challenges, CAPTCHA, fingerprinting | challenge pages, CAPTCHA DOM, bot cookies | stop scraping design, find compliant alternatives |

## Passive Detection Flow

1. Inspect robots.txt and sitemap.
2. Fetch or inspect public HTML/API only when permitted by the task and environment.
3. Compare static response vs expected content.
4. Review headers and status codes for 401, 403, 429, 503.
5. Note challenge/captcha indicators without trying to defeat them.
6. Output a risk level and compliant path.

## Rate Limit Design

Use the most conservative value among robots crawl-delay, response time, and a baseline delay.

```text
base_delay = max(robots_crawl_delay, response_time * 5, 1.0)
jitter = random value from 0 to base_delay * 0.5
delay = base_delay + jitter

on HTTP 429:
  delay = min(base_delay * (2 ** retry_count), 300 seconds)
```

Also consider reducing activity during the target site's peak business hours.

## robots.txt Checklist

- Crawl-delay.
- Sitemap URLs.
- Disallow patterns.
- Allow exceptions.
- User-agent specific rules.
- Whether the requested target path is allowed.

## Compliant Alternative Search Order

1. Official API or developer portal.
2. RSS/Atom feed.
3. Sitemap XML.
4. Open data or public dataset.
5. Export/download feature.
6. Partnership or permission request.
7. Web archive only for historical, non-real-time needs.

## Legal And Privacy Risk Checklist

| Item | Risk Signal |
|---|---|
| robots.txt ignored | high |
| ToS prohibits scraping | high |
| personal data collected | high |
| copyrighted content copied at scale | high |
| login/session required | medium to high |
| high request volume | high |
| analysis-only public metadata | lower, still review |

## Report Snippet

```markdown
## 안티봇/준수 분석
- 방어 수준:
- robots.txt 결과:
- 허용 가능한 수집 범위:
- 중단해야 할 범위:
- 권장 대안:
- 잔여 리스크:
```
