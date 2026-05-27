# Legal Research Harness

법률 리서치 — 판례검색→법리분석→의견서→전략수립을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── case-searcher.md        — 판례 검색자 (관련 판례 발굴, 판례 요지 정리, 트렌드 분석)
│   ├── legal-analyst.md        — 법리 분석가 (법적 쟁점 도출, 판례 법리 분석, 학설 검토)
│   ├── opinion-writer.md       — 의견서 작성자 (법률 의견서, 논리 구성, 근거 정리)
│   └── strategy-advisor.md     — 전략 수립자 (소송/분쟁 전략, 대응 방안, 리스크 평가)
├── skills/
│   ├── legal-research/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── case-analysis-framework/
│   │   └── SKILL.md            — 판례 분석 프레임워크 (case-searcher, legal-analyst용)
│   └── legal-writing-methodology/
│       └── SKILL.md            — 법률 문서 작성 방법론 (opinion-writer용)
└── README.md                   — 이 파일
```

## 사용법

`/legal-research` 스킬을 트리거하거나, "법률 리서치 해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리 (법률 이슈)
- `01_case_search.md` — 판례 검색 보고서
- `02_legal_analysis.md` — 법리 분석 보고서
- `03_legal_opinion.md` — 법률 의견서
- `04_legal_strategy.md` — 전략 수립 보고서
