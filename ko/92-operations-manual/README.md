# Operations Manual Harness

업무 매뉴얼 자동 생성 하네스. 기존 문서/코드를 분석하여 프로세스 플로차트, 단계별 매뉴얼, FAQ, 교육자료를 에이전트 팀이 협업하여 생성한다.

## 구조

```

├── agents/
│   ├── document-analyst.md    — 기존 문서·코드 분석 (구조파악, 프로세스추출, 용어정리)
│   ├── flowchart-designer.md  — 프로세스 플로차트 설계 (Mermaid 다이어그램, 분기로직)
│   ├── manual-writer.md       — 단계별 매뉴얼 작성 (절차서, 스크린샷가이드, 체크리스트)
│   ├── faq-builder.md         — FAQ 및 트러블슈팅 가이드 작성
│   └── training-producer.md   — 교육자료 제작 (퀴즈, 실습과제, 요약카드)
├── skills/
│   ├── operations-manual/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── flowchart-standards/
│   │   └── SKILL.md           — 프로세스 플로차트 표준 (flowchart-designer 확장)
│   └── knowledge-base-design/
│       └── SKILL.md           — 지식 베이스 구축 가이드 (faq-builder 확장)
└── README.md                  — 이 파일
```

## 사용법

`/operations-manual` 스킬을 트리거하거나, "업무 매뉴얼 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 분석 대상 정리
- `01_document_analysis.md` — 기존 문서/코드 분석 결과
- `02_process_flowcharts.md` — 프로세스 플로차트 (Mermaid)
- `03_step_by_step_manual.md` — 단계별 업무 매뉴얼
- `04_faq_troubleshooting.md` — FAQ 및 트러블슈팅 가이드
- `05_training_materials.md` — 교육자료 패키지
- `06_review_report.md` — 통합 검증 보고서
