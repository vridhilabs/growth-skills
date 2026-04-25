# 🗺️ Skill: JD to GTM Roadmap

Convert any job description into a Founder-Operator GTM strategy. Instantly understand what a company needs and how to position yourself or your solution.

## Input
```json
{
  "job_description": "string (raw JD text or URL)",
  "context": "string (optional — your product/service being positioned)"
}
```

## Process
1. Extract role signals: mission, responsibilities, tools, KPIs, seniority
2. Cluster into 5-7 functional workstreams (paid, content, CRM, analytics, etc.)
3. Identify gaps, hidden expectations, and implied tech stack
4. Generate phased 3-month roadmap with priorities and success metrics
5. Map to a tool stack recommendation (open-source first)

## Output
```json
{
  "role_summary": "string",
  "workstreams": [
    {
      "name": "string",
      "objective": "string",
      "tools": ["string"],
      "kpis": ["string"],
      "month_1_priority": "string"
    }
  ],
  "roadmap": {
    "month_1": ["string"],
    "month_2": ["string"],
    "month_3_plus": ["string"]
  },
  "hidden_expectations": ["string"],
  "tool_stack": {
    "crm": "string",
    "analytics": "string",
    "automation": "string",
    "content": "string"
  },
  "positioning_angle": "string"
}
```

## Usage
```bash
growth-skills run --skill jd_to_gtm_roadmap --input jd.json
```

## Value
- Instantly decode what a company actually needs (beyond the job post)
- Position your product or yourself against their real gaps
- Founder-Operator style: systems + metrics first, not just tasks
