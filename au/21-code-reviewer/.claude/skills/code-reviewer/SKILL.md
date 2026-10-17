---
name: code-reviewer
description: "Full pipeline for automated code review. An agent team collaborates to systematically review 4 domains: style, security, performance, and architecture. Use this skill for any code review task including 'review this code', 'look at this code', 'code inspection', 'PR review', 'code quality analysis', 'security review', 'performance review', 'architecture review', 'code style check', etc. Also supports requests for specific domains only. Note: actual CI/CD integration, auto-fix, and Git commit/merge operations are outside the scope of this skill."
---

# Code Reviewer — Automated Code Review Pipeline

An agent team systematically reviews code across style, security, performance, and architecture.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| style-inspector | `.claude/agents/style-inspector.md` | Conventions, formatting, naming, readability | general-purpose |
| security-analyst | `.claude/agents/security-analyst.md` | Vulnerabilities, injection, authentication, data exposure | general-purpose |
| performance-analyst | `.claude/agents/performance-analyst.md` | Complexity, memory, concurrency, queries | general-purpose |
| architecture-reviewer | `.claude/agents/architecture-reviewer.md` | Design patterns, SOLID, dependencies, coupling | general-purpose |
| review-synthesizer | `.claude/agents/review-synthesizer.md` | Priority synthesis, conflict resolution, final verdict | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Target Code**: File paths, PR number, diff, directory
   - **Language/Framework**: Auto-detect or user-specified
   - **Review Scope** (optional): If only specific domains were requested
   - **Context** (optional): PR description, related issues, change rationale
   - **Style Guide** (optional): Team-specific conventions
2. Create the `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. Identify the target code and determine the review scope
5. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
6. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1a | Style Review | style-inspector | None | `_workspace/01_style_review.md` |
| 1b | Security Review | security-analyst | None | `_workspace/02_security_review.md` |
| 1c | Performance Review | performance-analyst | None | `_workspace/03_performance_review.md` |
| 1d | Architecture Review | architecture-reviewer | None | `_workspace/04_architecture_review.md` |
| 2 | Comprehensive Review | review-synthesizer | Tasks 1a-1d | `_workspace/05_review_summary.md` |

Tasks 1a-1d (all 4 domain reviews) are **all executed in parallel**.

**Inter-team communication flow:**
- style-inspector -> Delivers sensitive info in comments to security-analyst, complex function lists to performance-analyst
- security-analyst -> Delivers security measure performance impact to performance-analyst, authentication architecture to architecture-reviewer
- performance-analyst -> Delivers structural bottlenecks to architecture-reviewer
- review-synthesizer integrates all reviews. Requests additional analysis from relevant analysts when cross-domain conflicts are found

### Phase 3: Integration and Final Artifacts

Organise the final artifacts based on the comprehensive report:

1. Verify all reviews in `_workspace/`
2. Determine the final verdict (Approve/Request Changes/Reject)
3. Report the final summary to the user

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Review this code", "full review" | **Full Review** | All 5 agents |
| "Security review only" | **Security Mode** | security-analyst + review-synthesizer |
| "Analyse performance" | **Performance Mode** | performance-analyst + review-synthesizer |
| "Architecture review" | **Architecture Mode** | architecture-reviewer + review-synthesizer |
| "Just check code style" | **Style Mode** | style-inspector + review-synthesizer |

**PR Review**: When a PR number is provided, extract the diff and focus review on changed code. Reference full file context but concentrate the review on the diff.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary artifacts |
| Message-based | SendMessage | Real-time delivery of key information, additional analysis requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{artifact}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Language not identified | Auto-detect from file extensions + code patterns |
| Large codebase | Focus on changed or core files; note the scope in the review report |
| Agent failure | Retry once -> If still fails, proceed without that domain; note the omission in the comprehensive report |
| Cross-domain conflict | review-synthesizer performs trade-off analysis and renders verdict |
| Insufficient context | Review based on code alone if no PR description or issue number; note limitations |

## Test Scenarios

### Normal Flow
**Prompt**: "Do a full code review of this Python Flask project" + code files/directory
**Expected Result**:
- Style: PEP 8 standards, naming/formatting/readability checks, Black/flake8 config suggestions
- Security: SQL injection, XSS, hardcoded secrets, dependency CVE checks
- Performance: Query optimisation, N+1, memory usage, caching opportunities
- Architecture: MVC pattern compliance, SOLID, dependency analysis
- Comprehensive: Unified priorities, final verdict, action items

### Existing File Flow
**Prompt**: "Review only the security of this PR" + PR diff
**Expected Result**:
- Security mode: deploy security-analyst + review-synthesizer
- Diff-focused review, full file context for reference
- Skip style-inspector, performance-analyst, architecture-reviewer

### Error Flow
**Prompt**: "Look at this code" + single file (under 100 lines)
**Expected Result**:
- Small codebase -> Architecture review shifts to function separation/module design perspective
- Run in full review mode, but each domain adjusts to code scale
- Comprehensive report notes "single file review, architecture assessment limited"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Skill | Target Agent | Role |
|-------|-------------|------|
| `vulnerability-patterns` | security-analyst | CWE classification, language-specific vulnerability patterns, safe alternatives |
| `refactoring-catalog` | architecture-reviewer, performance-analyst | Code smell to refactoring mapping, SOLID violations, complexity metrics |
