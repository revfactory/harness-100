# Feedback Analyzer Harness

고객·직원 피드백 분석 하네스. 데이터 수집부터 감성분석, 주제분류, 트렌드 도출, 인사이트 보고서까지 에이전트 팀이 협업하여 생성한다.

## 구조

```

├── agents/
│   ├── data-collector.md       — 피드백 데이터 수집·정제
│   ├── sentiment-analyst.md    — 감성분석 (긍정/부정/중립, 감정강도)
│   ├── topic-classifier.md    — 주제분류 (카테고리, 키워드 클러스터링)
│   ├── trend-detector.md      — 트렌드 도출 (시계열, 이상탐지)
│   └── insight-writer.md      — 인사이트 보고서 (액션아이템, 우선순위)
├── skills/
│   ├── feedback-analyzer/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── sentiment-scoring/
│   │   └── SKILL.md           — 감성 분석 스코어링 (sentiment-analyst 확장)
│   └── text-analytics-methods/
│       └── SKILL.md           — 텍스트 분석 방법론 (topic-classifier 확장)
└── README.md                  — 이 파일
```

## 사용법

`/feedback-analyzer` 스킬을 트리거하거나, "고객 피드백 분석해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 원본 피드백 데이터 및 분석 요건 정리
- `01_data_collection.md` — 데이터 수집·정제 결과
- `02_sentiment_analysis.md` — 감성분석 결과
- `03_topic_classification.md` — 주제분류 결과
- `04_trend_report.md` — 트렌드 분석 결과
- `05_insight_report.md` — 종합 인사이트 보고서
