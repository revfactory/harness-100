---
name: web-scraper
description: "웹 스크래핑 시스템을 에이전트 팀이 협업하여 구축하는 풀 파이프라인. '웹 스크래핑 만들어줘', '크롤러 개발해줘', '사이트 데이터 수집', '웹 크롤링 시스템', '스크래퍼 구축', '데이터 수집 자동화', '사이트 파싱', '웹 데이터 추출' 등 웹 스크래핑 시스템 구축 전반에 이 스킬을 사용한다. 특정 사이트 분석만 필요한 경우에도 대상분석 모드로 지원한다. 단, 실시간 스트리밍 데이터 처리(Kafka/Flink), 브라우저 자동화 테스트(Selenium 테스트), 웹사이트 성능 모니터링은 이 스킬의 범위가 아니다."
---

# Web Scraper — 웹 스크래핑 시스템 구축 파이프라인

웹 스크래핑 시스템의 대상분석→크롤러설계→파싱→저장→모니터링을 에이전트 팀이 협업하여 구축한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| target-analyst | `agents/target-analyst.md` | 대상 사이트 분석, 리스크 평가 | general-purpose |
| crawler-developer | `agents/crawler-developer.md` | 크롤러 아키텍처 및 구현 | general-purpose |
| parser-engineer | `agents/parser-engineer.md` | 파싱 로직 설계 및 구현 | general-purpose |
| data-manager | `agents/data-manager.md` | 데이터 저장·검증·내보내기 | general-purpose |
| monitor-operator | `agents/monitor-operator.md` | 모니터링·알림·스케줄링 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 사이트 URL**: 스크래핑할 웹사이트
    - **수집 데이터**: 어떤 데이터를 추출할 것인가
    - **용도**: 수집 데이터의 활용 목적 (분석/모니터링/아카이빙)
    - **규모**: 예상 데이터 볼륨, 수집 빈도
    - **제약 조건** (선택): 기술 스택 제한, 예산, 법적 요구사항
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. `_workspace/src/` 디렉토리를 생성한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 대상 사이트 분석 | analyst | 없음 | `_workspace/01_target_analysis.md` |
| 2a | 크롤러 설계·구현 | crawler | 작업 1 | `_workspace/02_crawler_design.md` + `src/` |
| 2b | 파싱 로직 설계·구현 | parser | 작업 1 | `_workspace/03_parser_logic.md` + `src/` |
| 3 | 데이터 저장 설계 | data-mgr | 작업 2b | `_workspace/04_data_storage.md` + `src/` |
| 4 | 모니터링 설정 | monitor | 작업 2a, 2b, 3 | `_workspace/05_monitor_config.md` + `src/` |

작업 2a(크롤러)와 2b(파서)는 **병렬 실행**한다. 둘 다 작업 1(분석)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- analyst 완료 → crawler에게 URL 패턴·안티봇·rate limit 전달, parser에게 데이터 포인트·DOM 구조 전달
- crawler 완료 → parser에게 원본 데이터 형식 전달, monitor에게 크롤러 상태 체크포인트 전달
- parser 완료 → data-mgr에게 데이터 스키마 전달, monitor에게 파싱 메트릭 전달
- data-mgr 완료 → monitor에게 데이터 품질 메트릭 전달
- monitor는 모든 컴포넌트를 통합하여 운영 설정 완성

### Phase 3: 통합 및 최종 산출물

모든 에이전트의 작업이 완료되면 통합한다:

1. `_workspace/` 내 모든 파일과 `src/` 코드를 확인한다
2. 컴포넌트 간 인터페이스 정합성을 검증한다
3. 실행 가능한 통합 스크립트(`_workspace/src/main.py`)를 생성한다
4. 최종 요약을 사용자에게 보고한다:
    - 대상 분석 — `01_target_analysis.md`
    - 크롤러 설계 — `02_crawler_design.md`
    - 파싱 로직 — `03_parser_logic.md`
    - 데이터 저장 — `04_data_storage.md`
    - 모니터링 — `05_monitor_config.md`
    - 소스코드 — `src/`

## 작업 규모별 모드

사용자 요청의 범위에 따라 투입 에이전트를 조절한다:

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "스크래핑 시스템 구축", "크롤러 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "이 사이트 분석해줘", "스크래핑 가능한지 확인" | **분석 모드** | analyst 단독 |
| "크롤러만 만들어줘" (분석 완료) | **크롤러 모드** | crawler + parser |
| "데이터 저장 구조 설계해줘" | **저장 모드** | data-manager 단독 |
| "기존 스크래퍼에 모니터링 추가" | **모니터링 모드** | monitor 단독 |

**기존 코드 활용**: 사용자가 기존 크롤러 코드를 제공하면, 해당 코드를 `_workspace/src/`에 복사하고 해당 단계의 에이전트는 코드 리뷰 및 개선에 집중한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 설계 문서 및 코드 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 코드 기반 | `_workspace/src/` | 실행 가능한 소스코드 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 대상 사이트 접근 불가 | WebSearch로 캐시 조사, 대안 URL 탐색, API 존재 확인 |
| robots.txt 전면 차단 | 공개 API/RSS/데이터 피드 대안 제시, 법적 검토 포함 |
| 안티봇 우회 불가 | 기술적 한계를 명시하고, 합법적 대안(API, 제휴) 제안 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 통합 보고서에 명시 |
| 사이트 구조 변경 | monitor가 감지 → parser에게 선택자 업데이트 요청 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "네이버 부동산 매물 데이터를 매일 수집하는 스크래핑 시스템 만들어줘"
**기대 결과**:
- 대상 분석: robots.txt 분석, API 엔드포인트 발견, 안티봇 평가
- 크롤러: httpx 비동기 기반, rate limit 준수, 재시도 로직
- 파서: 매물 정보(가격/면적/위치/층수) 추출 선택자, 검증 로직
- 저장: SQLite 스키마, upsert 기반 중복 제거, CSV 내보내기
- 모니터링: 일간 cron 스케줄, 파싱 성공률 알림, 변경 감지

### 기존 파일 활용 흐름
**프롬프트**: "이 크롤러 코드가 있는데 파싱 로직이랑 모니터링만 추가해줘" + 크롤러 코드 첨부
**기대 결과**:
- 기존 크롤러 코드를 `_workspace/src/`에 복사
- analyst와 crawler는 건너뛰고 parser + data-mgr + monitor 투입
- 기존 코드 리뷰 후 호환되는 파서 구현

### 에러 흐름
**프롬프트**: "이 사이트 데이터 수집해줘" (URL만 제공, 수집 대상 불명확)
**기대 결과**:
- analyst가 사이트를 분석하여 수집 가능한 데이터 목록 제시
- 사용자에게 수집 대상 선택을 요청
- 선택 후 나머지 파이프라인 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| anti-bot-analyzer | `skills/anti-bot-analyzer/SKILL.md` | target-analyst, crawler-developer | 안티봇 방어 계층 분류, 감지 플로우, Rate Limit 공식, 법적 리스크 체크 |
| selector-generator | `skills/selector-generator/SKILL.md` | parser-engineer, monitor-operator | CSS/XPath 선택자 생성, 견고성 점수, 변경 감지 패턴, 데이터 정제 |
