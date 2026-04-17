# Lead Qualification Enricher (Uplizd) - Automated lead scoring and data enrichment for high-velocity sales

## Summary
The Lead Qualification Enricher is an intelligent Uplizd workflow that automates the process of researching, enriching, and scoring incoming leads. By leveraging AgentQL to extract web data and integrating with your CRM, this solution eliminates manual data entry, ensures your sales team focuses only on high-intent prospects, and maintains a clean, actionable pipeline.

---

## Demo
![Lead Qualification Enricher workflow dashboard showing automated data extraction and CRM scoring](image.png)
**Alt text (SEO-ready):** Lead Qualification Enricher Uplizd workflow, automated lead scoring, AgentQL web data extraction, CRM sales pipeline enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d1606025-0409-507b-aa4a-d2d62dd9a99c)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** `lead qualification`, `data enrichment`, `agentql`, `crm`, `salesops`, `pipeline velocity`, `ai workflow`  
This solution streamlines the lead-to-opportunity lifecycle by automating the research and qualification steps required for modern RevOps teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual research time and improve lead conversion rates.

- **Sales Development Representative (SDR)**
    - Instantly receives qualified lead profiles with enriched company data, allowing for more personalized outreach.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent lead scoring criteria across the entire pipeline, reducing data decay and improving reporting accuracy.
- **Account Executive (AE)**
    - Focuses time on high-intent prospects that have been pre-vetted by the AI, significantly increasing meeting-to-opportunity conversion.
- **Sales Manager**
    - Gains visibility into lead quality metrics and pipeline health without requiring manual audits of CRM records.

---

## Features
- **Automated Web Enrichment**
    - Uses AgentQL to scrape and parse relevant prospect information from company websites and public profiles in real-time.
- **Dynamic Lead Scoring**
    - Applies custom business logic to assign scores based on firmographic data, intent signals, and historical conversion patterns.
- **CRM Synchronization**
    - Automatically updates lead records in your CRM with enriched fields, ensuring a single source of truth for the entire sales organization.
- **Intelligent Triage**
    - Routes high-scoring leads directly to senior sales queues while flagging low-quality leads for automated nurturing sequences.
- **Real-time Pipeline Alerts**
    - Triggers notifications for newly qualified leads, ensuring the sales team can engage at the moment of peak interest.

---

## Use Cases
**Lead Research & Enrichment**
- Automatically populate missing job titles, company sizes, and industry tags from public web sources.
- Cross-reference lead contact details against professional networks to ensure data accuracy before outreach.

**Pipeline Qualification**
- Score incoming leads based on specific criteria like "Company Revenue" or "Tech Stack" to prioritize high-value targets.
- Filter out unqualified leads automatically to prevent sales teams from wasting cycles on low-probability prospects.

**Sales Operations Hygiene**
- Standardize lead formatting across multiple inbound channels to maintain a clean and searchable CRM database.
- Identify and flag duplicate lead entries for merging, preventing conflicting outreach from different sales reps.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Enricher template from the solution library.
3. Connect your preferred CRM and AgentQL credentials in the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data or URL to be processed.
- **Agent**: Analyzes the input, executes research logic, and determines qualification status.
- **Composio Toolset**: Executes the web extraction and CRM update commands.
- **Chat Output**: Returns the enriched lead profile and qualification score to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Qualify this lead: [URL/Email] and check for company size.`
- `Research the latest funding news for this prospect and update their CRM score.`
- `Enrich the following lead data and determine if they meet our ideal customer profile.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your qualification criteria.
- **Instruction Pattern:** Define the specific ICP (Ideal Customer Profile) attributes clearly.
- **Instruction Pattern:** Instruct the agent to prioritize accuracy over speed when scraping web data.
- **Instruction Pattern:** Define the scoring threshold (e.g., "Only mark as 'Qualified' if company size > 50 employees").

### 2) Composio Toolset Node
- **API Key:** Provide your valid AgentQL and CRM API keys.
- **Connection Scope:** Ensure the toolset has read/write permissions for your CRM's Lead/Contact objects.

### 3) Tool Availability
- **Web Scraper:** For extracting firmographic data via AgentQL.
- **CRM Connector:** For updating fields and status labels in your sales platform.
- **Data Validator:** For checking email formats and phone number validity.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](Account Intelligence Gatherer) — Automates deep-dive research on target accounts.
- [../account-research-assistant-by-zoominfo/README.md](Account Research Assistant) — Provides comprehensive firmographic data for enterprise prospecting.
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) — Keeps lead data consistent across multiple platforms and tools.
- [../whats-app-lead-qualifier-by-wati/README.md](WhatsApp Lead Qualifier) — Qualifies inbound leads directly through messaging channels.
