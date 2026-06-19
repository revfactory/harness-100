---
name: security-audit
description: "A full security audit pipeline where an agent team collaborates to perform vulnerability scanning, code security analysis, penetration test scenario writing, and remediation recommendations. Use this skill across all security audit work, including 'run a security audit', 'check for vulnerabilities', 'security assessment', 'code security analysis', 'penetration test report', 'security vulnerability scan', 'OWASP check', 'secure coding review', 'security improvement plan', 'infrastructure security check', and similar requests. It also supports cases where only code analysis or only remediation recommendations are needed. However, actual network penetration execution, malware analysis, SOC operations, and real-time security monitoring are out of scope for this skill."
---

# Security Audit — full security audit pipeline

An agent team collaborates to perform the security audit's vulnerability scan → code analysis → penetration test report → remediation recommendations in a single pass.

## Execution mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other.

## Agent composition

| Agent | File | Role | Type |
|---------|------|------|------|
| vulnerability-scanner | `.claude/agents/vulnerability-scanner.md` | CVE, dependency, misconfiguration scanning | general-purpose |
| code-analyst | `.claude/agents/code-analyst.md` | SAST, secure coding, pattern detection | general-purpose |
| pentest-reporter | `.claude/agents/pentest-reporter.md` | Attack scenarios, PoC, impact analysis | general-purpose |
| security-consultant | `.claude/agents/security-consultant.md` | Remediation recommendations, roadmap, framework mapping | general-purpose |
| audit-reviewer | `.claude/agents/audit-reviewer.md` | Cross-validation, risk level adjustment, final report | general-purpose |

## Workflow

### Phase 1: Preparation (orchestrator performs directly)

1. Extract from the user input:
    - **Audit target**: code repository, infrastructure, application URL
    - **Audit scope**: full/partial, included/excluded items
    - **Tech stack**: language, framework, cloud, DB
    - **Regulatory requirements** (optional): GDPR, personal information protection law, electronic financial supervision regulations
    - **Existing reports** (optional): previous audit reports, vulnerability lists
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If there is audit target code, finalize the analysis scope
5. If existing files are present, copy them into `_workspace/` and skip the corresponding Phase
6. **Decide the execution mode** based on the request scope

### Phase 2: Team setup and execution

Set up the team and assign tasks. The dependencies between tasks are as follows:

| Order | Task | Owner | Depends on | Deliverable |
|------|------|------|------|--------|
| 1a | Vulnerability scan | scanner | None | `_workspace/01_vulnerability_scan.md` |
| 1b | Code security analysis | analyst | None | `_workspace/02_code_analysis.md` |
| 2 | Penetration test report | pentest | Tasks 1a, 1b | `_workspace/03_pentest_report.md` |
| 3 | Remediation recommendations | consultant | Tasks 1a, 1b, 2 | `_workspace/04_remediation_plan.md` |
| 4 | Audit review | reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_audit_report.md` |

Tasks 1a (scan) and 1b (code analysis) run **in parallel**. Since neither has initial dependencies, they can start at the same time.

**Communication flow between team members:**
- scanner done → send CWE mapping to analyst, send exploitable vulnerabilities to pentest
- analyst done → send data flow and attack vectors to pentest
- pentest done → send business impact and urgency to consultant
- consultant done → send the full remediation plan to reviewer
- reviewer cross-validates all deliverables. When a 🔴 required fix is found, send a fix request to the corresponding agent → rework → re-validate (maximum 2 times)

### Phase 3: Integration and final deliverables

Compile the final deliverables based on the reviewer's report:

1. Confirm all files in `_workspace/`
2. Confirm that all 🔴 required fixes in the review report have been reflected
3. Report the final summary to the user:
    - Vulnerability scan — `01_vulnerability_scan.md`
    - Code analysis — `02_code_analysis.md`
    - Penetration test — `03_pentest_report.md`
    - Remediation recommendations — `04_remediation_plan.md`
    - Final audit report — `05_audit_report.md`

## Modes by task size

| User request pattern | Execution mode | Agents engaged |
|----------------|----------|-------------|
| "Run a full security audit" | **Full audit** | All 5 members |
| "Analyze the security of this code" | **Code analysis mode** | analyst + reviewer |
| "Scan for vulnerabilities" | **Scan mode** | scanner + reviewer |
| "Create a security improvement plan" (existing report) | **Consulting mode** | consultant + reviewer |
| "Review this security report" | **Review mode** | reviewer alone |

## Data transfer protocol

| Strategy | Method | Use |
|------|------|------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time transfer of key information, fix requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error handling

| Error type | Strategy |
|----------|------|
| Code not provided | Request the code path from the user, provide a general security checklist up front |
| CVE DB inaccessible | Local knowledge-based analysis, mark as "offline scan" |
| Tech stack unknown | Attempt automatic detection from code extensions/import statements |
| Agent failure | Retry once → if it still fails, proceed without that deliverable and note the omission in the review report |
| 🔴 found in review | Send a fix request to the corresponding agent → rework → re-validate (maximum 2 times) |

## Test scenarios

### Normal flow
**Prompt**: "Run a full security audit on this Node.js Express web app codebase"
**Expected result**:
- Scan: npm dependency CVE list, secret detection, configuration check
- Code analysis: OWASP Top 10 vulnerabilities (XSS, SQL Injection, CSRF, etc.), with fix code included
- Penetration test: 3–5 attack scenarios, MITRE ATT&CK mapping, PoC procedures
- Remediation recommendations: NIST CSF gap analysis, short-/mid-/long-term roadmap
- Review: confirm all items in the consistency matrix

### Existing file utilization flow
**Prompt**: "Based on the previous audit report, check remediation progress and provide additional recommendations" + attach the previous report
**Expected result**:
- Copy the previous report into `_workspace/`
- Consulting mode: engage consultant + reviewer
- Track whether previous vulnerabilities are resolved + provide new recommendations

### Error flow
**Prompt**: "Run a security check, I'll give you the code later"
**Expected result**:
- When code is absent, provide a general security audit checklist and framework mapping up front
- Note that "detailed analysis is possible once the code is provided"
- Guide on infrastructure/configuration level check items


## Per-agent enhancement skills

| Skill | Path | Target agents to enhance | Role |
|------|------|-----------------|------|
| owasp-testing-guide | `.claude/skills/owasp-testing-guide/skill.md` | code-analyst, pentest-reporter | Per-vulnerability test methods and fix guides for OWASP Top 10 |
| cve-analysis | `.claude/skills/cve-analysis/skill.md` | vulnerability-scanner | CVSS score interpretation, dependency scanning tools, secret detection |
| threat-modeling | `.claude/skills/threat-modeling/skill.md` | security-consultant, pentest-reporter | STRIDE, DREAD, Attack Tree, attack surface analysis |
