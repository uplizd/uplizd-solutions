# Contact Enrichment Agent (Uplizd) - Automate CRM profile data enrichment and lead intelligence

## Summary
The Contact Enrichment Agent is an intelligent automation workflow designed to eliminate manual data entry by automatically populating missing contact details within your CRM. By leveraging the Composio Toolset to query external intelligence platforms, this solution ensures your sales and marketing teams have a single source of truth, significantly improving pipeline velocity and data hygiene for every lead.

---

## Demo
![Contact Enrichment Agent workflow showing automated data population from Folk CRM to external intelligence sources](image.png)
**Alt text (SEO-ready):** Contact Enrichment Agent workflow by Uplizd for automated CRM data synchronization, lead intelligence, and pipeline hygiene using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a2a988f7-35b4-5ec0-a131-f0b7a37dccbf)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, folk, data enrichment, lead intelligence, sales operations, data hygiene, composio, ai workflow
- This solution streamlines the lead qualification process by ensuring that every contact record in your CRM is automatically enriched with the latest professional data.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual research time and improve data accuracy across their sales stack.

- **Sales Development Representative (SDR)**
    - Spend less time manually searching for contact details and more time engaging with qualified leads.
- **Revenue Operations Manager**
    - Maintain high-quality CRM data hygiene by automating the backfilling of missing professional attributes.
- **Account Executive**
    - Access comprehensive lead intelligence directly within the CRM to personalize outreach and shorten sales cycles.
- **Marketing Operations Specialist**
    - Ensure lead scoring models are based on complete, accurate data by automating the enrichment of incoming contact records.

---

## Features
- **Automated Data Retrieval**
  Leverages the Composio Toolset to fetch real-time professional data from external intelligence providers.
- **CRM Integration**
  Seamlessly connects with Folk CRM to read contact records and write enriched data back to the appropriate fields.
- **Intelligent Field Mapping**
  Automatically identifies missing data points such as job titles, company size, or industry and populates them accurately.
- **Real-time Processing**
  Triggers enrichment workflows the moment a new contact is added or updated, ensuring data is always current.
- **Customizable Logic**
  Allows users to define specific enrichment rules and priority fields to match unique organizational requirements.

---

## Use Cases
**Lead Qualification**
- Automatically append company revenue and employee count to new leads to prioritize high-value accounts.
- Flag contacts missing critical decision-maker attributes for immediate manual review by the sales team.

**Data Hygiene Maintenance**
- Periodically scan existing CRM records to update outdated job titles or company information.
- Standardize contact formatting across the database to ensure consistent reporting and segmentation.

**Outreach Personalization**
- Inject enriched company insights into sales sequences to create highly tailored cold outreach messages.
- Use enriched industry data to route leads to the correct specialized sales representative.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace and project destination.
3. Authenticate your CRM and intelligence provider connections via the Composio dashboard.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request to enrich a specific contact.
- **Agent**: Processes the request, identifies missing fields, and orchestrates the enrichment logic.
- **Composio Toolset**: Executes secure API calls to fetch and update data within the CRM.
- **Chat Output**: Confirms the successful enrichment or logs any data discrepancies for the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Enrich the contact record for [Name] at [Company] with the latest job title and company size.`
- `Scan my recent leads in Folk and fill in any missing industry information.`
- `Update the profile for [Email Address] with current professional data from available intelligence sources.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence layer, interpreting data requirements and managing tool execution.
- **Instruction Pattern**:
    - "Identify missing fields in the provided CRM contact object."
    - "Query the Composio Toolset to retrieve the most accurate professional data."
    - "Update the CRM record only if the retrieved data is more current than existing information."

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is configured with read/write access to your CRM and enrichment tools.
- **Connection Scope**: Grant the agent permission to access contact objects and perform bulk updates.

### 3) Tool Availability
- **CRM Connector**: Read/Write access to contact and company objects.
- **Intelligence Provider**: Read access to professional profile databases.
- **Data Validator**: Logic to verify data format before writing to the CRM.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate the collection of deep account insights for better targeting.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Streamline account-level research to support complex sales cycles.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean and compliant CRM databases through automated cleanup.
