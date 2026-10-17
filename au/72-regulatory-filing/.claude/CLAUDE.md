# Regulatory Filing Harness

A regulatory filing and permit application agent team harness.

## Structure

```
.claude/
├── agents/
│   ├── requirements-investigator.md
│   ├── document-drafter.md
│   ├── attachment-preparer.md
│   └── submission-verifier.md
├── skills/
│   ├── regulatory-filing/
│   │   └── skill.md              — Orchestrator
│   ├── permit-requirements-db/
│   │   └── skill.md              — Permit requirements database (filing types, required documents, processing timelines)
│   └── form-filling-guide/
│       └── skill.md              — Form filling guide (field-by-field instructions, common mistakes, example entries)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/regulatory-filing` skill, or make a natural language request.

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 8 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
