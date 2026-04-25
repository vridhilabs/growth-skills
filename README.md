# growth-skills

A collection of GTM skills for founders, operators, and builders. Add them to your AI agent and run them on demand.

These skills cover the full go-to-market motion — from scoring leads to writing cold emails to mapping competitors.

---

## Skills

### Acquisition

**score-lead** — Score any inbound lead against your ICP. Get a 0–100 score, ICP fit, intent level, next action, and CRM tags.

```
npx skills@latest add vridhilabs/growth-skills/score-lead
```

**write-cold-email** — Turn a prospect + one hook into 3 email variations (pain, curiosity, proof) + a 2-step follow-up sequence.

```
npx skills@latest add vridhilabs/growth-skills/write-cold-email
```

---

### Strategy

**gtm-roadmap** — Paste a job description and get a Founder-Operator GTM strategy: workstreams, 3-month phased roadmap, tool stack, and KPIs.

```
npx skills@latest add vridhilabs/growth-skills/gtm-roadmap
```

**competitor-map** — Map a competitor's GTM from their public footprint. Get their positioning, growth channels, hiring signals, gaps, and a counter-messaging battle card.

```
npx skills@latest add vridhilabs/growth-skills/competitor-map
```

---

### Content

**content-engine** — One signal → LinkedIn post + X thread + Email snippet. Platform-native. Voice-matched. Compression rules applied.

```
npx skills@latest add vridhilabs/growth-skills/content-engine
```

---

## CRM Integration

These skills are designed to connect to **[Twenty CRM](https://github.com/twentyhq/twenty)** — free, open-source, self-hosted.

`score-lead` output maps directly to Twenty CRM opportunity fields. See [`crm/twenty_crm_setup.md`](crm/twenty_crm_setup.md) for the full pipeline setup.

---

## Templates

The original template library (social hooks, outreach frameworks, compression rules) lives in [`src/growth_skills/templates/`](src/growth_skills/templates/).

```bash
pip install -e .
growth-skills list
growth-skills get --id binary_choice --category social_media_templates
```

---

## Contributing

Each skill is a single `SKILL.md` file inside a folder at the root of this repo.

To add a skill:
1. Create a folder with a short, verb-first name (e.g. `score-lead`, `write-brief`)
2. Add a `SKILL.md` — explain what to provide, what you get back, and show an example
3. Submit a PR

---

*Built by [Vridhi Labs](https://github.com/vridhilabs)*
