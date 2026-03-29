# Risk Register Harness

An agent team collaborates to produce a complete project risk management register, covering risk identification, probability and impact assessment, response strategy development, monitoring planning, and status reporting.

## Structure

```
.claude/
├── agents/
│   ├── risk-identifier.md        — Risk identification (category-based risk elicitation, RBS)
│   ├── assessment-analyst.md     — Probability and impact assessment (quantitative/qualitative analysis, risk matrix)
│   ├── response-strategist.md    — Response strategy development (avoid / transfer / mitigate / accept)
│   ├── monitoring-planner.md     — Monitoring plan (KRIs, triggers, cadence)
│   └── report-writer.md          — Status report (dashboard, trends, executive summary)
├── skills/
│   ├── risk-register/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── risk-scoring-matrix/
│   │   └── skill.md              — Risk assessment matrix (assessment-analyst extension)
│   └── risk-response-patterns/
│       └── skill.md              — Risk response strategy patterns (response-strategist extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/risk-register` skill, or make a natural-language request such as "Create a project risk management register."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Structured user input
- `01_risk_identification.md` — Risk identification report
- `02_risk_assessment.md` — Probability and impact assessment matrix
- `03_response_strategy.md` — Response strategy plan
- `04_monitoring_plan.md` — Monitoring plan
- `05_status_report.md` — Risk status report
