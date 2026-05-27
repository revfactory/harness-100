# Translation & Localization Harness

다국어 번역·현지화·문화적응·용어관리를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── translator.md            — 번역가 (원문 분석, 1차 번역, 뉘앙스 보존)
│   ├── localizer.md             — 현지화 전문가 (문화 적응, 관용구, 도량형, 날짜 형식)
│   ├── terminology-manager.md   — 용어 관리자 (용어집 구축, 일관성 유지, 업계 표준)
│   ├── quality-reviewer.md      — 품질 검증자 (정확성, 유창성, 현지화 적합성 검증)
│   └── style-harmonizer.md      — 스타일 통일자 (톤앤보이스 일관성, 브랜드 어조 적용)
├── skills/
│   ├── translation-localization/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── translation-quality-mqm/
│   │   └── SKILL.md             — 품질검증자 확장 (MQM 오류 분류, 심각도, 점수 산출)
│   └── cultural-adaptation-guide/
│       └── SKILL.md             — 현지화전문가 확장 (시장별 형식 변환, 문화 금기, 관용구 대체)
└── README.md                    — 이 파일
```

## 사용법

`/translation-localization` 스킬을 트리거하거나, "이 문서 번역해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_source_analysis.md` — 원문 분석·번역 전략
- `02_terminology.md` — 용어집
- `03_translation.md` — 번역문
- `04_localization.md` — 현지화 적용 결과
- `05_review_report.md` — 품질 검증 보고서
