# Grant Writer Harness

보조금 및 지원사업 신청을 위한 공고 분석, 사업계획 작성, 예산 편성, 제출 검증까지 에이전트 팀이 협업하는 하네스.

## 구조

```

├── agents/
│   ├── announcement-analyst.md   — 공고 분석 (자격 요건, 평가 기준, 핵심 키워드 추출)
│   ├── plan-writer.md            — 사업계획서 작성 (사업 개요, 추진 전략, 기대 효과)
│   ├── budget-designer.md        — 예산 편성 (비목별 산정, 대응 자금, 집행 계획)
│   ├── submission-verifier.md    — 제출 검증 (서류 완비, 자격 체크, 오류 검출)
│   └── compliance-checker.md     — 규정 준수 검증 (공고 요건 매칭, 배점 최적화)
├── skills/
│   ├── grant-writer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── scoring-optimizer/
│   │   └── SKILL.md              — 배점 최적화 (평가 기준 해부, 탈락 방지, 가점 전략)
│   └── budget-rule-engine/
│       └── SKILL.md              — 예산 규정 엔진 (비목별 상한, 인건비 단가, 정산 가이드)
└── README.md                     — 이 파일
```

## 사용법

`/grant-writer` 스킬을 트리거하거나, "보조금 신청서 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_announcement_analysis.md` — 공고 분석서
- `02_business_plan.md` — 사업계획서
- `03_budget_plan.md` — 예산 편성서
- `04_compliance_report.md` — 규정 준수 보고서
- `05_submission_checklist.md` — 제출 체크리스트
- `06_review_report.md` — 리뷰 보고서
