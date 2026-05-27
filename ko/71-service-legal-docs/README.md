# Service Legal Docs Harness

서비스 법무문서 세트 — 이용약관→개인정보처리방침→쿠키정책→환불정책→저작권고지 일체를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── tos-specialist.md        — 약관 전문가 (이용약관 작성, 불공정약관 방지, 책임제한)
│   ├── privacy-specialist.md    — 개인정보 전문가 (처리방침, 쿠키정책, 동의체계)
│   ├── consumer-analyst.md      — 소비자보호 분석가 (환불정책, 소비자권익, 전자상거래법)
│   └── consistency-reviewer.md  — 정합성 검증자 (문서 간 일관성, 법적 정합성, 최종 QA)
├── skills/
│   ├── service-legal-docs/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── unfair-terms-detector/
│   │   └── SKILL.md             — 불공정약관 감지·수정 (tos-specialist용)
│   └── cross-document-linker/
│       └── SKILL.md             — 문서 간 교차 참조·정합성 관리 (consistency-reviewer용)
└── README.md                    — 이 파일
```

## 사용법

`/service-legal-docs` 스킬을 트리거하거나, "서비스 약관 세트 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_terms_of_service.md` — 이용약관
- `02_privacy_policy.md` — 개인정보처리방침
- `03_cookie_policy.md` — 쿠키 정책
- `04_refund_policy.md` — 환불 정책
- `05_copyright_notice.md` — 저작권 고지
- `06_review_report.md` — 정합성 검증 보고서
