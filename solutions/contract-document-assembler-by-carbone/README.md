# Contract Document Assembler (Uplizd) - Automated legal document generation from deal data

## Summary
The Contract Document Assembler by Carbone is an intelligent Uplizd workflow that automates the creation of customized legal agreements and contracts by pulling real-time deal data from your CRM. By streamlining the document generation process, this solution eliminates manual drafting errors, ensures template consistency, and accelerates the sales-to-contract pipeline velocity for legal and operations teams.

---

## Demo
![Contract Document Assembler workflow interface showing data mapping from CRM to Carbone templates](image.png)
**Alt text (SEO-ready):** Uplizd Contract Document Assembler workflow, automated legal document generation, CRM data integration, Carbone template processing, and sales pipeline automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2f68dc18-7700-5df4-b4c9-40fe85ec63c9)

---

## Category
**Primary category:** Legal Operations
**Secondary tags:** `document automation`, `carbone`, `crm`, `salesforce`, `contract management`, `data sync`, `composio`, `ai workflow`

This solution bridges the gap between CRM opportunity data and professional document generation, serving as a critical tool for automated legal and sales documentation.

---

## Who is this for?
This solution is designed for professionals who manage high-volume contract workflows and require precision in document assembly.

- **Sales Operations Manager**
    - Ensures that every contract generated reflects the most current deal terms and pricing, reducing administrative overhead.
- **Legal Counsel**
    - Maintains compliance by using standardized, pre-approved templates while allowing for dynamic data insertion.
- **Account Executive**
    - Accelerates the closing process by generating professional, error-free agreements instantly from the opportunity record.
- **RevOps Specialist**
    - Standardizes the documentation lifecycle by integrating data directly from the CRM into the final contract output.

---

## Features
- **Dynamic Data Mapping**
    - Automatically maps CRM fields like client name, deal value, and service terms directly into your Carbone templates.
- **Template Version Control**
    - Ensures that the latest approved legal language is used for every document generated, maintaining organizational compliance.
- **Real-time CRM Integration**
    - Leverages the Composio Toolset to fetch live opportunity data, ensuring no manual data entry is required during assembly.
- **Automated Document Delivery**
    - Triggers the generation process instantly, allowing for rapid turnaround from verbal agreement to signed contract.
- **Error Reduction Engine**
    - Eliminates human error in contract drafting by automating the population of complex legal clauses and variable data.

---

## Use Cases
**Contract Lifecycle Management**
- Generating Master Service Agreements (MSAs) based on specific deal parameters.
- Creating Statements of Work (SOWs) that automatically reflect the scope defined in the CRM.

**Sales Velocity Optimization**
- Reducing the time between opportunity qualification and document delivery to under 60 seconds.
- Automating the creation of renewal contracts for existing accounts to improve retention workflows.

**Legal Compliance & Hygiene**
- Ensuring all generated contracts contain mandatory legal disclaimers based on the client's region.
- Auditing document generation history to maintain a clear trail of which deal data informed each contract.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `contract-document-assembler` JSON configuration.
3. Connect your CRM and Carbone accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger to generate a document for a specific deal ID.
- **Agent**: Interprets the request and orchestrates the data retrieval and template population.
- **Composio Toolset**: Executes the API calls to fetch CRM data and trigger the Carbone generation engine.
- **Chat Output**: Returns the link to the finalized document or confirms the generation status.

### 3) Run the Flow
Use the Playground to test the assembly process with these prompts:
- `Generate a new MSA for Deal ID 98765 using the standard template.`
- `Create a Statement of Work for the current opportunity in the enterprise tier.`
- `Draft a renewal agreement for the account linked to Deal ID 44321.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your data sources and the document engine.
- Use a model capable of high-precision instruction following.
- **Recommended instruction pattern:**
    - "Extract all relevant deal parameters from the provided CRM data."
    - "Map the extracted variables to the corresponding fields in the Carbone template."
    - "Verify that all mandatory legal fields are populated before finalizing the document."

### 2) Composio Toolset Node
- **API Key**: Ensure your CRM and Carbone API keys are securely stored in the Composio environment.
- **Connection Scope**: Grant read-access to your CRM opportunity objects and write-access to the Carbone document generation service.

### 3) Tool Availability
- **CRM Connector**: For fetching deal-specific metadata.
- **Carbone Engine**: For rendering templates with dynamic data.
- **Notification Service**: For alerting the user once the document is ready for review.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into accounts to prepare for contract negotiations.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Streamline the creation of new CRM records to feed into your document assembly workflows.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage the stages of your deals to ensure documents are generated at the right time.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean your CRM data before assembly to ensure contracts are generated with accurate information.
