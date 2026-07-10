# YouTube Production Harness

YouTube 영상 콘텐츠의 기획→대본→썸네일→SEO를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── content-strategist.md  — 콘텐츠 전략 (주제분석, 경쟁벤치마킹, 컨셉설계)
│   ├── scriptwriter.md        — 대본 작성 (훅, 세그먼트, CTA, 시각큐)
│   ├── thumbnail-designer.md  — 썸네일 설계 + Gemini 이미지 생성
│   ├── seo-optimizer.md       — SEO 패키지 (제목/설명/태그/챕터/자막)
│   └── production-reviewer.md — 교차 검증 (전략↔대본↔썸네일↔SEO 정합성)
├── skills/
│   └── youtube-production/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
└── README.md                  — 이 파일
```

## 사용법

`/youtube-production` 스킬을 트리거하거나, "유튜브 영상 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_strategist_brief.md` — 전략 브리프
- `02_scriptwriter_script.md` — 영상 대본
- `03_thumbnail_concept.md` — 썸네일 컨셉
- `04_seo_package.md` — SEO 패키지
- `05_review_report.md` — 리뷰 보고서
- `subtitle.srt` — 자막 파일
