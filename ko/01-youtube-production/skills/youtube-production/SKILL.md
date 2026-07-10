---
name: youtube-production
description: "YouTube 영상 콘텐츠의 기획, 대본(스크립트), 썸네일, SEO 메타데이터를 에이전트 팀이 협업하여 한 번에 생성하는 풀 프로덕션 파이프라인. '유튜브 영상 기획해줘', '영상 대본 써줘', '영상 스크립트', '유튜브 콘텐츠 전략', '영상 시나리오', '유튜브 쇼츠 기획', 'YouTube 썸네일 만들어줘', '영상 SEO 최적화', '유튜브 채널 콘텐츠' 등 YouTube 영상 콘텐츠 제작 전반에 이 스킬을 사용한다. 기존 대본이 있는 경우에도 SEO 최적화나 썸네일 제작을 지원한다. 단, 실제 영상 편집(Premiere, DaVinci), 유튜브 Analytics API 연동, 채널 운영 대시보드 구축은 이 스킬의 범위가 아니다."
---

# YouTube Production — 영상 콘텐츠 풀 프로덕션 파이프라인

YouTube 영상의 기획→대본→썸네일→SEO를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| content-strategist | `agents/content-strategist.md` | 주제분석, 경쟁벤치마킹, 컨셉설계 | general-purpose |
| scriptwriter | `agents/scriptwriter.md` | 대본 작성, 시각 큐 삽입 | general-purpose |
| thumbnail-designer | `agents/thumbnail-designer.md` | 썸네일 컨셉 + 이미지 생성 | general-purpose |
| seo-optimizer | `agents/seo-optimizer.md` | 제목/설명/태그/챕터/자막 | general-purpose |
| production-reviewer | `agents/production-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **주제/키워드**: 영상이 다룰 주제
   - **채널 정보** (선택): 채널 톤, 구독자 규모, 기존 콘텐츠 방향
   - **제약 조건** (선택): 영상 길이, 특정 요구사항
   - **기존 파일** (선택): 사용자가 제공한 대본, 기획서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 콘텐츠 전략 수립 | strategist | 없음 | `_workspace/01_strategist_brief.md` |
| 2a | 대본 작성 | writer | 작업 1 | `_workspace/02_scriptwriter_script.md` |
| 2b | 썸네일 설계·생성 | designer | 작업 1 | `_workspace/03_thumbnail_concept.md` |
| 3 | SEO 패키지 | seo | 작업 1, 2a | `_workspace/04_seo_package.md`, `_workspace/subtitle.srt` |
| 4 | 프로덕션 리뷰 | reviewer | 작업 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(대본)와 2b(썸네일)는 **병렬 실행**한다. 둘 다 작업 1(전략)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- strategist 완료 → writer에게 핵심 앵글·톤 전달, designer에게 제목 후보·감정 포인트 전달, seo에게 키워드 맵 전달
- writer 완료 → designer에게 훅 핵심 메시지 전달 (썸네일-훅 일관성), seo에게 대본 전달
- seo 완료 → designer에게 제목-썸네일 조합 피드백 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 전략 브리프 — `01_strategist_brief.md`
   - 영상 대본 — `02_scriptwriter_script.md`
   - 썸네일 컨셉 + 이미지 — `03_thumbnail_concept.md`
   - SEO 패키지 — `04_seo_package.md`
   - 리뷰 보고서 — `05_review_report.md`
   - 자막 파일 — `subtitle.srt`

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "유튜브 영상 기획해줘", "풀 프로덕션" | **풀 파이프라인** | 5명 전원 |
| "대본만 써줘", "스크립트만" | **대본 모드** | strategist + writer + reviewer |
| "이 대본으로 SEO 최적화해줘" (기존 파일) | **SEO 모드** | seo + reviewer |
| "영상 썸네일 만들어줘" (기존 기획 있음) | **썸네일 모드** | designer + reviewer |
| "이 대본 검토해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 대본, 기획서 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다. 예: 기존 대본 제공 → `_workspace/02_scriptwriter_script.md`로 복사 → writer 건너뛰고 seo·designer·reviewer만 투입.

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
| 웹 검색 실패 | 전략가가 일반 지식 기반으로 작업, 보고서에 "데이터 제한" 명시 |
| 썸네일 이미지 생성 실패 | 텍스트 컨셉만으로 진행, Gemini 프롬프트 포함하여 사용자 재시도 가능 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 에이전트별 확장 스킬

| 스킬 | 경로 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| hook-writing | `skills/hook-writing/SKILL.md` | scriptwriter | 15가지 훅 패턴, 시청 유지율 심리학, 훅-썸네일-제목 삼각 정합성 |
| thumbnail-psychology | `skills/thumbnail-psychology/SKILL.md` | thumbnail-designer | 색상 심리학, 7가지 구도 패턴, 텍스트 가독성, 3초 테스트 |

에이전트는 자신의 작업 수행 시 해당 확장 스킬을 참조하여 도메인 전문성을 강화한다.

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "AI 프롬프트 엔지니어링 초보자 가이드로 10분짜리 유튜브 영상을 기획해줘"
**기대 결과**:
- 전략 브리프: 경쟁 분석 3건 이상, 키워드 맵, 제목 후보 3개
- 대본: 10분 분량(약 2,500단어 한국어 기준), 훅+3~4세그먼트+클로징
- 썸네일: A/B안 컨셉 + 이미지 생성 시도
- SEO: 제목/설명/태그/챕터/SRT
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 대본 파일로 SEO 최적화랑 썸네일 만들어줘" + 대본 파일 첨부
**기대 결과**:
- 기존 대본을 `_workspace/02_scriptwriter_script.md`로 복사
- SEO 모드 + 썸네일 모드 병합: seo + designer + reviewer 투입
- strategist, writer는 건너뜀

### 에러 흐름
**프롬프트**: "유튜브 영상 대본만 빨리 써줘, 주제는 아무거나"
**기대 결과**:
- 대본 모드로 전환 (strategist + writer + reviewer)
- 주제가 불분명하므로 전략가가 트렌드 기반 주제 3개 제안 후 진행
- 리뷰 보고서에 "썸네일/SEO 미생성" 명시
