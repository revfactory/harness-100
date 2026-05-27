---
name: citation-standards
description: "학술 인용 및 참고문헌 표준 가이드. paper-writer와 submission-preparer 에이전트가 논문의 인용과 레퍼런스를 작성할 때 참조. '인용 형식', 'APA', '참고문헌' 요청 시 사용. 단, 원문 논문 검색이나 전문 데이터베이스 접근은 범위 밖."
---

# Citation Standards — 학술 인용 표준

paper-writer / submission-preparer 에이전트의 인용/참고문헌 작성 역량 강화.

## 주요 인용 스타일

### APA 7th Edition

**본문 인용:**
```
- 1저자: (Kim, 2024)
- 2저자: (Kim & Lee, 2024)
- 3저자+: (Kim et al., 2024)
- 직접 인용: (Kim, 2024, p. 42)
- 복수 인용: (Kim, 2024; Lee, 2023)
```

**참고문헌:**
```
학술지:
  Kim, J. H., & Lee, S. (2024). Title of article. 
  Journal Name, 15(2), 123-145. 
  https://doi.org/10.xxxx/xxxxx

도서:
  Kim, J. H. (2024). Title of book (2nd ed.). Publisher.

학위논문:
  Kim, J. H. (2024). Title of dissertation 
  [Doctoral dissertation, University Name]. Database Name.

웹페이지:
  Organization. (2024, January 15). Title of page. 
  https://www.example.com/page
```

### IEEE

**본문 인용:**
```
- 순서 번호: [1], [2], [3]
- 복수: [1], [3]-[5]
- "As shown in [1]..."
```

**참고문헌:**
```
[1] J. H. Kim and S. Lee, "Title of article," 
    J. Name, vol. 15, no. 2, pp. 123-145, 2024.

[2] J. H. Kim, Title of Book, 2nd ed. 
    City: Publisher, 2024.
```

### Chicago (Notes-Bibliography)

```
각주:
  1. Ji-Hoon Kim, "Title," Journal 15, no. 2 (2024): 123.

참고문헌:
  Kim, Ji-Hoon. "Title." Journal 15, no. 2 (2024): 123-145.
```

## 저널별 스타일 매핑

| 분야 | 주요 저널 | 인용 스타일 |
|------|---------|-----------|
| 심리학/사회과학 | APA 계열 | APA 7th |
| 공학/컴퓨터 | IEEE 계열 | IEEE |
| 인문학 | 인문학 저널 | Chicago |
| 의학 | NEJM, Lancet | Vancouver |
| 자연과학 | Nature, Science | Nature style |

## 인용 원칙

### 인용해야 하는 경우

| 상황 | 인용 유형 |
|------|----------|
| 타인의 아이디어/주장 | 간접 인용 |
| 정확한 문구 사용 | 직접 인용 (따옴표) |
| 데이터/통계 인용 | 출처 인용 |
| 방법론 차용 | 방법 인용 |
| 이론적 프레임워크 | 원저 인용 |

### 자기 표절 방지

```
- 이전 논문 재사용 시 명시적 인용
- 동일 데이터 복수 논문 → 이전 출판 언급
- 리뷰 논문에서 자기 논문 과다 인용 자제
```

## 논문 구조 표준 (IMRaD)

| 섹션 | 내용 | 시제 |
|------|------|------|
| **I**ntroduction | 배경, 선행연구, 연구 질문 | 현재/과거 |
| **M**ethods | 연구 설계, 대상, 절차, 분석 | 과거 |
| **R**esults | 발견사항, 통계 결과 | 과거 |
| **D**iscussion | 해석, 한계, 시사점 | 현재/과거 |

### 통계 결과 보고 표준 (APA)

```
t-test: t(df) = 값, p = 값, d = 값
  예: t(48) = 2.34, p = .023, d = 0.67

ANOVA: F(df1, df2) = 값, p = 값, η² = 값
  예: F(2, 87) = 4.56, p = .013, η² = .095

상관: r(df) = 값, p = 값
  예: r(58) = .45, p < .001

카이제곱: χ²(df, N = n) = 값, p = 값
  예: χ²(3, N = 200) = 12.34, p = .006
```

## 투고 체크리스트

### 원고 준비

- [ ] 저널 Author Guidelines 확인
- [ ] Word count 준수
- [ ] 인용 스타일 통일
- [ ] 참고문헌 본문 인용과 일치 확인
- [ ] 표/그림 번호 순서
- [ ] Abstract 단어 수 (보통 150~300)
- [ ] Keywords 5~7개
- [ ] 블라인드 리뷰 시 저자 정보 제거

### 커버레터 구조

```
1. 논문 제목 및 저자
2. 논문의 핵심 기여
3. 저널 적합성 설명
4. 윤리 준수 확인
5. 이해충돌 진술
6. 교신저자 연락처
```

## 품질 체크리스트

| 항목 | 기준 |
|------|------|
| 인용 스타일 | 저널 가이드 준수 |
| 일관성 | 본문 인용 ↔ 참고문헌 일치 |
| 최신성 | 최근 5년 인용 50%+ |
| 다양성 | 자기 인용 과다 방지 |
| 표절 | Turnitin 등 검사 |
| 통계 보고 | APA 보고 형식 준수 |
