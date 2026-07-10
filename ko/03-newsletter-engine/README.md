# Newsletter Engine Harness

뉴스레터 콘텐츠의 큐레이션→작성→A/B테스트→발송 최적화를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── curator.md             — 큐레이터 (소스 수집, 트렌드 분석, 콘텐츠 선별)
│   ├── copywriter.md          — 카피라이터 (헤드라인, 본문, CTA 작성)
│   ├── analyst.md             — 분석가 (A/B테스트 설계, 발송 최적화, 성과 예측)
│   ├── editor-in-chief.md     — 편집장 (톤 일관성, 브랜드 가이드, 최종 편집)
│   └── quality-reviewer.md    — 품질 검증자 (교차 검증, 정합성 확인)
├── skills/
│   ├── newsletter-engine/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── email-copywriting/
│   │   └── SKILL.md           — copywriter 확장 (CURVE 제목줄, CTA 설계, F-패턴)
│   ├── audience-segmentation/
│   │   └── SKILL.md           — analyst+curator 확장 (BEAR 모델, 발송 최적화)
│   └── deliverability-optimization/
│       └── SKILL.md           — editor-in-chief+analyst 확장 (스팸 필터, 도달률)
└── README.md                  — 이 파일
```

## 사용법

`/newsletter-engine` 스킬을 트리거하거나, "뉴스레터 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_curation_brief.md` — 큐레이션 브리프
- `02_newsletter_draft.md` — 뉴스레터 초안
- `03_ab_test_plan.md` — A/B테스트 설계
- `04_editorial_final.md` — 편집장 최종본
- `05_review_report.md` — 리뷰 보고서
