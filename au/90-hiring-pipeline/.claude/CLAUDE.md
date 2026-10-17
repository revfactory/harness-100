# Hiring Pipeline Harness

hiring process: JDwriting→sourcing→screening→interview→assessment→offerto A harness where an agent team collaborates to produce deliverables.

## structure

```
.claude/
├── agents/
│ ├── jd-writer.md — JD writing (job description, qualificationrequirement, hiringposting)
│ ├── sourcing-specialist.md — sourcing (channelstrategy, Full, value)
│ ├── screening-expert.md — screening (fromassessment, companybeforetask, beforeinterview)
│ ├── interview-designer.md — interview design (structureinterview, questiondesign, evaluation form)
│ └── offer-coordinator.md — assessment·offer (finalassessment, reportpackage, offer)
├── skills/
│ ├── hiring-pipeline/
│ │ └── skill.md — Orchestrator (team , workflow, error handling)
│ ├── competency-model/
│ │ └── skill.md — competency model design (jd-writer extension)
│ └── interview-scorecard/
│ └── skill.md — structure interview design (interview-designer extension)
└── CLAUDE.md — file
```

## usage

`/hiring-pipeline` skill , "hiring process designplease do" specialistannual request.

## deliverable

all deliverable `_workspace/` save:
- `00_input.md` — user input organisation
- `01_job_description.md` — job description and hiringposting
- `02_sourcing_strategy.md` — sourcing strategy
- `03_screening_framework.md` — screening framework
- `04_interview_design.md` — interview designfrom
- `05_evaluation_offer.md` — final assessment and offer guide

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 5 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
