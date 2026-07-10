# Customer Support Harness

고객지원 시스템 구축: FAQ→응대매뉴얼→에스컬레이션→분석을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── faq-builder.md           — FAQ 구축 (질문 수집·분류, 답변 작성, 검색 최적화)
│   ├── response-specialist.md   — 응대 매뉴얼 (시나리오별 스크립트, 톤앤매너)
│   ├── escalation-manager.md    — 에스컬레이션 (단계 설계, 라우팅, SLA)
│   ├── cs-analyst.md            — CS 분석 (메트릭, 트렌드, 개선 제안)
│   └── cs-reviewer.md           — 교차 검증 (FAQ↔매뉴얼↔에스컬레이션↔분석 정합성)
├── skills/
│   ├── customer-support/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── csat-analyzer/
│   │   └── SKILL.md             — CSAT 분석 (NPS/CES, VOC, CS 대시보드)
│   └── escalation-flowchart/
│       └── SKILL.md             — 에스컬레이션 설계 (L1/L2/L3, SLA, 위기 대응)
└── README.md                    — 이 파일
```

## 사용법

`/customer-support` 스킬을 트리거하거나, "고객지원 시스템 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_faq.md` — FAQ 문서
- `02_response_manual.md` — 응대 매뉴얼
- `03_escalation_policy.md` — 에스컬레이션 정책
- `04_cs_analytics.md` — CS 분석 프레임워크
- `05_review_report.md` — 리뷰 보고서
