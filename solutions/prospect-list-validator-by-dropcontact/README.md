# Prospect List Validator (Uplizd) - Automated lead verification and data hygiene

## Summary
The Prospect List Validator (Uplizd) AI workflow automates the verification and enrichment of prospect contact data, ensuring high-quality outreach lists. By leveraging the Composio Toolset to interface with Dropcontact, this solution eliminates manual data entry, reduces bounce rates for sales campaigns, and maintains a clean, actionable CRM database for revenue teams.

---

## Demo
![Prospect List Validator workflow showing input, Dropcontact verification, and output nodes](image.png)
**Alt text (SEO-ready):** Prospect List Validator workflow in Uplizd showing automated contact verification, data enrichment, and CRM integration via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/46e10630-99ab-560f-8331-fec36b2fcd7c)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** prospect, lead verification, dropcontact, data hygiene, crm, sales ops, lead enrichment, composio
- This solution streamlines the lead qualification process by validating contact information in real-time, ensuring your sales team focuses only on verified, high-intent prospects.

---

## Who is this for?
This workflow is designed for revenue-focused teams aiming to improve outreach efficiency and data accuracy.

- **Sales Development Representative (SDR)**
    - Ensures every lead in the sequence is verified, preventing wasted time on invalid contact details.
- **Revenue Operations (RevOps) Manager**
    - Maintains high data hygiene standards across the CRM by automating the cleanup of decayed contact lists.
- **Marketing Operations Specialist**
    - Increases campaign ROI by ensuring email deliverability through validated prospect data.
- **Growth Lead**
    - Accelerates pipeline velocity by feeding high-quality, enriched prospect data directly into the sales funnel.

---

## Features
- **Automated Verification**
    - Instantly validates email addresses and contact details using the Dropcontact API to prevent bounce-backs.
- **Real-time Data Enrichment**
    - Automatically appends missing professional information to existing records, providing a 360-degree view of the prospect.
- **Composio Toolset Integration**
    - Seamlessly connects the Uplizd agent to external CRM and verification tools for end-to-end workflow execution.
- **Bulk Processing Capability**
    - Handles large lists of prospects efficiently, reducing the manual burden of individual record checking.
- **Customizable Output Logic**
    - Configures how verified data is formatted and pushed back into your systems, ensuring compatibility with existing workflows.

---

## Use Cases
**Lead List Hygiene**
- Automatically flagging and removing invalid or outdated email addresses from cold outreach lists.
- Standardizing contact naming conventions and job titles to ensure consistent CRM reporting.

**Sales Outreach Optimization**
- Enriching inbound leads with professional data before they are routed to an Account Executive.
- Validating prospect contact information immediately after a form submission to ensure instant follow-up capability.

**CRM Data Maintenance**
- Periodic batch cleaning of stagnant CRM records to prevent data decay over time.
- Syncing verified prospect updates across multiple platforms to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Connect your Dropcontact and CRM credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect list or individual contact details for validation.
- **Agent**: Processes the data, triggers verification logic, and decides on the enrichment steps.
- **Composio Toolset**: Executes the specific Dropcontact API calls to verify and enrich the provided data.
- **Chat Output**: Returns the verified, cleaned, and enriched prospect information to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Verify the following email list for accuracy: [insert list]`
- `Enrich the contact data for this prospect: [insert name and company]`
- `Clean my current prospect list and remove all invalid entries`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data validation and enrichment tasks.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize accuracy and handle API errors gracefully.
- Configure the system prompt to output results in a clean, readable table format.

### 2) Composio Toolset Node
- Provide your Dropcontact API key within the Composio configuration.
- Set the connection scope to allow read/write access to your CRM and contact databases.

### 3) Tool Availability
- **Dropcontact Verification**: Validates email deliverability and contact existence.
- **Data Enrichment**: Fetches professional details like company size, industry, and social profiles.
- **CRM Connector**: Pushes the validated and enriched data back into your primary database.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Deep-dive research and intelligence gathering for target accounts.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for maintaining CRM data integrity and removing duplicates.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automated account research using ZoomInfo for high-value prospecting.
