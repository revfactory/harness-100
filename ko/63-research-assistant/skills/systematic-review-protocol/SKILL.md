---
name: systematic-review-protocol
description: "체계적 문헌 고찰(Systematic Review)의 PRISMA 프로토콜과 문헌 검색 전략을 제공하는 전문 스킬. literature-searcher와 critic-synthesizer가 학술 문헌을 체계적으로 검색, 선별, 종합할 때 활용한다. '체계적 문헌 고찰', 'systematic review', 'PRISMA', '문헌 검색 전략', '포함/배제 기준', 'Boolean 검색' 등의 맥락에서 자동 적용한다. 단, 학술 DB(Scopus, WoS) 직접 접속이나 메타분석 통계 실행은 이 스킬의 범위가 아니다."
---

# Systematic Review Protocol — 체계적 문헌 고찰 프로토콜

literature-searcher, critic-synthesizer 에이전트의 문헌 고찰 역량을 강화하는 전문 스킬.

## 적용 대상 에이전트

- **literature-searcher** — 검색 전략, PRISMA 흐름도, 포함/배제 기준
- **critic-synthesizer** — 비판적 평가, 테마 종합, 연구 갭 도출

## PRISMA 2020 흐름도

```
식별 (Identification)
├── 데이터베이스 검색: n = [X]
├── 레지스트리 검색: n = [Y]
└── 기타 소스: n = [Z]
         │
    중복 제거 후: n = [A]
         │
선별 (Screening)
├── 제목/초록 선별: n = [A]
│   └── 배제: n = [B] (이유별 분류)
│
적격성 (Eligibility)
├── 전문 평가: n = [C]
│   └── 배제: n = [D]
│       ├── 이유 1: n = [d1]
│       ├── 이유 2: n = [d2]
│       └── 이유 3: n = [d3]
│
포함 (Included)
└── 최종 포함: n = [E]
    ├── 양적 연구: n = [e1]
    └── 질적 연구: n = [e2]
```

## 검색 전략 설계

### PICO/PICo 프레임워크

**양적 연구 (PICO):**

| 요소 | 정의 | 예시 |
|------|------|------|
| P - Population | 대상 집단 | "대학생", "제조업 근로자" |
| I - Intervention | 개입/노출 | "플립러닝", "원격근무" |
| C - Comparison | 비교 대상 | "전통 강의", "사무실 근무" |
| O - Outcome | 결과 변수 | "학업 성취도", "생산성" |

**질적 연구 (PICo):**

| 요소 | 정의 |
|------|------|
| P - Population | 대상 집단 |
| I - Interest | 관심 현상 |
| Co - Context | 맥락/환경 |

### Boolean 검색식 구성

```
("flipped learning" OR "flipped classroom" OR "inverted classroom")
AND
("motivation" OR "learning motivation" OR "academic motivation" OR "intrinsic motivation")
AND
("higher education" OR "university" OR "college" OR "undergraduate")
```

### 검색식 설계 원칙

| 원칙 | 방법 |
|------|------|
| 동의어 포함 | OR로 연결 |
| 개념 교차 | AND로 연결 |
| 확장 검색 | 절단기호(*) 사용: learn* → learning, learner, learned |
| 구문 검색 | 따옴표 사용: "flipped classroom" |
| 제한 | 연도, 언어, 문서 유형 필터 |

### 데이터베이스별 검색 전략

| DB | 분야 | 특징 |
|----|------|------|
| Google Scholar | 범용 | 넓은 커버리지, 회색문헌 포함 |
| PubMed | 의학/보건 | MeSH 용어 활용 |
| Scopus | 다학제 | 인용 분석 우수 |
| Web of Science | 다학제 | JCR 임팩트팩터 |
| ERIC | 교육 | 교육 전문 시소러스 |
| IEEE Xplore | 공학/IT | 컨퍼런스 논문 포함 |
| RISS | 한국 학술 | 국내 논문/학위논문 |

## 포함/배제 기준 설정

```markdown
### 포함 기준 (Inclusion Criteria)

| 기준 | 상세 |
|------|------|
| 출판 기간 | 2015-2025 |
| 언어 | 영어, 한국어 |
| 연구 설계 | 실험, 준실험, 설문 조사 |
| 대상 | 대학생 |
| 개입 | 플립러닝 적용 |
| 결과 변수 | 학습 동기 측정 포함 |
| 출판 유형 | 피어리뷰 학술지 |

### 배제 기준 (Exclusion Criteria)

| 기준 | 상세 | 사유 |
|------|------|------|
| 연구 프로토콜만 | 결과 없음 | 데이터 없음 |
| 학회 발표 초록 | 세부 정보 부족 | 방법론 검증 불가 |
| K-12 대상 | 맥락 상이 | 범위 제한 |
```

## 문헌 품질 평가 도구

### 양적 연구 품질 평가 (간소화)

| 기준 | 높음 | 중간 | 낮음 |
|------|------|------|------|
| 표본 크기 | 충분 (검정력 분석) | 적정 | 부족 |
| 무작위 배정 | 예 | 준실험 | 비실험 |
| 타당한 측정 도구 | 검증된 도구 | 수정 도구 | 자체 개발 |
| 통계 방법 적절성 | 적절 | 부분 적절 | 부적절 |
| 탈락률 | < 10% | 10-20% | > 20% |

### 질적 연구 품질 평가

| 기준 | 확인 질문 |
|------|----------|
| 연구 목적 명확성 | 연구 질문이 명확한가? |
| 방법론 적절성 | 질적 방법이 적합한가? |
| 연구 설계 | 목적에 맞는 설계인가? |
| 데이터 수집 | 충분히 깊이 있는 데이터인가? |
| 분석 엄밀성 | 분석 과정이 투명한가? |
| 연구자 성찰 | 연구자의 영향을 성찰했는가? |

## 테마 종합 (Thematic Synthesis)

### 3단계 종합 프로세스

```
1단계: 코딩 (Line-by-line coding)
  → 각 연구의 핵심 발견을 코드로 추출

2단계: 기술적 테마 (Descriptive themes)
  → 유사 코드를 묶어 기술적 테마 형성

3단계: 분석적 테마 (Analytical themes)
  → 기술적 테마를 넘어서는 해석적 통찰 도출
```
