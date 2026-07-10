# Book Publishing Harness

전자책 출판의 원고편집→표지→목차→메타데이터→배포를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── manuscript-editor.md     — 편집자 (구조편집, 문체교정, 일관성)
│   ├── proofreader.md           — 교정교열자 (맞춤법, 문법, 표기통일)
│   ├── cover-designer.md        — 표지디자이너 (표지컨셉, 이미지생성, 타이포)
│   ├── metadata-manager.md      — 메타데이터관리자 (ISBN, 분류, 설명, 키워드, 배포)
│   └── publishing-reviewer.md   — 출판검증자 (품질검증, 규격확인, 최종체크)
├── skills/
│   ├── book-publishing/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── developmental-editing/
│   │   └── SKILL.md             — manuscript-editor 확장 (SPINE 체크, 장르별 편집, 페이싱)
│   ├── cover-design-psychology/
│   │   └── SKILL.md             — cover-designer 확장 (장르별 컨벤션, 타이포, AI 프롬프트)
│   └── book-metadata-seo/
│       └── SKILL.md             — metadata-manager 확장 (BISAC/KDC, 키워드, AIDA 설명문)
└── README.md                    — 이 파일
```

## 사용법

`/book-publishing` 스킬을 트리거하거나, "전자책 출판해줘", "원고 편집해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_edited_manuscript.md` — 편집된 원고
- `02_proofread_report.md` — 교정교열 보고서
- `03_cover_concept.md` — 표지 컨셉/이미지
- `04_metadata.md` — 메타데이터/배포 설정
- `05_review_report.md` — 리뷰 보고서
