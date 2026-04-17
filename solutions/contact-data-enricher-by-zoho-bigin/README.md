# Contact Data Enricher by Zoho Bigin (Uplizd) - Automated CRM record enrichment and data hygiene

## Summary
The Contact Data Enricher by Zoho Bigin is an intelligent Uplizd workflow designed to automate the enhancement of your CRM contact database. By leveraging the Composio Toolset to bridge AI agents with Zoho Bigin, this solution identifies missing fields, standardizes contact information, and ensures your sales team operates with a single source of truth, significantly increasing pipeline velocity and data hygiene.

---

## Demo
![Contact Data Enricher workflow interface showing Zoho Bigin integration and AI-driven data mapping](image.png)
**Alt text (SEO-ready):** Contact Data Enricher by Zoho Bigin workflow, Uplizd CRM data hygiene automation, AI-driven contact record enrichment, and Composio integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/e7cb54ba-8cf9-5c07-be38-10fe088f71b5)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** zoho bigin, data enrichment, crm, data hygiene, sales operations, lead management, composio, ai workflow
- This solution streamlines CRM operations by automatically populating and validating contact records to maintain high-quality sales data.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to eliminate manual data entry and improve lead quality.

- **Sales Operations Manager**
    - Ensures CRM data integrity and reduces manual cleanup time for the entire sales department.
- **Account Executive**
    - Gains access to complete, verified contact profiles, allowing for more personalized and effective outreach.
- **Growth Marketer**
    - Maintains accurate contact segments for targeted campaigns by ensuring all lead records are fully enriched.
- **CRM Administrator**
    - Automates the maintenance of database hygiene, preventing data decay and improving overall system reliability.

---

## Features
- **Automated Data Enrichment**
    - Automatically fetches and populates missing contact details from external sources directly into Zoho Bigin.
- **Intelligent Data Standardization**
    - Normalizes contact formats, such as phone numbers and addresses, ensuring consistency across your entire CRM.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely connect the Uplizd agent with Zoho Bigin APIs for real-time updates.
- **Proactive Hygiene Checks**
    - Identifies incomplete or outdated records, prompting the agent to perform updates before data becomes stale.
- **Customizable Logic Flows**
    - Tailors enrichment rules to match your specific business requirements and field mapping preferences.

---

## Use Cases
**Lead Qualification**
- Automatically append job titles and company sizes to new leads to prioritize high-value prospects.
- Flag incomplete lead records for immediate enrichment before they enter the sales pipeline.

**Database Maintenance**
- Periodically scan existing contacts to update outdated email addresses or professional contact information.
- Merge duplicate contact entries identified during the enrichment process to maintain a clean database.

**Sales Outreach Preparation**
- Ensure every contact has a verified LinkedIn profile or company website link before an AE initiates outreach.
- Populate custom fields in Zoho Bigin based on external research to provide context for sales calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Select your workspace and import the template.
3. Connect your Zoho Bigin account via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual request to enrich a specific contact or list.
- **Agent**: Processes the data, determines missing fields, and formulates update instructions.
- **Composio Toolset**: Executes the API calls to read and write data to Zoho Bigin.
- **Chat Output**: Confirms the enrichment status and reports any records that could not be updated.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Enrich the contact record for John Doe in Zoho Bigin.`
- `Find and update missing company information for all leads created this week.`
- `Check the contact list for missing phone numbers and update them if available.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the data steward, interpreting CRM data and deciding which fields require enrichment.
- Use a model capable of structured data extraction and JSON formatting.
- Instruct the agent to prioritize accuracy and flag records where information is ambiguous.
- Configure the agent to output a summary of changes made to the CRM.

### 2) Composio Toolset Node
- Provide your Zoho Bigin API credentials within the Composio dashboard.
- Set the connection scope to allow read/write access to the 'Contacts' and 'Leads' modules.

### 3) Tool Availability
- **Zoho Bigin Search**: Locate contact records by email or name.
- **Zoho Bigin Update**: Modify fields for existing records.
- **Data Validation Tool**: Verify format and completeness of contact fields.

---

## Related Solutions
- [Account Research Assistant by ZoomInfo](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research for B2B account enrichment.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize contact data across multiple platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for CRM databases.
