# 🏦 Twenty CRM — GTM Pipeline Integration Guide

Twenty CRM is a free, open-source, self-hostable CRM with a modern UI and full REST + GraphQL API.  
**GitHub:** https://github.com/twentyhq/twenty  
**Why Twenty:** Clean API, Notion-like interface, self-hosted = no data lock-in.

---

## GTM Data Flow

```
SIGNAL (LinkedIn / Ad Click / Email Reply)
      ↓
PROCESS (growth-skills: gtm_lead_scorer)
      ↓
OUTPUT → Twenty CRM (API update)
      ↓
TRIGGER (email sequence / Telegram alert / demo booking)
```

---

## Quick Setup (Docker)

```bash
# Clone and run Twenty CRM locally
git clone https://github.com/twentyhq/twenty.git
cd twenty
cp .env.example .env
docker-compose up -d
# Access at http://localhost:3000
```

---

## API Integration

### Environment Variables
```bash
TWENTY_CRM_URL=http://localhost:3000
TWENTY_API_KEY=your_api_key_here  # Generate in Twenty Settings → API
```

### Create / Update a Lead

```python
import httpx

TWENTY_URL = "http://localhost:3000"
TWENTY_KEY = "your_api_key"

def upsert_lead(lead_data: dict, score_result: dict) -> dict:
    """Push a scored lead into Twenty CRM."""
    
    headers = {
        "Authorization": f"Bearer {TWENTY_KEY}",
        "Content-Type": "application/json",
    }
    
    # Map growth-skills output to Twenty fields
    payload = {
        "name": {
            "firstName": lead_data.get("name", "").split(" ")[0],
            "lastName": " ".join(lead_data.get("name", "").split(" ")[1:]),
        },
        "jobTitle": lead_data.get("title"),
        "company": {"name": lead_data.get("company")},
        # Custom fields (create these in Twenty Settings → Fields)
        "leadScore": score_result.get("score"),
        "icpFit": score_result.get("icp_fit"),
        "nextAction": score_result.get("next_action"),
        "tags": score_result.get("crm_tags", []),
    }
    
    response = httpx.post(
        f"{TWENTY_URL}/api/people",
        json=payload,
        headers=headers,
    )
    return response.json()
```

### Full Pipeline Example

```python
from growth_skills.skills.gtm_lead_scorer.prompt import score_lead

# 1. Score the lead
lead = {
    "name": "Jane Doe",
    "title": "Head of Growth",
    "company": "Acme SaaS",
    "source": "linkedin",
    "behavior_signals": ["visited pricing page", "opened email 2x"]
}
score = score_lead(lead, llm_client=your_llm)

# 2. Push to Twenty CRM
crm_result = upsert_lead(lead, score)

# 3. Trigger next action based on score
if score["next_action"] == "demo":
    # Trigger calendar link email
    pass
elif score["next_action"] == "nurture":
    # Add to email sequence
    pass
```

---

## Recommended Custom Fields in Twenty CRM

| Field Name | Type | Source |
|---|---|---|
| `lead_score` | Number | `gtm_lead_scorer.score` |
| `icp_fit` | Select | `gtm_lead_scorer.icp_fit` |
| `next_action` | Select | `gtm_lead_scorer.next_action` |
| `intent_level` | Select | `gtm_lead_scorer.intent_level` |
| `lead_source` | Select | Input data |
| `ai_reasoning` | Text | `gtm_lead_scorer.reasoning` |

---

## Stage Mapping

| Score | ICP Fit | Next Action | Twenty Stage |
|---|---|---|---|
| 70-100 | Strong | Demo | Opportunity → Demo Scheduled |
| 40-69 | Moderate | Nurture | Lead → In Sequence |
| 0-39 | Weak | Disqualify | Lead → Disqualified |

---

## Resources
- [Twenty CRM Docs](https://docs.twenty.com)
- [Twenty API Reference](https://docs.twenty.com/api-reference)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
