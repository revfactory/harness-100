# Security Audit Harness

보안 감사의 취약점스캔→코드분석→침투테스트보고→개선권고를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── vulnerability-scanner.md  — 취약점 스캐너 (CVE, 의존성, 설정오류)
│   ├── code-analyst.md           — 코드 보안 분석 (SAST, 시큐어코딩, 패턴탐지)
│   ├── pentest-reporter.md       — 침투 테스트 보고 (공격시나리오, PoC, 영향분석)
│   ├── security-consultant.md    — 보안 컨설턴트 (개선권고, 로드맵, 프레임워크매핑)
│   └── audit-reviewer.md         — 감사 리뷰어 (교차검증, 위험등급조정, 최종보고서)
├── skills/
│   ├── security-audit/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── owasp-testing-guide/
│   │   └── SKILL.md              — OWASP Top 10 보안 테스트 가이드
│   ├── cve-analysis/
│   │   └── SKILL.md              — CVE 분석 및 의존성 취약점 관리 가이드
│   └── threat-modeling/
│       └── SKILL.md              — 위협 모델링 방법론 가이드
└── README.md                     — 이 파일
```

## 사용법

`/security-audit` 스킬을 트리거하거나, "보안 감사해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 감사 범위 및 사용자 입력 정리
- `01_vulnerability_scan.md` — 취약점 스캔 결과
- `02_code_analysis.md` — 코드 보안 분석 보고서
- `03_pentest_report.md` — 침투 테스트 시나리오 보고서
- `04_remediation_plan.md` — 개선 권고 및 로드맵
- `05_audit_report.md` — 최종 감사 보고서
