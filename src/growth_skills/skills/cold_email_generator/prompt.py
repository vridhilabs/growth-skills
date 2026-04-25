"""
Cold Email Generator — Hyper-personalized outreach from a prospect URL.
Source: RaGa Sovereign OS / email_outreach.py + fork_synthesizer.py
"""

import json
from typing import Any

RESEARCH_PROMPT = """
You are a GTM researcher. Extract key personalization data from this prospect information.

## Prospect Data
{prospect_data}

Extract:
1. Current role and what they likely own/care about
2. Company's biggest visible challenge or growth moment
3. One specific hook (recent news, job post, content they shared)
4. Their likely buying priorities given their stage

Output as JSON:
{{
  "role_focus": "string",
  "company_challenge": "string", 
  "personalization_hook": "string",
  "buying_priority": "string"
}}
"""

EMAIL_PROMPT = """
You are a world-class cold email writer. Write 3 email variations using the prospect intel below.

## Sender Context
{sender_context}

## Prospect Intel
{prospect_intel}

## Goal
{goal}

## Rules
- Subject line: max 7 words, no clickbait
- Body: max 4 sentences. No "I hope this finds you well."
- CTA: one specific ask, not "let me know if interested"
- Each variation uses a different angle

Angles:
1. Pain Point: Lead with their specific challenge, position your solution
2. Curiosity: Open a loop, make them want to know more
3. Social Proof: Lead with a result for someone like them

Output as JSON:
{{
  "subject_lines": ["pain subject", "curiosity subject", "proof subject"],
  "email_body": {{
    "angle_1_pain": "string",
    "angle_2_curiosity": "string", 
    "angle_3_social_proof": "string"
  }},
  "follow_up": {{
    "day_3": "string",
    "day_7": "string"
  }},
  "personalization_hooks": ["hook1", "hook2"],
  "send_time_recommendation": "string"
}}
"""


def generate_emails(
    prospect_url: str,
    sender_context: str,
    goal: str = "demo",
    scraper=None,
    llm_client=None,
) -> dict[str, Any]:
    """
    Generate cold email sequence for a prospect.
    
    Args:
        prospect_url: LinkedIn or company URL of the prospect
        sender_context: Who you are and what you offer (2-3 sentences)
        goal: Outreach goal — 'demo', 'partnership', 'intro', 'job'
        scraper: Optional scraper client with .scrape(url) -> str
        llm_client: LLM client with .complete(prompt) -> str
    
    Returns:
        Dict with subject lines, 3 email variations, follow-up sequence
    """
    # Step 1: Get prospect data
    if scraper:
        raw_data = scraper.scrape(prospect_url)
    else:
        raw_data = f"Prospect URL: {prospect_url} (scraper not configured — add key facts manually)"

    # Step 2: Research phase
    if llm_client:
        research_raw = llm_client.complete(
            RESEARCH_PROMPT.format(prospect_data=raw_data)
        )
        try:
            prospect_intel = json.loads(research_raw)
        except json.JSONDecodeError:
            prospect_intel = {"raw": research_raw}

        # Step 3: Email generation
        email_raw = llm_client.complete(
            EMAIL_PROMPT.format(
                sender_context=sender_context,
                prospect_intel=json.dumps(prospect_intel, indent=2),
                goal=goal,
            )
        )
        try:
            return json.loads(email_raw)
        except json.JSONDecodeError:
            import re
            match = re.search(r'\{.*\}', email_raw, re.DOTALL)
            if match:
                return json.loads(match.group())
            return {"raw_output": email_raw}
    
    # Fallback template when no LLM configured
    return _template_fallback(sender_context, goal)


def _template_fallback(sender_context: str, goal: str) -> dict[str, Any]:
    """Returns a structured template when no LLM is available."""
    return {
        "subject_lines": [
            "Quick question about [their_challenge]",
            "How [similar_company] solved [problem] in 30 days",
            "[mutual_connection] suggested I reach out",
        ],
        "email_body": {
            "angle_1_pain": f"Hi [Name],\n\nI noticed [specific challenge]. Most [their role]s I talk to lose X hours/week on this.\n\n{sender_context}\n\nWorth a 15-min call this week?",
            "angle_2_curiosity": "Hi [Name],\n\nThere's a pattern I keep seeing in [their industry] — [hook]. Curious if you're seeing the same.\n\nHappy to share what we've found if useful.",
            "angle_3_social_proof": "Hi [Name],\n\n[Similar company] used this approach to [result]. Given [their specific context], I thought it might be relevant.\n\nCan I send over a quick breakdown?",
        },
        "follow_up": {
            "day_3": "Just bumping this up — did the timing work for you?",
            "day_7": "Last follow-up. If now's not the right time, totally fine — just let me know and I'll check back in [month].",
        },
        "personalization_hooks": ["[recent company news]", "[job posting signal]"],
        "send_time_recommendation": "Tuesday-Thursday, 8-10am or 4-5pm local time",
    }
