# Service Legal Docs Harness

A service terms and legal document drafting agent team harness.

## Structure

```
.claude/
├── agents/
│   ├── tos-specialist.md
│   ├── privacy-specialist.md
│   ├── consumer-analyst.md
│   └── consistency-reviewer.md
├── skills/
│   ├── service-legal-docs/
│   │   └── skill.md              — Orchestrator
│   ├── unfair-terms-detector/
│   │   └── skill.md              — Unfair terms detector (unfairness criteria, regulatory examples, amendment suggestions)
│   └── cross-document-linker/
│       └── skill.md              — Cross-document linker (term consistency, cross-reference mapping, version management)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/service-legal-docs` skill, or make a natural language request.

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 4 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
