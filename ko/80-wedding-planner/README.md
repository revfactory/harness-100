# Wedding Planner Harness

결혼 준비 종합의 타임라인설계→예산관리표→업체비교표→체크리스트→청첩장문구를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── timeline-designer.md   — 타임라인 설계 (D-day 역산, 월별 할 일)
│   ├── budget-controller.md   — 예산 관리 (항목별 배분, 추적, 절감)
│   ├── vendor-analyst.md      — 업체 비교 (웨딩홀·스드메·허니문 조사)
│   ├── checklist-builder.md   — 체크리스트 + 청첩장 (할 일, 문구 작성)
│   └── wedding-reviewer.md   — 교차 검증 (타임라인↔예산↔업체↔체크리스트 정합성)
├── skills/
│   ├── wedding-planner/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── vendor-negotiation-guide/
│   │   └── SKILL.md           — 웨딩 업체 비교·협상 가이드 (vendor-analyst용)
│   └── wedding-budget-optimizer/
│       └── SKILL.md           — 결혼 예산 최적화 (budget-controller용)
└── README.md                  — 이 파일
```

## 사용법

`/wedding-planner` 스킬을 트리거하거나, "결혼 준비 도와줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_timeline.md` — 결혼 준비 타임라인
- `02_budget.md` — 예산 관리표
- `03_vendor_comparison.md` — 업체 비교표
- `04_checklist_invitation.md` — 체크리스트 + 청첩장 문구
- `05_review_report.md` — 리뷰 보고서
