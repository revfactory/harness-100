---
name: nlp-preprocessing-toolkit
description: "텍스트 전처리 기법 카탈로그: 토큰화, 정규화, 불용어, 형태소 분석, 임베딩 선택, 한국어 특화 처리 가이드. '텍스트 전처리', '토큰화', '형태소 분석', 'KoNLPy', '불용어', '정규화', 'TF-IDF', '임베딩', 'Word2Vec', '한국어 NLP' 등 텍스트 전처리 시 이 스킬을 사용한다. preprocessor와 extractor의 텍스트 처리 역량을 강화한다. 단, 감성분석 모델이나 분류 알고리즘 선택은 이 스킬의 범위가 아니다."
---

# NLP Preprocessing Toolkit — 텍스트 전처리 도구 가이드

텍스트 데이터를 분석 가능한 형태로 변환하는 전처리 기법 카탈로그.

## 전처리 파이프라인

```
원본 텍스트
├── 1. 인코딩 정규화 (UTF-8)
├── 2. HTML/특수문자 제거
├── 3. 유니코드 정규화 (NFKC)
├── 4. 소문자 변환 (영문)
├── 5. 토큰화
├── 6. 불용어 제거
├── 7. 형태소 분석 / 어간 추출
├── 8. 정규표현식 필터링
└── 9. 벡터화 (TF-IDF / 임베딩)
```

## 한국어 특화 처리

### 형태소 분석기 비교

| 분석기 | 속도 | 정확도 | 사용자 사전 | 설치 |
|--------|------|--------|-----------|------|
| Mecab | 가장 빠름 | 높음 | ✅ | C 의존 |
| Okt (Twitter) | 빠름 | 중간 | ✅ | Java 의존 |
| Komoran | 중간 | 높음 | ✅ | Java 의존 |
| Kkma | 느림 | 높음 | ❌ | Java 의존 |
| Kiwi | 빠름 | 높음 | ✅ | Python 네이티브 |

```python
# Kiwi (설치 가장 간편, 성능 우수)
from kiwipiepy import Kiwi
kiwi = Kiwi()

tokens = kiwi.tokenize("아버지가방에들어가셨다")
# [Token(form='아버지', tag='NNG'), Token(form='가', tag='JKS'),
#  Token(form='방', tag='NNG'), Token(form='에', tag='JKB'),
#  Token(form='들어가', tag='VV'), Token(form='시', tag='EP'),
#  Token(form='었', tag='EP'), Token(form='다', tag='EF')]

# 명사만 추출
nouns = [t.form for t in tokens if t.tag.startswith('NN')]
```

### 한국어 정규화

```python
import re, unicodedata

def normalize_korean(text):
    # 유니코드 정규화 (호환 분해 + 정준 결합)
    text = unicodedata.normalize('NFKC', text)

    # 반복 문자 제거 ("ㅋㅋㅋㅋㅋ" → "ㅋㅋ")
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    # 자음/모음만 있는 것 제거 ("ㅎㅎ", "ㅠㅠ" 등은 감성 분석용 보존 가능)
    # text = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]+', '', text)

    # 영문+한글+숫자+공백만 보존
    text = re.sub(r'[^\w\s가-힣]', ' ', text)

    # 다중 공백 제거
    text = re.sub(r'\s+', ' ', text).strip()

    return text
```

### 한국어 불용어

```python
KOREAN_STOPWORDS = {
    # 조사
    '이', '가', '은', '는', '을', '를', '에', '의', '와', '과',
    '도', '로', '에서', '까지', '부터', '만', '으로',
    # 대명사
    '그', '이', '저', '것', '수', '등', '들',
    # 부사
    '매우', '아주', '정말', '너무', '잘', '또', '더',
    # 접속사/감탄사
    '그리고', '하지만', '그런데', '그래서',
}
```

## 텍스트 벡터화

### TF-IDF

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    max_features=10000,
    min_df=2,           # 최소 2개 문서에 등장
    max_df=0.95,        # 95% 이상 문서에 등장하면 제외
    ngram_range=(1, 2), # 유니그램 + 바이그램
    sublinear_tf=True,  # 1 + log(tf) — 고빈도 완화
)
tfidf_matrix = vectorizer.fit_transform(texts)
```

### 임베딩 선택 가이드

| 방법 | 차원 | 적합 | 특징 |
|------|------|------|------|
| TF-IDF | 고차원 (희소) | 키워드 중심, 소규모 | 해석 가능, 빠름 |
| Word2Vec | 100~300 | 유사도, 유추 | 단어 수준, 문맥 제한 |
| FastText | 100~300 | 한국어, OOV 처리 | 자소 기반, 미등록어 강건 |
| BERT | 768 | 분류, NER, QA | 문맥 의존적, 양방향 |
| Sentence-BERT | 384~768 | 문서 유사도, 검색 | 문장 수준 임베딩 |

```python
# Sentence-BERT (한국어)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('jhgan/ko-sroberta-multitask')
embeddings = model.encode(texts, show_progress_bar=True)
# 코사인 유사도
from sklearn.metrics.pairwise import cosine_similarity
sim_matrix = cosine_similarity(embeddings)
```

## 텍스트 품질 메트릭

| 메트릭 | 계산 | 기준 |
|--------|------|------|
| 평균 토큰 수 | 텍스트당 토큰 수 | < 3이면 분석 한계 |
| 어휘 다양성 | 고유 토큰 / 전체 토큰 | 0.2~0.8 양호 |
| 언어 순도 | 주 언어 비율 | > 90% 권장 |
| 결측률 | 빈 텍스트 비율 | < 5% |
| 중복률 | 동일 텍스트 비율 | < 10% |

## 전처리 결정 체크리스트

- [ ] 인코딩 문제 해결 (CP949 등)
- [ ] HTML 태그/URL 제거
- [ ] 이모지 처리 결정 (제거 vs 텍스트 변환 vs 감성 활용)
- [ ] 숫자 처리 (제거 vs 토큰화 vs [NUM] 대체)
- [ ] 형태소 분석기 선택
- [ ] 불용어 목록 도메인 맞춤
- [ ] 최소 토큰 수 필터링
- [ ] 벡터화 방법 선택
