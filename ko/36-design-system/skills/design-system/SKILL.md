---
name: design-system
description: "UI 디자인 시스템을 체계적으로 구축하는 풀 파이프라인. 디자인 토큰 설계, React/Vue 컴포넌트 라이브러리, 스토리북, 접근성(WCAG) 검증, 문서화를 에이전트 팀이 협업하여 생성한다. '디자인 시스템 만들어줘', '컴포넌트 라이브러리', 'UI 키트', '디자인 토큰', '스토리북 구축', '접근성 검증', 'WCAG 검증', 'UI 컴포넌트', '버튼 컴포넌트 만들어줘' 등 디자인 시스템 구축 전반에 이 스킬을 사용한다. 단, Figma 플러그인 개발, 디자인 시스템 SaaS 구축, 네이티브 앱 컴포넌트(SwiftUI/Jetpack Compose)는 이 스킬의 범위가 아니다."
---

# Design System — UI 디자인 시스템 풀 파이프라인

디자인토큰→컴포넌트→스토리북→접근성→문서를 에이전트 팀이 협업하여 구축한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| token-designer | `agents/token-designer.md` | 디자인 토큰 설계 | general-purpose |
| component-developer | `agents/component-developer.md` | 컴포넌트 개발 | general-purpose |
| a11y-auditor | `agents/a11y-auditor.md` | 접근성 검증 | general-purpose |
| storybook-builder | `agents/storybook-builder.md` | 스토리북 구축 | general-purpose |
| doc-writer | `agents/doc-writer.md` | 문서 작성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **브랜드 정보**: 브랜드 색상, 로고, 톤앤매너
    - **프레임워크**: React/Vue/Angular/Web Components
    - **컴포넌트 범위**: 필요한 컴포넌트 목록 (또는 "전체")
    - **접근성 수준**: WCAG AA(기본) / AAA
    - **기존 시스템** (선택): 마이그레이션 대상 기존 디자인 시스템
2. `_workspace/` 디렉토리와 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 토큰 설계 | token-designer | 없음 | `01_design_tokens/` |
| 2 | 컴포넌트 개발 | component-developer | 작업 1 | `02_components/` |
| 3a | 스토리북 구축 | storybook-builder | 작업 1, 2 | `03_storybook/` |
| 3b | 접근성 검증 | a11y-auditor | 작업 1, 2 | `04_a11y_report.md` |
| 4 | 문서 작성 | doc-writer | 작업 1, 2, 3a, 3b | `05_docs/` |

작업 3a(스토리북)와 3b(접근성)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- token-designer 완료 → component-developer에게 토큰 임포트 방법 전달, a11y-auditor에게 대비비 검증 전달
- component-developer 완료 → storybook-builder에게 props 타입 전달, a11y-auditor에게 ARIA 현황 전달
- a11y-auditor → P0/P1 이슈 발견 시 component-developer에게 수정 요청 (최대 2회)
- storybook-builder 완료 → doc-writer에게 스토리북 구조 전달
- a11y-auditor 완료 → doc-writer에게 접근성 가이드 전달
- doc-writer는 모든 산출물의 정합성을 최종 검증

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 접근성 P0 이슈가 모두 해결되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 토큰 시스템 — `01_design_tokens/`
    - 컴포넌트 — `02_components/`
    - 스토리북 — `03_storybook/`
    - 접근성 보고서 — `04_a11y_report.md`
    - 문서 — `05_docs/`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "디자인 시스템 전체 구축" | **풀 파이프라인** | 5명 전원 |
| "토큰만 설계해줘" | **토큰 모드** | token-designer 단독 |
| "이 토큰으로 컴포넌트 만들어줘" | **컴포넌트 모드** | component-developer + storybook-builder |
| "접근성 검증만 해줘" | **검증 모드** | a11y-auditor 단독 |
| "스토리북만 추가해줘" | **스토리북 모드** | storybook-builder 단독 |
| "문서만 작성해줘" | **문서 모드** | doc-writer 단독 |
| "Button 컴포넌트만 추가" | **단일 컴포넌트** | component-developer + a11y-auditor + storybook-builder |

**기존 시스템 활용**: 기존 토큰이 있으면 token-designer를 건너뛴다. 기존 컴포넌트에 스토리북만 추가하는 경우 storybook-builder만 투입한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 코드, 설정, 문서 |
| 메시지 기반 | SendMessage | 핵심 정보, 수정 요청, 검증 결과 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 브랜드 색상 미제공 | 중립 팔레트(slate)로 시작, 사용자에게 색상 요청 |
| 프레임워크 미지정 | React + TypeScript 기본, 사용자 확인 후 변경 |
| 대비비 미충족 | 자동 조정 후 원본/조정값 함께 보고 |
| 접근성 P0 미해결 | 릴리스 차단, component-developer에 재수정 요청 |
| 에이전트 실패 | 1회 재시도 후 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "파란색 브랜드 색상의 React 디자인 시스템을 만들어줘. Button, Input, Card, Modal이 필요해"
**기대 결과**:
- 토큰: 파란색 기반 color scale, 시맨틱 색상, 타이포, 간격, 다크모드
- 컴포넌트: Button(4 variant, 3 size), Input(text/password/search), Card, Modal + 공유 훅
- 스토리북: 토큰 시각화, 컴포넌트별 Default/AllVariants/Playground 스토리
- 접근성: WCAG AA 준수 검증, 키보드 테스트, 대비비 매트릭스
- 문서: 설계 원칙, 시작 가이드, 컴포넌트별 Do/Don't, 기여 가이드

### 기존 파일 활용 흐름
**프롬프트**: "기존 디자인 시스템에 DatePicker 컴포넌트를 추가해줘"
**기대 결과**:
- component-developer가 기존 토큰 기반 DatePicker 구현
- a11y-auditor가 날짜 선택 접근성 (키보드, 스크린리더) 검증
- storybook-builder가 DatePicker 스토리 추가
- token-designer, doc-writer는 최소 투입

### 에러 흐름
**프롬프트**: "디자인 시스템 만들어줘" (색상, 프레임워크 미지정)
**기대 결과**:
- token-designer가 중립 팔레트로 시작하되 사용자에게 브랜드 색상 확인 요청
- component-developer가 React + TypeScript 기본 채택
- a11y-auditor가 기본 팔레트의 대비비 검증
- doc-writer가 커스터마이징 가이드(색상 변경 방법) 강조

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| wcag-checker | `skills/wcag-checker/SKILL.md` | a11y-auditor, component-developer | WCAG 2.1 접근성 검증 체크리스트, 대비비 계산, ARIA 패턴, 키보드 매트릭스 |
| token-generator | `skills/token-generator/SKILL.md` | token-designer, component-developer | 디자인 토큰 3-tier 구조, 색상 스케일 알고리즘, 타이포/간격/모션 체계 |
