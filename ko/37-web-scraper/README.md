# Web Scraper Harness

웹 스크래핑 시스템의 대상분석→크롤러설계→파싱→저장→모니터링을 에이전트 팀이 협업하여 구축하는 하네스.

## 구조

```

├── agents/
│   ├── target-analyst.md      — 대상 사이트 분석 (구조, robots.txt, 법적 검토)
│   ├── crawler-developer.md   — 크롤러 설계 및 구현 (요청전략, 세션관리, 우회)
│   ├── parser-engineer.md     — HTML/JSON 파싱 로직 (선택자, 데이터 추출)
│   ├── data-manager.md        — 데이터 저장·정제·검증 (스키마, 중복제거, 내보내기)
│   └── monitor-operator.md    — 모니터링·알림·유지보수 (헬스체크, 변경감지, 로그)
├── skills/
│   ├── web-scraper/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── anti-bot-analyzer/
│   │   └── SKILL.md           — 안티봇 분석 (방어 계층, Rate Limit, 법적 리스크)
│   └── selector-generator/
│       └── SKILL.md           — 선택자 생성 (CSS/XPath, 견고성 점수, 변경 감지)
└── README.md                  — 이 파일
```

## 사용법

`/web-scraper` 스킬을 트리거하거나, "웹 스크래핑 시스템 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_target_analysis.md` — 대상 사이트 분석 보고서
- `02_crawler_design.md` — 크롤러 설계 및 코드
- `03_parser_logic.md` — 파싱 로직 및 코드
- `04_data_storage.md` — 데이터 저장 설계
- `05_monitor_config.md` — 모니터링 설정
- `src/` — 실제 스크래핑 소스코드
