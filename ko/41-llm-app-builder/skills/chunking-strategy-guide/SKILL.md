---
name: chunking-strategy-guide
description: "RAG 파이프라인의 문서 청킹 전략을 체계적으로 설계하는 방법론. '청킹 전략', '문서 분할', 'RAG 청킹', '임베딩 최적화', '시맨틱 청킹', '텍스트 분할' 등 RAG 데이터 전처리 시 사용한다. 단, 벡터 DB 인프라 구축, 임베딩 모델 학습은 이 스킬의 범위가 아니다."
---

# Chunking Strategy Guide — RAG 문서 청킹 전략

rag-architect의 데이터 전처리 역량을 강화하는 스킬.

## 대상 에이전트

- **rag-architect** — 문서를 효과적으로 청킹하여 검색 품질을 높인다
- **eval-specialist** — 청킹 전략의 검색 품질을 평가한다

## 청킹 전략 비교표

| 전략 | 원리 | 장점 | 단점 | 적합 |
|------|------|------|------|------|
| 고정 크기 | N토큰 단위 절단 | 구현 간단 | 의미 단절 | 로그, 코드 |
| 문장 기반 | 문장 단위 분리 | 의미 보존 | 크기 불균등 | 뉴스, 블로그 |
| 단락 기반 | 빈 줄 기준 | 논리 단위 유지 | 단락 크기 편차 | 문서, 리포트 |
| 시맨틱 | 임베딩 유사도 기준 | 최고 품질 | 느림, 비용 | 복잡한 문서 |
| 재귀적 | 계층적 분리자 | 균형적 | 설정 복잡 | 범용 |
| 마크다운 | 헤딩 기준 | 구조 보존 | MD 전용 | 기술 문서 |

## 청킹 파라미터 가이드

### 최적 청크 크기

```
| 문서 유형 | 청크 크기 | 오버랩 | 이유 |
|----------|----------|--------|------|
| FAQ | 100-200 토큰 | 0 | 질문-답변 쌍이 짧음 |
| 기술 문서 | 300-500 토큰 | 50 | 코드+설명 단위 |
| 법률 문서 | 500-800 토큰 | 100 | 조항 단위 |
| 학술 논문 | 400-600 토큰 | 80 | 단락 단위 |
| 채팅 로그 | 200-300 토큰 | 30 | 대화 턴 단위 |
| 소설/에세이 | 300-500 토큰 | 50 | 장면/단락 단위 |
```

### 오버랩 비율 공식

```
optimal_overlap = chunk_size * 0.1 ~ 0.2

규칙:
- 독립적 문서 (FAQ): 오버랩 0
- 연속적 문서 (매뉴얼): 10-15%
- 고밀도 문서 (법률): 15-20%
- 최대 오버랩: chunk_size의 25% 초과 금지
```

## 시맨틱 청킹 알고리즘

```python
def semantic_chunking(text, model, threshold=0.5):
    """
    1. 문장 단위로 분리
    2. 인접 문장 쌍의 임베딩 코사인 유사도 계산
    3. 유사도가 threshold 이하인 지점에서 분리
    4. 최소/최대 청크 크기 제약 적용
    """
    sentences = split_sentences(text)
    embeddings = model.encode(sentences)

    breakpoints = []
    for i in range(len(embeddings) - 1):
        sim = cosine_similarity(embeddings[i], embeddings[i+1])
        if sim < threshold:
            breakpoints.append(i + 1)

    chunks = split_at(sentences, breakpoints)
    return enforce_size_limits(chunks, min=100, max=800)
```

## 문서 유형별 전처리 파이프라인

### PDF

```
PDF → 텍스트 추출 (pdfplumber/pymupdf)
→ 헤더/푸터 제거
→ 페이지 번호 제거
→ 표 → 마크다운 변환
→ 이미지 → alt text / OCR
→ 메타데이터 추출 (제목, 저자, 날짜)
→ 청킹
```

### HTML/웹페이지

```
HTML → 본문 추출 (trafilatura/readability)
→ 네비게이션/사이드바/광고 제거
→ 마크다운 변환
→ 링크 텍스트 보존 ([텍스트](URL))
→ 테이블 보존
→ 메타데이터 추출 (title, description)
→ 청킹
```

### 코드

```
코드 → AST 파싱
→ 함수/클래스 단위 분리
→ docstring + 시그니처 + 본문
→ 파일 경로 메타데이터 추가
→ 관련 테스트 코드 연결
→ 청킹 (함수 단위)
```

## 메타데이터 강화 전략

```python
chunk_with_metadata = {
    "text": "청크 텍스트...",
    "metadata": {
        "source": "document.pdf",
        "page": 5,
        "section": "3.2 아키텍처",
        "heading_hierarchy": ["3. 설계", "3.2 아키텍처"],
        "chunk_index": 12,
        "total_chunks": 45,
        "created_at": "2025-01-15",
        "document_type": "technical_spec",
        "language": "ko"
    }
}
```

## 청킹 품질 평가 메트릭

| 메트릭 | 공식 | 기준 |
|--------|------|------|
| 정보 완전성 | 원본 핵심 정보 / 전체 핵심 정보 | >= 95% |
| 의미 단절률 | 문장 중간 절단 / 전체 청크 | <= 5% |
| 크기 균일성 | 1 - (std / mean) | >= 0.7 |
| 검색 정밀도 | 관련 청크 / 반환 청크 (top-5) | >= 60% |
| 검색 재현율 | 반환 관련 / 전체 관련 (top-10) | >= 80% |

## 임베딩 모델 선택 가이드

| 모델 | 차원 | 한국어 | 비용 | 용도 |
|------|------|--------|------|------|
| text-embedding-3-small | 1536 | 양호 | $0.02/1M | 범용, 비용 효율 |
| text-embedding-3-large | 3072 | 양호 | $0.13/1M | 고품질 |
| multilingual-e5-large | 1024 | 우수 | 무료(로컬) | 한국어 특화 |
| bge-m3 | 1024 | 우수 | 무료(로컬) | 다국어, 긴 컨텍스트 |
| voyage-multilingual-2 | 1024 | 우수 | $0.12/1M | 다국어 최고 |
