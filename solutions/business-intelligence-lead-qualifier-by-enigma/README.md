# Business Intelligence Lead Qualifier (Uplizd) - Automate lead enrichment and qualification with real-time business data

## Summary
The Business Intelligence Lead Qualifier is an automated Uplizd AI workflow that streamlines your sales pipeline by instantly enriching raw lead data with deep business intelligence. By leveraging the Composio Toolset to query external data providers, this solution identifies high-value prospects, scores their potential, and ensures your team focuses only on qualified opportunities, significantly increasing pipeline velocity and data hygiene.

---

## Demo
![Business Intelligence Lead Qualifier workflow showing data enrichment, scoring, and CRM update nodes](image.png)
**Alt text (SEO-ready):** Business Intelligence Lead Qualifier workflow for Uplizd, featuring automated lead enrichment, sales pipeline qualification, and CRM data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ede8782b-47b5-5247-8cfc-df4de112b694)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead qualification, business intelligence, data enrichment, sales pipeline, lead scoring, composio, ai workflow
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the research process.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to eliminate manual research and prioritize high-intent prospects.

- **Sales Development Representative (SDR)**
    - Reduces time spent on manual prospect research and lead vetting.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent lead scoring criteria and high-quality data across the CRM.
- **Account Executive (AE)**
    - Increases win rates by focusing energy on pre-qualified, high-intent accounts.
- **Growth Marketer**
    - Improves conversion rates by passing only enriched, validated leads to the sales team.

---

## Features
- **Automated Lead Enrichment**
    - Instantly pulls firmographic and technographic data to build a complete profile for every incoming lead.
- **Intelligent Lead Scoring**
    - Applies custom business logic to rank leads based on company size, industry fit, and recent activity.
- **CRM Integration**
    - Seamlessly pushes enriched data and qualification status back into your CRM using the Composio Toolset.
- **Real-time Data Validation**
    - Cross-references lead information against live business intelligence databases to ensure accuracy.
- **Pipeline Velocity Optimization**
    - Accelerates the handoff from marketing to sales by removing manual qualification bottlenecks.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads that match your Ideal Customer Profile (ICP) for immediate outreach.
- Deprioritize or archive leads that fail to meet minimum business intelligence thresholds.

**Data Hygiene & Enrichment**
- Populate missing fields like company revenue, employee count, and industry tags automatically.
- Standardize company naming conventions and contact details to maintain a clean CRM database.

**Sales Handoff Automation**
- Trigger notifications to the assigned AE only when a lead reaches a specific qualification score.
- Create tasks in your CRM for follow-up actions based on the enriched lead data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Business Intelligence Lead Qualifier template from the marketplace.
3. Connect your CRM and Business Intelligence API credentials via the Composio Toolset.
4. Ensure nodes are correctly mapped from Chat Input through the Agent to the final Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data (email, company domain, or name).
- **Agent**: Processes the data, executes search queries, and performs qualification logic.
- **Composio Toolset**: Connects to external BI providers and your CRM to fetch and write data.
- **Chat Output**: Returns the enriched lead profile and qualification status to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Qualify this lead: acme-corp.com`
- `Enrich the profile for john.doe@tech-startup.io and check if they match our ICP`
- `Fetch business intelligence for the latest leads in the queue and update their CRM scores`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets raw data and applies your qualification rules.
- **Instruction Pattern:**
    - "Analyze the provided company domain to extract firmographic data."
    - "Compare the extracted data against the defined ICP criteria."
    - "Format the final output as a structured summary including the qualification score."

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure tool execution.
- **Connection Scope:** Ensure the toolset has read/write permissions for your specific CRM and BI data providers.

### 3) Tool Availability
- **CRM Connector:** For reading lead data and updating records.
- **BI Search Tool:** For fetching real-time company intelligence.
- **Data Formatter:** For cleaning and standardizing input strings.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Deep-dive research for target accounts.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Automated prospecting and contact discovery.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Monitor and score active sales opportunities.
