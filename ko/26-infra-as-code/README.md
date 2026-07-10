# Infra as Code Harness

Infrastructure as Code(IaC) 설계 및 구현을 에이전트 팀이 협업하여 수행하는 하네스. Terraform/Pulumi 기반 환경 구성, 보안, 비용 최적화 파이프라인을 자동화한다.

## 구조

```

├── agents/
│   ├── infra-architect.md        — 인프라 설계 (아키텍처, 모듈 구조, 환경 분리)
│   ├── security-engineer.md      — 보안 엔지니어 (IAM, 네트워크, 암호화, 컴플라이언스)
│   ├── cost-optimizer.md         — 비용 최적화 (리소스 사이징, 예약, FinOps)
│   ├── drift-detector.md         — 드리프트 감지 (상태 검증, 정책 준수, 자동 교정)
│   └── iac-reviewer.md           — 교차 검증 (설계↔보안↔비용↔드리프트 정합성)
├── skills/
│   ├── infra-as-code/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── terraform-module-patterns/
│   │   └── SKILL.md              — Terraform 모듈 설계 패턴 가이드
│   └── cloud-cost-models/
│       └── SKILL.md              — 클라우드 비용 모델 및 FinOps 가이드
└── README.md                     — 이 파일
```

## 사용법

`/infra-as-code` 스킬을 트리거하거나, "인프라 코드 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_infra_design.md` — 인프라 설계서
- `02_security_design.md` — 보안 설계서
- `03_cost_analysis.md` — 비용 분석 보고서
- `04_drift_policy.md` — 드리프트 감지 정책
- `05_review_report.md` — 최종 리뷰 보고서
