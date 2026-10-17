# Privacy Engineer Harness

A privacy engineering agent team harness.

## Structure

```
.claude/
├── agents/
│   ├── privacy-law-analyst.md
│   ├── pia-assessor.md
│   ├── process-architect.md
│   └── consent-designer.md
├── skills/
│   ├── privacy-engineer/
│   │   └── skill.md              — Orchestrator
│   ├── gdpr-pipa-cross-reference/
│   │   └── skill.md              — GDPR-PIPA cross-reference (article mapping, requirements comparison, implementation guide)
│   └── data-flow-mapper/
│       └── skill.md              — Data flow mapper (data inventory, transfer mapping, legal basis matrix)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/privacy-engineer` skill, or make a natural language request.

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 8 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
