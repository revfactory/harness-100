# Contract Analyser Harness

A contract analysis agent team harness.

## Structure

```
.claude/
├── agents/
│   ├── clause-analyst.md
│   ├── risk-assessor.md
│   ├── comparison-reviewer.md
│   ├── clause-drafter.md
│   └── contract-coordinator.md
├── skills/
│   ├── contract-analyzer/
│   │   └── skill.md              — Orchestrator
│   ├── clause-risk-database/
│   │   └── skill.md              — Clause risk DB (risk levels, standard clauses, amendment examples)
│   └── negotiation-playbook/
│       └── skill.md              — Negotiation playbook (BATNA, concession strategies, clause alternatives)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/contract-analyzer` skill, or make a natural language request.

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 19 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
