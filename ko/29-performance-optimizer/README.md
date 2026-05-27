# Performance Optimizer Harness

성능 최적화의 프로파일링→병목분석→최적화→벤치마크를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── profiler.md              — 프로파일러 (CPU, 메모리, I/O, 네트워크 프로파일링)
│   ├── bottleneck-analyst.md    — 병목 분석가 (핫스팟 식별, 근본원인, 영향산정)
│   ├── optimization-engineer.md — 최적화 엔지니어 (코드/쿼리/아키텍처 최적화)
│   ├── benchmark-manager.md     — 벤치마크 관리자 (테스트설계, 실행, 비교분석)
│   └── perf-reviewer.md         — 성능 리뷰어 (교차검증, 회귀방지, 최종보고서)
├── skills/
│   ├── performance-optimizer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── query-optimization-patterns/
│   │   └── SKILL.md              — 쿼리 최적화 패턴 가이드
│   └── caching-strategy-selector/
│       └── SKILL.md              — 캐싱 전략 선택 가이드
└── README.md                    — 이 파일
```

## 사용법

`/performance-optimizer` 스킬을 트리거하거나, "성능 최적화해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_profiling_report.md` — 프로파일링 결과
- `02_bottleneck_analysis.md` — 병목 분석 보고서
- `03_optimization_plan.md` — 최적화 계획 및 구현
- `04_benchmark_results.md` — 벤치마크 결과 및 비교
- `05_review_report.md` — 리뷰 보고서
