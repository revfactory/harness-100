---
name: investor-report
description: "투자자 보고서를 재무 실적 분석, KPI 대시보드, 시장 동향, 전략 업데이트, 리스크 공시로 체계화하는 풀 파이프라인. '투자자 보고서 만들어줘', 'IR 보고서', '분기 보고서', '주주 보고서', '실적 보고서', '투자자 업데이트', 'KPI 대시보드', '재무 분석 보고서', '사업 보고서', '경영 실적' 등 투자자 커뮤니케이션 전반에 이 스킬을 사용한다. 기존 재무 데이터나 KPI가 있는 경우에도 분석·보고서화를 지원한다. 단, 회계 감사, 법정 공시 문서, 증권 신고서, 주식 발행 실무는 이 스킬의 범위가 아니다."
---

# Investor Report — 투자자 보고서 풀 파이프라인

투자자 보고서의 재무→KPI→시장→전략→리스크를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| financial-analyst | `agents/financial-analyst.md` | P&L, 현금흐름, 재무지표 | general-purpose |
| kpi-designer | `agents/kpi-designer.md` | KPI 선정, 트렌드, 벤치마크 | general-purpose |
| market-analyst | `agents/market-analyst.md` | 산업 트렌드, 경쟁, 규제 | general-purpose |
| strategy-updater | `agents/strategy-updater.md` | 전략 진행, 로드맵, 리스크, 통합 | general-purpose |
| ir-reviewer | `agents/ir-reviewer.md` | 교차 검증, 수치 정합성 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **기업 정보**: 기업명, 산업, 단계(스타트업/성장/상장)
    - **보고 기간**: 분기/반기/연간, 대상 기간
    - **재무 데이터**: P&L, 현금흐름, KPI 등 (파일 또는 텍스트)
    - **전략 정보** (선택): 기존 전략, 이니셔티브 진행 상황
    - **대상 투자자**: VC/PE/상장 주주/채권자
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 재무 분석 | financial-analyst | 없음 | `_workspace/01_financial_analysis.md` |
| 1b | 시장 동향 | market-analyst | 없음 | `_workspace/03_market_trends.md` |
| 2 | KPI 대시보드 | kpi-designer | 작업 1a | `_workspace/02_kpi_dashboard.md` |
| 3 | 전략+리스크+통합 | strategy-updater | 작업 1a,1b,2 | `_workspace/04_strategy_update.md`, `_workspace/06_investor_report_final.md` |
| 4 | IR 리뷰 | ir-reviewer | 작업 1a,1b,2,3 | `_workspace/05_review_report.md` |

작업 1a(재무)와 1b(시장)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- financial-analyst 완료 → kpi-designer에게 재무 KPI 데이터 전달, market-analyst에게 매출 변동 요인 분석 요청
- market-analyst 완료 → kpi-designer에게 벤치마크 데이터 전달, strategy-updater에게 시사점 전달
- kpi-designer 완료 → strategy-updater에게 KPI 달성 현황 전달
- strategy-updater 완료 → ir-reviewer에게 모든 문서 + 최종 통합 보고서 전달
- ir-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 통합 보고서(`06_investor_report_final.md`)를 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "투자자 보고서 만들어줘", "IR 풀 리포트" | **풀 파이프라인** | 5명 전원 |
| "재무 분석만 해줘" | **재무 모드** | financial-analyst + reviewer |
| "KPI 대시보드 만들어줘" | **KPI 모드** | kpi-designer + reviewer |
| "시장 동향 보고서 써줘" | **시장 모드** | market-analyst + reviewer |
| "이 보고서 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 재무 데이터 불완전 | 제공 데이터로 가능한 분석 수행, 누락 항목 명시 |
| 웹 검색 실패 | 일반 시장 지식 기반 작업, "데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 수치 불일치 | 재무분석가를 기준(Source of Truth)으로 통일 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "시리즈B SaaS 스타트업의 2024년 Q4 투자자 보고서를 만들어줘. ARR 80억, 매출 성장률 120% YoY, NRR 115%, 직원 60명이야. 주요 투자자는 A벤처캐피탈이야"
**기대 결과**:
- 재무: SaaS 특화 P&L 분석, ARR/MRR 트렌드, 현금 Runway
- KPI: SaaS 핵심 메트릭(ARR, NRR, CAC, LTV, Rule of 40) 대시보드
- 시장: SaaS 시장 트렌드, 경쟁 동향
- 전략: 성장 전략 업데이트, 채용 계획, 리스크 공시
- 통합: VC 대상 투자자 보고서 완성본

### 기존 파일 활용 흐름
**프롬프트**: "이 재무 데이터로 투자자 보고서 만들어줘" + 엑셀/CSV 데이터 첨부
**기대 결과**:
- 재무 데이터를 기반으로 financial-analyst가 분석 (파일 참조)
- 나머지 에이전트 정상 실행
- 통합 보고서 완성

### 에러 흐름
**프롬프트**: "투자자 보고서 만들어줘, 매출 50억이야"
**기대 결과**:
- 재무 데이터 부족 → 추가 정보(비용, 성장률, KPI) 요청
- 최소 정보만 제공 시 일반적 보고서 프레임워크 생성
- "데이터 보완 후 업데이트 필요" 태그 명시

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| financial-analyst | `financial-ratio-analyzer` | DuPont 분석, SaaS 메트릭, 재무비율 5대 카테고리 체계 |
| kpi-designer | `kpi-benchmark-engine` | 산업별 KPI 벤치마크, SMART-R 선정 프레임워크, 피라미드 구조 |
| strategy-updater, ir-reviewer | `ir-narrative-builder` | Equity Story 5단계, 투자자 유형별 서사 톤, EBITDA Bridge |
