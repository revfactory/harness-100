---
name: cicd-pipeline
description: "Full pipeline for CI/CD pipeline design, build, monitoring, and optimisation. An agent team collaborates to perform stage design, YAML configuration generation, security scan integration, and monitoring/alert design. Use this skill for any CI/CD task including 'create a CI/CD pipeline', 'GitHub Actions', 'GitLab CI', 'Jenkins pipeline', 'deployment automation', 'build pipeline', 'DevOps pipeline', 'auto deploy', 'CI setup', 'CD setup', etc. Also supports optimisation and security hardening for existing pipelines. Note: actual infrastructure provisioning (AWS/GCP resource creation), server configuration, and cluster management are outside the scope of this skill."
---

# CI/CD Pipeline — Pipeline Design, Build, Monitoring, and Optimisation

An agent team collaborates to perform CI/CD pipeline design, configuration generation, security integration, and monitoring in a single pass.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| pipeline-designer | `.claude/agents/pipeline-designer.md` | Stage design, branch strategy, deployment strategy | general-purpose |
| infra-engineer | `.claude/agents/infra-engineer.md` | Runners, containers, secrets, environment configuration | general-purpose |
| monitoring-specialist | `.claude/agents/monitoring-specialist.md` | Metrics, alerts, dashboards, DORA | general-purpose |
| security-scanner | `.claude/agents/security-scanner.md` | SAST, SCA, container scanning, secret detection | general-purpose |
| pipeline-reviewer | `.claude/agents/pipeline-reviewer.md` | Efficiency, reliability, security, alignment verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Project Type**: Language/framework (Node.js, Python, Go, Java, etc.)
   - **CI/CD Tool**: GitHub Actions / GitLab CI / Jenkins
   - **Deployment Target**: AWS / GCP / Azure / Kubernetes / Docker
   - **Branch Strategy** (optional): GitFlow, Trunk-based
   - **Existing Files** (optional): Existing CI/CD configuration, Dockerfile, etc.
2. Create the `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | Pipeline Design | pipeline-designer | None | `_workspace/01_pipeline_design.md` |
| 2a | Infrastructure Config | infra-engineer | Task 1 | `_workspace/02_pipeline_config/`, `02_infra_config.md` |
| 2b | Security Scan Design | security-scanner | Task 1 | `_workspace/04_security_scan.md` |
| 3 | Monitoring Design | monitoring-specialist | Tasks 1, 2a | `_workspace/03_monitoring.md` |
| 4 | Pipeline Review | pipeline-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (infrastructure) and 2b (security) are **executed in parallel**.

**Inter-team communication flow:**
- pipeline-designer completes -> Delivers stage requirements to infra-engineer, scan placement to security-scanner, deployment strategy to monitoring-specialist
- infra-engineer completes -> Delivers log/metric points to monitoring-specialist, image/dependency paths to security-scanner
- security-scanner completes -> Delivers security alert rules to monitoring-specialist
- pipeline-reviewer cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organise the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Create a CI/CD pipeline", "full design" | **Full Pipeline** | All 5 agents |
| "Just set up CI" | **CI Mode** | pipeline-designer + infra-engineer + pipeline-reviewer |
| "Add security scanning to this pipeline" (existing config) | **Security Mode** | security-scanner + pipeline-reviewer |
| "Design pipeline monitoring" (existing config) | **Monitoring Mode** | monitoring-specialist + pipeline-reviewer |
| "Review this CI/CD config" | **Review Mode** | pipeline-reviewer only |

**Leveraging existing files**: If the user provides YAML, Dockerfile, or other existing files, skip the corresponding steps.

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
| CI/CD tool not specified | Default to GitHub Actions |
| Deployment target not specified | Docker container-based generic configuration |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing YAML parsing failure | Manually analyse and create new configuration files |

## Test Scenarios

### Normal Flow
**Prompt**: "Create a GitHub Actions CI/CD pipeline for a Node.js Express app. I want to deploy to AWS ECS with a Canary deployment strategy"
**Expected Result**:
- Design: CI (lint -> test -> build -> scan) + CD (staging -> approval -> canary -> rollout)
- Infrastructure: GitHub Actions YAML, Dockerfile, ECR config, secret management
- Security: Semgrep + Trivy + Gitleaks configuration
- Monitoring: DORA metrics, build/deploy alerts, dashboards
- Review: All items in the alignment matrix verified

### Existing File Flow
**Prompt**: "Add security scanning to this GitHub Actions config" + YAML file
**Expected Result**:
- Copy existing YAML to `_workspace/02_pipeline_config/`
- Security mode: deploy security-scanner + pipeline-reviewer
- Skip pipeline-designer, infra-engineer, monitoring-specialist

### Error Flow
**Prompt**: "Create a CI/CD quickly, Python project"
**Expected Result**:
- Deployment target not specified -> Docker-based generic design
- GitHub Actions selected as default
- Review report notes "deployment target unspecified, Docker container-based generic configuration"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | Target Agent | Role |
|-------|-------------|------|
| `pipeline-security-gates` | security-scanner | SAST/SCA/secret detection tool selection, gate placement, thresholds |
| `deployment-strategies` | pipeline-designer | Blue-Green/Canary/Rolling deployment, rollback, DORA metrics |
