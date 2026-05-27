---
name: sentiment-lexicon-builder
description: "감성 사전 구축, ABSA(Aspect-Based Sentiment Analysis) 설계, 감성 점수 보정, 도메인 특화 감성 분석 방법론 가이드. '감성 사전', '감성 분석 모델', 'ABSA', '측면별 감성', '감성 점수', '극성 사전', '도메인 감성', '감정 분류' 등 감성분석 설계 시 이 스킬을 사용한다. sentiment-analyzer의 감성분석 역량을 강화한다. 단, 텍스트 전처리나 보고서 작성은 이 스킬의 범위가 아니다."
---

# Sentiment Lexicon Builder — 감성 사전 및 ABSA 설계 가이드

도메인 특화 감성 분석 시스템을 설계하고 구축하는 방법론.

## 감성 분석 접근법 비교

| 접근법 | 장점 | 단점 | 적합 |
|--------|------|------|------|
| 사전 기반 | 빠름, 해석 가능 | 도메인 한계, 문맥 무시 | 소규모, 빠른 프로토타입 |
| ML 기반 (전통) | 도메인 적응 | 학습 데이터 필요 | 레이블 데이터 있을 때 |
| 딥러닝 (BERT) | 문맥 이해, 높은 정확도 | 리소스 필요 | 대규모, 정확도 중시 |
| LLM (프롬프트) | 제로샷, 유연 | 비용, 속도 | 다양한 도메인, 소량 |

## 감성 사전 구축

### 한국어 기본 사전

```python
SENTIMENT_LEXICON = {
    # 긍정 (1.0 ~ 0.1)
    "좋다": 0.8, "훌륭하다": 0.9, "만족": 0.7, "추천": 0.8,
    "편리하다": 0.7, "깔끔하다": 0.6, "최고": 0.9, "친절하다": 0.8,
    "빠르다": 0.6, "저렴하다": 0.5,

    # 부정 (-0.1 ~ -1.0)
    "나쁘다": -0.8, "불만": -0.7, "실망": -0.8, "느리다": -0.6,
    "비싸다": -0.5, "불편하다": -0.7, "최악": -0.9, "불친절": -0.8,
    "고장": -0.7, "환불": -0.6,

    # 강도 수정자
    "매우": 1.5,    # 강화
    "약간": 0.5,    # 약화
    "정말": 1.5,
    "조금": 0.5,
    "너무": 1.3,    # 문맥 따라 긍/부정 모두
}

NEGATION_WORDS = {"않다", "않", "못", "없다", "없", "안"}
```

### 도메인 특화 사전 자동 구축

```python
def build_domain_lexicon(corpus, labels, base_lexicon, top_n=200):
    """
    TF-IDF + PMI 기반 도메인 감성 사전 자동 구축

    1. 긍정/부정 리뷰에서 각각 TF-IDF 상위 단어 추출
    2. PMI(Pointwise Mutual Information)로 감성 극성 계산
    3. 기존 사전과 병합
    """
    pos_texts = [t for t, l in zip(corpus, labels) if l == 'positive']
    neg_texts = [t for t, l in zip(corpus, labels) if l == 'negative']

    # 각 클래스에서의 출현 확률
    for word in vocabulary:
        p_word = count(word, corpus) / len(corpus)
        p_pos = count(word, pos_texts) / len(pos_texts)
        p_neg = count(word, neg_texts) / len(neg_texts)

        pmi_pos = log2(p_pos / p_word) if p_pos > 0 else 0
        pmi_neg = log2(p_neg / p_word) if p_neg > 0 else 0

        polarity = pmi_pos - pmi_neg  # 양수=긍정, 음수=부정

    return domain_lexicon
```

## ABSA (Aspect-Based Sentiment Analysis)

### 설계 구조

```
입력: "배송은 빠른데 제품 품질이 별로예요"

1. 측면(Aspect) 추출:
   - "배송" → [배송/서비스]
   - "품질" → [제품/품질]

2. 측면별 감성 분석:
   - 배송: "빠른" → 긍정 (0.6)
   - 품질: "별로" → 부정 (-0.7)

3. 결과:
   {
     "overall": -0.05,
     "aspects": {
       "배송": {"sentiment": "positive", "score": 0.6, "keywords": ["빠른"]},
       "품질": {"sentiment": "negative", "score": -0.7, "keywords": ["별로"]}
     }
   }
```

### 측면 카테고리 설계 (이커머스 예시)

```yaml
aspects:
  제품:
    품질: [품질, 퀄리티, 소재, 재질, 마감, 내구성]
    디자인: [디자인, 색상, 색깔, 모양, 외관]
    사이즈: [사이즈, 크기, 사이즈감, 피팅]
    가격: [가격, 가성비, 비싸, 저렴, 합리적]
  서비스:
    배송: [배송, 택배, 도착, 배달]
    포장: [포장, 박스, 패키지]
    교환환불: [교환, 환불, 반품, AS]
    고객응대: [응대, 상담, 친절, 불친절]
```

## 감성 점수 보정

### 부정어 처리

```python
def handle_negation(tokens, scores):
    """부정어 뒤 3토큰 이내 감성 반전"""
    negation_window = 0
    adjusted = []
    for token, score in zip(tokens, scores):
        if token in NEGATION_WORDS:
            negation_window = 3
        elif negation_window > 0:
            score = -score * 0.8  # 완전 반전이 아닌 80% 반전
            negation_window -= 1
        adjusted.append(score)
    return adjusted
```

### 강도 수정자 처리

```python
def apply_intensifiers(tokens, scores):
    """강도 수정자에 따른 점수 조정"""
    adjusted = []
    for i, (token, score) in enumerate(zip(tokens, scores)):
        if i > 0 and tokens[i-1] in INTENSIFIERS:
            score *= INTENSIFIERS[tokens[i-1]]
        adjusted.append(score)
    return adjusted
```

### 이모지 감성 매핑

```python
EMOJI_SENTIMENT = {
    "😊": 0.8, "😍": 0.9, "👍": 0.7, "❤️": 0.8, "🙏": 0.5,
    "😡": -0.9, "😤": -0.7, "👎": -0.8, "😢": -0.6, "💔": -0.7,
    "😐": 0.0, "🤔": -0.1,
}
```

## 감성 분석 평가 메트릭

```python
# 감성 분류 평가
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred,
    target_names=['부정', '중립', '긍정']))

# ABSA 평가
# - 측면 추출: Precision, Recall, F1
# - 측면별 감성: Accuracy, Macro-F1
# - 전체: Micro-F1 (측면추출 + 감성 모두 정확해야 정답)
```

## 보고서 구조

```markdown
## 감성 분석 결과

### 전체 요약
| 극성 | 건수 | 비율 |
|------|------|------|
| 긍정 | 650 | 65% |
| 중립 | 150 | 15% |
| 부정 | 200 | 20% |

### 측면별 감성
| 측면 | 긍정 | 부정 | 점수 | 주요 키워드 |
|------|------|------|------|-----------|
| 배송 | 80% | 10% | +0.6 | 빠른, 정확 |
| 품질 | 40% | 45% | -0.2 | 별로, 약함 |

### 시계열 추이
### 주요 부정 패턴 (액션 아이템)
```
