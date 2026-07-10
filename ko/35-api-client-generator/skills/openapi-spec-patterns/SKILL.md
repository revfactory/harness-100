---
name: openapi-spec-patterns
description: "OpenAPI 3.x 스펙 분석 패턴, 스키마 정규화, 인증 방식 매핑, 페이지네이션/에러 패턴 추출, GraphQL/gRPC 스펙 해석 가이드. 'OpenAPI', 'Swagger', '스펙 분석', '스키마 정규화', 'API 인증', '페이지네이션 패턴', 'GraphQL 스키마', 'gRPC proto' 등 API 스펙 분석 시 이 스킬을 사용한다. spec-parser의 스펙 분석 역량을 강화한다. 단, SDK 코드 생성이나 테스트 작성은 이 스킬의 범위가 아니다."
---

# OpenAPI Spec Patterns — API 스펙 분석 패턴 가이드

OpenAPI/GraphQL/gRPC 스펙을 효과적으로 분석하고 SDK 생성에 필요한 메타데이터를 추출하는 방법론.

## OpenAPI 3.x 분석 절차

### 1. 엔드포인트 그룹핑

```yaml
# Tag 기반 그룹핑 → SDK 클래스 매핑
paths:
  /users:
    get:
      tags: [Users]         # → UsersClient.list()
    post:
      tags: [Users]         # → UsersClient.create()
  /users/{id}:
    get:
      tags: [Users]         # → UsersClient.get(id)
    put:
      tags: [Users]         # → UsersClient.update(id, data)
    delete:
      tags: [Users]         # → UsersClient.delete(id)
  /users/{id}/orders:
    get:
      tags: [Users, Orders] # → UsersClient.listOrders(id)
```

### 매핑 규칙

| HTTP Method | 패턴 | SDK 메서드명 |
|------------|------|------------|
| GET /resources | 목록 | `list()` |
| GET /resources/{id} | 상세 | `get(id)` |
| POST /resources | 생성 | `create(data)` |
| PUT /resources/{id} | 전체 수정 | `update(id, data)` |
| PATCH /resources/{id} | 부분 수정 | `patch(id, data)` |
| DELETE /resources/{id} | 삭제 | `delete(id)` |
| POST /resources/{id}/action | 액션 | `actionName(id, data)` |

### 2. 인증 방식 매핑

```yaml
securitySchemes:
  BearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
  ApiKeyAuth:
    type: apiKey
    in: header
    name: X-API-Key
  OAuth2:
    type: oauth2
    flows:
      authorizationCode:
        authorizationUrl: https://auth.example.com/authorize
        tokenUrl: https://auth.example.com/token
        scopes:
          read: Read access
          write: Write access
```

| 인증 유형 | SDK 구현 | 코드 패턴 |
|----------|---------|----------|
| Bearer | 헤더 인터셉터 | `Authorization: Bearer {token}` |
| API Key | 헤더/쿼리 인터셉터 | `X-API-Key: {key}` |
| OAuth2 | 토큰 관리 + 갱신 | 자동 refresh_token 처리 |
| Basic | 헤더 | `Authorization: Basic {base64}` |

### 3. 페이지네이션 패턴 탐지

```yaml
# 패턴 1: Offset-based
parameters:
  - name: offset
    in: query
    schema: { type: integer }
  - name: limit
    in: query
    schema: { type: integer, default: 20 }

# 패턴 2: Cursor-based
parameters:
  - name: cursor
    in: query
    schema: { type: string }
  - name: limit
    in: query
    schema: { type: integer }

# 패턴 3: Page-based
parameters:
  - name: page
    in: query
    schema: { type: integer }
  - name: per_page
    in: query
    schema: { type: integer }
```

| 탐지 패턴 | SDK 구현 |
|----------|---------|
| offset/limit | `listAll()` 자동 페이지 순회 |
| cursor/after | `iterate()` 이터레이터 |
| page/per_page | `listPage(page)` |
| Link 헤더 | HTTP Link 헤더 파싱 |

### 4. 에러 응답 패턴

```yaml
# 표준 에러 구조 추출
responses:
  '400':
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Error'

components:
  schemas:
    Error:
      type: object
      properties:
        code: { type: string }
        message: { type: string }
        details: { type: array, items: { $ref: '#/components/schemas/ErrorDetail' } }
```

### SDK 에러 클래스 매핑

| HTTP Status | SDK 예외 | 재시도 |
|------------|---------|--------|
| 400 | BadRequestError | No |
| 401 | AuthenticationError | No (토큰 갱신 후 1회) |
| 403 | PermissionError | No |
| 404 | NotFoundError | No |
| 409 | ConflictError | No |
| 422 | ValidationError | No |
| 429 | RateLimitError | Yes (Retry-After) |
| 500 | InternalError | Yes (지수 백오프) |
| 502/503/504 | ServiceUnavailableError | Yes |

## 스키마 정규화

### 순환 참조 처리

```yaml
# 순환: User → Order → User
User:
  properties:
    orders:
      type: array
      items: { $ref: '#/components/schemas/Order' }
Order:
  properties:
    user: { $ref: '#/components/schemas/User' }  # 순환!

# 해결: Lazy Reference
# TypeScript: type User = { orders: () => Order[] }
# Python: User = ForwardRef('User')
```

### allOf/oneOf/anyOf 해석

```yaml
# allOf → 인터섹션 (상속/확장)
UpdateUser:
  allOf:
    - $ref: '#/components/schemas/BaseUser'
    - type: object
      properties:
        password: { type: string }
# → class UpdateUser extends BaseUser { password?: string }

# oneOf → 유니온 (택일)
Pet:
  oneOf:
    - $ref: '#/components/schemas/Cat'
    - $ref: '#/components/schemas/Dog'
  discriminator:
    propertyName: petType
# → type Pet = Cat | Dog (discriminated union)

# anyOf → 유연한 유니온
Filter:
  anyOf:
    - type: string
    - type: integer
    - type: array
      items: { type: string }
# → type Filter = string | number | string[]
```

## GraphQL 스키마 분석

```graphql
# Query → SDK read 메서드
type Query {
    user(id: ID!): User        # → client.users.get(id)
    users(first: Int, after: String): UserConnection  # → client.users.list()
}

# Mutation → SDK write 메서드
type Mutation {
    createUser(input: CreateUserInput!): User  # → client.users.create(input)
    updateUser(id: ID!, input: UpdateUserInput!): User
}

# Connection 패턴 → 자동 페이지네이션
type UserConnection {
    edges: [UserEdge!]!
    pageInfo: PageInfo!
}
```

## gRPC Proto 분석

```protobuf
service UserService {
    rpc GetUser (GetUserRequest) returns (User);           // → client.getUser(id)
    rpc ListUsers (ListUsersRequest) returns (ListUsersResponse);
    rpc CreateUser (CreateUserRequest) returns (User);
    rpc StreamUsers (StreamRequest) returns (stream User); // → 스트리밍 API
}
```

| gRPC 패턴 | SDK 구현 |
|----------|---------|
| Unary | 일반 비동기 메서드 |
| Server Stream | AsyncIterator |
| Client Stream | 스트림 전송 메서드 |
| Bidirectional | 양방향 스트림 |
