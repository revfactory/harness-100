# Course Builder Harness

온라인 강의 설계의 커리큘럼→교안→퀴즈→실습과제를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── curriculum-designer.md   — 교육설계자 (학습목표, 커리큘럼, 모듈구조)
│   ├── content-writer.md        — 콘텐츠작성자 (교안, 슬라이드, 강의노트)
│   ├── quiz-maker.md            — 퀴즈출제자 (형성평가, 총괄평가, 피드백)
│   ├── lab-designer.md          — 실습설계자 (실습과제, 프로젝트, 평가루브릭)
│   └── course-reviewer.md      — 과정검증자 (학습목표 정렬, 난이도, 품질)
├── skills/
│   ├── course-builder/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── learning-design/
│   │   └── SKILL.md             — curriculum-designer+content-writer 확장 (블룸, 가네, 인지부하)
│   ├── assessment-engineering/
│   │   └── SKILL.md             — quiz-maker 확장 (문항 설계, 오답지 심리학, 루브릭)
│   └── lab-scaffolding/
│       └── SKILL.md             — lab-designer 확장 (5단계 피라미드, 스타터코드, 캡스톤)
└── README.md                    — 이 파일
```

## 사용법

`/course-builder` 스킬을 트리거하거나, "온라인 강의 만들어줘", "커리큘럼 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_curriculum.md` — 커리큘럼/과정 설계서
- `02_lesson_plans.md` — 교안/강의노트
- `03_quizzes.md` — 퀴즈/평가 문항
- `04_labs.md` — 실습과제/프로젝트
- `05_review_report.md` — 리뷰 보고서
