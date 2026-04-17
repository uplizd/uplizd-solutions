# Contact Data Enrichment Agent (Uplizd) - Automated CRM contact hygiene and intelligence

## Summary
The Contact Data Enrichment Agent by ActiveCampaign is an intelligent Uplizd workflow designed to automate the synchronization and enhancement of your CRM contact database. By leveraging the Composio Toolset, this agent identifies incomplete records, fetches missing professional insights, and updates your CRM in real-time, ensuring your sales and marketing teams always have a single source of truth for high-quality, actionable lead data.

---

## Demo
![Contact Data Enrichment Agent workflow showing CRM integration and data synchronization](image.png)
**Alt text (SEO-ready):** Contact Data Enrichment Agent by Uplizd for automated CRM data hygiene, lead intelligence, and ActiveCampaign synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1dace194-ace5-586f-8b91-fea933fea463)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** crm, activecampaign, data enrichment, lead intelligence, data hygiene, sales automation, composio, ai workflow
- This solution bridges the gap between raw lead capture and structured CRM data, enabling automated enrichment to fuel personalized outreach.

---

## Who is this for?
This agent is built for teams looking to eliminate manual data entry and improve lead conversion rates through automated intelligence.

- **Marketing Operations Manager**
    - Automates the enrichment of lead records to ensure segmentation lists are always accurate and up-to-date.
- **Sales Development Representative (SDR)**
    - Receives enriched lead profiles directly in the CRM, allowing for faster research and more personalized outreach.
- **RevOps Specialist**
    - Maintains high data hygiene standards across the tech stack, reducing technical debt and improving pipeline reporting accuracy.
- **Growth Marketer**
    - Leverages enriched professional data to optimize lead scoring models and improve campaign targeting precision.

---

## Features
- **Automated Data Enrichment**
    - Automatically triggers lookups to fill missing contact fields like job titles, company size, and industry.
- **Real-time CRM Sync**
    - Seamlessly pushes enriched data back into ActiveCampaign, ensuring the CRM remains the single source of truth.
- **Intelligent Conflict Resolution**
    - Uses AI logic to compare incoming data against existing records, preventing duplicates and overwriting outdated information.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely connect with CRM APIs and external data providers without custom middleware.
- **Customizable Enrichment Rules**
    - Allows users to define specific fields that require enrichment, ensuring the agent only updates the data points that matter most.

---

## Use Cases
**Lead Qualification & Scoring**
- Automatically append firmographic data to new leads to prioritize high-value accounts.
- Flag incomplete records for manual review if the agent cannot find sufficient enrichment data.

**CRM Data Hygiene**
- Run periodic sweeps to identify and update stale contact information, such as outdated job titles or company names.
- Standardize formatting for phone numbers and email addresses across the entire contact database.

**Sales Pipeline Acceleration**
- Trigger enrichment workflows immediately upon lead capture to provide sales teams with instant context.
- Sync enriched data to custom fields to enable dynamic content personalization in email sequences.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Authenticate your ActiveCampaign account within the Uplizd environment.
3. Configure your API keys for the Composio Toolset to enable external data lookups.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) before deploying.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request for contact enrichment.
- **Agent**: The core logic node that processes the contact request and determines which fields need enrichment.
- **Composio Toolset**: Executes the API calls to fetch external data and update the CRM.
- **Chat Output**: Returns a summary of the enrichment actions taken or flags records that require attention.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Enrich the contact record for john.doe@example.com with current job title and company industry.`
- `Scan the last 50 leads in the 'New Signups' list and update any missing professional data.`
- `Identify and fix any formatting issues in the phone number fields for the 'Q3 Leads' segment.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data steward, interpreting enrichment requirements and managing tool execution.
- Instruction: "You are an expert CRM data analyst. Your goal is to fetch missing contact information and ensure data accuracy."
- Instruction: "Always verify the existing record before applying updates to prevent overwriting valid, manually entered data."
- Instruction: "If an enrichment source returns multiple results, select the most relevant match based on company domain or email address."

### 2) Composio Toolset Node
- Requires an active API key for your CRM (ActiveCampaign) and any secondary data enrichment providers.
- Connection scope should be limited to "Read/Write" access for contact objects to ensure the agent can perform updates.

### 3) Tool Availability
- **CRM Connector**: Ability to read and update contact records.
- **Enrichment API**: Capability to query external databases for professional contact insights.
- **Data Validator**: Logic to check for field completeness and format compliance.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep-dive company and contact research for high-value account targeting.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Multi-platform synchronization for maintaining consistent data across your entire tech stack.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and deduplication for maintaining a healthy CRM database.
