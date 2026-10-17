# YouTube Production Harness

A harness where an agent team collaborates to produce YouTube video content through the pipeline of strategy, script, thumbnail, and SEO.

## Structure

```
.claude/
├── agents/
│   ├── content-strategist.md  — Content strategy (topic analysis, competitive benchmarking, concept design)
│   ├── scriptwriter.md        — Script writing (hook, segments, CTA, visual cues)
│   ├── thumbnail-designer.md  — Thumbnail design + Gemini image generation
│   ├── seo-optimizer.md       — SEO package (title/description/tags/chapters/subtitles)
│   └── production-reviewer.md — Cross-validation (strategy↔script↔thumbnail↔SEO consistency)
├── skills/
│   └── youtube-production/
│       └── skill.md           — Orchestrator (team coordination, workflow, error handling)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/youtube-production` skill, or make a natural language request like "plan a YouTube video for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_strategist_brief.md` — Strategy brief
- `02_scriptwriter_script.md` — Video script
- `03_thumbnail_concept.md` — Thumbnail concept
- `04_seo_package.md` — SEO package
- `05_review_report.md` — Review report
- `subtitle.srt` — Subtitle file

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 41 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
