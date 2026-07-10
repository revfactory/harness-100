---
name: mobile-ux-patterns
description: "모바일 UX 설계 패턴 라이브러리. iOS HIG/Material Design 3 가이드라인, 네비게이션 패턴, 제스처 인터랙션, 반응형 레이아웃, 접근성 체크리스트를 제공하는 ux-designer 확장 스킬. '모바일 UX', 'iOS 가이드라인', 'Material Design', '네비게이션 패턴', '제스처', '디자인 토큰', '모바일 접근성' 등 모바일 UI/UX 설계 시 사용한다. 단, 실제 디자인 파일 생성이나 코드 구현은 이 스킬의 범위가 아니다."
---

# Mobile UX Patterns — 모바일 UX 설계 패턴 라이브러리

ux-designer 에이전트가 모바일 앱 UX 설계 시 활용하는 플랫폼 가이드라인, 네비게이션 패턴, 디자인 토큰 레퍼런스.

## 대상 에이전트

`ux-designer` — 이 스킬의 UX 패턴과 가이드라인을 앱 설계에 직접 적용한다.

## 플랫폼 가이드라인 핵심 비교

### iOS (Human Interface Guidelines) vs Android (Material Design 3)

| 요소 | iOS HIG | Material Design 3 |
|------|---------|-------------------|
| **네비게이션** | Tab Bar (하단) + Nav Bar (상단) | Bottom Navigation + Top App Bar |
| **버튼 스타일** | 라운드, 시스템 블루, 미니멀 | Filled, Outlined, Tonal, Text |
| **타이포** | SF Pro (시스템) | Roboto (시스템), 커스텀 가능 |
| **아이콘** | SF Symbols, 라인 스타일 | Material Symbols, 채움 가능 |
| **모달** | Sheet (하단), Alert | Bottom Sheet, Dialog |
| **스와이프** | 뒤로가기 (엣지 스와이프) | 제스처 네비게이션 |
| **색상** | Dynamic Color (라이트/다크) | Material You (동적 색상) |
| **터치 타깃** | 최소 44x44pt | 최소 48x48dp |

## 네비게이션 패턴

### 패턴 선택 가이드

| 패턴 | 적합 | 탭 수 | 예시 앱 |
|------|------|--------|---------|
| **Tab Bar** | 3~5개 주요 섹션 | 3~5 | Instagram, YouTube |
| **Drawer** | 6개+ 섹션, 설정 포함 | 무제한 | Gmail, Notion |
| **Stack** | 계층적 콘텐츠 | - | 설정, 상세 화면 |
| **Tab + Stack** | 섹션 내 깊은 탐색 | 3~5 | 대부분의 앱 |
| **Bottom Sheet** | 임시 선택/필터 | - | 지도, 음악 플레이어 |

### 네비게이션 깊이 규칙
- 최대 3~4 depth (홈 → 카테고리 → 목록 → 상세)
- 어디서든 홈으로 돌아갈 수 있어야 함
- 뒤로가기 항상 가능 (뒤로 버튼 또는 엣지 스와이프)
- 현재 위치를 항상 알 수 있어야 함 (타이틀, 하이라이트)

## 화면 유형별 레이아웃

### 목록 화면 (List)
- 아이템 높이: 최소 48dp (iOS 44pt)
- 썸네일: 40~56dp 정사각/원형
- 제목: 16~17sp, 1줄
- 부제: 14sp, 1~2줄, secondary 색상
- 액션: trailing 영역 (아이콘 또는 스위치)
- 구분선: 1dp, 텍스트 시작점부터

### 상세 화면 (Detail)
- 히어로 이미지: 화면 너비 100%, 높이 250~300dp
- 스크롤 시 App Bar 변환 (Collapsing Toolbar)
- 제목: 24~28sp Bold
- 본문: 16sp, 행간 1.5
- FAB 또는 하단 고정 CTA

### 폼 화면 (Form)
- 필드 간격: 16~24dp
- 라벨: 필드 위 또는 플로팅
- 에러 메시지: 필드 아래, 빨간색
- 키보드: 필드 타입에 맞는 키보드 (email, number, tel)
- 버튼: 하단 고정, 키보드 위에 표시

### 빈 상태 (Empty State)
- 중앙 정렬 일러스트/아이콘
- 제목 (무엇이 비어있는지)
- 설명 (무엇을 할 수 있는지)
- CTA 버튼

## 제스처 인터랙션 가이드

| 제스처 | 용도 | 주의사항 |
|--------|------|---------|
| **탭** | 선택, 실행 | 항상 시각적 피드백 (ripple/highlight) |
| **롱프레스** | 컨텍스트 메뉴, 멀티선택 | 힌트 필요 (시각적 단서) |
| **스와이프 좌/우** | 삭제/보관, 탭 전환 | 뒤로가기와 충돌 주의 |
| **풀 다운** | 새로고침 | Pull-to-Refresh 표준 사용 |
| **핀치** | 줌 인/아웃 | 이미지/지도에서만 |
| **드래그** | 순서 변경, 이동 | 핸들 아이콘 표시 |

## 디자인 토큰

### 스페이싱 스케일 (8dp 기반)
| 토큰 | 값 | 용도 |
|------|---|------|
| xs | 4dp | 인라인 요소 간격 |
| sm | 8dp | 카드 내부 패딩 |
| md | 16dp | 섹션 간격, 화면 마진 |
| lg | 24dp | 섹션 간 구분 |
| xl | 32dp | 주요 섹션 간 |
| 2xl | 48dp | 히어로/헤더 간격 |

### 타이포 스케일
| 역할 | 크기 | 무게 | 행간 |
|------|------|------|------|
| Display | 34~57sp | Bold | 1.12 |
| Headline | 24~32sp | SemiBold | 1.25 |
| Title | 16~22sp | Medium | 1.27 |
| Body | 14~16sp | Regular | 1.5 |
| Label | 11~14sp | Medium | 1.45 |
| Caption | 11~12sp | Regular | 1.33 |

### 색상 시스템 (Material 3 기반)
| 역할 | 용도 |
|------|------|
| Primary | 주요 CTA, 활성 요소 |
| On Primary | Primary 위 텍스트/아이콘 |
| Primary Container | 배경 강조 |
| Secondary | 보조 버튼, 칩 |
| Surface | 카드, 시트 배경 |
| Error | 에러 상태 |
| Outline | 테두리, 비활성 |

## 접근성 체크리스트

- [ ] 터치 타깃 최소 48x48dp (iOS 44x44pt)
- [ ] 색상 대비 4.5:1 이상 (텍스트), 3:1 (대형 텍스트)
- [ ] 색상만으로 정보 전달하지 않기 (아이콘/텍스트 병행)
- [ ] 스크린 리더 라벨 (contentDescription/accessibilityLabel)
- [ ] 동적 글꼴 크기 지원 (Dynamic Type/sp 단위)
- [ ] 모션 축소 설정 대응 (prefers-reduced-motion)
- [ ] 키보드/외부 입력 지원
- [ ] 포커스 순서 논리적 배치

## 성능 UX 패턴

| 상황 | 패턴 | 설명 |
|------|------|------|
| 로딩 | Skeleton UI | 레이아웃 미리 보여주기 |
| 느린 응답 | Progress Indicator | 0.5초 후 표시 |
| 오프라인 | Cache + Banner | 캐시 데이터 표시 + 오프라인 알림 |
| 에러 | Retry + Fallback | 재시도 버튼 + 마지막 정상 데이터 |
| 낙관적 UI | Optimistic Update | 즉시 반영, 실패 시 롤백 |
