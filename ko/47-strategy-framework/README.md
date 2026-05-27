# Strategy Framework Harness

조직의 전략 프레임워크를 OKR설계→BSC매핑→SWOT분석→비전·미션선언문→전략실행로드맵 순으로 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── okr-designer.md          — OKR 설계 (목표·핵심결과 구조화, 정렬)
│   ├── bsc-analyst.md           — BSC 매핑 (4대 관점 연계, KPI 설계)
│   ├── swot-specialist.md       — SWOT 분석 (내외부 환경, 전략 매트릭스)
│   ├── strategy-writer.md       — 전략 문서 (비전·미션, 로드맵 작성)
│   └── strategy-reviewer.md     — 교차 검증 (OKR↔BSC↔SWOT↔문서 정합성)
├── skills/
│   ├── strategy-framework/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── okr-quality-checker/
│   │   └── SKILL.md             — OKR 품질 검증 (QSIM/SMART-V, 정렬, 안티패턴)
│   └── tows-matrix-builder/
│       └── SKILL.md             — TOWS 매트릭스 (SO/WO/ST/WT 전략, 우선순위)
└── README.md                    — 이 파일
```

## 사용법

`/strategy-framework` 스킬을 트리거하거나, "전략 프레임워크 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_okr_design.md` — OKR 설계서
- `02_bsc_mapping.md` — BSC 매핑표
- `03_swot_analysis.md` — SWOT 분석서
- `04_vision_mission.md` — 비전·미션 선언문
- `05_strategy_roadmap.md` — 전략 실행 로드맵
- `06_review_report.md` — 리뷰 보고서
