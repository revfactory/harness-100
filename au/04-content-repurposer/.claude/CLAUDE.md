# Content Repurposer Harness

A harness where an agent team transforms a single source piece of content into multiple formats: blog posts, social media, newsletters, presentations, and scripts.

## Structure

```
.claude/
├── agents/
│   ├── source-analyst.md        — Source Analyst (structure analysis, key extraction, conversion strategy)
│   ├── blog-writer.md           — Blog Writer (SEO-optimized blog posts)
│   ├── sns-copywriter.md        — Social Media Copywriter (platform-specific posts)
│   ├── presentation-builder.md  — Presentation Builder (slide composition)
│   └── quality-reviewer.md      — Quality Reviewer (cross-validation, message consistency)
├── skills/
│   ├── content-repurposer/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── platform-adaptation/
│   │   └── skill.md             — sns-copywriter+blog-writer extension (platform DNA, conversion matrix)
│   └── content-atomization/
│       └── skill.md             — source-analyst+presentation-builder extension (MINE analysis, atom classification)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/content-repurposer` skill, or make a natural language request like "repurpose this content for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_source_analysis.md` — Source analysis report
- `02_blog_post.md` — Blog post
- `03_sns_package.md` — Social media post package
- `04_presentation.md` — Presentation slides
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 28 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
