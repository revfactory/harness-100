---
name: knowledge-base-builder
description: "조직 지식관리 체계를 에이전트 팀이 구축하는 파이프라인. '지식베이스 만들어줘', '위키 구축', '지식 관리 체계', 'knowledge base', '사내 위키', '팀 문서 정리', '기술 문서 위키', '온보딩 문서 만들어줘', '조직 지식 정리', '문서화 체계 구축' 등 조직 지식 관리 전반에 이 스킬을 사용한다. 단, CMS 서버 구축, 데이터베이스 설치, 검색 엔진 배포 등 인프라 작업은 이 스킬의 범위가 아니다."
---

# Knowledge Base Builder — 조직 지식관리 체계 구축 파이프라인

지식 수집→분류 체계 설계→마크다운 위키 생성→검색 인덱스→유지보수 가이드를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| knowledge-collector | `agents/knowledge-collector.md` | 지식 수집·인벤토리 구성 | general-purpose |
| taxonomy-designer | `agents/taxonomy-designer.md` | 분류 체계·태그·네비게이션 설계 | general-purpose |
| wiki-builder | `agents/wiki-builder.md` | 마크다운 위키 페이지 생성 | general-purpose |
| search-optimizer | `agents/search-optimizer.md` | 검색 인덱스·메타데이터 최적화 | general-purpose |
| maintenance-planner | `agents/maintenance-planner.md` | 거버넌스·갱신 주기·품질 관리 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 조직/프로젝트**: 어떤 지식을 관리하는가
    - **대상 독자**: 누가 사용하는가
    - **기존 문서** (선택): 현재 존재하는 문서, 코드베이스
    - **플랫폼 선호** (선택): MkDocs, Docusaurus, Notion, GitHub Wiki 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 문서가 있으면 분석 대상으로 지정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 지식 수집 | knowledge-collector | 없음 | `_workspace/01_knowledge_inventory.md` |
| 2 | 분류 체계 설계 | taxonomy-designer | 작업 1 | `_workspace/02_taxonomy.md` |
| 3a | 위키 페이지 생성 | wiki-builder | 작업 1, 2 | `_workspace/03_wiki/` |
| 3b | 검색 인덱스 | search-optimizer | 작업 1, 2 | `_workspace/04_search_index.md` (초안) |
| 4 | 검색 인덱스 최종화 | search-optimizer | 작업 3a | `_workspace/04_search_index.md` (최종) |
| 5 | 유지보수 가이드 | maintenance-planner | 작업 1, 2, 3a | `_workspace/05_maintenance_guide.md` |

작업 3a(위키 생성)와 3b(검색 인덱스 초안)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- knowledge-collector 완료 → taxonomy-designer에게 인벤토리 전달, wiki-builder에게 원본 내용 전달
- taxonomy-designer 완료 → wiki-builder에게 구조·명명 규칙 전달, search-optimizer에게 태그 체계 전달
- wiki-builder 완료 → search-optimizer에게 페이지 목록 전달, maintenance-planner에게 구조 정보 전달
- maintenance-planner는 전체 산출물 기반으로 가이드 작성

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 위키 내 깨진 링크, 누락 페이지를 검증한다
3. 최종 요약을 사용자에게 보고한다:
    - 지식 인벤토리 — `01_knowledge_inventory.md`
    - 분류 체계 — `02_taxonomy.md`
    - 마크다운 위키 — `03_wiki/`
    - 검색 인덱스 — `04_search_index.md`
    - 유지보수 가이드 — `05_maintenance_guide.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "지식베이스 구축해줘", "위키 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "기존 문서 정리만 해줘" | **정리 모드** | knowledge-collector + taxonomy-designer |
| "분류 체계만 설계해줘" | **분류 모드** | taxonomy-designer 단독 |
| "이 구조로 위키 페이지 만들어줘" | **생성 모드** | wiki-builder + search-optimizer |
| "유지보수 가이드만 써줘" | **가이드 모드** | maintenance-planner 단독 |

**기존 파일 활용**: 기존 문서가 있으면 knowledge-collector가 분석하여 인벤토리로 변환한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 코드 탐색 | Read/Grep/Glob | 코드베이스에서 문서화 대상 추출 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 소스 접근 불가 | 사용자 설명 기반으로 지식 추론, "추론 기반" 명시 |
| 지식 범위 과다 | MVP 범위 제안, 우선순위 기반 단계적 접근 |
| 기존 분류 체계 충돌 | 기존 구조를 존중하면서 개선안 병행 제시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고에 누락 명시 |
| 위키 플랫폼 미지정 | 순수 마크다운(GitHub/MkDocs 호환)으로 기본 생성 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "우리 팀 개발 프로세스와 온보딩 문서를 위키로 만들어줘. 개발자 5명 팀이고, React + Node.js 스택이야."
**기대 결과**:
- 지식 수집: 개발 프로세스, 환경 설정, 코딩 컨벤션, 배포 절차 등 인벤토리
- 분류 체계: Getting Started, Development, Deployment, Reference 등 카테고리
- 위키: 10+ 페이지, YAML 프론트매터, 상호 링크
- 검색 인덱스: JSON 형태, 동의어 사전
- 유지보수 가이드: 거버넌스 모델, 갱신 주기

### 기존 자료 활용 흐름
**프롬프트**: "이 README 파일들을 기반으로 위키를 만들어줘" + README 파일 다수
**기대 결과**:
- knowledge-collector가 README에서 지식 추출
- 기존 구조를 분석하여 분류 체계 설계
- 마크다운 위키로 변환, 원본 내용 보존

### 에러 흐름
**프롬프트**: "회사 지식베이스 만들어줘"
**기대 결과**:
- 범위가 넓으므로 knowledge-collector가 도메인 범위 확인 질문 제안
- 일반적인 기업 지식 구조 템플릿 기반으로 MVP 제안
- 유지보수 가이드에 "단계적 확장 로드맵" 포함

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| taxonomy-designer | `information-architecture` | IA 4대 체계, 카드 소팅, 사이트맵 설계, 태그 거버넌스 |
| maintenance-planner, wiki-builder | `content-lifecycle-manager` | 생명주기 5단계, 품질 스코어카드, RACI 거버넌스, 콘텐츠 감사 |
