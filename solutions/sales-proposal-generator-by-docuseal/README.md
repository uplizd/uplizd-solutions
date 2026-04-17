# Sales Proposal Generator (Uplizd) - Automate personalized document creation and delivery

## Summary
The Sales Proposal Generator is an intelligent Uplizd workflow that automates the creation, formatting, and delivery of professional sales proposals. By integrating LLM-driven content generation with DocuSeal, this solution eliminates manual drafting time, ensures brand consistency across all client communications, and accelerates the transition from lead qualification to contract signature.

---

## Demo
![Sales Proposal Generator workflow showing Chat Input, Agent, DocuSeal Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Uplizd Sales Proposal Generator workflow using DocuSeal for automated document creation, sales pipeline acceleration, and AI-driven proposal management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b37175fb-f628-5084-b98d-8d462ea9553a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, docuseal, proposal, automation, document generation, crm, composio, ai workflow
- This solution streamlines the document lifecycle by connecting AI agents directly to your e-signature infrastructure for faster deal closures.

---

## Who is this for?
This solution is designed for revenue teams looking to reduce administrative overhead and improve proposal turnaround times.

- **Account Executive**
    - Generate custom-tailored proposals in seconds without leaving the chat interface.
- **Sales Operations Manager**
    - Enforce standardized proposal templates and pricing structures across the entire sales team.
- **Customer Success Manager**
    - Quickly generate renewal contracts or service agreements to maintain account momentum.
- **Business Development Representative**
    - Accelerate the handoff process by automating the creation of initial engagement documents.

---

## Features
- **Automated Template Population**
    - Dynamically injects prospect data, pricing, and service terms into pre-approved DocuSeal templates.
- **AI-Powered Personalization**
    - Uses the Agent node to refine proposal language based on specific client needs and previous conversation context.
- **Real-Time E-Signature Integration**
    - Seamlessly triggers document dispatch via the Composio Toolset to ensure immediate delivery to the client.
- **Centralized Document Tracking**
    - Maintains a single source of truth for all generated proposals, linking them directly to the relevant CRM record.
- **Error-Free Data Mapping**
    - Eliminates manual copy-paste errors by pulling verified data directly from your connected business tools.

---

## Use Cases
**Standardized Sales Outreach**
- Automatically generate a standard proposal based on a prospect's selected service tier.
- Send personalized follow-up documents immediately after a discovery call concludes.

**Contract Lifecycle Management**
- Draft renewal agreements for existing clients based on historical usage data.
- Update terms and conditions dynamically within the proposal based on regional compliance requirements.

**Rapid Deal Acceleration**
- Create custom quotes for non-standard deals that require specific pricing adjustments.
- Dispatch urgent service agreements to prospects to capitalize on immediate buying intent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Sales Proposal Generator template from the solution library.
3. Connect your DocuSeal API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives prospect details and specific proposal requirements from the user.
- **Agent**: Processes input data and maps it to the appropriate DocuSeal template fields.
- **Composio Toolset**: Executes the API calls to generate and send the document via DocuSeal.
- **Chat Output**: Confirms successful document generation and provides a status update or link to the proposal.

### 3) Run the Flow
Use the Playground to test your proposal generation:
- `Generate a proposal for Acme Corp using the standard enterprise template with a 10% discount.`
- `Create a service agreement for John Doe at TechFlow Inc based on the Q3 pricing sheet.`
- `Draft a renewal proposal for Global Logistics, including the updated support addendum.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for document logic and template selection.
- **Instruction Pattern:**
    - Always verify the prospect's company name and service tier before initiating the DocuSeal call.
    - If data is missing, prompt the user for the specific pricing or term details.
    - Ensure the tone remains professional and aligned with your company's brand guidelines.

### 2) Composio Toolset Node
- **API Key**: Input your unique DocuSeal API key to authorize document creation.
- **Connection Scope**: Ensure the agent has 'write' access to your DocuSeal templates and 'send' permissions for document delivery.

### 3) Tool Availability
- **DocuSeal Template Fetcher**: Retrieves available templates for selection.
- **Document Generator**: Maps variables to template fields.
- **Signature Dispatcher**: Sends the final document to the recipient's email.

---

## Related Solutions
- [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) — Automate CRM account creation and data entry.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Track and manage sales opportunities through custom pipeline stages.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean and standardize CRM data to ensure accurate proposal generation.
