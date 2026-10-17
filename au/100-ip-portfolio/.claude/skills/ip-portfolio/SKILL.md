---
name: ip-portfolio
description: "Full IP management pipeline for intellectual property portfolio management where an agent team collaborates to generate IP status analysis, patent/trademark/copyright mapping, renewal schedules, license strategies, and protection strategy reports. Use this skill for requests such as 'manage IP portfolio', 'patent portfolio analysis', 'trademark management', 'develop IP strategy', 'patent renewal schedule', 'license strategy', 'IP protection strategy', 'intellectual property status analysis', 'create a patent map', 'trade secret management', and other intellectual property management tasks. Also supports analysis of specific IP types (patents/trademarks/copyrights) or updating existing portfolios. However, actual patent application drafting (use patent-drafter skill), patent office electronic filing, legal opinion writing, and litigation representation are outside the scope of this skill."
---

# IP Portfolio — Intellectual Property Portfolio Management Full Pipeline

An agent team collaborates to generate IP status analysis, asset mapping, renewal schedules, license strategies, and protection strategy reports.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| ip-analyst | `.claude/agents/ip-analyst.md` | IP status assessment, value evaluation, portfolio mapping | general-purpose |
| patent-mapper | `.claude/agents/patent-mapper.md` | Patent/trademark/copyright classification, rights scope mapping | general-purpose |
| renewal-scheduler | `.claude/agents/renewal-scheduler.md` | Renewal deadlines, cost calculation, retention/abandonment | general-purpose |
| license-strategist | `.claude/agents/license-strategist.md` | Monetisation, cross-licensing, open source | general-purpose |
| protection-advisor | `.claude/agents/protection-advisor.md` | Infringement response, defence strategy, protection report | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Company Information**: Company name, industry, size
    - **IP Information** (optional): IP list, registration numbers, filing status
    - **Areas of Interest** (optional): Specific technology domains, specific IP types
    - **Objectives** (optional): Monetisation, enhanced protection, cost optimisation, dispute preparedness
    - **Existing Materials** (optional): IP register, license agreements, dispute history
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and use as reference materials
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | IP Status Analysis | analyst | None | `_workspace/01_ip_analysis.md` |
| 2 | IP Asset Mapping | mapper | Task 1 | `_workspace/02_ip_map.md` |
| 3a | Renewal Schedule | scheduler | Tasks 1, 2 | `_workspace/03_renewal_schedule.md` |
| 3b | License Strategy | license | Tasks 1, 2 | `_workspace/04_license_strategy.md` |
| 4 | Protection Strategy Report | protection | Tasks 1, 2, 3a, 3b | `_workspace/05_protection_report.md` |
| 5 | Integrated Review | orchestrator | All | `_workspace/06_review_report.md` |

Tasks 3a (Renewal) and 3b (License) run **in parallel**. Both depend only on Tasks 1 and 2.

**Inter-Agent Communication Flow:**
- analyst completes -> delivers inventory and classification to mapper, ratings to scheduler, monetisation candidates to license, core IP and threats to protection
- mapper completes -> delivers registration/expiration dates to scheduler, rights scope to license, claims analysis to protection
- scheduler <-> license: Cross-verify which abandonment candidates are still licensable
- protection synthesizes everything into the final protection strategy

### Phase 3: Integration and Final Deliverables

1. Verify consistency across all files in `_workspace/`
2. Detect discrepancies across valuation, renewal strategy, licensing, and protection
3. Generate the integrated review report
4. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|-----------------|
| "Manage my IP portfolio" | **Full Pipeline** | All 5 agents |
| "Analyse patent status" | **Analysis Mode** | analyst + mapper |
| "Organise IP renewal schedule" | **Renewal Mode** | analyst + mapper + scheduler |
| "Develop a licensing strategy" | **License Mode** | analyst + license |
| "Develop IP protection strategy" | **Protection Mode** | analyst + mapper + protection |
| "Build a management system for this IP list" + list | **Custom Mode** | Relevant agents |

**Using Existing Files**: When the user provides IP registers, existing analysis reports, etc., copy them to `_workspace/` and use as reference materials.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-Based | `_workspace/` directory | Store and share main deliverables |
| Message-Based | SendMessage | Real-time key information delivery, cross-verification |
| Task-Based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| IP list not provided | Collect via company name search on public IP Australia (AusPat) databases |
| Web search failure | Work with user-provided information only, note "Data limitations" |
| Foreign IP information unavailable | Prioritise domestic IP analysis, tag with "Foreign verification needed" |
| Agent failure | Retry once -> if still fails, proceed without that deliverable |
| Valuation-protection strategy mismatch | Detected in cross-validation -> request corrections (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Analyse our company's (IT firm, 50 patents, 20 trademarks) IP portfolio and build a management system"
**Expected Results**:
- Analysis: 50-patent + 20-trademark inventory, technology domain distribution, value ratings
- Mapping: IPC classification, family relationships, technology-product matrix
- Renewal: 12-month calendar, annual costs, retention/abandonment recommendations
- License: B/C-tier IP monetisation strategy, royalty terms
- Protection: Infringement monitoring system, defensive filing plan, trade secret management

### Specific Area Flow
**Prompt**: "Organise our patent renewal schedule, and sort out which to keep and which to abandon"
**Expected Results**:
- analyst performs lightweight value assessment
- mapper organises registration/expiration dates
- scheduler produces renewal calendar + retention/abandonment recommendations

### Error Flow
**Prompt**: "Manage our IP, but I don't have an IP list. Company name is XX Tech"
**Expected Results**:
- analyst searches IP Australia (AusPat) for "XX Tech" as applicant
- Builds portfolio from publicly available patents/trademarks only
- Notes "Non-public IP not included — available for update upon internal list provision"

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|-------------|------|
| patent-valuation | `.claude/skills/patent-valuation/skill.md` | ip-analyst, license-strategist | Three valuation approaches, royalty benchmarks, patent strength |
| ip-landscape-analysis | `.claude/skills/ip-landscape-analysis/skill.md` | patent-mapper, protection-advisor | Patent maps, gap analysis, FTO, IP strategy |
