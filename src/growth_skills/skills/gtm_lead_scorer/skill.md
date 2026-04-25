# 🎯 Skill: GTM Lead Scorer

Score any inbound lead against your ICP in seconds. Replaces 30min of manual CRM triage per lead.

## Input
```json
{
  "name": "string",
  "title": "string",
  "company": "string",
  "company_size": "string (optional)",
  "source": "string (linkedin | email | ad | referral | inbound)",
  "behavior_signals": ["string"] // e.g. ['opened email 3x', 'visited pricing page']
}
```

## Process
1. Extract seniority level and buying power from title
2. Match company profile against ICP criteria (size, industry, stage)
3. Weight intent signals by recency and depth
4. Run LLM scoring chain against configurable ICP definition
5. Assign next action tag

## Output
```json
{
  "score": 0-100,
  "icp_fit": "strong | moderate | weak",
  "intent_level": "high | medium | low",
  "next_action": "demo | nurture | disqualify | watch",
  "reasoning": "string",
  "crm_tags": ["string"]
}
```

## CRM Integration
Output maps directly to **Twenty CRM** opportunity fields:
- `score` → custom field `lead_score`
- `next_action` → stage update
- `crm_tags` → tag array

## Usage
```bash
growth-skills run --skill gtm_lead_scorer --input lead.json
```

## Value
- **Time saved:** ~25-30 min per lead manually scored
- **Consistency:** Same ICP criteria applied every time, no gut-feel drift
- **Scale:** Works on 1 lead or 1000 in batch mode
