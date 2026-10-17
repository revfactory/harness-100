# Social Media Manager Harness

A harness where an agent team collaborates to produce SNS content calendars, post copy, hashtags, and performance analysis.

## Structure

```
.claude/
├── agents/
│   ├── sns-strategist.md       — SNS Strategist (channel analysis, content calendar, campaign design)
│   ├── copywriter.md           — Copywriter (post writing, captions, CTAs)
│   ├── visual-planner.md       — Visual Planner (image concepts, card news, Reels planning)
│   ├── hashtag-analyst.md      — Hashtag Analyst (hashtag strategy, trend analysis, performance prediction)
│   └── performance-reviewer.md — Performance Reviewer (KPI alignment, content quality, consistency)
├── skills/
│   ├── social-media-manager/
│   │   └── skill.md            — Orchestrator (team coordination, workflow, error handling)
│   ├── platform-algorithms/
│   │   └── skill.md            — sns-strategist+visual-planner extension (algorithms, golden hours)
│   ├── viral-copywriting/
│   │   └── skill.md            — copywriter extension (15 hook patterns, emotion triggers, CTAs)
│   └── hashtag-science/
│       └── skill.md            — hashtag-analyst extension (pyramid strategy, research, shadowban)
└── CLAUDE.md                   — This file
```

## Usage

Trigger the `/social-media-manager` skill, or make a natural language request such as "Create SNS content."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_strategy.md` — SNS strategy/content calendar
- `02_posts.md` — Post copy collection
- `03_visuals.md` — Visual plan
- `04_hashtags.md` — Hashtag strategy
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 39 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
