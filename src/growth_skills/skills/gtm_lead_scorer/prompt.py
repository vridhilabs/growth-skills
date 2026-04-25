"""
GTM Lead Scorer — AI-native ICP scoring for inbound leads.
Source: RaGa Sovereign OS / analyzer.py + curator.py
"""

import json
from typing import Any

SCORE_PROMPT = """
You are a GTM analyst scoring an inbound lead against an Ideal Customer Profile (ICP).

## Lead Data
{lead_data}

## ICP Definition
{icp_definition}

## Scoring Rules
- Score 0-100 based on ICP fit and intent signals
- Title/seniority: VP/Director/Head/Founder = high weight
- Company size: Match ICP size band (startup <50, SMB 50-500, Enterprise 500+)
- Intent signals: Each signal adds weight (email opens, pricing page, demo request = highest)
- Source weight: referral > inbound > linkedin > ad

## Output Format (JSON only, no markdown)
{{
  "score": <integer 0-100>,
  "icp_fit": "<strong|moderate|weak>",
  "intent_level": "<high|medium|low>",
  "next_action": "<demo|nurture|disqualify|watch>",
  "reasoning": "<1-2 sentence explanation>",
  "crm_tags": ["<tag1>", "<tag2>"]
}}
"""

DEFAULT_ICP = {
    "target_titles": ["VP", "Director", "Head of Growth", "CMO", "Founder", "CEO"],
    "target_industries": ["SaaS", "EdTech", "FinTech", "HealthTech", "Marketplace"],
    "company_size_band": "10-500",
    "high_intent_signals": ["pricing page", "demo request", "opened 3+ times", "replied"],
}


def build_prompt(lead: dict[str, Any], icp: dict[str, Any] | None = None) -> str:
    """Build the scoring prompt with lead data and ICP definition."""
    icp = icp or DEFAULT_ICP
    return SCORE_PROMPT.format(
        lead_data=json.dumps(lead, indent=2),
        icp_definition=json.dumps(icp, indent=2),
    )


def score_lead(lead: dict[str, Any], icp: dict[str, Any] | None = None, llm_client=None) -> dict[str, Any]:
    """
    Score a lead against ICP criteria using LLM.
    
    Args:
        lead: Lead data dict (see schema.json for structure)
        icp: Optional custom ICP definition. Uses DEFAULT_ICP if not provided.
        llm_client: LLM client (OpenAI, Anthropic, etc.). Must have .complete(prompt) method.
    
    Returns:
        Scoring result dict with score, icp_fit, intent_level, next_action, reasoning, crm_tags
    """
    prompt = build_prompt(lead, icp)

    if llm_client is None:
        # Fallback: rule-based scoring for environments without LLM
        return _rule_based_score(lead, icp or DEFAULT_ICP)

    raw = llm_client.complete(prompt)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Extract JSON from response if wrapped in markdown
        import re
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError(f"Could not parse LLM response: {raw}")


def _rule_based_score(lead: dict[str, Any], icp: dict[str, Any]) -> dict[str, Any]:
    """Lightweight rule-based scorer for LLM-free environments."""
    score = 0
    tags = []

    # Title scoring
    title = lead.get("title", "").lower()
    senior_signals = ["vp", "director", "head", "cmo", "ceo", "founder", "chief"]
    if any(s in title for s in senior_signals):
        score += 35
        tags.append("senior-buyer")
    elif "manager" in title or "lead" in title:
        score += 20
        tags.append("mid-level")

    # Intent signals
    behavior = [s.lower() for s in lead.get("behavior_signals", [])]
    high_intent = ["pricing", "demo", "trial", "replied"]
    for signal in behavior:
        if any(h in signal for h in high_intent):
            score += 20
            tags.append("high-intent")
            break
        score += 5

    # Source scoring
    source_weights = {"referral": 20, "inbound": 15, "linkedin": 10, "email": 8, "ad": 5}
    score += source_weights.get(lead.get("source", ""), 5)

    score = min(score, 100)

    if score >= 70:
        icp_fit, intent, action = "strong", "high", "demo"
    elif score >= 40:
        icp_fit, intent, action = "moderate", "medium", "nurture"
    else:
        icp_fit, intent, action = "weak", "low", "disqualify"

    return {
        "score": score,
        "icp_fit": icp_fit,
        "intent_level": intent,
        "next_action": action,
        "reasoning": f"Rule-based score: {score}/100 based on title, behavior signals, and source.",
        "crm_tags": list(set(tags)),
    }


def batch_score(leads: list[dict[str, Any]], icp: dict[str, Any] | None = None, llm_client=None) -> list[dict[str, Any]]:
    """Score a list of leads. Returns results with original lead data merged."""
    results = []
    for lead in leads:
        result = score_lead(lead, icp, llm_client)
        results.append({**lead, "scoring": result})
    return results
