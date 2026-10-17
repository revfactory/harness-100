# CI/CD Pipeline Harness

A harness where an agent team collaborates to design, build, monitor, and optimise CI/CD pipelines.

## Structure

```
.claude/
├── agents/
│   ├── pipeline-designer.md     — Pipeline design (stages, triggers, branch strategies)
│   ├── infra-engineer.md        — Infrastructure configuration (runners, containers, environment variables, secrets)
│   ├── monitoring-specialist.md — Monitoring (metrics, alerts, dashboards, SLA)
│   ├── security-scanner.md      — Security scanning (SAST, DAST, dependencies, containers)
│   └── pipeline-reviewer.md     — Pipeline review (efficiency, reliability, security, alignment)
├── skills/
│   ├── cicd-pipeline/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── pipeline-security-gates/
│   │   └── skill.md              — Security scanner extension (SAST/SCA/secret detection tools, gate placement, thresholds)
│   └── deployment-strategies/
│       └── skill.md              — Pipeline designer extension (Blue-Green/Canary/Rolling, DORA)
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/cicd-pipeline` skill or make a natural language request such as "Create a CI/CD pipeline."

## Artifacts

All artifacts are saved in the `_workspace/` directory:
- `00_input.md` — Organised user input
- `01_pipeline_design.md` — Pipeline design document
- `02_pipeline_config/` — Pipeline configuration files (YAML, etc.)
- `03_monitoring.md` — Monitoring design document
- `04_security_scan.md` — Security scan configuration and report
- `05_review_report.md` — Pipeline review report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 19 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
