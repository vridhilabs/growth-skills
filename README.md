# growth-skills

A collection of AI-native GTM skills for founders, operators, and builders. These are self-contained prompt-engine modules designed to be plugged directly into your AI agent (Claude, GPT, RaGa, etc.).

---

## How to Use These Skills

Since we are in the early days, there are three ways to "fetch" a skill:

### 1. The Quickest Way (Copy-Paste)
Every skill is a single `SKILL.md` file. Simply open the folder for the skill you want, copy the content of `SKILL.md`, and paste it into your agent's system instructions or knowledge base.

### 2. For Local Agents (Clone)
If you use a local AI IDE or agent (like RaGa or Claude Code), clone this repo and point it to the skill folder.
```bash
git clone https://github.com/vridhilabs/growth-skills.git
```

### 3. Automated Download (Coming Soon)
We are building a dedicated CLI to fetch these directly. For now, you can use `curl` to grab any skill:
```bash
# Example: Download the 'score-lead' skill to your current directory
curl -L https://raw.githubusercontent.com/vridhilabs/growth-skills/main/score-lead/SKILL.md > score-lead.md
```

---

## The GTM Skills Library

### 🔱 Acquisition
**[score-lead](score-lead/)** — Score any inbound lead against your ICP. Get a 0–100 score, fit rating, and CRM tags.
**[write-cold-email](write-cold-email/)** — Turn a prospect + hook into 3 email variations + a follow-up sequence.

### 🔱 Strategy
**[gtm-roadmap](gtm-roadmap/)** — Turn a job description into a 3-month Founder-Operator strategy with tools and KPIs.
**[competitor-map](competitor-map/)** — Map a competitor's GTM from their public footprint + get a sales battle card.

### 🔱 Content
**[content-engine](content-engine/)** — 1 signal → LinkedIn post + X thread + Email snippet. Platform-native and voice-matched.

---

## CRM Integration

These skills connect natively to **[Twenty CRM](https://github.com/twentyhq/twenty)** (Open-Source/Self-Hosted).  
See the [Twenty CRM Setup Guide](crm/twenty_crm_setup.md) to build your own autonomous GTM pipeline.

---

*Built by [Vridhi Labs](https://vridhilabs.ai)*
