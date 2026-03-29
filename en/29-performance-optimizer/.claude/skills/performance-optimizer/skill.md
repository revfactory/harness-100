---
name: performance-optimizer
description: "Full pipeline for application performance optimization — profiling, bottleneck analysis, optimization implementation, and benchmark verification — performed collaboratively by an agent team. Use this skill for general performance improvement including 'optimize performance', 'improve slow API', 'query optimization', 'reduce response time', 'performance profiling', 'bottleneck analysis', 'benchmark test', 'improve loading speed', 'reduce P95 response time', 'increase throughput', and similar requests. Also supports cases where only specific query optimization or profiling is needed. Note: direct infrastructure provisioning, load balancer configuration, and CDN deployment are outside the scope of this skill."
---

# Performance Optimizer — Full Performance Optimization Pipeline

An agent team collaboratively performs profiling → bottleneck analysis → optimization → benchmarking for an application in a single pass.

## Execution Mode

**Agent team** — 5 members communicate directly via SendMessage and cross-validate results.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| profiler | `.claude/agents/profiler.md` | CPU, memory, I/O, network profiling | general-purpose |
| bottleneck-analyst | `.claude/agents/bottleneck-analyst.md` | Hotspot identification, root cause, impact assessment | general-purpose |
| optimization-engineer | `.claude/agents/optimization-engineer.md` | Code/query/architecture optimization | general-purpose |
| benchmark-manager | `.claude/agents/benchmark-manager.md` | Test design, execution, comparative analysis | general-purpose |
| perf-reviewer | `.claude/agents/perf-reviewer.md` | Cross-validation, regression prevention, final report | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Optimization target**: Code, API, query, or entire system
    - **Performance goals**: Concrete figures for response time, throughput, memory usage, etc.
    - **Technology stack**: Language, framework, DB, infrastructure
    - **Current issues** (optional): Specific symptoms, error logs, user complaints
    - **Existing files** (optional): Profiling results, execution plans, code
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding phase
5. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Step | Task | Responsible | Depends On | Deliverable |
|------|------|-------------|------------|-------------|
| 1 | Profiling | profiler | None | `_workspace/01_profiling_report.md` |
| 2 | Bottleneck analysis | bottleneck-analyst | Step 1 | `_workspace/02_bottleneck_analysis.md` |
| 3 | Optimization implementation | optimization-engineer | Step 2 | `_workspace/03_optimization_plan.md` |
| 4 | Benchmark verification | benchmark-manager | Steps 1, 3 | `_workspace/04_benchmark_results.md` |
| 5 | Performance review | perf-reviewer | Steps 1–4 | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- profiler done → deliver hotspots and resource patterns to analyst; deliver baseline figures to benchmark
- analyst done → deliver bottleneck priority and root cause to engineer; deliver performance budget to benchmark
- engineer done → deliver optimized code and expected figures to benchmark
- benchmark done → deliver comparison analysis results to reviewer
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request correction from responsible agent → rework → re-verify (up to 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report final summary to the user:
    - Profiling — `01_profiling_report.md`
    - Bottleneck analysis — `02_bottleneck_analysis.md`
    - Optimization plan — `03_optimization_plan.md`
    - Benchmark — `04_benchmark_results.md`
    - Review report — `05_review_report.md`

## Modes by Task Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|--------------------|----------------|----------------|
| "Optimize overall performance" | **Full pipeline** | All 5 agents |
| "Profile this code" | **Profiling mode** | profiler + reviewer |
| "Optimize this query" | **Query optimization mode** | profiler + analyst + engineer + reviewer |
| "Design a benchmark test" | **Benchmark mode** | benchmark + reviewer |
| "Verify this optimization result" | **Review mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time delivery of key information and correction requests |
| Task-based | TaskCreate/TaskUpdate | Track progress and manage dependencies |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Profiling tool cannot be executed | Replace with static code analysis; provide tool setup guide |
| Execution environment unavailable | Provide benchmark script + execution guide; simulate expected results |
| Performance target undefined | Propose industry-standard targets (P95 < 200ms, error rate < 1%) |
| Agent failure | 1 retry → if still failing, proceed without that deliverable and note the omission in the review report |
| 🔴 Found in review | Request correction from responsible agent → rework → re-verify (up to 2 iterations) |

## Test Scenarios

### Normal Flow
**Prompt**: "The P95 response time of my Django REST API is 2 seconds. I want to bring it under 500ms. Analyze the code and optimize it."
**Expected result**:
- Profiling: Analyze Django middleware, ORM queries, serialization; detect N+1 queries
- Bottleneck analysis: DB queries account for 70% of total response time → ORM N+1 + missing index
- Optimization: Apply select_related/prefetch_related, add indexes, cache querysets
- Benchmark: k6 script comparing before/after; verify P95 2s → 400ms
- Review: Verify consistency, assess regression risk

### Existing File Flow
**Prompt**: "Analyze this profiling result and suggest optimization approaches" + flame graph attached
**Expected result**:
- Use existing profiling data as `_workspace/01_profiling_report.md`
- Skip profiler; deploy analyst + engineer + benchmark + reviewer

### Error Flow
**Prompt**: "My site is slow but I don't know what's wrong"
**Expected result**:
- Perform profiling based on static code analysis
- Apply general performance anti-pattern checklist
- Note "recommend applying detailed profiling tools"


## Per-Agent Extension Skills

| Skill | Path | Enhances Agent | Role |
|-------|------|---------------|------|
| query-optimization-patterns | `.claude/skills/query-optimization-patterns/skill.md` | bottleneck-analyst, optimization-engineer | Execution plan analysis, index design, N+1 resolution, pagination |
| caching-strategy-selector | `.claude/skills/caching-strategy-selector/skill.md` | optimization-engineer | Cache Aside/Write Through/Behind, invalidation, stampede prevention |
