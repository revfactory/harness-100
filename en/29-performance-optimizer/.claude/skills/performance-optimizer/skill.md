---
name: performance-optimizer
description: "A full pipeline where an agent team collaborates to carry out application performance optimization from profiling through bottleneck analysis, optimization implementation, and benchmark verification. Use this skill for all performance improvement work such as 'optimize performance', 'improve a slow API', 'optimize a query', 'reduce response time', 'performance profiling', 'bottleneck analysis', 'benchmark test', 'improve loading speed', 'reduce P95 response time', and 'increase throughput'. It also supports cases where only a specific query optimization or profiling is needed. However, directly executing infrastructure provisioning, configuring load balancers, and deploying a CDN setup directly are out of scope for this skill."
---

# Performance Optimizer — full performance optimization pipeline

An agent team collaborates to carry out an application's profiling→bottleneck analysis→optimization→benchmark in a single pass.

## Execution mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other.

## Agent composition

| Agent | File | Role | Type |
|---------|------|------|------|
| profiler | `.claude/agents/profiler.md` | CPU, memory, I/O, network profiling | general-purpose |
| bottleneck-analyst | `.claude/agents/bottleneck-analyst.md` | hotspot identification, root cause, impact estimation | general-purpose |
| optimization-engineer | `.claude/agents/optimization-engineer.md` | code/query/architecture optimization | general-purpose |
| benchmark-manager | `.claude/agents/benchmark-manager.md` | test design, execution, comparative analysis | general-purpose |
| perf-reviewer | `.claude/agents/perf-reviewer.md` | cross-validation, regression prevention, final report | general-purpose |

## Workflow

### Phase 1: Preparation (orchestrator performs directly)

1. Extract from the user input:
    - **Optimization target**: code, API, query, the whole system
    - **Performance goals**: response time, throughput, memory usage, and other concrete numbers
    - **Tech stack**: language, framework, DB, infrastructure
    - **Current problems** (optional): concrete symptoms, error logs, user complaints
    - **Existing files** (optional): profiling results, execution plans, code
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them into `_workspace/` and skip the corresponding Phase
5. **Decide the execution mode** based on the scope of the request

### Phase 2: Team setup and execution

| Order | Task | Owner | Depends on | Deliverable |
|------|------|------|------|--------|
| 1 | profiling | profiler | none | `_workspace/01_profiling_report.md` |
| 2 | bottleneck analysis | bottleneck-analyst | task 1 | `_workspace/02_bottleneck_analysis.md` |
| 3 | optimization implementation | optimization-engineer | task 2 | `_workspace/03_optimization_plan.md` |
| 4 | benchmark verification | benchmark-manager | tasks 1, 3 | `_workspace/04_benchmark_results.md` |
| 5 | performance review | perf-reviewer | tasks 1~4 | `_workspace/05_review_report.md` |

**Communication flow between team members:**
- profiler done → send hotspot·resource patterns to the analyst, send baseline numbers to benchmark
- analyst done → send bottleneck priorities·root causes to the engineer, send the performance budget to benchmark
- engineer done → send the optimized code·expected numbers to benchmark
- benchmark done → send the comparative analysis results to the reviewer
- The reviewer cross-validates all deliverables. When a 🔴 required fix is found, request a fix from the corresponding agent → rework → re-verify (up to 2 times)

### Phase 3: Integration and final deliverables

1. Verify all files in `_workspace/`
2. Verify that every 🔴 required fix in the review report has been applied
3. Report the final summary to the user:
    - profiling — `01_profiling_report.md`
    - bottleneck analysis — `02_bottleneck_analysis.md`
    - optimization plan — `03_optimization_plan.md`
    - benchmark — `04_benchmark_results.md`
    - review report — `05_review_report.md`

## Modes by task size

| User request pattern | Execution mode | Agents deployed |
|----------------|----------|-------------|
| "optimize overall performance" | **full pipeline** | all 5 members |
| "profile this code" | **profiling mode** | profiler + reviewer |
| "optimize this query" | **query optimization mode** | profiler + analyst + engineer + reviewer |
| "design a benchmark test" | **benchmark mode** | benchmark + reviewer |
| "verify this optimization result" | **review mode** | reviewer alone |

## Data passing protocol

| Strategy | Method | Use |
|------|------|------|
| File-based | `_workspace/` directory | storing and sharing major deliverables |
| Message-based | SendMessage | real-time delivery of key information, fix requests |
| Task-based | TaskCreate/TaskUpdate | progress tracking, dependency management |

## Error handling

| Error type | Strategy |
|----------|------|
| Profiling tool cannot run | fall back to static code analysis, provide a tool setup guide |
| No execution environment | provide a benchmark script + execution guide, simulate expected results |
| Performance goals undefined | propose goals based on industry standards (P95 < 200ms, error rate < 1%) |
| Agent failure | 1 retry → on failure proceed without that deliverable, note the omission in the review report |
| 🔴 found in review | request a fix from the corresponding agent → rework → re-verify (up to 2 times) |

## Test scenarios

### Normal flow
**Prompt**: "The response time of my Django REST API is 2 seconds at P95, and I want to get it under 500ms. Analyze the code and optimize it."
**Expected result**:
- profiling: analyze Django middleware, ORM queries, and the serialization process, detect N+1 queries
- bottleneck analysis: DB queries account for 70% of total response time → diagnose ORM N+1 + missing indexes
- optimization: apply select_related/prefetch_related, add indexes, cache querysets
- benchmark: compare before/after with a k6 script, verify P95 2s → 400ms
- review: confirm consistency, assess regression risk

### Flow using existing files
**Prompt**: "Analyze this profiling result and propose an optimization plan" + flame graph attached
**Expected result**:
- use the existing profiling data as `_workspace/01_profiling_report.md`
- skip profiler and deploy analyst + engineer + benchmark + reviewer

### Error flow
**Prompt**: "The site is slow but I can't tell what's wrong"
**Expected result**:
- perform profiling based on static code analysis
- apply a checklist of common performance anti-patterns
- note "applying a detailed profiling tool is recommended"


## Per-agent extension skills

| Skill | Path | Target agents to strengthen | Role |
|------|------|-----------------|------|
| query-optimization-patterns | `.claude/skills/query-optimization-patterns/skill.md` | bottleneck-analyst, optimization-engineer | execution plan analysis, index design, N+1 resolution, pagination |
| caching-strategy-selector | `.claude/skills/caching-strategy-selector/skill.md` | optimization-engineer | Cache Aside/Write Through/Behind, invalidation, stampede prevention |
