---
name: community-health-metrics
description: "Open source project community health measurement metrics, GitHub project configuration best practices, and contributor experience optimization guide. Use this skill when working on open source community operations involving 'community health', 'GitHub configuration', 'issue templates', 'PR templates', 'CONTRIBUTING', 'Code of Conduct', 'contributor experience', or 'GitHub Actions CI'. Enhances the community design capabilities of community-manager and doc-writer agents. Note: legal license analysis and code refactoring are outside the scope of this skill."
---

# Community Health Metrics — Open Source Community Health Guide

A framework for measuring and improving the community health of open source projects.

## Health Metric System

### CHAOSS Model Core Metrics

| Category | Metric | Measurement | Health Threshold |
|---------|--------|------------|-----------------|
| **Activity** | Commit frequency | Weekly commit count | > 5/week |
| **Activity** | Issue resolution time | Median time from issue open to close | < 7 days |
| **Activity** | PR review time | Median time from PR submission to first review | < 48 hours |
| **Diversity** | New contributor ratio | Monthly first-time contributor count | > 2/month |
| **Diversity** | Bus Factor | Minimum contributors responsible for 80% of code | > 2 |
| **Inclusion** | Contributor retention | Re-contribution rate (6 months) | > 30% |
| **Inclusion** | First PR merge time | First contribution to merge | < 1 week |

### GitHub Project Score Card

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
- [ ] Automated dependency updates (Dependabot/Renovate)
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
      label: Bug Description
      description: What went wrong?
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      description: Please describe the steps to reproduce the bug.
      value: |
        1.
        2.
        3.
  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
  - type: textarea
    id: actual
    attributes:
      label: Actual Behavior
  - type: input
    id: version
    attributes:
      label: Version
  - type: dropdown
    id: os
    attributes:
      label: Operating System
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
- [ ] Tests have been added or updated
- [ ] Documentation has been updated
- [ ] CHANGELOG.md has been updated
- [ ] Existing tests pass

## Related Issues
Closes #
```

## CI/CD Configuration Recommendation

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
Discover → README → Install → Use → Report Issue → First PR → Regular Contributor

Optimization at each stage:
1. Discover: SEO, social media, conferences
2. README: Project comprehensible within 30 seconds
3. Install: 3 steps or fewer, copy-paste friendly
4. Use: Immediately runnable examples
5. Issue: Lower barrier to entry with templates
6. First PR: "good first issue" label, mentoring
7. Regular contribution: Recognition (CONTRIBUTORS.md), role assignment
```

## First-Time Contributor Onboarding

```markdown
## Contributing

### Development Environment Setup
# Step 1: Fork & Clone
git clone https://github.com/YOUR_ID/project.git

# Step 2: Install Dependencies
npm install

# Step 3: Run Tests
npm test

### Finding a Good First Issue
Check issues labeled "good first issue".

### PR Submission Process
1. Create a branch: git checkout -b fix/issue-123
2. Make changes and confirm tests pass
3. Follow commit message conventions (Conventional Commits)
4. Submit the PR and confirm CI passes
```
