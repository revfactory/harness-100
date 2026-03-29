---
name: nutrition-calculator
description: "Specialized calculation engine for nutrient requirement estimation and macro distribution. The 'nutritionist' and 'meal-designer' agents must use this skill's formulas and reference tables when calculating individual calorie/macro targets and designing meal plans. Use for 'calorie calculation', 'macro distribution', 'TDEE estimation', etc. Recipe writing and grocery lists are outside the scope of this skill."
---

# Nutrition Calculator — Nutrient Calculation Engine

Calculates energy requirements, macro distribution, and micronutrient targets based on individual body metrics.

## Basal Metabolic Rate (BMR) Calculation

### Mifflin-St Jeor Formula (Recommended)

```
Male:   BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5
Female: BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161

Example: 30-year-old male, 178 cm, 80 kg
  BMR = (10 × 80) + (6.25 × 178) - (5 × 30) + 5
      = 800 + 1112.5 - 150 + 5 = 1767.5 kcal
```

### Harris-Benedict Formula (Secondary)

```
Male:   BMR = 88.362 + (13.397 × weight_kg) + (4.799 × height_cm) - (5.677 × age)
Female: BMR = 447.593 + (9.247 × weight_kg) + (3.098 × height_cm) - (4.330 × age)
```

## Total Daily Energy Expenditure (TDEE) Calculation

```
TDEE = BMR × Activity Factor

Activity Factors:
  1.2:   Sedentary (desk job, no exercise)
  1.375: Lightly active (light exercise 1-3 days/week)
  1.55:  Moderately active (moderate exercise 3-5 days/week)
  1.725: Very active (intense exercise 6-7 days/week)
  1.9:   Extremely active (athletes, physical labor)
```

## Goal-Based Calorie Adjustment

| Goal | Calorie Adjustment | Recommended Rate | Notes |
|------|--------------------|------------------|-------|
| Weight loss | TDEE - 300~500 kcal | 0.3~0.5 kg/week | Never go below BMR |
| Gradual loss | TDEE - 200~300 kcal | 0.2~0.3 kg/week | Minimize muscle loss |
| Maintenance | TDEE ± 0 | 0 | Stable weight |
| Lean bulk | TDEE + 200~300 kcal | 0.1~0.2 kg/week | Minimize fat gain |
| Bulk | TDEE + 300~500 kcal | 0.3~0.5 kg/week | Favorable for beginners |

**Safe minimum threshold**: No less than 1500 kcal for males, 1200 kcal for females

## Macronutrient Distribution

### Macro Ratios by Goal

| Goal | Protein | Carbohydrates | Fat | Notes |
|------|---------|---------------|-----|-------|
| General health | 15-20% | 50-60% | 20-30% | Korean Nutrition Society recommendation |
| Weight loss | 25-30% | 40-50% | 25-30% | High protein for satiety |
| Muscle gain | 25-35% | 40-50% | 20-25% | 1.6-2.2g protein per kg body weight |
| Low-carb / high-fat | 20-25% | 10-20% | 55-65% | Keto adaptation required |
| Diabetes management | 20-25% | 40-45% | 30-35% | Low-GI carbohydrates |

### Gram Conversion

```
Protein:      1g = 4 kcal
Carbohydrates: 1g = 4 kcal
Fat:           1g = 9 kcal
Alcohol:       1g = 7 kcal

Example: 1800 kcal, weight loss goal (25/45/30)
  Protein:      1800 × 0.25 / 4 = 112.5g
  Carbohydrates: 1800 × 0.45 / 4 = 202.5g
  Fat:           1800 × 0.30 / 9 = 60g
```

## Daily Micronutrient Reference Intake (Korean Standards)

| Nutrient | Adult Male | Adult Female | Main Sources |
|----------|------------|--------------|--------------|
| Vitamin A | 800 μg RE | 650 μg RE | Liver, carrots, spinach |
| Vitamin C | 100 mg | 100 mg | Kiwi, peppers, strawberries |
| Vitamin D | 10 μg | 10 μg | Salmon, eggs, mushrooms |
| Calcium | 800 mg | 800 mg | Milk, dried anchovies, tofu |
| Iron | 10 mg | 14 mg | Beef, spinach, clams |
| Dietary fiber | 25-30 g | 20-25 g | Brown rice, vegetables, fruit |
| Sodium | <2000 mg | <2000 mg | — (limit) |

## Meal Distribution Strategy

| Pattern | Distribution | Best For |
|---------|--------------|----------|
| 3 equal meals | 33/33/34 | Regular lifestyle |
| Breakfast-heavy | 40/35/25 | High morning activity |
| Light dinner | 30/40/30 | Weight loss goal |
| 3 meals + snack | 25/30/30/15 | Blood sugar management |
| Intermittent fasting 16:8 | 0/50/50 | Weight loss (lunch–dinner) |

## Special Situation Adjustments

| Situation | Adjustment |
|-----------|------------|
| Early pregnancy | +0 kcal, folate 600 μg |
| Mid/late pregnancy | +300-450 kcal, iron 24 mg |
| Breastfeeding | +500 kcal, increased calcium |
| Elderly (65+) | Protein 1.0-1.2g/kg, increased vitamin D |
| Adolescents | +300-500 kcal for growth |

## References

- Based on Korean Dietary Reference Intakes (KDRIs) 2020 by the Korean Nutrition Society
- Detailed nutrient database: see `references/nutrient-database.md`
