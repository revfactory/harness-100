---
name: data-pipeline
description: "A full pipeline where an agent team collaborates to design and implement the ingestion, transformation, loading, quality verification, and monitoring of a data pipeline. Use this skill for the full span of data pipeline design and construction, such as 'design a data pipeline', 'build an ETL pipeline', 'automate data ingestion', 'data warehouse pipeline', 'design an ELT', 'batch pipeline', 'streaming pipeline', 'build me an Airflow DAG', 'design a dbt model', 'data quality verification system'. It also supports cases where only quality verification or monitoring of an existing pipeline is needed. However, directly running a real-time streaming engine (Flink/Spark Streaming), provisioning cloud infrastructure, and database administrator (DBA) work are out of this skill's scope."
---

# Data Pipeline — data pipeline design and implementation

An agent team collaborates to design and implement the ingestion→transformation→loading→quality verification→monitoring of a data pipeline in one pass.

## Execution mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate.

## Agent composition

| Agent | File | Role | Type |
|---------|------|------|------|
| etl-architect | `.claude/agents/etl-architect.md` | Source analysis, schema design, pipeline structure | general-purpose |
| data-quality-manager | `.claude/agents/data-quality-manager.md` | Validation rules, profiling, anomaly detection | general-purpose |
| scheduler-engineer | `.claude/agents/scheduler-engineer.md` | DAG design, dependencies, retry strategy | general-purpose |
| monitoring-specialist | `.claude/agents/monitoring-specialist.md` | Metrics, alerts, dashboards, SLA | general-purpose |
| pipeline-reviewer | `.claude/agents/pipeline-reviewer.md` | Cross-validation, consistency, operational readiness | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from the user input:
    - **Data sources**: source systems (DB, API, files, streaming)
    - **Target system**: data warehouse, data lake, analytics platform
    - **Business needs**: reporting cycle, SLA, data freshness
    - **Technical constraints** (optional): cloud vendor, existing stack, budget
    - **Existing files** (optional): schemas, queries, and configuration files provided by the user
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them into `_workspace/` and skip the corresponding Phase
5. **Decide the execution mode** based on the scope of the request (see "Modes by work scale" below)

### Phase 2: Team setup and execution

Set up the team and assign the work. The dependencies between jobs are as follows:

| Order | Job | Owner | Depends on | Deliverable |
|------|------|------|------|--------|
| 1 | ETL architecture design | etl-architect | None | `_workspace/01_etl_architecture.md` |
| 2a | Data quality plan | data-quality-manager | Job 1 | `_workspace/02_data_quality_plan.md` |
| 2b | Scheduling configuration | scheduler-engineer | Job 1 | `_workspace/03_scheduler_config.md` |
| 3 | Monitoring configuration | monitoring-specialist | Jobs 1, 2a, 2b | `_workspace/04_monitoring_setup.md` |
| 4 | Pipeline review | pipeline-reviewer | Jobs 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

Jobs 2a (quality) and 2b (scheduling) run **in parallel**. Since both depend only on Job 1 (architecture), they can start at the same time.

**Communication flow between team members:**
- etl-architect done → deliver schema·business rules to quality-manager, deliver dependencies·resource requirements to scheduler, deliver core metrics to monitoring
- quality-manager done → deliver the validation-job insertion point·halt conditions to scheduler, deliver quality metrics·SLA to monitoring
- scheduler done → deliver DAG execution metrics to monitoring
- reviewer cross-validates all deliverables. When a 🔴 required fix is found, request a fix from the relevant agent → rework → re-verify (up to 2 times)

### Phase 3: Integration and final deliverables

Organize the final deliverables based on the reviewer's report:

1. Confirm all files within `_workspace/`
2. Confirm that all 🔴 required fixes from the review report have been applied
3. Report the final summary to the user:
    - ETL architecture — `01_etl_architecture.md`
    - Quality management plan — `02_data_quality_plan.md`
    - Scheduling configuration — `03_scheduler_config.md`
    - Monitoring configuration — `04_monitoring_setup.md`
    - Review report — `05_review_report.md`
    - Pipeline code — `pipeline_code/`

## Modes by work scale

Adjust which agents are deployed based on the scope of the user's request:

| User request pattern | Execution mode | Deployed agents |
|----------------|----------|-------------|
| "design a data pipeline", "build the whole ETL" | **Full pipeline** | All 5 members |
| "build a data quality verification system" | **Quality mode** | etl-architect + quality-manager + reviewer |
| "design an Airflow DAG" | **Schedule mode** | etl-architect + scheduler + reviewer |
| "set up a pipeline monitoring dashboard" | **Monitoring mode** | monitoring + reviewer |
| "review this pipeline" | **Review mode** | reviewer alone |

**Reusing existing files**: When the user provides existing files such as schemas or DAG code, copy those files to the appropriate location in `_workspace/` and skip the agent for that stage.

## Data handoff protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time delivery of core information, fix requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error handling

| Error type | Strategy |
|----------|------|
| Missing source connection details | Architect proceeds with a placeholder-based template, marking "connection info not entered" in the deliverable |
| Unknown technology stack | List options for the 3 major clouds (AWS/GCP/Azure) side by side and prompt the user to choose |
| Missing volume information | Present 3-tier architecture options: small (10K/day)·medium (1M/day)·large (100M/day) |
| Agent failure | Retry once → on failure, proceed without that deliverable and mark the omission in the review report |
| 🔴 found in review | Request a fix from the relevant agent → rework → re-verify (up to 2 times) |

## Test scenarios

### Normal flow
**Prompt**: "Design a daily batch pipeline that loads PostgreSQL order data into a BigQuery data warehouse. Based on Airflow."
**Expected result**:
- ETL architecture: PostgreSQL CDC/incremental load strategy, 4 layers Raw→Staging→Curated→Analytics
- Quality plan: P0/P1/P2 validation rules based on order data characteristics, revenue aggregation cross-check
- Scheduling: Airflow DAG code (extract→stage→curate→analytics→quality_check), retry policy
- Monitoring: dashboard for daily load count, latency, and quality score
- Review: all-item consistency matrix

### Existing-file reuse flow
**Prompt**: "Design data quality verification and monitoring for these dbt model files" + dbt model files attached
**Expected result**:
- Copy the existing dbt models to `_workspace/`
- Merge quality mode + monitoring mode: deploy quality-manager + monitoring + reviewer
- Skip etl-architect and scheduler

### Error flow
**Prompt**: "Design a data pipeline quickly; there are several sources but I'm not sure exactly yet"
**Expected result**:
- Architect proceeds with a generic multi-source pipeline template
- Includes per-source connector placeholders, presents 3-tier options by volume
- Marks "source info not finalized — redesign needed after finalization" in the review report


## Per-agent extension skills

| Skill | Path | Agent it reinforces | Role |
|------|------|-----------------|------|
| data-quality-framework | `.claude/skills/data-quality-framework/skill.md` | data-quality-manager | Quality 6 dimensions, Great Expectations, dbt tests, data contracts |
| dag-orchestration-patterns | `.claude/skills/dag-orchestration-patterns/skill.md` | scheduler-engineer | Airflow DAG patterns, idempotency, retries, backfill, dependencies |
