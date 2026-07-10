# Social Media Manager Harness

SNS 콘텐츠 달력·포스트작성·해시태그·성과분석을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── sns-strategist.md       — SNS 전략가 (채널분석, 콘텐츠달력, 캠페인설계)
│   ├── copywriter.md           — 카피라이터 (포스트작성, 캡션, CTA)
│   ├── visual-planner.md       — 비주얼기획자 (이미지컨셉, 카드뉴스, 릴스기획)
│   ├── hashtag-analyst.md      — 해시태그분석가 (해시태그전략, 트렌드분석, 성과예측)
│   └── performance-reviewer.md — 성과검증자 (KPI정렬, 콘텐츠품질, 정합성)
├── skills/
│   ├── social-media-manager/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── platform-algorithms/
│   │   └── SKILL.md            — sns-strategist+visual-planner 확장 (알고리즘, 골든타임)
│   ├── viral-copywriting/
│   │   └── SKILL.md            — copywriter 확장 (15 훅 패턴, 감정 트리거, CTA)
│   └── hashtag-science/
│       └── SKILL.md            — hashtag-analyst 확장 (피라미드 전략, 리서치, 섀도우밴)
└── README.md                   — 이 파일
```

## 사용법

`/social-media-manager` 스킬을 트리거하거나, "SNS 콘텐츠 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_strategy.md` — SNS 전략/콘텐츠 달력
- `02_posts.md` — 포스트 카피 모음
- `03_visuals.md` — 비주얼 기획서
- `04_hashtags.md` — 해시태그 전략서
- `05_review_report.md` — 리뷰 보고서
