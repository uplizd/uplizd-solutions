# Account Intelligence Gatherer (Uplizd) - Automate B2B lead enrichment and account profiling

## Summary
The Account Intelligence Gatherer (Uplizd) is an automated AI workflow designed to streamline B2B sales research by pulling verified contact data and firmographic insights directly into your CRM. By leveraging the Dropcontact integration, this solution eliminates manual data entry, ensures lead accuracy, and accelerates pipeline velocity for sales and revenue operations teams.

---

## Demo
![Account Intelligence Gatherer workflow showing data flow from Chat Input to Dropcontact enrichment and CRM update](image.png)
**Alt text (SEO-ready):** Account Intelligence Gatherer Uplizd workflow, automated B2B lead enrichment, Dropcontact CRM integration, sales intelligence automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/9d88a48a-1ccc-5b2d-9a5f-d05028aeb19c)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, dropcontact, lead enrichment, sales intelligence, data hygiene, b2b, pipeline, composio
- This solution bridges the gap between raw lead lists and actionable account profiles by automating the verification and enrichment process.

---

## Who is this for?
This solution is built for revenue-focused teams looking to reduce manual research time and improve data quality.

- **Sales Development Reps (SDRs)**
    - Instantly verify lead contact information to ensure high-quality outreach.
- **Revenue Operations Managers**
    - Maintain a single source of truth for account data by automating enrichment pipelines.
- **Account Executives**
    - Access comprehensive account profiles before discovery calls to personalize the sales pitch.
- **Growth Marketers**
    - Segment target accounts based on accurate firmographic data retrieved during the enrichment process.

---

## Features
- **Automated Enrichment**
    - Uses the Composio Toolset to trigger real-time lookups via Dropcontact for verified email and phone data.
- **CRM Synchronization**
    - Seamlessly pushes enriched data fields back into your CRM, ensuring your database remains current and clean.
- **Intelligent Account Profiling**
    - Aggregates firmographic details to provide a holistic view of the target organization’s size, industry, and location.
- **Error Handling & Validation**
    - Automatically flags incomplete or invalid lead records for manual review to maintain high data hygiene standards.
- **Scalable Workflow Execution**
    - Processes bulk lead lists or individual entries with consistent logic, significantly reducing the time spent on manual research.

---

## Use Cases
**Lead Qualification**
- Enrich inbound leads with missing contact details to prioritize high-intent prospects.
- Verify professional email addresses to reduce bounce rates in automated email sequences.

**Account Research**
- Gather firmographic insights for target accounts to tailor outreach messaging effectively.
- Map out key stakeholders within an organization by pulling verified contact networks.

**Data Hygiene**
- Periodically scan existing CRM records to update outdated contact information and company details.
- Standardize lead formatting across the database to ensure consistent reporting and analytics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your preferred CRM and Dropcontact API credentials within the integration settings.
3. Configure the trigger settings to match your specific lead ingestion source.
4. Ensure nodes are properly linked from the **Chat Input** to the **Agent** and finally to the **Composio Toolset**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead name or company domain for processing.
- **Agent**: Orchestrates the logic, deciding when to call the enrichment tool based on the input.
- **Composio Toolset**: Executes the Dropcontact API calls to fetch and verify account data.
- **Chat Output**: Returns the enriched profile summary and confirms the update status.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Enrich the account profile for Acme Corp using their domain acme.com.`
- `Find and verify the contact information for the lead at tech-startup.io.`
- `Update the CRM record for the lead with the latest firmographic data from Dropcontact.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence, interpreting lead data and managing the tool execution flow.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to prioritize accuracy and verify the presence of required fields before updating the CRM.
- Set the agent to output a clear summary of the enrichment results for the user.

### 2) Composio Toolset Node
- Provide your active Dropcontact API key within the Composio configuration panel.
- Ensure the connection scope includes read/write permissions for your specific CRM (e.g., Salesforce or HubSpot).

### 3) Tool Availability
- **Dropcontact API**: For email verification, phone enrichment, and company data retrieval.
- **CRM Connector**: For pushing enriched data fields (e.g., `company_size`, `verified_email`) back into your system.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive account research and contact discovery.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms and ensure consistency.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and formatting of CRM lead data.
- [Account Expansion Identifier](../account-expansion-identifier-by-crustdata/README.md) - Identify upsell and cross-sell opportunities within existing accounts.
