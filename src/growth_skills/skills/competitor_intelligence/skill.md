# 🔍 Skill: Competitor Intelligence

Map a competitor's GTM from their public footprint before they brief their own team.

## Input
```json
{
  "competitor": "string (name or URL)",
  "your_product": "string (optional — for gap analysis)",
  "depth": "string (quick | full)"
}
```

## Process
1. Scrape competitor's homepage, pricing page, and careers page
2. Extract: positioning statement, ICP signals, pricing model, growth channels
3. Scan job listings for GTM intent signals (hiring = investing)
4. Analyze ad copy and content strategy (if available)
5. Generate positioning map + counter-messaging brief

## Output
```json
{
  "positioning": {
    "headline_claim": "string",
    "icp_signals": ["string"],
    "pricing_model": "string",
    "key_features_emphasized": ["string"]
  },
  "growth_channels": ["string"],
  "hiring_signals": ["string"],
  "content_themes": ["string"],
  "gap_analysis": {
    "their_weakness": ["string"],
    "your_opportunity": ["string"]
  },
  "counter_messaging": {
    "positioning_angle": "string",
    "battle_card_bullets": ["string"]
  }
}
```

## Usage
```bash
growth-skills run --skill competitor_intelligence --competitor "Company Name" --depth full
```

## Value
- Know their GTM before they finish their weekly standup
- Hiring signals reveal where they're investing next quarter
- Battle card generated automatically — paste into sales deck
