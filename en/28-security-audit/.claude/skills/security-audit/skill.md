---
name: security-audit
description: "A full security audit pipeline in which an agent team collaboratively performs vulnerability scanning, code security analysis, penetration test scenario writing, and remediation recommendations. Use this skill for all security audit activities including 'perform a security audit', 'vulnerability assessment', 'security diagnosis', 'code security analysis', 'penetration test report', 'security vulnerability scan', 'OWASP review', 'secure coding review', 'security improvement recommendations', and 'infrastructure security review'. Also supports cases where only code analysis or only remediation recommendations are needed. Note: actual network penetration execution, malware analysis, SOC operations, and real-time security monitoring are outside the scope of this skill."
---

# Security Audit — Full Security Audit Pipeline

An agent team collaboratively performs vulnerability scanning → code analysis → penetration test reporting → remediation recommendations in a single end-to-end workflow.

## Execution Mode

**Agent team** — 5 agents communicate directly via SendMessage and perform cross-validation.

## Agent Configuration

| Agent | File | Role | Type |
|-------|------|------|------|
| vulnerability-scanner | `.claude/agents/vulnerability-scanner.md` | CVE, dependency, misconfiguration scanning | general-purpose |
| code-analyst | `.claude/agents/code-analyst.md` | SAST, secure coding, pattern detection | general-purpose |
| pentest-reporter | `.claude/agents/pentest-reporter.md` | Attack scenarios, PoC, impact analysis | general-purpose |
| security-consultant | `.claude/agents/security-consultant.md` | Remediation recommendations, roadmap, framework mapping | general-purpose |
| audit-reviewer | `.claude/agents/audit-reviewer.md` | Cross-validation, risk level adjustment, final report | general-purpose |

## Workflow

### Phase 1: Preparation (orchestrator performs directly)

1. Extract from user input:
    - **Audit target**: code repository, infrastructure, application URL
    - **Audit scope**: full/partial, included/excluded items
    - **Technology stack**: language, framework, cloud, DB
    - **Regulatory requirements** (optional): GDPR, data protection law, financial regulations
    - **Existing reports** (optional): previous audit reports, vulnerability lists
2. Create `_workspace/` directory at the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If audit target code is available, finalize the analysis scope
5. If existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1a | Vulnerability scan | scanner | none | `_workspace/01_vulnerability_scan.md` |
| 1b | Code security analysis | analyst | none | `_workspace/02_code_analysis.md` |
| 2 | Penetration test report | pentest | tasks 1a, 1b | `_workspace/03_pentest_report.md` |
| 3 | Remediation recommendations | consultant | tasks 1a, 1b, 2 | `_workspace/04_remediation_plan.md` |
| 4 | Audit review | reviewer | tasks 1a, 1b, 2, 3 | `_workspace/05_audit_report.md` |

Tasks 1a (scan) and 1b (code analysis) are executed **in parallel** — both have no initial dependencies and can start simultaneously.

**Team communication flow:**
- scanner completes → delivers CWE mappings to analyst; delivers exploitable vulnerabilities to pentest
- analyst completes → delivers data flows and attack vectors to pentest
- pentest completes → delivers business impact and urgency ratings to consultant
- consultant completes → delivers the full improvement plan to reviewer
- reviewer cross-validates all deliverables. If 🔴 required fixes are found, request corrections from the relevant agent → rework → re-validation (maximum 2 rounds)

### Phase 3: Integration and Final Deliverables

Finalize deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 required fixes from the review report have been addressed
3. Report the final summary to the user:
    - Vulnerability scan — `01_vulnerability_scan.md`
    - Code analysis — `02_code_analysis.md`
    - Penetration test — `03_pentest_report.md`
    - Remediation recommendations — `04_remediation_plan.md`
    - Final audit report — `05_audit_report.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Perform a full security audit" | **Full audit** | All 5 agents |
| "Analyze the security of this code" | **Code analysis mode** | analyst + reviewer |
| "Run a vulnerability scan" | **Scan mode** | scanner + reviewer |
| "Create security improvement recommendations" (existing report) | **Consulting mode** | consultant + reviewer |
| "Review this security report" | **Review mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key information delivery, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No code provided | Request code path from user; provide a general security checklist upfront |
| CVE DB inaccessible | Perform analysis based on local knowledge; mark as "offline scan" |
| Technology stack unknown | Attempt auto-detection from file extensions and import statements |
| Agent failure | Retry once → if still failing, continue without that deliverable; note the omission in the review report |
| 🔴 found in review | Request corrections from the relevant agent → rework → re-validation (maximum 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Perform a full security audit on this Node.js Express web application codebase"
**Expected result**:
- Scan: npm dependency CVE list, secret detection, configuration review
- Code analysis: Vulnerabilities per OWASP Top 10 (XSS, SQL Injection, CSRF, etc.) including fix code
- Penetration test: 3–5 attack scenarios, MITRE ATT&CK mapping, PoC procedures
- Remediation: NIST CSF gap analysis, short/mid/long-term roadmap
- Review: All items in the consistency matrix verified

### Existing File Flow
**Prompt**: "Based on the previous audit report, check remediation progress and provide additional recommendations" + previous report attached
**Expected result**:
- Previous report copied to `_workspace/`
- Consulting mode: consultant + reviewer deployed
- Previous vulnerability resolution tracked + new recommendations added

### Error Flow
**Prompt**: "Check our security; I'll provide the code later"
**Expected result**:
- Proactively provide a general security audit checklist and framework mapping in the absence of code
- State "detailed analysis available once code is provided"
- Guide through infrastructure/configuration-level review items


## Per-Agent Extension Skills

| Skill | Path | Target Agent | Role |
|-------|------|-------------|------|
| owasp-testing-guide | `.claude/skills/owasp-testing-guide/skill.md` | code-analyst, pentest-reporter | Per-vulnerability test methods and fix guides for OWASP Top 10 |
| cve-analysis | `.claude/skills/cve-analysis/skill.md` | vulnerability-scanner | CVSS score interpretation, dependency scanning tools, secret detection |
| threat-modeling | `.claude/skills/threat-modeling/skill.md` | security-consultant, pentest-reporter | STRIDE, DREAD, Attack Tree, attack surface analysis |
