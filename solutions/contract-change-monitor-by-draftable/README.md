# Contract Change Monitor (Uplizd) - Automated document version control and clause analysis

## Summary
The Contract Change Monitor by Draftable is an intelligent Uplizd workflow designed to automate the detection, comparison, and reporting of modifications within legal documents. By leveraging advanced document comparison tools, this solution provides legal teams and contract administrators with a single source of truth, significantly reducing manual review time, eliminating oversight errors, and ensuring pipeline velocity during high-stakes negotiations.

---

## Demo
![Contract Change Monitor workflow showing document upload, Draftable comparison, and change summary output](image.png)
**Alt text (SEO-ready):** Contract Change Monitor workflow in Uplizd showing automated document comparison, clause analysis, and change detection using the Composio Toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/78005242-26a7-57b8-bd0d-3fb997be4b4e)

---

## Category
- **Primary category:** Legal operations
- **Secondary tags:** contract management, document analysis, draftable, compliance, risk mitigation, ai workflow, composio, legal tech
- This solution streamlines the legal review lifecycle by integrating automated document comparison directly into your existing operational stack.

---

## Who is this for?
This solution is designed for professionals managing high volumes of legal documentation who require precision and speed.

- **Legal Counsel**
    - Ensures all redlined changes are identified and reviewed for compliance before final signature.
- **Contract Manager**
    - Maintains version control across multiple document iterations to prevent unauthorized clause modifications.
- **Sales Operations Lead**
    - Accelerates deal cycles by instantly highlighting changes in incoming contract redlines from prospects.
- **Compliance Officer**
    - Audits document history to ensure that critical terms remain consistent with organizational standards.

---

## Features
- **Automated Redline Detection**
    - Instantly identifies additions, deletions, and formatting changes between document versions using Draftable.
- **Intelligent Clause Summarization**
    - Uses the Agent node to distill complex legal changes into concise, actionable summaries for stakeholders.
- **Seamless Composio Integration**
    - Connects directly to document repositories to fetch files and push comparison reports back into your workflow.
- **Real-time Alerting**
    - Triggers notifications via the Chat Output node when significant changes are detected in high-priority contracts.
- **Version History Tracking**
    - Maintains a clear audit trail of document states, ensuring transparency throughout the negotiation process.

---

## Use Cases
**Contract Negotiation Review**
- Automatically compare a received contract against your standard template to identify deviations.
- Flag non-standard clauses that require immediate attention from the legal department.

**Compliance and Risk Auditing**
- Perform bulk comparisons on legacy contracts to ensure updated privacy clauses are present.
- Generate summary reports for internal stakeholders highlighting potential risks introduced in new drafts.

**Sales Cycle Acceleration**
- Rapidly process redlines from prospects to provide Sales teams with immediate feedback on requested terms.
- Reduce the "time-to-signature" by automating the initial review phase of the contract lifecycle.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the pre-configured workflow.
3. Authenticate your Draftable and storage provider connections via the Composio dashboard.
4. Ensure nodes are correctly mapped from Chat Input to Chat Output to verify the data pipeline.

### 2) Setup the Nodes
- **Chat Input**: Receives the original and revised document files or URLs.
- **Agent**: Analyzes the comparison data and generates human-readable insights.
- **Composio Toolset**: Executes the document comparison and retrieves file metadata.
- **Chat Output**: Delivers the final summary and change report to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Compare the attached 'Service_Agreement_v1.pdf' with 'Service_Agreement_v2.pdf' and list all clause changes.`
- `Summarize the key differences in the indemnity section of these two documents.`
- `Are there any unauthorized changes to the payment terms in the latest contract draft?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your legal assistant, focusing on accuracy and context-aware summarization.
- Set the system prompt to prioritize "Legal Reviewer" persona.
- Enable "Strict Mode" to ensure no hallucinated changes are reported.
- Configure the temperature to 0.2 for precise, factual output.

### 2) Composio Toolset Node
- Provide your Draftable API key within the Composio integration settings.
- Ensure the connection scope includes read/write access to your document storage (e.g., Google Drive, SharePoint).

### 3) Tool Availability
- **Draftable Compare**: Core engine for file diffing.
- **File Fetcher**: Retrieves source documents from cloud storage.
- **Report Generator**: Formats findings into structured Markdown or PDF summaries.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Gather deep intelligence on accounts before contract negotiations.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manage follow-up tasks derived from legal and operational meetings.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean contact data for accurate contract association.
