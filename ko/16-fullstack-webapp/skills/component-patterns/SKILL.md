---
name: component-patterns
description: "React/Next.js 컴포넌트 설계 패턴 라이브러리. Compound/Render Props/HOC/Custom Hooks 패턴, 상태관리 전략(Zustand/React Query/Context), 폴더 구조 컨벤션을 제공하는 frontend-dev 확장 스킬. '컴포넌트 패턴', 'React 패턴', '상태관리', '폴더 구조', 'Custom Hook', '컴포넌트 분리' 등 프론트엔드 아키텍처 설계 시 사용한다. 단, 실제 코드 구현이나 백엔드 로직은 이 스킬의 범위가 아니다."
---

# Component Patterns — React/Next.js 컴포넌트 설계 패턴

frontend-dev 에이전트가 프론트엔드 개발 시 활용하는 컴포넌트 패턴, 상태관리 전략, 프로젝트 구조 레퍼런스.

## 대상 에이전트

`frontend-dev` — 이 스킬의 패턴을 컴포넌트 설계와 상태관리에 직접 적용한다.

## 컴포넌트 설계 패턴

### 1. Compound Components
부모-자식이 암묵적 상태를 공유하는 패턴.

**적합**: Tab, Accordion, Dropdown, Select 등 복합 UI
**구조**: `<Select>` + `<Select.Trigger>` + `<Select.Option>`
**핵심**: Context로 상태 공유, children으로 유연한 구성

### 2. Render Props / Children as Function
렌더링 로직을 외부에 위임.

**적합**: 데이터 fetching 래퍼, 마우스/스크롤 추적
**구조**: `<DataLoader render={(data) => <UI data={data} />} />`
**주의**: Hook 패턴으로 대체 가능한 경우 Hook 우선

### 3. Custom Hooks (추출 패턴)
상태 로직을 재사용 가능한 Hook으로 추출.

**적합**: 폼 관리, API 호출, 로컬스토리지, 디바운스
**네이밍**: `use` 프리픽스 필수 — `useForm`, `useDebounce`, `useAuth`

### 4. Container/Presentational 분리
데이터 로직(Container)과 UI 표현(Presentational) 분리.

**적합**: 대규모 앱, 테스트 용이성 필요 시
**Container**: 데이터 fetch, 상태 관리, 이벤트 핸들러
**Presentational**: props만 받아 렌더링, 순수 함수적

### 5. Higher-Order Component (HOC)
컴포넌트를 감싸 기능을 추가.

**적합**: 인증 가드, 레이아웃 래퍼, 에러 바운더리
**네이밍**: `with` 프리픽스 — `withAuth`, `withLayout`
**주의**: Hook/Context로 대체 가능하면 그것 우선

### 6. Headless Component
UI 없이 동작/상태만 제공.

**적합**: 디자인 시스템에 구애받지 않는 로직 공유
**예시**: headless `useCombobox`, `useDialog`, `useTable`

## 상태관리 전략 선택 가이드

| 상태 유형 | 추천 도구 | 근거 |
|----------|----------|------|
| **UI 로컬 상태** | useState, useReducer | 컴포넌트 내부 |
| **서버 상태** | React Query (TanStack Query) | 캐싱, 리페치, 낙관적 업데이트 |
| **전역 클라이언트 상태** | Zustand | 간결, 보일러플레이트 최소 |
| **복잡한 전역 상태** | Zustand + Immer | 불변성 편의 |
| **URL 상태** | nuqs / useSearchParams | 필터, 페이지네이션 |
| **폼 상태** | React Hook Form + Zod | 유효성 검증 통합 |
| **테마/언어** | Context + Provider | 변경 빈도 낮음 |

### 상태 배치 결정 흐름
```
이 상태를 URL에서 복원해야 하는가? → URL 상태
서버 데이터인가? → React Query
여러 컴포넌트가 공유하는가? → Zustand
한 컴포넌트 내부인가? → useState
복잡한 전환 로직인가? → useReducer
```

## Next.js App Router 폴더 구조

### 권장 구조 (Feature-Based)
```
src/
├── app/                    # Next.js App Router
│   ├── (auth)/             # 인증 관련 라우트 그룹
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   ├── (main)/             # 메인 라우트 그룹
│   │   ├── dashboard/page.tsx
│   │   └── settings/page.tsx
│   ├── api/                # API Routes
│   │   └── [...]/route.ts
│   ├── layout.tsx          # 루트 레이아웃
│   └── page.tsx            # 홈
├── components/
│   ├── ui/                 # 범용 UI (Button, Input, Modal)
│   └── features/           # 기능별 컴포넌트
│       ├── auth/
│       └── dashboard/
├── hooks/                  # Custom Hooks
├── lib/                    # 유틸, 설정
│   ├── api.ts              # API 클라이언트
│   ├── auth.ts             # 인증 유틸
│   └── utils.ts
├── stores/                 # Zustand 스토어
├── types/                  # TypeScript 타입
└── styles/                 # 전역 스타일
```

## 컴포넌트 파일 컨벤션

| 항목 | 규칙 |
|------|------|
| 파일명 | PascalCase: `UserProfile.tsx` |
| 디렉토리 | kebab-case: `user-profile/` |
| 인덱스 | `index.ts`로 re-export |
| 테스트 | `UserProfile.test.tsx` 동일 디렉토리 |
| 스토리 | `UserProfile.stories.tsx` 동일 디렉토리 |
| 타입 | 같은 파일 또는 `types.ts` 분리 |

## 성능 최적화 패턴

| 패턴 | 언제 | 도구 |
|------|------|------|
| **메모이제이션** | 비싼 계산, 잦은 리렌더 | `useMemo`, `React.memo` |
| **지연 로딩** | 초기 번들 크기 | `React.lazy`, `next/dynamic` |
| **가상화** | 1000+ 아이템 리스트 | `@tanstack/react-virtual` |
| **이미지 최적화** | 이미지 로딩 | `next/image` |
| **코드 스플리팅** | 라우트별 분리 | App Router 자동 |
| **낙관적 업데이트** | 즉각 피드백 | React Query `onMutate` |
| **Debounce** | 검색, 입력 | `useDeferredValue` 또는 custom hook |

## 에러 처리 패턴

### 계층적 에러 바운더리
```
RootErrorBoundary (전역)
  └── LayoutErrorBoundary (섹션별)
      └── ComponentErrorFallback (개별)
```

### API 에러 처리
| HTTP 상태 | 클라이언트 처리 |
|----------|---------------|
| 401 | 자동 로그아웃 + 리다이렉트 |
| 403 | 권한 없음 UI |
| 404 | Not Found 페이지 |
| 422 | 폼 필드별 에러 표시 |
| 429 | 재시도 + 대기 안내 |
| 500 | 일반 에러 UI + 재시도 버튼 |

## 접근성 (a11y) 체크리스트

- [ ] 모든 이미지에 alt 텍스트
- [ ] 키보드 네비게이션 (Tab, Enter, Escape)
- [ ] ARIA 라벨 (aria-label, role)
- [ ] 색상 대비 4.5:1 이상
- [ ] 포커스 표시자 visible
- [ ] 스크린 리더 테스트
- [ ] 시맨틱 HTML (button, nav, main, section)
