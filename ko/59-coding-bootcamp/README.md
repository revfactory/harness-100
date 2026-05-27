# Coding Bootcamp Harness

코딩 교육의 커리큘럼설계→실습과제→코드리뷰→프로젝트→포트폴리오를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── curriculum-designer.md  — 커리큘럼 설계 (학습경로, 단계별 목표)
│   ├── exercise-creator.md     — 실습과제 출제 (난이도별 문제, 테스트케이스)
│   ├── code-reviewer.md        — 코드 리뷰 (품질, 패턴, 개선점)
│   └── mentor.md               — 멘토 (프로젝트 설계, 포트폴리오, 커리어)
├── skills/
│   ├── coding-bootcamp/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── code-kata-generator/
│   │   └── SKILL.md            — 코딩 과제 설계 (5-Tier 난이도, 테스트케이스, 스캐폴딩)
│   └── tech-interview-prep/
│       └── SKILL.md            — 기술 면접 준비 (UMPIRE, 시스템 디자인, STAR 행동면접)
└── README.md                   — 이 파일
```

## 사용법

`/coding-bootcamp` 스킬을 트리거하거나, "코딩 배우고 싶어" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_curriculum.md` — 커리큘럼
- `02_exercises/` — 실습과제 디렉토리
- `03_code_review.md` — 코드 리뷰 보고서
- `04_project_spec.md` — 프로젝트 기획서
- `05_portfolio_guide.md` — 포트폴리오 가이드
