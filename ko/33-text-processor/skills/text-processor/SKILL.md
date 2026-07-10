---
name: text-processor
description: "텍스트 처리 파이프라인: 대량 텍스트의 전처리, 분류, 개체/키워드 추출, 감성분석, 요약 생성, 구조화 데이터 변환, 보고서 작성을 에이전트 팀이 협업하여 수행한다. '텍스트 분석해줘', '텍스트 처리', '문서 분류해줘', '감성분석 해줘', '키워드 추출', '개체명 인식', 'NER', '텍스트 요약', '리뷰 분석', '설문 텍스트 분석', '댓글 분석' 등 텍스트 NLP 처리 전반에 이 스킬을 사용한다. 단, 음성인식(STT), 기계번역, 챗봇 대화 관리, LLM 파인튜닝은 이 스킬의 범위가 아니다."
---

# Text Processor — 텍스트 처리 풀 파이프라인

대량 텍스트의 전처리→분류→추출→감성분석→구조화→보고서를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| preprocessor | `agents/preprocessor.md` | 텍스트 전처리, 노이즈 제거 | general-purpose |
| classifier | `agents/classifier.md` | 주제/의도 분류, 태깅 | general-purpose |
| extractor | `agents/extractor.md` | 개체명, 키워드, 관계, 요약 추출 | general-purpose |
| sentiment-analyzer | `agents/sentiment-analyzer.md` | 감성/감정/의견 분석 | general-purpose |
| report-writer | `agents/report-writer.md` | 최종 보고서, 품질 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **텍스트 소스**: 파일 경로, 포맷, 문서 수, 언어
    - **분석 목적**: 무엇을 알고 싶은가 (분류, 감성, 키워드 등)
    - **도메인 정보** (선택): 업종, 텍스트 유형(리뷰/뉴스/SNS/문서)
    - **분류 체계** (선택): 사용자 정의 분류 카테고리
2. `_workspace/` 디렉토리와 `_workspace/structured_data/` 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 전처리 | preprocessor | 없음 | `01_preprocessing_result.md` |
| 2a | 분류 | classifier | 작업 1 | `02_classification_result.md` |
| 2b | 추출 | extractor | 작업 1 | `03_extraction_result.md` |
| 3 | 감성분석 | sentiment-analyzer | 작업 1, 2a, 2b | `04_sentiment_result.md` |
| 4 | 보고서 | report-writer | 작업 2a, 2b, 3 | `05_final_report.md` |

작업 2a(분류)와 2b(추출)는 **병렬 실행**한다. 감성분석은 분류와 추출 결과를 활용하여 측면별 분석의 정확도를 높인다.

**팀원 간 소통 흐름:**
- preprocessor 완료 → classifier, extractor, sentiment-analyzer에게 정제 텍스트와 메타데이터 전달
- classifier 완료 → extractor에게 주제 분류 결과 전달 (주제별 맞춤 추출), sentiment-analyzer에게 분류 전달
- extractor 완료 → sentiment-analyzer에게 개체 목록 전달 (개체별 감성 분석)
- sentiment-analyzer 완료 → report-writer에게 결과 전달
- report-writer는 모든 산출물을 교차 검증. 불일치 시 해당 에이전트에 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일과 `structured_data/` 디렉토리를 확인한다
2. 보고서의 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "텍스트 분석해줘", "풀 파이프라인" | **풀 파이프라인** | 5명 전원 |
| "분류만 해줘", "카테고리 분류" | **분류 모드** | preprocessor + classifier |
| "감성분석만 해줘", "리뷰 감성" | **감성 모드** | preprocessor + sentiment-analyzer |
| "키워드 추출", "개체명 인식" | **추출 모드** | preprocessor + extractor |
| "요약해줘", "텍스트 요약" | **요약 모드** | preprocessor + extractor(요약 기능) |
| "보고서 써줘" (기존 분석 있음) | **보고서 모드** | report-writer 단독 |

**기존 파일 활용**: 사용자가 이미 전처리된 텍스트나 분류 결과 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 마크다운 산출물 |
| 구조화 데이터 | `_workspace/structured_data/` | JSON/CSV 프로그래밍 활용 데이터 |
| 메시지 기반 | SendMessage | 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 인코딩 오류 | chardet 자동 감지 → UTF-8 강제 변환, 손실 기록 |
| 대용량 텍스트(>10만 문서) | 배치 처리, 샘플 분석 후 전체 적용 |
| 다국어 혼재 | 언어별 세그먼트 분리 후 개별 처리 |
| NER 도메인 미스매치 | 패턴 기반 추출 보완, 커스텀 사전 생성 제안 |
| 에이전트 실패 | 1회 재시도 후 실패 시 해당 산출물 없이 진행 |
| 보고서 불일치 발견 | 해당 에이전트에 수정 요청 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "고객 리뷰 1000건을 분석해서 제품별 만족도와 불만 사항을 뽑아줘"
**기대 결과**:
- 전처리: 리뷰 텍스트 정규화, 중복 제거, 통계 산출
- 분류: 제품 카테고리별, 리뷰 의도별(칭찬/불만/문의/제안) 분류
- 추출: 제품명, 기능명, 핵심 키워드, 리뷰별 요약
- 감성: 전체 감성 분포, 제품별·기능별 감성(ABSA), 불만 패턴
- 보고서: 제품별 만족도 순위, 주요 불만 Top 5, 개선 권고안

### 기존 파일 활용 흐름
**프롬프트**: "이미 전처리된 텍스트 데이터가 있는데 감성분석만 해줘" + 전처리 파일 첨부
**기대 결과**:
- 기존 전처리 결과를 `_workspace/01_preprocessing_result.md`로 복사
- 감성 모드: preprocessor 건너뛰고 sentiment-analyzer만 투입
- classifier, extractor, report-writer는 투입하지 않음

### 에러 흐름
**프롬프트**: "이 CSV 파일의 댓글을 분석해줘" (다국어 혼재, 이모지 다수, 짧은 텍스트)
**기대 결과**:
- preprocessor가 언어별 세그먼트 분리, 이모지 처리 전략 결정
- classifier가 짧은 텍스트 분류 신뢰도 저하를 명시
- sentiment-analyzer가 이모지의 감성 정보를 활용
- report-writer가 다국어·짧은 텍스트의 분석 한계를 보고서에 기록


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| nlp-preprocessing-toolkit | `skills/nlp-preprocessing-toolkit/SKILL.md` | preprocessor, extractor | 토큰화, 한국어 형태소 분석, 임베딩 선택, 벡터화 |
| sentiment-lexicon-builder | `skills/sentiment-lexicon-builder/SKILL.md` | sentiment-analyzer | 감성 사전 구축, ABSA, 부정어/강도 보정, 이모지 매핑 |
