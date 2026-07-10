# LLM App Builder Harness

LLM 앱 개발의 프롬프트엔지니어링→RAG파이프라인설계→평가프레임워크→최적화→배포설정을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── prompt-engineer.md       — 프롬프트 엔지니어링 (시스템 프롬프트, few-shot, 가드레일)
│   ├── rag-architect.md         — RAG 파이프라인 설계 (임베딩, 검색, 청킹, 리랭킹)
│   ├── eval-specialist.md       — 평가 프레임워크 (벤치마크, A/B, 회귀 테스트)
│   ├── optimization-engineer.md — 최적화 (비용, 레이턴시, 품질 트레이드오프)
│   └── deploy-engineer.md       — 배포 설정 (API, 스케일링, 모니터링, 가드레일)
├── skills/
│   ├── llm-app-builder/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── prompt-optimizer/
│   │   └── SKILL.md             — 프롬프트 최적화 (CRISP, 가드레일, A/B 테스트)
│   └── chunking-strategy-guide/
│       └── SKILL.md             — 청킹 전략 (시맨틱 청킹, 문서별 전처리, 품질)
└── README.md                    — 이 파일
```

## 사용법

`/llm-app-builder` 스킬을 트리거하거나, "LLM 앱 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_prompt_design.md` — 프롬프트 설계서
- `02_rag_pipeline.md` — RAG 파이프라인 설계
- `03_eval_framework.md` — 평가 프레임워크
- `04_optimization.md` — 최적화 전략
- `05_deploy_config.md` — 배포 설정
- `src/` — 앱 소스코드
