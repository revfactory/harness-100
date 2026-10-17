# Security Audit Harness

An agent team harness for performing security audits covering vulnerability scanning, code analysis, penetration test reporting, and remediation recommendations.

## Structure

```
.claude/
├── agents/
│   ├── vulnerability-scanner.md  — Vulnerability scanner (CVE, dependencies, misconfigurations)
│   ├── code-analyst.md           — Code security analysis (SAST, secure coding, pattern detection)
│   ├── pentest-reporter.md       — Penetration test reporting (attack scenarios, PoC, impact analysis)
│   ├── security-consultant.md    — Security consultant (remediation recommendations, roadmap, framework mapping)
│   └── audit-reviewer.md         — Audit reviewer (cross-validation, risk level adjustment, final report)
├── skills/
│   ├── security-audit/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── owasp-testing-guide/
│   │   └── skill.md              — OWASP Top 10 security testing guide
│   ├── cve-analysis/
│   │   └── skill.md              — CVE analysis and dependency vulnerability management guide
│   └── threat-modeling/
│       └── skill.md              — Threat modeling methodology guide
└── CLAUDE.md                     — This file
```

## Usage

Trigger the `/security-audit` skill, or make a natural language request such as "perform a security audit."

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Audit scope and organised user input
- `01_vulnerability_scan.md` — Vulnerability scan results
- `02_code_analysis.md` — Code security analysis report
- `03_pentest_report.md` — Penetration test scenario report
- `04_remediation_plan.md` — Remediation recommendations and roadmap
- `05_audit_report.md` — Final audit report

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 2 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 10 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
