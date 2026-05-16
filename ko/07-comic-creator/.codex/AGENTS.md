# Comic Creator Codex Harness

이 폴더는 만화 제작용 Codex 하네스입니다. 한국어 만화, 4컷 만화, 웹툰, 스토리보드, 대사, 이미지 프롬프트, 레이아웃, 리뷰 작업에는 `comic-creator` 스킬을 사용합니다.

## 폴더 구조

```text
.codex/
|-- AGENTS.md
`-- skills/
    `-- comic-creator/
        |-- SKILL.md
        `-- references/
            |-- role-guides.md
            |-- panel-composition.md
            |-- visual-narrative.md
            `-- character-design-system.md
```

## 기본 사용법

Codex에게 만화 아이디어나 기존 시나리오를 전달하면, `comic-creator` 스킬 규칙에 따라 제작 산출물을 날짜 기반의 고유 작업 폴더 아래에 작성합니다. 기본은 `_workspace/YYYY-MM-DD/`이고, 같은 날짜 폴더가 이미 있으면 `_workspace/YYYY-MM-DD-01/`, `_workspace/YYYY-MM-DD-02/`처럼 다음 번호를 붙입니다.

예시 요청:

```text
comic-creator 스킬로 4컷 만화 제작 패키지 만들어줘.
주제: AI 비서와 초보 개발자
톤: 가볍고 웃긴 느낌
대상: 중학생 이상
스타일: 한국 웹툰풍
```

짧게 요청해도 됩니다.

```text
4컷 만화 만들어줘. 주제는 코딩하다가 버그 잡는 이야기.
```

요청에 형식이 명확하지 않으면, 작은 만화는 기본적으로 4컷 만화로 진행합니다. 필요한 정보가 비어 있어도 안전한 기본값을 둘 수 있으면 진행하고, 가정한 내용은 `00_input.md`에 기록합니다.

## 생성 산출물

기본 산출물은 고유 작업 폴더 `WORKSPACE_DIR` 아래에 저장합니다. 예를 들어 2026년 5월 16일에 처음 작업하면 `_workspace/2026-05-16/`을 사용하고, 이미 있으면 `_workspace/2026-05-16-01/`부터 순서대로 사용합니다.

- `WORKSPACE_DIR/00_input.md`: 사용자 요청을 정리한 제작 브리프
- `WORKSPACE_DIR/01_storyboard.md`: 줄거리, 캐릭터 시트, 페이지/컷별 스토리보드
- `WORKSPACE_DIR/02_dialogue.md`: 대사, 내레이션, 효과음, 말풍선 메모
- `WORKSPACE_DIR/03_image_prompts.md`: 캐릭터 기준 프롬프트와 컷별 이미지 프롬프트
- `WORKSPACE_DIR/04_layout.md`: 페이지 또는 웹툰 레이아웃/편집 지시서
- `WORKSPACE_DIR/05_review_report.md`: 전체 검토 결과와 수정 필요 사항
- `WORKSPACE_DIR/panels/`: 생성되었거나 배치 예정인 패널 이미지

이미지 생성 도구를 사용할 수 없거나 실행 범위를 벗어난 경우에도, 실제 제작에 쓸 수 있는 프롬프트와 지시서를 작성하고 제한 사항을 `05_review_report.md`에 명확히 남깁니다.

## 작업 모드

- 전체 제작: 스토리보드, 대사, 이미지 프롬프트, 레이아웃, 리뷰까지 작성
- 스토리보드 모드: `01_storyboard.md`와 `05_review_report.md` 중심으로 작성
- 대사 모드: `01_storyboard.md`, `02_dialogue.md`, `05_review_report.md` 작성
- 이미지 모드: 기존 스토리보드나 대본을 바탕으로 `03_image_prompts.md`, `04_layout.md`, `05_review_report.md` 작성
- 이미지 생성 모드: 사용자가 실제 패널 이미지를 요청하면 `imagegen` 스킬을 사용해 `03_image_prompts.md`의 프롬프트를 이미지로 만들고 결과를 `WORKSPACE_DIR/panels/`에 저장
- 리뷰 모드: 제공된 산출물을 검토하고 `05_review_report.md` 작성

## 작업 원칙

- durable output은 채팅에만 남기지 말고 고유 작업 폴더 `WORKSPACE_DIR/`에 파일로 저장합니다.
- 레거시 하네스 명령, hooks, 커스텀 메시지 API에 의존하지 않습니다.
- 사용자가 명시적으로 병렬 에이전트나 위임을 요청한 경우에만 Codex subagent를 사용합니다.
- 이론 설명보다 바로 제작에 쓸 수 있는 간결한 산출물을 우선합니다.
