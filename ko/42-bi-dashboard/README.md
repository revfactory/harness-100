# BI Dashboard Harness

BI 대시보드 구축의 데이터웨어하우스 설계→KPI 정의→시각화→자동 보고를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── data-engineer.md       — 데이터 엔지니어 (웨어하우스 설계, ETL, 데이터모델링)
│   ├── kpi-designer.md        — KPI 설계자 (지표 정의, 계산 로직, 목표치 설정)
│   ├── dashboard-builder.md   — 대시보드 빌더 (시각화 설계, 레이아웃, 인터랙션)
│   ├── report-automator.md    — 보고서 자동화 (정기 보고, 알림 설정, 배포)
│   └── bi-reviewer.md         — BI 검증자 (데이터 정합성, 지표 검증, UX 검토)
├── skills/
│   ├── bi-dashboard/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── kpi-tree-builder/
│   │   └── SKILL.md           — KPI 트리 (분해 방법론, 도메인 템플릿, 임계값)
│   └── chart-selector/
│       └── SKILL.md           — 차트 선택 (의사결정 트리, 차트별 규칙, 레이아웃)
└── README.md                  — 이 파일
```

## 사용법

`/bi-dashboard` 스킬을 트리거하거나, "BI 대시보드 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_data_warehouse_design.md` — 데이터 웨어하우스 설계서
- `02_kpi_definition.md` — KPI 정의서
- `03_dashboard_spec.md` — 대시보드 시각화 명세
- `04_report_automation.md` — 자동 보고 설정서
- `05_review_report.md` — 검증 보고서
