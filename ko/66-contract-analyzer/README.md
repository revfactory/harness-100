# Contract Analyzer Harness

계약서 분석·작성·검토·위험 평가를 에이전트 팀이 협업하여 수행하는 하네스.
조항 분석부터 리스크 평가, 비교 검토, 수정 제안까지 계약 관리 전 과정을 체계적으로 처리한다.

## 구조

```

├── agents/
│   ├── clause-analyst.md        — 조항 분석 (구조 파악, 조항별 해석, 법적 의미 분석)
│   ├── clause-drafter.md        — 조항 작성·수정 (표준 조항, 맞춤 조항, 수정안)
│   ├── risk-assessor.md         — 리스크 평가 (법적·사업적 위험, 불리 조항 식별)
│   ├── comparison-reviewer.md   — 비교 검토 (표준 계약 대비, 이전 버전 대비)
│   └── contract-coordinator.md  — 계약 조율 (종합 검토, 정합성 확인, 최종 의견)
├── skills/
│   ├── contract-analyzer/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── clause-risk-database/
│   │   └── SKILL.md             — 위험 조항 패턴 DB, 리스크 스코어링 (risk-assessor, clause-analyst용)
│   └── negotiation-playbook/
│       └── SKILL.md             — 협상 전략 플레이북, 수정안 문구 템플릿 (clause-drafter용)
└── README.md                    — 이 파일
```

## 사용법

`/contract-analyzer` 스킬을 트리거하거나, "계약서 검토해줘", "계약서 분석" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리 (계약 유형, 당사자, 요구사항)
- `01_clause_analysis.md` — 조항 분석서
- `02_draft_clauses.md` — 조항 작성/수정안
- `03_risk_assessment.md` — 리스크 평가 보고서
- `04_comparison_report.md` — 비교 검토 보고서
- `05_final_opinion.md` — 종합 법률 의견서

## 면책 고지

이 하네스는 법률 전문가의 조언을 대체하지 않습니다. 중요한 계약에 대해서는 반드시 자격 있는 변호사의 검토를 받으십시오.
