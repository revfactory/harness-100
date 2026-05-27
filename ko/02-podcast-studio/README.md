# Podcast Studio Harness

팟캐스트 콘텐츠의 기획→리서치→대본→쇼노트→배포 전략을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── researcher.md          — 리서치 (주제 심층 조사, 팩트체크, 참고자료 정리)
│   ├── scriptwriter.md        — 대본 작성 (오프닝, 세그먼트, 대화 큐, 클로징)
│   ├── shownote-editor.md     — 쇼노트 편집 (타임스탬프, 요약, 링크, 참고자료)
│   ├── distribution-manager.md — 배포 관리 (플랫폼별 메타데이터, 홍보 카피)
│   └── production-reviewer.md — 교차 검증 (리서치↔대본↔쇼노트↔배포 정합성)
├── skills/
│   ├── podcast-studio/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── interview-techniques/
│   │   └── SKILL.md           — scriptwriter 확장 (DEPTH 질문 모델, 감정 곡선)
│   ├── audio-storytelling/
│   │   └── SKILL.md           — scriptwriter+shownote-editor 확장 (서사 아크, BPM 페이싱)
│   └── podcast-growth/
│       └── SKILL.md           — distribution-manager 확장 (플랫폼 최적화, HIKE 카피)
└── README.md                  — 이 파일
```

## 사용법

`/podcast-studio` 스킬을 트리거하거나, "팟캐스트 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_research_brief.md` — 리서치 브리프
- `02_script.md` — 팟캐스트 대본
- `03_shownotes.md` — 쇼노트
- `04_distribution_package.md` — 배포 패키지
- `05_review_report.md` — 리뷰 보고서
