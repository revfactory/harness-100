---
name: image-prompt-engineering
description: "AI 이미지 생성(Gemini/DALL-E/Midjourney) 프롬프트 작성 가이드. 구도별 프롬프트 템플릿, 스타일 키워드 사전, 일관성 유지 기법, 네거티브 프롬프트 패턴을 제공하는 image-prompter 확장 스킬. '이미지 프롬프트', 'AI 이미지 스타일', '프롬프트 작성법', '구도 키워드', '스타일 일관성', '네거티브 프롬프트' 등 AI 이미지 생성 프롬프트 최적화 시 사용한다. 단, 이미지 직접 생성이나 후보정은 이 스킬의 범위가 아니다."
---

# Image Prompt Engineering — AI 이미지 프롬프트 작성 가이드

image-prompter 에이전트가 AI 이미지 생성 시 활용하는 프롬프트 구조, 스타일 키워드, 일관성 기법 레퍼런스.

## 대상 에이전트

`image-prompter` — 이 스킬의 프롬프트 패턴과 키워드를 이미지 생성에 직접 적용한다.

## 프롬프트 구조 공식

### 5-Layer 프롬프트 구조
```
[1. 매체/스타일] + [2. 구도/카메라] + [3. 주체 묘사] + [4. 환경/배경] + [5. 조명/분위기]
```

#### Layer 1: 매체/스타일
| 카테고리 | 키워드 | 효과 |
|---------|--------|------|
| 사진 | "editorial photography", "professional photo" | 사실적 |
| 일러스트 | "digital illustration", "vector art" | 그래픽적 |
| 수채화 | "watercolor painting", "soft watercolor" | 서정적 |
| 유화 | "oil painting", "impressionist oil" | 클래식 |
| 미니멀 | "minimalist flat design", "simple clean" | 모던 |
| 시네마틱 | "cinematic still", "movie scene" | 드라마틱 |
| 애니메이션 | "anime style", "Studio Ghibli inspired" | 애니 |
| 3D 렌더 | "3D render", "isometric 3D" | 입체적 |

#### Layer 2: 구도/카메라
| 구도 | 키워드 | 용도 |
|------|--------|------|
| 와이드샷 | "wide shot", "establishing shot" | 장소 소개, 스케일 |
| 미디엄샷 | "medium shot", "waist-up" | 인물 소개, 대화 |
| 클로즈업 | "close-up", "macro detail" | 감정, 디테일 |
| 버드아이 | "bird's eye view", "top-down" | 전체 구조, 고립감 |
| 로우앵글 | "low angle shot", "worm's eye" | 위압감, 웅장함 |
| 오버더숄더 | "over-the-shoulder" | 대화 장면 |
| 대칭 | "symmetrical composition" | 안정감, 격식 |
| 황금비 | "golden ratio composition" | 자연스러운 시선 유도 |

#### Layer 3: 주체 묘사 원칙
- **구체적 > 추상적**: "woman" → "30-year-old Korean woman with short black hair"
- **행동 포함**: "standing" → "leaning against a wall, reading a book"
- **표정 명시**: "smiling softly with closed eyes"
- **의상 디테일**: "wearing a dark navy wool coat"

#### Layer 4: 환경/배경
| 키워드 | 효과 |
|--------|------|
| "blurred background, bokeh" | 주체 강조 |
| "detailed urban environment" | 도시 맥락 |
| "vast empty landscape" | 고독/자유 |
| "cozy indoor setting" | 따뜻한 분위기 |
| "abstract gradient background" | 미니멀, 디자인적 |

#### Layer 5: 조명/분위기
| 키워드 | 효과 | 적합 장면 |
|--------|------|----------|
| "golden hour light" | 따뜻한 황금빛 | 감성, 희망 |
| "blue hour" | 차가운 청색 | 고요, 우울 |
| "dramatic chiaroscuro" | 강한 명암 | 긴장, 갈등 |
| "soft diffused light" | 부드러운 산광 | 평화, 일상 |
| "neon glow" | 네온 발광 | 도시, SF |
| "moonlight" | 달빛 | 신비, 밤 |
| "overcast, flat lighting" | 흐린 하늘 | 다큐멘터리, 일상 |

