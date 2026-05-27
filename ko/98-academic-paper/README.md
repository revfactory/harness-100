# Academic Paper Harness

학술 논문 작성의 연구설계→실험→분석→집필→투고준비를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── research-designer.md    — 연구 설계자 (연구 질문, 가설, 방법론)
│   ├── experiment-manager.md   — 실험 관리자 (프로토콜, 데이터 수집)
│   ├── statistical-analyst.md  — 통계 분석가 (분석, 시각화, 해석)
│   ├── paper-writer.md         — 논문 작성자 (구조, 집필, 레퍼런스)
│   └── submission-preparer.md  — 투고 준비자 (저널 선정, 포맷팅)
├── skills/
│   ├── academic-paper/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── research-methodology/
│   │   └── SKILL.md            — 연구 방법론 가이드 (research-designer 확장)
│   └── citation-standards/
│       └── SKILL.md            — 학술 인용 표준 (paper-writer 확장)
└── README.md                   — 이 파일
```

## 사용법

`/academic-paper` 스킬을 트리거하거나, "학술 논문 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_research_design.md` — 연구 설계서
- `02_experiment_protocol.md` — 실험 프로토콜
- `03_analysis_report.md` — 분석 보고서
- `04_manuscript.md` — 논문 원고
- `05_submission_package.md` — 투고 패키지
- `06_review_report.md` — 통합 리뷰 보고서
