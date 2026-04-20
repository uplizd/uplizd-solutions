# Talent Acquisition Scout (Uplizd) - Automated high-growth company identification for passive recruiting

## Summary
The Talent Acquisition Scout is an intelligent Uplizd workflow designed to streamline the identification of high-growth companies for passive recruiting pipelines. By leveraging real-time data from Crustdata, this solution enables talent acquisition teams to pinpoint organizations experiencing rapid headcount expansion, ensuring recruiters reach out to top-tier talent before competitors do.

---

## Demo
![Talent Acquisition Scout workflow interface showing Crustdata integration and candidate pipeline generation](image.png)
**Alt text (SEO-ready):** Talent Acquisition Scout Uplizd workflow for passive recruiting, high-growth company identification, and Crustdata integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4913f293-006d-59a9-8a28-e2e64e0873a0)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** recruiting, talent acquisition, crustdata, pipeline, growth intelligence, hiring, composio, ai workflow
- This solution bridges the gap between market intelligence and talent sourcing by automating the discovery of high-growth companies.

---

## Who is this for?
This workflow is built for talent teams looking to gain a competitive edge in the hiring market.

- **Technical Recruiter**
    - Proactively identify companies with aggressive engineering headcount growth to target passive candidates.
- **Head of Talent**
    - Build data-driven sourcing strategies that prioritize companies with high funding or rapid scaling signals.
- **Sourcing Specialist**
    - Reduce manual research time by automating the discovery of target organizations based on real-time growth metrics.
- **Growth Operations Manager**
    - Align recruiting efforts with market trends by integrating external growth data directly into the talent pipeline.

---

## Features
- **Real-time Growth Signals**
    - Automatically pulls headcount expansion data from Crustdata to identify companies in hyper-growth phases.
- **Automated Prospecting**
    - Uses the Composio Toolset to query company data and filter targets based on specific industry or size criteria.
- **Intelligent Filtering**
    - Applies custom logic to rank companies based on growth velocity, ensuring recruiters focus on the most relevant targets.
- **Seamless CRM Integration**
    - Syncs identified target companies directly into your recruiting workflow or CRM for immediate outreach.
- **Dynamic Reporting**
    - Generates summarized insights on company growth trends, providing context for personalized candidate outreach.

---

## Use Cases
**Targeted Sourcing**
- Identify companies that have recently secured Series B funding and are likely to begin aggressive hiring.
- Filter target organizations by specific technical stacks or industry verticals to match your open roles.

**Competitive Intelligence**
- Monitor headcount shifts in competitor organizations to anticipate potential talent churn.
- Analyze growth patterns over a 90-day window to prioritize companies with sustained momentum.

**Pipeline Velocity**
- Automate the daily discovery of new leads, feeding them directly into your sourcing queue.
- Reduce time-to-market for new roles by having a pre-vetted list of high-growth companies ready for outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Import the workflow into your workspace.
3. Connect your Crustdata API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** through the **Agent** to the **Composio Toolset** and finally the **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your search criteria (e.g., "Find high-growth SaaS companies in Berlin").
*   **Agent**: Processes the request and determines the necessary data points to fetch.
*   **Composio Toolset**: Executes the Crustdata API calls to retrieve real-time company growth metrics.
*   **Chat Output**: Delivers a structured list of target companies with growth insights.

### 3) Run the Flow
Use the Playground to test your sourcing queries:
- `Find all fintech companies with >20% headcount growth in the last quarter.`
- `List high-growth startups in the AI space that have expanded their engineering team recently.`
- `Identify companies with rapid growth signals in the healthcare sector for potential passive candidate outreach.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your research assistant, interpreting natural language queries and mapping them to API parameters.
- Focus on identifying growth-related keywords in user prompts.
- Prioritize accuracy when filtering company data from Crustdata.
- Maintain a professional tone when summarizing company growth insights for the recruiter.

### 2) Composio Toolset Node
- Requires a valid Crustdata API key to access company headcount and growth data.
- Ensure the connection scope includes read access to company growth and hiring metrics.

### 3) Tool Availability
- **Crustdata Search**: For querying company growth and headcount data.
- **Data Filter Utility**: For sorting and ranking companies based on user-defined growth thresholds.
- **CRM Connector**: For pushing identified companies into your existing talent management system.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich your target company data with contact-level insights.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research for specific target accounts.
- [Account Expansion Identifier](../account-expansion-identifier-by-crustdata/README.md) - Track company growth signals for sales and expansion opportunities.
