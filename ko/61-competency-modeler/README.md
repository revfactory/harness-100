# Competency Modeler Harness

역량 모델링의 직무분석→역량사전작성→평가루브릭설계→개발계획수립→역량매트릭스를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── job-analyst.md            — 직무 분석가 (직무기술서, 과업분석, KSA도출)
│   ├── competency-architect.md   — 역량사전 작성자 (역량정의, 행동지표, 수준체계)
│   ├── rubric-designer.md        — 루브릭 설계자 (평가기준, 채점표, 평가도구)
│   └── development-planner.md    — 개발계획 수립자 (역량개발, 학습경로, 매트릭스)
├── skills/
│   ├── competency-modeler/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── bars-assessment/
│   │   └── SKILL.md              — BARS 평가 설계 (행동 앵커, BEI 질문, SJT 문항)
│   └── ksa-taxonomy/
│       └── SKILL.md              — KSA 분류 체계 (NCS/O*NET 매핑, 역량 수준, JD 표준)
└── README.md                     — 이 파일
```

## 사용법

`/competency-modeler` 스킬을 트리거하거나, "역량 모델 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_job_analysis.md` — 직무 분석서
- `02_competency_dictionary.md` — 역량 사전
- `03_assessment_rubric.md` — 평가 루브릭
- `04_development_plan.md` — 역량 개발 계획서
- `05_competency_matrix.md` — 역량 매트릭스
