---
name: game-narrative
description: "게임 스토리, 퀘스트, 대사, 분기 시나리오를 에이전트 팀이 협업하여 한 번에 설계하는 풀 내러티브 파이프라인. '게임 시나리오 만들어줘', '게임 스토리 설계', '퀘스트 디자인', '게임 대사 작성', '분기 시나리오', '세계관 설계', 'NPC 대사', '게임 시나리오 분기', '인터랙티브 스토리' 등 게임 내러티브 설계 전반에 이 스킬을 사용한다. 기존 세계관이나 스토리가 있는 경우에도 퀘스트/대사/분기 설계를 지원한다. 단, 게임 프로그래밍, 레벨 디자인(지형/맵), 게임 밸런싱(수치), UI/UX 설계는 이 스킬의 범위가 아니다."
---

# Game Narrative — 게임 내러티브 풀 설계 파이프라인

게임의 세계관→퀘스트→대사→분기를 에이전트 팀이 협업하여 한 번에 설계한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| worldbuilder | `agents/worldbuilder.md` | 세계관, 세력, 인물 설계 | general-purpose |
| quest-designer | `agents/quest-designer.md` | 메인/사이드 퀘스트 설계 | general-purpose |
| dialogue-writer | `agents/dialogue-writer.md` | NPC 대사, 선택지, 컷신 | general-purpose |
| branch-architect | `agents/branch-architect.md` | 분기 구조, 엔딩, 플래그 | general-purpose |
| narrative-reviewer | `agents/narrative-reviewer.md` | 정합성, 플롯홀 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **게임 장르**: RPG/어드벤처/비주얼노벨/MMORPG 등
   - **세계관 방향**: 판타지/SF/현대/역사 등
   - **스토리 톤**: 다크/라이트/유머/서사적
   - **예상 규모**: 플레이타임, 퀘스트 수
   - **기존 설정** (선택): 사용자가 제공한 세계관, 캐릭터 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 세계관 설계 | worldbuilder | 없음 | `_workspace/01_worldbuilding.md` |
| 2 | 퀘스트 설계 | quest-designer | 작업 1 | `_workspace/02_quest_design.md` |
| 3a | 대사 작성 | dialogue-writer | 작업 1, 2 | `_workspace/03_dialogue_script.md` |
| 3b | 분기 설계 | branch-architect | 작업 1, 2 | `_workspace/04_branch_map.md` |
| 4 | 내러티브 검증 | narrative-reviewer | 작업 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(대사)와 3b(분기)는 **병렬 실행**한다. 둘 다 작업 2(퀘스트)에 의존하므로 퀘스트 설계 완성 후 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- worldbuilder 완료 → quest-designer에게 세력·인물·장소 전달, dialogue-writer에게 인물 성격·말투 전달, branch-architect에게 세력 관계·세계 규칙 전달
- quest-designer 완료 → dialogue-writer에게 퀘스트별 대사 목록 전달, branch-architect에게 분기 포인트 전달
- dialogue-writer ↔ branch-architect: 선택지와 분기 플래그를 상호 조율
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 세계관 설정 — `01_worldbuilding.md`
   - 퀘스트 설계 — `02_quest_design.md`
   - 대사 스크립트 — `03_dialogue_script.md`
   - 분기 구조도 — `04_branch_map.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "게임 시나리오 전체 설계", "풀 내러티브" | **풀 파이프라인** | 5명 전원 |
| "세계관만 설계해줘" | **세계관 모드** | worldbuilder + narrative-reviewer |
| "이 세계관으로 퀘스트 만들어줘" (기존 파일) | **퀘스트 모드** | quest-designer + dialogue-writer + narrative-reviewer |
| "NPC 대사만 써줘" (기존 퀘스트 있음) | **대사 모드** | dialogue-writer + narrative-reviewer |
| "분기 시나리오만 설계해줘" (기존 퀘스트 있음) | **분기 모드** | branch-architect + narrative-reviewer |

**기존 파일 활용**: 사용자가 세계관, 퀘스트 등 기존 설정을 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 장르/배경 불명확 | 세계관설계자가 3가지 컨셉 제안, 사용자 선택 후 진행 |
| 기존 IP 기반 요청 | 원작 설정 존중, 확장 가능 부분만 창작, 저작권 주의사항 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "스팀펑크 세계관의 RPG 게임 시나리오를 만들어줘. 메인 퀘스트 5개, 3가지 엔딩"
**기대 결과**:
- 세계관: 스팀펑크 세계 설정, 3개 이상 세력, 핵심 인물 5명+, 역사 타임라인
- 퀘스트: 메인 5개 + 사이드 3~5개, 보상 테이블, 난이도 곡선
- 대사: 컷신 5개+, NPC 대화 10명+, 바크 테이블
- 분기: 핵심 분기점 3~5개, 엔딩 3개+히든 1개, 플래그 시스템
- 리뷰: 정합성 매트릭스 전항목, 분기 경로 시뮬레이션

### 기존 파일 활용 흐름
**프롬프트**: "이 세계관 설정으로 퀘스트와 대사를 만들어줘" + 세계관 문서 첨부
**기대 결과**:
- 기존 세계관을 `_workspace/01_worldbuilding.md`로 복사
- 퀘스트 모드: quest-designer + dialogue-writer + narrative-reviewer 투입
- worldbuilder는 건너뜀

### 에러 흐름
**프롬프트**: "게임 시나리오 만들어줘, 장르는 알아서"
**기대 결과**:
- 세계관설계자가 판타지/SF/포스트아포칼립스 3가지 컨셉 제안
- 사용자 선택 후 풀 파이프라인 진행
- 리뷰 보고서에 "사용자 선택 기반 진행" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| quest-designer | `/quest-design-patterns` | 12가지 퀘스트 아키타입, DRIP 보상 모델, 난이도 곡선 |
| dialogue-writer | `/dialogue-systems` | VOICE 캐릭터 보이스, 선택지 심리학, 바크 시스템, 컷신 연출 |
| branch-architect | `/branching-logic` | 6가지 분기 패턴, 플래그 시스템 설계, 엔딩 아키텍처 |
