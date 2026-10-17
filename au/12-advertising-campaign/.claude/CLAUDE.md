# Advertising Campaign Harness

A harness where an agent team collaborates to design advertising campaigns: target analysis, copy, creative, and media plans.

## Structure

```
.claude/
├── agents/
│   ├── market-analyst.md        — Market/Target Analysis (audience segmentation, competitive ad analysis, insight extraction)
│   ├── copywriter.md            — Ad Copywriting (headlines, body copy, CTAs, tone & voice)
│   ├── creative-director.md     — Creative Design (visual concepts, storyboards, image generation)
│   ├── media-planner.md         — Media Planning (channel selection, budget allocation, scheduling)
│   └── campaign-reviewer.md     — Campaign QA (strategy<->copy<->creative<->media consistency verification)
├── skills/
│   ├── advertising-campaign/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── ad-copywriting-formulas/
│   │   └── skill.md             — copywriter extension (AIDA/PAS/BAB persuasion formulas, psychological triggers, channel-specific character limits)
│   └── media-mix-calculator/
│       └── skill.md             — media-planner extension (GRP/CPM/ROAS calculations, budget allocation models, benchmarks)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/advertising-campaign` skill, or make a natural language request such as "Plan an advertising campaign."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_market_analysis.md` — Market/target analysis report
- `02_ad_copy.md` — Ad copy set
- `03_creative_concept.md` — Creative concept/storyboards
- `04_media_plan.md` — Media plan
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 17 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
