# Chatbot Builder Harness

챗봇 구축의 의도분석→대화설계→NLU→통합→테스트를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── conversation-designer.md — 대화 설계 (시나리오, 플로우, 폴백 전략)
│   ├── nlu-developer.md         — NLU 개발 (의도분류, 엔티티추출, 컨텍스트관리)
│   ├── integration-engineer.md  — 통합 엔지니어 (채널연동, API, 백엔드)
│   ├── dialog-tester.md         — 대화 테스터 (시나리오 테스트, 엣지케이스, 품질검증)
│   └── persona-architect.md     — 페르소나 설계 (봇 성격, 톤, 브랜드 정합성)
├── skills/
│   ├── chatbot-builder/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── intent-taxonomy-builder/
│   │   └── SKILL.md             — 의도 분류 체계 (엔티티, 슬롯, 학습 데이터)
│   └── conversation-flow-validator/
│       └── SKILL.md             — 대화 흐름 검증 (결함 탐지, 테스트, 메트릭)
└── README.md                    — 이 파일
```

## 사용법

`/chatbot-builder` 스킬을 트리거하거나, "챗봇 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_persona_spec.md` — 봇 페르소나 명세
- `02_conversation_design.md` — 대화 설계서
- `03_nlu_config.md` — NLU 설정 및 학습 데이터
- `04_integration_spec.md` — 통합 명세서
- `05_test_report.md` — 테스트 보고서
- `src/` — 챗봇 소스코드
