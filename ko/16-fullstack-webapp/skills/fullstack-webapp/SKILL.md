---
name: fullstack-webapp
description: "풀스택 웹앱의 요구사항 분석, 설계, 프론트엔드, 백엔드, 테스트, 배포를 에이전트 팀이 협업하여 개발하는 풀 개발 파이프라인. '웹앱 만들어줘', '웹 서비스 개발', 'SaaS 개발', 'CRUD 앱', '대시보드 만들어줘', '관리자 페이지', '회원가입/로그인 기능', 'REST API 개발', '풀스택 프로젝트', 'Next.js 앱' 등 웹 애플리케이션 개발 전반에 이 스킬을 사용한다. 기존 코드가 있는 경우에도 기능 추가나 리팩토링을 지원한다. 단, 모바일 앱(React Native/Flutter), 데스크톱 앱(Electron), 게임 개발, ML/AI 모델 학습은 이 스킬의 범위가 아니다."
---

# Fullstack Web App — 풀스택 웹앱 개발 파이프라인

웹앱의 요구사항→설계→프론트엔드→백엔드→테스트→배포를 에이전트 팀이 협업하여 개발한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| architect | `agents/architect.md` | 요구사항, 아키텍처, DB, API 설계 | general-purpose |
| frontend-dev | `agents/frontend-dev.md` | React/Next.js 프론트엔드 구현 | general-purpose |
| backend-dev | `agents/backend-dev.md` | API, DB, 인증, 비즈니스 로직 | general-purpose |
| qa-engineer | `agents/qa-engineer.md` | 테스트 전략, 테스트 코드, 코드 리뷰 | general-purpose |
| devops-engineer | `agents/devops-engineer.md` | CI/CD, 인프라, 배포, 모니터링 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **앱 설명**: 만들려는 웹앱의 목적과 핵심 기능
   - **기술 스택** (선택): 선호하는 프레임워크/라이브러리
   - **규모** (선택): MVP/소규모/중규모/대규모
   - **기존 코드** (선택): 확장할 기존 프로젝트
   - **배포 플랫폼** (선택): Vercel/AWS/Docker 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 코드가 있으면 분석하고 해당 단계를 조정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 아키텍처 설계 | architect | 없음 | `01_architecture.md`, `02_api_spec.md`, `03_db_schema.md` |
| 2a | 프론트엔드 개발 | frontend | 작업 1 | `src/` 프론트엔드 코드 |
| 2b | 백엔드 개발 | backend | 작업 1 | `src/` 백엔드 코드 |
| 2c | 배포 설정 | devops | 작업 1 | `05_deploy_guide.md`, CI/CD 설정 |
| 3 | 테스트 & 리뷰 | qa | 작업 2a, 2b | `04_test_plan.md`, `06_review_report.md`, 테스트 코드 |

작업 2a(프론트), 2b(백엔드), 2c(DevOps)는 **병렬 실행**한다. 모두 작업 1(설계)에만 의존한다.

**팀원 간 소통 흐름:**
- architect 완료 → frontend에게 컴포넌트 구조·라우팅 전달, backend에게 API·DB·인증 전달, devops에게 인프라 요구사항 전달, qa에게 기능 요구사항 전달
- frontend ↔ backend: API 연동 중 실시간 소통 (엔드포인트 변경, 에러 형식 등)
- devops 완료 → 전체에게 환경변수, 배포 URL 공유
- qa는 모든 코드를 리뷰하고 테스트. 🔴 필수 수정 발견 시 해당 개발자에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

QA의 리뷰를 기반으로 최종 산출물을 정리한다:

1. 모든 코드와 문서를 확인한다
2. 리뷰의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 아키텍처 설계 — `_workspace/01_architecture.md`
   - API 명세 — `_workspace/02_api_spec.md`
   - DB 스키마 — `_workspace/03_db_schema.md`
   - 테스트 계획 — `_workspace/04_test_plan.md`
   - 배포 가이드 — `_workspace/05_deploy_guide.md`
   - 리뷰 보고서 — `_workspace/06_review_report.md`
   - 소스 코드 — `src/` 디렉토리

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "웹앱 만들어줘", "풀스택 개발" | **풀 파이프라인** | 5명 전원 |
| "API만 만들어줘" | **백엔드 모드** | architect + backend + qa |
| "프론트엔드만 만들어줘" (API 있음) | **프론트 모드** | architect + frontend + qa |
| "이 코드 리팩토링해줘" | **리팩토링 모드** | architect + 해당 개발자 + qa |
| "배포 설정만 해줘" | **DevOps 모드** | devops 단독 |

**기존 코드 활용**: 사용자가 기존 코드를 제공하면, 아키텍트가 코드를 분석하여 확장 지점을 파악하고 필요한 에이전트만 투입한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` + `src/` | 설계 문서 + 소스 코드 |
| 메시지 기반 | SendMessage | API 연동 이슈, 코드 리뷰, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 요구사항 모호 | 가장 일반적인 CRUD 패턴 적용, 가정 사항 문서화 |
| 기술 스택 미지정 | 규모별 기본 스택 적용 (MVP: Next.js + SQLite) |
| 빌드 에러 | 에러 로그 분석 → 해당 개발자가 수정 → QA 재검증 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 명시 |
| 리뷰에서 🔴 발견 | 해당 개발자에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "할 일 관리 웹앱을 만들어줘. 회원가입/로그인, 할 일 CRUD, 카테고리 분류 기능"
**기대 결과**:
- 아키텍처: Next.js + Prisma + SQLite, ERD(users, todos, categories), API 명세 10개 이상
- 프론트: 로그인/회원가입 페이지, 대시보드, 할 일 CRUD UI, 반응형
- 백엔드: 인증 API, CRUD API, 입력 검증, 에러 처리
- 테스트: 인증+CRUD 테스트 시나리오, 커버리지 80% 목표
- 배포: Vercel 배포 가이드, GitHub Actions CI/CD

### 기존 파일 활용 흐름
**프롬프트**: "이 Next.js 프로젝트에 결제 기능을 추가해줘" + 기존 코드
**기대 결과**:
- architect가 기존 코드 분석, 결제 관련 API/DB 설계
- backend가 결제 API 추가, frontend가 결제 UI 추가
- qa가 결제 플로우 테스트

### 에러 흐름
**프롬프트**: "간단한 웹앱 만들어줘"
**기대 결과**:
- 요구사항 모호 → architect가 기본 CRUD 앱(메모/노트) 제안
- MVP 규모 기본 스택(Next.js + SQLite) 적용
- 리뷰 보고서에 "요구사항 가정 적용" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `component-patterns` | frontend-dev | React/Next.js 컴포넌트 패턴, 상태관리 전략, 폴더 구조 |
| `api-security-checklist` | backend-dev | OWASP Top 10, 인증/인가 패턴, 보안 헤더, Rate Limiting |
