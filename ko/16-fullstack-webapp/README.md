# Fullstack Web App Harness

풀스택 웹앱의 요구사항→설계→프론트엔드→백엔드→테스트→배포를 에이전트 팀이 협업하여 개발하는 하네스.

## 구조

```

├── agents/
│   ├── architect.md             — 시스템 설계 (요구사항 분석, 아키텍처, DB 모델링, API 설계)
│   ├── frontend-dev.md          — 프론트엔드 개발 (React/Next.js, UI 컴포넌트, 상태관리)
│   ├── backend-dev.md           — 백엔드 개발 (API 구현, DB, 인증, 비즈니스 로직)
│   ├── qa-engineer.md           — QA 엔지니어 (테스트 전략, 단위/통합/E2E 테스트)
│   └── devops-engineer.md       — DevOps 엔지니어 (CI/CD, 인프라, 배포, 모니터링)
├── skills/
│   ├── fullstack-webapp/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── component-patterns/
│   │   └── SKILL.md             — 프론트엔드 확장 (React 패턴, 상태관리, 폴더 구조)
│   └── api-security-checklist/
│       └── SKILL.md             — 백엔드 확장 (OWASP Top 10, 인증/인가, 보안 헤더)
└── README.md                    — 이 파일
```

## 사용법

`/fullstack-webapp` 스킬을 트리거하거나, "웹앱 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 프로젝트 루트에 직접 생성된다:
- `_workspace/00_input.md` — 사용자 입력 정리
- `_workspace/01_architecture.md` — 아키텍처 설계 문서
- `_workspace/02_api_spec.md` — API 명세
- `_workspace/03_db_schema.md` — DB 스키마
- `_workspace/04_test_plan.md` — 테스트 계획
- `_workspace/05_deploy_guide.md` — 배포 가이드
- `_workspace/06_review_report.md` — 리뷰 보고서
- `src/` — 소스 코드 (프론트엔드 + 백엔드)
