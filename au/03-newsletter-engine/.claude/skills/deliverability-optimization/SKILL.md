---
name: deliverability-optimization
description: "Email deliverability optimisation skill used by the Editor-in-Chief and analyst agents. Provides spam filter avoidance, technical authentication, content filtering rules, and list hygiene management methodologies. Use for 'deliverability,' 'spam filters,' 'email authentication,' 'send optimisation,' and similar requests."
---

# Deliverability Optimisation — Email Deliverability Optimisation Methodology

Technical deliverability expertise used by the editor-in-chief and analyst agents when designing final edits and send strategies.

## Why Deliverability Matters

No matter how perfect your newsletter is, **if it doesn't reach the inbox**, all effort is wasted. On average, 15–20% of emails land in spam folders or promotional tabs.

## Spam Filter Trigger Avoidance Guide

### Subject Line Spam Trigger Words

| Risk Level | Word/Pattern | Alternative |
|-----------|-------------|-------------|
| **High** | Free, FREE, 100% off, Winner | "Complimentary," "Gift," "Special offer" |
| **High** | !!!, ???, ALL CAPS | One exclamation max, sentence case |
| **Medium** | Act now, Urgent, Deadline | "By this week," "Limited time" |
| **Medium** | Click here, Click now | "Check it out," "Take a look" |
| **Low** | Re:, Fwd: (fake reply/forward) | Absolutely prohibited — destroys trust |

### Body Content Filtering Rules

1. **Image-to-text ratio**: Keep images at 40% or less, text at 60% or more
2. **Link count**: 5–7 per email is optimal; 15+ risks spam classification
3. **Shortened URLs**: Shortened URLs (bit.ly, etc.) trigger spam filters — use original URLs
4. **HTML code quality**: No broken tags or excessive inline styles
5. **Unsubscribe link**: Must be clearly included at the bottom (legal obligation + spam prevention)

### Sender Reputation Management

| Factor | Optimal State | Management Method |
|--------|-------------|-------------------|
| **Bounce Rate** | Below 2% | Remove hard bounces immediately, soft bounces after 3 |
| **Spam Complaint Rate** | Below 0.01% | Maintain content quality, make unsubscribing easy |
| **Authentication** | SPF + DKIM + DMARC configured | Coordinate with domain administrator |
| **Dedicated IP** | When sending 100K+/month | Shared IPs are affected by others' reputation |
| **IP Warm-up** | Gradual increase over 2–4 weeks for new IPs | Day 1: 50 emails → double daily → target volume |

## Email Client Rendering Checks

Rendering issues that must be verified during newsletter editing:

| Client | Considerations |
|--------|---------------|
| **Gmail** | Prevent Promotions tab classification — reduce images, increase text, use personal tone |
| **Outlook** | Limited CSS support — avoid complex layouts, use table-based layouts |
| **Apple Mail** | Dark mode support — use transparent background images, test colour inversion |
| **All Mobile** | Single-column layout, buttons minimum 44x44px, font 14px+ |

### Gmail Promotions Tab Avoidance Strategy

1. **Personal tone**: "Hi [Name]" — minimise marketing-speak
2. **Minimise images**: Text-centric, limit to 1–2 images
3. **Minimise links**: Keep to 2–3 essential links only
4. **Encourage replies**: "Reply to this email" — signals two-way communication
5. **Sender name**: Personal name over brand name (e.g., "Jane from [Newsletter Name]")

## Legal Compliance Checklist

Legal requirements that must be verified when publishing a newsletter:

### Spam Act 2003 (Cth) (US)
- [ ] Physical mailing address included
- [ ] Unsubscribe processed within 10 business days
- [ ] No deceptive subject lines

### Privacy Act 1988 (Cth)/APPs (EU)
- [ ] Explicit consent (no pre-checked boxes)
- [ ] Data processing purpose stated
- [ ] Data deletion request handling system
- [ ] Privacy policy link

### CASL (Canada)
- [ ] Express or implied consent obtained
- [ ] Sender identification included
- [ ] Unsubscribe mechanism provided

## Editor-in-Chief's Pre-Send Checklist

| # | Item | Check |
|---|------|-------|
| 1 | No spam trigger words in subject line | [ ] |
| 2 | Preheader text configured | [ ] |
| 3 | All links verified working | [ ] |
| 4 | Image alt text entered | [ ] |
| 5 | Mobile rendering tested | [ ] |
| 6 | Unsubscribe link working | [ ] |
| 7 | Sender information accurate | [ ] |
| 8 | A/B test setup confirmed | [ ] |
| 9 | Send time optimised per segment | [ ] |
| 10 | Test send → receipt confirmed | [ ] |
