---
name: infra-as-code
description: "A full Infrastructure as Code design and implementation pipeline. An agent team collaborates to perform Terraform/Pulumi-based infrastructure design, security policies, cost optimisation, and drift detection. Use this skill for requests like 'design IaC', 'write Terraform code', 'create infrastructure code', 'Pulumi project design', 'cloud infrastructure design', 'infrastructure security design', 'infrastructure cost optimisation', 'drift detection setup', and other IaC tasks. Also supports codifying existing infrastructure (import). Note: actual terraform apply execution, cloud console operations, and production deployment are outside the scope of this skill."
---

# Infra as Code — IaC Design Pipeline

An agent team collaborates to perform Terraform/Pulumi-based infrastructure design -> security -> cost optimisation -> drift detection.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| infra-architect | `.claude/agents/infra-architect.md` | Architecture, module structure, environment separation | general-purpose |
| security-engineer | `.claude/agents/security-engineer.md` | IAM, networking, encryption, compliance | general-purpose |
| cost-optimizer | `.claude/agents/cost-optimizer.md` | Resource sizing, reservations, FinOps | general-purpose |
| drift-detector | `.claude/agents/drift-detector.md` | State verification, policy compliance, auto-remediation | general-purpose |
| iac-reviewer | `.claude/agents/iac-reviewer.md` | Cross-validation, IaC best practices | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Infrastructure Requirements**: What service the infrastructure is for
    - **Cloud Provider** (optional): AWS / GCP / Azure
    - **IaC Tool** (optional): Terraform / Pulumi / OpenTofu
    - **Constraints** (optional): Budget, compliance, existing infrastructure
    - **Existing Code** (optional): Existing IaC code, architecture documents
2. Create `_workspace/` directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on the scope of the request (see "Modes by Task Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Infrastructure Design | architect | None | `_workspace/01_infra_design.md` |
| 2a | Security Design | security | Task 1 | `_workspace/02_security_design.md` |
| 2b | Cost Analysis | cost | Task 1 | `_workspace/03_cost_analysis.md` |
| 3 | Drift Policy | drift | Tasks 1, 2a | `_workspace/04_drift_policy.md` |
| 4 | Final Review | reviewer | Tasks 1-3 | `_workspace/05_review_report.md` |

Tasks 2a (security) and 2b (cost) can be **executed in parallel**.

**Inter-team Communication Flow:**
- architect completes -> delivers network, IAM, data stores to security; delivers resource specs and scaling to cost; delivers module structure and core resources to drift
- security completes -> delivers security policies and compliance checks to drift; delivers security cost items to cost
- cost completes -> delivers cost anomaly detection criteria to drift
- reviewer cross-validates all deliverables. Requests fixes for RED Must Fix items (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Check all files in `_workspace/`
2. Verify all RED Must Fix items have been addressed
3. Report the final summary to the user

## Modes by Task Scale

| User Request Pattern | Execution Mode | Deployed Agents |
|---------------------|----------------|-----------------|
| "Design infrastructure code", "Full IaC" | **Full Pipeline** | All 5 agents |
| "Design infrastructure architecture only" | **Design Mode** | architect + reviewer |
| "Review infrastructure security" | **Security Mode** | security + reviewer |
| "Analyse infrastructure costs" | **Cost Mode** | cost + reviewer |
| "Set up drift detection" | **Drift Mode** | drift + reviewer |
| "Codify existing infrastructure" | **Import Mode** | architect + drift + reviewer |

**Leveraging Existing Files**: If the user provides existing IaC code, architecture documents, etc., copy the files to the appropriate location in `_workspace/` and skip the corresponding agent's step.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share main deliverables |
| Message-based | SendMessage | Real-time delivery of key information, fix requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Provider undecided | Design with AWS as default, note multi-cloud considerations |
| Scale unestimable | Start small + Auto Scaling for elastic response |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Existing infrastructure conflict | Include terraform import strategy, establish gradual migration plan |

## Test Scenarios

### Normal Flow
**Prompt**: "Design Terraform infrastructure on AWS for running a NestJS API server. Use ECS Fargate + RDS PostgreSQL + ElastiCache Redis, with dev/staging/prod environment separation."
**Expected Result**:
- Design: VPC/subnet design, ECS/RDS/ElastiCache configuration, 3-environment module structure
- Security: Security group matrix, IAM roles, KMS encryption, Checkov policies
- Cost: Per-environment monthly cost estimates, Savings Plan suggestions, dev environment scheduling
- Drift: Security group/IAM immediate remediation, config drift alerts
- Review: Full consistency verification across all items

### Existing Infrastructure Codification Flow
**Prompt**: "I want to convert infrastructure currently managed manually in the AWS console to Terraform"
**Expected Result**:
- Import mode: Establish terraform import strategy
- Resource inventory, import command generation, state verification plan
- Include gradual migration roadmap

### Error Flow
**Prompt**: "Create simple web server infrastructure" (no detailed requirements)
**Expected Result**:
- Start design with basic configuration (VPC + EC2/ECS + ALB + RDS)
- Ask additional requirement questions (scale, DB, domain, etc.)
- Provide minimum configuration + expansion guide

## Agent Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| terraform-module-patterns | `.claude/skills/terraform-module-patterns/skill.md` | infra-architect, drift-detector | Module structure, state management, environment separation, tagging strategy |
| cloud-cost-models | `.claude/skills/cloud-cost-models/skill.md` | cost-optimizer | AWS/GCP cost models, sizing, Savings Plan, FinOps maturity |
