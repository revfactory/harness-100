# Compliance Checker Harness

Regulatory compliance verification — an agent team collaborates to perform law mapping, status audit, gap analysis, and remediation planning.

## Structure

```
.claude/
├── agents/
│   ├── law-mapper.md           — Law analyst (identifies applicable regulations, maps clauses, extracts obligations)
│   ├── status-auditor.md       — Status auditor (investigates organizational status, collects evidence, assesses compliance)
│   ├── gap-analyst.md          — Gap analyst (compares legal requirements vs. status, calculates risk, derives priorities)
│   └── remediation-planner.md  — Remediation planner (corrective actions, scheduling, monitoring framework)
├── skills/
│   ├── compliance-checker/
│   │   └── skill.md            — Orchestrator (team coordination, workflow, error handling)
│   ├── regulation-knowledge-base/
│   │   └── skill.md            — Industry-specific regulatory law DB (for law-mapper, gap-analyst)
│   └── audit-checklist-engine/
│       └── skill.md            — Audit checklist generation engine (for status-auditor)
└── CLAUDE.md                   — This file
```

## Usage

Trigger the `/compliance-checker` skill or make a request in natural language such as "check regulatory compliance."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_law_mapping.md` — Law mapping report
- `02_status_audit.md` — Status audit report
- `03_gap_analysis.md` — Gap analysis report
- `04_remediation_plan.md` — Remediation plan

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 1 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 36 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
