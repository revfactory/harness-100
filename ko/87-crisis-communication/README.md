# Crisis Communication Harness

위기 상황 발생 시 상황파악→메시지전략→보도자료→Q&A→모니터링까지 에이전트 팀이 협업하여 통합 위기소통 패키지를 생성하는 하네스.

## 구조

```

├── agents/
│   ├── situation-analyst.md      — 상황 분석 (사실관계, 이해관계자, 위기등급)
│   ├── message-strategist.md     — 메시지 전략 (핵심메시지, 톤, 채널전략)
│   ├── press-release-writer.md   — 보도자료 작성 (공식입장문, 타임라인)
│   ├── qa-preparer.md            — Q&A 준비 (예상질문, 답변가이드, 브리핑시트)
│   └── media-monitor.md          — 미디어 모니터링 (여론추적, 리스크감지, 후속대응)
├── skills/
│   ├── crisis-communication/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── stakeholder-mapping/
│   │   └── SKILL.md              — 이해관계자 매핑 프레임워크 (situation-analyst 확장)
│   └── media-response-templates/
│       └── SKILL.md              — 미디어 대응 템플릿 (press-release-writer 확장)
└── README.md                     — 이 파일
```

## 사용법

`/crisis-communication` 스킬을 트리거하거나, "위기 대응 커뮤니케이션 준비해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_situation_analysis.md` — 상황 분석 보고서
- `02_message_strategy.md` — 메시지 전략서
- `03_press_release.md` — 보도자료/공식 입장문
- `04_qa_briefing.md` — Q&A 브리핑 시트
- `05_monitoring_plan.md` — 모니터링 계획 및 후속 대응 가이드
