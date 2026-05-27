# CI/CD Pipeline Harness

CI/CD 파이프라인의 설계·구축·모니터링·최적화를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── pipeline-designer.md     — 파이프라인 설계 (스테이지, 트리거, 브랜치 전략)
│   ├── infra-engineer.md        — 인프라 구성 (러너, 컨테이너, 환경변수, 시크릿)
│   ├── monitoring-specialist.md — 모니터링 (메트릭, 알림, 대시보드, SLA)
│   ├── security-scanner.md      — 보안 스캔 (SAST, DAST, 의존성, 컨테이너)
│   └── pipeline-reviewer.md     — 파이프라인 리뷰 (효율성, 안정성, 보안, 정합성)
├── skills/
│   ├── cicd-pipeline/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── pipeline-security-gates/
│   │   └── SKILL.md              — 보안스캐너 확장 (SAST/SCA/시크릿 도구, 게이트 배치, 임계값)
│   └── deployment-strategies/
│       └── SKILL.md              — 파이프라인설계자 확장 (Blue-Green/Canary/Rolling, DORA)
└── README.md                     — 이 파일
```

## 사용법

`/cicd-pipeline` 스킬을 트리거하거나, "CI/CD 파이프라인 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_pipeline_design.md` — 파이프라인 설계 문서
- `02_pipeline_config/` — 파이프라인 설정 파일 (YAML 등)
- `03_monitoring.md` — 모니터링 설계 문서
- `04_security_scan.md` — 보안 스캔 설정 및 보고서
- `05_review_report.md` — 파이프라인 리뷰 보고서
