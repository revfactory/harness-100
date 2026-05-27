# Compliance Checker Harness

규정 준수 검증 — 법률매핑→현황진단→갭분석→개선계획을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── law-mapper.md           — 법률 분석가 (관련 법규 식별, 조항 매핑, 의무사항 추출)
│   ├── status-auditor.md       — 현황 진단자 (조직 현황 조사, 증거 수집, 준수 현황 평가)
│   ├── gap-analyst.md          — 갭 분석가 (법적 요구↔현황 비교, 리스크 산정, 우선순위 도출)
│   └── remediation-planner.md  — 개선 계획 수립자 (시정 조치, 일정 수립, 모니터링 체계)
├── skills/
│   ├── compliance-checker/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── regulation-knowledge-base/
│   │   └── SKILL.md            — 업종별 규제 법령 DB (law-mapper, gap-analyst용)
│   └── audit-checklist-engine/
│       └── SKILL.md            — 감사 체크리스트 생성 엔진 (status-auditor용)
└── README.md                   — 이 파일
```

## 사용법

`/compliance-checker` 스킬을 트리거하거나, "규정 준수 점검해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_law_mapping.md` — 법률 매핑 보고서
- `02_status_audit.md` — 현황 진단 보고서
- `03_gap_analysis.md` — 갭 분석 보고서
- `04_remediation_plan.md` — 개선 계획서
