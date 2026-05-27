# Public Speaking Harness

퍼블릭스피킹 종합의 연설문→발표대본→토론준비서→Q&A예상답변→리허설가이드를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── audience-analyst.md     — 청중 분석 (타깃 청중, 맥락, 기대)
│   ├── speech-writer.md        — 연설/발표 작가 (연설문, 발표대본)
│   ├── debate-preparer.md      — 토론 준비 전문가 (논증, 반론, 교차심문)
│   ├── qa-strategist.md        — Q&A 전략가 (예상 질문, 답변 전략)
│   └── rehearsal-coach.md      — 리허설 코치 및 교차 검증 (전달력, 정합성)
├── skills/
│   ├── public-speaking/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── rhetoric-patterns/
│   │   └── SKILL.md           — 수사학 패턴 라이브러리 (speech-writer 확장)
│   └── audience-engagement/
│       └── SKILL.md           — 청중 참여 전략 (audience-analyst 확장)
└── README.md                  — 이 파일
```

## 사용법

`/public-speaking` 스킬을 트리거하거나, "연설문 써줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_audience_analysis.md` — 청중 분석 보고서
- `02_speech_script.md` — 연설문/발표 대본
- `03_debate_prep.md` — 토론 준비서
- `04_qa_playbook.md` — Q&A 예상 답변집
- `05_rehearsal_guide.md` — 리허설 가이드 및 검증 보고서
