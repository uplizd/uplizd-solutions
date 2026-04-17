# Deal Document Organizer (Uplizd) - Automated CRM Attachment Management

## Summary
The Deal Document Organizer by Zoho Bigin is an intelligent Uplizd workflow that automates the classification, renaming, and filing of sales collateral within your CRM. By leveraging AI to parse incoming files and map them to the correct deal records, this solution eliminates manual data entry, ensures document compliance, and accelerates pipeline velocity by providing a single source of truth for all deal-related assets.

---

## Demo
![Deal Document Organizer workflow showing file parsing and Zoho Bigin integration](image.png)
**Alt text (SEO-ready):** Deal Document Organizer Uplizd workflow for automated CRM file management, Zoho Bigin document parsing, and sales pipeline data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/deal-document-organizer-by-zoho-bigin)

---

## Category
**Primary category:** CRM data hygiene
**Secondary tags:** zoho bigin, document management, sales automation, file organization, pipeline velocity, data sync, ai workflow, composio
This solution streamlines CRM operations by automating the lifecycle of sales documents from ingestion to archival.

---

## Who is this for?
This workflow is designed for sales and operations teams looking to reduce administrative overhead and improve data accuracy.

* **Sales Operations Manager**
    * Ensures consistent file naming conventions and folder structures across the entire sales organization.
* **Account Executive**
    * Saves time by automatically attaching contracts and proposals to the correct deal without manual uploads.
* **Sales Enablement Lead**
    * Maintains a clean repository of high-performing sales collateral linked directly to opportunity records.
* **CRM Administrator**
    * Reduces data decay and storage clutter by enforcing automated document filing policies.

---

## Features
- **Intelligent File Parsing**
    Uses AI to extract metadata from incoming documents to identify the associated deal or contact.
- **Automated CRM Mapping**
    Directly integrates with the Composio Toolset to push files to the correct Zoho Bigin record.
- **Standardized Naming Logic**
    Automatically renames files based on deal stages, dates, or document types to ensure searchability.
- **Real-time Sync**
    Processes documents as they arrive, ensuring that the CRM is always up-to-date with the latest collateral.
- **Compliance & Hygiene**
    Flags missing or incorrectly formatted documents, maintaining high data quality standards within the CRM.

---

## Use Cases
**Contract Lifecycle Management**
* Automatically attaching signed NDAs to the corresponding deal record in Zoho Bigin.
* Renaming executed contracts with standard naming conventions (e.g., `DealName_Contract_Date`).

**Sales Proposal Handling**
* Filing custom proposal PDFs generated for prospects directly into the active opportunity folder.
* Updating the "Last Proposal Sent" field in the CRM based on the document upload event.

**Document Audit & Cleanup**
* Identifying and moving orphaned documents that are not linked to any active deal or contact.
* Archiving outdated collateral to keep the active deal workspace focused and organized.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the **Deal Document Organizer**.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Zoho Bigin account via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API keys are authorized in the configuration panel.

### 2) Setup the Nodes
* **Chat Input**: Receives the file or document link for processing.
* **Agent**: Analyzes the file content and determines the target deal record.
* **Composio Toolset**: Executes the file upload and metadata update in Zoho Bigin.
* **Chat Output**: Confirms successful filing or notifies the user of any parsing errors.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Process the latest invoice uploaded to the staging folder and attach it to the Acme Corp deal.`
* `Rename the document 'Q3_Proposal.pdf' and link it to the current active opportunity for John Doe.`
* `Audit the document folder for 'Project X' and ensure all files are correctly mapped to the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for document classification.
* Use a model with strong extraction capabilities (e.g., GPT-4o or Claude 3.5).
* Instruction: "Extract the deal ID and document type from the provided file metadata."
* Instruction: "If the deal ID is missing, search for the client name in Zoho Bigin to find the correct record."

### 2) Composio Toolset Node
* Provide your Zoho Bigin API key within the Composio dashboard.
* Ensure the connection scope includes `CRM.Modules.ALL` to allow file attachments and record updates.

### 3) Tool Availability
* `zoho_bigin_search_records`: Locate deals by name or ID.
* `zoho_bigin_upload_attachment`: Securely store files against a specific record.
* `zoho_bigin_update_record`: Update custom fields related to document status.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and stalled deals.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize multi-platform data and resolve conflicts.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting.
