# Sales Enablement Harness

영업 지원 파이프라인: 고객분석→제안서→프레젠테이션→팔로업을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── customer-analyst.md      — 고객 분석 (니즈, 의사결정구조, 예산, 경쟁현황)
│   ├── proposal-writer.md       — 제안서 작성 (솔루션 매칭, 가격, ROI 산출)
│   ├── presenter.md             — 프레젠테이션 설계 (스토리라인, 슬라이드 구성)
│   ├── followup-manager.md      — 팔로업 관리 (일정, 이메일, 이의 대응)
│   └── sales-reviewer.md        — 교차 검증 (고객↔제안서↔PT↔팔로업 정합성)
├── skills/
│   ├── sales-enablement/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── roi-calculator/
│   │   └── SKILL.md             — ROI 계산 (TCO, Payback, 가치 정량화)
│   └── objection-handler/
│       └── SKILL.md             — 이의 대응 (BANT+C, LAER, 협상 전략)
└── README.md                    — 이 파일
```

## 사용법

`/sales-enablement` 스킬을 트리거하거나, "영업 제안서 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_customer_analysis.md` — 고객 분석서
- `02_proposal.md` — 제안서
- `03_presentation.md` — 프레젠테이션 구성안
- `04_followup_plan.md` — 팔로업 계획서
- `05_review_report.md` — 리뷰 보고서
