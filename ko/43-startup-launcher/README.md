# Startup Launcher Harness

스타트업 런칭의 아이디어 검증→비즈니스 모델→MVP→피칭→투자 유치를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── market-analyst.md      — 시장 분석가 (아이디어 검증, TAM/SAM/SOM, 경쟁분석)
│   ├── business-modeler.md    — 비즈니스 모델러 (BMC, 수익모델, 유닛이코노믹스)
│   ├── mvp-architect.md       — MVP 설계자 (기능 우선순위, 기술스택, 로드맵)
│   ├── pitch-creator.md       — 피치덱 작성자 (투자자 프레젠테이션, 스토리라인)
│   └── launch-reviewer.md     — 런칭 검증자 (전체 일관성, 투자 준비도 평가)
├── skills/
│   ├── startup-launcher/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── unit-economics-calculator/
│   │   └── SKILL.md           — 유닛이코노믹스 (LTV/CAC/BEP, 벤치마크)
│   └── pitch-deck-framework/
│       └── SKILL.md           — 피치덱 프레임워크 (10-슬라이드, Q&A 대비)
└── README.md                  — 이 파일
```

## 사용법

`/startup-launcher` 스킬을 트리거하거나, "스타트업 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_market_validation.md` — 시장 검증 보고서
- `02_business_model.md` — 비즈니스 모델 설계서
- `03_mvp_blueprint.md` — MVP 설계도
- `04_pitch_deck.md` — 피치덱
- `05_review_report.md` — 런칭 검증 보고서
