# Regulatory Filing Harness

인허가·신고서류의 요건조사→구비서류목록→신청서작성→첨부자료준비→제출체크리스트를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── requirements-investigator.md — 요건 조사 (법령근거, 관할기관, 허가요건, 기간·수수료)
│   ├── document-drafter.md          — 서류 작성 (신청서, 사업계획서, 각종 양식)
│   ├── attachment-preparer.md       — 첨부자료 준비 (증빙서류, 도면, 인증서 등)
│   └── submission-verifier.md       — 제출 검증 (완전성 확인, 보정사항 점검, 체크리스트)
├── skills/
│   ├── regulatory-filing/
│   │   └── SKILL.md                 — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── permit-requirements-db/
│   │   └── SKILL.md                 — 업종별 인허가 요건 DB (requirements-investigator용)
│   └── form-filling-guide/
│       └── SKILL.md                 — 행정 서식 기재 가이드 (document-drafter용)
└── README.md                        — 이 파일
```

## 사용법

`/regulatory-filing` 스킬을 트리거하거나, "인허가 서류 준비해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_requirements_research.md` — 요건 조사 보고서
- `02_document_list.md` — 구비서류 목록
- `03_application_draft.md` — 신청서 초안
- `04_attachments_guide.md` — 첨부자료 준비 가이드
- `05_submission_checklist.md` — 제출 체크리스트 및 검증 보고서
