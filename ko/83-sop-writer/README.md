# SOP Writer Harness

표준운영절차(SOP)의 프로세스분석→절차서→체크리스트→교육자료→버전관리를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── process-analyst.md      — 프로세스 분석 (현행 업무 흐름 분석, 병목 식별)
│   ├── procedure-writer.md     — 절차서 작성 (단계별 절차, 의사결정 분기)
│   ├── checklist-designer.md   — 체크리스트 설계 (실행 점검표, 품질 게이트)
│   ├── training-developer.md   — 교육자료 제작 (학습 가이드, 평가 문항)
│   └── version-controller.md   — 버전 관리 및 교차 검증 (변경 이력, 정합성 확인)
├── skills/
│   ├── sop-writer/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── process-mapping/
│   │   └── SKILL.md           — 프로세스 매핑 방법론 (process-analyst 확장)
│   └── checklist-design/
│       └── SKILL.md           — 체크리스트 설계 원칙 (checklist-designer 확장)
└── README.md                  — 이 파일
```

## 사용법

`/sop-writer` 스킬을 트리거하거나, "SOP 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_process_analysis.md` — 프로세스 분석 결과
- `02_procedure_document.md` — 표준 절차서
- `03_checklists.md` — 체크리스트 세트
- `04_training_materials.md` — 교육자료
- `05_version_control.md` — 버전 관리 및 검증 보고서
