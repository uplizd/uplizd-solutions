# CRM Data Quality Guardian (Uplizd) - Automated CRM data hygiene and standardization

## Summary
The CRM Data Quality Guardian is an intelligent Uplizd workflow designed to maintain a single source of truth by automatically identifying, cleaning, and standardizing customer records. By leveraging PeopleDataLabs for enrichment and automated validation, this solution eliminates manual data entry errors, reduces record decay, and ensures your CRM remains a reliable foundation for sales and marketing operations.

---

## Demo
![CRM Data Quality Guardian workflow showing data enrichment and validation nodes](image.png)
**Alt text (SEO-ready):** CRM Data Quality Guardian workflow for automated data hygiene, record enrichment, and CRM standardization using Uplizd and PeopleDataLabs.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/faa01501-3172-5a54-81e7-0321e6c27c5d)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** crm, peopledatalabs, data hygiene, data enrichment, salesforce, hubspot, data sync, ai workflow
- This solution bridges the gap between raw, messy CRM inputs and high-fidelity, enriched customer profiles ready for outreach.

---

## Who is this for?
This solution is designed for teams managing high-volume customer data who need to maintain pipeline velocity without sacrificing data integrity.

- **RevOps Manager**
    - Automates the enforcement of data standards across the entire lead lifecycle.
- **Sales Operations Specialist**
    - Reduces time spent on manual record cleanup and duplicate merging.
- **Marketing Operations Lead**
    - Ensures high-quality contact data for targeted segmentation and campaign performance.
- **Account Executive**
    - Provides reliable, enriched contact information to improve outreach personalization.

---

## Features
- **Automated Data Enrichment**
    - Automatically pulls missing firmographic and demographic details via PeopleDataLabs to complete sparse records.
- **Real-time Validation**
    - Checks incoming data against standard formatting rules to prevent invalid entries from entering the CRM.
- **Intelligent Deduplication**
    - Identifies potential duplicate records based on cross-referenced email and domain patterns.
- **Standardization Engine**
    - Normalizes job titles, industry tags, and location formats to ensure consistent reporting across the organization.
- **Seamless CRM Integration**
    - Uses the Composio Toolset to push cleaned and enriched data directly back into Salesforce or HubSpot.

---

## Use Cases
**Data Hygiene & Maintenance**
- Automatically flagging and correcting malformed email addresses or missing phone numbers in new lead imports.
- Standardizing company industry classifications to match internal reporting taxonomies.

**Lead Enrichment**
- Appending missing LinkedIn profiles and professional background data to inbound leads for better qualification.
- Identifying the correct decision-maker seniority level based on enriched PeopleDataLabs insights.

**Pipeline Integrity**
- Scrubbing stale or incomplete records before they reach the sales pipeline to prevent wasted outreach.
- Syncing enriched data points to ensure AEs have the context needed for high-conversion discovery calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your CRM and PeopleDataLabs credentials within the workflow settings.
4. Ensure nodes are correctly mapped to your specific CRM objects and field names.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request for record cleanup.
- **Agent**: Analyzes the record, determines missing fields, and orchestrates the enrichment logic.
- **Composio Toolset**: Executes the API calls to PeopleDataLabs and performs the write-back to your CRM.
- **Chat Output**: Returns a summary of the cleaning actions taken and the updated record status.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Clean and enrich the contact record for john.doe@example.com`
- `Standardize the industry field for all new leads created in the last 24 hours`
- `Identify and merge duplicate accounts associated with the domain 'acme-corp.com'`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic controller for data validation and enrichment decisions.
- Use a model capable of structured JSON output for reliable API interactions.
- Instruct the agent to prioritize data accuracy and flag records that fall below a specific confidence score.
- Ensure the agent is configured to handle null values gracefully during the enrichment process.

### 2) Composio Toolset Node
- Provide your PeopleDataLabs API key and CRM (Salesforce/HubSpot) credentials.
- Set the connection scope to allow read/write access to lead and account objects.

### 3) Tool Availability
- **PeopleDataLabs API**: For fetching enriched firmographic and contact data.
- **CRM Connector**: For updating record fields and managing duplicate status.
- **Data Validator**: For checking format compliance and field completeness.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](Account Intelligence Gatherer) - Enrich accounts with contact data and firmographic insights.
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize data across multiple platforms with conflict resolution.
- [../account-research-assistant-by-zoominfo/README.md](Account Research Assistant) - Deep dive into account details using ZoomInfo intelligence.
