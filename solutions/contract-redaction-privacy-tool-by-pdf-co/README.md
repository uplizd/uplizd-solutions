# Contract Redaction & Privacy Tool (Uplizd) - Automated PII masking for legal compliance

## Summary
The Contract Redaction & Privacy Tool is an intelligent Uplizd workflow designed to automate the identification and redaction of sensitive Personally Identifiable Information (PII) and confidential data within legal documents. By leveraging advanced AI agents and the Composio Toolset, this solution ensures data privacy, reduces manual review time, and maintains strict compliance with GDPR and CCPA standards, providing a single source of truth for document security.

---

## Demo
![Contract Redaction & Privacy Tool workflow showing document ingestion, AI-driven PII detection, and automated redaction output](image.png)
**Alt text (SEO-ready):** Contract Redaction & Privacy Tool by Uplizd, automated PII masking workflow, legal document compliance, AI-driven data redaction, Composio PDF.co integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e9043419-6f0d-59f9-a1ff-c3ed68c5d629)

---

## Category
- **Primary category:** Legal operations
- **Secondary tags:** `privacy`, `compliance`, `document processing`, `pii redaction`, `legal tech`, `composio`, `ai workflow`, `data security`
- This solution streamlines legal document hygiene by automating the removal of sensitive identifiers, ensuring organizations remain compliant while accelerating contract review cycles.

---

## Who is this for?
This solution is built for legal and operations teams managing high volumes of sensitive documentation.

- **Legal Counsel**
    - Ensures all outgoing contracts and filings are scrubbed of sensitive data to prevent privacy breaches.
- **Compliance Officer**
    - Maintains an automated audit trail of redacted documents to satisfy GDPR, CCPA, and internal security mandates.
- **Contract Administrator**
    - Eliminates the manual bottleneck of reviewing and blacking out PII in long-form legal agreements.
- **Data Privacy Manager**
    - Standardizes the redaction process across the enterprise to ensure consistent protection of client and employee information.

---

## Features
- **Automated PII Detection**
    - Uses AI to scan documents for names, social security numbers, addresses, and financial identifiers in real-time.
- **Intelligent Redaction Engine**
    - Applies permanent masking to identified sensitive fields while preserving the surrounding legal context.
- **Composio-Powered Integration**
    - Seamlessly connects with PDF.co and other document processing tools to handle complex file formats and layouts.
- **Compliance-Ready Output**
    - Generates sanitized versions of documents that are ready for secure sharing or public disclosure.
- **High-Velocity Processing**
    - Reduces the time required for document preparation from hours to seconds through automated batch processing.

---

## Use Cases
**Legal Document Sanitization**
- Redacting sensitive client data from service agreements before sharing with third-party vendors.
- Masking financial details in internal contracts to prevent unauthorized access during cross-departmental reviews.

**Regulatory Compliance Audits**
- Preparing historical document archives for GDPR compliance checks by ensuring all PII is systematically removed.
- Automating the redaction of employee data in HR contracts to meet internal privacy standards.

**Secure Collaboration**
- Scrubbing confidential deal terms from project briefs before distributing them to external stakeholders.
- Protecting sensitive information in legal discovery documents to ensure only relevant, non-private data is exposed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Contract Redaction & Privacy Tool template from the marketplace.
3. Connect your preferred document storage provider (e.g., Google Drive, Dropbox) within the workflow settings.
4. Ensure nodes are correctly linked from the **Chat Input** to the **Agent** and finally to the **Composio Toolset** for output.

### 2) Setup the Nodes
- **Chat Input**: Receives the document file path or raw text for processing.
- **Agent**: Analyzes the input to identify PII based on configured privacy rules.
- **Composio Toolset**: Executes the redaction commands via the PDF.co API.
- **Chat Output**: Returns the link to the sanitized, redacted document.

### 3) Run the Flow
Use the Playground to test the redaction capabilities:
- `Redact all social security numbers and client names in the attached contract.`
- `Scan this document for sensitive financial data and provide a redacted version.`
- `Identify and mask all addresses in the provided legal agreement.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligence layer for identifying sensitive patterns.
- Set the system prompt to prioritize high-recall PII detection.
- Configure the temperature to 0.1 for consistent, deterministic redaction results.
- Enable the "Tool Use" capability to allow the agent to invoke the Composio redaction functions.

### 2) Composio Toolset Node
- Authenticate the node using your PDF.co API key.
- Define the connection scope to allow read/write access to your document processing folders.

### 3) Tool Availability
- **PDF.co Redaction API**: For precise, pixel-level masking of document content.
- **Text Analysis Tools**: For identifying PII entities within unstructured legal text.
- **File Management Utilities**: For retrieving source files and saving redacted outputs.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Ensures account data adheres to privacy and usage policies.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the sanitization and organization of post-incident action items.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audits user permissions to ensure data access remains compliant.
