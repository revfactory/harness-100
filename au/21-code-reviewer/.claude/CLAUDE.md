# Code Reviewer Harness

A harness where an agent team collaborates to perform automated code review across style, security, performance, and architecture.

## Structure

```
.claude/
├── agents/
│   ├── style-inspector.md       — Code style inspection (conventions, formatting, naming, readability)
│   ├── security-analyst.md      — Security analysis (vulnerabilities, injection, authentication, data exposure)
│   ├── performance-analyst.md   — Performance analysis (complexity, memory, concurrency, queries)
│   ├── architecture-reviewer.md — Architecture review (design patterns, dependencies, SOLID, coupling)
│   └── review-synthesizer.md    — Review synthesis (prioritization, alignment, final verdict)
├── skills/
│   ├── code-reviewer/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── vulnerability-patterns/
│   │   └── skill.md              — Security analyst extension (CWE classification, language-specific vulnerability patterns, safe alternatives)
│   └── refactoring-catalog/
│       └── skill.md              — Architecture/performance extension (code smells, SOLID violations, complexity metrics)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/code-reviewer` skill or make a natural language request such as "Review this code."

## Artifacts

All artifacts are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_style_review.md` — Code style review
- `02_security_review.md` — Security review
- `03_performance_review.md` — Performance review
- `04_architecture_review.md` — Architecture review
- `05_review_summary.md` — Comprehensive review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 28 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
