# IP Portfolio Harness

지식재산 포트폴리오 관리의 IP현황분석→특허·상표·저작권매핑→갱신일정→라이선스전략→보호전략보고서를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── ip-analyst.md             — IP 분석가 (현황 파악, 가치 평가, 포트폴리오 맵)
│   ├── patent-mapper.md          — 특허·상표·저작권 매퍼 (IP 자산 분류, 등록현황)
│   ├── renewal-scheduler.md      — 갱신 일정 관리자 (기한 관리, 비용 산정)
│   ├── license-strategist.md     — 라이선스 전략가 (수익화, 크로스라이선스)
│   └── protection-advisor.md     — 보호 전략 수립자 (침해 대응, 방어 전략)
├── skills/
│   ├── ip-portfolio/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── patent-valuation/
│   │   └── SKILL.md              — 특허 가치 평가 (ip-analyst 확장)
│   └── ip-landscape-analysis/
│       └── SKILL.md              — IP 랜드스케이프 분석 (patent-mapper 확장)
└── README.md                     — 이 파일
```

## 사용법

`/ip-portfolio` 스킬을 트리거하거나, "IP 포트폴리오 관리해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_ip_analysis.md` — IP 현황 분석서
- `02_ip_map.md` — 특허·상표·저작권 매핑
- `03_renewal_schedule.md` — 갱신 일정 관리표
- `04_license_strategy.md` — 라이선스 전략서
- `05_protection_report.md` — 보호 전략 보고서
- `06_review_report.md` — 통합 리뷰 보고서
