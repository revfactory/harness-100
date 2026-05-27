---
name: sdk-design-patterns
description: "SDK/API 클라이언트 설계 패턴: 빌더 패턴, 인터셉터 체인, 재시도 전략, 타입 안전 설계, 에러 핸들링, 페이지네이션 래퍼 가이드. 'SDK 설계', '클라이언트 패턴', '재시도 전략', '인터셉터', '빌더 패턴', 'SDK 에러 처리', '타입 안전', 'SDK 아키텍처' 등 SDK 구조 설계 시 이 스킬을 사용한다. sdk-developer의 SDK 설계 역량을 강화한다. 단, API 스펙 파싱이나 테스트/문서 작성은 이 스킬의 범위가 아니다."
---

# SDK Design Patterns — SDK 설계 패턴 가이드

타입 안전하고 사용하기 쉬운 API 클라이언트 SDK를 설계하는 패턴 카탈로그.

## SDK 아키텍처

```
┌─────────────────────────────────────────┐
│              SDK Public API              │
│  client.users.list()                     │
│  client.orders.create({...})             │
├─────────────────────────────────────────┤
│           Resource Clients               │
│  UsersClient, OrdersClient, ...          │
├─────────────────────────────────────────┤
│           Middleware Chain                │
│  Auth → Retry → RateLimit → Logger       │
├─────────────────────────────────────────┤
│           HTTP Transport                 │
│  fetch / axios / httpx                   │
└─────────────────────────────────────────┘
```

## 빌더 패턴 (Client 초기화)

### TypeScript

```typescript
const client = new ApiClient({
  baseUrl: 'https://api.example.com',
  apiKey: process.env.API_KEY,
  timeout: 30000,
  retries: 3,
  // 선택적 커스텀
  fetch: customFetch,
  headers: { 'X-Custom': 'value' },
});

// 리소스 접근
const users = await client.users.list({ page: 1, perPage: 20 });
const user = await client.users.get('user_123');
const newUser = await client.users.create({ name: '홍길동', email: 'hong@test.com' });
```

### Python

```python
client = ApiClient(
    base_url="https://api.example.com",
    api_key=os.environ["API_KEY"],
    timeout=30.0,
    max_retries=3,
)

# Context Manager 지원
async with ApiClient(api_key="...") as client:
    users = await client.users.list(page=1, per_page=20)
```

## 인터셉터/미들웨어 체인

```typescript
// 인터셉터 인터페이스
interface Interceptor {
  beforeRequest(config: RequestConfig): Promise<RequestConfig>;
  afterResponse(response: Response): Promise<Response>;
  onError(error: Error): Promise<never>;
}

// 인증 인터셉터
class AuthInterceptor implements Interceptor {
  async beforeRequest(config) {
    config.headers['Authorization'] = `Bearer ${this.token}`;
    return config;
  }
  async onError(error) {
    if (error.status === 401 && this.refreshToken) {
      await this.refresh();
      return this.retry(error.config);
    }
    throw error;
  }
}

// 재시도 인터셉터
class RetryInterceptor implements Interceptor {
  async onError(error) {
    if (this.shouldRetry(error) && this.attempt < this.maxRetries) {
      await this.backoff(this.attempt);
      return this.retry(error.config);
    }
    throw error;
  }
}
```

## 재시도 전략

```typescript
class RetryStrategy {
  private maxRetries = 3;
  private baseDelay = 1000; // ms

  shouldRetry(error: ApiError): boolean {
    // 재시도 가능한 에러만
    return [408, 429, 500, 502, 503, 504].includes(error.status);
  }

  getDelay(attempt: number, error: ApiError): number {
    // 429: Retry-After 헤더 우선
    if (error.status === 429 && error.headers['retry-after']) {
      return parseInt(error.headers['retry-after']) * 1000;
    }
    // 지수 백오프 + 지터
    const exponential = this.baseDelay * Math.pow(2, attempt);
    const jitter = Math.random() * this.baseDelay;
    return Math.min(exponential + jitter, 60000); // 최대 60초
  }
}
```

## 타입 안전 설계

### TypeScript 제네릭 활용

```typescript
// 리소스 타입 정의
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

interface CreateUserRequest {
  name: string;
  email: string;
}

interface ListUsersParams {
  page?: number;
  perPage?: number;
  sort?: 'name' | 'createdAt';
  order?: 'asc' | 'desc';
}

// 제네릭 리소스 클라이언트
class ResourceClient<T, CreateT, UpdateT, ListParams> {
  async list(params?: ListParams): Promise<PaginatedResponse<T>> { ... }
  async get(id: string): Promise<T> { ... }
  async create(data: CreateT): Promise<T> { ... }
  async update(id: string, data: UpdateT): Promise<T> { ... }
  async delete(id: string): Promise<void> { ... }
}

// 구체적 클라이언트
class UsersClient extends ResourceClient<User, CreateUserRequest, UpdateUserRequest, ListUsersParams> {
  // 추가 메서드
  async listOrders(userId: string): Promise<Order[]> { ... }
}
```

### Python Pydantic 모델

```python
from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime = Field(alias="createdAt")

    class Config:
        populate_by_name = True

class CreateUserRequest(BaseModel):
    name: str
    email: str
```

## 페이지네이션 래퍼

```typescript
// 자동 페이지 순회
class PaginatedResponse<T> {
  data: T[];
  hasMore: boolean;
  nextCursor?: string;

  // 이터레이터 지원
  async *[Symbol.asyncIterator](): AsyncIterator<T> {
    let response: PaginatedResponse<T> = this;
    while (true) {
      for (const item of response.data) {
        yield item;
      }
      if (!response.hasMore) break;
      response = await this.fetchNext(response.nextCursor);
    }
  }
}

// 사용법
for await (const user of client.users.list()) {
  console.log(user.name);  // 모든 페이지를 자동 순회
}

// 특정 페이지만
const page1 = await client.users.list({ perPage: 20 });
```

## 에러 핸들링

```typescript
// 에러 계층 구조
class ApiError extends Error {
  status: number;
  code: string;
  details?: any;
}

class BadRequestError extends ApiError { status = 400; }
class AuthenticationError extends ApiError { status = 401; }
class NotFoundError extends ApiError { status = 404; }
class RateLimitError extends ApiError {
  status = 429;
  retryAfter: number;
}
class InternalError extends ApiError { status = 500; }

// 사용
try {
  const user = await client.users.get('invalid_id');
} catch (e) {
  if (e instanceof NotFoundError) {
    console.log('사용자를 찾을 수 없습니다');
  } else if (e instanceof RateLimitError) {
    console.log(`${e.retryAfter}초 후 재시도하세요`);
  }
}
```

## SDK 품질 체크리스트

```markdown
### 사용성
- [ ] 3줄 이내로 시작 가능 (Quick Start)
- [ ] IDE 자동완성 100% 지원 (타입 완전)
- [ ] 에러 메시지가 해결 방법을 안내
- [ ] 동기/비동기 모두 지원

### 견고성
- [ ] 재시도 + 지수 백오프
- [ ] 토큰 자동 갱신
- [ ] Rate Limit 자동 대기
- [ ] 타임아웃 설정 가능
- [ ] 커스텀 HTTP 클라이언트 주입 가능

### 테스트
- [ ] 모든 공개 API 단위 테스트
- [ ] Mock 서버 통합 테스트
- [ ] 에러 시나리오 테스트
- [ ] 페이지네이션 테스트
```
