# Proposal Writer Harness

제안서의 고객분석→솔루션설계→가격→차별화→디자인을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── client-analyst.md        — 고객 분석 (니즈, 의사결정구조, 경쟁상황)
│   ├── solution-architect.md    — 솔루션 설계 (기술/서비스 구성, 구현 계획)
│   ├── pricing-strategist.md    — 가격 전략 (원가, 가격 모델, ROI)
│   ├── differentiator.md        — 차별화 전략 (USP, 경쟁우위, 레퍼런스)
│   └── proposal-designer.md     — 제안서 통합 및 교차 검증 (구성, 디자인, QA)
├── skills/
│   ├── proposal-writer/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── roi-calculator/
│   │   └── SKILL.md             — ROI 산출 프레임워크 (pricing-strategist 확장)
│   └── win-theme-builder/
│       └── SKILL.md             — Win Theme 구축 (differentiator 확장)
└── README.md                    — 이 파일
```

## 사용법

`/proposal-writer` 스킬을 트리거하거나, "제안서 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_client_analysis.md` — 고객 분석 보고서
- `02_solution_design.md` — 솔루션 설계서
- `03_pricing_model.md` — 가격 전략서
- `04_differentiation.md` — 차별화 전략서
- `05_final_proposal.md` — 최종 제안서 및 검증 보고서
