---
name: text-analytics-methods
description: "Text analytics methodology. Referenced by topic-classifier and trend-detector agents when extracting topics and deriving trends from unstructured text. Used for 'topic classification', 'keyword analysis', 'text mining' requests. Note: NLP model training and large-scale data processing pipeline development are out of scope."
---

# Text Analytics Methods

Enhances the text analysis capabilities of topic-classifier / trend-detector agents.

## Topic Classification Methodology

### Bottom-up Classification

```
1. Read all feedback (sample: 100+ entries)
2. Identify recurring keywords/phrases
3. Cluster similar keywords
4. Assign topic names to clusters
5. Finalize topic system (MECE verification)
6. Tag all data with topics
```

### Top-down Classification

```
Pre-defined categories:
├── Product/Service Quality
│   ├── Features
│   ├── Performance
│   ├── Design
│   └── Reliability
├── Customer Experience
│   ├── Usability
│   ├── Customer Support
│   ├── Purchase Process
│   └── Delivery
├── Price/Value
│   ├── Price Level
│   ├── Value for Money
│   └── Discounts/Promotions
└── Other
    ├── Competitor Comparison
    └── Improvement Requests
```

## Keyword Analysis

### TF-IDF Concept Application

```
TF (Term Frequency) = Word frequency in a specific document
IDF (Inverse Document Frequency) = Rarity across all documents
TF-IDF = TF × IDF

High TF-IDF = Words important in a specific document but uncommon overall
→ Useful for identifying feedback anomalies
```

### Keyword Extraction Process

```
1. Remove stop words: articles, conjunctions, common verbs
2. Extract nouns/adjectives
3. Calculate frequency (top 30)
4. N-gram analysis (2-gram, 3-gram)
   "slow delivery", "support not reachable"
5. Keyword cloud visualization
```

## Trend Analysis Techniques

### Time-series Topic Trends

| Topic | Q1 | Q2 | Q3 | Q4 | Trend |
|-------|-----|-----|-----|-----|-------|
| Delivery | 15% | 18% | 22% | 25% | ↑ Attention |
| Quality | 30% | 28% | 25% | 20% | ↓ Improving |
| Price | 20% | 22% | 20% | 21% | → Stable |

### Anomaly Detection Criteria

```
Anomaly signals:
- Topic ratio +50% vs previous period → urgent analysis
- Negative sentiment surge of +0.3 or more → investigate cause
- New keyword emergence (absent in previous quarter) → new issue
```

## Insight Derivation Framework

### Pyramid Principle (So What?)

```
Level 1 (Data): "Delivery complaints at 25%, up 7pp from previous quarter"
Level 2 (Analysis): "Delivery delays mainly caused by new logistics partner switch"
Level 3 (Insight): "Need to renegotiate logistics SLA or revert to previous provider"
Level 4 (Action): "Request SLA review from logistics team, improvement plan due in 2 weeks"
```

### Action Priority Matrix

| Insight | Frequency | Sentiment Intensity | Impact | Ease of Implementation | Priority |
|---------|-----------|--------------------| -------|----------------------|----------|
| Delivery improvement | High | -0.8 | High | Medium | ★★★★★ |
| UI improvement | Medium | -0.5 | Medium | High | ★★★★ |
| New feature A | Low | +0.3 | Low | Low | ★★ |

## Quality Checklist

| Item | Criteria |
|------|----------|
| Classification system | MECE (Mutually Exclusive, Collectively Exhaustive) |
| Sample size | 100+ entries or full dataset |
| Multi-tagging | Multiple topics per entry allowed |
| Trends | Minimum 3-period comparison |
| So What | Data → Analysis → Insight → Action |
| Visualisation | Keyword cloud + trend chart |
