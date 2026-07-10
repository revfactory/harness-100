---
name: pipeline-security-gates
description: "CI/CD 파이프라인 보안 게이트 설계 가이드. SAST/DAST/SCA/컨테이너 스캔/시크릿 탐지 도구 선택, 게이트 배치 전략, 임계값 설정, 취약점 분류 기준을 제공하는 security-scanner 확장 스킬. '보안 게이트', 'SAST', 'DAST', 'SCA', '컨테이너 스캔', '시크릿 탐지', '취약점 임계값' 등 파이프라인 보안 통합 시 사용한다. 단, 실제 스캔 실행이나 취약점 수정은 이 스킬의 범위가 아니다."
---

# Pipeline Security Gates — CI/CD 보안 게이트 설계 가이드

security-scanner 에이전트가 파이프라인 보안 설계 시 활용하는 스캔 도구 선택, 게이트 배치, 임계값 설정 레퍼런스.

## 대상 에이전트

`security-scanner` — 이 스킬의 보안 게이트 패턴과 도구 선택을 파이프라인 보안 설계에 직접 적용한다.

## 보안 스캔 유형 & 도구 매트릭스

### 스캔 유형 개요

| 유형 | 정식 명칭 | 대상 | 시점 | 비용 |
|------|----------|------|------|------|
| **SAST** | Static Application Security Testing | 소스 코드 | 커밋/PR | 낮음 |
| **SCA** | Software Composition Analysis | 의존성/라이브러리 | 빌드 전 | 낮음 |
| **Secret** | Secret Detection | 코드 내 민감정보 | 커밋/PR | 낮음 |
| **Container** | Container Image Scanning | Docker 이미지 | 빌드 후 | 중간 |
| **DAST** | Dynamic Application Security Testing | 실행 중 앱 | 스테이징 | 높음 |
| **IaC** | Infrastructure as Code Scanning | Terraform/K8s | PR | 낮음 |
| **License** | License Compliance | 오픈소스 라이선스 | 빌드 | 낮음 |

### 도구 선택 가이드

#### SAST (정적 분석)
| 도구 | 언어 지원 | 오픈소스 | 특징 |
|------|----------|---------|------|
| **Semgrep** | 20+ 언어 | O | 규칙 커스텀 용이, 빠름 |
| **CodeQL** | 10+ 언어 | O (GitHub) | GitHub 네이티브, 심층 분석 |
| **SonarQube** | 25+ 언어 | 부분 | 품질 + 보안 통합 |
| **Bandit** | Python 전용 | O | Python 특화 |
| **ESLint Security** | JS/TS 전용 | O | ESLint 플러그인 |

#### SCA (의존성 분석)
| 도구 | 특징 |
|------|------|
| **Dependabot** | GitHub 네이티브, 자동 PR |
| **Snyk** | DB 최대, 자동 수정 제안 |
| **OWASP Dependency-Check** | OWASP 공식, 오픈소스 |
| **Trivy** | 컨테이너 + SCA 통합 |
| **npm audit / pip-audit** | 언어 네이티브 |

#### 시크릿 탐지
| 도구 | 특징 |
|------|------|
| **Gitleaks** | Git 히스토리 전체 스캔, 빠름 |
| **TruffleHog** | 엔트로피 + 패턴 기반 |
| **detect-secrets** | Yelp 개발, pre-commit hook |
| **GitHub Secret Scanning** | GitHub 네이티브, 파트너 패턴 |

#### 컨테이너 스캔
| 도구 | 특징 |
|------|------|
| **Trivy** | 가장 포괄적, OS + 앱 패키지 |
| **Grype** | Anchore 오픈소스, 빠름 |
| **Docker Scout** | Docker 공식 |
| **Snyk Container** | 수정 가이드 포함 |

#### IaC 스캔
| 도구 | 대상 |
|------|------|
| **tfsec** | Terraform |
| **Checkov** | Terraform, K8s, CloudFormation |
| **KICS** | 다중 IaC 지원 |
| **kubescape** | Kubernetes 전용 |

## 게이트 배치 전략

### 파이프라인 단계별 보안 게이트

```
[1. Pre-Commit]
  ├── Secret Detection (Gitleaks pre-commit)
  └── Lint Security Rules

[2. PR/커밋]
  ├── SAST (Semgrep/CodeQL)
  ├── SCA (Dependabot/Snyk)
  ├── Secret Detection (전체 스캔)
  ├── License Check
  └── IaC Scan (해당 시)

[3. 빌드]
  ├── Container Image Scan (Trivy)
  └── SBOM 생성 (Software Bill of Materials)

[4. 스테이징]
  ├── DAST (선택적)
  └── 통합 보안 테스트

[5. 프로덕션 배포]
  └── 최종 승인 게이트 (보안 리포트 확인)
```

### 게이트 차단/경고 정책

| 스캔 유형 | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| SAST | 차단 | 차단 | 경고 | 무시 |
| SCA (CVE) | 차단 | 차단 | 경고 | 무시 |
| Secret | 차단 | 차단 | 차단 | 경고 |
| Container | 차단 | 경고 | 무시 | 무시 |
| IaC | 차단 | 경고 | 무시 | 무시 |
| License | 차단 (GPL) | 경고 | 무시 | 무시 |

## 취약점 심각도 분류

### CVSS v3.1 기반

| 등급 | CVSS 점수 | SLA (수정 기한) | 게이트 액션 |
|------|----------|---------------|-----------|
| Critical | 9.0~10.0 | 24시간 이내 | 배포 차단 |
| High | 7.0~8.9 | 7일 이내 | 배포 차단 |
| Medium | 4.0~6.9 | 30일 이내 | 경고, 배포 허용 |
| Low | 0.1~3.9 | 90일 이내 | 정보성 |

### 예외 처리 (Suppression)
```yaml
# .trivyignore 또는 .semgrepignore 예시
# 사유와 만료일 필수 기록

CVE-2024-12345  # 영향 없음 (사용하지 않는 기능). 만료: 2025-06-30
RULE-001        # False positive. 검토자: @security-team
```

## GitHub Actions 보안 게이트 YAML 패턴

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

### SBOM 생성 도구
| 도구 | 포맷 | 특징 |
|------|------|------|
| **Syft** | SPDX, CycloneDX | Anchore, 가장 포괄적 |
| **Trivy** | SPDX, CycloneDX | 스캔과 통합 |
| **docker sbom** | SPDX | Docker 공식 |

### SBOM 필수 정보
- 패키지명, 버전, 라이선스
- 의존성 트리 (직접/간접)
- 해시값 (무결성 검증)
- 공급자 정보
