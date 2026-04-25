# 📧 Skill: Cold Email Generator

Turn a prospect URL into a hyper-personalized cold email + follow-up sequence. No generic templates.

## Input
```json
{
  "prospect_url": "string (LinkedIn URL or company website)",
  "sender_context": "string (who you are, what you offer)",
  "goal": "string (demo | partnership | intro | job)"
}
```

## Process
1. Scrape prospect's LinkedIn profile or company homepage
2. Extract: current role, recent activity, company pain points, news signals
3. Map to sender's value proposition
4. Generate 3 email variations with different angles (pain, curiosity, social proof)
5. Generate 2-step follow-up sequence

## Output
```json
{
  "subject_lines": ["string x3"],
  "email_body": {
    "angle_1_pain": "string",
    "angle_2_curiosity": "string",
    "angle_3_social_proof": "string"
  },
  "follow_up": {
    "day_3": "string",
    "day_7": "string"
  },
  "personalization_hooks": ["string"],
  "send_time_recommendation": "string"
}
```

## Usage
```bash
growth-skills run --skill cold_email_generator --input prospect.json
```

## Value
- Replaces 45min of research + writing per prospect
- 3x variations means you can A/B test from day one
- Follow-up sequence built in — no forgetting
