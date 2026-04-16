# Bulk Signature Orchestrator (Uplizd) - Automated document signing and tracking at scale

## Summary
The Bulk Signature Orchestrator streamlines high-volume document workflows by automating the distribution, tracking, and management of electronic signatures via Eversign. This Uplizd AI workflow eliminates manual bottlenecks, ensuring that legal, HR, and sales teams maintain pipeline velocity while keeping a single source of truth for all pending and completed agreements.

---

## Demo
![Bulk Signature Orchestrator workflow showing document distribution and status tracking](image.png)
**Alt text (SEO-ready):** Bulk Signature Orchestrator workflow for automated document signing, Eversign integration, and real-time status tracking on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/bulk-signature-orchestrator-by-eversign)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** eversign, document signing, workflow automation, sales operations, hr operations, contract management, composio, ai workflow.
This solution bridges the gap between document generation and execution by automating the Eversign lifecycle within your existing business processes.

---

## Who is this for?
This workflow is designed for teams managing high volumes of documentation who need to reduce administrative overhead and accelerate time-to-signature.

*   **Sales Operations Manager**
    *   Automates contract delivery to prospects, reducing the time from verbal agreement to signed deal.
*   **HR Coordinator**
    *   Simplifies the onboarding process by triggering bulk offer letters and NDAs for new hires.
*   **Legal Counsel**
    *   Ensures consistent document tracking and audit trails for compliance without manual intervention.
*   **Account Executive**
    *   Focuses on closing deals rather than chasing signatures, with automated status updates in the CRM.

---

## Features
- **Automated Distribution**
  Triggers signature requests to multiple recipients simultaneously, reducing manual email preparation time.
- **Real-time Status Tracking**
  Monitors document progress via the Composio Toolset to provide instant visibility into pending vs. completed agreements.
- **Dynamic Template Mapping**
  Automatically populates Eversign templates with data from your CRM or input source for personalized document generation.
- **Centralized Audit Trail**
  Maintains a secure, timestamped record of all signature events, ensuring full compliance and transparency.
- **Exception Handling**
  Automatically flags stalled or rejected documents for manual review, preventing deals from slipping through the cracks.

---

## Use Cases
**Contract Lifecycle Management**
*   Automating the dispatch of Master Service Agreements (MSAs) upon deal entry in the CRM.
*   Triggering renewal signature requests 30 days prior to contract expiration.

**Employee Onboarding**
*   Sending bulk offer letters and tax forms to a list of new hires from a CSV or database.
*   Tracking the completion of mandatory policy acknowledgments for internal compliance.

**Sales Pipeline Acceleration**
*   Generating and sending customized SOWs (Statements of Work) immediately after a demo.
*   Updating CRM deal stages automatically once a document is signed by all parties.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `bulk-signature-orchestrator-by-eversign` JSON template.
3. Connect your Eversign account via the Composio integration settings.
4. Ensure nodes are correctly mapped from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event (e.g., a list of signers or a deal ID).
*   **Agent**: Interprets the request and orchestrates the Eversign API calls.
*   **Composio Toolset**: Executes the document creation and signature request functions.
*   **Chat Output**: Returns the status of the signature requests and any error logs.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Send the 'Standard NDA' template to the following list of emails: [email1, email2, email3].`
* `Check the status of all pending signature requests for Deal ID #9982.`
* `Generate a summary report of all documents signed this week and notify the sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for document logic and status reporting.
*   Instruction: "You are an expert document operations assistant. Use the Eversign toolset to dispatch documents and retrieve status updates."
*   Instruction: "Always verify the recipient's email format before initiating a signature request."
*   Instruction: "If a document status is 'declined', provide the reason and suggest a follow-up action."

### 2) Composio Toolset Node
*   **API Key**: Provide your Eversign API key via the Composio connection manager.
*   **Connection Scope**: Ensure the scope includes `document_read`, `document_write`, and `template_access`.

### 3) Tool Availability
*   `eversign_send_document`: Initiates a new signature request.
*   `eversign_get_document_status`: Retrieves real-time progress for a specific document ID.
*   `eversign_list_templates`: Fetches available templates for dynamic population.
*   `eversign_cancel_document`: Allows the agent to revoke requests if data is incorrect.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups for active opportunities.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize records across multiple platforms with conflict resolution.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather account intelligence to personalize document content.
