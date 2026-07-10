# E-commerce Launcher Harness

이커머스 상품 런칭의 기획→상세페이지→가격전략→마케팅→CS 셋업을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── product-planner.md      — 상품 기획 (시장조사, 타깃, 포지셔닝)
│   ├── detail-page-writer.md   — 상세페이지 작성 (카피, SEO, 전환)
│   ├── pricing-strategist.md   — 가격 전략 (원가, 경쟁가격, 마진)
│   ├── marketing-manager.md    — 마케팅 매니저 (채널, 광고, 런칭)
│   └── cs-architect.md         — CS 설계자 (FAQ, 응대매뉴얼, 반품정책)
├── skills/
│   ├── ecommerce-launcher/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── conversion-optimization/
│   │   └── SKILL.md            — 구매전환 최적화 (detail-page-writer 확장)
│   └── product-copy-formulas/
│       └── SKILL.md            — 상품 카피 공식 (marketing-manager 확장)
└── README.md                   — 이 파일
```

## 사용법

`/ecommerce-launcher` 스킬을 트리거하거나, "이커머스 상품 런칭해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_product_brief.md` — 상품 기획서
- `02_detail_page.md` — 상세페이지 원고
- `03_pricing_plan.md` — 가격 전략서
- `04_marketing_plan.md` — 마케팅 플랜
- `05_cs_manual.md` — CS 운영 매뉴얼
- `06_review_report.md` — 통합 리뷰 보고서
