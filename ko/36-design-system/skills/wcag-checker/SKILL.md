---
name: wcag-checker
description: "WCAG 2.1/2.2 접근성 검증 체크리스트와 자동 감사 방법론을 제공하는 스킬. '접근성 검증해줘', 'WCAG 체크', '대비비 확인', 'ARIA 검사', '키보드 접근성', '스크린리더 테스트' 등 접근성 검증이 필요할 때 사용한다. 단, 실제 보조기기(JAWS/NVDA) 실행, 법적 소송 자문, 접근성 인증 발급은 이 스킬의 범위가 아니다."
---

# WCAG Checker — 접근성 검증 체크리스트 + 도구

a11y-auditor 에이전트의 접근성 검증 역량을 강화하는 도메인 지식 스킬.

## 대상 에이전트

- **a11y-auditor** — 이 스킬의 체크리스트와 공식을 사용하여 컴포넌트별 접근성을 검증한다
- **component-developer** — 개발 시 접근성 요구사항을 사전 확인한다

## WCAG 2.1 AA 필수 기준 체크리스트

### 1. 인식 가능 (Perceivable)

| 기준 | 항목 | 검증 방법 | 심각도 |
|------|------|----------|--------|
| 1.1.1 | 비텍스트 콘텐츠에 대체 텍스트 | `img`에 `alt`, 장식 이미지에 `alt=""` | P0 |
| 1.3.1 | 정보와 관계 프로그래밍 방식 전달 | 시맨틱 HTML, ARIA role | P0 |
| 1.3.2 | 의미 있는 순서 | DOM 순서 = 시각적 순서 | P1 |
| 1.4.1 | 색상만으로 정보 전달 금지 | 아이콘/텍스트 보조 표시 | P0 |
| 1.4.3 | 대비비 최소 4.5:1 (일반), 3:1 (대형) | 대비비 공식 계산 | P0 |
| 1.4.4 | 200% 확대 시 콘텐츠 손실 없음 | `rem`/`em` 단위 사용 | P1 |
| 1.4.11 | 비텍스트 UI 대비비 3:1 이상 | 포커스 링, 테두리, 아이콘 | P0 |

### 2. 운용 가능 (Operable)

| 기준 | 항목 | 검증 방법 | 심각도 |
|------|------|----------|--------|
| 2.1.1 | 키보드 접근 가능 | Tab/Enter/Space/Esc/Arrow 동작 | P0 |
| 2.1.2 | 키보드 트랩 없음 | 모든 요소에서 Tab out 가능 | P0 |
| 2.4.3 | 포커스 순서 논리적 | `tabindex` 양수 금지 | P0 |
| 2.4.7 | 포커스 시각적 표시 | `:focus-visible` 스타일 | P0 |

### 3. 이해 가능 (Understandable)

| 기준 | 항목 | 검증 방법 | 심각도 |
|------|------|----------|--------|
| 3.1.1 | 페이지 언어 명시 | `<html lang="ko">` | P0 |
| 3.2.1 | 포커스 시 컨텍스트 변경 없음 | focus만으로 페이지 이동 금지 | P0 |
| 3.3.1 | 오류 식별 텍스트 제공 | 색상 외 텍스트 에러 메시지 | P0 |
| 3.3.2 | 레이블 또는 지시문 | `<label>` 연결, placeholder만 사용 금지 | P0 |

### 4. 견고 (Robust)

| 기준 | 항목 | 검증 방법 | 심각도 |
|------|------|----------|--------|
| 4.1.2 | 이름, 역할, 값 프로그래밍 방식 | ARIA 속성 정확성 | P0 |
| 4.1.3 | 상태 메시지 보조기술 전달 | `aria-live`, `role="status"` | P1 |

## 대비비 계산 공식

### 상대 휘도 (Relative Luminance)

```
L = 0.2126 * R_lin + 0.7152 * G_lin + 0.0722 * B_lin

여기서:
- sRGB를 0~1로 정규화 (예: #FF → 1.0)
- C_lin = C_srgb <= 0.04045 ? C_srgb/12.92 : ((C_srgb+0.055)/1.055)^2.4
```

### 대비비 공식

```
CR = (L_lighter + 0.05) / (L_darker + 0.05)

AA 기준:
- 일반 텍스트 (< 18pt 또는 < 14pt bold): CR >= 4.5
- 대형 텍스트 (>= 18pt 또는 >= 14pt bold): CR >= 3.0
- UI 컴포넌트/그래픽: CR >= 3.0

AAA 기준:
- 일반 텍스트: CR >= 7.0
- 대형 텍스트: CR >= 4.5
```

### 대비비 미충족 시 자동 조정

```
1. 현재 전경색과 배경색의 대비비 계산
2. CR < 목표 시:
   a. HSL 색공간에서 L만 조정하여 색조 유지
   b. L_target 역산: (L_fg + 0.05) / target_CR - 0.05
3. 조정 전후 색상 함께 보고
```

## 컴포넌트별 ARIA 패턴

### Button
```html
<button type="button" aria-label="닫기" aria-pressed="false">
  <svg aria-hidden="true">...</svg>
</button>
```

### Modal/Dialog
```html
<div role="dialog" aria-modal="true" aria-labelledby="title-id">
  <h2 id="title-id">제목</h2>
  <!-- 포커스 트랩: Tab은 dialog 내부에서만 순환 -->
  <!-- Esc로 닫기, 닫힐 때 트리거 요소로 포커스 복귀 -->
</div>
```

### Select/Combobox
```html
<div role="combobox" aria-expanded="false" aria-haspopup="listbox">
  <input aria-autocomplete="list" aria-controls="listbox-id" />
  <ul id="listbox-id" role="listbox">
    <li role="option" aria-selected="true">옵션 1</li>
  </ul>
</div>
```

### Tab
```html
<div role="tablist" aria-label="설정">
  <button role="tab" aria-selected="true" aria-controls="panel-1">탭1</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">내용</div>
```

## 키보드 인터랙션 매트릭스

| 컴포넌트 | Tab | Enter | Space | Esc | Arrow | Home/End |
|---------|-----|-------|-------|-----|-------|----------|
| Button | 포커스 | 클릭 | 클릭 | - | - | - |
| Checkbox | 포커스 | 토글 | 토글 | - | - | - |
| Radio | 그룹포커스 | 선택 | 선택 | - | 순환 | 처음/끝 |
| Select | 포커스 | 열기 | 열기 | 닫기 | 항목이동 | 처음/끝 |
| Modal | 내부순환 | - | - | 닫기 | - | - |
| Tab | 탭포커스 | 활성화 | 활성화 | - | 탭이동 | 처음/끝 |
| Menu | 포커스 | 열기/실행 | 열기/실행 | 닫기 | 항목이동 | 처음/끝 |
| Slider | 포커스 | - | - | - | 값조정 | 최소/최대 |

## 검증 보고서 템플릿

```markdown
## 접근성 검증 보고서

### 요약
- 검증 수준: WCAG 2.1 AA
- P0 이슈: N건 (릴리스 차단)
- P1 이슈: N건 (권고)

### P0 이슈 (필수 수정)
| # | 컴포넌트 | 기준 | 문제 | 수정 방안 |

### 대비비 매트릭스
| 전경 | 배경 | 대비비 | AA일반 | AA대형 |

### 키보드 테스트 결과
| 컴포넌트 | Tab | Enter | Space | Esc | Arrow | 결과 |
```
