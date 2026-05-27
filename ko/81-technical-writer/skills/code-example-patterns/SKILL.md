---
name: code-example-patterns
description: "기술 문서용 코드 예제 패턴 라이브러리. doc-writer 에이전트가 코드 예제, 튜토리얼을 작성할 때 참조. '코드 예제 패턴', '튜토리얼 코드 작성' 요청 시 사용. 단, 실제 코드 컴파일이나 테스트 실행은 범위 밖."
---

# Code Example Patterns — 코드 예제 패턴 라이브러리

doc-writer 에이전트가 기술 문서에 포함할 코드 예제의 품질을 높이는 패턴.

## 5단계 예제 구조

```
1. 목표 선언 — "이 코드는 X를 수행합니다"
2. 사전 조건 — 라이브러리, 환경 변수, 설정
3. 핵심 코드 — 최소 작동 예제
4. 실행 결과 — 예상 출력
5. 확장 포인트 — "다음 단계로 Y를 할 수 있습니다"
```

## 좋은 예제 vs 나쁜 예제

**나쁜 예제** (컨텍스트 없음):
```python
result = client.process(data)
```

**좋은 예제** (자기완결적):
```python
# pip install example-sdk
from example_sdk import Client

client = Client(api_key="your-api-key")
data = {"name": "테스트", "value": 42}
result = client.process(data)
print(result.status)  # "success"
```

## 언어별 스타일 가이드

### Python
- 임포트 순서: 표준 → 서드파티 → 로컬
- 타입 힌트 포함 (3.10+)
- docstring: Google 스타일 (Args, Returns, Raises)
- f-string 사용, format() 지양

### TypeScript
- ESM import 사용 (require 지양)
- async/await 사용 (Promise 체이닝 지양)
- 인터페이스/타입 명시
- try/catch로 에러 처리

### cURL
- 줄바꿈(\)으로 가독성 확보
- 환경변수로 민감 정보 분리
- 예상 응답을 주석으로 포함

## 튜토리얼 코드 구성 패턴

### 패턴 1: 점진적 구축 (Progressive Build)
```
Step 1: 최소 동작 코드
Step 2: 입력 처리 추가
Step 3: 에러 처리 추가
Step 4: 설정 외부화
Step 5: 프로덕션 코드
```
각 단계에서 **변경 부분만 강조**, 기존 코드는 `...`으로 축약.

### 패턴 2: 문제-해결 쌍
```markdown
#### 문제: [구체적 문제 설명]
#### 해결: [코드와 함께 해결 방법]
```

### 패턴 3: 비교 테이블
| 방식 | 장점 | 단점 | 코드 |
|------|------|------|------|
| 동기 | 단순 | 블로킹 | `result = fetch()` |
| 비동기 | 성능 | 복잡 | `result = await fetch()` |

## 코드 주석 규칙

| 규칙 | 설명 |
|------|------|
| WHY 주석 | "왜" 이렇게 작성했는지 |
| WHAT 금지 | "무엇"은 코드 자체로 |
| 한글 주석 | 한국어 문서에서 한글 |
| TODO 금지 | 예제에 미완성 금지 |
| 하드코딩 설명 | "실제 환경에서는..." 주석 |

## 민감 정보 처리

```python
# 올바름: 환경변수
api_key = os.environ["API_KEY"]

# 문서용 플레이스홀더
api_key = "your-api-key-here"  # 실제 키로 교체
```

## 품질 체크리스트

| 항목 | 기준 |
|------|------|
| 자기완결성 | import~실행까지 복사-붙여넣기 동작 |
| 에러 처리 | try/catch 포함 |
| 타입 정보 | 변수/파라미터/반환값 타입 명시 |
| 실행 결과 | 예상 출력 포함 |
| 민감 정보 | 하드코딩 시크릿 없음 |
| 버전 명시 | 언어/라이브러리 버전 |
