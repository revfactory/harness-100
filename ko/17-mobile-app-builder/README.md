# Mobile App Builder Harness

모바일 앱의 UI/UX 설계→네이티브 코드 생성→API 연동→스토어 배포 준비를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── ux-designer.md        — UX/UI 설계 (와이어프레임, 디자인 시스템, 인터랙션)
│   ├── app-developer.md      — 네이티브/크로스플랫폼 앱 개발 (Swift, Kotlin, Flutter, RN)
│   ├── api-integrator.md     — API 연동 (REST/GraphQL 클라이언트, 인증, 캐싱)
│   ├── store-manager.md      — 스토어 배포 (메타데이터, 스크린샷, 심사 대응)
│   └── qa-engineer.md        — 품질 검증 (UI 테스트, 성능, 접근성, 보안)
├── skills/
│   ├── mobile-app-builder/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── mobile-ux-patterns/
│   │   └── SKILL.md           — UX디자이너 확장 (iOS HIG/Material 3, 네비게이션, 디자인 토큰)
│   └── app-store-optimization/
│       └── SKILL.md           — 스토어매니저 확장 (ASO 메타데이터, 키워드 전략, 심사 대응)
└── README.md                  — 이 파일
```

## 사용법

`/mobile-app-builder` 스킬을 트리거하거나, "모바일 앱 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_ux_design.md` — UX/UI 설계 문서
- `02_app_code/` — 앱 소스 코드
- `02_app_architecture.md` — 앱 아키텍처 문서
- `03_api_integration.md` — API 연동 명세
- `04_store_listing.md` — 스토어 배포 메타데이터
- `05_qa_report.md` — QA 검증 보고서
