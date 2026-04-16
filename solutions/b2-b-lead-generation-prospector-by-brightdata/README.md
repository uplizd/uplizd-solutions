# B2B Lead Generation Prospector (Uplizd) - Automated lead discovery and qualification pipeline

## Summary
The B2B Lead Generation Prospector is an intelligent Uplizd workflow designed to automate the identification, extraction, and qualification of high-value business leads. By leveraging the Composio Toolset to connect with external data providers, this solution enables sales teams to maintain a consistent pipeline velocity, ensuring that only high-intent prospects reach the CRM, thereby improving data hygiene and reducing manual prospecting overhead.

---

## Demo
![B2B Lead Generation Prospector workflow interface showing lead extraction and qualification nodes](image.png)
**Alt text (SEO-ready):** B2B Lead Generation Prospector Uplizd workflow for automated lead discovery, sales pipeline qualification, and data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMiAxMnYxMGgyMFYxMkwxMiAyem0wIDJsOCA4djZIMDR2LTZsOC04eiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/aafd8b00-2e75-5f7c-8b72-c8949185fede)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** b2b, lead generation, sales prospecting, data enrichment, crm, pipeline, salesops, composio
- This solution streamlines the top-of-funnel sales process by automating lead research and qualification workflows.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach efforts without increasing manual administrative tasks.

- **Sales Development Representative (SDR)**
    - Accelerates daily lead list building and reduces time spent on manual research.
- **Growth Marketer**
    - Ensures a steady flow of qualified prospects into the CRM for targeted campaigns.
- **Sales Operations Manager**
    - Standardizes lead qualification criteria across the team to maintain high data hygiene.
- **Account Executive**
    - Focuses energy on high-intent leads that have already been vetted by the automated agent.

---

## Features
- **Automated Lead Discovery**
    - Scrapes and aggregates potential lead data from multiple web and database sources in real-time.
- **Intelligent Qualification**
    - Applies custom business logic to score prospects based on firmographic data and intent signals.
- **CRM Integration**
    - Automatically pushes qualified leads directly into your CRM, ensuring no opportunity is lost.
- **Data Enrichment**
    - Uses the Composio Toolset to fetch verified contact details and company insights for every prospect.
- **Pipeline Velocity Tracking**
    - Monitors the time from lead discovery to initial outreach, identifying bottlenecks in the sales process.

---

## Use Cases
**Outbound Sales Prospecting**
- Automatically identify companies that match your Ideal Customer Profile (ICP) from industry databases.
- Enrich lead profiles with verified email addresses and LinkedIn handles before adding them to a sequence.

**Lead Qualification & Scoring**
- Filter incoming leads based on specific criteria like company size, revenue, or recent funding rounds.
- Flag high-intent prospects for immediate follow-up by the sales team to increase conversion rates.

**CRM Data Hygiene**
- Prevent duplicate entries by checking existing records before creating new lead profiles in the CRM.
- Standardize lead formatting and field values to ensure consistent reporting across the sales organization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your required CRM and data provider accounts within the integration settings.
4. Ensure nodes are correctly mapped and all API keys are active before triggering the first run.

### 2) Setup the Nodes
- **Chat Input**: Receives the target industry or search parameters from the user.
- **Agent**: Processes search queries and executes qualification logic.
- **Composio Toolset**: Connects to data providers and CRM APIs to fetch and sync lead information.
- **Chat Output**: Returns a summary of discovered leads and their qualification status.

### 3) Run the Flow
Use the Playground to test your prospecting logic:
- `Find 10 leads in the SaaS industry with over 50 employees.`
- `Search for companies in the fintech space that recently raised Series B funding.`
- `Qualify leads from the current list based on high growth signals and add to Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary brain for interpreting search intent and applying qualification rules.
- Maintain a professional and analytical tone.
- Prioritize accuracy in data extraction over volume.
- Follow strict JSON formatting for CRM data synchronization.

### 2) Composio Toolset Node
- Requires valid API keys for your chosen CRM (e.g., Salesforce, HubSpot) and lead data providers.
- Ensure the connection scope includes read/write permissions for lead and account objects.

### 3) Tool Availability
- **Search Connectors**: Web search and industry-specific database access.
- **CRM Connectors**: Create, update, and search functionality for lead management.
- **Data Enrichment Tools**: Email verification and firmographic data retrieval.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate deep-dive research on target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your lead data consistent across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score opportunities as they move through the pipeline.
