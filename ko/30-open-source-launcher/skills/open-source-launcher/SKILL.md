---
name: open-source-launcher
description: "오픈소스 프로젝트 런칭 준비를 코드 정리, 문서 작성, 라이선스 선정, 커뮤니티 구축까지 에이전트 팀이 협업하여 수행하는 풀 런칭 파이프라인. '오픈소스 공개 준비해줘', '프로젝트 오픈소스화', 'GitHub 공개 준비', '오픈소스 라이선스 선정', 'README 작성', 'CONTRIBUTING 가이드 만들어줘', '오픈소스 커뮤니티 설계', '릴리스 준비', 'CI/CD 구성해줘', '코드 공개 전 점검' 등 오픈소스 런칭 전반에 이 스킬을 사용한다. README만 필요하거나 라이선스 검토만 필요한 경우에도 지원한다. 단, 실제 저장소 생성, GitHub 설정 API 호출, 패키지 레지스트리 배포 실행은 이 스킬의 범위가 아니다."
---

# Open Source Launcher — 오픈소스 프로젝트 런칭 파이프라인

오픈소스 프로젝트의 코드정리→문서→라이선스→커뮤니티를 에이전트 팀이 협업하여 한 번에 준비한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| code-organizer | `agents/code-organizer.md` | 구조재편, 리팩토링, 코드표준 | general-purpose |
| doc-writer | `agents/doc-writer.md` | README, 기여가이드, API문서 | general-purpose |
| license-specialist | `agents/license-specialist.md` | 라이선스선정, 호환성, 법적검토 | general-purpose |
| community-manager | `agents/community-manager.md` | 거버넌스, CoC, 이슈템플릿, CI/CD | general-purpose |
| launch-reviewer | `agents/launch-reviewer.md` | 교차검증, 런칭준비도, 최종체크리스트 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **프로젝트 코드**: 오픈소스화할 코드 또는 저장소
    - **프로젝트 목표**: 라이브러리/프레임워크/도구/애플리케이션
    - **대상 사용자**: 누가 이 프로젝트를 사용할 것인가
    - **라이선스 선호** (선택): 상용 허용 여부, 카피레프트 선호 등
    - **기존 문서** (선택): 이미 작성된 README, 문서
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 코드 정리 | code-organizer | 없음 | `_workspace/01_code_organization.md` |
| 2a | 문서 작성 | doc-writer | 작업 1 | `_workspace/02_documentation.md` |
| 2b | 라이선스 검토 | license-specialist | 작업 1 | `_workspace/03_license_review.md` |
| 3 | 커뮤니티 구성 | community-manager | 작업 1, 2a, 2b | `_workspace/04_community_setup.md` |
| 4 | 런칭 리뷰 | launch-reviewer | 작업 1~3 | `_workspace/05_launch_report.md` |

작업 2a(문서)와 2b(라이선스)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- organizer 완료 → doc-writer에게 프로젝트 구조·API 전달, license에게 의존성 목록 전달, community에게 빌드/테스트 절차 전달
- doc-writer 완료 → community에게 CONTRIBUTING과 이슈 템플릿 일관성 확인 요청
- license 완료 → doc-writer에게 라이선스 섹션 내용 전달, community에게 CLA/DCO 전달
- community 완료 → reviewer에게 전체 설정 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 및 `_workspace/generated_files/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 코드 정리 — `01_code_organization.md`
    - 문서 패키지 — `02_documentation.md`
    - 라이선스 — `03_license_review.md`
    - 커뮤니티 — `04_community_setup.md`
    - 런칭 보고서 — `05_launch_report.md`
    - 생성 파일 — `generated_files/` (README, LICENSE, CONTRIBUTING, CI 등)

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "오픈소스 런칭 전체 준비해줘" | **풀 런칭** | 5명 전원 |
| "README 작성해줘" | **문서 모드** | doc-writer + reviewer |
| "라이선스 검토해줘" | **라이선스 모드** | license-specialist + reviewer |
| "CI/CD 구성해줘" | **CI 모드** | community-manager + reviewer |
| "오픈소스 공개 전 점검해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 생성 파일 | `_workspace/generated_files/` | 프로젝트에 실제 배치할 파일 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 코드 미제공 | 일반 오픈소스 프로젝트 템플릿과 체크리스트 제공 |
| 프로젝트 언어 불명 | 범용 설정(EditorConfig, gitignore)으로 진행, 언어별 옵션 병기 |
| 라이선스 충돌 | 대체 패키지 또는 라이선스 변경 옵션을 제시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 Python CLI 도구를 오픈소스로 공개하려고 해. MIT 라이선스로, PyPI에 배포하고 싶어."
**기대 결과**:
- 코드정리: pyproject.toml 구성, 구조 표준화, 시크릿 스캔, .gitignore
- 문서: README(배지+Quick Start+API), CONTRIBUTING, CHANGELOG
- 라이선스: MIT 선정, 의존성 호환성 확인, LICENSE 파일 생성
- 커뮤니티: GitHub Actions CI, PyPI 배포 워크플로우, 이슈/PR 템플릿
- 리뷰: 전항목 정합성 매트릭스, 런칭 최종 체크리스트

### 기존 파일 활용 흐름
**프롬프트**: "README는 이미 있는데, 라이선스 검토하고 CI 구성해줘" + README 첨부
**기대 결과**:
- 기존 README를 `_workspace/generated_files/README.md`로 복사
- 라이선스 모드 + CI 모드 병합: license + community + reviewer 투입

### 에러 흐름
**프롬프트**: "오픈소스 준비해줘, 코드는 아직 정리 안 됐어"
**기대 결과**:
- 코드 부재 시 일반 오픈소스 체크리스트와 템플릿 세트를 제공
- "코드 제공 후 상세 분석 가능" 명시
- 범용 프로젝트 구조 + 문서 템플릿 + 라이선스 비교표 선제공


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| license-compatibility-matrix | `skills/license-compatibility-matrix/SKILL.md` | license-specialist | 라이선스 호환성 매트릭스, SPDX, 듀얼 라이선스, 충돌 해결 |
| community-health-metrics | `skills/community-health-metrics/SKILL.md` | community-manager, doc-writer | CHAOSS 지표, GitHub 설정, 이슈/PR 템플릿, 기여자 온보딩 |
