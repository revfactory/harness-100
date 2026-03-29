# Hiring Pipeline Harness

Recruitment process: a harness where an agent team collaborates to produce deliverables covering JD writing → sourcing → screening → interview → evaluation → offer.

## Structure

```
.claude/
├── agents/
│   ├── jd-writer.md              — JD writing (job description, qualifications, job posting)
│   ├── sourcing-specialist.md    — Sourcing (channel strategy, talent pool, outreach)
│   ├── screening-expert.md       — Screening (resume evaluation, take-home task, phone interview)
│   ├── interview-designer.md     — Interview design (structured interview, question design, scorecard)
│   └── offer-coordinator.md      — Evaluation and offer (final evaluation, compensation package, offer letter)
├── skills/
│   ├── hiring-pipeline/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── competency-model/
│   │   └── skill.md              — Competency model design (jd-writer extension)
│   └── interview-scorecard/
│       └── skill.md              — Structured interview design (interview-designer extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/hiring-pipeline` skill, or make a natural language request such as "design a hiring process for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_job_description.md` — Job description and job posting
- `02_sourcing_strategy.md` — Sourcing strategy
- `03_screening_framework.md` — Screening framework
- `04_interview_design.md` — Interview design document
- `05_evaluation_offer.md` — Final evaluation and offer guide
