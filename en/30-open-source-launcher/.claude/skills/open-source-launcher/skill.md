---
name: open-source-launcher
description: "A full launching pipeline where an agent team collaborates to prepare an open source project launch end-to-end: code cleanup, documentation, license selection, and community building. Use this skill for all open source launching tasks involving requests like 'prepare open source publication', 'open source a project', 'prepare for GitHub release', 'select an open source license', 'write a README', 'create a CONTRIBUTING guide', 'design an open source community', 'prepare a release', 'set up CI/CD', or 'pre-publication code review'. Also supported for README-only or license-review-only requests. Note: actual repository creation, GitHub Settings API calls, and package registry deployment are outside the scope of this skill."
---

# Open Source Launcher — Open Source Project Launching Pipeline

An agent team collaborates to prepare an open source project's code cleanup, documentation, licensing, and community setup all at once.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| code-organizer | `.claude/agents/code-organizer.md` | Restructuring, refactoring, code standards | general-purpose |
| doc-writer | `.claude/agents/doc-writer.md` | README, contributing guide, API documentation | general-purpose |
| license-specialist | `.claude/agents/license-specialist.md` | License selection, compatibility, legal review | general-purpose |
| community-manager | `.claude/agents/community-manager.md` | Governance, CoC, issue templates, CI/CD | general-purpose |
| launch-reviewer | `.claude/agents/launch-reviewer.md` | Cross-validation, launch readiness, final checklist | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Project code**: The code or repository to be open-sourced
    - **Project goal**: Library / framework / tool / application
    - **Target audience**: Who will use this project
    - **License preference** (optional): Commercial use allowed, copyleft preference, etc.
    - **Existing documentation** (optional): Already-written README, docs
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding phase
5. **Decide the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Output |
|-------|------|-------|-----------|--------|
| 1 | Code cleanup | code-organizer | None | `_workspace/01_code_organization.md` |
| 2a | Documentation | doc-writer | Task 1 | `_workspace/02_documentation.md` |
| 2b | License review | license-specialist | Task 1 | `_workspace/03_license_review.md` |
| 3 | Community setup | community-manager | Tasks 1, 2a, 2b | `_workspace/04_community_setup.md` |
| 4 | Launch review | launch-reviewer | Tasks 1–3 | `_workspace/05_launch_report.md` |

Tasks 2a (documentation) and 2b (license) are executed **in parallel**.

**Team communication flow:**
- organizer complete → delivers project structure and API info to doc-writer, dependency list to license-specialist, build/test procedures to community-manager
- doc-writer complete → requests consistency check of CONTRIBUTING and issue templates from community-manager
- license-specialist complete → delivers license section content to doc-writer, CLA/DCO details to community-manager
- community-manager complete → delivers full configuration to reviewer
- reviewer cross-validates all outputs. When a 🔴 required fix is found, requests correction from the relevant agent → rework → re-validation (maximum 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Confirm all files in `_workspace/` and `_workspace/generated_files/`
2. Verify that all 🔴 required fixes from the review report have been applied
3. Report the final summary to the user:
    - Code cleanup — `01_code_organization.md`
    - Documentation package — `02_documentation.md`
    - License — `03_license_review.md`
    - Community — `04_community_setup.md`
    - Launch report — `05_launch_report.md`
    - Generated files — `generated_files/` (README, LICENSE, CONTRIBUTING, CI, etc.)

## Mode by Request Scale

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|---------------|----------------|
| "Prepare full open source launch" | **Full Launch** | All 5 agents |
| "Write a README" | **Documentation Mode** | doc-writer + reviewer |
| "Review the license" | **License Mode** | license-specialist + reviewer |
| "Set up CI/CD" | **CI Mode** | community-manager + reviewer |
| "Review before open source release" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary outputs |
| Generated files | `_workspace/generated_files/` | Files to be placed directly in the project |
| Message-based | SendMessage | Real-time core information delivery, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|---------|
| No code provided | Provide a generic open source project template and checklist |
| Project language unknown | Proceed with universal configuration (EditorConfig, gitignore), list language-specific options |
| License conflict | Present alternative packages or license change options |
| Agent failure | Retry once → if still failing, proceed without that output and note the gap in the review report |
| 🔴 found in review | Request correction from the relevant agent → rework → re-validation (maximum 2 iterations) |

## Test Scenarios

### Normal Flow
**Prompt**: "I want to open source this Python CLI tool. MIT license, with PyPI distribution."
**Expected Result**:
- Code cleanup: pyproject.toml setup, structure standardization, secret scan, .gitignore
- Documentation: README (badges + Quick Start + API), CONTRIBUTING, CHANGELOG
- License: MIT selected, dependency compatibility verified, LICENSE file generated
- Community: GitHub Actions CI, PyPI deployment workflow, issue/PR templates
- Review: consistency matrix across all items, final launch checklist

### Existing File Flow
**Prompt**: "I already have a README — review the license and set up CI" + README attached
**Expected Result**:
- Copy existing README to `_workspace/generated_files/README.md`
- Merge License Mode + CI Mode: license-specialist + community-manager + reviewer deployed

### Error Flow
**Prompt**: "Prepare for open source, the code isn't cleaned up yet"
**Expected Result**:
- When code is absent, provide a generic open source checklist and template set
- Explicitly state: "Detailed analysis possible after code is provided"
- Pre-provide universal project structure + documentation templates + license comparison table


## Per-Agent Extension Skills

| Skill | Path | Augmented Agent | Role |
|-------|------|----------------|------|
| license-compatibility-matrix | `.claude/skills/license-compatibility-matrix/skill.md` | license-specialist | License compatibility matrix, SPDX, dual licensing, conflict resolution |
| community-health-metrics | `.claude/skills/community-health-metrics/skill.md` | community-manager, doc-writer | CHAOSS metrics, GitHub configuration, issue/PR templates, contributor onboarding |
