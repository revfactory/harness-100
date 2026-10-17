# Fullstack Web App Harness

A harness where an agent team collaborates to develop fullstack web apps through the pipeline of requirements, design, frontend, backend, testing, and deployment.

## Structure

```
.claude/
├── agents/
│   ├── architect.md             — System design (requirements analysis, architecture, DB modeling, API design)
│   ├── frontend-dev.md          — Frontend development (React/Next.js, UI components, state management)
│   ├── backend-dev.md           — Backend development (API implementation, DB, auth, business logic)
│   ├── qa-engineer.md           — QA engineer (test strategy, unit/integration/E2E tests)
│   └── devops-engineer.md       — DevOps engineer (CI/CD, infrastructure, deployment, monitoring)
├── skills/
│   ├── fullstack-webapp/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── component-patterns/
│   │   └── skill.md             — Frontend extension (React patterns, state management, folder structure)
│   └── api-security-checklist/
│       └── skill.md             — Backend extension (OWASP Top 10, auth, security headers)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/fullstack-webapp` skill, or make a natural language request like "Build me a web app."

## Deliverables

All deliverables are generated directly at the project root:
- `_workspace/00_input.md` — Organised user input
- `_workspace/01_architecture.md` — Architecture design document
- `_workspace/02_api_spec.md` — API specification
- `_workspace/03_db_schema.md` — DB schema
- `_workspace/04_test_plan.md` — Test plan
- `_workspace/05_deploy_guide.md` — Deployment guide
- `_workspace/06_review_report.md` — Review report
- `src/` — Source code (frontend + backend)

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 26 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
