# Legal Document Curator (Uplizd) - Intelligent compliance tracking and document lifecycle management

## Summary
The Legal Document Curator is an automated AI workflow designed to streamline the organization, review, and compliance monitoring of legal documentation. By leveraging the Composio Toolset to interface with document repositories and legal databases, this solution provides a single source of truth for legal teams, reducing manual filing errors and accelerating pipeline velocity for contract reviews and regulatory audits.

---

## Demo
![Legal Document Curator dashboard showing automated document classification and compliance status tracking](image.png)
**Alt text (SEO-ready):** Legal Document Curator Uplizd workflow, automated document classification, compliance tracking, and legal document management with Composio integrations.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/db29d84a-9355-56ba-8be9-67c898ed6cd9)

---

## Category
**Primary category**: Legal operations
**Secondary tags**: compliance, document management, legal tech, automation, data hygiene, composio, ai workflow, audit readiness.
This solution bridges the gap between unstructured legal documentation and structured compliance reporting through intelligent AI-driven classification.

---

## Who is this for?
This solution is designed for legal and operations teams managing high volumes of sensitive documentation and regulatory requirements.

* **General Counsel**
    * Ensures company-wide adherence to regulatory standards through automated document auditing.
* **Legal Operations Manager**
    * Reduces administrative overhead by automating the categorization and filing of incoming legal contracts.
* **Compliance Officer**
    * Maintains a real-time, searchable audit trail of all legal documents and their current status.
* **Contract Administrator**
    * Accelerates the contract lifecycle by identifying pending actions and expiration dates automatically.

---

## Features
- **Automated Document Classification**
    Uses AI to identify document types, such as NDAs, MSAs, or employment agreements, and routes them to the appropriate folder.
- **Compliance Status Monitoring**
    Real-time tracking of document expiration dates and renewal requirements to ensure continuous regulatory compliance.
- **Intelligent Metadata Extraction**
    Automatically pulls key terms, dates, and parties from unstructured text to populate your document management system.
- **Cross-Platform Integration**
    Leverages the Composio Toolset to sync document metadata across cloud storage providers and legal databases.
- **Audit-Ready Reporting**
    Generates summary reports of document status, highlighting potential risks or missing documentation for upcoming audits.

---

## Use Cases
**Contract Lifecycle Management**
* Automating the renewal notification process for expiring vendor contracts.
* Extracting signature dates and effective dates to update internal CRM records.

**Regulatory Compliance Audits**
* Flagging missing mandatory clauses in standard service agreements.
* Organizing historical documents by fiscal year and regulatory category for rapid retrieval.

**Legal Operations Efficiency**
* Automatically renaming and filing documents based on extracted entity names.
* Routing urgent legal requests to the appropriate counsel based on document priority tags.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Legal Document Curator template from the solution gallery.
3. Connect your preferred document storage and legal database accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives document metadata or user queries regarding specific legal files.
* **Agent**: Analyzes the document content and determines the required compliance or classification action.
* **Composio Toolset**: Executes file operations, updates database records, and fetches external legal data.
* **Chat Output**: Returns the status update, classification confirmation, or audit summary to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Classify the uploaded document and extract the expiration date.`
* `List all contracts that are expiring in the next 30 days.`
* `Check if the new MSA contains the standard liability clause and flag if missing.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the legal operations assistant, focusing on precision and compliance.
* Set the system prompt to prioritize accuracy in legal terminology.
* Configure the agent to output structured JSON for database updates.
* Enable "Chain of Thought" reasoning to ensure complex contract clauses are interpreted correctly.

### 2) Composio Toolset Node
* Provide your API key for the relevant document storage provider (e.g., Google Drive, SharePoint).
* Set the connection scope to "Read/Write" to allow the agent to move and rename files.

### 3) Tool Availability
* **File Search**: Locate documents across your repository.
* **Metadata Update**: Modify tags and properties of stored files.
* **Database Query**: Fetch current contract status from your legal database.
* **Notification Service**: Alert legal staff via email or Slack when a document requires review.

---

## Related Solutions
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Ensures customer account data meets regulatory and internal standards.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Manages and resolves pending tasks derived from legal and operational meetings.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the creation of new client records and associated legal documentation.
