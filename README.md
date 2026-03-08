# 📈 Growth Skills

An open-source collection of high-engagement templates for X (Twitter), LinkedIn, Email, and DM outreach. Designed to be used as a standalone CLI tool or integrated into AI-driven content pipelines.

## 🚀 Overview

Growth Skills is a curated library of "proven" content structures and outreach frameworks. It eliminates the "blank page" problem for founders, builders, and operators.

### 🪝 Social Hooks

#### X (Twitter)
- **Binary Choice**: Direct instruction, optimal path with metric, and a sharp binary conclusion.
- **Upgrade Contrast**: Negative outcome vs. positive upgrade with stats.
- **Unpopular Opinion**: Bold contrarian take with its specific implication.
- **Thread Opener (Stat)**: Hook using a shocking statistic to lead into a thread.

#### LinkedIn
- **Tactical Deep-dive**: Paragraph-based industry analysis with bulleted takeaways.

#### Minimalist Frames
- **Strategic Reframe**: Flip current state into new perspective (e.g., 'overthinkers are underpaid').
- **Parallel Declaration**: Identical sentence structures to contrast pros vs. amateurs.
- **Paradox Reveal**: Counter-intuitive truths that reveal deep logic.
- **Math Quantifier**: Using simple math symbols (+, -, x, /) to quantify abstract ideas.
- **Conditional Reveal**: Surprising 'If/Then' setups that challenge assumptions.

### 📐 Rules of Compression (Meta-Style)
*Extracted from analyzing high-performance signal frames.*

1. **Drop the Period**: Bare-word endings get ~20% more engagement.
2. **Land on a Noun**: Final word should be a thing, not an action.
3. **Lowercase as Register**: Use lowercase for a "thinking out loud" vibe.
4. **Use Colons as Pivots**: Keeps both sides short (2-4 words).
5. **No Clutter**: No tribe-signaling, no "diary" entries, and no cliches.

### ✉️ Outreach Frameworks

#### Email (Cold Outreach & Newsletter)
- **Direct Pain Point**: Solve a specific problem you spotted for them.
- **Pattern Match**: Leverage a competitor's success to pique interest.
- **Newsletter Bridge**: High-CTR teaser for long-form content.

#### DM (Direct Messages)
- **Low Friction Curiosity**: Non-salesy, high-response intent start for LinkedIn.
- **Founder Alignment**: Direct intro targeting other founders on X.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/vridhilabs/growth-skills.git
cd growth-skills

# Install the CLI tool locally
pip install -e .
```

## 📖 Usage

### List all templates
```bash
growth-skills list
```

### Get a specific template by ID
```bash
growth-skills get --id binary_choice --category social_media_templates
```

### Get a random DM template
```bash
growth-skills random --category dm_templates
```

## 🧩 Structure

- `src/growth_skills/templates/templates.json`: The core library of templates.
- `src/growth_skills/cli.py`: The CLI entry point.

## 🤝 Contributing

We are actively looking for more patterns! If you have a specific structure that consistently drives results:
1. Fork this repo.
2. Add your framework to `templates.json`.
3. Submit a PR.

## 📄 License

MIT License. See `LICENSE` for details.
