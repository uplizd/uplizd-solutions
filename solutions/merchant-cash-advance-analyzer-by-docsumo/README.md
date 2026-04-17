# Merchant Cash Advance Analyzer (Uplizd) - Automated MCA eligibility and risk assessment

## Summary
The Merchant Cash Advance (MCA) Analyzer is an intelligent Uplizd workflow that automates the extraction and evaluation of financial data from bank statements to determine funding eligibility. By leveraging the Docsumo integration, this solution eliminates manual document review, accelerates pipeline velocity for underwriters, and ensures a single source of truth for risk assessment metrics.

---

## Demo
![Merchant Cash Advance Analyzer workflow diagram showing document ingestion, Docsumo data extraction, and eligibility scoring](image.png)
**Alt text (SEO-ready):** Uplizd Merchant Cash Advance Analyzer workflow for automated bank statement processing, financial data extraction, and MCA eligibility scoring using Docsumo and AI agents.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e51dc83b-381c-55a4-92d7-393770dc166d)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** mca, fintech, document processing, docsumo, underwriting, risk assessment, data extraction, ai workflow
- This solution streamlines the merchant cash advance lifecycle by automating document-heavy underwriting tasks.

---

## Who is this for?
This solution is designed for financial services teams looking to reduce manual data entry and improve the accuracy of funding decisions.

- **Underwriting Manager**
    - Accelerates the review process for high-volume merchant applications.
- **Risk Analyst**
    - Ensures consistent evaluation criteria across all incoming bank statements.
- **Sales Operations Lead**
    - Reduces the time-to-funding, increasing overall pipeline conversion rates.
- **Fintech Product Owner**
    - Integrates automated document intelligence into existing lending workflows.

---

## Features
- **Automated Data Extraction**
    - Uses Docsumo to parse complex bank statements into structured financial data points.
- **Real-time Eligibility Scoring**
    - Applies custom business logic to calculate cash flow health and repayment capacity instantly.
- **Seamless CRM Integration**
    - Syncs verified financial summaries directly into your CRM to update deal status.
- **Compliance-Ready Audit Trails**
    - Maintains a clear record of extracted data and decision logic for regulatory reporting.
- **Intelligent Exception Handling**
    - Automatically flags statements with missing pages or poor image quality for manual review.

---

## Use Cases
**Automated Underwriting**
- Extracting monthly revenue trends to determine maximum advance amounts.
- Identifying high-risk transaction patterns automatically before human review.

**Pipeline Management**
- Updating deal stages in the CRM based on the outcome of the eligibility check.
- Notifying account managers immediately when a merchant meets funding criteria.

**Data Hygiene**
- Standardizing disparate bank statement formats into a unified internal data schema.
- Archiving processed documents with associated metadata for future historical analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your Docsumo API credentials and CRM integration within the builder.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the bank statement file or document URL from the user.
- **Agent**: Orchestrates the analysis, interpreting the extracted data against lending criteria.
- **Composio Toolset**: Executes the Docsumo extraction and updates the CRM records.
- **Chat Output**: Returns the eligibility status and summary report to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze the attached bank statement for Merchant ID 9982 and provide an eligibility score.`
- `Extract the average monthly balance from this document and update the CRM deal record.`
- `Review the provided statement for any signs of non-sufficient funds (NSF) and summarize findings.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst, focusing on precision and adherence to lending policies.
- **Instruction Pattern:**
    - Analyze the provided document using the Docsumo toolset to identify key financial metrics.
    - Compare extracted revenue against the defined threshold for MCA approval.
    - Format the final output as a concise summary for the underwriting team.

### 2) Composio Toolset Node
- **API Key:** Provide your Docsumo and CRM API keys in the environment settings.
- **Connection Scope:** Ensure the agent has read access to document storage and write access to your CRM's deal objects.

### 3) Tool Availability
- **Docsumo API:** For document parsing and data extraction.
- **CRM Connector:** For updating deal status and opportunity fields.
- **Notification Service:** For alerting the underwriting team upon completion.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research into prospect accounts.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Streamlines financial ledger matching and reconciliation.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages stage transitions and follow-ups for sales opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes data across multiple CRM platforms and tools.
