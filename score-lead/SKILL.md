# Score Lead

Score an inbound lead against your ICP. Tell me the lead's name, title, company, how they came in, and any behavior signals (email opens, page visits, replies). I'll return a score 0–100, ICP fit rating, intent level, recommended next action, and CRM tags.

## What to provide

- Name and title
- Company name (and size if known)
- Source: linkedin / email / ad / referral / inbound
- Behavior signals: anything they've done (e.g. "opened email 3x", "visited pricing page", "replied to follow-up")

## What you'll get back

```
Score: 82/100
ICP Fit: Strong
Intent: High
Next Action: Demo
Reasoning: VP-level buyer at a 200-person SaaS company. Visited pricing page + replied. High-purchase-intent pattern.
CRM Tags: [senior-buyer, high-intent, pricing-signal]
```

## Scoring rules I apply

- **Title weight**: VP / Director / Head / Founder / CEO = high buying power
- **Company size**: Match against your ICP band (startup <50, SMB 50–500, Enterprise 500+)
- **Intent signals**: Pricing page, demo request, multiple email opens, direct reply = strong intent
- **Source weight**: referral > inbound > linkedin > ad

## CRM mapping (Twenty CRM)

| Field | Maps to |
|---|---|
| Score | `opportunity.lead_score` |
| Next Action | `opportunity.stage` |
| CRM Tags | `opportunity.tags` |

## Example

**Input:**
> Jane Doe, Head of Growth at Acme (150 people), came in through LinkedIn. Visited our pricing page twice and replied to my cold email.

**Output:**
> Score: 78/100 · ICP Fit: Strong · Intent: High · Next Action: Demo
> Reasoning: Senior GTM buyer, company in ICP size range, pricing page + reply = high intent combo.
> Tags: [senior-buyer, high-intent, pricing-signal, linkedin]
