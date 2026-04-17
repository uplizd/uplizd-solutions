# Contact Enrichment Engine (Uplizd) - Automated CRM data enrichment and behavioral profiling

## Summary
The Contact Enrichment Engine is an intelligent Uplizd workflow that automatically updates and enriches customer contact profiles by synthesizing behavioral data from multiple sources. By leveraging the Composio Toolset, this solution eliminates manual data entry, ensures a single source of truth for your CRM, and significantly increases pipeline velocity by providing sales and marketing teams with real-time, high-fidelity contact intelligence.

---

## Demo
![Contact Enrichment Engine workflow diagram showing data flow from CRM to enrichment tools](image.png)
**Alt text (SEO-ready):** Uplizd Contact Enrichment Engine workflow for automated CRM data synchronization, behavioral profile enrichment, and sales intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ca1873c3-6a97-5060-a2c6-3c744b70d308)

---

## Category
**Primary category:** CRM data
**Secondary tags:** crm, enrichment, data hygiene, sales operations, lead scoring, composio, ai workflow, data sync.
This solution bridges the gap between raw contact records and actionable sales intelligence by automating the enrichment process across your existing tech stack.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maintain pristine data hygiene and actionable lead insights.

*   **Sales Operations Manager**
    *   Ensures CRM data integrity by automating the reconciliation of fragmented contact records.
*   **Revenue Operations (RevOps) Lead**
    *   Standardizes lead scoring models by injecting behavioral data directly into the CRM pipeline.
*   **Account Executive**
    *   Reduces research time by having enriched company and contact insights ready before every discovery call.
*   **Marketing Operations Specialist**
    *   Improves segmentation accuracy by syncing enriched behavioral attributes back into marketing automation platforms.

---

## Features
- **Automated Data Synthesis**
  Aggregates behavioral signals from web activity, email engagement, and third-party databases into a unified contact profile.
- **Real-time CRM Sync**
  Utilizes the Composio Toolset to push enriched data directly into Salesforce, HubSpot, or Dynamics 365 without manual intervention.
- **Intelligent Field Mapping**
  Automatically identifies and updates empty or outdated contact fields, ensuring your CRM remains a reliable single source of truth.
- **Behavioral Scoring Integration**
  Calculates and updates lead scores based on the latest enrichment data, allowing teams to prioritize high-intent prospects.
- **Compliance-Aware Processing**
  Ensures all enrichment activities respect data privacy settings and field-level permissions defined in your connected CRM.

---

## Use Cases
**Lead Qualification & Prioritization**
*   Automatically flag leads that meet high-value firmographic criteria after enrichment.
*   Update lead status based on real-time behavioral triggers synced from external tools.

**CRM Data Hygiene**
*   Standardize job titles, company sizes, and industry tags across thousands of legacy contact records.
*   Identify and merge duplicate contact profiles identified during the enrichment process.

**Sales Intelligence**
*   Inject "Company News" or "Recent Funding" alerts directly into the CRM notes field for AE preparation.
*   Sync social media handles and professional bios to contact records to facilitate personalized outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the **Contact Enrichment Engine**.
2. Click "Import" to add the workflow to your workspace.
3. Connect your CRM credentials and API keys within the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM objects and enrichment triggers.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event (e.g., new lead creation or periodic update request).
*   **Agent**: Analyzes the contact data and determines which enrichment tools to query.
*   **Composio Toolset**: Executes the API calls to fetch external data and write updates to the CRM.
*   **Chat Output**: Confirms the enrichment status and logs the changes made to the contact record.

### 3) Run the Flow
Use the Playground to test the flow with the following prompts:
* `Enrich the contact record for john.doe@example.com with current company and professional data.`
* `Scan the last 50 leads in the 'New' stage and update their industry and revenue fields.`
* `Find and append the LinkedIn URL and recent funding news to the account record for Acme Corp.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data retrieval and mapping logic.
*   **System Prompt:** Focus on data accuracy and CRM field mapping constraints.
*   **Tool Selection:** Enable only the necessary enrichment and CRM write-back tools.
*   **Error Handling:** Configure the agent to flag records that require manual review for ambiguous matches.

### 2) Composio Toolset Node
Requires an active API key and appropriate scope permissions for your CRM (e.g., read/write access to Contacts and Accounts).

### 3) Tool Availability
*   **CRM Connectors:** Salesforce, HubSpot, Dynamics 365.
*   **Enrichment APIs:** Clearbit, ZoomInfo, Apollo.io.
*   **Utility Tools:** Data formatting, string normalization, and deduplication logic.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Deep-dive firmographic and contact intelligence gathering.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Multi-platform synchronization and conflict resolution for CRM records.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automated cleanup and formatting for large-scale CRM databases.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automated account-level research and discovery for sales teams.
