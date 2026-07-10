---
name: techstack-decision-matrix
description: "사이드프로젝트 기술스택을 체계적으로 비교·선정하는 의사결정 매트릭스. 'techstack-analyst' 에이전트가 기술스택을 비교하고 추천할 때 이 스킬의 평가 기준, 비용 계산법, 스택 조합 패턴을 반드시 활용해야 한다. '기술스택 비교', '인프라 비용 계산', '스택 선정' 등에 사용한다. 단, 시장 분석이나 MVP 설계는 이 스킬의 범위가 아니다."
---

# TechStack Decision Matrix — 기술스택 의사결정 매트릭스

사이드프로젝트에 최적화된 기술스택 비교, 비용 산출, 추천 조합.

## 평가 기준 프레임워크 (5축)

```
1. 학습 곡선 (Learning Curve): 새로 배우는 데 걸리는 시간
2. 개발 속도 (Development Speed): MVP까지의 소요 시간
3. 운영 비용 (Operating Cost): 월 인프라 비용
4. 확장성 (Scalability): 사용자 증가 시 대응 용이성
5. 생태계 (Ecosystem): 라이브러리, 커뮤니티, 채용 시장
```

## 프론트엔드 비교

| 프레임워크 | 학습 | 속도 | 생태계 | 적합 | 비고 |
|-----------|------|------|--------|------|------|
| Next.js | 3/5 | 5/5 | 5/5 | 웹앱, SaaS | SSR+API 통합 |
| React (Vite) | 3/5 | 4/5 | 5/5 | SPA, 대시보드 | 유연성 최고 |
| Vue.js | 4/5 | 4/5 | 4/5 | 중소 프로젝트 | 쉬운 학습 |
| Svelte | 4/5 | 4/5 | 3/5 | 성능 중시 | 번들 크기 최소 |
| Astro | 4/5 | 5/5 | 3/5 | 콘텐츠/블로그 | 정적 사이트 |
| Flutter Web | 3/5 | 3/5 | 3/5 | 크로스 플랫폼 | 모바일 겸용 |

## 백엔드 비교

| 프레임워크 | 학습 | 속도 | 성능 | 적합 | 비고 |
|-----------|------|------|------|------|------|
| Next.js API | 4/5 | 5/5 | 3/5 | 풀스택, BFF | 프론트 통합 |
| FastAPI (Python) | 4/5 | 4/5 | 4/5 | API, AI/ML | 타입 힌트 |
| Express (Node) | 4/5 | 4/5 | 3/5 | 범용 API | 유연성 |
| Django | 3/5 | 4/5 | 4/5 | 관리자 필요 시 | 배터리 포함 |
| Spring Boot | 2/5 | 3/5 | 5/5 | 대규모 시스템 | 과투자 주의 |
| Go (Fiber) | 3/5 | 3/5 | 5/5 | 고성능 API | 동시성 강점 |

## 데이터베이스 비교

| DB | 유형 | 무료 티어 | 적합 | 비고 |
|----|------|----------|------|------|
| Supabase (PostgreSQL) | SQL | 500MB, 50K MAU | CRUD 앱, 인증 포함 | Firebase 대안 |
| PlanetScale (MySQL) | SQL | 1GB, 1B reads | 확장성 필요 시 | 브랜칭 기능 |
| Firebase Firestore | NoSQL | 1GB, 50K reads/일 | 실시간, 모바일 | 구글 생태계 |
| MongoDB Atlas | NoSQL | 512MB | 유연한 스키마 | JSON 네이티브 |
| Turso (SQLite) | SQL | 9GB, 500 DB | 엣지, 빠른 시작 | 서버리스 |
| Neon (PostgreSQL) | SQL | 3GB | Next.js 궁합 | 서버리스 PG |

## 인프라·배포 비용 비교

### 무료 티어 활용 스택

```
$0/월 스택:
  호스팅: Vercel Free (100GB 대역폭)
  DB: Supabase Free (500MB)
  인증: Supabase Auth (50K MAU)
  스토리지: Supabase Storage (1GB)
  도메인: 서브도메인 (*.vercel.app)
  이메일: Resend Free (100/일)

적합: MVP 검증, 초기 사용자 100명 이하
```

### 저비용 스택 ($10-30/월)

```
호스팅: Vercel Pro ($20/월) 또는 Railway ($5~)
DB: Supabase Pro ($25/월) 또는 PlanetScale Scaler ($29/월)
도메인: 연 $12-15
이메일: Resend ($20/월)
모니터링: Sentry Free

총: $25-50/월 (약 3-7만원)
적합: 유료 사용자 100-1,000명
```

### 스택 ROI 계산

```
손익분기점 = 월 운영비 / (ARPU × 유료전환율 × MAU)

예시:
  월 운영비: 5만원
  구독료: 9,900원/월
  유료 전환: 3%
  필요 MAU: 5만 / (9,900 × 0.03) = 168명

168명의 활성 사용자가 필요
```

## 추천 스택 조합

### 웹 SaaS (1인 개발자)

```
✅ 추천: Next.js + Supabase + Vercel + Tailwind CSS
  - 풀스택 통합
  - 무료 시작 → 유료 스케일
  - 인증·DB·스토리지 올인원
  - 학습 곡선 보통, 생산성 최고
```

### 모바일 앱

```
✅ 추천: Flutter + Firebase + Google Play/App Store
  - iOS + Android 동시
  - 실시간 DB, 푸시 알림 내장
  - 무료 시작 → 유료 스케일

대안: React Native + Expo + Supabase
```

### AI/ML 제품

```
✅ 추천: Next.js + FastAPI + OpenAI API + Vercel + Railway
  - 프론트: Next.js (Vercel)
  - AI 백엔드: FastAPI (Railway)
  - LLM: OpenAI/Anthropic API
  - DB: Supabase (벡터 검색 pgvector)
```

### 콘텐츠/블로그

```
✅ 추천: Astro + Markdown + Vercel + 무료 CMS
  - 빌드 시 정적 생성 (빠름, 저비용)
  - SEO 최적화 내장
  - $0/월 운영 가능
```

## 의사결정 매트릭스 출력 형식

```markdown
## 기술스택 비교 매트릭스

| 기준 (가중치) | 옵션 A | 옵션 B | 옵션 C |
|-------------|--------|--------|--------|
| 학습곡선 (20%) | 4/5 | 3/5 | 5/5 |
| 개발속도 (30%) | 5/5 | 4/5 | 3/5 |
| 운영비용 (20%) | 5/5 | 3/5 | 4/5 |
| 확장성 (15%) | 4/5 | 5/5 | 3/5 |
| 생태계 (15%) | 5/5 | 5/5 | 3/5 |
| **가중 합계** | **4.6** | **3.9** | **3.7** |
| **추천** | ✅ 1순위 | 2순위 | 3순위 |
```

## 참고

- 2024-2025 시장 기준, 가격·무료 티어는 변동 가능
- 상세 스택 가이드: `references/techstack-details.md` 참조
