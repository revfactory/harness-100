---
name: database-architect
description: "Full pipeline for DB design. An agent team collaborates to perform data modelling, migration, indexing, query optimisation, and security verification. Use this skill for any database design task including 'design a database', 'database modelling', 'table design', 'ERD', 'migration', 'query optimisation', 'index design', 'SQL schema', 'PostgreSQL design', 'MySQL design', etc. Also supports optimisation and security auditing for existing schemas. Note: actual DB server installation/operation, cloud infrastructure provisioning, and monitoring dashboard setup are outside the scope of this skill."
---

# Database Architect — DB Design Full Pipeline

An agent team collaborates to perform data modelling, migration, indexing, query optimisation, and security verification in a single pass.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| data-modeler | `.claude/agents/data-modeler.md` | ERD, normalisation, relationship design | general-purpose |
| migration-manager | `.claude/agents/migration-manager.md` | DDL, version control, rollback | general-purpose |
| performance-analyst | `.claude/agents/performance-analyst.md` | Indexing, query optimisation | general-purpose |
| security-auditor | `.claude/agents/security-auditor.md` | Access control, encryption, auditing | general-purpose |
| integration-reviewer | `.claude/agents/integration-reviewer.md` | Alignment, operational readiness verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Domain**: What service is the DB for
   - **DBMS**: PostgreSQL / MySQL / MongoDB / DynamoDB
   - **Core Entities**: Primary data subjects
   - **Expected Scale** (optional): Row counts, TPS
   - **Existing Files** (optional): Existing schemas, ERDs, SQL, etc.
2. Create the `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | Data Modelling | data-modeler | None | `_workspace/01_data_model.md` |
| 2 | Migration Generation | migration-manager | Task 1 | `_workspace/02_migration.sql`, `02_migration_plan.md` |
| 3a | Performance Optimisation | performance-analyst | Tasks 1, 2 | `_workspace/03_performance.md` |
| 3b | Security Verification | security-auditor | Tasks 1, 2 | `_workspace/04_security.md` |
| 4 | Integration Review | integration-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (performance) and 3b (security) are **executed in parallel**.

**Inter-team communication flow:**
- data-modeler completes -> Delivers DDL basis to migration-manager, access patterns to performance-analyst, sensitive data to security-auditor
- migration-manager completes -> Delivers index DDL to performance-analyst, permission DDL to security-auditor
- performance-analyst <-> security-auditor: Mutually verify that performance optimisations do not compromise security
- integration-reviewer cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organise the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Design a database", "full design" | **Full Pipeline** | All 5 agents |
| "Just draw the ERD", "table design only" | **Modelling Mode** | data-modeler + integration-reviewer |
| "Optimise this schema" (existing SQL) | **Optimisation Mode** | performance-analyst + integration-reviewer |
| "DB security audit" (existing DB) | **Security Mode** | security-auditor + integration-reviewer |
| "Review this schema" | **Review Mode** | integration-reviewer only |

**Leveraging existing files**: If the user provides schemas, ERDs, or other existing files, skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary artifacts |
| Message-based | SendMessage | Real-time delivery of key information, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{artifact}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| DBMS not specified | Default to PostgreSQL; add compatibility notes for other DBMSs |
| Insufficient domain information | Data modeler starts with common patterns; document assumptions |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing schema parsing failure | Manually analyse and reconstruct the data model |

## Test Scenarios

### Normal Flow
**Prompt**: "Design a PostgreSQL database for an e-commerce platform. I need user, product, order, payment, and review tables. Expecting 100K orders per day"
**Expected Result**:
- Model: 5 core tables + junction tables, 3NF normalisation, ERD
- Migration: Sequential DDL + rollback scripts + seed data
- Performance: Index strategy, key query optimisation, partitioning design
- Security: RBAC, PII encryption, audit logging, backup strategy
- Review: All items in the alignment matrix verified

### Existing File Flow
**Prompt**: "Optimise the performance of this SQL schema" + SQL file
**Expected Result**:
- Copy existing schema to `_workspace/02_migration.sql`
- Optimisation mode: deploy performance-analyst + integration-reviewer
- Skip data-modeler, migration-manager, security-auditor

### Error Flow
**Prompt**: "Design a database, blog platform"
**Expected Result**:
- Scale/DBMS unknown -> data-modeler infers PostgreSQL + standard blog entities (Post, User, Comment, Tag)
- Execute in full pipeline mode
- Review report notes "design based on inferred requirements"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | Target Agent | Role |
|-------|-------------|------|
| `normalization-patterns` | data-modeler | 1NF-BCNF identification, denormalization strategies, domain-specific ERD templates |
| `query-optimization-catalog` | performance-analyst | Index strategies, EXPLAIN analysis, N+1 resolution, partitioning |
