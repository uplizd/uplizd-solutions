# Automated Loan Underwriter (Uplizd) - Accelerate credit decisions with AI-driven document analysis

## Summary
The Automated Loan Underwriter (Uplizd) workflow leverages AI to ingest, parse, and evaluate loan application documents, significantly reducing manual review time for financial institutions. By integrating Docsumo for intelligent document processing, this solution extracts critical financial data, validates applicant information, and generates risk assessments, ensuring consistent underwriting standards and faster pipeline velocity.

---

## Demo
![Automated Loan Underwriter workflow interface showing document ingestion, data extraction, and risk scoring nodes](image.png)
**Alt text (SEO-ready):** Automated Loan Underwriter workflow interface showing document ingestion, data extraction, and risk scoring nodes for Uplizd AI-powered financial processing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/49d7d287-e2cf-519b-8f86-f2c969d0fae4)

---

## Category
**Primary category:** Financial Operations  
**Secondary tags:** `loan underwriting`, `docsumo`, `document processing`, `fintech`, `risk assessment`, `ai workflow`, `data extraction`, `automation`  
This solution streamlines the credit lifecycle by automating the transformation of unstructured loan documents into actionable underwriting insights.

---

## Who is this for?
This solution is designed for financial services teams looking to eliminate manual data entry and accelerate the loan approval process.

* **Loan Officers**
    * Reduce time spent manually reviewing bank statements and tax returns for applicant verification.
* **Risk Analysts**
    * Gain immediate access to structured financial data to perform accurate credit risk scoring.
* **Operations Managers**
    * Standardize the underwriting workflow to ensure compliance and consistent decision-making across the team.
* **Compliance Officers**
    * Maintain a clear, automated audit trail of all document extractions and underwriting decisions.

---

## Features
- **Intelligent Document Parsing**
    Automated extraction of key fields from complex loan documents using Docsumo’s specialized OCR models.
- **Real-time Data Validation**
    Cross-reference extracted applicant data against internal criteria to flag discrepancies immediately.
- **Automated Risk Scoring**
    Calculate applicant risk profiles based on extracted income, debt, and credit history metrics.
- **Seamless CRM Integration**
    Automatically push approved or flagged application summaries into your existing CRM or loan management system.
- **Exception Handling Workflow**
    Route incomplete or high-risk applications to human reviewers with a pre-populated summary of findings.

---

## Use Cases
**Loan Application Processing**
* Automate the intake of mortgage or personal loan applications from email attachments.
* Extract and verify income figures from W-2s and pay stubs within seconds.

**Risk and Credit Analysis**
* Generate automated risk summaries for loan committees based on extracted financial ratios.
* Identify missing documentation or expired credentials early in the underwriting cycle.

**Operational Efficiency**
* Reduce the "time-to-decision" by eliminating manual data entry tasks for the underwriting team.
* Standardize document formatting across multiple branches or regional offices.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Workflow" to add the Automated Loan Underwriter to your workspace.
3. Connect your Docsumo API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the loan document or application reference ID.
* **Agent**: Orchestrates the extraction logic and applies underwriting business rules.
* **Composio Toolset**: Executes the Docsumo API calls to parse and validate documents.
* **Chat Output**: Returns the structured underwriting summary and risk assessment to the user.

### 3) Run the Flow
Use the Playground to test your underwriting logic with these prompts:
* `Analyze the attached tax return and extract the total annual income and debt-to-income ratio.`
* `Validate the provided bank statement and flag any unusual transaction patterns over $5,000.`
* `Generate a summary report for the loan application ID #99283 and highlight any missing required documents.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary underwriter, interpreting extracted data against your specific lending policies.
* Set the system prompt to define the institution's risk appetite and required document thresholds.
* Use a high-reasoning model (e.g., GPT-4o) to ensure accurate interpretation of financial statements.
* Configure the agent to output structured JSON for easy integration with downstream systems.

### 2) Composio Toolset Node
* Provide your Docsumo API key to enable secure document processing.
* Set the connection scope to allow read/write access to your document management folders.

### 3) Tool Availability
* **Document Extraction**: Capability to parse PDFs, images, and scanned financial records.
* **Data Validation**: Capability to check extracted values against predefined business rules.
* **Notification Service**: Capability to alert loan officers when a file is ready for final review.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial ledger matching and account balancing.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich applicant data for better risk profiling.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Manage end-to-end task routing for complex operational processes.
