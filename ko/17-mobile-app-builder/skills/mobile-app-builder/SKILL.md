---
name: mobile-app-builder
description: "모바일 앱 개발 풀 파이프라인. UI/UX 설계→네이티브/크로스플랫폼 코드 생성→API 연동→스토어 배포 준비까지 에이전트 팀이 협업하여 수행한다. '모바일 앱 만들어줘', '앱 개발해줘', 'iOS 앱', 'Android 앱', 'Flutter 앱', 'React Native 앱', '앱 UI 설계', '앱 스토어 배포', '앱 API 연동' 등 모바일 앱 개발 전반에 이 스킬을 사용한다. 기존 코드가 있는 경우에도 API 연동이나 스토어 배포를 지원한다. 단, 실제 빌드/컴파일(Xcode, Gradle), 실제 스토어 제출, CI/CD 파이프라인 구축은 이 스킬의 범위가 아니다."
---

# Mobile App Builder — 모바일 앱 개발 풀 파이프라인

모바일 앱의 UX 설계→코드 생성→API 연동→스토어 배포를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| ux-designer | `agents/ux-designer.md` | UX/UI 설계, 와이어프레임, 디자인 시스템 | general-purpose |
| app-developer | `agents/app-developer.md` | 네이티브/크로스플랫폼 앱 코드 생성 | general-purpose |
| api-integrator | `agents/api-integrator.md` | API 클라이언트, 인증, 캐싱 | general-purpose |
| store-manager | `agents/store-manager.md` | 스토어 메타데이터, ASO, 심사 대응 | general-purpose |
| qa-engineer | `agents/qa-engineer.md` | 품질 검증, 교차 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **앱 유형**: 어떤 앱인가 (SNS, 커머스, 유틸리티, 게임 등)
   - **플랫폼**: iOS / Android / 크로스플랫폼
   - **프레임워크 선호** (선택): Flutter, React Native, SwiftUI, Jetpack Compose
   - **백엔드 API** (선택): 기존 API 명세가 있는 경우
   - **기존 파일** (선택): 디자인, 코드, API 명세 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | UX/UI 설계 | ux-designer | 없음 | `_workspace/01_ux_design.md` |
| 2a | 앱 코드 생성 | app-developer | 작업 1 | `_workspace/02_app_code/`, `02_app_architecture.md` |
| 2b | 스토어 메타데이터 | store-manager | 작업 1 | `_workspace/04_store_listing.md` |
| 3 | API 연동 | api-integrator | 작업 1, 2a | `_workspace/03_api_integration.md` |
| 4 | QA 검증 | qa-engineer | 작업 2a, 2b, 3 | `_workspace/05_qa_report.md` |

작업 2a(앱 코드)와 2b(스토어 메타데이터)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- ux-designer 완료 → app-developer에게 화면 구조·디자인 토큰 전달, store-manager에게 스크린샷 시나리오 전달, api-integrator에게 데이터 필드 전달
- app-developer 완료 → api-integrator에게 Repository 인터페이스 전달, store-manager에게 권한 목록 전달
- api-integrator 완료 → app-developer에게 API 클라이언트 코드 전달
- qa-engineer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

QA 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. QA 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - UX 설계 — `01_ux_design.md`
   - 앱 아키텍처 — `02_app_architecture.md`
   - 앱 코드 — `02_app_code/`
   - API 연동 — `03_api_integration.md`
   - 스토어 배포 — `04_store_listing.md`
   - QA 보고서 — `05_qa_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "모바일 앱 만들어줘", "풀 개발" | **풀 파이프라인** | 5명 전원 |
| "앱 UI만 설계해줘" | **UX 모드** | ux-designer + qa-engineer |
| "이 설계로 코드 생성해줘" (기존 설계) | **코드 모드** | app-developer + api-integrator + qa-engineer |
| "앱 스토어 배포 준비해줘" (기존 앱) | **스토어 모드** | store-manager + qa-engineer |
| "이 앱 코드 검토해줘" | **리뷰 모드** | qa-engineer 단독 |

**기존 파일 활용**: 사용자가 설계서, 코드 등 기존 파일을 제공하면 해당 단계를 건너뛴다.

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
| 플랫폼 미지정 | UX 설계자가 크로스플랫폼(Flutter) 기본 선택, 양 플랫폼 가이드라인 반영 |
| 백엔드 API 없음 | API 연동자가 Mock API 설계, 향후 실제 API로 교체 가능한 구조 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, QA 보고서에 누락 명시 |
| QA에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 프레임워크 호환성 | 앱 개발자가 대안 프레임워크 제안, 장단점 비교 제공 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "할 일 관리 앱을 Flutter로 만들어줘. 할 일 추가/삭제/완료 체크, 카테고리 분류, 알림 기능이 필요해"
**기대 결과**:
- UX 설계: 5개 화면(목록/추가/상세/카테고리/설정), 네비게이션 구조, 디자인 시스템
- 앱 코드: Flutter + Riverpod + go_router, MVVM 구조, 화면별 위젯·뷰모델
- API 연동: RESTful CRUD 엔드포인트, 인증, 로컬 캐시
- 스토어: iOS + Android 메타데이터, ASO 키워드
- QA: 전 영역 교차 검증, 정합성 매트릭스

### 기존 파일 활용 흐름
**프롬프트**: "이 Figma 설계서로 iOS 앱 코드 생성해줘" + 설계 파일
**기대 결과**:
- 기존 설계를 `_workspace/01_ux_design.md`로 복사
- 코드 모드: app-developer + api-integrator + qa-engineer 투입
- ux-designer, store-manager 건너뜀

### 에러 흐름
**프롬프트**: "앱 하나 빨리 만들어줘, 뭐든 좋아"
**기대 결과**:
- 앱 유형 불분명 → UX 설계자가 트렌드 기반 앱 유형 3가지 제안 후 진행
- 풀 파이프라인 모드로 실행
- QA 보고서에 "사용자 요구사항 부재로 가정 기반 설계" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `mobile-ux-patterns` | ux-designer | iOS HIG/Material Design 3 비교, 네비게이션 패턴, 디자인 토큰 |
| `app-store-optimization` | store-manager | ASO 메타데이터 최적화, 키워드 전략, 심사 거절 대응 |
