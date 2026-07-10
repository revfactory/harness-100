# Gov Funding Plan Harness

정부지원사업 사업계획서의 공고요건분석→기술성·사업성작성→예산편성→증빙준비→제출검증을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── announcement-analyst.md — 공고 분석가 (공고요건, 평가기준, 자격요건 분석)
│   ├── tech-writer.md          — 기술성 작성자 (기술 개발 내용, 차별성, 구현방안)
│   ├── biz-writer.md           — 사업성 작성자 (시장성, 사업화 전략, 기대효과)
│   ├── budget-planner.md       — 예산 편성자 (정부 예산 기준, 비목별 편성, 증빙)
│   └── submission-reviewer.md  — 제출 검증자 (교차 검증, 누락 확인, 감점 방지)
├── skills/
│   ├── gov-funding-plan/
│       └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── budget-standard-checker/
│   │   └── SKILL.md            — 예산 기준 검증 (비목별 규정, 사업별 기준)
│   └── scoring-optimizer/
│       └── SKILL.md            — 평가 고득점 (항목별 전략, 감점 방지, 키워드)
└── README.md                   — 이 파일
```

## 사용법

`/gov-funding-plan` 스킬을 트리거하거나, "정부지원사업 사업계획서 써줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_announcement_analysis.md` — 공고 요건 분석서
- `02_tech_proposal.md` — 기술성 파트
- `03_biz_proposal.md` — 사업성 파트
- `04_budget_plan.md` — 예산 편성서
- `05_review_report.md` — 제출 검증 보고서
