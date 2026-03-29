---
name: data-pipeline
description: "A full pipeline skill where an agent team collaborates to design and implement data pipelines covering ingestion, transformation, loading, quality validation, and monitoring. Use this skill for requests such as 'design a data pipeline', 'build an ETL pipeline', 'automate data ingestion', 'data warehouse pipeline', 'ELT design', 'batch pipeline', 'streaming pipeline', 'create an Airflow DAG', 'design dbt models', or 'build a data quality validation system'. Also supports cases where only quality validation or monitoring is needed for an existing pipeline. Note: direct execution of real-time streaming engines (Flink/Spark Streaming), cloud infrastructure provisioning, and database administrator (DBA) tasks are outside this skill's scope."
---

# Data Pipeline — Pipeline Design and Implementation

An agent team collaborates to design and implement a complete data pipeline — ingestion → transformation → loading → quality validation → monitoring — in a single pass.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| etl-architect | `.claude/agents/etl-architect.md` | Source analysis, schema design, pipeline structure | general-purpose |
| data-quality-manager | `.claude/agents/data-quality-manager.md` | Validation rules, profiling, anomaly detection | general-purpose |
| scheduler-engineer | `.claude/agents/scheduler-engineer.md` | DAG design, dependencies, retry strategy | general-purpose |
| monitoring-specialist | `.claude/agents/monitoring-specialist.md` | Metrics, alerts, dashboards, SLA | general-purpose |
| pipeline-reviewer | `.claude/agents/pipeline-reviewer.md` | Cross-validation, consistency, operational readiness | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract the following from user input:
    - **Data Sources**: origin systems (DB, API, files, streaming)
    - **Target System**: data warehouse, data lake, analytics platform
    - **Business Requirements**: reporting cadence, SLA, data freshness
    - **Technical Constraints** (optional): cloud vendor, existing stack, budget
    - **Existing Files** (optional): schemas, queries, or config files provided by the user
2. Create the `_workspace/` directory at the project root
3. Organize the inputs and save them to `_workspace/00_input.md`
4. If existing files are provided, copy them into `_workspace/` and skip the corresponding phase
5. Based on the request scope, **decide the execution mode** (see "Mode by Request Scale" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|------------|
| 1 | ETL architecture design | etl-architect | None | `_workspace/01_etl_architecture.md` |
| 2a | Data quality plan | data-quality-manager | Task 1 | `_workspace/02_data_quality_plan.md` |
| 2b | Scheduling configuration | scheduler-engineer | Task 1 | `_workspace/03_scheduler_config.md` |
| 3 | Monitoring setup | monitoring-specialist | Tasks 1, 2a, 2b | `_workspace/04_monitoring_setup.md` |
| 4 | Pipeline review | pipeline-reviewer | Tasks 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (quality) and 2b (scheduling) run **in parallel** — both depend only on Task 1 (architecture) and can start simultaneously.

**Inter-Agent Communication Flow:**
- etl-architect completes → sends schema and business rules to quality-manager; sends dependency graph and resource requirements to scheduler; sends key metric definitions to monitoring
- quality-manager completes → sends validation task insertion points and halt conditions to scheduler; sends quality metrics and SLA to monitoring
- scheduler completes → sends DAG execution metrics to monitoring
- reviewer cross-validates all deliverables. If 🔴 required fixes are found, the reviewer requests corrections from the relevant agent → rework → re-validation (maximum 2 rounds)

### Phase 3: Integration and Final Deliverables

Consolidate final deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm all 🔴 required fixes from the review report have been applied
3. Report the final summary to the user:
    - ETL Architecture — `01_etl_architecture.md`
    - Quality Management Plan — `02_data_quality_plan.md`
    - Scheduling Configuration — `03_scheduler_config.md`
    - Monitoring Setup — `04_monitoring_setup.md`
    - Review Report — `05_review_report.md`
    - Pipeline Code — `pipeline_code/`

## Mode by Request Scale

Adjust which agents are engaged based on the scope of the user request:

| User Request Pattern | Execution Mode | Agents Engaged |
|---------------------|---------------|---------------|
| "Design a data pipeline", "Build the full ETL" | **Full Pipeline** | All 5 agents |
| "Build a data quality validation system" | **Quality Mode** | etl-architect + quality-manager + reviewer |
| "Design an Airflow DAG" | **Schedule Mode** | etl-architect + scheduler + reviewer |
| "Set up a pipeline monitoring dashboard" | **Monitoring Mode** | monitoring + reviewer |
| "Review this pipeline" | **Review Mode** | reviewer only |

**Reusing Existing Files**: If the user provides existing files (schemas, DAG code, etc.), copy them to the appropriate location in `_workspace/` and skip the corresponding agent's phase.

## Data Handoff Protocol

| Strategy | Mechanism | Purpose |
|----------|-----------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time critical information handoff, correction requests |
| Task-based | TaskCreate / TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|---------|
| Missing connection details | Architect proceeds with placeholder-based templates; marks "connection info not provided" in the output |
| Unknown technology stack | List options for AWS / GCP / Azure; prompt user to choose |
| Missing volume information | Present 3-tier architecture options: small (10K records/day) / medium (1M records/day) / large (100M records/day) |
| Agent failure | 1 retry → if still failing, proceed without that deliverable and note the gap in the review report |
| 🔴 found in review | Request correction from the relevant agent → rework → re-validation (maximum 2 rounds) |

## Test Scenarios

### Happy Path
**Prompt**: "Design a daily batch pipeline to load PostgreSQL order data into a BigQuery data warehouse. Use Airflow."
**Expected Result**:
- ETL architecture: PostgreSQL CDC / incremental load strategy, 4-layer design (Raw → Staging → Curated → Analytics)
- Quality plan: P0 / P1 / P2 validation rules based on order data characteristics, revenue aggregation cross-check
- Scheduling: Airflow DAG code (extract → stage → curate → analytics → quality_check), retry policy
- Monitoring: daily load count, latency, quality score dashboard
- Review: consistency matrix across all sections

### Reusing Existing Files
**Prompt**: "Design data quality validation and monitoring for these dbt model files" + dbt model files attached
**Expected Result**:
- Copy existing dbt models into `_workspace/`
- Merge Quality Mode + Monitoring Mode: engage quality-manager + monitoring + reviewer
- Skip etl-architect and scheduler

### Error Path
**Prompt**: "Quickly design a data pipeline — there are multiple sources but I don't know the details yet"
**Expected Result**:
- Architect proceeds with a generic multi-source pipeline template
- Include per-source connector placeholders and present 3-tier volume options
- Review report notes: "Source details unconfirmed — redesign required once confirmed"


## Per-Agent Extension Skills

| Skill | Path | Augments Agent | Role |
|-------|------|---------------|------|
| data-quality-framework | `.claude/skills/data-quality-framework/skill.md` | data-quality-manager | 6 quality dimensions, Great Expectations, dbt tests, data contracts |
| dag-orchestration-patterns | `.claude/skills/dag-orchestration-patterns/skill.md` | scheduler-engineer | Airflow DAG patterns, idempotency, retry, backfill, dependencies |
