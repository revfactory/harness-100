---
name: comic-creator
description: "4컷 만화, 단편 만화, 장편 만화(웹툰 포함)의 콘티→대사→이미지생성→편집을 에이전트 팀이 협업하여 한 번에 제작하는 풀 프로덕션 파이프라인. '만화 만들어줘', '4컷 만화 그려줘', '웹툰 제작', '만화 콘티', '코믹 스트립', '만화 시나리오', '일러스트 만화', '만화 스토리보드' 등 만화 제작 전반에 이 스킬을 사용한다. 기존 시나리오가 있는 경우에도 이미지 생성이나 편집 지시서 작성을 지원한다. 단, 실제 이미지 편집 소프트웨어(포토샵, 클립스튜디오) 조작, 인쇄 입고, 웹툰 플랫폼 업로드는 이 스킬의 범위가 아니다."
---

# Comic Creator — 만화 제작 풀 프로덕션 파이프라인

4컷/단편/장편 만화의 콘티→대사→이미지생성→편집을 에이전트 팀이 협업하여 한 번에 제작한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| storyboarder | `agents/storyboarder.md` | 시놉시스, 콘티, 패널 레이아웃 설계 | general-purpose |
| dialogue-writer | `agents/dialogue-writer.md` | 캐릭터 대사, 효과음, 나레이션 | general-purpose |
| image-generator | `agents/image-generator.md` | Gemini 기반 패널 이미지 생성 | general-purpose |
| comic-editor | `agents/comic-editor.md` | 말풍선 배치, 페이지 편집 지시서 | general-purpose |
| quality-reviewer | `agents/quality-reviewer.md` | 정합성 검증, 연속성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **주제/스토리 아이디어**: 만화로 만들 이야기
   - **형식**: 4컷 / 단편(8~16페이지) / 장편(챕터제) / 웹툰
   - **장르**: 코미디, 드라마, 판타지, 일상, 액션 등
   - **아트 스타일** (선택): 일본 만화풍, 미국 코믹, 웹툰 스타일 등
   - **기존 파일** (선택): 시나리오, 캐릭터 설정 등
2. `_workspace/` 디렉토리와 `_workspace/panels/` 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 스토리보드/콘티 | storyboarder | 없음 | `_workspace/01_storyboard.md` |
| 2a | 대사 작성 | dialogue-writer | 작업 1 | `_workspace/02_dialogue.md` |
| 2b | 패널 이미지 생성 | image-generator | 작업 1 | `_workspace/03_image_prompts.md`, `_workspace/panels/` |
| 3 | 페이지 편집 지시서 | comic-editor | 작업 1, 2a, 2b | `_workspace/04_layout.md` |
| 4 | 품질 검증 | quality-reviewer | 작업 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(대사)와 2b(이미지)는 **병렬 실행**한다. 둘 다 작업 1(스토리보드)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- storyboarder 완료 → dialogue-writer에게 패널별 상황·감정 전달, image-generator에게 캐릭터시트·구도 전달
- dialogue-writer 완료 → image-generator에게 효과음 스타일 전달, comic-editor에게 말풍선 유형·순서 전달
- image-generator 완료 → comic-editor에게 이미지 파일·여백 정보 전달
- comic-editor 완료 → quality-reviewer에게 편집 지시서 전달
- quality-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 스토리보드 — `01_storyboard.md`
   - 대사 스크립트 — `02_dialogue.md`
   - 이미지 프롬프트/결과 — `03_image_prompts.md`
   - 편집 지시서 — `04_layout.md`
   - 리뷰 보고서 — `05_review_report.md`
   - 패널 이미지 — `panels/` 디렉토리

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "만화 만들어줘", "풀 프로덕션" | **풀 파이프라인** | 5명 전원 |
| "콘티만 짜줘", "스토리보드만" | **콘티 모드** | storyboarder + reviewer |
| "이 시나리오로 만화 그려줘" (기존 파일) | **이미지 모드** | image-generator + comic-editor + reviewer |
| "대사만 써줘" | **대사 모드** | storyboarder + dialogue-writer + reviewer |
| "이 만화 검토해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 시나리오, 콘티 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물명}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 이미지 생성 실패 | 텍스트 프롬프트만으로 진행, 사용자가 프롬프트로 재시도 가능 |
| 캐릭터 일관성 깨짐 | 프롬프트에 캐릭터 설명 강화 후 재생성 (최대 2회) |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 부적절한 콘텐츠 거부 | 프롬프트 수정 후 재시도, 보고서에 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "프로그래머의 일상을 주제로 4컷 만화를 만들어줘. 코미디 장르로."
**기대 결과**:
- 스토리보드: 기승전결 4패널 콘티, 캐릭터 시트
- 대사: 캐릭터별 말투, 효과음, 펀치라인
- 이미지: 4개 패널 이미지 생성 시도 (일관된 아트 스타일)
- 편집: 말풍선 배치, 읽기 흐름 지시서
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 시나리오로 웹툰 만들어줘" + 시나리오 파일 첨부
**기대 결과**:
- 기존 시나리오를 `_workspace/01_storyboard.md`에 반영
- storyboarder는 시나리오 기반으로 패널 레이아웃만 추가 설계
- dialogue-writer + image-generator + comic-editor + reviewer 투입

### 에러 흐름
**프롬프트**: "만화 콘티만 빨리 짜줘, 주제는 아무거나"
**기대 결과**:
- 콘티 모드로 전환 (storyboarder + reviewer)
- 주제가 불분명하므로 스토리보더가 장르별 시놉시스 3개 제안 후 진행
- 리뷰 보고서에 "대사/이미지/편집 미생성" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| storyboarder, image-generator | `/panel-composition` | 카메라 앵글, 시선 유도, 페이지 리듬, 프롬프트 구조 |
| dialogue-writer, comic-editor | `/visual-narrative` | 말풍선 시스템, 효과음 타이포, Show-Don't-Tell, 장면 전환 |
| storyboarder, image-generator | `/character-design-system` | 캐릭터 시트, 실루엣 테스트, 표정 차트, AI 일관성 전략 |
