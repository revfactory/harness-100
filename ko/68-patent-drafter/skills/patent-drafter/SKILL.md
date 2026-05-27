---
name: patent-drafter
description: "특허 명세서 작성 풀 파이프라인. 선행기술조사→청구항→명세서→도면설명을 에이전트 팀이 협업하여 한 번에 생성한다. '특허 명세서 작성해줘', '특허 출원', '발명 특허', '청구항 작성', '선행기술 조사', '특허 초안', '특허 명세서 초안', '발명 신고서를 특허로', '아이디어를 특허로' 등 특허 명세서 작성 전반에 이 스킬을 사용한다. 단, 실제 특허청 출원 대행, 특허 심사 대응(의견서/보정서), 특허 소송, 해외 출원(PCT/파리조약) 실무는 이 스킬의 범위가 아니다."
---

# Patent Drafter — 특허 명세서 작성 파이프라인

발명의 기술적 아이디어를 체계적인 특허 명세서 세트로 변환한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| prior-art-researcher | `agents/prior-art-researcher.md` | 선행기술 조사, 신규성·진보성 분석 | general-purpose |
| claim-drafter | `agents/claim-drafter.md` | 독립항·종속항 작성, 권리범위 설계 | general-purpose |
| specification-writer | `agents/specification-writer.md` | 발명의 상세한 설명, 실시예 작성 | general-purpose |
| drawing-designer | `agents/drawing-designer.md` | 도면 구성, 부호 설명 | general-purpose |
| patent-reviewer | `agents/patent-reviewer.md` | 정합성 교차 검증, 기재불비 점검 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **발명의 명칭**: 기술적 명칭
    - **기술 분야**: 발명이 속하는 기술 분야
    - **발명의 개요**: 핵심 기술 사상, 구성요소, 동작 원리
    - **해결 과제**: 기존 기술의 문제점과 해결하려는 과제
    - **기존 자료** (선택): 발명 신고서, 기술 문서, 프로토타입 정보
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 선행기술 조사 | prior-art-researcher | 없음 | `_workspace/01_prior_art_report.md` |
| 2 | 청구항 작성 | claim-drafter | 작업 1 | `_workspace/02_claims.md` |
| 3a | 명세서 작성 | specification-writer | 작업 1, 2 | `_workspace/03_specification.md` |
| 3b | 도면 설계 | drawing-designer | 작업 2 | `_workspace/04_drawings.md` |
| 4 | 특허 검증 | patent-reviewer | 작업 1, 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(명세서)와 3b(도면)는 **병렬 실행**한다. 둘 다 청구항에 의존하므로 작업 2 완료 후 동시 시작 가능하다. 단, 부호 번호 조율을 위해 양쪽이 소통한다.

**팀원 간 소통 흐름:**
- prior-art-researcher 완료 → claim-drafter에게 차별점·회피 설계 방향 전달
- claim-drafter 완료 → specification-writer에게 구성요소·용어 전달, drawing-designer에게 구조 전달
- specification-writer ↔ drawing-designer: 부호 번호 체계 상호 조율
- patent-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 선행기술 조사 보고서 — `01_prior_art_report.md`
    - 청구항 세트 — `02_claims.md`
    - 발명의 상세한 설명 — `03_specification.md`
    - 도면 설명서 — `04_drawings.md`
    - 검증 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "특허 명세서 전체 작성해줘" | **풀 파이프라인** | 5명 전원 |
| "선행기술만 조사해줘" | **조사 모드** | prior-art-researcher 단독 |
| "청구항만 작성해줘" | **청구항 모드** | claim-drafter + reviewer |
| "이 청구항으로 명세서 써줘" (기존 청구항 있음) | **명세서 모드** | specification-writer + drawing-designer + reviewer |
| "명세서 검토해줘" | **검증 모드** | patent-reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 부호 조율, 수정 요청 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 선행기술 조사원이 일반 지식 기반으로 작업, "DB 검색 미실시" 명시 |
| 발명 정보 부족 | 사용자에게 추가 정보 요청, 최소 정보로 초안 작성 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 검증 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 부호 불일치 | drawing-designer와 specification-writer가 상호 조율 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "IoT 기반 스마트 화분 자동 급수 시스템에 대한 특허 명세서를 작성해줘. 토양 수분 센서로 측정하고, AI가 식물 종류에 따라 급수량을 조절하는 시스템이야."
**기대 결과**:
- 선행기술 조사: IoT 급수 시스템, 스마트 화분 관련 선행특허 5건 이상
- 청구항: 장치 독립항 + 방법 독립항 + 종속항 5개 이상
- 명세서: 기술 분야~실시예까지 완전한 구성
- 도면: 시스템 블록도 + 상세 구조도 + 플로우차트
- 검증: 정합성 매트릭스 전항목 확인

### 부분 흐름
**프롬프트**: "이 발명 아이디어로 선행기술 조사만 해줘"
**기대 결과**:
- 조사 모드로 전환 (prior-art-researcher 단독)
- 선행기술 목록 + 심층 분석 + 신규성/진보성 평가

### 에러 흐름
**프롬프트**: "특허 명세서 써줘, 아이디어는 새로운 배터리 기술이야"
**기대 결과**:
- 풀 파이프라인 실행, 발명 상세 정보 부족으로 추가 질문
- 최소 정보로 초안 작성 시 "발명자 확인 필요" 항목 다수 명시
- 검증 보고서에 "상세 정보 보완 후 재작성 권고" 포함

## 에이전트별 확장 스킬

| 에이전트 | 확장 스킬 | 용도 |
|---------|----------|------|
| claim-drafter, patent-reviewer | `claim-drafting-patterns` | 청구항 작성 패턴, 권리범위 설계 전략 |
| prior-art-researcher | `prior-art-search-strategy` | 선행기술 검색 전략, 신규성·진보성 분석 프레임워크 |
