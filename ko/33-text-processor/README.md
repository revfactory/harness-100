# Text Processor Harness

텍스트 처리 파이프라인: 대량 텍스트→요약·분류·개체추출·감성분석→구조화 데이터→보고서를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── preprocessor.md      — 전처리 (토큰화, 정규화, 노이즈 제거, 언어 감지)
│   ├── classifier.md        — 분류 엔진 (주제 분류, 의도 분류, 멀티라벨 태깅)
│   ├── extractor.md         — 추출 전문가 (개체명, 키워드, 관계, 요약 생성)
│   ├── sentiment-analyzer.md — 감성 분석 (극성, 감정, 측면별 감성, 의견 마이닝)
│   └── report-writer.md     — 보고서 작성 (구조화 데이터 통합, 인사이트, 시각화)
├── skills/
│   ├── text-processor/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── nlp-preprocessing-toolkit/
│   │   └── SKILL.md              — 텍스트 전처리 도구 가이드
│   └── sentiment-lexicon-builder/
│       └── SKILL.md              — 감성 사전 및 ABSA 설계 가이드
└── README.md                — 이 파일
```

## 사용법

`/text-processor` 스킬을 트리거하거나, "텍스트 분석해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 텍스트 소스 정리
- `01_preprocessing_result.md` — 전처리 결과 및 텍스트 통계
- `02_classification_result.md` — 분류 결과
- `03_extraction_result.md` — 추출 결과 (개체, 키워드, 요약)
- `04_sentiment_result.md` — 감성 분석 결과
- `05_final_report.md` — 최종 통합 보고서
- `structured_data/` — JSON/CSV 구조화 데이터
