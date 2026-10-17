# Onboarding System Harness

New hire onboarding: A harness where an agent team collaborates to generate everything from checklists to training, mentor assignments, and 30-60-90 day plans.

## Structure

```
.claude/
├── agents/
│   ├── onboarding-architect.md   — Onboarding design (checklists, schedules, milestones)
│   ├── training-builder.md       — Training content (curriculum, materials, quizzes)
│   ├── mentor-matcher.md         — Mentor/buddy assignment (criteria, matching, guides)
│   ├── milestone-tracker.md      — 30-60-90 days (goals, evaluation, feedback)
│   └── experience-reviewer.md    — Experience review (consistency, improvements, reports)
├── skills/
│   ├── onboarding-system/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── learning-path-design/
│   │   └── skill.md              — Learning path design (training-builder extension)
│   └── buddy-program-guide/
│       └── skill.md              — Buddy program guide (mentor-matcher extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/onboarding-system` skill, or make a natural language request such as "Create an onboarding program."

## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_onboarding_checklist.md` — Onboarding checklist and schedule
- `02_training_program.md` — Training program
- `03_mentor_guide.md` — Mentor/buddy assignment guide
- `04_30_60_90_plan.md` — 30-60-90 day plan
- `05_review_report.md` — Onboarding experience review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 19 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
