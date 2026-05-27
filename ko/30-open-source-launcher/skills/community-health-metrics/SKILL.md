---
name: community-health-metrics
description: "오픈소스 프로젝트 커뮤니티 건강도 측정 지표, GitHub 프로젝트 설정 베스트 프랙티스, 기여자 경험 최적화 가이드. '커뮤니티 건강도', 'GitHub 설정', '이슈 템플릿', 'PR 템플릿', 'CONTRIBUTING', 'Code of Conduct', '기여자 경험', 'GitHub Actions CI' 등 오픈소스 커뮤니티 운영 시 이 스킬을 사용한다. community-manager와 doc-writer의 커뮤니티 설계 역량을 강화한다. 단, 라이선스 법적 분석이나 코드 리팩토링은 이 스킬의 범위가 아니다."
---

# Community Health Metrics — 오픈소스 커뮤니티 건강도 가이드

오픈소스 프로젝트의 커뮤니티 건강을 측정하고 개선하는 프레임워크.

## 건강도 지표 체계

### CHAOSS 모델 핵심 지표

| 카테고리 | 지표 | 측정 | 건강 기준 |
|---------|------|------|----------|
| **활동** | Commit 빈도 | 주간 커밋 수 | > 5/주 |
| **활동** | 이슈 해결 시간 | 이슈 오픈→클로즈 중앙값 | < 7일 |
| **활동** | PR 리뷰 시간 | PR 제출→첫 리뷰 중앙값 | < 48시간 |
| **다양성** | 신규 기여자 비율 | 월간 첫 기여자 수 | > 2명/월 |
| **다양성** | Bus Factor | 코드 80% 기여 최소 인원 | > 2명 |
| **포용성** | 기여자 유지율 | 재기여 비율 (6개월) | > 30% |
| **포용성** | 첫 PR 머지 시간 | 첫 기여→머지 | < 1주 |

### GitHub 프로젝트 점수 카드

```markdown
## 프로젝트 건강도 체크리스트

### 필수 파일 (Must-have)
- [ ] README.md (배지, Quick Start, 설치, 사용법)
- [ ] LICENSE
- [ ] CONTRIBUTING.md
- [ ] CODE_OF_CONDUCT.md
- [ ] CHANGELOG.md

### GitHub 설정
- [ ] .github/ISSUE_TEMPLATE/ (bug, feature, question)
- [ ] .github/PULL_REQUEST_TEMPLATE.md
- [ ] .github/workflows/ (CI, 릴리스)
- [ ] .github/FUNDING.yml (선택)
- [ ] .github/SECURITY.md (취약점 보고 절차)

### 품질 도구
- [ ] CI 파이프라인 (테스트, 린트, 빌드)
- [ ] 코드 커버리지 배지
- [ ] 의존성 자동 업데이트 (Dependabot/Renovate)
- [ ] 릴리스 자동화 (semantic-release)
```

## 이슈 템플릿

### 버그 리포트

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: 버그를 발견하셨나요? 알려주세요.
labels: ["bug", "triage"]
body:
  - type: textarea
    id: description
    attributes:
      label: 버그 설명
      description: 무엇이 잘못되었나요?
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: 재현 절차
      description: 버그를 재현하는 단계를 알려주세요.
      value: |
        1.
        2.
        3.
  - type: textarea
    id: expected
    attributes:
      label: 기대 동작
  - type: textarea
    id: actual
    attributes:
      label: 실제 동작
  - type: input
    id: version
    attributes:
      label: 버전
  - type: dropdown
    id: os
    attributes:
      label: 운영체제
      options: [macOS, Windows, Linux, Other]
```

## PR 템플릿

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->
## 변경 사항
<!-- 무엇을 왜 변경했나요? -->

## 변경 유형
- [ ] 버그 수정
- [ ] 새 기능
- [ ] 문서 개선
- [ ] 리팩토링
- [ ] 테스트 추가

## 체크리스트
- [ ] 테스트를 추가/수정했습니다
- [ ] 문서를 업데이트했습니다
- [ ] CHANGELOG.md를 업데이트했습니다
- [ ] 기존 테스트가 통과합니다

## 관련 이슈
Closes #
```

## CI/CD 구성 권장

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: [18, 20, 22]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm test
      - run: npm run lint
```

## 기여자 여정 최적화

```
발견 → README → 설치 → 사용 → 이슈 보고 → 첫 PR → 정규 기여자

각 단계 최적화:
1. 발견: SEO, 소셜 미디어, 컨퍼런스
2. README: 30초 내 프로젝트 이해 가능
3. 설치: 3단계 이하, 복사-붙여넣기 가능
4. 사용: 즉시 실행 가능한 예제
5. 이슈: 템플릿으로 진입 장벽 낮춤
6. 첫 PR: "good first issue" 라벨, 멘토링
7. 정규 기여: 인정(CONTRIBUTORS.md), 역할 부여
```

## 첫 기여자 온보딩

```markdown
## 기여하기

### 개발 환경 설정
# 1단계: 포크 & 클론
git clone https://github.com/YOUR_ID/project.git

# 2단계: 의존성 설치
npm install

# 3단계: 테스트 실행
npm test

### 좋은 첫 이슈 찾기
"good first issue" 라벨이 붙은 이슈를 확인하세요.

### PR 제출 절차
1. 브랜치 생성: git checkout -b fix/issue-123
2. 변경 후 테스트 통과 확인
3. 커밋 메시지 컨벤션 준수 (Conventional Commits)
4. PR 제출 후 CI 통과 확인
```
