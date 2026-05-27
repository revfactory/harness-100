# Privacy Engineer Harness

개인정보보호 엔지니어링 — GDPR/PIPA 분석→PIA→동의서→프로세스설계를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── privacy-law-analyst.md   — 법률 분석가 (GDPR/PIPA/개인정보보호법 분석, 적용 범위 판단)
│   ├── pia-assessor.md          — PIA 수행자 (개인정보 영향평가, 위험도 산정, 보호 조치)
│   ├── consent-designer.md     — 동의서 작성자 (동의서 설계, 고지사항, 처리방침)
│   └── process-architect.md    — 프로세스 설계자 (개인정보 처리 프로세스, 기술적 보호조치)
├── skills/
│   ├── privacy-engineer/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── data-flow-mapper/
│   │   └── SKILL.md            — 데이터 플로우 매핑 (pia-assessor, process-architect용)
│   └── gdpr-pipa-cross-reference/
│       └── SKILL.md            — GDPR·PIPA 교차 참조 (privacy-law-analyst용)
└── README.md                   — 이 파일
```

## 사용법

`/privacy-engineer` 스킬을 트리거하거나, "개인정보보호 체계 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_privacy_law_analysis.md` — 법률 분석 보고서
- `02_pia_report.md` — 개인정보 영향평가 보고서
- `03_consent_documents.md` — 동의서·고지사항 세트
- `04_process_design.md` — 개인정보 처리 프로세스 설계서
