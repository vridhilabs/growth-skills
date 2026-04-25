# 📢 Skill: Social Content Engine

Turn one signal or idea into platform-native content for LinkedIn, X (Twitter), and Email. No copy-paste — each piece is natively formatted for its platform.

## Input
```json
{
  "signal": "string (topic, URL, insight, or raw idea)",
  "persona": "string (founder | operator | analyst | builder)",
  "target_audience": "string (who you're writing for)",
  "platforms": ["linkedin", "x", "email"]
}
```

## Process
1. Analyze the signal for core insight, hook potential, and audience relevance
2. Extract the strongest angle (data, story, opinion, or framework)
3. Generate platform-native content per platform:
   - **LinkedIn**: 3-paragraph format, line breaks, no hashtag spam
   - **X (Twitter)**: Single punchy tweet OR 5-tweet thread opener
   - **Email**: Subject line + 3-paragraph newsletter snippet with CTA
4. Apply compression rules (drop period, land on noun, lowercase register)

## Output
```json
{
  "core_insight": "string",
  "best_hook": "string",
  "linkedin": {
    "post": "string",
    "first_comment": "string"
  },
  "x_twitter": {
    "single_tweet": "string",
    "thread_opener": "string",
    "thread": ["string x5"]
  },
  "email": {
    "subject": "string",
    "preview_text": "string",
    "body": "string"
  }
}
```

## Usage
```bash
growth-skills run --skill social_content_engine --input signal.json
```

## Value
- 1 signal → 3 platform-native pieces in under 60 seconds
- Built-in persona engine — content matches your voice, not generic AI slop
- Compression rules applied automatically for maximum engagement
