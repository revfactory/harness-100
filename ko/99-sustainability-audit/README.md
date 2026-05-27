# Sustainability Audit Harness

ESG/지속가능성 감사의 환경→사회→거버넌스→보고서→개선계획을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── environmental-analyst.md  — 환경 분석가 (탄소배출, 에너지, 폐기물)
│   ├── social-assessor.md        — 사회 영향 평가자 (노동, 인권, 지역사회)
│   ├── governance-reviewer.md    — 거버넌스 검토자 (이사회, 윤리, 컴플라이언스)
│   ├── esg-reporter.md           — ESG 보고서 작성자 (GRI, SASB, TCFD)
│   └── improvement-planner.md    — 개선 계획 수립자 (로드맵, KPI, 우선순위)
├── skills/
│   ├── sustainability-audit/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── ghg-protocol/
│   │   └── SKILL.md              — GHG Protocol 가이드 (environmental-analyst 확장)
│   └── materiality-assessment/
│       └── SKILL.md              — 중대성 평가 매트릭스 (esg-reporter 확장)
└── README.md                     — 이 파일
```

## 사용법

`/sustainability-audit` 스킬을 트리거하거나, "ESG 감사 해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_environmental_assessment.md` — 환경(E) 평가서
- `02_social_assessment.md` — 사회(S) 평가서
- `03_governance_assessment.md` — 거버넌스(G) 평가서
- `04_esg_report.md` — 통합 ESG 보고서
- `05_improvement_plan.md` — 개선 계획서
- `06_review_report.md` — 교차 검증 보고서
