# Contact Database Cleaner (Uplizd) - Automated CRM data hygiene and enrichment

## Summary
The Contact Database Cleaner by Segmetrics is an intelligent Uplizd workflow designed to automate the deduplication, formatting, and enrichment of your contact records. By leveraging the Composio Toolset, this solution ensures your CRM remains a single source of truth, eliminating manual data entry errors and improving pipeline velocity through high-quality, actionable contact data.

---

## Demo
![Contact Database Cleaner workflow interface showing automated data validation and enrichment nodes](image.png)
**Alt text (SEO-ready):** Uplizd Contact Database Cleaner workflow for CRM data hygiene, automated contact deduplication, and Segmetrics data enrichment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c58c4e50-1d92-597c-abc0-525aa6cc06a7)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** crm, segmetrics, data cleaning, lead enrichment, automation, data sync, pipeline, composio
- This solution streamlines CRM operations by maintaining pristine contact records, ensuring your marketing and sales teams always work with accurate, up-to-date information.

---

## Who is this for?
This solution is built for teams looking to eliminate data decay and improve the reliability of their customer intelligence.

- **RevOps Managers**
    - Automate the maintenance of clean, standardized contact records across the entire tech stack.
- **Marketing Operations Specialists**
    - Ensure high deliverability and accurate segmentation by removing duplicate or malformed contact entries.
- **Sales Development Representatives (SDRs)**
    - Spend less time researching contact details and more time engaging with verified, enriched leads.
- **Data Analysts**
    - Reduce noise in reporting by ensuring the underlying contact database is consistent and free of redundant data.

---

## Features
- **Automated Deduplication**
    - Identifies and merges duplicate contact records based on custom matching logic to prevent fragmented customer profiles.
- **Real-time Data Formatting**
    - Standardizes phone numbers, email addresses, and naming conventions automatically to maintain professional data quality.
- **Segmetrics Enrichment**
    - Integrates directly with Segmetrics to append missing behavioral and attribution data to your existing contact records.
- **Compliance-Aware Cleanup**
    - Automatically flags or removes contacts that do not meet your organization's data privacy and compliance standards.
- **Composio-Powered Sync**
    - Utilizes the Composio Toolset to bridge the gap between your CRM and external data sources for seamless, real-time updates.

---

## Use Cases
**Lead Management**
- Automatically merge duplicate leads created by multiple marketing campaigns or web forms.
- Standardize lead source fields to ensure accurate attribution reporting in your CRM.

**Data Hygiene**
- Identify and purge inactive or "dead" contacts that haven't engaged with your brand in over 12 months.
- Correct common formatting errors in contact fields like state abbreviations or international phone formats.

**Sales Intelligence**
- Enrich existing contact profiles with missing job titles or company information retrieved via integrated tools.
- Flag incomplete records for manual review by the sales team to ensure no high-value opportunity is missed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Contact Database Cleaner template from the solution library.
3. Connect your CRM and Segmetrics accounts via the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM environment and verify all API credentials.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled batch processing requests for database cleanup.
- **Agent**: Analyzes contact records for inconsistencies and determines the necessary cleaning or enrichment actions.
- **Composio Toolset**: Executes the specific API calls required to update, merge, or enrich data within your CRM.
- **Chat Output**: Provides a summary report of all cleaned, merged, or enriched records for your review.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Clean all duplicate contacts in the 'New Leads' list created in the last 30 days.`
- `Standardize all phone numbers to E.164 format for the current contact database.`
- `Enrich all contacts missing job titles using the latest Segmetrics data.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for data validation and transformation.
- Use a high-reasoning model to ensure accurate identification of duplicate records.
- Configure the system prompt to prioritize data integrity and strict adherence to formatting rules.
- Enable tool-calling capabilities to allow the agent to interact with your CRM API dynamically.

### 2) Composio Toolset Node
- Provide your unique API key to authorize the Composio Toolset.
- Set the connection scope to include read/write access for your specific CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **CRM Connector**: For fetching, updating, and deleting contact records.
- **Data Validator**: For checking email syntax, phone number formats, and field completeness.
- **Enrichment Engine**: For querying Segmetrics and other external data providers to fill missing record attributes.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enhance account data with deep intelligence and firmographic insights.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize contact and lead data across multiple platforms in real-time.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Optimize your sales stages and manage deal velocity effectively.
