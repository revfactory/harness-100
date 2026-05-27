# Report Generator Harness

업무 보고서의 데이터수집→분석→시각화→집필→요약을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── data-collector.md      — 데이터 수집 (소스 탐색, 수치 추출, 정제)
│   ├── analyst.md             — 데이터 분석 (통계, 트렌드, 인사이트 도출)
│   ├── visualizer.md          — 시각화 설계 (차트, 테이블, 인포그래픽 명세)
│   ├── report-writer.md       — 보고서 집필 (구조화된 보고서 작성)
│   └── executive-summarizer.md — 요약 및 교차 검증 (핵심 요약, 정합성 확인)
├── skills/
│   ├── report-generator/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── data-visualization-guide/
│   │   └── SKILL.md           — 데이터 시각화 가이드 (visualizer 확장)
│   └── kpi-dashboard-patterns/
│       └── SKILL.md           — KPI 대시보드 설계 패턴 (analyst 확장)
└── README.md                  — 이 파일
```

## 사용법

`/report-generator` 스킬을 트리거하거나, "업무 보고서 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_data_collection.md` — 수집된 데이터 정리
- `02_analysis_report.md` — 분석 결과
- `03_visualization_spec.md` — 시각화 명세
- `04_full_report.md` — 최종 보고서
- `05_executive_summary.md` — 경영진 요약 및 검증 보고
