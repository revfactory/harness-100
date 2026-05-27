# Patent Drafter Harness

특허 명세서 작성 — 선행기술조사→청구항→명세서→도면설명을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── prior-art-researcher.md — 선행기술 조사원 (특허DB 검색, 선행기술 분석, 신규성·진보성 판단)
│   ├── claim-drafter.md        — 청구항 작성자 (독립항·종속항, 권리범위 설계, 청구항 전략)
│   ├── specification-writer.md — 명세서 작성자 (발명의 설명, 실시예, 기술적 효과)
│   ├── drawing-designer.md     — 도면 설계자 (도면 구성, 부호 설명, 플로우차트)
│   └── patent-reviewer.md     — 특허 검증자 (명세서-청구항 정합성, 기재불비 점검)
├── skills/
│   ├── patent-drafter/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── claim-drafting-patterns/
│   │   └── SKILL.md            — 청구항 작성 패턴, 권리범위 설계 (claim-drafter용)
│   └── prior-art-search-strategy/
│       └── SKILL.md            — 선행기술 검색 전략 (prior-art-researcher용)
└── README.md                   — 이 파일
```

## 사용법

`/patent-drafter` 스킬을 트리거하거나, "특허 명세서 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리 (발명 개요)
- `01_prior_art_report.md` — 선행기술 조사 보고서
- `02_claims.md` — 청구항 세트
- `03_specification.md` — 발명의 상세한 설명
- `04_drawings.md` — 도면 설명서
- `05_review_report.md` — 검증 보고서
