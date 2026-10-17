# API Designer Harness

A harness where an agent team collaborates to design, document, mock, and test REST/GraphQL APIs.

## Structure

```
.claude/
├── agents/
│   ├── api-architect.md      — API design (resource modeling, endpoints, versioning)
│   ├── schema-validator.md   — Schema validation (OpenAPI/GraphQL schemas, type safety)
│   ├── doc-writer.md         — API documentation (developer guides, examples, error references)
│   ├── mock-tester.md        — Mock server and testing (Mock API, integration tests, load scenarios)
│   └── review-auditor.md     — API review (security, consistency, performance, best practice compliance)
├── skills/
│   ├── api-designer/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── rest-api-conventions/
│   │   └── skill.md           — API architect extension (URL naming, status codes, pagination, versioning)
│   └── api-error-design/
│       └── skill.md           — Doc writer/tester extension (error code system, error responses, retry strategies)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/api-designer` skill or make a natural language request such as "Design an API."

## Artifacts

All artifacts are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_api_design.md` — API design document
- `02_schema.yaml` — OpenAPI/GraphQL schema file
- `03_api_docs.md` — API developer documentation
- `04_mock_tests.md` — Mock server setup and test results
- `05_review_report.md` — API review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 15 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
