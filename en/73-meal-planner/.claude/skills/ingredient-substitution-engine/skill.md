---
name: ingredient-substitution-engine
description: "A guide for ingredient substitutions and allergy/dietary restriction responses. When the 'recipe-writer' and 'meal-designer' agents write recipes that accommodate dietary restrictions or select substitute ingredients, they must use the substitution matrix and conversion rules from this skill. Use for 'ingredient substitution', 'allergy response', 'vegan substitution', and similar requests. Note: calorie calculation and grocery lists are outside the scope of this skill."
---

# Ingredient Substitution Engine

Selects appropriate substitutes and adjusts cooking methods for dietary restrictions, allergies, and missing ingredients.

## Allergy Substitution Matrix

### Substitutes for the 8 Major Allergens

| Allergen | Substitute | Ratio by Use Case | Nutritional Notes |
|-------------|--------|-----------|----------|
| Milk | Soy milk, oat milk, coconut milk | 1:1 | Calcium supplementation needed |
| Egg | Flaxseed + water (1T:3T), 1/2 banana, 1/4 cup tofu | Per egg | Separate protein supplementation |
| Wheat (gluten) | Rice flour, buckwheat flour, cornstarch | 0.7~1:1 | Dietary fiber supplementation |
| Soy | Peas, sunflower seeds, coconut aminos | By use case | Check protein content |
| Peanut | Sunflower seed butter, pumpkin seed butter | 1:1 | Similar nutrition |
| Tree nuts | Sunflower seeds, pumpkin seeds, coconut | 1:1 | Check unsaturated fats |
| Shellfish | King oyster mushrooms, hearts of palm | Texture substitute | Iodine supplementation |
| Fish | Seaweed (wakame, nori), chia seeds (omega-3) | Nutritional substitute | Omega-3 supplementation |

### Cross-Allergy Warnings

```
Milk allergy → Goat milk also caution (approx. 90% cross-reactivity)
Wheat allergy → Barley, rye also caution (gluten)
Soy allergy → Other legumes generally safe (confirmation needed)
Peanut → Cross-reaction possible with other tree nuts
Shrimp → High cross-reactivity with crab, lobster
```

## Substitution Guide by Dietary Restriction

### Vegan

| Original Ingredient | Substitute | Notes |
|--------|--------|------|
| Beef / pork | Tofu, seitan, tempeh, jackfruit | Check protein content |
| Chicken | Soy meat, tofu, chickpeas | Similar texture |
| Fish | Seaweed, coconut aminos | Supplement umami |
| Butter | Coconut oil, vegan margarine | 1:1 |
| Honey | Agave syrup, maple syrup | 1:1 (sweetness varies) |
| Cheese | Nutritional yeast, cashew cream | Umami substitute |
| Gelatin | Agar-agar, guar gum | Ratio varies by use case |

### Diabetes / Low-Carb

| High-Carb Ingredient | Low-Carb Substitute | Carb Reduction |
|-----------|-----------|------------|
| White rice | Cauliflower rice, konjac rice | -80% |
| Wheat noodles | Konjac noodles, tofu noodles, zucchini noodles | -70~90% |
| Potato | Cauliflower, daikon radish | -60% |
| Sugar | Erythritol, stevia, allulose | -100% (calories) |
| Bread | Egg bread, almond flour bread | -50~70% |

### Halal / Kosher

| Prohibited Ingredient | Substitute |
|----------|--------|
| Pork | Beef, chicken, lamb |
| Lard | Vegetable oil, butter |
| Mirin (alcohol) | Vinegar + sugar, plum syrup |
| Gelatin (pork) | Fish gelatin, agar-agar |

## Cooking Adjustment Rules

### Cooking Time Changes When Substituting

| Change | Adjustment |
|------|------|
| Wheat flour → Rice flour | Reduce moisture by 10%, same temperature |
| Butter → Oil | Reduce quantity by 20%, temperature -10°C |
| Sugar → Erythritol | Use 130% quantity (70% sweetness) |
| Heavy cream → Coconut cream | Same quantity, refrigeration time +2 hours |
| Regular tofu → Frozen tofu | Thaw and remove moisture, similar texture |

### Flavor Compensation Strategies

```
Lacking umami (when removing meat):
  → Soy sauce + shiitake mushrooms + kelp + nutritional yeast

Lacking creamy texture (when removing dairy):
  → Cashew cream + coconut milk + avocado

Lacking crispy texture (when removing wheat flour):
  → Rice flour + starch + high-heat oven finish

Lacking binding (when removing eggs):
  → Flaxseed water + starch + mashed tofu
```

## References

- Ministry of Food and Drug Safety food allergy labeling standards
- Detailed substitution recipes: see `references/substitution-recipes.md`
