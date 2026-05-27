---
name: token-generator
description: "디자인 토큰을 체계적으로 생성하는 방법론과 도구. '디자인 토큰 만들어줘', '토큰 체계 설계', '색상 스케일 생성', '타이포 스케일', '간격 체계', '다크모드 토큰' 등 디자인 토큰 설계 시 사용한다. 단, Figma 토큰 플러그인 실행, Style Dictionary 런타임 빌드는 이 스킬의 범위가 아니다."
---

# Token Generator — 디자인 토큰 생성 방법론

token-designer 에이전트의 토큰 설계 역량을 강화하는 도메인 지식 스킬.

## 대상 에이전트

- **token-designer** — 색상, 타이포, 간격 등 토큰 체계를 설계할 때 이 방법론을 사용한다
- **component-developer** — 컴포넌트에서 토큰을 참조할 때 네이밍 규칙을 확인한다

## 토큰 계층 구조 (3-tier)

```
Global (Primitive) → Alias (Semantic) → Component
────────────────────────────────────────────────
blue-500: #3B82F6   primary: blue-500    button-bg: primary
gray-100: #F3F4F6   surface: gray-100    card-bg: surface
```

### Tier 1: Primitive — `{category}-{scale}` (예: `blue-500`)
### Tier 2: Semantic — `{용도}` (예: `primary`, `surface`)
### Tier 3: Component — `{component}-{property}-{variant}-{state}`

## 색상 스케일 생성 알고리즘

입력: 브랜드 색상 1개 → HSL 변환 후 10단계 스케일 생성:

| 단계 | L 조정 | S 조정 | 용도 |
|------|--------|--------|------|
| 50   | 95-97% | S×0.3  | 배경 틴트 |
| 100  | 90-93% | S×0.5  | 호버 배경 |
| 200  | 82-87% | S×0.7  | 보조 배경 |
| 300  | 70-76% | S×0.85 | 테두리 |
| 400  | 58-64% | S×0.95 | 보조 텍스트 |
| 500  | 45-55% | S×1.0  | 기본 (입력값) |
| 600  | 38-44% | S×1.0  | 호버 |
| 700  | 30-36% | S×0.95 | 액티브 |
| 800  | 22-28% | S×0.9  | 강조 텍스트 |
| 900  | 14-20% | S×0.85 | 최고 강조 |
| 950  | 8-12%  | S×0.8  | 거의 검정 |

## 시맨틱 색상 매핑 표준

| 시맨틱 토큰 | 라이트 모드 | 다크 모드 | 용도 |
|------------|-----------|----------|------|
| `primary` | blue-500 | blue-400 | 주 액션 |
| `on-primary` | white | white | 주 액션 위 텍스트 |
| `surface` | white | gray-900 | 기본 배경 |
| `surface-raised` | white | gray-800 | 카드/모달 |
| `on-surface` | gray-900 | gray-50 | 기본 텍스트 |
| `on-surface-muted` | gray-500 | gray-400 | 보조 텍스트 |
| `border` | gray-200 | gray-700 | 기본 테두리 |
| `success` | green-500 | green-400 | 성공 |
| `warning` | amber-500 | amber-400 | 경고 |
| `error` | red-500 | red-400 | 오류 |

## 타이포그래피 스케일 (Major Third 1.250)

```
base = 16px (1rem), ratio = 1.250

| 토큰 | px | rem | 용도 |
|------|----|-----|------|
| text-xs | 10.24 | 0.64 | 캡션 |
| text-sm | 12.80 | 0.80 | 보조 텍스트 |
| text-base | 16.00 | 1.00 | 본문 |
| text-lg | 20.00 | 1.25 | 강조 본문 |
| text-xl | 25.00 | 1.563 | 소제목 |
| text-2xl | 31.25 | 1.953 | 제목 |
| text-3xl | 39.06 | 2.441 | 대제목 |
| text-4xl | 48.83 | 3.052 | 히어로 |

줄높이: heading 1.2~1.3, body 1.5~1.7, compact 1.25~1.4
가중치: light(300), regular(400), medium(500), semibold(600), bold(700)
```

## 간격 체계 (4px 기반)

| 토큰 | 값 | rem | 용도 |
|------|----|-----|------|
| space-1 | 4px | 0.25 | 최소 간격 |
| space-2 | 8px | 0.5 | 인라인 간격 |
| space-3 | 12px | 0.75 | 컴팩트 패딩 |
| space-4 | 16px | 1.0 | 기본 패딩 |
| space-6 | 24px | 1.5 | 섹션 간격 |
| space-8 | 32px | 2.0 | 큰 간격 |
| space-12 | 48px | 3.0 | 레이아웃 간격 |
| space-16 | 64px | 4.0 | 대형 레이아웃 |

## 그림자 체계

| 토큰 | 값 | 용도 |
|------|----|------|
| shadow-sm | 0 1px 3px rgba(0,0,0,0.1) | 카드 |
| shadow-md | 0 4px 6px rgba(0,0,0,0.1) | 드롭다운 |
| shadow-lg | 0 10px 15px rgba(0,0,0,0.1) | 모달 |
| shadow-xl | 0 20px 25px rgba(0,0,0,0.1) | 팝오버 |

## 모션 토큰

| 토큰 | 값 | 용도 |
|------|----|------|
| duration-fast | 150ms | 호버, 토글 |
| duration-normal | 250ms | 전환 |
| duration-slow | 400ms | 복잡한 애니메이션 |
| easing-default | cubic-bezier(0.4, 0, 0.2, 1) | 기본 |

## 출력 포맷

### CSS Custom Properties
```css
:root { --color-primary: #3B82F6; --space-4: 1rem; }
[data-theme="dark"] { --color-primary: #60A5FA; }
```

### TypeScript
```typescript
export const tokens = {
  color: { primary: '#3B82F6' },
  space: { 4: '1rem' },
} as const;
```

### JSON (Style Dictionary)
```json
{ "color": { "primary": { "value": "#3B82F6", "type": "color" } } }
```
