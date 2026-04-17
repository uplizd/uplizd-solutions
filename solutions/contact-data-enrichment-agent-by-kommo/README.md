# Contact Data Enrichment Agent (Uplizd) - Automate CRM record enrichment with Kommo

## Summary
The Contact Data Enrichment Agent is an intelligent Uplizd workflow designed to bridge the gap between incomplete CRM records and actionable business intelligence. By leveraging the Composio Toolset to query external data sources and update Kommo CRM in real-time, this solution eliminates manual data entry, ensures your sales team has the most accurate contact details, and significantly improves pipeline velocity through automated data hygiene.

---

## Demo
![Contact Data Enrichment Agent workflow interface showing Kommo CRM integration and data mapping nodes](image.png)
**Alt text (SEO-ready):** Contact Data Enrichment Agent workflow for Kommo CRM, showing automated data synchronization, record updates, and Uplizd AI integration for sales operations.

---

## 🚀 Run on Uplizd
[**Launch Contact Data Enrichment Agent**](https://uplizd.ai/solutions/26ff36e6-fec7-5eab-b6f5-03aec5571950)

---

## Category
- **Primary category:** CRM data
- **Secondary tags:** kommo, crm, data enrichment, sales automation, lead management, data hygiene, composio, ai workflow
- This solution streamlines your RevOps stack by automatically populating missing contact fields within Kommo using AI-driven data retrieval.

---

## Who is this for?
This agent is built for teams looking to maintain a pristine CRM database without the manual overhead of constant research.

- **Sales Operations Manager**
    - Ensures data integrity across the sales stack while reducing time spent on manual record updates.
- **Account Executive**
    - Gains immediate access to enriched contact profiles, allowing for more personalized outreach and faster deal progression.
- **Lead Generation Specialist**
    - Automates the qualification process by ensuring every incoming lead is automatically enriched with company and contact context.
- **CRM Administrator**
    - Maintains high-quality data hygiene standards across the organization with automated, rule-based field population.

---

## Features
- **Automated Data Retrieval**
    - Uses the Composio Toolset to fetch missing contact information from verified external databases in real-time.
- **Seamless Kommo Integration**
    - Directly maps enriched data points to specific fields within your Kommo CRM account for instant availability.
- **Intelligent Field Mapping**
    - Configurable logic that determines which contact or company attributes require enrichment based on your specific business rules.
- **Real-time Sync Engine**
    - Triggers enrichment workflows the moment a new contact is created or updated, ensuring no lead remains incomplete.
- **Error Handling & Validation**
    - Built-in checks to ensure that only accurate, formatted data is pushed to your CRM, preventing data corruption.

---

## Use Cases
**Lead Qualification & Routing**
- Automatically append job titles and company sizes to new leads to facilitate faster lead scoring.
- Populate missing email addresses or phone numbers for inbound inquiries to ensure immediate follow-up capability.

**Sales Pipeline Maintenance**
- Refresh stale contact records with updated professional information to keep your outreach relevant.
- Sync LinkedIn profile URLs or company industry tags directly into Kommo to provide context for sales calls.

**Data Hygiene & Compliance**
- Standardize contact formatting across your database to ensure consistent reporting and segmentation.
- Identify and fill gaps in critical contact fields to ensure your CRM remains a single source of truth for the entire team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Launch" link above to open the solution in the Uplizd builder.
2. Connect your Kommo account via the Composio Toolset node.
3. Configure your preferred LLM in the Agent node to handle data parsing.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request for contact enrichment.
- **Agent**: Processes the request and determines which data fields are missing or require updates.
- **Composio Toolset**: Executes the API calls to fetch external data and push updates to Kommo.
- **Chat Output**: Confirms the successful enrichment and provides a summary of updated fields.

### 3) Run the Flow
Use the Playground to test your enrichment logic:
- `Enrich the contact record for john.doe@example.com in Kommo.`
- `Find and update the company website and industry for the latest leads.`
- `Check for missing phone numbers in my 'New Leads' pipeline and enrich them.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your data enrichment logic.
- Set the system prompt to prioritize accuracy and data formatting.
- Instruct the agent to only update fields that are currently empty or outdated.
- Enable tool-calling capabilities to allow the agent to interact with the Composio Toolset.

### 2) Composio Toolset Node
- Provide your Kommo API credentials to establish a secure connection.
- Define the scope to allow read/write access to contact and company objects.

### 3) Tool Availability
- **Kommo API**: For reading existing records and performing bulk updates.
- **Data Enrichment APIs**: Integrated via Composio to fetch professional contact details.
- **Validation Logic**: Custom scripts to ensure data conforms to your CRM's specific field requirements.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain multi-platform synchronization for your CRM records.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean and standardize your CRM data at scale.
- [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Engage enriched leads directly through automated messaging.
