# Lead Qualification Assistant (Uplizd) - Automated lead scoring and nurturing workflow

## Summary
The Lead Qualification Assistant is an intelligent Uplizd workflow designed to streamline the sales funnel by automatically evaluating incoming leads and initiating personalized engagement. By leveraging the Composio Toolset to interface with your CRM, this solution ensures that high-intent prospects are prioritized for sales outreach while maintaining consistent data hygiene, ultimately increasing pipeline velocity and conversion rates for revenue teams.

---

## Demo
![Lead Qualification Assistant workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Qualification Assistant workflow for Uplizd, featuring automated CRM lead scoring, sales pipeline integration, and AI-driven prospect nurturing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6214b144-21d7-5cd2-a47b-f48e7460f55c)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead qualification, sales pipeline, lead scoring, ai workflow, composio, revenue operations, sales efficiency
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the qualification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual administrative overhead and improve lead response times.

- **Sales Development Representative (SDR)**
    - Focuses on high-value prospects by automating the initial qualification and data enrichment steps.
- **Revenue Operations Manager**
    - Ensures data consistency and pipeline hygiene by enforcing standardized qualification criteria across all incoming leads.
- **Account Executive (AE)**
    - Receives pre-qualified opportunities directly in the CRM, allowing for faster discovery calls and improved closing rates.
- **Marketing Operations Specialist**
    - Bridges the gap between lead generation campaigns and sales readiness by tracking lead engagement signals in real-time.

---

## Features
- **Automated Lead Scoring**
    - Dynamically assigns scores to incoming leads based on predefined criteria and interaction history.
- **CRM Integration**
    - Seamlessly syncs qualification status and notes back to your CRM using the Composio Toolset.
- **Intelligent Nurturing**
    - Triggers personalized follow-up actions based on the lead's qualification tier and industry profile.
- **Real-time Data Enrichment**
    - Pulls external company and contact data to provide a comprehensive view of the prospect before human intervention.
- **Pipeline Hygiene**
    - Automatically flags incomplete or duplicate lead records to maintain a clean and actionable sales database.

---

## Use Cases
**Lead Prioritization**
- Automatically route "Hot" leads to the appropriate sales queue based on real-time scoring.
- Flag stalled leads for re-engagement campaigns when qualification criteria are not met within a set window.

**CRM Data Enrichment**
- Populate missing job title or company size fields using external data providers via the Composio Toolset.
- Standardize lead source tagging to ensure accurate attribution reporting in your CRM dashboard.

**Sales Outreach Automation**
- Draft personalized follow-up emails for qualified leads based on their specific pain points identified during the chat.
- Schedule discovery meetings directly in the CRM calendar for leads that cross the "Ready to Buy" threshold.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the solution JSON file provided in this repository.
3. Configure your environment variables for your CRM and AI provider.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or manual triggers from your sales team.
- **Agent**: Processes lead information, applies scoring logic, and determines the next best action.
- **Composio Toolset**: Executes CRM updates, performs data lookups, and manages external API connections.
- **Chat Output**: Delivers the qualification summary and recommended follow-up steps to the user.

### 3) Run the Flow
Open the Playground and test the workflow with the following prompts:
- `Qualify the lead from Acme Corp: John Doe, interested in enterprise tier.`
- `Check if the lead 'Jane Smith' exists in Salesforce and update her status to 'Qualified'.`
- `Score the latest batch of leads from the website and notify the sales team of any high-intent prospects.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for lead assessment.
- **System Prompt:** Act as a professional sales assistant that evaluates leads based on provided scoring rubrics.
- **Tone:** Professional, objective, and action-oriented.
- **Constraint:** Only update CRM fields when the lead meets the minimum qualification threshold.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key in the node settings.
- **Connection Scope:** Ensure the CRM integration (e.g., Salesforce, HubSpot) has read/write permissions for Leads and Contacts.

### 3) Tool Availability
- **CRM Read/Write:** Access to lead objects, contact records, and opportunity stages.
- **Data Enrichment:** Capability to query external databases for company intelligence.
- **Calendar Management:** Ability to check availability and book meetings for qualified leads.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich prospect data to improve qualification accuracy.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage the lifecycle of qualified opportunities through to closing.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure lead data remains consistent across multiple platforms.
