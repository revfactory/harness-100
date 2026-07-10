---
name: personal-branding
description: "개인 브랜딩을 에이전트 팀이 체계적으로 수행하는 파이프라인. '이력서 써줘', '개인 브랜딩', 'resume', 'CV 작성', '포트폴리오 만들어줘', 'LinkedIn 프로필 최적화', '자기소개서 써줘', '커버레터', '경력 정리', '취업 준비 도와줘', '이직 준비' 등 개인 브랜딩·커리어 문서 전반에 이 스킬을 사용한다. 단, 구인 공고 검색, 면접 시뮬레이션, 연봉 협상 코칭은 이 스킬의 범위가 아니다."
---

# Personal Branding — 개인 브랜딩 파이프라인

포지셔닝 분석→이력서·CV→포트폴리오→LinkedIn 프로필→자기소개서·커버레터를 에이전트 팀이 협업하여 제작한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 일관된 브랜드를 구축한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| positioning-strategist | `agents/positioning-strategist.md` | 강점 분석·차별화·키워드 전략 | general-purpose |
| resume-writer | `agents/resume-writer.md` | 이력서·CV 작성 | general-purpose |
| portfolio-designer | `agents/portfolio-designer.md` | 포트폴리오 큐레이션·설계 | general-purpose |
| profile-optimizer | `agents/profile-optimizer.md` | LinkedIn 프로필 최적화 | general-purpose |
| cover-letter-writer | `agents/cover-letter-writer.md` | 자기소개서·커버레터 작성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **경력 정보**: 현재 직무, 경력 연차, 주요 경험
    - **목표**: 원하는 포지션, 타깃 기업/업계
    - **기존 자료** (선택): 현재 이력서, 포트폴리오, LinkedIn URL
    - **요청 범위** (선택): 전체 패키지 또는 특정 문서만
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 분석 기반으로 활용한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 포지셔닝 전략 | positioning-strategist | 없음 | `_workspace/01_positioning_brief.md` |
| 2a | 이력서 작성 | resume-writer | 작업 1 | `_workspace/02_resume.md` |
| 2b | 포트폴리오 설계 | portfolio-designer | 작업 1 | `_workspace/03_portfolio.md` |
| 3a | LinkedIn 프로필 | profile-optimizer | 작업 1, 2a | `_workspace/04_linkedin_profile.md` |
| 3b | 커버레터 | cover-letter-writer | 작업 1, 2a | `_workspace/05_cover_letter.md` |

작업 2a(이력서)와 2b(포트폴리오)는 **병렬 실행**한다.
작업 3a(LinkedIn)와 3b(커버레터)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- positioning-strategist 완료 → 전 에이전트에게 UVP, 키워드, 내러티브 전달
- resume-writer 완료 → profile-optimizer에게 경력 서술, cover-letter-writer에게 핵심 성과 전달
- portfolio-designer 완료 → profile-optimizer에게 Featured 항목, cover-letter-writer에게 프로젝트 성과 전달
- 전체 산출물 간 **브랜드 일관성** 교차 확인

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 산출물 간 브랜드 메시지 일관성을 검증한다:
    - 이력서↔LinkedIn 경력 서술 일관성
    - 포트폴리오↔이력서 프로젝트 정합성
    - 커버레터↔포지셔닝 UVP 반영 여부
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "개인 브랜딩 해줘", "취업 준비" | **풀 패키지** | 5명 전원 |
| "이력서만 써줘" | **이력서 모드** | positioning-strategist + resume-writer |
| "포트폴리오 만들어줘" | **포트폴리오 모드** | positioning-strategist + portfolio-designer |
| "LinkedIn 프로필 최적화해줘" | **프로필 모드** | positioning-strategist + profile-optimizer |
| "자기소개서 써줘", "커버레터" | **커버레터 모드** | positioning-strategist + cover-letter-writer |

**기존 파일 활용**: 기존 이력서를 제공하면 positioning-strategist가 분석하여 전략 수립에 활용한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 웹 탐색 | WebSearch/WebFetch | JD 분석, 업계 트렌드 조사 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 경력 정보 부족 | 핵심 질문 리스트 제시, 가용 정보로 초안 작성 |
| 목표 미지정 | 3가지 포지셔닝 시나리오 제안 |
| 웹 검색 실패 | 일반적 JD 트렌드 지식 기반 작업, "시장 데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고에 누락 명시 |
| 기밀 경력 | 수치·사명 추상화 가이드 적용 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "3년차 백엔드 개발자인데, 시니어 포지션으로 이직 준비하고 있어. 전체 브랜딩 패키지 만들어줘."
**기대 결과**:
- 포지셔닝: 시니어 역할에 맞는 UVP, 기술+리더십 강점 분석
- 이력서: ATS 최적화, 성과 정량화, 시니어 키워드 반영
- 포트폴리오: 3~5개 프로젝트 케이스 스터디, 기술적 의사결정 강조
- LinkedIn: 시니어 개발자 키워드, About 섹션 서술
- 커버레터: 성장 스토리 + 시니어 역할 준비도

### 단일 문서 요청 흐름
**프롬프트**: "이 JD에 맞는 커버레터만 써줘" + JD 제공
**기대 결과**:
- positioning-strategist가 JD 분석 → 핵심 요건 추출
- cover-letter-writer가 맞춤 커버레터 작성
- 다른 에이전트는 건너뜀

### 에러 흐름
**프롬프트**: "이력서 써줘"
**기대 결과**:
- 경력 정보 부족하므로 positioning-strategist가 질문 리스트 제시
- 사용자 응답 기반으로 이력서 모드 실행
- LinkedIn, 포트폴리오, 커버레터는 건너뛰되, "추가 제작 가능" 안내

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| resume-writer | `ats-optimizer` | ATS 파싱 원리, 키워드 최적화, 성과 정량화(STAR-Q), 형식 규칙 |
| profile-optimizer | `linkedin-seo` | LinkedIn 검색 알고리즘, 섹션별 최적화, 리크루터 검색 패턴, SSI |
