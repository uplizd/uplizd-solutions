# Smart Proposal Generator (Uplizd) - Automate personalized sales proposals from CRM data

## Summary
The Smart Proposal Generator is an intelligent Uplizd workflow that bridges the gap between CRM opportunity data and professional document creation. By leveraging the Composio Toolset to interface with Bidsketch and your CRM, this solution automates the drafting of tailored proposals, ensuring high-velocity sales cycles and consistent brand messaging without manual copy-pasting.

---

## Demo
![Smart Proposal Generator workflow diagram showing CRM data integration with Bidsketch for automated document creation](image.png)
**Alt text (SEO-ready):** Smart Proposal Generator workflow for Uplizd, automating CRM to Bidsketch proposal creation, sales pipeline acceleration, and AI-driven document generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5f607d11-83d7-5b2a-8d66-9989841e9834)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, bidsketch, proposal generation, sales operations, pipeline velocity, ai workflow, document automation, composio

This solution streamlines the transition from lead qualification to formal proposal delivery by automating document generation directly from your CRM opportunity records.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce administrative overhead and accelerate the closing process.

- **Account Executives**
    - Spend less time on manual document drafting and more time on high-value client discovery.
- **Sales Operations Managers**
    - Standardize proposal templates and ensure all client-facing documents align with CRM data.
- **Business Development Representatives**
    - Quickly generate professional follow-up materials immediately after qualifying a new lead.
- **Revenue Operations Leads**
    - Improve pipeline velocity by removing manual bottlenecks in the proposal-to-contract phase.

---

## Features
- **CRM Data Integration**
    - Automatically pulls opportunity details, pricing, and client information from your CRM to populate proposal fields.
- **Bidsketch Automation**
    - Uses the Composio Toolset to trigger document creation in Bidsketch, eliminating manual entry errors.
- **Dynamic Template Mapping**
    - Selects the appropriate proposal template based on the deal size or industry tags defined in your CRM.
- **Real-time Status Updates**
    - Automatically updates the CRM opportunity stage once a proposal has been successfully generated.
- **AI-Driven Personalization**
    - The Agent node refines proposal language based on specific deal notes and historical client interactions.

---

## Use Cases
**Accelerated Sales Closing**
- Generate a full proposal within seconds of moving an opportunity to the "Proposal Sent" stage.
- Automatically include personalized executive summaries based on previous meeting transcripts.

**Standardized Brand Compliance**
- Ensure every proposal uses the latest approved pricing and legal terms from your Bidsketch library.
- Eliminate formatting inconsistencies by mapping CRM fields directly to verified document templates.

**Proactive Lead Nurturing**
- Create "lite" proposals or service summaries for early-stage leads to maintain momentum.
- Trigger automated follow-up tasks in the CRM immediately after a proposal is successfully generated.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the Smart Proposal Generator JSON file provided in this repository.
3. Connect your CRM and Bidsketch accounts via the Composio integration portal.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the CRM Opportunity ID or client name to initiate the request.
- **Agent**: Processes the CRM data and instructs the toolset on which proposal template to utilize.
- **Composio Toolset**: Executes the API calls to fetch CRM data and push the new document to Bidsketch.
- **Chat Output**: Confirms the successful generation of the proposal and provides a direct link to the document.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Generate a standard service proposal for Opportunity ID 98234.`
- `Create a custom enterprise proposal for Acme Corp using the 'Q3-Pricing' template.`
- `Draft a follow-up proposal for the current lead and save it to the 'Pending' folder in Bidsketch.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your CRM and the proposal platform.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Ensure the system prompt includes specific instructions on how to handle missing CRM fields.
- Configure the agent to prioritize accuracy in pricing and client contact information.

### 2) Composio Toolset Node
- Provide your unique API key via the Uplizd environment variables.
- Ensure the connection scope includes read access to your CRM and write access to Bidsketch.

### 3) Tool Availability
- **CRM Connector**: For fetching opportunity details and updating deal stages.
- **Bidsketch API**: For template retrieval, document creation, and status tracking.
- **Data Formatter**: For cleaning and mapping CRM strings into the required proposal format.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather deep intelligence on prospects before generating proposals.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Maintain overall pipeline health and stage hygiene.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensure data consistency across all sales platforms.
