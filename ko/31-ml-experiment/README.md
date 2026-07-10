# ML Experiment Harness

ML 실험 관리의 데이터준비→모델설계→학습→평가→배포를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── data-engineer.md         — 데이터 엔지니어 (수집, 전처리, 피처엔지니어링, 분할)
│   ├── model-designer.md        — 모델 설계자 (아키텍처, 하이퍼파라미터, 손실함수)
│   ├── training-manager.md      — 학습 관리자 (실험추적, GPU관리, 체크포인트, 재현성)
│   ├── evaluation-analyst.md    — 평가 분석가 (메트릭, 편향검증, 해석가능성, A/B)
│   └── experiment-reviewer.md   — 실험 리뷰어 (교차검증, 논문품질, 재현성검증)
├── skills/
│   ├── ml-experiment/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── feature-engineering-cookbook/
│   │   └── SKILL.md              — 피처 엔지니어링 기법 카탈로그
│   ├── model-selection-guide/
│   │   └── SKILL.md              — ML 모델 선택 매트릭스 가이드
│   └── experiment-tracking-setup/
│       └── SKILL.md              — 실험 추적 및 재현성 가이드
└── README.md                    — 이 파일
```

## 사용법

`/ml-experiment` 스킬을 트리거하거나, "ML 실험 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_data_preparation.md` — 데이터 준비 계획 및 파이프라인
- `02_model_design.md` — 모델 아키텍처 설계
- `03_training_config.md` — 학습 설정 및 실험 추적
- `04_evaluation_report.md` — 평가 보고서
- `05_review_report.md` — 실험 리뷰 보고서
- `experiment_code/` — 실험 구현 코드
