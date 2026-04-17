# Sales Proposal Generator (Uplizd) - Automate branded RFP responses and sales documents

## Summary
The Sales Proposal Generator by Carbone is an intelligent Uplizd workflow designed to transform raw RFP data and prospect requirements into polished, branded sales documents. By leveraging the Composio Toolset to bridge document generation APIs with CRM data, this solution eliminates manual formatting, ensures brand consistency, and accelerates pipeline velocity for sales and operations teams.

---

## Demo
![Sales Proposal Generator workflow interface showing data mapping from CRM to Carbone document templates](image.png)
**Alt text (SEO-ready):** Sales Proposal Generator workflow by Uplizd, automating RFP responses and document creation via Composio and Carbone.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-390ceb73-blue)](https://uplizd.ai/solutions/390ceb73-b637-5a74-8409-45f40709c117)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** sales, proposal, carbone, document generation, rfp, crm, automation, composio, ai workflow
This solution streamlines the document generation lifecycle, turning complex sales requirements into professional, client-ready proposals.

---

## Who is this for?
This solution is designed for sales and operations professionals looking to reduce administrative overhead and improve proposal turnaround times.

* **Account Executive**
    * Generate custom, professional proposals in seconds rather than hours to beat competitors to the deal.
* **Sales Operations Manager**
    * Standardize brand identity across all outgoing documents by enforcing template-based generation.
* **Proposal Writer**
    * Automate the population of repetitive RFP fields using existing CRM data to focus on high-value content.
* **Solutions Consultant**
    * Quickly map technical requirements to proposal sections to ensure accuracy and alignment with prospect needs.

---

## Features
- **Automated Template Population**
    * Dynamically injects CRM data into Carbone templates, ensuring every proposal is personalized and accurate.
- **RFP Data Integration**
    * Seamlessly pulls prospect requirements and scope details directly into the generation pipeline via Composio.
- **Brand Consistency Engine**
    * Maintains strict adherence to corporate design guidelines and formatting standards across all generated documents.
- **Real-time Document Delivery**
    * Triggers document creation instantly upon request, allowing for rapid iteration during the sales cycle.
- **CRM-Centric Workflow**
    * Syncs generated proposal links back to the relevant CRM records for centralized tracking and auditability.

---

## Use Cases
**RFP Response Automation**
* Automatically populate complex RFP questionnaires with historical data and standard company responses.
* Generate a draft proposal document immediately after a discovery call summary is logged in the CRM.

**Sales Proposal Customization**
* Tailor pricing and service tiers in proposals based on specific prospect usage data or identified needs.
* Create localized versions of standard sales decks for international prospects using pre-defined language templates.

**Document Lifecycle Management**
* Maintain a searchable history of all generated proposals directly within the CRM account view.
* Automate the generation of follow-up documentation based on changes in deal stage or opportunity status.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your required CRM and Carbone accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API keys and template IDs.

### 2) Setup the Nodes
* **Chat Input**: Receives the prospect details, RFP requirements, or deal context from the user.
* **Agent**: Orchestrates the logic, extracting key data points and determining the appropriate template to use.
* **Composio Toolset**: Executes the document generation calls to Carbone and retrieves/updates CRM records.
* **Chat Output**: Delivers the final generated document link or status confirmation to the user.

### 3) Run the Flow
Use the Playground to test your proposal generation:
* `Generate a proposal for Acme Corp based on the latest RFP requirements in the CRM.`
* `Create a standard sales proposal using the Enterprise template for the current opportunity.`
* `Draft a technical scope document for the Q3 expansion project using the Carbone template.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for data mapping and template selection.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
* Instruction: "Analyze the input data, map it to the required fields in the Carbone template, and trigger the generation tool."
* Ensure the agent is instructed to verify that all mandatory fields are present before initiating the document creation.

### 2) Composio Toolset Node
* Provide your Carbone API key to enable document rendering.
* Ensure the connection scope includes read access to your CRM (e.g., Salesforce or HubSpot) to pull prospect data.

### 3) Tool Availability
* **Carbone API**: For rendering templates and generating final PDFs.
* **CRM Connector**: For fetching account, contact, and opportunity data.
* **Data Parser**: For cleaning and formatting raw input text into template-ready variables.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather deep intelligence on prospects to inform proposal content.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the creation of CRM records once a proposal is accepted.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Track the status of deals as proposals move through the sales cycle.
