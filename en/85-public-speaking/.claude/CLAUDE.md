# Public Speaking Harness

A harness where an agent team collaborates to produce comprehensive public speaking deliverables — speeches, presentation scripts, debate preparation, Q&A playbooks, and rehearsal guides.

## Structure

```
.claude/
├── agents/
│   ├── audience-analyst.md     — Audience analysis (target audience, context, expectations)
│   ├── speech-writer.md        — Speech/presentation writer (speeches, presentation scripts)
│   ├── debate-preparer.md      — Debate preparation expert (arguments, counterarguments, cross-examination)
│   ├── qa-strategist.md        — Q&A strategist (anticipated questions, answer strategies)
│   └── rehearsal-coach.md      — Rehearsal coach and cross-verification (delivery, consistency)
├── skills/
│   ├── public-speaking/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── rhetoric-patterns/
│   │   └── skill.md           — Rhetoric pattern library (for speech-writer)
│   └── audience-engagement/
│       └── skill.md           — Audience engagement strategies (for audience-analyst)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/public-speaking` skill, or make a natural language request such as "Help me write a speech."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_audience_analysis.md` — Audience analysis report
- `02_speech_script.md` — Speech/presentation script
- `03_debate_prep.md` — Debate preparation document
- `04_qa_playbook.md` — Q&A anticipated answers playbook
- `05_rehearsal_guide.md` — Rehearsal guide and verification report
