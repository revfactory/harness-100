# Brand Identity Harness

브랜드 아이덴티티의 네이밍→슬로건→톤앤매너→가이드라인을 에이전트 팀이 협업하여 설계하는 하네스.

## 구조

```

├── agents/
│   ├── naming-specialist.md    — 네이밍 전문가 (브랜드명, 도메인, 상표 검토)
│   ├── copywriter.md           — 카피라이터 (슬로건, 태그라인, 브랜드 스토리)
│   ├── visual-director.md      — 비주얼 디렉터 (컬러, 타이포, 로고 컨셉)
│   ├── brand-strategist.md     — 브랜드 전략가 (포지셔닝, 타깃, 경쟁 분석)
│   └── identity-reviewer.md    — 아이덴티티 검증자 (교차 검증, 정합성 확인)
├── skills/
│   ├── brand-identity/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── naming-methodology/
│   │   └── SKILL.md            — naming-specialist 확장 (12 기법, SMILE 평가, 음운론)
│   ├── color-psychology/
│   │   └── SKILL.md            — visual-director 확장 (색상 심리, 60-30-10, 접근성)
│   └── brand-archetype/
│       └── SKILL.md            — brand-strategist+copywriter 확장 (12 아키타입, 톤앤보이스)
└── README.md                   — 이 파일
```

## 사용법

`/brand-identity` 스킬을 트리거하거나, "브랜드 아이덴티티 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_brand_strategy.md` — 브랜드 전략 보고서
- `02_naming_candidates.md` — 네이밍 후보
- `03_verbal_identity.md` — 버벌 아이덴티티 (슬로건, 톤앤매너)
- `04_visual_identity.md` — 비주얼 아이덴티티 (컬러, 타이포, 로고)
- `05_review_report.md` — 리뷰 보고서
