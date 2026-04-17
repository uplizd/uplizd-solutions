# Smart Proposal Generator (Uplizd) - Automated CRM-driven document creation

## Summary
The Smart Proposal Generator is an intelligent Uplizd workflow that bridges the gap between CRM opportunity data and professional documentation. By leveraging the Composio Toolset to interface with PandaDoc, this solution automatically pulls deal details, customizes proposal templates, and generates ready-to-send documents, significantly reducing manual administrative overhead and accelerating the sales cycle for revenue teams.

---

## Demo
![Smart Proposal Generator workflow dashboard showing CRM data integration and PandaDoc document generation](image.png)
**Alt text (SEO-ready):** Smart Proposal Generator Uplizd workflow, automated CRM proposal creation, PandaDoc integration, and sales document automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/6627ab89-ae5e-5b6f-b58a-dd25423a5c9e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, pandadoc, proposal generation, sales operations, document automation, composio, ai workflow, revenue operations
- This solution streamlines the transition from lead qualification to contract delivery by automating document generation directly from your CRM pipeline.

---

## Who is this for?
This solution is designed for high-velocity sales and operations teams looking to eliminate manual document drafting.

- **Account Executives**
    - Spend less time on administrative document preparation and more time closing deals.
- **Sales Operations Managers**
    - Ensure brand consistency and pricing accuracy across all outbound sales proposals.
- **Revenue Operations (RevOps) Leads**
    - Standardize the proposal generation process to improve pipeline velocity and data hygiene.
- **Customer Success Managers**
    - Quickly generate renewal or expansion agreements with pre-populated customer usage data.

---

## Features
- **CRM Data Mapping**
    - Automatically extracts key opportunity fields like deal value, contact names, and service terms from your CRM.
- **Template Personalization**
    - Dynamically injects CRM data into pre-approved PandaDoc templates to ensure every proposal is tailored.
- **Real-time Document Creation**
    - Triggers the creation of new documents in PandaDoc the moment an opportunity reaches a specific stage.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to maintain secure, authenticated connections between your CRM and document platforms.
- **Automated Status Tracking**
    - Updates the CRM opportunity status automatically once the proposal is generated or sent to the client.

---

## Use Cases
**Sales Pipeline Acceleration**
- Automatically generate a quote when an opportunity moves to the "Proposal Sent" stage.
- Populate custom pricing tables based on specific SKU data stored in the CRM.

**Standardized Document Hygiene**
- Ensure all proposals follow the latest legal and branding guidelines by using locked templates.
- Eliminate manual copy-paste errors by pulling client contact information directly from the CRM record.

**Expansion and Renewal Management**
- Generate expansion proposals for existing accounts based on current usage metrics.
- Create renewal contracts automatically 30 days before a subscription expiration date.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Smart Proposal Generator solution.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your CRM and PandaDoc accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM custom fields and template IDs.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to generate a proposal for a specific Opportunity ID.
- **Agent**: Processes the request, fetches CRM data, and formats the information for the document template.
- **Composio Toolset**: Executes the API calls to PandaDoc to create and populate the document.
- **Chat Output**: Confirms the document creation and provides a direct link to the generated proposal.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Generate a proposal for Opportunity ID: 98765 using the Standard Service Agreement template.`
- `Create a renewal proposal for client Acme Corp based on their current CRM data.`
- `Draft a custom quote for the high-priority deal associated with contact John Doe.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your data and the document engine.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruction: "Extract opportunity details from the CRM, map them to the corresponding PandaDoc template placeholders, and trigger the document creation tool."
- Ensure the agent is instructed to verify that all required fields are present before initiating the document generation.

### 2) Composio Toolset Node
- Provide your unique API key to authorize the Composio Toolset.
- Ensure the connection scope includes read access for your CRM and write/create access for PandaDoc.

### 3) Tool Availability
- **CRM Connector**: For fetching opportunity, contact, and account data.
- **PandaDoc API**: For template retrieval, document creation, and status updates.
- **Data Formatter**: For cleaning and normalizing CRM strings before template injection.

---

## Related Solutions
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage complex account hierarchies and relationship mapping.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Track and optimize deal stages and pipeline velocity.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather deep intelligence on prospects to inform proposal content.
