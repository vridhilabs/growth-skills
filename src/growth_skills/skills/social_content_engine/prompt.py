"""
Social Content Engine — 1 signal → LinkedIn + X + Email in under 60 seconds.
Source: RaGa Sovereign OS / content_factory.py + fork_synthesizer.py + proactive_writer.py
"""

import json
from typing import Any

PERSONA_VOICES = {
    "founder": "Contrarian, direct, data-backed. You've built and failed. You share what works, not theory.",
    "operator": "Systems-first, practical, efficiency-obsessed. Every post has a framework or a process.",
    "analyst": "Metrics-driven, precise, pattern-spotting. You back every claim with data or a source.",
    "builder": "Curious, technical, show-don't-tell. You share what you're making and what you're learning.",
}

CONTENT_PROMPT = """
You are a world-class social media strategist and ghostwriter. Generate platform-native content from the signal below.

## Signal / Idea
{signal}

## Persona Voice
{persona_voice}

## Target Audience
{target_audience}

## Compression Rules (apply to all content)
1. Drop the Period: Bare-word endings get ~20% more engagement
2. Land on a Noun: Final word should be a thing, not an action
3. Lowercase as Register: Use lowercase for a "thinking out loud" vibe where appropriate
4. Use Colons as Pivots: Keep both sides short (2-4 words)
5. No Clutter: No tribe-signaling, no "diary" entries, no clichés

## Platform Formats

### LinkedIn
- Opening line: must create a pattern interrupt (no "I'm excited to share")
- Body: 3-5 short paragraphs with line breaks
- Closing: One clear takeaway or question, no hashtag spam (max 2 relevant tags)
- First comment: Additional value or source link

### X (Twitter)
- Single tweet: max 280 chars, punchy, opinionated
- Thread: 5 tweets. Tweet 1 = hook. Tweets 2-4 = insight. Tweet 5 = CTA

### Email
- Subject: 5-7 words, specific, no clickbait
- Preview text: 10-15 words that extend the subject
- Body: 3 paragraphs. Problem → Insight → CTA

Output as JSON:
{{
  "core_insight": "string (the key idea in one sentence)",
  "best_hook": "string (the strongest opening line)",
  "linkedin": {{
    "post": "string",
    "first_comment": "string"
  }},
  "x_twitter": {{
    "single_tweet": "string",
    "thread": ["tweet1", "tweet2", "tweet3", "tweet4", "tweet5"]
  }},
  "email": {{
    "subject": "string",
    "preview_text": "string",
    "body": "string"
  }}
}}
"""


def generate_content(
    signal: str,
    persona: str = "operator",
    target_audience: str = "founders and growth operators",
    platforms: list[str] | None = None,
    llm_client=None,
) -> dict[str, Any]:
    """
    Generate platform-native content from a single signal.
    
    Args:
        signal: Topic, URL, insight, or raw idea to write about
        persona: 'founder' | 'operator' | 'analyst' | 'builder'
        target_audience: Who you're writing for
        platforms: List of platforms to generate for (defaults to all)
        llm_client: LLM client with .complete(prompt) -> str
    
    Returns:
        Dict with LinkedIn post, X thread, and email newsletter snippet
    """
    platforms = platforms or ["linkedin", "x", "email"]
    persona_voice = PERSONA_VOICES.get(persona, PERSONA_VOICES["operator"])

    if llm_client is None:
        return {
            "error": "LLM client required. Provide an OpenAI or Anthropic client.",
            "signal": signal,
            "persona": persona,
        }

    raw = llm_client.complete(
        CONTENT_PROMPT.format(
            signal=signal,
            persona_voice=persona_voice,
            target_audience=target_audience,
        )
    )

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        result = json.loads(match.group()) if match else {"raw": raw}

    # Filter to requested platforms
    filtered = {
        "core_insight": result.get("core_insight"),
        "best_hook": result.get("best_hook"),
    }
    if "linkedin" in platforms:
        filtered["linkedin"] = result.get("linkedin")
    if "x" in platforms or "twitter" in platforms:
        filtered["x_twitter"] = result.get("x_twitter")
    if "email" in platforms:
        filtered["email"] = result.get("email")

    return filtered
