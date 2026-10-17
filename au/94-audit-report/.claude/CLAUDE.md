# Audit Report Harness

An internal audit report generation harness. An agent team collaborates to handle everything from audit scope design through checklist creation, findings analysis, improvement recommendations, and tracking ledger management.

## Structure

```
.claude/
├── agents/
│   ├── scope-designer.md       — Audit scope design (objectives, criteria, targets, schedule)
│   ├── checklist-builder.md    — Audit checklist creation (control items, test procedures)
│   ├── findings-analyst.md     — Findings analysis (risk rating, root cause, impact assessment)
│   ├── recommendation-writer.md — Improvement recommendations (corrective actions, implementation plans)
│   └── tracking-manager.md    — Tracking ledger management (implementation status, follow-up)
├── skills/
│   ├── audit-report/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── internal-control-framework/
│   │   └── skill.md           — Internal control framework (scope-designer extension)
│   └── finding-classification/
│       └── skill.md           — Finding classification (findings-analyst extension)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/audit-report` skill, or make a natural language request such as "Create an internal audit report."

## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Audit request and background
- `01_audit_scope.md` — Audit scope and plan
- `02_audit_checklist.md` — Audit checklist
- `03_audit_findings.md` — Findings report
- `04_recommendations.md` — Improvement recommendations
- `05_tracking_ledger.md` — Implementation tracking ledger
- `06_final_report.md` — Comprehensive audit report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 9 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
