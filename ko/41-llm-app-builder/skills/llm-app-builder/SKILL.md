---
name: llm-app-builder
description: "LLM 앱을 에이전트 팀이 협업하여 개발하는 풀 파이프라인. 'LLM 앱 만들어줘', 'AI 앱 개발', 'RAG 시스템 구축', 'GPT 앱', 'AI 챗봇 개발', '프롬프트 엔지니어링', 'LLM 파이프라인', 'AI 어시스턴트 개발', '생성 AI 앱', 'RAG 파이프라인' 등 LLM 기반 앱 개발 전반에 이 스킬을 사용한다. 프롬프트 설계만 필요한 경우에도 프롬프트 모드로 지원한다. 단, LLM 모델 학습(fine-tuning 실행), GPU 인프라 구축, 모델 서빙(vLLM/TGI 배포)은 이 스킬의 범위가 아니다."
---

# LLM App Builder — LLM 앱 개발 파이프라인

LLM 앱의 프롬프트→RAG→평가→최적화→배포를 에이전트 팀이 협업하여 개발한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| prompt-engineer | `agents/prompt-engineer.md` | 프롬프트 설계 | general-purpose |
| rag-architect | `agents/rag-architect.md` | RAG 파이프라인 | general-purpose |
| eval-specialist | `agents/eval-specialist.md` | 평가 프레임워크 | general-purpose |
| optimization-engineer | `agents/optimization-engineer.md` | 비용/성능 최적화 | general-purpose |
| deploy-engineer | `agents/deploy-engineer.md` | 프로덕션 배포 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **앱 목적**: 무엇을 하는 LLM 앱인가
    - **데이터 소스**: RAG에 사용할 문서/데이터 (선택)
    - **LLM 모델**: 사용할 모델 (기본: Claude/GPT-4o)
    - **배포 환경**: API/웹앱/챗봇/내부 도구
    - **예산**: 월간 API 비용 예산
    - **제약 조건** (선택): 보안, 규정, 성능 요구사항
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. `_workspace/src/` 디렉토리를 생성한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 프롬프트 설계 | prompt | 없음 | `_workspace/01_prompt_design.md` |
| 1b | RAG 파이프라인 | rag | 없음 | `_workspace/02_rag_pipeline.md` + `src/` |
| 2 | 평가 프레임워크 | eval | 작업 1a, 1b | `_workspace/03_eval_framework.md` + `src/` |
| 3 | 최적화 | optimizer | 작업 2 | `_workspace/04_optimization.md` + `src/` |
| 4 | 배포 설정 | deploy | 작업 1b, 3 | `_workspace/05_deploy_config.md` + `src/` |

작업 1a(프롬프트)와 1b(RAG)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- prompt 완료 → rag에게 컨텍스트 주입 포맷 전달, eval에게 기대 출력 전달
- rag 완료 → eval에게 검색 테스트 데이터 전달, deploy에게 벡터DB 인프라 요구사항 전달
- eval 완료 → optimizer에게 성능 베이스라인 전달, prompt에게 약점 피드백
- optimizer 완료 → deploy에게 캐시/라우팅 설정 전달
- deploy는 모든 컴포넌트를 통합하여 프로덕션 배포 구성 완성

### Phase 3: 통합 및 최종 산출물

1. `_workspace/src/`의 코드가 실행 가능한지 확인한다
2. 평가 메트릭이 기준을 충족하는지 확인한다
3. 배포 설정이 완전한지 검증한다
4. 최종 요약을 사용자에게 보고한다:
    - 프롬프트 설계 — `01_prompt_design.md`
    - RAG 파이프라인 — `02_rag_pipeline.md`
    - 평가 프레임워크 — `03_eval_framework.md`
    - 최적화 전략 — `04_optimization.md`
    - 배포 설정 — `05_deploy_config.md`
    - 소스코드 — `src/`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "LLM 앱 만들어줘", "RAG 앱 전체" | **풀 파이프라인** | 5명 전원 |
| "프롬프트만 설계해줘" | **프롬프트 모드** | prompt + eval |
| "RAG 파이프라인만 구축" | **RAG 모드** | rag + eval + deploy |
| "LLM 앱 평가 시스템 구축" | **평가 모드** | eval 단독 |
| "기존 앱 비용 최적화" | **최적화 모드** | optimizer + eval |
| "프로덕션 배포 설정" | **배포 모드** | deploy 단독 |

**RAG 불필요 시**: 사용자가 외부 데이터 소스가 없다고 명시하면 rag 에이전트를 건너뛴다.

**기존 파일 활용**: 사용자가 기존 프롬프트, RAG 설정, 코드 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다. 예: 기존 프롬프트 제공 → `_workspace/01_prompt_design.md`로 복사 → prompt 건너뛰고 나머지 에이전트만 투입.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 설계 문서 및 설정 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 피드백 |
| 코드 기반 | `_workspace/src/` | 실행 가능한 소스코드 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| LLM API 키 없음 | 환경 변수 설정 가이드 제공, 로컬 모델 대안 제시 |
| RAG 데이터 소스 없음 | RAG 없이 순수 LLM 앱으로 구축, 추후 RAG 추가 가이드 |
| 평가 데이터셋 없음 | LLM으로 합성 데이터 생성, 수동 검증 가이드 |
| 비용 예산 초과 예상 | 소형 모델 라우팅, 캐싱 강화, 요청 제한 제안 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "회사 내부 문서를 기반으로 직원 Q&A 챗봇을 만들어줘. Confluence 문서 500개 정도야. 월 예산 $200"
**기대 결과**:
- 프롬프트: Q&A용 시스템 프롬프트, 소스 인용 강제, 환각 방지 가드레일
- RAG: Confluence → 마크다운 변환 → 시맨틱 청킹 → text-embedding-3-small → Chroma
- 평가: 20개 골든 Q&A 셋, Recall@5, 충실도 LLM-as-Judge
- 최적화: 시맨틱 캐싱(예상 히트율 40%), 소형 모델 라우팅(단순 질문)
- 배포: FastAPI + Docker + 비용 상한 $200/월

### 기존 파일 활용 흐름
**프롬프트**: "이 RAG 코드를 기반으로 평가 프레임워크와 최적화만 해줘" + RAG 코드 첨부
**기대 결과**:
- 기존 코드를 `_workspace/src/`에 복사, RAG 설계를 `_workspace/02_rag_pipeline.md`로 복사
- rag 건너뛰고 eval + optimizer + deploy 투입
- prompt는 기존 코드에서 추출

### 에러 흐름
**프롬프트**: "AI 앱 만들어줘" (목적/데이터 불명확)
**기대 결과**:
- 사용자에게 앱 목적과 데이터 소스 확인 요청
- RAG 필요 여부 판단을 위한 질문
- 확인 후 적절한 모드로 파이프라인 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| prompt-optimizer | `skills/prompt-optimizer/SKILL.md` | prompt-engineer, eval-specialist | CRISP 루브릭, RCTF 템플릿, 가드레일 패턴, A/B 테스트, 토큰 최적화 |
| chunking-strategy-guide | `skills/chunking-strategy-guide/SKILL.md` | rag-architect, eval-specialist | 청킹 전략 비교, 시맨틱 청킹 알고리즘, 문서별 전처리, 품질 메트릭 |
