# Local Business Lead Finder (Uplizd) - Automated Prospecting and Qualification

## Summary
The Local Business Lead Finder (Uplizd) is an automated AI workflow designed to streamline the discovery and qualification of local business prospects. By leveraging real-time search data, this solution helps sales and marketing teams identify high-intent leads, verify business details, and populate their CRM pipelines with accurate, actionable intelligence, significantly reducing manual research time.

---

## Demo
![Local Business Lead Finder workflow showing search, qualification, and CRM sync nodes](image.png)
**Alt text (SEO-ready):** Local Business Lead Finder Uplizd workflow showing automated lead discovery, Zenserp integration, and CRM qualification pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4c466b37-e6ed-508e-88c4-9d682617cbd8)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead generation, local business, zenserp, prospecting, crm, sales intelligence, ai workflow, composio
- This solution bridges the gap between raw search data and structured sales opportunities, ensuring your team focuses only on qualified leads.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outbound efforts without increasing headcount.

- **Sales Development Rep (SDR)**
    - Automates the tedious process of finding and verifying local business contact information.
- **Marketing Manager**
    - Ensures a steady stream of high-quality, localized leads for regional campaigns.
- **Small Business Owner**
    - Identifies potential B2B partners or local service providers to expand market reach.
- **RevOps Specialist**
    - Maintains data hygiene by ensuring all discovered leads meet specific qualification criteria before entering the CRM.

---

## Features
- **Automated Prospect Discovery**
    - Uses Zenserp to perform targeted local searches based on industry, location, and business intent.
- **Intelligent Qualification**
    - The Agent node evaluates search results against predefined criteria to filter out irrelevant or low-quality prospects.
- **Real-time Data Enrichment**
    - Fetches live business details including contact information, ratings, and operational status.
- **Seamless CRM Integration**
    - Automatically pushes qualified leads into your CRM via the Composio Toolset to ensure immediate follow-up.
- **Customizable Search Parameters**
    - Easily adjust search queries and qualification logic to pivot between different target markets or industries.

---

## Use Cases
**Outbound Sales Prospecting**
- Automatically generate a list of local businesses in a specific niche for cold outreach campaigns.
- Filter prospects by geographic radius and business rating to ensure high-quality lead lists.

**Market Expansion Research**
- Identify key competitors and potential partners in new geographic territories.
- Aggregate business data to analyze market saturation and identify untapped service areas.

**Lead Pipeline Hygiene**
- Regularly audit local business databases to remove closed or inactive entities.
- Update existing CRM records with the latest contact information retrieved from search results.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Local Business Lead Finder template file provided in this repository.
3. Configure your API credentials for Zenserp and your target CRM within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target industry, location, and qualification criteria from the user.
- **Agent**: Processes the search request, formulates queries, and evaluates business data against your criteria.
- **Composio Toolset**: Executes Zenserp search commands and performs write operations to your CRM.
- **Chat Output**: Returns a summary of discovered leads and confirms their successful addition to the CRM.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Find 5 top-rated plumbing businesses in Austin, Texas and add them to my CRM.`
- `Search for digital marketing agencies in London and qualify them based on a 4.5+ star rating.`
- `Identify local coffee shops in Seattle that have not been contacted in the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your research assistant, interpreting search intent and applying business logic.
- **Instruction Pattern:**
    - "Act as a professional sales researcher; prioritize accuracy and business relevance."
    - "Use the provided search tools to find businesses matching the user's location and industry."
    - "Only pass businesses to the CRM if they meet the minimum rating and contact availability requirements."

### 2) Composio Toolset Node
- **API Key:** Ensure your Zenserp and CRM API keys are active within the Composio dashboard.
- **Connection Scope:** Grant the toolset read access to search engines and write access to your CRM's lead or account objects.

### 3) Tool Availability
- **Zenserp API**: For performing localized search queries and extracting business metadata.
- **CRM Connector**: For creating new lead records and updating existing account fields.
- **Data Parser**: For cleaning and formatting contact information before storage.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich your discovered leads with deep firmographic data.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive into specific accounts to prepare for high-stakes outreach.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your local business leads synchronized across multiple platforms.
