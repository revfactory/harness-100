---
name: fullstack-webapp
description: "A full development pipeline where an agent team collaborates to develop fullstack web apps through requirements analysis, design, frontend, backend, testing, and deployment. Use this skill for requests like 'build me a web app', 'web service development', 'SaaS development', 'CRUD app', 'build a dashboard', 'admin page', 'signup/login feature', 'REST API development', 'fullstack project', 'Next.js app', and other general web application development. Also supports feature additions and refactoring for existing codebases. However, mobile apps (React Native/Flutter), desktop apps (Electron), game development, and ML/AI model training are outside this skill's scope."
---

# Fullstack Web App — Fullstack Web App Development Pipeline

An agent team collaborates to develop web apps through the pipeline of requirements → design → frontend → backend → testing → deployment.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| architect | `.claude/agents/architect.md` | Requirements, architecture, DB, API design | general-purpose |
| frontend-dev | `.claude/agents/frontend-dev.md` | React/Next.js frontend implementation | general-purpose |
| backend-dev | `.claude/agents/backend-dev.md` | API, DB, auth, business logic | general-purpose |
| qa-engineer | `.claude/agents/qa-engineer.md` | Test strategy, test code, code review | general-purpose |
| devops-engineer | `.claude/agents/devops-engineer.md` | CI/CD, infrastructure, deployment, monitoring | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
   - **App Description**: Purpose and core features of the web app to build
   - **Technology Stack** (optional): Preferred frameworks/libraries
   - **Scale** (optional): MVP/small/medium/large
   - **Existing Code** (optional): Existing project to extend
   - **Deployment Platform** (optional): Vercel/AWS/Docker, etc.
2. Create `_workspace/` directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing code is provided, analyse it and adjust relevant phases
5. Determine **execution mode** based on request scope (see "Scale-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverables |
|-------|------|-------|-------------|--------------|
| 1 | Architecture Design | architect | None | `01_architecture.md`, `02_api_spec.md`, `03_db_schema.md` |
| 2a | Frontend Development | frontend | Task 1 | `src/` frontend code |
| 2b | Backend Development | backend | Task 1 | `src/` backend code |
| 2c | Deployment Setup | devops | Task 1 | `05_deploy_guide.md`, CI/CD config |
| 3 | Testing & Review | qa | Tasks 2a, 2b | `04_test_plan.md`, `06_review_report.md`, test code |

Tasks 2a (frontend), 2b (backend), and 2c (DevOps) run **in parallel**. All depend only on Task 1 (design).

**Inter-team Communication Flow:**
- architect completes → delivers component structure/routing to frontend, API/DB/auth to backend, infrastructure requirements to devops, functional requirements to qa
- frontend ↔ backend: Real-time communication during API integration (endpoint changes, error formats, etc.)
- devops completes → shares environment variables and deployment URLs with all
- qa reviews all code and tests. On 🔴 required fix: requests fix from the relevant developer → rework → re-verify (max 2 rounds)

### Phase 3: Integration and Final Deliverables

Organise final deliverables based on the QA review:

1. Verify all code and documents
2. Confirm all 🔴 required fixes from the review have been addressed
3. Report final summary to the user:
   - Architecture Design — `_workspace/01_architecture.md`
   - API Specification — `_workspace/02_api_spec.md`
   - DB Schema — `_workspace/03_db_schema.md`
   - Test Plan — `_workspace/04_test_plan.md`
   - Deployment Guide — `_workspace/05_deploy_guide.md`
   - Review Report — `_workspace/06_review_report.md`
   - Source Code — `src/` directory

## Scale-Based Modes

Adjust the agents deployed based on the scope of the user's request:

| Request Pattern | Execution Mode | Deployed Agents |
|----------------|---------------|----------------|
| "Build me a web app", "fullstack development" | **Full Pipeline** | All 5 |
| "Just build the API" | **Backend Mode** | architect + backend + qa |
| "Just build the frontend" (API exists) | **Frontend Mode** | architect + frontend + qa |
| "Refactor this code" | **Refactoring Mode** | architect + relevant developer + qa |
| "Just set up deployment" | **DevOps Mode** | devops alone |

**Leveraging Existing Code**: If the user provides existing code, the architect analyses it to identify extension points and deploys only the necessary agents.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` + `src/` | Design documents + source code |
| Message-based | SendMessage | API integration issues, code review, fix requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Ambiguous requirements | Apply the most common CRUD pattern, document assumptions |
| Unspecified tech stack | Apply default stack by scale (MVP: Next.js + SQLite) |
| Build errors | Analyse error logs → relevant developer fixes → QA re-verifies |
| Agent failure | Retry once → proceed without that deliverable if failed, note in review |
| 🔴 found in review | Request fix from relevant developer → rework → re-verify (max 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "Build me a to-do management web app. I need signup/login, to-do CRUD, and category classification features."
**Expected Result**:
- Architecture: Next.js + Prisma + SQLite, ERD (users, todos, categories), 10+ API specs
- Frontend: Login/signup pages, dashboard, to-do CRUD UI, responsive
- Backend: Auth API, CRUD API, input validation, error handling
- Tests: Auth + CRUD test scenarios, 80% coverage target
- Deployment: Vercel deployment guide, GitHub Actions CI/CD

### Existing Code Flow
**Prompt**: "Add payment functionality to this Next.js project" + existing code
**Expected Result**:
- architect analyses existing code, designs payment-related API/DB
- backend adds payment API, frontend adds payment UI
- qa tests payment flow

### Error Flow
**Prompt**: "Build me a simple web app"
**Expected Result**:
- Ambiguous requirements → architect proposes a basic CRUD app (memos/notes)
- MVP scale default stack (Next.js + SQLite) applied
- Review report notes "assumptions applied due to vague requirements"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | Target Agent | Role |
|-------|-------------|------|
| `component-patterns` | frontend-dev | React/Next.js component patterns, state management strategies, folder structure |
| `api-security-checklist` | backend-dev | OWASP Top 10, auth patterns, security headers, Rate Limiting |
