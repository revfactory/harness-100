---
name: podcast-studio
description: "팟캐스트 에피소드의 기획, 리서치, 대본, 쇼노트, 배포 전략을 에이전트 팀이 협업하여 한 번에 생성하는 풀 프로덕션 파이프라인. '팟캐스트 기획해줘', '에피소드 대본 써줘', '팟캐스트 스크립트', '팟캐스트 쇼노트 만들어줘', '에피소드 기획', '인터뷰 대본', '팟캐스트 배포', '오디오 콘텐츠 기획' 등 팟캐스트 제작 전반에 이 스킬을 사용한다. 기존 대본이나 리서치가 있는 경우에도 쇼노트나 배포 패키지 제작을 지원한다. 단, 실제 오디오 녹음/편집(Audacity, GarageBand), 팟캐스트 호스팅 API 연동, RSS 피드 기술적 설정은 이 스킬의 범위가 아니다."
---

# Podcast Studio — 팟캐스트 풀 프로덕션 파이프라인

팟캐스트 에피소드의 기획→리서치→대본→쇼노트→배포를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| researcher | `agents/researcher.md` | 주제 조사, 팩트체크, 토킹포인트 도출 | general-purpose |
| scriptwriter | `agents/scriptwriter.md` | 에피소드 대본 작성, 대화 큐 삽입 | general-purpose |
| shownote-editor | `agents/shownote-editor.md` | 쇼노트, 타임스탬프, 참고자료 정리 | general-purpose |
| distribution-manager | `agents/distribution-manager.md` | 플랫폼별 메타데이터, 홍보 카피 | general-purpose |
| production-reviewer | `agents/production-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **주제/키워드**: 에피소드가 다룰 주제
   - **팟캐스트 정보** (선택): 채널 톤, 청취자 규모, 기존 에피소드 방향
   - **에피소드 유형** (선택): 솔로/대담/패널/스토리텔링/Q&A
   - **게스트 정보** (선택): 게스트 이름, 전문 분야
   - **제약 조건** (선택): 에피소드 길이, 특정 요구사항
   - **기존 파일** (선택): 사용자가 제공한 대본, 리서치 자료 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 주제 리서치 | researcher | 없음 | `_workspace/01_research_brief.md` |
| 2 | 대본 작성 | scriptwriter | 작업 1 | `_workspace/02_script.md` |
| 3a | 쇼노트 작성 | shownote-editor | 작업 1, 2 | `_workspace/03_shownotes.md` |
| 3b | 배포 패키지 | distribution-manager | 작업 1, 2 | `_workspace/04_distribution_package.md` |
| 4 | 프로덕션 리뷰 | production-reviewer | 작업 2, 3a, 3b | `_workspace/05_review_report.md` |

작업 3a(쇼노트)와 3b(배포)는 **병렬 실행**한다. 둘 다 작업 2(대본)에 의존하므로 대본 완성 후 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- researcher 완료 → scriptwriter에게 토킹포인트·팩트 전달, shownote-editor에게 참고자료 전달, distribution-manager에게 트렌드 키워드 전달
- scriptwriter 완료 → shownote-editor에게 세그먼트별 타임코드 전달, distribution-manager에게 핵심 인용구 전달
- shownote-editor 완료 → distribution-manager에게 에피소드 요약·인용구 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 리서치 브리프 — `01_research_brief.md`
   - 에피소드 대본 — `02_script.md`
   - 쇼노트 — `03_shownotes.md`
   - 배포 패키지 — `04_distribution_package.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "팟캐스트 에피소드 기획해줘", "풀 프로덕션" | **풀 파이프라인** | 5명 전원 |
| "대본만 써줘", "스크립트만" | **대본 모드** | researcher + scriptwriter + reviewer |
| "이 대본으로 쇼노트 만들어줘" (기존 파일) | **쇼노트 모드** | shownote-editor + reviewer |
| "에피소드 홍보 카피 만들어줘" (기존 대본 있음) | **배포 모드** | distribution-manager + reviewer |
| "이 대본 검토해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 대본, 리서치 자료 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

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
| 웹 검색 실패 | 리서처가 일반 지식 기반으로 작업, 보고서에 "데이터 제한" 명시 |
| 게스트 정보 미확인 | 범용 인터뷰 프레임워크 제공, 사용자에게 게스트 정보 요청 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "AI 윤리에 대한 30분짜리 대담 팟캐스트 에피소드를 기획해줘. 게스트는 AI 연구자"
**기대 결과**:
- 리서치: AI 윤리 최신 이슈 5건 이상, 게스트 사전조사, 토킹포인트 5개
- 대본: 30분 분량(약 7,500단어 한국어 기준), 오프닝+3~4세그먼트+클로징, 게스트 질문 포함
- 쇼노트: 타임스탬프, 참고자료 링크, 핵심 인용구
- 배포: 플랫폼별 설명문, SNS 카피 3종, 홍보 캘린더
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 대본 파일로 쇼노트랑 배포 패키지 만들어줘" + 대본 파일 첨부
**기대 결과**:
- 기존 대본을 `_workspace/02_script.md`로 복사
- 쇼노트 모드 + 배포 모드 병합: shownote-editor + distribution-manager + reviewer 투입
- researcher, scriptwriter는 건너뜀

### 에러 흐름
**프롬프트**: "팟캐스트 대본만 빨리 써줘, 주제는 아무거나"
**기대 결과**:
- 대본 모드로 전환 (researcher + scriptwriter + reviewer)
- 주제가 불분명하므로 리서처가 트렌드 기반 주제 3개 제안 후 진행
- 리뷰 보고서에 "쇼노트/배포 패키지 미생성" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| scriptwriter | `/interview-techniques` | DEPTH 질문 모델, 감정 곡선, 유형별 질문 패턴 |
| scriptwriter, shownote-editor | `/audio-storytelling` | 5가지 서사 아크, BPM 페이싱, 12가지 오디오 장치 |
| distribution-manager | `/podcast-growth` | 플랫폼별 메타데이터 최적화, 7일 홍보 캘린더, HIKE 카피 공식 |
