# Documentary Research Harness

다큐멘터리 리서치·구성안·인터뷰질문·내레이션 대본을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── researcher.md           — 리서처 (자료조사, 팩트확인, 통계수집)
│   ├── story-architect.md      — 구성작가 (3막 구성안, 씬 분할, 서사 아크)
│   ├── interviewer.md          — 인터뷰어 (인터뷰 대상 선정, 질문 설계)
│   ├── narrator.md             — 내레이터 (내레이션 대본, 톤, 리듬)
│   └── fact-checker.md         — 팩트체커 (교차검증, 출처확인, 정합성)
├── skills/
│   ├── documentary-research/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── investigative-research/
│   │   └── SKILL.md            — researcher+fact-checker 확장 (PRIMA, CRAAP, 삼각검증)
│   ├── narrative-structure/
│   │   └── SKILL.md            — story-architect+narrator 확장 (5 서사유형, 감정곡선)
│   └── interview-design/
│       └── SKILL.md            — interviewer 확장 (VOICE 대상선정, 깔때기 모델, 윤리)
└── README.md                   — 이 파일
```

## 사용법

`/documentary-research` 스킬을 트리거하거나, "다큐멘터리 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_research_brief.md` — 리서치 브리프
- `02_structure.md` — 구성안/구조 설계
- `03_interview_guide.md` — 인터뷰 가이드
- `04_narration_script.md` — 내레이션 대본
- `05_review_report.md` — 팩트체크/리뷰 보고서
