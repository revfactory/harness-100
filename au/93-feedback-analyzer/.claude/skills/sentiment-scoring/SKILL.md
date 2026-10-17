---
name: sentiment-scoring
description: "Sentiment analysis scoring framework. Referenced by the sentiment-analyst agent for systematic sentiment classification and scoring of text data. Used for 'sentiment analysis', 'emotion score', 'NPS analysis' requests. Note: ML model training and NLP pipeline development are out of scope."
---

# Sentiment Scoring

Enhances the sentiment-analyst agent's sentiment classification and scoring capabilities.

## Sentiment Classification System

### 3-Level Basic Classification

| Classification | Score Range | Signal Words |
|---------------|------------|--------------|
| Positive | +0.5 to +1.0 | good, satisfied, recommend, convenient, best |
| Neutral | -0.5 to +0.5 | average, okay, so-so |
| Negative | -1.0 to -0.5 | dissatisfied, disappointed, worst, inconvenient, slow |

### 5-Level Detailed Classification

| Classification | Score | Expression Examples |
|---------------|-------|-------------------|
| Very Positive | +0.8 to +1.0 | "Absolutely the best!", "Highly recommend" |
| Positive | +0.3 to +0.7 | "Pretty good", "Satisfied" |
| Neutral | -0.2 to +0.2 | "It's average", "Not bad" |
| Negative | -0.7 to -0.3 | "Somewhat inconvenient", "Below expectations" |
| Very Negative | -1.0 to -0.8 | "Never using this again", "Worst ever" |

## Sentiment Analysis Methodology

### Rule-based Analysis

```
1. Tokenize: Sentence → word/phrase segmentation
2. Sentiment dictionary matching:
   - Positive words (+1): satisfied, good, convenient, recommend...
   - Negative words (-1): dissatisfied, disappointed, inconvenient, slow...
   - Intensifiers (×1.5): very, really, extremely, totally...
   - Negators (×-1): not, no, cannot, never...
3. Sentence score = Σ(word scores) / word count
4. Document score = Σ(sentence scores) / sentence count
```

### Context Correction Rules

| Pattern | Handling | Example |
|---------|----------|---------|
| Positive + "but" + Negative | Weight latter part | "Good but expensive" → -0.3 |
| Negative + "but" + Positive | Weight latter part | "Expensive but good" → +0.3 |
| Sarcasm | Invert | "Really impressive (sarcastic)" → -0.5 |
| Comparison | Relative evaluation | "B is better than A" → B positive |
| Conditional | Weaken | "It would be nice if..." → -0.2 |

## NPS (Net Promoter Score) Analysis

### NPS Calculation

```
NPS Question: "Would you recommend this product?" (0-10 scale)

Promoter: 9-10
Passive: 7-8
Detractor: 0-6

NPS = Promoter% - Detractor%
Range: -100 to +100
```

### NPS Benchmark

| NPS Range | Rating | Interpretation |
|-----------|--------|----------------|
| 70+ | World-class | Apple, Tesla tier |
| 50-69 | Excellent | Industry leader |
| 30-49 | Good | Above average |
| 0-29 | Needs improvement | Average level |
| Below 0 | At risk | Immediate action needed |

## Sentiment Trend Analysis

### Time-series Sentiment Tracking

```
Monthly sentiment score changes:
  Jan: +0.45 (positive-dominant)
  Feb: +0.38 (slight decline)
  Mar: -0.12 (negative shift) ← event investigation needed
  Apr: +0.22 (recovering)

Anomaly detection threshold:
  ±0.3 or greater change from previous month → root cause analysis required
```

## Quality Checklist

| Item | Criteria |
|------|----------|
| Classification system | Consistent 3-level or 5-level application |
| Context correction | Inversion/intensification/conditional handling |
| Confidence interval | Ambiguous cases treated as neutral |
| NPS calculation | Standard formula applied |
| Trend | Time-series tracking + anomaly detection |
