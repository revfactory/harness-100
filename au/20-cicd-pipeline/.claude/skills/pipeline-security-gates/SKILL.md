---
name: pipeline-security-gates
description: "CI/CD pipeline security gate design guide. An extension skill for security-scanner that provides scan tool selection for SAST/DAST/SCA/container scanning/secret detection, gate placement strategies, threshold configuration, and vulnerability classification criteria. Use when integrating pipeline security involving 'security gates', 'SAST', 'DAST', 'SCA', 'container scanning', 'secret detection', 'vulnerability thresholds', etc. Note: actual scan execution and vulnerability remediation are outside the scope of this skill."
---

# Pipeline Security Gates — CI/CD Security Gate Design Guide

A reference of scan tool selection, gate placement, and threshold configuration used by the security-scanner agent when designing pipeline security.

## Target Agent

`security-scanner` — Directly applies the security gate patterns and tool selection from this skill to pipeline security design.

## Security Scan Types & Tool Matrix

### Scan Type Overview

| Type | Full Name | Target | Timing | Cost |
|------|-----------|--------|--------|------|
| **SAST** | Static Application Security Testing | Source code | Commit/PR | Low |
| **SCA** | Software Composition Analysis | Dependencies/libraries | Pre-build | Low |
| **Secret** | Secret Detection | Sensitive data in code | Commit/PR | Low |
| **Container** | Container Image Scanning | Docker images | Post-build | Medium |
| **DAST** | Dynamic Application Security Testing | Running application | Staging | High |
| **IaC** | Infrastructure as Code Scanning | Terraform/K8s | PR | Low |
| **License** | License Compliance | Open source licenses | Build | Low |

### Tool Selection Guide

#### SAST (Static Analysis)
| Tool | Language Support | Open Source | Features |
|------|-----------------|------------|----------|
| **Semgrep** | 20+ languages | Yes | Easy custom rules, fast |
| **CodeQL** | 10+ languages | Yes (GitHub) | GitHub native, deep analysis |
| **SonarQube** | 25+ languages | Partial | Quality + security integration |
| **Bandit** | Python only | Yes | Python-specific |
| **ESLint Security** | JS/TS only | Yes | ESLint plugin |

#### SCA (Dependency Analysis)
| Tool | Features |
|------|----------|
| **Dependabot** | GitHub native, automatic PRs |
| **Snyk** | Largest DB, automatic fix suggestions |
| **OWASP Dependency-Check** | OWASP official, open source |
| **Trivy** | Container + SCA integration |
| **npm audit / pip-audit** | Language native |

#### Secret Detection
| Tool | Features |
|------|----------|
| **Gitleaks** | Full Git history scan, fast |
| **TruffleHog** | Entropy + pattern based |
| **detect-secrets** | Developed by Yelp, pre-commit hook |
| **GitHub Secret Scanning** | GitHub native, partner patterns |

#### Container Scanning
| Tool | Features |
|------|----------|
| **Trivy** | Most comprehensive, OS + app packages |
| **Grype** | Anchore open source, fast |
| **Docker Scout** | Docker official |
| **Snyk Container** | Includes fix guidance |

#### IaC Scanning
| Tool | Target |
|------|--------|
| **tfsec** | Terraform |
| **Checkov** | Terraform, K8s, CloudFormation |
| **KICS** | Multi-IaC support |
| **kubescape** | Kubernetes only |

## Gate Placement Strategy

### Security Gates by Pipeline Stage

```
[1. Pre-Commit]
  ├── Secret Detection (Gitleaks pre-commit)
  └── Lint Security Rules

[2. PR/Commit]
  ├── SAST (Semgrep/CodeQL)
  ├── SCA (Dependabot/Snyk)
  ├── Secret Detection (full scan)
  ├── License Check
  └── IaC Scan (if applicable)

[3. Build]
  ├── Container Image Scan (Trivy)
  └── SBOM Generation (Software Bill of Materials)

[4. Staging]
  ├── DAST (optional)
  └── Integration Security Tests

[5. Production Deployment]
  └── Final Approval Gate (security report review)
```

### Gate Block/Warn Policy

| Scan Type | Critical | High | Medium | Low |
|-----------|----------|------|--------|-----|
| SAST | Block | Block | Warn | Ignore |
| SCA (CVE) | Block | Block | Warn | Ignore |
| Secret | Block | Block | Block | Warn |
| Container | Block | Warn | Ignore | Ignore |
| IaC | Block | Warn | Ignore | Ignore |
| License | Block (GPL) | Warn | Ignore | Ignore |

## Vulnerability Severity Classification

### CVSS v3.1 Based

| Rating | CVSS Score | SLA (Fix Deadline) | Gate Action |
|--------|-----------|-------------------|------------|
| Critical | 9.0-10.0 | Within 24 hours | Block deployment |
| High | 7.0-8.9 | Within 7 days | Block deployment |
| Medium | 4.0-6.9 | Within 30 days | Warn, allow deployment |
| Low | 0.1-3.9 | Within 90 days | Informational |

### Exception Handling (Suppression)
```yaml
# .trivyignore or .semgrepignore example
# Reason and expiry date required

CVE-2024-12345  # No impact (unused feature). Expires: 2025-06-30
RULE-001        # False positive. Reviewer: @security-team
```

## GitHub Actions Security Gate YAML Patterns

### Semgrep (SAST)
```yaml
semgrep:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: returntocorp/semgrep-action@v1
      with:
        config: >-
          p/owasp-top-ten
          p/r2c-security-audit
```

### Trivy (Container + SCA)
```yaml
trivy:
  runs-on: ubuntu-latest
  steps:
    - uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'image'
        image-ref: '${{ env.IMAGE }}'
        severity: 'CRITICAL,HIGH'
        exit-code: '1'
```

### Gitleaks (Secret)
```yaml
gitleaks:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - uses: gitleaks/gitleaks-action@v2
```

## SBOM (Software Bill of Materials)

### SBOM Generation Tools
| Tool | Format | Features |
|------|--------|----------|
| **Syft** | SPDX, CycloneDX | Anchore, most comprehensive |
| **Trivy** | SPDX, CycloneDX | Integrated with scanning |
| **docker sbom** | SPDX | Docker official |

### SBOM Required Information
- Package name, version, license
- Dependency tree (direct/transitive)
- Hash values (integrity verification)
- Supplier information
