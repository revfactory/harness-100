---
name: techstack-decision-matrix
description: "A systematic comparison and decision-making matrix for selecting a side project tech stack. The 'techstack-analyst' agent must use this skill's evaluation criteria, cost calculations, and stack combination patterns when comparing and recommending tech stacks. Use for 'tech stack comparison', 'infrastructure cost calculation', 'stack selection', and similar requests. However, market analysis and MVP design are outside the scope of this skill."
---

# TechStack Decision Matrix — Tech Stack Decision-Making Matrix

Optimized tech stack comparison, cost calculation, and recommended combinations for side projects.

## Evaluation Criteria Framework (5 Axes)

```
1. Learning Curve: Time required to learn something new
2. Development Speed: Time to reach MVP
3. Operating Cost: Monthly infrastructure cost
4. Scalability: Ease of handling user growth
5. Ecosystem: Libraries, community, hiring market
```

## Frontend Comparison

| Framework | Learning | Speed | Ecosystem | Best For | Notes |
|-----------|----------|-------|-----------|----------|-------|
| Next.js | 3/5 | 5/5 | 5/5 | Web apps, SaaS | SSR + API integration |
| React (Vite) | 3/5 | 4/5 | 5/5 | SPA, dashboards | Maximum flexibility |
| Vue.js | 4/5 | 4/5 | 4/5 | Small-medium projects | Easy to learn |
| Svelte | 4/5 | 4/5 | 3/5 | Performance-focused | Minimal bundle size |
| Astro | 4/5 | 5/5 | 3/5 | Content / blogs | Static site |
| Flutter Web | 3/5 | 3/5 | 3/5 | Cross-platform | Mobile dual-use |

## Backend Comparison

| Framework | Learning | Speed | Performance | Best For | Notes |
|-----------|----------|-------|-------------|----------|-------|
| Next.js API | 4/5 | 5/5 | 3/5 | Full-stack, BFF | Frontend integration |
| FastAPI (Python) | 4/5 | 4/5 | 4/5 | API, AI/ML | Type hints |
| Express (Node) | 4/5 | 4/5 | 3/5 | General API | Flexible |
| Django | 3/5 | 4/5 | 4/5 | When admin needed | Batteries included |
| Spring Boot | 2/5 | 3/5 | 5/5 | Large-scale systems | Caution: over-engineering |
| Go (Fiber) | 3/5 | 3/5 | 5/5 | High-performance API | Concurrency strength |

## Database Comparison

| DB | Type | Free Tier | Best For | Notes |
|----|------|-----------|----------|-------|
| Supabase (PostgreSQL) | SQL | 500MB, 50K MAU | CRUD apps, auth included | Firebase alternative |
| PlanetScale (MySQL) | SQL | 1GB, 1B reads | When scalability needed | Branching feature |
| Firebase Firestore | NoSQL | 1GB, 50K reads/day | Real-time, mobile | Google ecosystem |
| MongoDB Atlas | NoSQL | 512MB | Flexible schema | JSON native |
| Turso (SQLite) | SQL | 9GB, 500 DB | Edge, quick start | Serverless |
| Neon (PostgreSQL) | SQL | 3GB | Next.js compatibility | Serverless PG |

## Infrastructure and Deployment Cost Comparison

### Free Tier Stack

```
$0/month stack:
  Hosting: Vercel Free (100GB bandwidth)
  DB: Supabase Free (500MB)
  Auth: Supabase Auth (50K MAU)
  Storage: Supabase Storage (1GB)
  Domain: Subdomain (*.vercel.app)
  Email: Resend Free (100/day)

Best for: MVP validation, initial users under 100
```

### Low-Cost Stack ($10–30/month)

```
Hosting: Vercel Pro ($20/month) or Railway ($5+)
DB: Supabase Pro ($25/month) or PlanetScale Scaler ($29/month)
Domain: $12–15/year
Email: Resend ($20/month)
Monitoring: Sentry Free

Total: $25–50/month (approx. 30,000–70,000 KRW)
Best for: 100–1,000 paid users
```

### Stack ROI Calculation

```
Break-even point = Monthly operating cost / (ARPU × Paid conversion rate × MAU)

Example:
  Monthly operating cost: 50,000 KRW
  Subscription price: 9,900 KRW/month
  Paid conversion: 3%
  Required MAU: 50,000 / (9,900 × 0.03) = 168 users

168 active users required
```

## Recommended Stack Combinations

### Web SaaS (Solo Developer)

```
✅ Recommended: Next.js + Supabase + Vercel + Tailwind CSS
  - Full-stack integration
  - Free start → paid scale
  - Auth + DB + storage all-in-one
  - Moderate learning curve, maximum productivity
```

### Mobile App

```
✅ Recommended: Flutter + Firebase + Google Play/App Store
  - iOS + Android simultaneously
  - Real-time DB, push notifications built-in
  - Free start → paid scale

Alternative: React Native + Expo + Supabase
```

### AI/ML Product

```
✅ Recommended: Next.js + FastAPI + OpenAI API + Vercel + Railway
  - Frontend: Next.js (Vercel)
  - AI backend: FastAPI (Railway)
  - LLM: OpenAI/Anthropic API
  - DB: Supabase (vector search with pgvector)
```

### Content / Blog

```
✅ Recommended: Astro + Markdown + Vercel + free CMS
  - Static generation at build time (fast, low cost)
  - SEO optimization built-in
  - $0/month operating cost possible
```

## Decision Matrix Output Format

```markdown
## Tech Stack Comparison Matrix

| Criterion (Weight) | Option A | Option B | Option C |
|-------------------|---------|---------|---------|
| Learning Curve (20%) | 4/5 | 3/5 | 5/5 |
| Development Speed (30%) | 5/5 | 4/5 | 3/5 |
| Operating Cost (20%) | 5/5 | 3/5 | 4/5 |
| Scalability (15%) | 4/5 | 5/5 | 3/5 |
| Ecosystem (15%) | 5/5 | 5/5 | 3/5 |
| **Weighted Total** | **4.6** | **3.9** | **3.7** |
| **Recommendation** | ✅ 1st | 2nd | 3rd |
```

## Reference

- 2024–2025 market standards; prices and free tiers are subject to change
- Detailed stack guide: see `references/techstack-details.md`
