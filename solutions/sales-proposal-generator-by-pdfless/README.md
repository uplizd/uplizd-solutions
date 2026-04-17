# Sales Proposal Generator (Uplizd) - Automate high-conversion sales documents from CRM data

## Summary
The Sales Proposal Generator is an intelligent Uplizd workflow that bridges the gap between CRM opportunity data and professional document creation. By leveraging the Composio Toolset, the agent extracts key deal details, pricing, and client requirements to draft tailored proposals, significantly reducing manual administrative overhead and accelerating the sales cycle for revenue teams.

---

## Demo
![Sales Proposal Generator workflow interface showing data extraction from CRM to document generation](image.png)
**Alt text (SEO-ready):** Sales Proposal Generator Uplizd workflow, CRM data integration, automated proposal creation, sales pipeline acceleration, Composio AI agent.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/09fc2ca2-9654-5d29-b7f3-4e6115b9e858)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, salesforce, proposal generation, document automation, revops, ai workflow, composio, pipeline velocity
- This solution streamlines the transition from opportunity identification to formal proposal delivery by automating document drafting directly from your CRM data.

---

## Who is this for?
This solution is designed for sales and operations professionals looking to eliminate manual document drafting and ensure consistent messaging across all client communications.

- **Account Executive**
    - Spend less time on administrative document creation and more time on high-value client interactions.
- **Sales Operations Manager**
    - Standardize proposal templates and ensure all client-facing documents align with current CRM data.
- **Business Development Representative**
    - Quickly generate professional follow-up materials for qualified leads to maintain momentum in the pipeline.
- **Revenue Operations Lead**
    - Improve pipeline velocity by removing bottlenecks in the quote-to-close process through automated data mapping.

---

## Features
- **CRM Data Integration**
    - Seamlessly pulls opportunity details, contact information, and product pricing directly from your CRM via the Composio Toolset.
- **Intelligent Drafting**
    - Uses advanced LLMs to synthesize deal context into persuasive, professional proposal language tailored to the prospect.
- **Dynamic Template Mapping**
    - Automatically populates predefined document templates with specific deal variables, ensuring brand consistency and accuracy.
- **Real-time Updates**
    - Syncs proposal status and generated document links back to the CRM, maintaining a single source of truth for the sales team.
- **Customizable Tone Control**
    - Allows users to adjust the formality and style of the proposal to match the specific industry or client relationship.

---

## Use Cases
**Standardizing Sales Collateral**
- Automatically generate standardized SOWs (Statements of Work) based on selected product bundles in the CRM.
- Ensure all proposals include the latest pricing and discount terms without manual verification.

**Accelerating Deal Velocity**
- Draft initial proposal versions immediately after a discovery call to keep the prospect engaged.
- Reduce the time between verbal agreement and document delivery from days to minutes.

**Improving Data Hygiene**
- Enforce consistent data entry by requiring specific fields in the CRM to be populated before the proposal generator can trigger.
- Eliminate copy-paste errors by pulling client and project data directly from the source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and navigate to the "Templates" library.
2. Search for "Sales Proposal Generator" and click "Import Flow."
3. Configure your API credentials for your CRM and document storage provider.
4. Ensure nodes are correctly connected in the canvas, verifying the flow from input to output.

### 2) Setup the Nodes
- **Chat Input**: Receives the Opportunity ID or client name from the user.
- **Agent**: Analyzes the request and determines which CRM data points are required.
- **Composio Toolset**: Executes the retrieval of CRM records and triggers the document generation service.
- **Chat Output**: Returns the link to the generated proposal or a summary of the drafted content.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Generate a proposal for the Acme Corp opportunity based on the latest deal data.`
- `Draft a follow-up proposal for the pending deal in the Enterprise segment.`
- `Create a summary proposal for the current open opportunity for TechFlow Inc.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data extraction and document synthesis.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data mapping.
- Instruction: "Extract opportunity details, map them to the proposal template, and ensure all pricing matches the CRM records."
- Instruction: "Maintain a professional and persuasive tone throughout the document."

### 2) Composio Toolset Node
- Provide your CRM API key and ensure the connection scope includes read access to Opportunities, Accounts, and Products.

### 3) Tool Availability
- **CRM Connector**: For fetching deal-specific data.
- **Document Service**: For rendering and saving the final proposal file.
- **Notification Tool**: For alerting the user once the proposal is ready for review.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on prospects before generating proposals.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track the status of deals as they move through the sales funnel.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensure your CRM data remains consistent across all integrated platforms.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather real-time account signals to enrich your sales proposals.
