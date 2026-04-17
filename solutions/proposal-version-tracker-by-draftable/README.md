# Proposal Version Tracker (Uplizd) - Automated document iteration and change analysis

## Summary
The Proposal Version Tracker is an intelligent Uplizd workflow designed to monitor, compare, and report on changes across multiple iterations of sales proposals. By leveraging the Composio Toolset to interface with document management platforms, this solution eliminates manual version comparison, ensuring that sales teams and stakeholders always have a single source of truth regarding document status, redlines, and approval history.

---

## Demo
![Proposal Version Tracker workflow interface showing document comparison and change logs](image.png)
**Alt text (SEO-ready):** Uplizd Proposal Version Tracker workflow interface showing automated document comparison, version history logs, and change analysis using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a126bacd-4310-5dcf-9771-1a1d8eb2e3ba)

---

## Category
**Primary category:** Operations
**Secondary tags:** sales operations, document management, version control, proposal automation, audit trail, composio, ai workflow, data hygiene.
This solution streamlines the document lifecycle by automating the tracking of proposal iterations, reducing administrative overhead for sales teams.

---

## Who is this for?
This solution is designed for professionals managing high-stakes document workflows who need to maintain visibility into complex negotiation cycles.

*   **Sales Operations Manager**
    *   Ensures compliance and consistency across all outgoing proposal versions.
*   **Account Executive**
    *   Tracks client feedback and redlines automatically to accelerate the closing process.
*   **Legal Counsel**
    *   Reviews document iterations quickly to identify critical changes in contract terms.
*   **Bid Coordinator**
    *   Maintains a clean audit trail of document versions for complex RFP responses.

---

## Features
- **Automated Version Comparison**
  Instantly detect and highlight textual differences between document versions using AI-powered analysis.
- **Centralized Change Log**
  Maintain a persistent, searchable history of all modifications, including timestamps and author attribution.
- **Composio-Powered Integration**
  Seamlessly connect with document storage and CRM platforms to fetch and update proposal files in real-time.
- **Smart Redline Detection**
  Automatically flag critical changes in pricing, scope, or legal clauses for immediate human review.
- **Approval Status Tracking**
  Monitor the lifecycle of a proposal from draft to final sign-off with automated status updates.

---

## Use Cases
**Document Lifecycle Management**
*   Automatically archive previous versions of proposals when a new iteration is uploaded to the repository.
*   Generate summary reports of changes made between the initial draft and the final client-ready document.

**Sales Compliance & Audit**
*   Maintain a strict audit trail of all modifications to contract terms for regulatory and internal reporting.
*   Flag unauthorized changes to standardized pricing or service level agreement (SLA) templates.

**Team Collaboration**
*   Notify relevant stakeholders via Slack or email when a new version of a high-value proposal is ready for review.
*   Consolidate feedback from multiple reviewers into a single, structured document update request.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Flow."
2. Upload the provided JSON configuration file for the Proposal Version Tracker.
3. Authenticate your document storage and CRM connections via the Composio dashboard.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API connections are active.

### 2) Setup the Nodes
*   **Chat Input**: Receives the document ID or file path from the user.
*   **Agent**: Analyzes the document content and compares it against previous versions.
*   **Composio Toolset**: Executes file retrieval and comparison commands across connected apps.
*   **Chat Output**: Returns a structured summary of changes and the current version status.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Compare the latest version of 'Q3_Proposal_Acme' with the previous iteration.`
* `List all changes made to the pricing section in the current proposal.`
* `Generate a summary of all redlines made by the client in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a document analyst, focusing on precision and context retention.
*   Instruction: "You are a professional document auditor. Focus on identifying changes in scope, pricing, and legal terms."
*   Instruction: "Maintain a neutral tone and provide clear, bulleted summaries of detected modifications."
*   Instruction: "If a document version is missing, request the correct file path from the user."

### 2) Composio Toolset Node
*   **API Key**: Ensure your Composio API key is configured with read/write access to your document storage provider.
*   **Connection Scope**: Limit the scope to specific folders containing active proposals to ensure data security.

### 3) Tool Availability
*   **File Retrieval**: Fetching document metadata and content.
*   **Version Comparison**: Running diff algorithms on text-based documents.
*   **Notification Dispatch**: Sending alerts to team communication channels.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into prospect accounts.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and deal velocity.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and standardize CRM data records.
