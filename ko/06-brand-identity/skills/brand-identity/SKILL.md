---
name: brand-identity
description: "브랜드 아이덴티티를 네이밍, 슬로건, 톤앤매너, 비주얼 가이드라인까지 에이전트 팀이 협업하여 한 번에 설계하는 풀 브랜딩 파이프라인. '브랜드 만들어줘', '브랜드 아이덴티티 설계', '브랜드 네이밍', '슬로건 만들어줘', '브랜드 가이드라인', '로고 컨셉', '톤앤매너 설계', '브랜드 전략' 등 브랜드 아이덴티티 설계 전반에 이 스킬을 사용한다. 기존 브랜드명이 있는 경우에도 슬로건/비주얼 설계를 지원한다. 단, 실제 로고 파일(.ai, .svg) 제작, 인쇄물 시안, 상표 출원 대행은 이 스킬의 범위가 아니다."
---

# Brand Identity — 브랜드 아이덴티티 풀 설계 파이프라인

브랜드의 전략→네이밍→버벌→비주얼을 에이전트 팀이 협업하여 한 번에 설계한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| brand-strategist | `agents/brand-strategist.md` | 시장 분석, 포지셔닝, 아키타입 | general-purpose |
| naming-specialist | `agents/naming-specialist.md` | 브랜드명 개발, 도메인/상표 검토 | general-purpose |
| copywriter | `agents/copywriter.md` | 슬로건, 톤앤매너, 브랜드 스토리 | general-purpose |
| visual-director | `agents/visual-director.md` | 컬러, 타이포, 로고 컨셉 | general-purpose |
| identity-reviewer | `agents/identity-reviewer.md` | 교차 검증, 일관성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **사업 영역**: 어떤 제품/서비스인가
   - **타깃 고객** (선택): 핵심 고객층
   - **경쟁 브랜드** (선택): 벤치마크할 브랜드
   - **브랜드 방향** (선택): 원하는 이미지, 키워드
   - **기존 요소** (선택): 이미 확정된 브랜드명, 컬러 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 브랜드 전략 수립 | brand-strategist | 없음 | `_workspace/01_brand_strategy.md` |
| 2 | 네이밍 개발 | naming-specialist | 작업 1 | `_workspace/02_naming_candidates.md` |
| 3a | 버벌 아이덴티티 | copywriter | 작업 1, 2 | `_workspace/03_verbal_identity.md` |
| 3b | 비주얼 아이덴티티 | visual-director | 작업 1, 2 | `_workspace/04_visual_identity.md` |
| 4 | 아이덴티티 검증 | identity-reviewer | 작업 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(버벌)와 3b(비주얼)는 **병렬 실행**한다. 둘 다 작업 2(네이밍)에 의존하므로 네이밍 완성 후 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- brand-strategist 완료 → naming-specialist에게 에센스·아키타입·경쟁 분석 전달, copywriter에게 미션/비전/타깃 전달, visual-director에게 아키타입·포지셔닝 전달
- naming-specialist 완료 → copywriter에게 TOP 5 네이밍+의미 전달, visual-director에게 네이밍 시각적 특성 전달
- copywriter ↔ visual-director: 톤앤매너와 비주얼 무드의 일관성을 상호 조율
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 브랜드 전략 — `01_brand_strategy.md`
   - 네이밍 후보 — `02_naming_candidates.md`
   - 버벌 아이덴티티 — `03_verbal_identity.md`
   - 비주얼 아이덴티티 — `04_visual_identity.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "브랜드 아이덴티티 전체 설계", "풀 브랜딩" | **풀 파이프라인** | 5명 전원 |
| "브랜드 네이밍만 해줘" | **네이밍 모드** | brand-strategist + naming-specialist + identity-reviewer |
| "이 브랜드명으로 슬로건 만들어줘" (기존 이름) | **버벌 모드** | copywriter + identity-reviewer |
| "비주얼 가이드라인 만들어줘" (기존 브랜드 있음) | **비주얼 모드** | visual-director + identity-reviewer |
| "이 브랜드 가이드라인 검토해줘" | **리뷰 모드** | identity-reviewer 단독 |

**기존 파일 활용**: 사용자가 기존 브랜드명, 가이드라인 등을 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 전략가가 일반 지식 기반으로 작업, "실시간 시장 데이터 미반영" 명시 |
| 도메인/상표 확인 불가 | "[확인 필요]"로 표시, 사용자 직접 확인 권장 |
| Gemini 이미지 생성 실패 | 텍스트 컨셉+프롬프트만으로 진행, 사용자 재시도 가능 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "친환경 생활용품 브랜드를 만들려고 해. 2030 여성 타깃, 프리미엄 포지셔닝으로 브랜드 아이덴티티 설계해줘"
**기대 결과**:
- 전략: 친환경 시장 분석, 경쟁 3개+ 벤치마킹, 페르소나, 아키타입(돌봄이/탐험가)
- 네이밍: 10개+ 후보 중 TOP 5, 도메인/상표 검토, 평가 매트릭스
- 버벌: 슬로건 5개+, 태그라인, 브랜드 스토리(3버전), 톤앤매너 가이드
- 비주얼: 컬러 팔레트(자연 계열), 타이포, 로고 컨셉 2개+, 적용 예시
- 리뷰: 일관성 점수, 정합성 매트릭스, 터치포인트 시뮬레이션

### 기존 파일 활용 흐름
**프롬프트**: "브랜드명은 'Greenleaf'로 정했어. 슬로건이랑 비주얼 가이드라인 만들어줘"
**기대 결과**:
- 기존 네이밍을 `_workspace/02_naming_candidates.md`에 기록
- 버벌 모드 + 비주얼 모드 병합: copywriter + visual-director + identity-reviewer 투입
- brand-strategist는 최소 전략만 수립, naming-specialist는 건너뜀

### 에러 흐름
**프롬프트**: "브랜드 만들어줘, 아무 분야나"
**기대 결과**:
- 전략가가 3가지 사업 영역+포지셔닝 방향을 제안
- 사용자 선택 후 풀 파이프라인 진행
- 리뷰 보고서에 "사용자 선택 기반 진행" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| naming-specialist | `/naming-methodology` | 12가지 네이밍 기법, SMILE 평가, 음운론적 분석, 도메인/상표 검토 |
| visual-director | `/color-psychology` | 색상별 심리 반응, 60-30-10 규칙, 접근성 기준, 팔레트 구축 |
| brand-strategist, copywriter | `/brand-archetype` | 12 아키타입 매핑, 톤앤보이스 변환, 브랜드 스토리 5장 구조 |
