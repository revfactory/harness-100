---
name: book-publishing
description: "전자책 출판의 원고 편집, 교정교열, 표지 디자인, 메타데이터 설정, 배포 준비를 에이전트 팀이 협업하여 한 번에 수행하는 풀 프로덕션 파이프라인. '전자책 출판해줘', '원고 편집해줘', '책 표지 만들어줘', '전자책 메타데이터', '도서 교정교열', '자가출판 준비', '전자책 배포', '원고 검토', 'ebook 제작' 등 전자책 출판 전반에 이 스킬을 사용한다. 기존 원고가 있는 경우에도 표지 제작이나 메타데이터 설정을 지원한다. 단, 실제 EPUB/PDF 파일 변환, 서점 계정 등록, 인쇄 발주, 마케팅 집행은 이 스킬의 범위가 아니다."
---

# Book Publishing — 전자책 출판 풀 프로덕션 파이프라인

전자책의 원고편집→교정교열→표지→메타데이터→배포설정을 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| manuscript-editor | `agents/manuscript-editor.md` | 구조편집, 문체교정, 목차 | general-purpose |
| proofreader | `agents/proofreader.md` | 맞춤법, 문법, 표기통일 | general-purpose |
| cover-designer | `agents/cover-designer.md` | 표지 컨셉, 이미지 생성 | general-purpose |
| metadata-manager | `agents/metadata-manager.md` | 분류, 설명문, 키워드, 배포 | general-purpose |
| publishing-reviewer | `agents/publishing-reviewer.md` | 품질검증, 규격확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **원고**: 편집 대상 원고 파일
   - **장르**: 비즈니스/자기계발/소설/에세이/기술서
   - **출판 목표**: 자가출판/출판사 투고/내부 배포
   - **배포 플랫폼** (선택): 교보문고, 리디북스, 아마존 KDP 등
   - **기존 파일** (선택): 편집된 원고, 표지 등
2. `_workspace/` 디렉토리와 `_workspace/covers/` 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 원고 편집 | manuscript-editor | 없음 | `_workspace/01_edited_manuscript.md` |
| 2a | 교정교열 | proofreader | 작업 1 | `_workspace/02_proofread_report.md` |
| 2b | 표지 디자인 | cover-designer | 작업 1 | `_workspace/03_cover_concept.md` |
| 3 | 메타데이터 | metadata-manager | 작업 1, 2a | `_workspace/04_metadata.md` |
| 4 | 출판 검증 | publishing-reviewer | 작업 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(교정)와 2b(표지)는 **병렬 실행**한다. 둘 다 작업 1(편집)에 의존한다.

**팀원 간 소통 흐름:**
- manuscript-editor 완료 → proofreader에게 용어 통일 목록 전달, cover-designer에게 톤·장르·타깃 전달, metadata-manager에게 제목·키워드 전달
- proofreader 완료 → metadata-manager에게 최종 표기 확정 전달
- cover-designer ↔ metadata-manager: 제목·부제·저자명 정확한 표기 교차 확인
- publishing-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 편집 원고 — `01_edited_manuscript.md`
   - 교정교열 보고서 — `02_proofread_report.md`
   - 표지 컨셉/이미지 — `03_cover_concept.md`
   - 메타데이터/배포 — `04_metadata.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "전자책 출판해줘", "풀 출판 준비" | **풀 파이프라인** | 5명 전원 |
| "원고 편집만 해줘" | **편집 모드** | manuscript-editor + proofreader + reviewer |
| "교정교열만 해줘" | **교정 모드** | proofreader + reviewer |
| "책 표지만 만들어줘" | **표지 모드** | cover-designer + reviewer |
| "메타데이터만 세팅해줘" | **메타 모드** | metadata-manager + reviewer |

**기존 파일 활용**: 사용자가 편집된 원고, 표지 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물명}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 원고 미제공 | 제목/주제에서 목차와 챕터 개요를 설계하는 "기획 모드"로 전환 |
| 표지 이미지 생성 실패 | 텍스트 컨셉과 프롬프트만으로 진행, 사용자 재시도 가능 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| ISBN 미발급 | 발급 절차 안내 포함, 나머지 메타데이터는 정상 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 원고를 전자책으로 출판하고 싶어요. 자기계발서이고, 교보문고랑 리디북스에 배포할 거예요." + 원고 파일 첨부
**기대 결과**:
- 편집: 구조 편집 + 라인 편집 의견, 목차 최적화
- 교정: 맞춤법/문법/표기 교정 보고서
- 표지: A/B 컨셉 + 이미지 생성 시도
- 메타데이터: BISAC/KDC 분류, 설명문, 키워드, 교보/리디 배포 설정
- 리뷰: 정합성 매트릭스 전항목 확인, 배포 전 체크리스트

### 기존 파일 활용 흐름
**프롬프트**: "이미 편집 끝난 원고인데, 표지랑 메타데이터만 세팅해줘" + 편집 원고 첨부
**기대 결과**:
- 편집 원고를 `_workspace/01_edited_manuscript.md`로 복사
- 표지 모드 + 메타 모드 병합: cover-designer + metadata-manager + reviewer 투입
- manuscript-editor, proofreader는 건너뜀

### 에러 흐름
**프롬프트**: "전자책 출판 준비해줘, 원고는 아직 없고 주제만 있어 — 'MZ세대 재테크'"
**기대 결과**:
- 기획 모드로 전환: manuscript-editor가 목차와 챕터 개요 설계
- 교정교열은 건너뜀 (원고 없음)
- 표지 컨셉과 메타데이터는 기획 기반으로 초안 작성
- 리뷰 보고서에 "원고 미완성, 기획 단계" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| manuscript-editor | `/developmental-editing` | SPINE 체크, 장르별 편집 기준, 페이싱 분석, 편집 보고서 포맷 |
| cover-designer | `/cover-design-psychology` | 장르별 표지 컨벤션, 타이포 전략, AI 프롬프트, A/B 테스트 |
| metadata-manager | `/book-metadata-seo` | BISAC/KDC 분류, 키워드 최적화, AIDA 설명문, 가격 심리학 |
