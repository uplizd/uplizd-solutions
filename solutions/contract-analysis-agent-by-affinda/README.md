# Contract Analysis Agent (Uplizd) - Automated legal document review and clause extraction

## Summary
The Contract Analysis Agent leverages AI to streamline legal workflows by automatically extracting critical terms, clauses, and obligations from complex legal documents. By integrating with the Affinda document processing engine, this Uplizd workflow reduces manual review time, ensures consistency across contract portfolios, and accelerates the transition from drafting to execution for legal and operations teams.

---

## Demo
![Contract Analysis Agent workflow interface showing document upload and clause extraction results](image.png)
**Alt text (SEO-ready):** Contract Analysis Agent (Uplizd) workflow showing automated legal document processing, clause extraction, and AI-driven contract review using Affinda integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cfdaa793-2859-5fb6-a339-88c24e4c21e5)

---

## Category
- **Primary category:** Legal operations
- **Secondary tags:** contract analysis, document processing, affinda, ai workflow, legal tech, compliance, automation, composio
- This solution bridges the gap between raw legal documentation and actionable data insights, enabling automated compliance and risk assessment.

---

## Who is this for?
This solution is designed for professionals who manage high volumes of legal documentation and require rapid, accurate data extraction.

- **Legal Counsel**
    - Automate the preliminary review of standard agreements to focus on high-risk clauses.
- **Contract Managers**
    - Maintain a single source of truth for key dates, renewal terms, and liability limits.
- **Procurement Officers**
    - Quickly extract pricing and delivery terms from vendor contracts for budget reconciliation.
- **Operations Leads**
    - Ensure organizational compliance by flagging non-standard terms across all active contracts.

---

## Features
- **Automated Clause Extraction**
    - Instantly identify and categorize key legal provisions like indemnification, termination, and governing law.
- **Affinda Integration**
    - Utilize industry-leading document parsing to convert unstructured PDF or Word contracts into structured JSON data.
- **Compliance Monitoring**
    - Automatically flag contracts that deviate from company-standard templates or risk thresholds.
- **Real-time Data Sync**
    - Push extracted metadata directly into your CRM or document management system via the Composio Toolset.
- **Scalable Document Processing**
    - Handle bulk uploads of contract batches, significantly reducing the manual effort required for due diligence.

---

## Use Cases
**Contract Lifecycle Management**
- Automatically extract renewal dates and notice periods to prevent accidental auto-renewals.
- Compare incoming vendor contracts against internal master service agreement (MSA) templates.

**Risk and Compliance Audits**
- Scan large repositories of legacy contracts to identify exposure to specific liability clauses.
- Generate summary reports of all active contracts containing specific regulatory or data privacy language.

**Sales and Procurement Operations**
- Extract pricing tables and payment terms from signed contracts to update billing systems automatically.
- Rapidly qualify new vendor agreements by verifying mandatory security and insurance clauses.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your Affinda API credentials within the Composio Toolset node.
3. Configure your target destination (e.g., Google Drive, Salesforce, or Email) for the extracted data.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the contract file or document URL from the user.
- **Agent**: Analyzes the document content and identifies requested legal clauses.
- **Composio Toolset**: Executes the Affinda extraction and pushes data to external systems.
- **Chat Output**: Returns a summary of the extracted terms and confirmation of the data sync.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Extract all termination clauses and renewal dates from the attached service agreement.`
- `Review this contract and flag any indemnification clauses that exceed our standard liability cap.`
- `Summarize the payment terms and delivery obligations found in this vendor contract.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a legal assistant, focusing on precision and clause identification.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate legal interpretation.
- Set the system prompt to prioritize extraction accuracy over conversational filler.
- Enable structured output mode to ensure the extracted clauses map correctly to your database fields.

### 2) Composio Toolset Node
- Provide your Affinda API key to enable document parsing capabilities.
- Define the connection scope to include read access to your document storage and write access to your CRM or database.

### 3) Tool Availability
- **Document Parser**: Affinda integration for OCR and layout analysis.
- **Data Connector**: Composio-managed endpoints for CRM and cloud storage synchronization.
- **Notification Service**: Optional email or Slack integration to alert stakeholders of completed reviews.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather intelligence on companies to contextualize legal agreements.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Sync extracted contract data into your CRM account records.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Trigger downstream business processes based on extracted contract terms.
