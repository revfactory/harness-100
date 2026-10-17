---
name: security-audit
description: "security auditof vulnerability , code security analysis, penetration test  , improvement  inthisbefore teamthis to countlower  security audit pipeline. 'security audit', 'vulnerability ', 'security ', 'code security analysis', 'penetration test report', 'security vulnerability ', 'OWASP ', 'queue  ', 'security improvement ', 'infrastructure security ' etc. security audit beforein this  for. code analysisonly necessarylower improvement only necessary inalso supported. , actual network penetration execution, code analysis, SOC operations, real-time security monitoring this of scope ."
---

# Security Audit — security audit  pipeline

security auditof vulnerability→codeanalysis→penetrationtestreport→improvement inthisbefore teamthis to  in count.

## execution 

**inthisbefore team** — 5peoplethis SendMessageas direct and  verification.

## inthisbefore setup

| inthisbefore | day | role | type |
|---------|------|------|------|
| vulnerability-scanner | `.claude/agents/vulnerability-scanner.md` | CVE, dependency, configurationerror  | general-purpose |
| code-analyst | `.claude/agents/code-analyst.md` | SAST, queue, patterndetection | general-purpose |
| pentest-reporter | `.claude/agents/pentest-reporter.md` | attack, PoC, impactanalysis | general-purpose |
| security-consultant | `.claude/agents/security-consultant.md` | improvement, asmap, frameworkmapping | general-purpose |
| audit-reviewer | `.claude/agents/audit-reviewer.md` | verification, risketc., finalreport | general-purpose |

## workflow

### Phase 1:  (this direct count)

1. user from :
    - **audit upper**: code , infrastructure, this URL
    - **audit scope**: before/minutes, included/excluded item
    - ** stack**: language, framework, , DB
    - ** requiredmatter** (optional): Privacy Act 1988 (Cth)/APPs, itemsinformation, before
    - **existing report** (optional): thisbefore audit report, vulnerability 
2. `_workspace/`  project rootin creation
3.  to `_workspace/00_input.md`in 
4. audit upper code  analysis scope 
5. existing daythis  `_workspace/`in and corresponding Phase cases
6. request scopein  **execution  decision**

### Phase 2: team setup and execution

team setupand  .  between of  and :

|  |  | responsible | of |  |
|------|------|------|------|--------|
| 1a | vulnerability  | scanner |  | `_workspace/01_vulnerability_scan.md` |
| 1b | code security analysis | analyst |  | `_workspace/02_code_analysis.md` |
| 2 | penetration test report | pentest |  1a, 1b | `_workspace/03_pentest_report.md` |
| 3 | improvement  | consultant |  1a, 1b, 2 | `_workspace/04_remediation_plan.md` |
| 4 | audit review | reviewer |  1a, 1b, 2, 3 | `_workspace/05_audit_report.md` |

 1a()and 1b(codeanalysis) **parallel execution**.   initial ofthis as in startto count .

**team between  :**
- scanner completed → analystto CWE mapping before, pentestto attack possible vulnerability before
- analyst completed → pentestto data ·attack  before
- pentest completed → consultantto business impact·urgentalso before
- consultant completed → reviewerto before improvement plan before
- reviewer all   verification. 🔴 required modification   corresponding inthisbeforeto modification request →  → verification (maximum 2)

### Phase 3: integrated and final 

reviewerof report as final  :

1. `_workspace/` within all day confirmation
2. review reportof 🔴 required modificationthis   confirmation
3. final  userto report:
    - vulnerability  — `01_vulnerability_scan.md`
    - code analysis — `02_code_analysis.md`
    - penetration test — `03_pentest_report.md`
    - improvement  — `04_remediation_plan.md`
    - final audit report — `05_audit_report.md`

##  per 

| user request pattern | execution  |  inthisbefore |
|----------------|----------|-------------|
| "security audit before count" | ** audit** | 5people before |
| "this code security analysis" | **code analysis ** | analyst + reviewer |
| "vulnerability " | ** ** | scanner + reviewer |
| "security improvement  only" (existing report) | **consulting ** | consultant + reviewer |
| "this security report " | **review ** | reviewer  |

## data before as

| strategy |  | foralso |
|------|------|------|
| day  | `_workspace/`  | week   and shared |
| message  | SendMessage | real-time core information before, modification request |
|   | TaskCreate/TaskUpdate | in progress upper tracking, of   |

daypeople : `{}_{inthisbefore}_{}.{extension}`

## error 

| error type | strategy |
|----------|------|
| code provided | userto code as request, day security list provided |
| CVE DB  impossible | as   analysis, " "  |
|  stack people | code extension/import from automatic detection also |
| inthisbefore failure | 1 retry → failure  corresponding  this in progress, review reportin  people |
| reviewfrom 🔴  | corresponding inthisbeforein modification request →  → verification (maximum 2) |

## test 

### normal 
****: "this Node.js Express  codethisin about before security audit count"
** result**:
- : npm dependency CVE ,  detection, configuration 
- codeanalysis: OWASP Top 10 criteria vulnerability(XSS, SQL Injection, CSRF etc.), modification code included
- penetrationtest: 3~5items attack , MITRE ATT&CK mapping, PoC procedure
- improvement: NIST CSF  analysis, ·· asmap
- review:   beforeitem confirmation

### existing day for 
****: "thisbefore audit report as improvement in progress upper and addition " + thisbefore report 
** result**:
- thisbefore report `_workspace/`in 
- consulting : consultant + reviewer 
- thisbefore vulnerability resolution  tracking +  

### error 
****: "security , code in "
** result**:
- code   day-based security audit listand framework mapping provided
- "code provided after detailed analysis possible" people
- infrastructure/configuration count  item within


## inthisbeforeper extension 

|  | as | -ize upper inthisbefore | role |
|------|------|-----------------|------|
| owasp-testing-guide | `.claude/skills/owasp-testing-guide/skill.md` | code-analyst, pentest-reporter | OWASP Top 10 vulnerabilityper test , modification guide |
| cve-analysis | `.claude/skills/cve-analysis/skill.md` | vulnerability-scanner | CVSS count , dependency  also,  detection |
| threat-modeling | `.claude/skills/threat-modeling/skill.md` | security-consultant, pentest-reporter | STRIDE, DREAD, Attack Tree, attack  analysis |
