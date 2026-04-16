# Audit Document Comparator (Uplizd) - Automated document change detection and audit review

## Summary
The Audit Document Comparator by Draftable is an intelligent Uplizd workflow designed to automate the comparison of complex audit documents, contracts, and compliance reports. By leveraging the Draftable API via the Composio Toolset, this solution identifies discrepancies, tracks version changes, and highlights critical modifications, significantly reducing manual review time and ensuring high-fidelity document hygiene for legal and operations teams.

---

## Demo
![Audit Document Comparator workflow showing document upload, Draftable comparison, and change summary output](image.png)
**Alt text (SEO-ready):** Uplizd Audit Document Comparator workflow using Draftable API for automated document comparison, change detection, and compliance reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a36b9b9d-b9c4-5b43-8324-500482d40f69)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** document processing, audit, compliance, draftable, automation, data hygiene, workflow, composio
- This solution streamlines document-heavy audit workflows by automating the comparison of file versions to ensure accuracy and regulatory compliance.

---

## Who is this for?
This solution is designed for professionals managing high-stakes documentation who need to verify integrity across multiple versions.

- **Compliance Officer**
    - Ensures that all regulatory changes are captured and documented during audit cycles.
- **Legal Counsel**
    - Quickly identifies redlines and clause modifications in contract drafts to mitigate risk.
- **Operations Manager**
    - Reduces the time spent on manual document reconciliation, increasing team throughput.
- **Audit Analyst**
    - Maintains a single source of truth by automatically flagging discrepancies between source and revised documents.

---

## Features
- **Automated Change Detection**
    - Uses the Draftable engine to perform pixel-perfect and text-based comparisons between two documents.
- **Real-time Discrepancy Reporting**
    - Generates concise summaries of changes, allowing users to focus on high-impact modifications immediately.
- **Seamless Composio Integration**
    - Connects the Uplizd agent directly to the Draftable API for secure, authenticated document processing.
- **Multi-Format Support**
    - Handles various document types, ensuring consistency across PDF, Word, and text-based audit files.
- **Workflow Pipeline Velocity**
    - Eliminates manual "side-by-side" reading, accelerating the review lifecycle from hours to minutes.

---

## Use Cases
**Compliance & Regulatory Audits**
- Comparing current policy documents against previous versions to identify unauthorized changes.
- Generating audit trails for regulatory submissions by documenting all detected modifications.

**Contract Lifecycle Management**
- Reviewing contract redlines between internal teams and external vendors to ensure agreed-upon terms remain intact.
- Validating that final document versions match the approved draft before signature.

**Operational Data Hygiene**
- Identifying formatting inconsistencies or missing sections in recurring operational reports.
- Automating the reconciliation of financial audit statements against source ledger exports.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the `Audit Document Comparator` workflow.
3. Connect your Draftable API credentials within the Composio Toolset settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the two document URLs or files to be compared.
- **Agent**: Analyzes the comparison request and instructs the toolset to execute the diff.
- **Composio Toolset**: Executes the Draftable API calls to process the document comparison.
- **Chat Output**: Returns the structured summary of changes and a link to the comparison report.

### 3) Run the Flow
Use the Playground to test the workflow with prompts like:
- `Compare the document at [URL_A] with [URL_B] and list all major clause changes.`
- `Run a compliance audit comparison between the Q3 report and the Q4 draft.`
- `Identify any discrepancies in the pricing section between these two contract versions.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for document analysis, ensuring that the comparison output is human-readable and actionable.
- Focus on identifying material changes rather than minor formatting shifts.
- Summarize findings in a bulleted list categorized by impact level (High/Medium/Low).
- Maintain a professional, objective tone suitable for audit reporting.

### 2) Composio Toolset Node
- **API Key**: Ensure your Draftable API key is stored in the Uplizd environment variables.
- **Connection Scope**: Grant the agent access to read/write document comparison tasks within your Draftable account.

### 3) Tool Availability
- `draftable_compare_documents`: Initiates the comparison process between two provided files.
- `draftable_get_report`: Retrieves the detailed diff report after the comparison is processed.
- `file_url_validator`: Verifies that the input document links are accessible and valid.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automates infrastructure and account-level security audits.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manages and ranks tasks derived from audit and meeting notes.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the performance and status of automated operational pipelines.
