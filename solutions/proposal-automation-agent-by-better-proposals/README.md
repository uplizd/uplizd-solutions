# Proposal Automation Agent (Uplizd) - Streamline document generation and sales outreach

## Summary
The Proposal Automation Agent by Better Proposals leverages Uplizd AI workflows to transform raw CRM data into professional, high-converting sales proposals. By automating the drafting and delivery process, this solution eliminates manual document creation, reduces administrative overhead for sales teams, and ensures consistent brand messaging across every client interaction.

---

## Demo
![Proposal Automation Agent workflow interface showing CRM data integration and document generation](image.png)
**Alt text (SEO-ready):** Uplizd Proposal Automation Agent workflow for Better Proposals, showing CRM data integration, automated document generation, and sales pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFR0Wq57o5wAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAkSURBVHjaY2AYBaNgFIyCUUAHAAEEAEEAEEAEEAEEAEEAEAAA)](https://uplizd.ai/solutions/5241e9f4-824b-5603-aeff-83d41b895099)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, better proposals, document automation, sales operations, proposal management, ai workflow, composio, lead conversion
- This solution bridges the gap between customer relationship management and document delivery, optimizing the sales cycle through intelligent automation.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach without sacrificing quality.

- **Sales Representatives**
    - Spend less time on administrative document drafting and more time closing deals.
- **Sales Operations Managers**
    - Standardize proposal templates and ensure compliance across the entire sales organization.
- **Account Executives**
    - Accelerate the transition from lead qualification to proposal delivery with automated data mapping.
- **Growth Marketers**
    - Maintain brand consistency in every outbound document sent to prospective clients.

---

## Features
- **Automated Data Mapping**
    - Seamlessly pulls client details from your CRM to populate proposal fields, eliminating manual entry errors.
- **Dynamic Template Selection**
    - Automatically selects the appropriate proposal template based on deal size, industry, or product type.
- **Real-time Status Tracking**
    - Monitors proposal progress and updates your CRM pipeline automatically once a document is viewed or signed.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely connect with Better Proposals and your CRM for end-to-end workflow execution.
- **Intelligent Formatting**
    - Ensures all generated documents adhere to company branding guidelines and professional formatting standards.

---

## Use Cases
**Sales Pipeline Acceleration**
- Automatically trigger a proposal draft the moment a deal reaches the "Contract Sent" stage in your CRM.
- Sync client contact information from your CRM to the proposal recipient fields without manual copy-pasting.

**Standardized Outreach**
- Generate personalized proposals using pre-approved templates that reflect current pricing and service terms.
- Ensure all sales collateral is updated with the latest company information before it is sent to a prospect.

**Post-Proposal Analytics**
- Update CRM deal stages automatically based on document engagement signals like "Open" or "Signed."
- Log proposal activity in the CRM history to provide full visibility into the prospect's interaction with your documents.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Proposal Automation Agent template from the solution library.
3. Authenticate your Better Proposals and CRM accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or CRM deal ID to initiate the proposal generation.
- **Agent**: Processes the request, retrieves deal data, and instructs the toolset on which template to use.
- **Composio Toolset**: Executes the API calls to Better Proposals to create and send the document.
- **Chat Output**: Confirms successful document generation and provides a link to the created proposal.

### 3) Run the Flow
Use the Playground to test your automation with these prompts:
- `Generate a proposal for Deal ID 98765 using the Standard Service Agreement template.`
- `Create a new proposal for the client associated with Deal ID 4432 and notify the assigned account manager.`
- `Draft a follow-up proposal for the existing lead in the CRM with the latest pricing structure.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your CRM data and the document generation engine.
- Instruct the agent to prioritize accuracy in data mapping between CRM fields and proposal placeholders.
- Configure the agent to verify deal status before initiating any document creation.
- Set the tone of the agent to be professional and sales-oriented for all generated communications.

### 2) Composio Toolset Node
- Provide your **Better Proposals API Key** and **CRM API Credentials** within the Composio configuration.
- Define the connection scope to allow the agent to read deal information and write document status updates.

### 3) Tool Availability
- **CRM Connector**: For fetching client and deal-specific data.
- **Better Proposals API**: For template selection, document drafting, and delivery.
- **Notification Service**: To alert the sales team upon successful proposal delivery.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather deep intelligence on prospects before drafting proposals.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage deal stages and track progress alongside your proposal workflows.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the initial setup of new accounts in your CRM.
