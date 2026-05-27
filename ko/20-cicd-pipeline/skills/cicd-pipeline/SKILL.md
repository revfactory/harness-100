---
name: cicd-pipeline
description: "CI/CD 파이프라인 설계·구축·모니터링·최적화 풀 파이프라인. 스테이지 설계, YAML 설정 생성, 보안 스캔 통합, 모니터링/알림 설계를 에이전트 팀이 협업하여 수행한다. 'CI/CD 파이프라인 만들어줘', 'GitHub Actions', 'GitLab CI', 'Jenkins 파이프라인', '배포 자동화', '빌드 파이프라인', 'DevOps 파이프라인', '자동 배포', 'CI 설정', 'CD 설정' 등 CI/CD 전반에 이 스킬을 사용한다. 기존 파이프라인이 있는 경우에도 최적화나 보안 강화를 지원한다. 단, 실제 인프라 프로비저닝(AWS/GCP 리소스 생성), 서버 설정, 클러스터 관리는 이 스킬의 범위가 아니다."
---

# CI/CD Pipeline — 파이프라인 설계·구축·모니터링·최적화

CI/CD 파이프라인의 설계→설정 생성→보안 통합→모니터링을 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| pipeline-designer | `agents/pipeline-designer.md` | 스테이지 설계, 브랜치 전략, 배포 전략 | general-purpose |
| infra-engineer | `agents/infra-engineer.md` | 러너, 컨테이너, 시크릿, 환경 구성 | general-purpose |
| monitoring-specialist | `agents/monitoring-specialist.md` | 메트릭, 알림, 대시보드, DORA | general-purpose |
| security-scanner | `agents/security-scanner.md` | SAST, SCA, 컨테이너 스캔, 시크릿 탐지 | general-purpose |
| pipeline-reviewer | `agents/pipeline-reviewer.md` | 효율성, 안정성, 보안, 정합성 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **프로젝트 유형**: 언어/프레임워크 (Node.js, Python, Go, Java 등)
   - **CI/CD 도구**: GitHub Actions / GitLab CI / Jenkins
   - **배포 대상**: AWS / GCP / Azure / Kubernetes / Docker
   - **브랜치 전략** (선택): GitFlow, Trunk-based
   - **기존 파일** (선택): 기존 CI/CD 설정, Dockerfile 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 파이프라인 설계 | pipeline-designer | 없음 | `_workspace/01_pipeline_design.md` |
| 2a | 인프라 구성 | infra-engineer | 작업 1 | `_workspace/02_pipeline_config/`, `02_infra_config.md` |
| 2b | 보안 스캔 설계 | security-scanner | 작업 1 | `_workspace/04_security_scan.md` |
| 3 | 모니터링 설계 | monitoring-specialist | 작업 1, 2a | `_workspace/03_monitoring.md` |
| 4 | 파이프라인 리뷰 | pipeline-reviewer | 작업 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(인프라)와 2b(보안)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- pipeline-designer 완료 → infra-engineer에게 스테이지 요구사항 전달, security-scanner에게 스캔 위치 전달, monitoring-specialist에게 배포 전략 전달
- infra-engineer 완료 → monitoring-specialist에게 로그/메트릭 포인트 전달, security-scanner에게 이미지/의존성 경로 전달
- security-scanner 완료 → monitoring-specialist에게 보안 알림 규칙 전달
- pipeline-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "CI/CD 파이프라인 만들어줘", "풀 설계" | **풀 파이프라인** | 5명 전원 |
| "CI만 설정해줘" | **CI 모드** | pipeline-designer + infra-engineer + pipeline-reviewer |
| "이 파이프라인에 보안 스캔 추가해줘" (기존 설정) | **보안 모드** | security-scanner + pipeline-reviewer |
| "파이프라인 모니터링 설계해줘" (기존 설정) | **모니터링 모드** | monitoring-specialist + pipeline-reviewer |
| "이 CI/CD 설정 리뷰해줘" | **리뷰 모드** | pipeline-reviewer 단독 |

**기존 파일 활용**: 사용자가 YAML, Dockerfile 등을 제공하면 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| CI/CD 도구 미정 | GitHub Actions를 기본으로 설계 |
| 배포 대상 미정 | Docker 컨테이너 기반 범용 설정 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 기존 YAML 파싱 실패 | 수동 분석 후 새 설정 파일 생성 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "Node.js Express 앱의 GitHub Actions CI/CD 파이프라인을 만들어줘. AWS ECS에 배포하고, Canary 배포 전략을 사용하고 싶어"
**기대 결과**:
- 설계: CI(lint→test→build→scan) + CD(staging→approval→canary→rollout)
- 인프라: GitHub Actions YAML, Dockerfile, ECR 설정, 시크릿 관리
- 보안: Semgrep + Trivy + Gitleaks 설정
- 모니터링: DORA 메트릭, 빌드/배포 알림, 대시보드
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 GitHub Actions 설정에 보안 스캔을 추가해줘" + YAML 파일
**기대 결과**:
- 기존 YAML을 `_workspace/02_pipeline_config/`로 복사
- 보안 모드: security-scanner + pipeline-reviewer 투입
- pipeline-designer, infra-engineer, monitoring-specialist 건너뜀

### 에러 흐름
**프롬프트**: "CI/CD 빨리 만들어줘, Python 프로젝트"
**기대 결과**:
- 배포 대상 미정 → Docker 기반으로 범용 설계
- GitHub Actions 기본 선택
- 리뷰 보고서에 "배포 대상 미지정, Docker 컨테이너 기반 범용 설정" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `pipeline-security-gates` | security-scanner | SAST/SCA/시크릿 탐지 도구 선택, 게이트 배치, 임계값 |
| `deployment-strategies` | pipeline-designer | Blue-Green/Canary/Rolling 배포, 롤백, DORA 메트릭 |
