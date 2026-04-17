# Contact Data Enrichment Engine (Uplizd) - Automated Prospect Intelligence and Verification

## Summary
The Contact Data Enrichment Engine is an intelligent Uplizd workflow designed to automate the discovery, verification, and synchronization of prospect contact details. By leveraging the Composio Toolset to query external intelligence platforms, this solution eliminates manual data entry, reduces lead decay, and ensures your CRM maintains a single source of truth for high-quality outreach data.

---

## Demo
![Contact Data Enrichment Engine workflow diagram showing data flow from input to CRM sync](image.png)
**Alt text (SEO-ready):** Uplizd contact data enrichment workflow automating CRM lead verification and prospect intelligence via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/4490e3c8-6e4b-59b2-8f95-3814d6e34836)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** crm, lead enrichment, data hygiene, sales automation, prospect intelligence, composio, data sync, ai workflow
- This solution bridges the gap between raw lead lists and actionable sales intelligence by automating the enrichment process across your existing CRM infrastructure.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outbound efforts without sacrificing data quality.

- **Sales Development Representative (SDR)**
    - Reduces time spent manually searching for verified emails and phone numbers.
- **Revenue Operations (RevOps) Manager**
    - Ensures pipeline data remains clean and actionable through automated validation.
- **Growth Marketer**
    - Increases campaign conversion rates by targeting prospects with accurate, enriched contact profiles.
- **Account Executive (AE)**
    - Provides immediate access to decision-maker contact intelligence during the deal qualification process.

---

## Features
- **Automated Prospect Lookup**
    - Automatically triggers searches across intelligence providers to find missing contact fields for new leads.
- **Real-time Data Verification**
    - Validates email deliverability and phone number accuracy before syncing data to your CRM.
- **Intelligent CRM Sync**
    - Maps enriched data points directly to custom fields in Salesforce, HubSpot, or Dynamics 365.
- **Conflict Resolution Logic**
    - Prevents data overwrites by comparing existing CRM records against newly retrieved intelligence.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely connect with multiple data providers through a unified interface.

---

## Use Cases
**Lead Qualification**
- Automatically enrich inbound leads with job titles and company size upon form submission.
- Flag incomplete lead profiles for immediate enrichment before they reach the sales queue.

**Database Hygiene**
- Periodically scan existing CRM contacts to update outdated professional information.
- Remove or archive contacts that fail verification checks to maintain a healthy database.

**Outbound Sales Scaling**
- Bulk-enrich cold outreach lists to ensure high deliverability for multi-channel campaigns.
- Sync verified direct-dial numbers to the CRM to accelerate the sales prospecting cycle.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Contact Data Enrichment Engine.
2. Click "Import" to add the workflow to your workspace.
3. Connect your preferred CRM and data intelligence accounts via the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM field names and API endpoints.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect name or company domain to initiate the enrichment process.
- **Agent**: Analyzes the input and determines which data points are missing or require verification.
- **Composio Toolset**: Executes the search and validation queries against connected intelligence providers.
- **Chat Output**: Returns the enriched contact profile and confirms the successful update to the CRM.

### 3) Run the Flow
Use the Playground to test the enrichment logic with these example prompts:
- `Enrich the contact record for john.doe@example.com and update the phone field.`
- `Find the current job title and LinkedIn profile for the lead at domain: acmecorp.com.`
- `Verify the contact details for the latest 5 leads added to the 'New Prospect' list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for data retrieval and mapping.
- Use a high-reasoning model to handle complex mapping instructions.
- Ensure the system prompt includes strict field-mapping requirements for your CRM.
- Enable tool-calling capabilities to allow the agent to invoke the Composio Toolset.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure access to external data providers.
- Configure the connection scope to include read/write permissions for your CRM and enrichment tools.

### 3) Tool Availability
- **CRM Connector**: For reading and updating contact records.
- **Intelligence API**: For fetching verified prospect data.
- **Validation Utility**: For checking email and phone number formatting.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep-dive research for account-based marketing and sales.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Bi-directional synchronization for cross-platform data consistency.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for CRM databases.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automated lookup of company-level intelligence and firmographics.
