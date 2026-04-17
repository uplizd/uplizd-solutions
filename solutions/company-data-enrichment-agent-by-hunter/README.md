# Company Data Enrichment Agent (Uplizd) - Automated B2B profile enrichment and contact intelligence

## Summary
The Company Data Enrichment Agent leverages the Hunter API via the Composio Toolset to automatically populate and verify B2B lead data. By integrating real-time domain research into your CRM workflows, this agent eliminates manual data entry, reduces lead decay, and ensures your sales team has accurate, high-quality contact information for every prospect.

---

## Demo
![Company Data Enrichment Agent workflow interface showing Hunter API integration and CRM data mapping](image.png)

**Alt text (SEO-ready):** Company Data Enrichment Agent by Uplizd, automated B2B lead research, Hunter API integration, CRM data hygiene, and sales intelligence workflow.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/company-data-enrichment-agent-by-hunter)

---

## Category
**Primary category:** Sales automation

**Secondary tags:** crm, hunter, b2b, lead enrichment, data hygiene, sales intelligence, composio, ai workflow

This solution bridges the gap between raw domain data and actionable CRM insights, streamlining the lead qualification process for revenue teams.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to automate the tedious process of prospect research and contact verification.

*   **Sales Development Reps (SDRs)**
    *   Automate the discovery of verified professional email addresses and contact patterns to accelerate outreach.
*   **RevOps Managers**
    *   Maintain high-quality CRM data hygiene by ensuring all company records are enriched with up-to-date domain intelligence.
*   **Account Executives**
    *   Gain immediate context on target accounts, allowing for personalized messaging and higher conversion rates.
*   **Marketing Operations Specialists**
    *   Improve lead scoring accuracy by appending firmographic data and contact verification status to incoming inbound leads.

---

## Features
- **Real-time Domain Search**
    Automatically query the Hunter API to retrieve verified contact information associated with any company domain.
- **Automated CRM Sync**
    Seamlessly push enriched data, including job titles and email patterns, directly into your CRM records via the Composio Toolset.
- **Lead Verification Logic**
    Filter out invalid or low-confidence contact data before it enters your pipeline, ensuring only high-quality leads are processed.
- **Intelligent Pattern Matching**
    Detect and apply company-specific email formats to predict contact information for new leads where direct matches aren't available.
- **Workflow Automation**
    Trigger enrichment tasks automatically upon lead creation or status changes, keeping your sales pipeline moving without manual intervention.

---

## Use Cases
**Lead Prospecting & Outreach**
*   Automatically enrich new inbound leads with verified contact details to reduce time-to-first-touch.
*   Identify key decision-makers at target accounts by mapping domain-specific contact lists to CRM opportunities.

**CRM Data Hygiene**
*   Periodically scan existing company records to update outdated contact information and remove stale email addresses.
*   Standardize lead profiles by appending missing firmographic data to ensure consistent reporting across the sales funnel.

**Sales Intelligence**
*   Generate a "Company Profile" summary for sales teams before discovery calls, including verified contacts and domain insights.
*   Prioritize outreach efforts by scoring leads based on the availability and verification status of their professional contact data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Company Data Enrichment Agent.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Hunter API key and CRM credentials in the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM objects and field names.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target domain or company name from the user or automated trigger.
*   **Agent**: Processes the request, determines the necessary Hunter API calls, and formats the output.
*   **Composio Toolset**: Executes the secure API calls to Hunter and writes the enriched data back to your CRM.
*   **Chat Output**: Confirms the enrichment status and provides a summary of the data added to the record.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
* `Enrich the domain 'example.com' and update the lead record in Salesforce.`
* `Find and verify contact information for the marketing department at 'acme-corp.com'.`
* `Check for new contacts at 'tech-startup.io' and add them to my CRM pipeline.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data orchestrator between the user's intent and the Hunter API.
*   Prioritize accuracy when parsing domain names and company identifiers.
*   Use structured output to map Hunter API responses to your CRM's specific field requirements.
*   Maintain a professional tone when summarizing enrichment results for the user.

### 2) Composio Toolset Node
Requires a valid Hunter API key and appropriate CRM permissions (e.g., Read/Write access to Leads or Accounts). Ensure the connection scope allows for bulk updates if processing large lists.

### 3) Tool Availability
*   **Hunter Domain Search**: Retrieves contact patterns and verified emails.
*   **CRM Connector**: Handles the bi-directional sync of enriched data fields.
*   **Data Validation Utility**: Filters and formats contact strings before CRM ingestion.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep-dive firmographic and contact data enrichment.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize and resolve data conflicts across multiple platforms.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Comprehensive account research and intelligence aggregation.
