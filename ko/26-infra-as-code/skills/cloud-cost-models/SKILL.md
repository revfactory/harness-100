---
name: cloud-cost-models
description: "AWS/GCP/Azure 비용 모델, 사이징 가이드, 예약 인스턴스/Savings Plan 전략, FinOps 프레임워크 가이드. '클라우드 비용', '비용 최적화', 'FinOps', '인스턴스 사이징', 'Savings Plan', '예약 인스턴스', 'Spot 인스턴스', '비용 추정' 등 인프라 비용 관련 판단 시 이 스킬을 사용한다. cost-optimizer의 비용 분석 역량을 강화한다. 단, 실제 리소스 프로비저닝이나 결제 설정은 이 스킬의 범위가 아니다."
---

# Cloud Cost Models — 클라우드 비용 모델 및 FinOps 가이드

클라우드 인프라 비용을 정확히 추정하고 최적화하는 실전 가이드.

## AWS 핵심 서비스 비용 모델

### EC2 구매 옵션 비교 (ap-northeast-2 기준)

| 옵션 | 할인율 | 약정 | 유연성 | 적합 워크로드 |
|------|-------|------|--------|-------------|
| On-Demand | 0% | 없음 | 최대 | 변동 워크로드, 테스트 |
| Savings Plan (Compute) | ~30% | 1년 | 인스턴스 변경 가능 | 안정적 기본 부하 |
| Savings Plan (EC2) | ~40% | 1년 | 패밀리 내 변경 | 예측 가능한 워크로드 |
| Reserved Instance | ~40% | 1년/3년 | 제한적 | 24/7 서버 |
| Spot Instance | ~70% | 없음 | 중단 가능 | 배치, CI/CD, ML |

### 사이징 의사결정 테이블

```
CPU 사용률 < 20% 지속 → 다운사이징 권장
CPU 사용률 > 80% 지속 → 업사이징 또는 스케일아웃
메모리 사용률 < 30%   → 메모리 최적화 인스턴스 불필요

워크로드 유형 → 인스턴스 패밀리:
├── 범용: t3, m6i (CPU/메모리 균형)
├── 컴퓨팅 집약: c6i (API 서버, 연산)
├── 메모리 집약: r6i (캐시, 인메모리 DB)
├── 스토리지 집약: i3, d3 (데이터베이스)
└── GPU: p4d, g5 (ML 학습/추론)
```

### RDS 비용 요소

```
월간 비용 = 인스턴스 비용 + 스토리지 + I/O + 백업 + 전송

예: db.r6g.xlarge, Multi-AZ, 500GB gp3
├── 인스턴스: $0.54/h × 730h × 2(Multi-AZ) = $788.40
├── 스토리지: 500GB × $0.138/GB = $69.00
├── 백업(초과분): 100GB × $0.095/GB = $9.50
└── 월 합계: ~$866.90
```

## 환경별 비용 최적화 전략

| 환경 | 전략 | 예상 절감 |
|------|------|----------|
| **dev** | 업무 시간만 운영 (12h/day, 주5일) = 36% 가동 | ~60% 절감 |
| **staging** | dev와 동일 + 더 작은 인스턴스 | ~70% 절감 |
| **prod** | Savings Plan + Right-sizing + 오토스케일링 | ~40% 절감 |

### 개발 환경 스케줄링

```hcl
# Lambda로 dev 환경 자동 시작/중지
resource "aws_cloudwatch_event_rule" "start_dev" {
  schedule_expression = "cron(0 0 ? * MON-FRI *)"  # 평일 09:00 KST
}
resource "aws_cloudwatch_event_rule" "stop_dev" {
  schedule_expression = "cron(0 12 ? * MON-FRI *)"  # 평일 21:00 KST
}
```

## 비용 추정 템플릿

```markdown
# 월간 비용 추정서

## 아키텍처 요약
| 구성요소 | 사양 | 수량 |

## 환경별 비용
| 서비스 | Dev | Staging | Prod | 합계 |
|--------|-----|---------|------|------|
| EC2/ECS | | | | |
| RDS | | | | |
| ElastiCache | | | | |
| ALB | | | | |
| S3 | | | | |
| CloudWatch | | | | |
| 데이터 전송 | | | | |
| **소계** | | | | |

## 최적화 적용
| 최적화 | 절감액 |
|--------|--------|
| Savings Plan (1년) | |
| 개발환경 스케줄링 | |
| Right-sizing | |
| **총 절감** | |

## 최종 비용
- 최적화 전: ₩N/월
- 최적화 후: ₩N/월
- 절감률: N%
```

## FinOps 성숙도 모델

| 단계 | 활동 | 도구 |
|------|------|------|
| **Inform** | 비용 가시화, 태깅, 할당 | AWS Cost Explorer, 태그 정책 |
| **Optimize** | Right-sizing, 예약, 스팟 | Compute Optimizer, Trusted Advisor |
| **Operate** | 예산 알림, 자동 조치, 거버넌스 | AWS Budgets, Lambda 자동 정리 |
