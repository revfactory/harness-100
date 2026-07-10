---
name: visualization-chooser
description: "데이터 유형과 분석 목적에 따른 시각화 유형 선택 매트릭스, matplotlib/seaborn/plotly 구현 패턴 가이드. '시각화 선택', '차트 유형', '그래프 종류', 'matplotlib', 'seaborn', 'plotly', '히트맵', '산점도', '박스플롯', '대시보드 레이아웃' 등 데이터 시각화 설계 시 이 스킬을 사용한다. visualizer의 시각화 설계 역량을 강화한다. 단, 통계 분석이나 데이터 정제는 이 스킬의 범위가 아니다."
---

# Visualization Chooser — 시각화 유형 선택 매트릭스 가이드

데이터 유형과 커뮤니케이션 목적에 맞는 최적의 시각화를 선택하는 프레임워크.

## 시각화 선택 매트릭스

### 비교

| 목적 | 차트 | 적합 | 예시 |
|------|------|------|------|
| 항목 비교 | 막대 차트 | 5~15개 카테고리 | 제품별 매출 |
| 시간 추이 비교 | 라인 차트 | 연속 시간, 2~5 시리즈 | 월별 매출 추이 |
| 부분-전체 | 스택 막대 | 비율 비교 | 채널별 매출 비중 |
| 소수 비율 | 파이 차트 | 2~5개 항목만 | 시장 점유율 |
| 다수 비율 | 트리맵 | 계층적 데이터 | 카테고리별 매출 |

### 분포

| 목적 | 차트 | 적합 | 예시 |
|------|------|------|------|
| 단일 분포 | 히스토그램 | 연속 변수 | 나이 분포 |
| 분포 비교 | 박스플롯 | 그룹별 비교 | 부서별 급여 |
| 밀도 비교 | 바이올린 플롯 | 분포 형태 중요 | 점수 분포 |
| 이상치 강조 | 스트립 플롯 | 소규모 데이터 | 개별 데이터 포인트 |

### 관계

| 목적 | 차트 | 적합 | 예시 |
|------|------|------|------|
| 두 변수 관계 | 산점도 | 연속×연속 | 광고비 vs 매출 |
| 다변수 상관 | 히트맵 | 상관 매트릭스 | 변수 간 상관 |
| 추세선 | 회귀 플롯 | 선형 관계 | 경험 vs 급여 |
| 밀도 산점도 | 2D 밀도 | 데이터 과다 | 위치 데이터 |
| 버블 차트 | 산점도 + 크기 | 3변수 | 국가별 GDP/인구/기대수명 |

### 시간

| 목적 | 차트 | 적합 | 예시 |
|------|------|------|------|
| 추세 | 라인 차트 | 연속 시계열 | 일별 주가 |
| 계절성 | 분해 그래프 | 주기 패턴 | 월별 전력 사용 |
| 이벤트 강조 | 어노테이션 라인 | 특정 시점 | 마케팅 캠페인 효과 |
| 범위 | 영역 차트 | 누적/비율 | 채널별 트래픽 |

## 구현 코드 패턴

### 한글 설정 (필수)

```python
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Darwin':  # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:  # Linux
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
```

### 색상 팔레트

```python
# 순서형 (연속 값)
palette_sequential = 'YlOrRd'

# 범주형 (구분)
palette_categorical = ['#4C72B0', '#55A868', '#C44E52', '#8172B3', '#CCB974']

# 발산형 (양극)
palette_diverging = 'RdBu_r'

# 접근성 고려
palette_colorblind = sns.color_palette('colorblind')
```

### 대시보드 레이아웃

```python
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('매출 분석 대시보드', fontsize=16, fontweight='bold')

# KPI 카드 (텍스트 기반)
axes[0,0].text(0.5, 0.5, f'총 매출\n₩{total:,.0f}', ha='center', va='center', fontsize=20)

# 추이 차트
axes[0,1].plot(dates, sales, '-o')

# 분포
axes[0,2].boxplot([q1, q2, q3, q4])

# 비교
axes[1,0].barh(categories, values)

# 상관
sns.heatmap(corr_matrix, ax=axes[1,1], annot=True, cmap='RdBu_r')

# 파이
axes[1,2].pie(shares, labels=channels, autopct='%1.1f%%')

plt.tight_layout()
```

## 시각화 안티패턴

| 안티패턴 | 문제 | 해결 |
|---------|------|------|
| 3D 차트 | 왜곡, 읽기 어려움 | 2D 사용 |
| 이중 Y축 | 비교 오해 유발 | 별도 차트 또는 정규화 |
| 파이 5개 초과 | 비교 불가 | 막대 차트 전환 |
| 레인보우 색상 | 패턴 구분 어려움 | 순서/범주 팔레트 |
| 0이 아닌 Y축 시작 | 차이 과장 | Y축 0부터 시작 |
| 정보 과부하 | 핵심 놓침 | 강조점 하나에 집중 |
| 범례 없음 | 해석 불가 | 명확한 범례/라벨 |

## 인터랙티브 시각화 (Plotly)

```python
import plotly.express as px

# 산점도 + 색상 + 크기 + 호버
fig = px.scatter(
    df, x='광고비', y='매출',
    color='카테고리', size='고객수',
    hover_data=['제품명'],
    title='광고비 대비 매출 분석'
)
fig.show()

# Plotly → HTML 내보내기
fig.write_html('interactive_chart.html')
```

## 경영진 보고서용 시각화 원칙

```
1. 핵심 메시지 하나: 차트당 하나의 인사이트
2. 제목 = 결론: "매출이 15% 하락했다" (O) vs "월별 매출" (X)
3. 색상 = 의미: 빨강=나쁨, 초록=좋음, 회색=기준
4. 어노테이션: 핵심 수치 직접 표시
5. 비교 기준: 전월, 전년, 목표, 업계 평균
```
