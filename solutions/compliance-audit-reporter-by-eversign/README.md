# Compliance Audit Reporter (Uplizd) - Automated document compliance and audit trail generation

## Summary
The Compliance Audit Reporter (Uplizd) streamlines the verification of signed documents by automating the extraction and validation of audit trails. This workflow empowers legal and operations teams to maintain a single source of truth for document integrity, significantly reducing manual review time and ensuring pipeline velocity during critical compliance audits.

---

## Demo
![Compliance Audit Reporter dashboard showing document audit trail extraction and validation status](image.png)
**Alt text (SEO-ready):** Compliance Audit Reporter dashboard showing document audit trail extraction and validation status via Uplizd AI workflow and eversign integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/84614a8c-9ef6-5779-baa4-1fcdb0c147bb)

---

## Category
**Primary category:** Legal Operations
**Secondary tags:** compliance, audit, eversign, document management, data integrity, workflow automation, legal tech, composio
This solution bridges the gap between signed document repositories and regulatory reporting requirements through automated data extraction.

---

## Who is this for?
This solution is designed for professionals responsible for maintaining rigorous document standards and audit readiness.

*   **Compliance Officer**
    *   Automates the verification of digital signatures and audit logs to ensure regulatory adherence.
*   **Legal Operations Manager**
    *   Reduces the administrative burden of manual document audits by centralizing reporting.
*   **Operations Analyst**
    *   Provides real-time visibility into document status and potential compliance gaps across the organization.
*   **Risk Manager**
    *   Ensures a tamper-proof trail of evidence for every signed contract or agreement.

---

## Features
- **Automated Audit Extraction**
  Instantly pull comprehensive audit logs from eversign for any completed document.
- **Compliance Validation Engine**
  Automatically cross-reference document metadata against predefined compliance rules.
- **Unified Reporting Interface**
  Generate clean, exportable reports that summarize document status and signer activity.
- **Real-time Status Monitoring**
  Track document lifecycle stages from initiation to final signature and audit completion.
- **Composio-Powered Integration**
  Leverage the Composio Toolset to securely connect and query document management platforms.

---

## Use Cases
**Regulatory Compliance Audits**
*   Automatically aggregate audit trails for annual internal compliance reviews.
*   Flag documents missing required signer verification or timestamp data.

**Contract Lifecycle Management**
*   Verify that all signed agreements meet internal security and formatting standards.
*   Trigger alerts when a document audit trail fails to meet specific organizational criteria.

**Operational Efficiency**
*   Bulk-process document status reports to identify bottlenecks in the signing workflow.
*   Generate summary reports for stakeholders without manually opening individual document files.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Compliance Audit Reporter template from the solution gallery.
3. Connect your eversign account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the document ID or batch query parameters.
*   **Agent**: Analyzes the request and determines which audit data to retrieve.
*   **Composio Toolset**: Executes secure API calls to eversign to fetch document logs.
*   **Chat Output**: Returns the formatted audit report or compliance status summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Generate an audit report for document ID 12345 and check for signer verification.`
* `List all documents from the last 30 days that are missing audit trails.`
* `Verify compliance status for the latest batch of signed contracts.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting audit logs and identifying compliance discrepancies.
*   Focus on extracting signer identity and timestamp accuracy.
*   Prioritize clear, actionable summaries for non-technical stakeholders.
*   Maintain strict adherence to the provided compliance rule set during evaluation.

### 2) Composio Toolset Node
Requires a valid eversign API key. Ensure the connection scope includes `read_documents` and `read_audit_trail` permissions to allow the agent to pull necessary data.

### 3) Tool Availability
*   `eversign_get_document_details`: Retrieve metadata for specific documents.
*   `eversign_get_audit_trail`: Access the full history of document interactions.
*   `eversign_list_documents`: Query document lists based on status or date ranges.

---

## Related Solutions
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Automated monitoring for digital accessibility standards.
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Tracking account usage and compliance metrics.
* [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) - Ensuring workforce adherence to labor compliance policies.
