# RFP Responder Harness

RFI/RFP 응답서 작성을 위한 요구사항 분석, 역량 매칭, 기술 제안, 가격 제안, 차별화 전략까지 에이전트 팀이 협업하는 하네스.

## 구조

```

├── agents/
│   ├── requirement-analyst.md    — 요구사항 분석
│   ├── capability-matcher.md     — 역량 매칭
│   ├── technical-proposer.md     — 기술 제안서 작성
│   ├── pricing-strategist.md     — 가격 제안
│   └── proposal-reviewer.md      — 교차 검증
├── skills/
│   ├── rfp-responder/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── win-theme-builder/
│   │   └── SKILL.md              — Win Theme 구축 (차별화 전략, Ghost Team 분석)
│   └── pricing-calculator/
│       └── SKILL.md              — 가격 산정 (SW 원가, FP/MM, 투찰 전략)
└── README.md                     — 이 파일
```

## 사용법

`/rfp-responder` 스킬을 트리거하거나, "RFP 응답서 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_requirement_analysis.md` — 요구사항 분석서
- `02_capability_matrix.md` — 역량 매칭 매트릭스
- `03_technical_proposal.md` — 기술 제안서
- `04_pricing_proposal.md` — 가격 제안서
- `05_differentiation_strategy.md` — 차별화 전략서
- `06_review_report.md` — 리뷰 보고서
