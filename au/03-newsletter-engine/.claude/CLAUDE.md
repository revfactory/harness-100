# Newsletter Engine Harness

A harness where an agent team collaborates to produce newsletter content through the pipeline of curation, writing, A/B testing, and send optimisation.

## Structure

```
.claude/
├── agents/
│   ├── curator.md             — Curator (source collection, trend analysis, content selection)
│   ├── copywriter.md          — Copywriter (headlines, body copy, CTA writing)
│   ├── analyst.md             — Analyst (A/B test design, send optimization, performance forecasting)
│   ├── editor-in-chief.md     — Editor-in-Chief (tone consistency, brand guide, final editing)
│   └── quality-reviewer.md    — Quality Reviewer (cross-validation, consistency checks)
├── skills/
│   ├── newsletter-engine/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── email-copywriting/
│   │   └── skill.md           — copywriter extension (CURVE subject lines, CTA design, F-pattern)
│   ├── audience-segmentation/
│   │   └── skill.md           — analyst+curator extension (BEAR model, send optimization)
│   └── deliverability-optimization/
│       └── skill.md           — editor-in-chief+analyst extension (spam filters, deliverability)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/newsletter-engine` skill, or make a natural language request like "write a newsletter for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_curation_brief.md` — Curation brief
- `02_newsletter_draft.md` — Newsletter draft
- `03_ab_test_plan.md` — A/B test plan
- `04_editorial_final.md` — Editor-in-Chief final version
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 4 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 53 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
