# Brand Identity Harness

A harness where an agent team collaborates to design brand identity from naming through slogans, tone and manner, and visual guidelines.

## Structure

```
.claude/
├── agents/
│   ├── naming-specialist.md    — Naming Specialist (brand names, domains, trademark review)
│   ├── copywriter.md           — Copywriter (slogans, taglines, brand story)
│   ├── visual-director.md      — Visual Director (color, typography, logo concepts)
│   ├── brand-strategist.md     — Brand Strategist (positioning, target audience, competitive analysis)
│   └── identity-reviewer.md    — Identity Reviewer (cross-validation, consistency checks)
├── skills/
│   ├── brand-identity/
│   │   └── skill.md            — Orchestrator (team coordination, workflow, error handling)
│   ├── naming-methodology/
│   │   └── skill.md            — naming-specialist extension (12 techniques, SMILE evaluation, phonology)
│   ├── color-psychology/
│   │   └── skill.md            — visual-director extension (color psychology, 60-30-10, accessibility)
│   └── brand-archetype/
│       └── skill.md            — brand-strategist+copywriter extension (12 archetypes, tone and voice)
└── CLAUDE.md                   — This file
```

## Usage

Trigger the `/brand-identity` skill, or use natural language such as "Create a brand identity for me."

## Deliverables

All deliverables are saved to the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_brand_strategy.md` — Brand strategy report
- `02_naming_candidates.md` — Naming candidates
- `03_verbal_identity.md` — Verbal identity (slogans, tone and manner)
- `04_visual_identity.md` — Visual identity (colour, typography, logo)
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 1 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 71 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
