# Audit Report Harness

내부감사 보고서 생성 하네스. 감사 범위 설정부터 체크리스트 작성, 발견사항 정리, 개선 권고, 추적 대장까지 에이전트 팀이 협업하여 생성한다.

## 구조

```

├── agents/
│   ├── scope-designer.md       — 감사 범위 설계 (목표, 기준, 대상, 일정)
│   ├── checklist-builder.md    — 감사 체크리스트 작성 (통제항목, 테스트절차)
│   ├── findings-analyst.md     — 발견사항 분석 (위험등급, 근본원인, 영향평가)
│   ├── recommendation-writer.md — 개선 권고 작성 (시정조치, 이행계획)
│   └── tracking-manager.md    — 추적 대장 관리 (이행현황, 후속조치)
├── skills/
│   ├── audit-report/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── internal-control-framework/
│   │   └── SKILL.md           — 내부통제 프레임워크 (scope-designer 확장)
│   └── finding-classification/
│       └── SKILL.md           — 발견사항 분류 (findings-analyst 확장)
└── README.md                  — 이 파일
```

## 사용법

`/audit-report` 스킬을 트리거하거나, "내부감사 보고서 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 감사 요청 및 배경 정리
- `01_audit_scope.md` — 감사 범위 및 계획
- `02_audit_checklist.md` — 감사 체크리스트
- `03_audit_findings.md` — 발견사항 보고서
- `04_recommendations.md` — 개선 권고안
- `05_tracking_ledger.md` — 이행 추적 대장
- `06_final_report.md` — 종합 감사 보고서
