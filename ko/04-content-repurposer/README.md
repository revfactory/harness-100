# Content Repurposer Harness

1개 원본 콘텐츠를 블로그·SNS·뉴스레터·프레젠테이션·스크립트로 다중 변환하는 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── source-analyst.md        — 원본 분석가 (구조 분석, 핵심 추출, 변환 전략)
│   ├── blog-writer.md           — 블로그 작가 (SEO 최적화 블로그 포스트)
│   ├── sns-copywriter.md        — SNS 카피라이터 (플랫폼별 포스트)
│   ├── presentation-builder.md  — 프레젠테이션 빌더 (슬라이드 구성)
│   └── quality-reviewer.md      — 품질 검증자 (교차 검증, 메시지 일관성)
├── skills/
│   ├── content-repurposer/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── platform-adaptation/
│   │   └── SKILL.md             — sns-copywriter+blog-writer 확장 (플랫폼별 DNA, 변환 매트릭스)
│   └── content-atomization/
│       └── SKILL.md             — source-analyst+presentation-builder 확장 (MINE 분석, 원자 분류)
└── README.md                    — 이 파일
```

## 사용법

`/content-repurposer` 스킬을 트리거하거나, "이 콘텐츠 리퍼포징해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_source_analysis.md` — 원본 분석 보고서
- `02_blog_post.md` — 블로그 포스트
- `03_sns_package.md` — SNS 포스트 패키지
- `04_presentation.md` — 프레젠테이션 슬라이드
- `05_review_report.md` — 리뷰 보고서
