---
name: infra-as-code
description: "Infrastructure as Code 설계 및 구현 풀 파이프라인. Terraform/Pulumi 기반 인프라 설계, 보안 정책, 비용 최적화, 드리프트 감지를 에이전트 팀이 협업하여 수행한다. 'IaC 설계해줘', 'Terraform 코드 작성해줘', '인프라 코드 만들어줘', 'Pulumi 프로젝트 설계', '클라우드 인프라 설계', '인프라 보안 설계', '인프라 비용 최적화', '드리프트 감지 설정' 등 IaC 전반에 이 스킬을 사용한다. 기존 인프라의 코드화(import)도 지원한다. 단, 실제 terraform apply 실행, 클라우드 콘솔 작업, 프로덕션 배포는 이 스킬의 범위가 아니다."
---

# Infra as Code — IaC 설계 파이프라인

Terraform/Pulumi 기반 인프라 설계→보안→비용최적화→드리프트감지를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| infra-architect | `agents/infra-architect.md` | 아키텍처, 모듈 구조, 환경 분리 | general-purpose |
| security-engineer | `agents/security-engineer.md` | IAM, 네트워크, 암호화, 컴플라이언스 | general-purpose |
| cost-optimizer | `agents/cost-optimizer.md` | 리소스 사이징, 예약, FinOps | general-purpose |
| drift-detector | `agents/drift-detector.md` | 상태 검증, 정책 준수, 자동 교정 | general-purpose |
| iac-reviewer | `agents/iac-reviewer.md` | 교차 검증, IaC 베스트 프랙티스 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **인프라 요구사항**: 어떤 서비스를 위한 인프라인가
    - **클라우드 프로바이더** (선택): AWS / GCP / Azure
    - **IaC 도구** (선택): Terraform / Pulumi / OpenTofu
    - **제약 조건** (선택): 예산, 컴플라이언스, 기존 인프라
    - **기존 코드** (선택): 기존 IaC 코드, 아키텍처 문서
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 인프라 설계 | architect | 없음 | `_workspace/01_infra_design.md` |
| 2a | 보안 설계 | security | 작업 1 | `_workspace/02_security_design.md` |
| 2b | 비용 분석 | cost | 작업 1 | `_workspace/03_cost_analysis.md` |
| 3 | 드리프트 정책 | drift | 작업 1, 2a | `_workspace/04_drift_policy.md` |
| 4 | 최종 리뷰 | reviewer | 작업 1~3 | `_workspace/05_review_report.md` |

작업 2a(보안)와 2b(비용)는 **병렬 실행** 가능하다.

**팀원 간 소통 흐름:**
- architect 완료 → security에게 네트워크·IAM·데이터 저장소 전달, cost에게 리소스 사양·스케일링 전달, drift에게 모듈 구조·핵심 리소스 전달
- security 완료 → drift에게 보안 정책·컴플라이언스 체크 전달, cost에게 보안 비용 항목 전달
- cost 완료 → drift에게 비용 이상 탐지 기준 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "인프라 코드 설계해줘", "풀 IaC" | **풀 파이프라인** | 5명 전원 |
| "인프라 아키텍처만 설계해줘" | **설계 모드** | architect + reviewer |
| "인프라 보안 검토해줘" | **보안 모드** | security + reviewer |
| "인프라 비용 분석해줘" | **비용 모드** | cost + reviewer |
| "드리프트 감지 설정해줘" | **드리프트 모드** | drift + reviewer |
| "기존 인프라를 코드화해줘" | **Import 모드** | architect + drift + reviewer |

**기존 파일 활용**: 사용자가 기존 IaC 코드, 아키텍처 문서 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 프로바이더 미정 | AWS를 기본으로 설계, 멀티클라우드 고려사항 병기 |
| 규모 추정 불가 | 소규모 시작 + Auto Scaling으로 탄력적 대응 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 기존 인프라 충돌 | terraform import 전략 포함, 점진적 전환 계획 수립 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "AWS에서 NestJS API 서버를 운영할 Terraform 인프라를 설계해줘. ECS Fargate + RDS PostgreSQL + ElastiCache Redis로 구성하고, dev/staging/prod 환경 분리해줘"
**기대 결과**:
- 설계: VPC/서브넷 설계, ECS/RDS/ElastiCache 구성, 3환경 모듈 구조
- 보안: 보안 그룹 매트릭스, IAM 역할, KMS 암호화, Checkov 정책
- 비용: 환경별 월간 비용 추정, Savings Plan 제안, 개발환경 스케줄링
- 드리프트: 보안 그룹/IAM 즉시 교정, 구성 드리프트 알림
- 리뷰: 전 항목 정합성 검증

### 기존 인프라 코드화 흐름
**프롬프트**: "현재 AWS 콘솔에서 수동으로 관리 중인 인프라를 Terraform으로 전환하고 싶어"
**기대 결과**:
- Import 모드: terraform import 전략 수립
- 리소스 목록화, import 명령어 생성, 상태 검증 계획
- 점진적 전환 로드맵 포함

### 에러 흐름
**프롬프트**: "간단한 웹서버 인프라 만들어줘" (상세 요구사항 없음)
**기대 결과**:
- 기본 구성(VPC + EC2/ECS + ALB + RDS)으로 설계 시작
- 추가 요구사항 질문 (규모, DB, 도메인 등)
- 최소 구성 + 확장 가이드 제공


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| terraform-module-patterns | `skills/terraform-module-patterns/SKILL.md` | infra-architect, drift-detector | 모듈 구조, 상태 관리, 환경 분리, 태깅 전략 |
| cloud-cost-models | `skills/cloud-cost-models/SKILL.md` | cost-optimizer | AWS/GCP 비용 모델, 사이징, Savings Plan, FinOps 성숙도 |
