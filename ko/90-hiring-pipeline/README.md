# Hiring Pipeline Harness

채용 프로세스: JD작성→소싱→스크리닝→면접→평가→오퍼까지 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── jd-writer.md              — JD 작성 (직무기술서, 자격요건, 채용공고)
│   ├── sourcing-specialist.md    — 소싱 (채널전략, 탤런트풀, 아웃리치)
│   ├── screening-expert.md       — 스크리닝 (서류평가, 사전과제, 전화면접)
│   ├── interview-designer.md     — 면접 설계 (구조화면접, 질문설계, 평가표)
│   └── offer-coordinator.md      — 평가·오퍼 (최종평가, 보상패키지, 오퍼레터)
├── skills/
│   ├── hiring-pipeline/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── competency-model/
│   │   └── SKILL.md              — 역량 모델 설계 (jd-writer 확장)
│   └── interview-scorecard/
│       └── SKILL.md              — 구조화 면접 설계 (interview-designer 확장)
└── README.md                     — 이 파일
```

## 사용법

`/hiring-pipeline` 스킬을 트리거하거나, "채용 프로세스 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_job_description.md` — 직무기술서 및 채용공고
- `02_sourcing_strategy.md` — 소싱 전략
- `03_screening_framework.md` — 스크리닝 프레임워크
- `04_interview_design.md` — 면접 설계서
- `05_evaluation_offer.md` — 최종 평가 및 오퍼 가이드
