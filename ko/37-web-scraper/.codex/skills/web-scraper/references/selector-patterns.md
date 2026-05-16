# Selector Patterns

Use this for parser and monitor design.

## Selector Priority

1. Unique ID: `#product-price`
2. `data-*` attributes: `[data-testid="price"]`
3. Semantic class: `.product-price`
4. ARIA attribute: `[aria-label="가격"]`
5. Structural selector: `article > .info > span`
6. Text XPath: `//span[contains(text(),"원")]`

Avoid:

| Pattern | Problem | Alternative |
|---|---|---|
| `.css-1a2b3c` | generated hash changes | parent semantic element |
| `div > div > div > span` | fragile to layout changes | meaningful class or data attribute |
| bare `:nth-child(7)` | breaks when elements move | class plus nth-child if necessary |

## Common Recipes

### Product List

```javascript
const selectors = {
  container: 'ul.product-list > li',
  name: '.product-name, h3.title',
  currentPrice: '.sale-price, [data-price]',
  originalPrice: '.original-price, del',
  image: 'img.product-image',
  link: 'a.product-link',
  nextPage: 'a.next, [rel="next"]',
};
```

### News Or Board

```javascript
const selectors = {
  articleList: 'article, .post-item',
  title: 'h2 > a, .article-title',
  author: '.author, .writer',
  date: 'time, .date',
  content: 'article .content, .post-body',
};
```

### JSON API

```javascript
const mapping = {
  id: 'data.items[].id',
  title: 'data.items[].title',
  url: 'data.items[].url',
  updatedAt: 'data.items[].updated_at',
};
```

## CSS vs XPath

| Situation | Prefer | Example |
|---|---|---|
| ID/class/data attributes | CSS | `#price`, `[data-price]` |
| text contains | XPath | `//span[contains(text(),"원")]` |
| parent traversal | XPath | `//span[@class="price"]/parent::div` |
| sibling relation | XPath | `//dt[text()="가격"]/following-sibling::dd` |
| complex condition | XPath | `//div[@class="item" and .//span[@class="sale"]]` |

## Robustness Score

```text
+30 ID
+25 data-testid or stable data attribute
+20 semantic class
+15 ARIA attribute
-10 bare nth-child
-20 generated/hash class
-30 nesting deeper than 5 levels

80-100: stable
60-79: acceptable
40-59: fragile
0-39: dangerous
```

## Drift Detection

Track each critical selector with an expected pattern, expected count, fallback selectors, and status.

```json
{
  "selector": ".product-price",
  "expectedPattern": "[\\d,]+원",
  "expectedCountMin": 1,
  "fallbackSelectors": ["[data-price]", "span.price"],
  "status": "active"
}
```

## Cleaning Patterns

```javascript
function cleanPrice(raw) {
  const digits = String(raw || '').replace(/[^\d]/g, '');
  return digits ? Number(digits) : null;
}

function cleanWhitespace(raw) {
  return String(raw || '').replace(/\s+/g, ' ').trim();
}

function cleanUrl(raw, base) {
  return new URL(raw, base).toString();
}
```
