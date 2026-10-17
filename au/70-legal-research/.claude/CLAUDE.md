# Legal Research Harness

A legal research agent team harness.

## Structure

```
.claude/
├── agents/
│   ├── case-searcher.md
│   ├── legal-analyst.md
│   ├── strategy-advisor.md
│   └── opinion-writer.md
├── skills/
│   ├── legal-research/
│   │   └── skill.md              — Orchestrator
│   ├── case-analysis-framework/
│   │   └── skill.md              — Case analysis framework (IRAC methodology, precedent analysis, ratio decidendi extraction)
│   └── legal-writing-methodology/
│       └── skill.md              — Legal writing methodology (legal memo format, opinion structure, citation rules)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/legal-research` skill, or make a natural language request.

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 3 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
