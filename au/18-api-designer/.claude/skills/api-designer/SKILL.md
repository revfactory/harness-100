---
name: api-designer
description: "Full pipeline for REST/GraphQL API design, documentation, mocking, and testing. An agent team collaborates to perform API architecture design, OpenAPI/GraphQL schema generation, developer documentation writing, and mock server and test design. Use this skill for any API design task including 'design an API', 'REST API', 'GraphQL API', 'API documentation', 'API schema', 'OpenAPI', 'Swagger', 'API testing', 'API mocking', 'endpoint design', etc. Also supports documentation and testing for existing APIs. Note: actual server implementation (Express, FastAPI, etc.), API Gateway deployment, and monitoring dashboard setup are outside the scope of this skill."
---

# API Designer — API Design, Documentation, Mocking, and Testing Pipeline

An agent team collaborates to generate API design, schema, documentation, and mock/tests in a single pass.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| api-architect | `.claude/agents/api-architect.md` | Resource modelling, endpoints, versioning | general-purpose |
| schema-validator | `.claude/agents/schema-validator.md` | OpenAPI/GraphQL schema, type validation | general-purpose |
| doc-writer | `.claude/agents/doc-writer.md` | Developer documentation, examples, error references | general-purpose |
| mock-tester | `.claude/agents/mock-tester.md` | Mock server, integration tests, load scenarios | general-purpose |
| review-auditor | `.claude/agents/review-auditor.md` | Security, consistency, performance, alignment validation | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Domain**: What service is the API for
   - **Paradigm**: REST / GraphQL / Hybrid
   - **Key Resources**: List of core entities
   - **Authentication Method** (optional): OAuth, JWT, API Key
   - **Existing Files** (optional): Existing schemas, documentation, code, etc.
2. Create the `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | API Design | api-architect | None | `_workspace/01_api_design.md` |
| 2 | Schema Generation & Validation | schema-validator | Task 1 | `_workspace/02_schema.yaml`, `02_schema_validation.md` |
| 3a | API Documentation | doc-writer | Tasks 1, 2 | `_workspace/03_api_docs.md` |
| 3b | Mock Server & Tests | mock-tester | Tasks 1, 2 | `_workspace/04_mock_tests.md` |
| 4 | API Review | review-auditor | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (documentation) and 3b (tests) are **executed in parallel**.

**Inter-team communication flow:**
- api-architect completes -> Delivers resource model to schema-validator, endpoints to doc-writer, request/response examples to mock-tester
- schema-validator completes -> Delivers schema to doc-writer, schema-based examples to mock-tester
- doc-writer <-> mock-tester: Mutually verify that documentation examples and mock responses match
- review-auditor cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organise the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Design an API", "full design" | **Full Pipeline** | All 5 agents |
| "Just write API docs" (existing API) | **Documentation Mode** | doc-writer + review-auditor |
| "Validate this OpenAPI schema" | **Validation Mode** | schema-validator + review-auditor |
| "Design API tests" (existing schema) | **Test Mode** | mock-tester + review-auditor |
| "Review this API design" | **Review Mode** | review-auditor only |

**Leveraging existing files**: If the user provides schemas, documentation, or other existing files, skip the corresponding steps.

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
| Insufficient domain information | API architect starts with generic CRUD resources; designs an extensible structure |
| REST vs GraphQL undecided | Default to REST; present GraphQL extension options in an appendix |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing schema parsing failure | Manually extract endpoints and proceed |

## Test Scenarios

### Normal Flow
**Prompt**: "Design a REST API for an e-commerce platform. I need product, order, user, and cart resources"
**Expected Result**:
- API Design: 4 resources, CRUD endpoints, relationship modelling, authentication design
- Schema: OpenAPI 3.1 YAML, all model type definitions
- Documentation: Quick start + endpoint reference + error codes
- Tests: Per-resource CRUD tests + authentication tests + load scenarios
- Review: All items in the alignment matrix verified

### Existing File Flow
**Prompt**: "Create API docs and tests from this OpenAPI schema" + schema file
**Expected Result**:
- Copy existing schema to `_workspace/02_schema.yaml`
- Merged documentation + test mode: deploy doc-writer + mock-tester + review-auditor
- Skip api-architect and schema-validator

### Error Flow
**Prompt**: "Design an API quickly, blog platform"
**Expected Result**:
- Insufficient domain information -> api-architect infers standard blog resources (Post, Comment, User, Tag)
- Execute in full pipeline mode
- Review report notes "design based on inferred domain requirements"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | Target Agent | Role |
|-------|-------------|------|
| `rest-api-conventions` | api-architect | URL naming, HTTP status codes, pagination, versioning |
| `api-error-design` | doc-writer, mock-tester | Error code systems, error response structures, retry/fallback strategies |
