# Web Scraper Codex Harness

이 폴더는 기존 web scraper 하네스를 Codex에서 바로 사용할 수 있도록 정리한 스킬입니다.

## 구조

```
.codex/
├── AGENTS.md
└── skills/
    └── web-scraper/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── role-guides.md
            ├── anti-bot-and-compliance.md
            └── selector-patterns.md
```

## 사용법

`web-scraper` 스킬은 안전하고 준수 가능한 웹 스크래핑 분석, 크롤러/파서 구현, 데이터 저장, 모니터링 작업에 사용합니다.

사용 예:

- "이 사이트 스크래핑 가능한지 분석해줘"
- "이 URL에서 제목과 가격을 수집하는 크롤러 만들어줘"
- "기존 스크래퍼에 파싱 로직과 모니터링을 추가해줘"

## 출력물 위치

모든 출력물은 `_workspace/날짜/순번-작업명/` 하위에 저장합니다.

예:

```text
_workspace/2026-05-16/01-news-price-scraper/
├── 00_input.md
├── 01_target_analysis.md
├── 02_crawler_design.md
├── 03_parser_logic.md
├── 04_data_storage.md
├── 05_monitor_config.md
└── src/
```

같은 날짜에 작업 폴더가 이미 있으면 `01`, `02`, `03`처럼 다음 순번을 사용합니다.
