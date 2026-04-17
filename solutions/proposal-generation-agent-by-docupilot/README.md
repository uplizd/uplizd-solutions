# Proposal Generation Agent (Uplizd) - Automate professional sales proposals from CRM data

## Summary
The Proposal Generation Agent streamlines the sales cycle by automatically transforming lead qualification data into polished, professional proposals. By integrating directly with your CRM and DocuPilot, this Uplizd workflow eliminates manual document drafting, ensures consistent branding, and accelerates pipeline velocity by reducing the time from qualification to contract delivery.

---

## Demo
![Proposal Generation Agent workflow diagram showing CRM data input to DocuPilot document creation](image.png)
**Alt text (SEO-ready):** Proposal Generation Agent workflow diagram showing CRM data input to DocuPilot document creation, automating sales documentation with Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/82df5d73-bf24-53c6-91c5-51a32410a523)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, docupilot, proposal generation, sales operations, document automation, pipeline velocity, composio, ai workflow
- This solution bridges the gap between CRM lead intelligence and document generation, enabling automated, data-driven proposal creation.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate administrative bottlenecks in the sales process.

- **Account Executives**
    - Spend less time on manual document formatting and more time on high-value client interactions.
- **Sales Operations Managers**
    - Standardize proposal templates across the organization to ensure brand compliance and data accuracy.
- **Business Development Representatives**
    - Quickly generate personalized proposals immediately following a successful lead qualification call.
- **Revenue Leaders**
    - Reduce the "quote-to-close" cycle time by automating the transition from opportunity to formal proposal.

---

## Features
- **Automated Data Mapping**
    - Seamlessly pulls lead details from your CRM and maps them directly into DocuPilot templates.
- **Dynamic Template Selection**
    - Automatically selects the appropriate proposal template based on the deal size, industry, or service tier.
- **Real-time CRM Integration**
    - Uses the Composio Toolset to fetch the latest lead status and contact info, ensuring proposals are always up-to-date.
- **Error-Free Document Drafting**
    - Eliminates human error in pricing, contact details, and service descriptions through automated field population.
- **Instant Delivery Readiness**
    - Prepares the final document for immediate review or automated email dispatch to the prospect.

---

## Use Cases
**Sales Pipeline Acceleration**
- Automatically generate a custom proposal as soon as an opportunity moves to the "Proposal Sent" stage in your CRM.
- Update existing proposals in real-time if deal parameters or pricing tiers change during negotiation.

**Standardized Sales Collateral**
- Ensure every proposal follows the latest company branding and legal terms by pulling from verified DocuPilot templates.
- Create multi-language proposals for international leads by triggering specific regional templates based on CRM location data.

**Administrative Efficiency**
- Reduce manual data entry by syncing lead qualification notes directly into the executive summary section of the proposal.
- Batch-generate proposals for multiple stakeholders within the same account to ensure consistent messaging.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Proposal Generation Agent.
2. Click "Import" to add the workflow to your workspace.
3. Configure your CRM and DocuPilot credentials within the integration settings.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all connections are active.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead ID or opportunity details from the user.
- **Agent**: Processes the request, retrieves CRM data, and instructs the document generator.
- **Composio Toolset**: Executes the API calls to fetch CRM data and trigger the DocuPilot document creation.
- **Chat Output**: Confirms the proposal generation status and provides a link to the document.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Generate a proposal for Lead ID 98765 using the Standard Enterprise template.`
- `Create a follow-up proposal for the Acme Corp opportunity based on our latest pricing.`
- `Draft a proposal for the current lead and send it to the primary contact email.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your CRM and the document generation engine.
- Use a high-reasoning model to ensure accurate data extraction from CRM fields.
- Instruct the agent to prioritize data integrity and template-specific formatting.
- Configure the agent to verify all required fields are present before triggering the document creation.

### 2) Composio Toolset Node
- Provide your API keys for both your CRM (e.g., Salesforce, HubSpot) and DocuPilot.
- Ensure the connection scope includes read access to CRM opportunities and write access to DocuPilot document services.

### 3) Tool Availability
- **CRM Connector**: Fetch lead, contact, and opportunity data.
- **DocuPilot Connector**: Populate templates and generate final PDF/Docx files.
- **Notification Service**: Optional trigger to email the generated proposal to the sales rep.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather deep intelligence on prospects before generating proposals.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage the lifecycle of opportunities from lead to closed-won.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent lead and opportunity data across your entire tech stack.
