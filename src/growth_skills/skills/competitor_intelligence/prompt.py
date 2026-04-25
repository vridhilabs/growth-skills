"""
Competitor Intelligence — Map a competitor's GTM from their public footprint.
Source: RaGa Sovereign OS / scrapling_search.py + analyzer.py
"""

import json
from typing import Any

INTEL_PROMPT = """
You are a competitive intelligence analyst. Analyze the competitor data below and extract a GTM map.

## Competitor Data
{competitor_data}

## Your Product (for gap analysis)
{your_product}

## Analysis Tasks

1. **Positioning**: What's their core claim? Who are they targeting? What do they emphasize?
2. **Growth Channels**: What channels are they investing in? (infer from job posts, content, ads)
3. **Hiring Signals**: What roles are they hiring? What does this reveal about their next 6 months?
4. **Content Themes**: What topics do they own? What angle do they take?
5. **Gaps**: Where are they weak? Where is there a clear opening?
6. **Counter-Messaging**: How do you position against them?

Output as JSON:
{{
  "positioning": {{
    "headline_claim": "string",
    "icp_signals": ["string"],
    "pricing_model": "string",
    "key_features_emphasized": ["string"]
  }},
  "growth_channels": ["string"],
  "hiring_signals": ["string (role → intent signal)"],
  "content_themes": ["string"],
  "gap_analysis": {{
    "their_weakness": ["string"],
    "your_opportunity": ["string"]
  }},
  "counter_messaging": {{
    "positioning_angle": "string",
    "battle_card_bullets": ["string x5"]
  }}
}}
"""

SCRAPE_TARGETS = [
    "homepage",
    "pricing",
    "about",
    "blog (recent 3 posts)",
    "careers page",
]


def analyze_competitor(
    competitor: str,
    your_product: str = "",
    depth: str = "quick",
    scraper=None,
    llm_client=None,
) -> dict[str, Any]:
    """
    Generate competitor GTM intelligence map.
    
    Args:
        competitor: Competitor name or URL
        your_product: Your product/service for gap analysis (optional)
        depth: 'quick' (homepage + pricing) or 'full' (+ careers + blog)
        scraper: Optional scraper with .scrape(url) -> str
        llm_client: LLM client with .complete(prompt) -> str
    
    Returns:
        Dict with positioning map, growth channels, hiring signals, gap analysis, battle card
    """
    # Build competitor data string
    if scraper:
        pages = SCRAPE_TARGETS if depth == "full" else SCRAPE_TARGETS[:2]
        raw_data = f"Competitor: {competitor}\n\n"
        for page in pages:
            try:
                content = scraper.scrape(f"{competitor}/{page.split(' ')[0]}")
                raw_data += f"### {page}\n{content}\n\n"
            except Exception:
                pass
    else:
        raw_data = f"Competitor: {competitor}\n\nNote: Scraper not configured. Provide known data or configure a scraper client."

    if llm_client is None:
        return {
            "error": "LLM client required for analysis.",
            "competitor": competitor,
            "tip": "Set OPENAI_API_KEY or ANTHROPIC_API_KEY and pass an llm_client.",
        }

    raw = llm_client.complete(
        INTEL_PROMPT.format(
            competitor_data=raw_data,
            your_product=your_product or "Not specified — provide your product for gap analysis",
        )
    )

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        return json.loads(match.group()) if match else {"raw": raw}
