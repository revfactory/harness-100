# Presentation Designer Harness

A harness where an agent team collaborates to produce presentations: planning, storyboards, slides, and speaker notes.

## Structure

```
.claude/
├── agents/
│   ├── storyteller.md           — Story Design (message structuring, logical flow, audience analysis)
│   ├── info-architect.md        — Information Architecture (data visualization, chart selection, information hierarchy)
│   ├── visual-designer.md       — Visual Design (slide layout, color, typography, images)
│   ├── presentation-coach.md    — Presentation Coaching (speaker notes, timing, Q&A prep, rehearsal guide)
│   └── deck-reviewer.md         — Deck QA (story<->info<->visual<->presentation consistency verification)
├── skills/
│   ├── presentation-designer/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── slide-layout-patterns/
│   │   └── skill.md             — visual-designer extension (20 layout patterns, grids, design tokens)
│   └── data-visualization-guide/
│       └── skill.md             — info-architect extension (chart selection matrix, LATCH, color accessibility)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/presentation-designer` skill, or make a natural language request such as "Create a presentation."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_story_structure.md` — Story structure/message map
- `02_info_design.md` — Information design/data visualisation guide
- `03_slide_deck.md` — Slide deck (markdown-based)
- `04_speaker_notes.md` — Speaker notes/timing/Q&A
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 50 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
