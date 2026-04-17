# CRM Lead Enrichment Engine (Uplizd) - Automated data intelligence for sales pipeline growth

## Summary
The CRM Lead Enrichment Engine is an intelligent Uplizd workflow that automates the gathering of firmographic and contact data to ensure your sales pipeline remains accurate and actionable. By leveraging the Composio Toolset to bridge your CRM with external intelligence providers, this solution eliminates manual research, reduces data decay, and empowers sales teams with a single source of truth for every lead.

---

## Demo
![CRM Lead Enrichment Engine workflow showing automated data flow from input to CRM update](image.png)
**Alt text (SEO-ready):** Uplizd CRM Lead Enrichment Engine workflow diagram showing automated data synchronization, lead qualification, and CRM integration via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a96acb2a-fef8-5209-a211-3cdc2953bef2)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead enrichment, sales intelligence, data hygiene, pipeline, composio, ai workflow, salesforce, hubspot
- This solution bridges the gap between raw lead data and actionable sales intelligence by automating real-time enrichment across your CRM ecosystem.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize conversion rates through better data.

- **Sales Operations Manager**
    - Automates the enrichment of incoming leads to ensure sales reps have complete context without manual data entry.
- **Account Executive**
    - Gains immediate visibility into prospect firmographics and company size, allowing for highly personalized outreach.
- **BDR/SDR**
    - Reduces time spent on manual research by automatically populating missing lead fields from verified external sources.
- **Revenue Operations Lead**
    - Maintains high data hygiene standards across the CRM, ensuring consistent lead scoring and territory assignment.

---

## Features
- **Automated Data Retrieval**
    - Seamlessly queries external intelligence providers via the Composio Toolset to fetch missing lead details in real-time.
- **CRM Synchronization**
    - Automatically updates lead records in Salesforce, HubSpot, or Dynamics 365, ensuring your system of record is always current.
- **Intelligent Field Mapping**
    - Uses AI to map unstructured data points to specific CRM fields, handling formatting and normalization automatically.
- **Customizable Enrichment Triggers**
    - Configures the workflow to activate upon new lead creation or status changes, maintaining a clean and updated pipeline.
- **Error Handling & Logging**
    - Provides robust monitoring of enrichment tasks, ensuring that failed lookups are flagged for manual review without stalling the pipeline.

---

## Use Cases
**Lead Qualification & Scoring**
- Automatically append company headcount and revenue data to new leads to prioritize high-value accounts.
- Flag leads with missing contact information for immediate enrichment before they reach the sales queue.

**Sales Outreach Optimization**
- Populate lead records with verified LinkedIn profiles or company website data to enable personalized email sequences.
- Sync industry-specific tags to CRM records to segment leads for targeted marketing campaigns.

**Data Hygiene & Maintenance**
- Periodically refresh stale lead data to ensure that contact information remains accurate throughout the sales cycle.
- Standardize company names and job titles across the CRM to improve reporting and lead routing accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Solution."
2. Import the `crm-lead-enrichment-engine-by-composio` template file.
3. Connect your preferred CRM and intelligence provider accounts within the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead identifier or email address to trigger the enrichment process.
- **Agent**: Analyzes the request and determines which data points are missing from the CRM.
- **Composio Toolset**: Executes the API calls to fetch and verify data from external intelligence providers.
- **Chat Output**: Confirms the successful update of the CRM record or reports any missing data gaps.

### 3) Run the Flow
Use the Playground to test your enrichment logic:
- `Enrich lead with email: contact@example.com and update Salesforce.`
- `Fetch company details for the latest lead in the HubSpot 'New' stage.`
- `Check for missing industry data on all leads created in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your CRM and the enrichment tools.
- **Recommended instruction pattern:**
    - "Identify the missing firmographic data for the provided lead email."
    - "Use the Composio Toolset to fetch the latest company information."
    - "Update the CRM record only if the confidence score for the data is above 90%."

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for the necessary CRM and intelligence integrations.
- **Connection Scope**: Grant read/write access to your CRM (e.g., Salesforce, HubSpot) and read access to your enrichment data providers.

### 3) Tool Availability
- **CRM Connectors**: Read/Write access to Lead and Account objects.
- **Intelligence API Connectors**: Capability to query firmographic and contact databases.
- **Data Normalization Tools**: Logic to format and clean incoming data before CRM insertion.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Specialized tools for deep-dive company research and contact discovery.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize records across multiple platforms to maintain consistent data states.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for your CRM database.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Focused assistant for gathering high-intent account signals and intelligence.
