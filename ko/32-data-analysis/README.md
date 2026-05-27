# Data Analysis Harness

데이터 분석 프로젝트의 탐색→정제→분석→시각화→보고서를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── explorer.md          — 탐색 분석 (데이터 프로파일링, 분포 파악, 이상치 탐지)
│   ├── cleaner.md           — 데이터 정제 (결측치, 이상치, 타입변환, 정규화)
│   ├── analyst.md           — 통계 분석 (가설검정, 상관분석, 회귀, 클러스터링)
│   ├── visualizer.md        — 시각화 (차트 설계, 대시보드 레이아웃, 인터랙션)
│   └── reporter.md          — 보고서 작성 (인사이트 종합, 경영진 요약, 권고안)
├── skills/
│   ├── data-analysis/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── statistical-tests-selector/
│   │   └── SKILL.md              — 통계 검정 선택 가이드
│   └── visualization-chooser/
│       └── SKILL.md              — 시각화 유형 선택 매트릭스 가이드
└── README.md                — 이 파일
```

## 사용법

`/data-analysis` 스킬을 트리거하거나, "데이터 분석해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 데이터 소스 정리
- `01_exploration_report.md` — 탐색적 데이터 분석(EDA) 결과
- `02_cleaning_log.md` — 정제 작업 로그 및 변환 코드
- `03_analysis_results.md` — 통계 분석 결과
- `04_visualizations.md` — 시각화 컨셉 및 코드
- `05_final_report.md` — 최종 분석 보고서
- `scripts/` — 재현 가능한 분석 스크립트
