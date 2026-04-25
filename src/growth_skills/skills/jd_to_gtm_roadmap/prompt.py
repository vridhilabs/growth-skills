"""
JD to GTM Roadmap — Convert any job description into a Founder-Operator growth strategy.
Source: RaGa Sovereign OS / strategic_planner.py
"""

import json
from typing import Any

EXTRACT_PROMPT = """
You are a GTM strategist and systems thinker. Analyze this job description deeply.

## Job Description
{job_description}

## Extraction Task
Extract the following:
1. Core mission of the role (what business outcome they need)
2. Must-have skills and platforms
3. Implied tools and tech stack (even if not mentioned directly)
4. Hidden expectations (what they'll judge you on in month 3)
5. 5-7 functional workstreams this role covers
6. Success metrics implied by the language

Output as JSON:
{{
  "role_mission": "string",
  "must_have_skills": ["string"],
  "implied_tech_stack": {{"crm": "string", "analytics": "string", "automation": "string", "ads": "string"}},
  "hidden_expectations": ["string"],
  "workstreams": [
    {{"name": "string", "objective": "string", "kpis": ["string"], "tools": ["string"]}}
  ],
  "success_metrics_month_3": ["string"]
}}
"""

ROADMAP_PROMPT = """
You are a Founder-Operator GTM strategist. Build a phased execution roadmap from the role intelligence below.

## Role Intelligence
{role_intelligence}

## Context (optional)
{context}

## Roadmap Rules
- Month 1: Audit, instrument, and establish baselines. No big bets yet.
- Month 2: First experiments running. One channel scaled.
- Month 3+: Compound growth. Automation live. Team enablement.
- Every phase must have: goal, 3 key actions, and one metric to hit

Output as JSON:
{{
  "role_summary": "string (1 sentence, Founder-Operator style)",
  "roadmap": {{
    "month_1": {{
      "goal": "string",
      "actions": ["string x3"],
      "metric": "string"
    }},
    "month_2": {{
      "goal": "string",
      "actions": ["string x3"],
      "metric": "string"
    }},
    "month_3_plus": {{
      "goal": "string",
      "actions": ["string x3"],
      "metric": "string"
    }}
  }},
  "tool_stack": {{
    "crm": "string",
    "analytics": "string",
    "automation": "string",
    "content": "string",
    "ads": "string"
  }},
  "positioning_angle": "string (how to position yourself or your product against their needs)"
}}
"""


def generate_roadmap(
    job_description: str,
    context: str = "",
    llm_client=None,
) -> dict[str, Any]:
    """
    Convert a job description into a Founder-Operator GTM roadmap.
    
    Args:
        job_description: Raw JD text (paste directly)
        context: Optional — your product/service context for positioning
        llm_client: LLM client with .complete(prompt) -> str
    
    Returns:
        Full roadmap dict with workstreams, phases, tool stack, and positioning
    """
    if llm_client is None:
        return {"error": "LLM client required for roadmap generation. Set OPENAI_API_KEY or ANTHROPIC_API_KEY."}

    # Phase 1: Extract intelligence from JD
    extract_raw = llm_client.complete(
        EXTRACT_PROMPT.format(job_description=job_description)
    )
    
    try:
        role_intelligence = json.loads(extract_raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', extract_raw, re.DOTALL)
        role_intelligence = json.loads(match.group()) if match else {"raw": extract_raw}

    # Phase 2: Build roadmap from intelligence
    roadmap_raw = llm_client.complete(
        ROADMAP_PROMPT.format(
            role_intelligence=json.dumps(role_intelligence, indent=2),
            context=context or "Not provided",
        )
    )

    try:
        roadmap = json.loads(roadmap_raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', roadmap_raw, re.DOTALL)
        roadmap = json.loads(match.group()) if match else {"raw": roadmap_raw}

    return {
        "intelligence": role_intelligence,
        **roadmap,
    }
