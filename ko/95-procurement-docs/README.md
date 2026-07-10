# Procurement Docs Harness

구매 문서세트 생성 하네스. 요구사항 정의부터 벤더 비교표, 평가 기준표, 계약 조건 검토, 검수 기준서까지 에이전트 팀이 협업하여 생성한다.

## 구조

```

├── agents/
│   ├── requirements-definer.md   — 구매 요구사항 정의 (사양서, 수량, 납기, 예산)
│   ├── vendor-comparator.md      — 벤더 비교 분석 (후보 조사, 비교표, 레퍼런스)
│   ├── evaluation-designer.md    — 평가 기준표 설계 (배점, 가중치)
│   ├── contract-reviewer.md      — 계약 조건 검토 (약관, 리스크, 협상포인트)
│   └── acceptance-builder.md     — 검수 기준서 작성 (검수항목, 합격기준)
├── skills/
│   ├── procurement-docs/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── vendor-scoring/
│   │   └── SKILL.md              — 벤더 평가 스코어카드 (vendor-comparator 확장)
│   └── contract-checklist/
│       └── SKILL.md              — 계약 검토 체크리스트 (contract-reviewer 확장)
└── README.md                     — 이 파일
```

## 사용법

`/procurement-docs` 스킬을 트리거하거나, "구매 문서 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 구매 요청 및 배경 정리
- `01_requirements_spec.md` — 구매 요구사항 정의서
- `02_vendor_comparison.md` — 벤더 비교 분석표
- `03_evaluation_criteria.md` — 평가 기준표
- `04_contract_review.md` — 계약 조건 검토서
- `05_acceptance_criteria.md` — 검수 기준서
- `06_procurement_summary.md` — 구매 종합 보고서