## 스타일 일관성 유지 기법

### 시리즈 작업 시 일관성 핵심
1. **고정 프리픽스**: 모든 프롬프트 앞에 동일한 스타일 선언 고정
   ```
   "Soft watercolor illustration style, muted pastel palette, 
   Noto Serif Korean typography feel, [장면 묘사]"
   ```

2. **컬러 팔레트 고정**: 색상 코드를 명시
   ```
   "Color palette: dusty rose (#D4A5A5), sage green (#9CAF88), 
   cream (#FFF8E7), charcoal (#36454F)"
   ```

3. **분위기 앵커**: 감정/분위기 키워드 통일
   ```
   "melancholic yet hopeful atmosphere, nostalgic feeling"
   ```

4. **해상도/비율 통일**: 전 이미지 동일 사양
   ```
   "--ratio 16:9 --size 2K" (일관 적용)
   ```

## 네거티브 프롬프트 패턴

### 범용 네거티브
```
"NO text, NO watermark, NO signature, NO border, NO frame"
```

### 인물 사진용 네거티브
```
"NO distorted faces, NO extra fingers, NO deformed hands, 
NO unnatural proportions, NO uncanny valley"
```

### 깨끗한 배경용
```
"NO cluttered background, NO distracting elements, 
NO busy patterns"
```

### 텍스트 제어
```
"Text MUST be in Korean: '한글 텍스트'"
(텍스트 없는 이미지) "Absolutely NO text, NO letters, NO words, NO captions"
```

## 감정별 프롬프트 키워드 매핑

| 감정 | 조명 | 색상 | 구도 | 추가 키워드 |
|------|------|------|------|-----------|
| **희망** | golden hour, warm | 노랑, 주황, 밝은 파랑 | 로우앵글, 와이드 | "ascending", "opening" |
| **고독** | blue hour, dim | 청회색, 남색 | 와이드, 미니멀 | "isolated figure", "vast space" |
| **긴장** | harsh, chiaroscuro | 빨강, 검정 | 클로즈업, 틸트 | "sharp shadows", "contrast" |
| **평화** | soft diffused | 파스텔, 크림 | 와이드, 대칭 | "serene", "still", "gentle" |
| **슬픔** | overcast, rain | 회색, 탈채도 | 미디엄, 하이앵글 | "rain", "muted", "quiet" |
| **경외** | backlight, dramatic | 금색, 보라 | 로우앵글, 와이드 | "majestic", "awe-inspiring" |
| **따뜻함** | candlelight, warm | 앰버, 크림 | 클로즈업, 미디엄 | "cozy", "intimate", "soft" |

## 장면 유형별 프롬프트 템플릿

### 풍경 에스타블리싱
```
"[스타일] [시간대] [장소] landscape. [날씨/계절].
[전경 요소]. [중경 요소]. [원경 요소].
[조명]. [분위기 키워드]. NO text, NO people."
```

### 인물 포트레이트
```
"[스타일] [구도] portrait of [인물 묘사].
[표정/행동]. [의상]. [배경].
[조명]. [분위기]. [네거티브]."
```

### 사물/정물
```
"[스타일] [구도] [사물 묘사].
[배치/구성]. [배경/표면].
[조명: 보통 soft diffused]. [분위기]. NO text."
```

### 개념/추상
```
"[스타일: 보통 illustration/abstract] visual metaphor for [개념].
[시각적 요소 나열]. [컬러 팔레트].
[분위기]. Clean composition, NO text."
```

## 이미지 비율 가이드

| 비율 | 용도 | 설명 |
|------|------|------|
| 16:9 | 프레젠테이션, 배너 | 가장 범용적 |
| 3:2 | 사진, 포스터 | 자연스러운 프레임 |
| 1:1 | SNS 프로필, 썸네일 | 정사각 |
| 4:5 | Instagram 피드 | 세로 약간 긴 |
| 9:16 | 스토리, 릴스, 세로 배너 | 모바일 풀스크린 |
| 21:9 | 시네마틱, 히어로 배너 | 울트라와이드 |
