# Customer Support Harness

Build a customer support system: an agent team collaborates to produce FAQ, response manuals, escalation policies, and analytics.

## Structure

```
.claude/
├── agents/
│   ├── faq-builder.md           — FAQ construction (question collection/classification, answer writing, search optimization)
│   ├── response-specialist.md   — Response manual (scenario-based scripts, tone & manner)
│   ├── escalation-manager.md    — Escalation (level design, routing, SLA)
│   ├── cs-analyst.md            — CS analytics (metrics, trends, improvement proposals)
│   └── cs-reviewer.md           — Cross-validation (FAQ ↔ manual ↔ escalation ↔ analytics consistency)
├── skills/
│   ├── customer-support/
│       └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── csat-analyzer/
│   │   └── skill.md             — CSAT analysis (NPS/CES, VOC, CS dashboard)
│   └── escalation-flowchart/
│       └── skill.md             — Escalation design (L1/L2/L3, SLA, crisis response)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/customer-support` skill or make a natural language request such as "Build me a customer support system."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_faq.md` — FAQ document
- `02_response_manual.md` — Response manual
- `03_escalation_policy.md` — Escalation policy
- `04_cs_analytics.md` — CS analytics framework
- `05_review_report.md` — Review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 23 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
