# Client Proposal & Agreement Agent (Uplizd) - Automate document signing and contract workflows

## Summary
The Client Proposal & Agreement Agent streamlines the transition from sales proposal to legally binding contract by automating document generation and signature requests. Designed for service-based businesses and sales teams, this Uplizd workflow eliminates manual administrative bottlenecks, reduces turnaround time, and ensures a single source of truth for all client agreements, ultimately accelerating pipeline velocity and improving contract hygiene.

---

## Demo
![Client Proposal & Agreement Agent workflow screenshot showing document generation and SignWell integration](image.png)
**Alt text (SEO-ready):** Client Proposal and Agreement Agent workflow for automated document signing, featuring Uplizd, SignWell integration, and sales contract automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/d0935c65-c6af-5891-a4a3-a4675d695591)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, signwell, contract management, e-signature, sales operations, document automation, workflow, ai agent
- This solution bridges the gap between sales proposals and finalized agreements, providing a seamless automated bridge for RevOps and sales teams.

---

## Who is this for?
This agent is designed for teams looking to remove friction from the final stages of the sales cycle.

- **Account Executive**
    - Reduces administrative overhead by triggering signature requests directly from the CRM.
- **Sales Operations Manager**
    - Standardizes contract templates and ensures consistent data capture across all client agreements.
- **Customer Success Lead**
    - Accelerates the onboarding process by ensuring signed documents are processed and stored immediately.
- **Small Business Owner**
    - Eliminates the need for manual document tracking, allowing for faster deal closures and improved cash flow.

---

## Features
- **Automated Document Generation**
    - Dynamically populates contract templates with client data, ensuring accuracy and reducing manual entry errors.
- **Seamless E-Signature Integration**
    - Connects directly with SignWell to dispatch signature requests and monitor status in real-time.
- **Real-time Status Tracking**
    - Automatically updates the CRM or internal dashboard when a document is viewed, signed, or rejected.
- **Compliance-Aware Workflow**
    - Maintains an audit trail of all document interactions, ensuring that every agreement follows internal governance standards.
- **Intelligent Notification System**
    - Alerts the relevant stakeholders via the Chat Output node as soon as a client takes action on a proposal.

---

## Use Cases
**Contract Lifecycle Management**
- Automatically trigger a signature request the moment a proposal is marked as "Ready" in the CRM.
- Send automated follow-up reminders to clients who have not signed their agreements within 48 hours.

**Sales Operations Efficiency**
- Map custom fields from your CRM directly into the proposal template to ensure personalized, error-free contracts.
- Archive signed PDFs automatically into your cloud storage provider upon completion.

**Client Onboarding Acceleration**
- Trigger a welcome email sequence immediately after the SignWell webhook confirms a successful signature.
- Update the deal stage to "Closed-Won" automatically once the agreement is fully executed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Client Proposal & Agreement Agent template JSON file.
3. Connect your SignWell and CRM accounts within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or proposal data from the user.
- **Agent**: Interprets the intent and manages the logic for document preparation.
- **Composio Toolset**: Executes the API calls to SignWell and your CRM for document management.
- **Chat Output**: Confirms the action taken and provides a summary of the document status.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Generate a new agreement for the Acme Corp proposal and send it to the primary contact.`
- `What is the current signature status of the agreement for John Doe?`
- `Send a follow-up reminder for the pending contract associated with Opportunity ID 98765.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your document workflow.
- Instruction: You are a professional sales assistant focused on document management.
- Instruction: Always verify the client's email and document details before triggering a signature request.
- Instruction: Provide clear, concise updates on the status of all agreements handled through the Composio Toolset.

### 2) Composio Toolset Node
- Ensure your SignWell API key is active and the connection scope includes `documents.write` and `documents.read` permissions.

### 3) Tool Availability
- **SignWell API**: For document creation, signature requests, and status polling.
- **CRM Connector**: For fetching client contact details and updating deal stages.
- **Notification Service**: For sending internal alerts upon document completion.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on prospects before sending proposals.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Streamline the creation of new client records in Salesforce.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your client data consistent across multiple platforms during the sales process.
