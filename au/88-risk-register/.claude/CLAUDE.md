# Risk Register Harness

project risk managementversus: riskidentification→probability·impactassessment→responsestrategyestablish→monitoringplan→statusreportto A harness where an agent team collaborates to produce deliverables.

## structure

```
.claude/
├── agents/
│ ├── risk-identifier.md — risk identification (categoryby risk derive, RBS)
│ ├── assessment-analyst.md — probability·impact assessment (/nature analysis, risk matrix)
│ ├── response-strategist.md — response strategy establish (avoidance/transfer/mitigation/acceptance)
│ ├── monitoring-planner.md — monitoring plan (KRI, , cycle)
│ └── report-writer.md — status report (dashboard, trend, management reporting)
├── skills/
│ ├── risk-register/
│ │ └── skill.md — Orchestrator (team , workflow, error handling)
│ ├── risk-scoring-matrix/
│ │ └── skill.md — risk assessment matrix (assessment-analyst extension)
│ └── risk-response-patterns/
│ └── skill.md — risk response strategy pattern (response-strategist extension)
└── CLAUDE.md — file
```

## usage

`/risk-register` skill , "project risk managementversus create it" specialistannual request.

## deliverable

all deliverable `_workspace/` save:
- `00_input.md` — user input organisation
- `01_risk_identification.md` — risk identification report
- `02_risk_assessment.md` — probability·impact assessment matrix
- `03_response_strategy.md` — response strategy planfrom
- `04_monitoring_plan.md` — monitoring plan
- `05_status_report.md` — risk status report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 4 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
