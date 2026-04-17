# Proposal Generator (Uplizd) - Automate professional business proposal creation from PDF data

## Summary
The Proposal Generator by PDF API IO is an intelligent Uplizd workflow designed to streamline the creation of high-conversion business documents. By extracting key data points from existing templates and external inputs, this solution automates the drafting process, ensuring consistent branding, accurate pricing, and faster turnaround times for sales and operations teams.

---

## Demo
![Proposal Generator workflow interface showing PDF data extraction and document assembly](image.png)
**Alt text (SEO-ready):** Proposal Generator workflow by Uplizd, automating PDF document creation, sales proposal drafting, and data extraction using Composio and AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/05485c2c-324f-5893-a084-c237d9be5926)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** `proposal generation`, `pdf automation`, `sales operations`, `document workflow`, `composio`, `ai drafting`, `crm integration`  
This solution bridges the gap between raw data and polished client-facing documents, reducing manual administrative overhead in the sales cycle.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual document formatting and accelerate the deal-closing process.

*   **Sales Representatives**
    *   Generate custom proposals in seconds rather than hours, allowing more time for client interaction.
*   **Account Managers**
    *   Maintain brand consistency across all client communications with standardized, AI-verified templates.
*   **Sales Operations Managers**
    *   Standardize the proposal pipeline to ensure all documents follow company pricing and legal guidelines.
*   **Freelancers & Consultants**
    *   Automate administrative tasks to focus on high-value project delivery and client strategy.

---

## Features
- **Intelligent PDF Extraction**
    Leverages PDF API IO to pull structured data from existing templates, ensuring accuracy in every document.
- **Dynamic Content Assembly**
    Uses the Agent node to intelligently insert client-specific details, pricing, and scope of work into your templates.
- **Composio Toolset Integration**
    Seamlessly connects with your existing CRM and storage tools to pull client data and save generated proposals automatically.
- **Real-time Formatting**
    Ensures that all generated output adheres to predefined visual styles and professional business standards.
- **Automated Workflow Triggers**
    Reduces manual intervention by triggering the generation process based on specific CRM deal stages or status updates.

---

## Use Cases
**Sales Pipeline Acceleration**
*   Automatically generate a professional proposal as soon as a deal moves to the "Qualified" stage in your CRM.
*   Sync generated PDFs directly to the client's folder in your cloud storage for immediate access.

**Standardized Client Onboarding**
*   Draft custom service agreements by pulling client information from your CRM and merging it with standard legal templates.
*   Ensure all proposals include the latest pricing tiers by fetching real-time data via the Composio Toolset.

**Administrative Efficiency**
*   Reduce time spent on repetitive document creation by using AI to populate placeholders in complex PDF templates.
*   Enable bulk proposal generation for recurring contract renewals, ensuring accuracy across multiple accounts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to load the pre-configured workflow into your Uplizd workspace.
3. Connect your required API credentials (PDF API IO and CRM integrations) within the settings panel.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the client name, deal ID, and specific service requirements.
*   **Agent**: Processes the input, fetches data, and instructs the document generation engine.
*   **Composio Toolset**: Executes the API calls to extract data and generate the final PDF document.
*   **Chat Output**: Confirms the successful generation and provides a download link or file path.

### 3) Run the Flow
Use the Playground to test your proposal generation:
*   `Generate a proposal for Acme Corp using the standard service template.`
*   `Create a custom proposal for Project Alpha with a 15% discount applied to the total.`
*   `Draft a renewal agreement for client ID 9982 based on the Q3 pricing structure.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data mapping and document logic.
*   **Instruction Pattern**: 
    *   "Extract client details from the provided CRM data."
    *   "Map extracted variables to the corresponding fields in the PDF template."
    *   "Verify that all pricing and legal clauses match the current company policy."

### 2) Composio Toolset Node
Requires a valid API key for PDF API IO and your target CRM (e.g., Salesforce or HubSpot). Ensure the connection scope includes read/write access to document and contact objects.

### 3) Tool Availability
*   **Data Extraction**: Capability to parse and read PDF templates.
*   **Document Assembly**: Capability to merge variables into PDF placeholders.
*   **CRM Sync**: Capability to retrieve client data and update deal records with the generated file link.

---

## Related Solutions
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather deep intelligence on accounts before generating proposals.
*   [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the creation of new client records in your CRM.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage the lifecycle of deals that require proposal generation.
