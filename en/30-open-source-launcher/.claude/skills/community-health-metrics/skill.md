---
name: community-health-metrics
description: "Open source project community health metrics, GitHub project configuration best practices, and contributor experience optimization guide. Use this skill for open source community operations such as 'community health', 'GitHub configuration', 'issue template', 'PR template', 'CONTRIBUTING', 'Code of Conduct', 'contributor experience', or 'GitHub Actions CI'. It strengthens the community design capability of community-manager and doc-writer. However, legal license analysis and code refactoring are outside this skill's scope."
---

# Community Health Metrics — Open Source Community Health Guide

A framework for measuring and improving the community health of an open source project.

## Health Metrics System

### CHAOSS Model Core Metrics

| Category | Metric | Measurement | Health threshold |
|---------|------|------|----------|
| **Activity** | Commit frequency | Weekly commit count | > 5/week |
| **Activity** | Issue resolution time | Median issue open→close | < 7 days |
| **Activity** | PR review time | Median PR submission→first review | < 48 hours |
| **Diversity** | New contributor ratio | Monthly first-time contributor count | > 2/month |
| **Diversity** | Bus Factor | Minimum people contributing 80% of code | > 2 |
| **Inclusivity** | Contributor retention | Re-contribution rate (6 months) | > 30% |
| **Inclusivity** | First PR merge time | First contribution→merge | < 1 week |

### GitHub Project Scorecard

```markdown
## Project Health Checklist

### Required Files (Must-have)
- [ ] README.md (badges, Quick Start, installation, usage)
- [ ] LICENSE
- [ ] CONTRIBUTING.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CHANGELOG.md

### GitHub Configuration
- [ ] .github/ISSUE_TEMPLATE/ (bug, feature, question)
- [ ] .github/PULL_REQUEST_TEMPLATE.md
- [ ] .github/workflows/ (CI, release)
- [ ] .github/FUNDING.yml (optional)
- [ ] .github/SECURITY.md (vulnerability reporting procedure)

### Quality Tools
- [ ] CI pipeline (test, lint, build)
- [ ] Code coverage badge
- [ ] Automatic dependency updates (Dependabot/Renovate)
- [ ] Release automation (semantic-release)
```

## Issue Templates

### Bug Report

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: Found a bug? Let us know.
labels: ["bug", "triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: Bug description
      description: What went wrong?
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to reproduce
      description: Tell us the steps to reproduce the bug.
      value: |
        1.
        2.
        3.
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
  - type: textarea
    id: actual
    attributes:
      label: Actual behavior
  - type: input
    id: version
    attributes:
      label: Version
  - type: dropdown
    id: os
    attributes:
      label: Operating system
      options: [macOS, Windows, Linux, Other]
```

## PR Template

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->
## Changes
<!-- What did you change and why? -->

## Change Type
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation improvement
- [ ] Refactoring
- [ ] Test addition

## Checklist
- [ ] Added/updated tests
- [ ] Updated documentation
- [ ] Updated CHANGELOG.md
- [ ] Existing tests pass

## Related Issues
Closes #
```

## Recommended CI/CD Configuration

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: [18, 20, 22]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm test
      - run: npm run lint
```

## Contributor Journey Optimization

```
Discovery → README → Installation → Usage → Issue report → First PR → Regular contributor

Optimization at each stage:
1. Discovery: SEO, social media, conferences
2. README: project understandable within 30 seconds
3. Installation: 3 steps or fewer, copy-paste ready
4. Usage: immediately runnable examples
5. Issues: lower the entry barrier with templates
6. First PR: "good first issue" labels, mentoring
7. Regular contribution: recognition (CONTRIBUTORS.md), assigning roles
```

## First Contributor Onboarding

```markdown
## How to Contribute

### Development Environment Setup
# Step 1: Fork & clone
git clone https://github.com/YOUR_ID/project.git

# Step 2: Install dependencies
npm install

# Step 3: Run tests
npm test

### Finding a Good First Issue
Check issues labeled "good first issue".

### PR Submission Procedure
1. Create a branch: git checkout -b fix/issue-123
2. Confirm tests pass after your change
3. Follow the commit message convention (Conventional Commits)
4. Confirm CI passes after submitting the PR
```
