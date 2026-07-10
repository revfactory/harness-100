# Incident Postmortem Harness

장애 사후분석 보고서를 에이전트 팀이 협업하여 생성하는 하네스. 타임라인 재구성→근본원인 분석→영향범위 산정→재발방지 대책→보고서 생성 파이프라인을 자동화한다.

## 구조

```

├── agents/
│   ├── timeline-reconstructor.md — 타임라인 재구성 (이벤트 수집, 시간순 정렬, 갭 식별)
│   ├── root-cause-investigator.md — 근본원인 조사 (5 Whys, 피시본, Fault Tree)
│   ├── impact-assessor.md        — 영향범위 산정 (사용자, 매출, SLA, 평판)
│   ├── remediation-planner.md    — 재발방지 대책 (단기/중기/장기, 오너십, KPI)
│   └── postmortem-reviewer.md    — 교차 검증 (타임라인↔원인↔영향↔대책 정합성)
├── skills/
│   ├── incident-postmortem/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── rca-methodology/
│   │   └── SKILL.md              — 근본원인 분석 방법론 가이드
│   └── sla-impact-calculator/
│       └── SKILL.md              — SLA/SLO 기반 영향도 산정 가이드
└── README.md                     — 이 파일
```

## 사용법

`/incident-postmortem` 스킬을 트리거하거나, "장애 포스트모텀 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_timeline.md` — 장애 타임라인
- `02_root_cause.md` — 근본원인 분석
- `03_impact_assessment.md` — 영향범위 산정
- `04_remediation_plan.md` — 재발방지 대책
- `05_review_report.md` — 리뷰 보고서
- `postmortem_report.md` — 최종 통합 포스트모텀 보고서
