# Detecting PII in Medical Records (Uplizd) - Automated Health Data Privacy and Compliance

## Summary
The Detecting PII in Medical Records workflow provides an automated, intelligent layer for scanning and identifying sensitive personally identifiable information (PII) within clinical documentation. By leveraging advanced AI models and the Composio Toolset, this solution ensures that healthcare organizations maintain strict data hygiene, reduce the risk of accidental exposure, and streamline compliance with HIPAA and other privacy regulations.

---

## Demo
![Workflow diagram showing the PII detection pipeline from Chat Input to Agent analysis and secure Output](image.png)
**Alt text (SEO-ready):** Uplizd PII detection workflow for medical records, featuring automated data classification, healthcare compliance monitoring, and Composio integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/ac71727e-f363-5ba1-a70a-c1e84b1ed5eb)

---

## Category
- **Primary category:** Data Privacy & Compliance
- **Secondary tags:** healthcare, pii, data hygiene, compliance, security, ai workflow, composio, medical records
- This solution bridges the gap between unstructured clinical data and regulatory requirements by automating the identification of sensitive patient information.

---

## Who is this for?
This workflow is designed for healthcare professionals and technical teams tasked with maintaining data integrity and patient privacy.

- **Compliance Officer**
    - Ensures organizational adherence to HIPAA and GDPR standards through automated audit trails.
- **Health Informatics Specialist**
    - Maintains clean, de-identified datasets for research and clinical analysis.
- **Medical Records Administrator**
    - Reduces manual review time for incoming patient files and electronic health records.
- **Data Security Engineer**
    - Implements proactive data loss prevention (DLP) measures within internal document pipelines.

---

## Features
- **Automated PII Identification**
    - Uses advanced LLM reasoning to scan unstructured text for names, dates, IDs, and contact info.
- **Regulatory Compliance Mapping**
    - Aligns detection logic with standard healthcare privacy frameworks to ensure consistent data handling.
- **Composio-Powered Integration**
    - Connects directly to existing document repositories and EHR systems to pull records for real-time analysis.
- **Customizable Sensitivity Thresholds**
    - Allows users to define which data points are flagged as critical versus informative based on internal policy.
- **Secure Output Formatting**
    - Generates clean, redacted, or flagged reports that integrate seamlessly into downstream clinical workflows.

---

## Use Cases
**Clinical Data Auditing**
- Scanning legacy patient records to identify and flag un-redacted PII before migration.
- Auditing incoming medical transcripts for compliance with internal data handling policies.

**Research Data Preparation**
- Automatically de-identifying patient notes to create anonymized datasets for clinical research.
- Ensuring that shared medical case studies contain no identifiable patient markers.

**Regulatory Reporting**
- Generating automated summaries of data exposure risks across different departments.
- Providing documentation of proactive privacy measures for annual security audits.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution in the builder.
2. Select your preferred workspace to import the workflow template.
3. Connect your required document storage or EHR integrations via the Composio dashboard.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw medical text or document reference for analysis.
- **Agent**: Processes the input, applying PII detection logic and classification instructions.
- **Composio Toolset**: Executes secure data retrieval and interaction with your connected health systems.
- **Chat Output**: Returns the final analysis, including identified PII locations and recommended redaction actions.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Scan the provided medical record for any PII and list the identified fields.`
- `Identify and redact all patient names and social security numbers from this document.`
- `Analyze the attached clinical notes and flag any potential HIPAA compliance violations.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires a model capable of high-precision entity recognition.
- **Instruction Pattern:**
    - "Act as a medical data privacy expert specializing in PII identification."
    - "Strictly follow the provided list of sensitive data categories for classification."
    - "Return results in a structured format suitable for automated redaction tools."

### 2) Composio Toolset Node
- Requires a valid API key with read-access to your document management or EHR platform.
- Ensure the connection scope is limited to the specific folders or databases requiring audit.

### 3) Tool Availability
- **Document Reader**: Extracts text from PDFs and clinical notes.
- **Entity Classifier**: Categorizes identified PII types (e.g., PHI, PII, Financial).
- **Compliance Reporter**: Formats findings into standardized audit logs.

---

## Related Solutions
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Automates bulk data cleanup and formatting for CRM records.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronizes data across platforms while maintaining field-level integrity.
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) - Monitors and audits account security configurations and access logs.
