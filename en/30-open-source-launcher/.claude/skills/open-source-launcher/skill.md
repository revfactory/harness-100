---
name: open-source-launcher
description: "A full launch pipeline where an agent team collaborates to prepare an open source project launch — covering code cleanup, documentation, license selection, and community building. Use this skill for open source launches in general, such as 'prepare an open source release', 'open-source this project', 'prepare for GitHub release', 'select an open source license', 'write a README', 'create a CONTRIBUTING guide', 'design an open source community', 'prepare a release', 'set up CI/CD', or 'pre-release code review'. It also supports cases where only a README is needed or only a license review is needed. However, actually creating the repository, calling the GitHub configuration API, and executing package registry deployment are outside this skill's scope."
---

# Open Source Launcher — Open Source Project Launch Pipeline

An agent team collaborates to prepare an open source project's code cleanup → documentation → license → community in one pass.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| code-organizer | `.claude/agents/code-organizer.md` | Restructuring, refactoring, coding standards | general-purpose |
| doc-writer | `.claude/agents/doc-writer.md` | README, contributing guide, API docs | general-purpose |
| license-specialist | `.claude/agents/license-specialist.md` | License selection, compatibility, legal review | general-purpose |
| community-manager | `.claude/agents/community-manager.md` | Governance, CoC, issue templates, CI/CD | general-purpose |
| launch-reviewer | `.claude/agents/launch-reviewer.md` | Cross-validation, launch readiness, final checklist | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from the user's input:
    - **Project code**: the code or repository to open-source
    - **Project goal**: library/framework/tool/application
    - **Target users**: who will use this project
    - **License preference** (optional): commercial use allowed, copyleft preference, etc.
    - **Existing documentation** (optional): an already-written README or docs
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them into `_workspace/` and skip the corresponding Phase
5. **Decide the execution mode** based on the scope of the request

### Phase 2: Team Setup and Execution

| Order | Task | Owner | Depends on | Deliverable |
|------|------|------|------|--------|
| 1 | Code cleanup | code-organizer | None | `_workspace/01_code_organization.md` |
| 2a | Documentation | doc-writer | Task 1 | `_workspace/02_documentation.md` |
| 2b | License review | license-specialist | Task 1 | `_workspace/03_license_review.md` |
| 3 | Community setup | community-manager | Tasks 1, 2a, 2b | `_workspace/04_community_setup.md` |
| 4 | Launch review | launch-reviewer | Tasks 1~3 | `_workspace/05_launch_report.md` |

Tasks 2a (documentation) and 2b (license) run in **parallel**.

**Communication flow between team members:**
- organizer done → deliver project structure·API to doc-writer, deliver dependency list to license, deliver build/test procedures to community
- doc-writer done → request that community confirm consistency between CONTRIBUTING and the issue templates
- license done → deliver the license section content to doc-writer, deliver CLA/DCO to community
- community done → deliver the full configuration to reviewer
- reviewer cross-validates all deliverables. When a 🔴 must-fix is found, request a fix from the relevant agent → rework → re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Confirm all files within `_workspace/` and `_workspace/generated_files/`
2. Confirm that all 🔴 must-fixes from the review report have been addressed
3. Report the final summary to the user:
    - Code cleanup — `01_code_organization.md`
    - Documentation package — `02_documentation.md`
    - License — `03_license_review.md`
    - Community — `04_community_setup.md`
    - Launch report — `05_launch_report.md`
    - Generated files — `generated_files/` (README, LICENSE, CONTRIBUTING, CI, etc.)

## Mode by Task Scale

| User request pattern | Execution mode | Agents deployed |
|----------------|----------|-------------|
| "Prepare the full open source launch" | **Full launch** | All 5 members |
| "Write the README" | **Documentation mode** | doc-writer + reviewer |
| "Review the license" | **License mode** | license-specialist + reviewer |
| "Set up CI/CD" | **CI mode** | community-manager + reviewer |
| "Review before open source release" | **Review mode** | reviewer alone |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Generated files | `_workspace/generated_files/` | Files to actually place in the project |
| Message-based | SendMessage | Real-time transfer of key information, fix requests |

## Error Handling

| Error type | Strategy |
|----------|------|
| No code provided | Provide a general open source project template and checklist |
| Project language unknown | Proceed with a general-purpose configuration (EditorConfig, gitignore), noting per-language options |
| License conflict | Propose an alternative package or a license change option |
| Agent failure | Retry once → if it still fails, proceed without that deliverable and note the omission in the review report |
| 🔴 found in review | Request a fix from the relevant agent → rework → re-verify (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "I want to open-source this Python CLI tool under the MIT license and publish it to PyPI."
**Expected result**:
- Code cleanup: pyproject.toml configuration, structure standardization, secret scan, .gitignore
- Documentation: README (badges+Quick Start+API), CONTRIBUTING, CHANGELOG
- License: MIT selection, dependency compatibility check, LICENSE file generation
- Community: GitHub Actions CI, PyPI deployment workflow, issue/PR templates
- Review: all-item consistency matrix, launch final checklist

### Existing-File Reuse Flow
**Prompt**: "The README already exists, so review the license and set up CI" + README attached
**Expected result**:
- Copy the existing README to `_workspace/generated_files/README.md`
- Merge license mode + CI mode: deploy license + community + reviewer

### Error Flow
**Prompt**: "Prepare the open source release; the code isn't cleaned up yet"
**Expected result**:
- When code is absent, provide a general open source checklist and template set
- Note that "detailed analysis is possible once the code is provided"
- Pre-provide a general-purpose project structure + documentation template + license comparison table


## Per-Agent Extension Skills

| Skill | Path | Target agent | Role |
|------|------|-----------------|------|
| license-compatibility-matrix | `.claude/skills/license-compatibility-matrix/skill.md` | license-specialist | License compatibility matrix, SPDX, dual licensing, conflict resolution |
| community-health-metrics | `.claude/skills/community-health-metrics/skill.md` | community-manager, doc-writer | CHAOSS metrics, GitHub configuration, issue/PR templates, contributor onboarding |
