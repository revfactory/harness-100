# Procurement Docs Harness

A procurement document set generation harness. An agent team collaborates to produce everything from requirements definition through vendor comparison, evaluation criteria, contract review, and acceptance criteria.

## Structure

```
.claude/
├── agents/
│   ├── requirements-definer.md   — Procurement requirements definition (specs, quantity, delivery, budget)
│   ├── vendor-comparator.md      — Vendor comparison analysis (candidate research, comparison tables, references)
│   ├── evaluation-designer.md    — Evaluation criteria design (scoring, weighting)
│   ├── contract-reviewer.md      — Contract terms review (clauses, risks, negotiation points)
│   └── acceptance-builder.md     — Acceptance criteria creation (inspection items, pass/fail criteria)
├── skills/
│   ├── procurement-docs/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── vendor-scoring/
│   │   └── skill.md              — Vendor evaluation scorecard (vendor-comparator extension)
│   └── contract-checklist/
│       └── skill.md              — Contract review checklist (contract-reviewer extension)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/procurement-docs` skill, or make a natural language request such as "Create procurement documents."

## Outputs

All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Procurement request and background
- `01_requirements_spec.md` — Procurement requirements specification
- `02_vendor_comparison.md` — Vendor comparison analysis
- `03_evaluation_criteria.md` — Evaluation criteria
- `04_contract_review.md` — Contract terms review
- `05_acceptance_criteria.md` — Acceptance criteria
- `06_procurement_summary.md` — Procurement summary report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 6 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
