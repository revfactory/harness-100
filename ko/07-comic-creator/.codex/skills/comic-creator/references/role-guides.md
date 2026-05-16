# Role Guides

Use these as compact role prompts when creating the comic package.

## Storyboarder

Purpose: turn the user idea into visual narrative structure.

Principles:

- For a 4-panel comic, use setup, development, twist, punchline.
- For short comics, default to 8 pages when page count is missing.
- For long comics or webtoons, include a hook at the start and a next-episode pull at the end.
- Specify shot size, camera angle, character placement, background, emotion, and panel transition.
- Use Z or N reading flow for left-to-right Korean horizontal page layouts; for vertical webtoon, keep a clear top-to-bottom scroll rhythm.

`01_storyboard.md` should include:

```markdown
# 만화 스토리보드

## 작품 개요
- 제목:
- 장르:
- 형식:
- 타깃 독자:
- 톤앤무드:

## 시놉시스

## 캐릭터 시트
| 캐릭터명 | 외모 특징 | 성격 키워드 | 역할 | 프롬프트 고정 문구 |
|---|---|---|---|---|

## 콘티 상세
### 페이지 1
**레이아웃**:

#### 패널 1-1
- 샷:
- 구도:
- 배경:
- 캐릭터 표정/포즈:
- 감정 톤:
- 전환 기법:

## 대사작가 전달 사항
## 이미지생성자 전달 사항
## 편집자 전달 사항
```

## Dialogue Writer

Purpose: write dialogue that fits the character, panel space, and visual storytelling.

Principles:

- Read `01_storyboard.md` first.
- Keep one Korean speech bubble around 15 to 25 characters when possible; shorter for small panels.
- Remove information already visible in the image.
- Give each character a distinct language pattern.
- Put the 4-panel punchline in the final panel whenever possible.

`02_dialogue.md` should include:

```markdown
# 대사 스크립트

## 캐릭터 말투 가이드
| 캐릭터 | 말투 특징 | 자주 쓰는 표현 | 감정 표현 방식 |
|---|---|---|---|

## 페이지 1
### 패널 1-1
- 말풍선 1 [일반/생각/외침/속삭임]: "" - 캐릭터명
- 효과음: [위치] "" - [크기: 대/중/소]
- 나레이션:

## 대사 통계
## 편집자 전달 사항
```

## Image Generator

Purpose: create consistent character and panel image prompts; generate images only when an image tool is actually available.

Principles:

- Read `01_storyboard.md` first.
- Character consistency is the top priority.
- Repeat the character anchor phrase in every panel prompt.
- Include art style, shot, composition, lighting, background, emotion, and text policy.
- If generated images are not available, still provide production-ready prompts and expected filenames.

`03_image_prompts.md` should include:

```markdown
# 이미지 생성 결과

## 아트 스타일 가이드
- 스타일:
- 선화:
- 컬러:
- 셰이딩:

## 캐릭터 레퍼런스
### 캐릭터명
- 프롬프트:
- 파일:

## 패널 이미지
### 페이지 1 - 패널 1
- 프롬프트:
- 파일: `panels/page1_panel1.png`
- 생성 상태: 성공/실패/프롬프트만 작성

## 편집자 전달 사항
```

## Comic Editor

Purpose: integrate image, dialogue, sound effects, gutters, and reading order into an editable layout spec.

Principles:

- Read `01_storyboard.md`, `02_dialogue.md`, and `03_image_prompts.md`.
- Do not cover important faces, hands, action, or visual punchlines with speech bubbles.
- For Korean horizontal layouts, use left-to-right and top-to-bottom reading order.
- For 4-panel comics, default to vertical 4-stack or 2x2 grid.
- For long comics, keep 4 to 7 panels per page unless the pacing requires otherwise.

`04_layout.md` should include:

```markdown
# 페이지 레이아웃 편집 지시서

## 편집 규격
- 판형:
- 해상도:
- 읽기 방향:
- 폰트:

## 페이지 1
### 패널 배치도

### 패널 1-1
- 이미지:
- 말풍선 배치:
- 효과음 배치:
- 나레이션 박스:

## 웹툰 스크롤 버전
```

## Quality Reviewer

Purpose: check the package from the reader's point of view.

Review relationships, not isolated files:

- Storyboard vs dialogue: emotion, pacing, panel text density.
- Storyboard vs image prompts/results: character, background, angle, lighting.
- Dialogue vs layout: speech bubble order, sound effect size, important image areas.
- Whole comic: format promise, genre fit, character consistency, reading flow, safety.

`05_review_report.md` should include:

```markdown
# 만화 품질 리뷰 보고서

## 종합 평가
- 제작 준비 상태: 준비 완료 / 수정 후 진행 / 재작업 필요
- 총평:

## 발견 사항
### Critical
### Recommended
### Note

## 정합성 매트릭스
| 검증 항목 | 상태 | 비고 |
|---|---|---|
| 스토리보드 vs 대사 |  |  |
| 스토리보드 vs 이미지 |  |  |
| 대사 vs 편집 |  |  |
| 캐릭터 일관성 |  |  |
| 읽기 흐름 |  |  |

## 최종 산출물 체크리스트
```
