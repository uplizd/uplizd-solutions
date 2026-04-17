# Contract Template Manager (Uplizd) - Automated legal document generation and clause customization

## Summary
The Contract Template Manager is an intelligent Uplizd workflow designed to streamline the creation and management of legal agreements. By leveraging the Composio Toolset to interface with Google Docs, this solution enables legal teams and operations managers to generate standardized contracts, inject dynamic clauses, and maintain document hygiene, significantly reducing manual drafting time and ensuring consistent legal language across the organization.

---

## Demo
![Contract Template Manager workflow interface showing Google Docs integration and clause injection nodes](image.png)
**Alt text (SEO-ready):** Contract Template Manager Uplizd workflow for automated Google Docs legal document generation and clause customization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/f1294bdf-2bbd-5966-91cb-a53b4cba7beb)

---

## Category
**Primary category:** Legal Operations
**Secondary tags:** google docs, document automation, contract management, legal tech, workflow automation, composio, ai drafting, compliance.
This solution bridges the gap between static legal templates and dynamic business requirements through automated document assembly.

---

## Who is this for?
This solution is built for professionals who manage high volumes of legal documentation and require precision at scale.

*   **Legal Counsel**
    *   Ensures all generated contracts adhere to current corporate compliance and risk standards.
*   **Operations Manager**
    *   Reduces the administrative burden of drafting recurring agreements like NDAs and service contracts.
*   **Sales Representative**
    *   Accelerates the deal cycle by instantly generating contract drafts tailored to specific client terms.
*   **HR Coordinator**
    *   Standardizes employment agreements and onboarding documentation with automated field population.

---

## Features
- **Dynamic Clause Injection**
  Automatically inserts specific legal clauses into templates based on deal parameters or counterparty requirements.
- **Google Docs Integration**
  Utilizes the Composio Toolset to create, edit, and format documents directly within the Google Workspace ecosystem.
- **Template Version Control**
  Maintains a single source of truth for master templates, preventing the use of outdated or non-compliant contract versions.
- **Automated Field Mapping**
  Populates placeholders (e.g., entity names, dates, currency) from CRM data or user input to eliminate manual data entry errors.
- **Compliance-Aware Drafting**
  Ensures that generated documents follow predefined legal guardrails, flagging deviations for human review before finalization.

---

## Use Cases
**Sales Contract Automation**
*   Generating customized Master Service Agreements (MSAs) based on selected pricing tiers.
*   Auto-populating client contact information and effective dates from CRM records into standard templates.

**HR & Employment Documentation**
*   Creating standardized offer letters that dynamically adjust based on department and seniority level.
*   Batch-generating contractor agreements with specific jurisdictional compliance clauses.

**Operational Document Hygiene**
*   Updating legacy contract templates with new liability language across a library of stored documents.
*   Creating audit-ready document trails by logging every generated contract in a centralized Google Drive folder.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `contract-template-manager-by-googledocs` JSON configuration.
3. Authenticate your Google Docs and Google Drive connections via the Composio Toolset.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives parameters such as contract type, counterparty name, and specific terms.
*   **Agent**: Processes the request, selects the appropriate template, and determines necessary clause modifications.
*   **Composio Toolset**: Executes the Google Docs API calls to create the document and inject variables.
*   **Chat Output**: Returns a link to the newly generated document and a summary of the applied clauses.

### 3) Run the Flow
Use the Playground to test your document generation:
*   `Generate a standard NDA for 'Acme Corp' with a 2-year non-solicitation clause.`
*   `Create a service agreement template for a new vendor in the 'Software' category.`
*   `Draft an employment contract for a new hire in the 'Engineering' department with standard benefits.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the legal drafting assistant, ensuring tone and accuracy.
*   Instruction: "You are a legal operations assistant. Always verify that the template ID matches the requested contract type."
*   Instruction: "Use the Composio Toolset to fetch the master template before applying any variable replacements."
*   Instruction: "If a requested clause is missing from the library, notify the user rather than hallucinating legal text."

### 2) Composio Toolset Node
*   **API Key**: Ensure your Google Workspace API key is active within the Composio dashboard.
*   **Connection Scope**: Grant `drive.file` and `documents` permissions to allow the agent to read templates and write new files.

### 3) Tool Availability
*   `google_docs_create_document`: Initializes a blank contract from a template ID.
*   `google_docs_replace_text`: Swaps placeholders with dynamic data.
*   `google_drive_list_files`: Locates the correct template folder.
*   `google_drive_save_file`: Exports the finalized document to the designated client folder.

---

## Related Solutions
*   [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the creation of new client records in Salesforce.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Ensures data used in contract generation is clean and standardized.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks the status of deals associated with generated contracts.
