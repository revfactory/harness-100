# Side Project Launcher Harness

A harness where an agent team collaborates to produce side project planning deliverables — idea validation, tech stack selection, MVP spec, development roadmap, and launch checklist.

## Structure

```
.claude/
├── agents/
│   ├── idea-validator.md      — Idea validation (market analysis, competitive research, differentiation)
│   ├── techstack-analyst.md   — Tech stack analysis (selection criteria, comparison, recommendations)
│   ├── mvp-designer.md        — MVP design (core features, wireframes, spec)
│   ├── roadmap-builder.md     — Roadmap creation (development schedule, milestones, launch strategy)
│   └── launch-reviewer.md     — Cross-verification (idea ↔ tech ↔ MVP ↔ roadmap consistency)
├── skills/
│   ├── side-project-launcher/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── market-sizing-calculator/
│   │   └── skill.md           — Market sizing calculator (for idea-validator)
│   └── techstack-decision-matrix/
│       └── skill.md           — Tech stack decision matrix (for techstack-analyst)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/side-project-launcher` skill, or make a natural language request such as "Help me plan a side project."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_idea_validation.md` — Idea validation report
- `02_techstack_recommendation.md` — Tech stack recommendation
- `03_mvp_spec.md` — MVP spec document
- `04_roadmap_launch.md` — Development roadmap + launch checklist
- `05_review_report.md` — Review report
