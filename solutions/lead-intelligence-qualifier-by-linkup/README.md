# Lead Intelligence Qualifier (Uplizd) - Automate inbound lead research and scoring

## Summary
The Lead Intelligence Qualifier (Uplizd) is an automated AI workflow designed to streamline the sales pipeline by instantly researching and scoring inbound leads. By leveraging real-time data enrichment and intelligent analysis, this solution provides sales teams with a single source of truth for lead priority, significantly increasing pipeline velocity and ensuring that high-value prospects receive immediate attention.

---

## Demo
![Lead Intelligence Qualifier workflow showing automated data enrichment and scoring nodes](image.png)
**Alt text (SEO-ready):** Lead Intelligence Qualifier workflow in Uplizd for automated sales lead research, scoring, and CRM data enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2856b7b5-8ab9-58b1-8e8c-0e9910330cdb)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead scoring, sales intelligence, data enrichment, pipeline, salesops, composio, ai workflow
- This solution bridges the gap between raw inbound interest and actionable sales intelligence by automating the qualification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual research and prioritize high-intent prospects.

- **Sales Development Representative (SDR)**
    - Focuses energy on high-scoring leads that are ready for immediate outreach.
- **Revenue Operations Manager**
    - Maintains clean, enriched CRM data without manual administrative overhead.
- **Account Executive**
    - Receives pre-qualified lead dossiers to personalize discovery calls effectively.
- **Sales Manager**
    - Gains visibility into lead quality trends to optimize marketing and sales alignment.

---

## Features
- **Automated Lead Enrichment**
    - Fetches real-time firmographic and contact data to build a comprehensive lead profile.
- **Intelligent Scoring Engine**
    - Applies custom logic to rank leads based on fit, intent, and historical conversion data.
- **CRM Integration**
    - Seamlessly pushes qualified lead data back into your CRM using the Composio Toolset.
- **Real-time Alerting**
    - Triggers notifications for high-priority leads to ensure rapid response times.
- **Standardized Data Hygiene**
    - Normalizes incoming lead information to ensure consistency across your sales stack.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads from target accounts for immediate BDR follow-up.
- Rank inbound inquiries based on company size and industry fit.

**Sales Pipeline Acceleration**
- Reduce lead response time by automating the initial research phase.
- Populate CRM custom fields with enriched data to shorten the discovery process.

**Data Hygiene & Enrichment**
- Fill missing contact details automatically to ensure accurate lead routing.
- Standardize lead source and intent data for better reporting and analytics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Intelligence Qualifier template from the solution library.
3. Connect your preferred CRM and data enrichment tools via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data (email, domain, or name).
- **Agent**: Analyzes the lead, performs research, and calculates the qualification score.
- **Composio Toolset**: Executes data lookups and updates the CRM records.
- **Chat Output**: Returns the final lead dossier and qualification summary.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Qualify this lead: contact@example-company.com`
- `Research and score the lead from domain: tech-startup.io`
- `Analyze the following lead data and update the CRM: John Doe, Acme Corp`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a sales research analyst.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "Act as a sales intelligence expert. Research the provided lead, assess their fit based on the company profile, and assign a score from 1-10."
- Ensure the agent is configured to output structured JSON for CRM updates.

### 2) Composio Toolset Node
- Provide your API key to enable secure connections to your CRM and enrichment providers.
- Set the scope to allow read/write access to lead and account objects.

### 3) Tool Availability
- **CRM Connectors**: Salesforce, HubSpot, or Dynamics 365.
- **Enrichment APIs**: Clearbit, ZoomInfo, or Dropcontact.
- **Search Tools**: Web search capabilities for latest company news and signals.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate the collection of firmographic data for target accounts.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research and insights for enterprise-level prospecting.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score sales opportunities within your pipeline.
