# Territory Expansion Scout (Uplizd) - Identify and prioritize high-value prospects in your territory

## Summary
The Territory Expansion Scout (Uplizd) is an intelligent AI workflow designed to automate the identification and prioritization of new business prospects within specific geographic or market territories. By leveraging real-time data from ZoomInfo, this solution enables sales and operations teams to maintain a high-velocity pipeline, ensuring that outreach efforts are focused on accounts that align perfectly with your Ideal Customer Profile (ICP).

---

## Demo
![Territory Expansion Scout workflow showing ZoomInfo data integration and prospect scoring](image.png)
**Alt text (SEO-ready):** Territory Expansion Scout workflow in Uplizd, demonstrating automated prospect identification, ZoomInfo CRM data integration, and sales pipeline prioritization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cc3b5da4-4d8b-531c-972e-b2b5516abc27)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, zoominfo, sales prospecting, territory management, pipeline, lead generation, composio, ai workflow  
This solution streamlines territory planning by bridging the gap between raw market data and actionable sales intelligence.

---

## Who is this for?
This solution is built for revenue-focused teams looking to scale their outreach efforts with precision.

- **Sales Managers**
    - Gain granular visibility into untapped market segments and prioritize high-potential territories for their teams.
- **Account Executives**
    - Spend less time researching and more time engaging with qualified prospects that match their specific territory goals.
- **RevOps Specialists**
    - Standardize the prospect identification process across the organization to ensure consistent data hygiene and pipeline quality.
- **Business Development Representatives**
    - Receive automated, high-intent lead lists directly from ZoomInfo to accelerate daily outbound prospecting.

---

## Features
- **Automated Prospect Discovery**
    - Leverages the Composio Toolset to query ZoomInfo for companies matching specific industry, size, and revenue criteria.
- **ICP-Based Scoring**
    - Automatically filters and ranks prospects based on your predefined Ideal Customer Profile parameters.
- **Real-Time CRM Sync**
    - Pushes qualified prospect data directly into your CRM, ensuring your sales team has the latest intelligence at their fingertips.
- **Geographic Territory Mapping**
    - Segments data by region or zip code to ensure sales reps are focused on their assigned operational territories.
- **Intelligent Outreach Context**
    - Generates personalized research summaries for each prospect, providing context for more effective initial outreach.

---

## Use Cases
**Territory Planning**
- Automatically identify all companies in a new expansion region that meet specific revenue thresholds.
- Refresh territory lists monthly to capture new business registrations and emerging market players.

**Lead Qualification**
- Cross-reference incoming leads against ZoomInfo data to verify firmographic fit before assigning to an AE.
- Score prospects based on recent funding rounds or leadership changes to prioritize high-intent outreach.

**Pipeline Velocity**
- Populate empty sales territories with high-quality leads to ensure consistent activity levels for the sales team.
- Automate the research phase of the sales cycle, reducing the time from lead identification to first contact.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Territory Expansion Scout template from the marketplace.
3. Connect your ZoomInfo and CRM credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Define the target territory, industry focus, and company size constraints.
- **Agent**: Processes the request and orchestrates the search logic based on your ICP.
- **Composio Toolset**: Executes real-time queries against ZoomInfo to fetch and validate prospect data.
- **Chat Output**: Displays the prioritized prospect list with key firmographic details and contact insights.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Find 10 software companies in the Pacific Northwest with over 50 employees that match our ICP.`
- `List all healthcare providers in the Texas territory that have recently expanded their operations.`
- `Identify high-growth manufacturing prospects in the Midwest region for our Q3 outreach campaign.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your strategic sales researcher, interpreting territory parameters and translating them into precise search queries.
- **Recommended instruction pattern:**
    - Act as a senior sales operations analyst specializing in territory expansion.
    - Prioritize data accuracy by cross-referencing ZoomInfo firmographics against defined ICP criteria.
    - Format output as a prioritized table including company name, revenue, and key decision-maker insights.

### 2) Composio Toolset Node
- **API Key**: Ensure your ZoomInfo API key is active within the Composio dashboard.
- **Connection Scope**: Grant read-only access to company search and contact intelligence endpoints.

### 3) Tool Availability
- **ZoomInfo Search**: Retrieve firmographic data and contact details.
- **CRM Connector**: Sync qualified leads into your CRM pipeline.
- **Data Validation**: Cross-check prospect data against existing CRM records to prevent duplicates.

---

## Related Solutions
- [Account Research Assistant (ZoomInfo)](../account-research-assistant-by-zoominfo/README.md) — Deep-dive research and intelligence gathering for specific target accounts.
- [Account Intelligence Gatherer (Dropcontact)](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data and verify contact information for better outreach.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track your sales pipeline stages and follow-up cadence.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize prospect and account data across multiple platforms to maintain a single source of truth.
