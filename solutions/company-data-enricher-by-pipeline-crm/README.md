# Company Data Enricher (Uplizd) - Automated CRM record enrichment and data hygiene

## Summary
The Company Data Enricher is an intelligent Uplizd workflow that automatically fetches, validates, and updates company records within your CRM. By leveraging real-time data sources via the Composio Toolset, this solution eliminates manual research, ensures your sales pipeline remains populated with accurate firmographic data, and maintains high-quality CRM hygiene for better lead scoring and outreach.

---

## Demo
![Company Data Enricher workflow showing automated CRM record enrichment and data validation](image.png)
**Alt text (SEO-ready):** Company Data Enricher workflow for automated CRM record enrichment, data hygiene, and sales pipeline optimization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1ac22aee-774c-5a98-89d3-9d06b340c225)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** crm, data enrichment, sales operations, lead qualification, data hygiene, composio, ai workflow, pipeline management
- This solution bridges the gap between raw CRM entries and actionable business intelligence by automating the enrichment process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual data entry and improve lead accuracy.

- **Sales Operations Manager**
    - Automates the maintenance of clean, enriched company profiles to ensure consistent reporting.
- **Account Executive**
    - Gains immediate access to firmographic insights, allowing for more personalized and effective outreach.
- **Revenue Operations (RevOps) Lead**
    - Standardizes data quality across the organization, reducing decay and improving pipeline velocity.
- **Business Development Representative (BDR)**
    - Identifies high-value accounts faster by having pre-enriched data ready for qualification.

---

## Features
- **Automated Data Enrichment**
    - Automatically pulls firmographic details like industry, revenue, and employee count into your CRM records.
- **Real-time CRM Sync**
    - Ensures that updates are pushed directly to your CRM platform, keeping your source of truth current.
- **Intelligent Data Validation**
    - Cross-references existing CRM data against external sources to flag inconsistencies or outdated information.
- **Composio-Powered Connectivity**
    - Utilizes the Composio Toolset to securely interface with multiple CRM vendors and data providers.
- **Customizable Enrichment Rules**
    - Define specific fields and triggers to control exactly what data is updated and when the enrichment occurs.

---

## Use Cases
**Lead Qualification**
- Automatically enrich incoming leads with company size and industry to prioritize high-value prospects.
- Flag incomplete lead profiles for immediate enrichment before they reach the sales team.

**Account Management**
- Refresh account data periodically to identify growth opportunities within existing client portfolios.
- Sync updated firmographic data to ensure account health scores are calculated using the latest metrics.

**Data Hygiene**
- Identify and update stale company records that lack critical firmographic fields.
- Standardize company naming conventions and address formats across the entire CRM database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project to import the workflow.
3. Connect your CRM and data provider accounts via the Composio integration settings.
4. Ensure nodes are correctly mapped and all required API keys are active in the configuration panel.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to enrich a specific company record.
- **Agent**: Analyzes the request, determines the necessary data points, and orchestrates the enrichment logic.
- **Composio Toolset**: Executes the API calls to fetch external data and perform the write-back to your CRM.
- **Chat Output**: Confirms the enrichment status and provides a summary of the fields updated.

### 3) Run the Flow
Use the Playground to test the enrichment process with these prompts:
- `Enrich the company record for Acme Corp in Salesforce.`
- `Check and update the industry and employee count for the latest leads in HubSpot.`
- `Perform a bulk audit and enrichment for all accounts created in the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for data validation and field mapping.
- Use a high-reasoning model to ensure accurate parsing of company information.
- Instruct the agent to prioritize data completeness and format consistency.
- Configure the agent to handle missing data gracefully by logging errors for manual review.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication between Uplizd and your CRM/Data providers.
- Set the connection scope to allow read/write access to company and lead objects.

### 3) Tool Availability
- **CRM Connectors**: Read/Write access to company, lead, and account objects.
- **Data Enrichment APIs**: Capability to query firmographic databases.
- **Validation Logic**: Internal tools for identifying data decay and formatting errors.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Specialized tools for deep-dive firmographic research.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keeps data consistent across multiple platforms and environments.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Focused on gathering high-intent signals for sales outreach.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Focuses on bulk cleanup and compliance-aware data maintenance.
