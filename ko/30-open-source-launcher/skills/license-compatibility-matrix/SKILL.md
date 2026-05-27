---
name: license-compatibility-matrix
description: "오픈소스 라이선스 호환성 매트릭스, 라이선스별 의무사항, 듀얼 라이선스 전략, SPDX 식별자 가이드. '라이선스 호환성', '라이선스 선택', 'MIT', 'Apache', 'GPL', 'LGPL', 'BSD', '듀얼 라이선스', 'SPDX', '라이선스 충돌' 등 오픈소스 라이선스 관련 판단 시 이 스킬을 사용한다. license-specialist의 라이선스 분석 역량을 강화한다. 단, 법적 자문이나 실제 라이선스 파일 생성은 이 스킬의 범위가 아니다."
---

# License Compatibility Matrix — 오픈소스 라이선스 호환성 가이드

오픈소스 라이선스 선택, 호환성 분석, 의존성 라이선스 충돌 해결을 위한 실전 가이드.

## 주요 라이선스 비교

| 라이선스 | 유형 | 상용 사용 | 수정 공개 | 특허 보호 | 네트워크 조항 |
|---------|------|----------|----------|----------|-------------|
| MIT | 관대 | O | X | X | X |
| Apache 2.0 | 관대 | O | X | O | X |
| BSD 2-Clause | 관대 | O | X | X | X |
| BSD 3-Clause | 관대 | O | X | X | X |
| MPL 2.0 | 약한 카피레프트 | O | 파일 단위 | O | X |
| LGPL 2.1/3.0 | 약한 카피레프트 | O | 라이브러리만 | X | X |
| GPL 2.0/3.0 | 강한 카피레프트 | 조건부 | O (전체) | O(v3) | X |
| AGPL 3.0 | 강한 카피레프트 | 조건부 | O (전체) | O | O |

## 호환성 매트릭스

```
프로젝트 라이선스 ↓  |  의존성 라이선스 →
                    | MIT | Apache | BSD | MPL | LGPL | GPL | AGPL
────────────────────┼─────┼────────┼─────┼─────┼──────┼─────┼──────
MIT                 | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
Apache 2.0          | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
BSD                 | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
MPL 2.0             | ✅  | ✅     | ✅  | ✅  | ✅   | ✅* | ❌
LGPL 3.0            | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ❌
GPL 3.0             | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ❌
AGPL 3.0            | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ✅

✅ 호환 | ❌ 비호환 | ✅* 조건부 호환
```

**핵심 규칙:**
- GPL 의존성 사용 → 프로젝트 전체가 GPL 적용 (바이럴 효과)
- AGPL 의존성 사용 → 네트워크 서비스도 소스 공개 의무
- Apache 2.0 ↔ GPL 2.0 비호환 (특허 조항 충돌)

## 라이선스 선택 의사결정 트리

```
프로젝트 목표
├── 최대 채택 원함 → MIT 또는 Apache 2.0
│   ├── 특허 보호 필요 → Apache 2.0
│   └── 최대 단순함 → MIT
├── 수정본 공개 원함 (파일 단위) → MPL 2.0
├── 라이브러리, 링킹은 허용 → LGPL 3.0
├── 파생물 전부 공개 원함 → GPL 3.0
├── SaaS 포함 공개 원함 → AGPL 3.0
└── 듀얼 라이선스 (OSS + 상용) → GPL + Commercial
```

## 의존성 라이선스 충돌 해결

### 충돌 패턴과 해결

| 충돌 | 문제 | 해결 |
|------|------|------|
| MIT 프로젝트 + GPL 의존성 | GPL 전파 | 대체 패키지 탐색 또는 GPL 전환 |
| Apache + GPL 2.0 | 특허 조항 비호환 | GPL 3.0 버전 사용 |
| 상용 제품 + AGPL 의존성 | 소스 공개 의무 | 대체 패키지 또는 라이선스 구매 |
| 다중 GPL 버전 혼합 | 버전 호환성 | "GPL 2.0 or later" 활용 |

### 라이선스 감사 도구

```bash
# Node.js
npx license-checker --json --production

# Python
pip-licenses --format=json --with-urls

# Go
go-licenses check ./...

# 범용
scancode-toolkit --json-pp output.json src/
```

## SPDX 라이선스 표현식

```
# 단일 라이선스
SPDX-License-Identifier: MIT

# OR (선택 가능)
SPDX-License-Identifier: MIT OR Apache-2.0

# AND (두 라이선스 모두 준수)
SPDX-License-Identifier: MIT AND BSD-3-Clause

# WITH (예외 포함)
SPDX-License-Identifier: GPL-2.0-only WITH Classpath-exception-2.0
```

## 듀얼 라이선스 전략

```
Community Edition: AGPL 3.0
├── 무료 사용 가능
├── 수정본 + 서비스 제공 시 소스 공개 의무
└── 개인/소규모 오픈소스 프로젝트에 적합

Enterprise Edition: 상용 라이선스
├── AGPL 의무 면제
├── 추가 기능/지원 포함
└── 기업 고객 대상

성공 사례: MongoDB(SSPL), Redis(RSALv2), MySQL(GPL+Commercial)
```

## 라이선스 의무 체크리스트

```markdown
프로젝트 배포 전 확인:
- [ ] 모든 의존성의 라이선스 식별 완료
- [ ] 라이선스 호환성 매트릭스 검증 완료
- [ ] LICENSE 파일에 모든 제3자 라이선스 포함
- [ ] 저작권 고지(NOTICE) 파일 작성 (Apache 2.0 요구)
- [ ] GPL 의존성 사용 시 소스 공개 준비
- [ ] SPDX 식별자가 소스 파일에 포함
- [ ] package.json/pyproject.toml에 라이선스 필드 명시
```
