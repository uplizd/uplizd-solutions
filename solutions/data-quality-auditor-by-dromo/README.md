# Data Quality Auditor (Uplizd) - Automated spreadsheet validation and data hygiene

## Summary
The Data Quality Auditor is an intelligent Uplizd workflow designed to automate the validation, cleaning, and standardization of incoming spreadsheet data. By leveraging AI-driven logic, this solution ensures that your datasets remain accurate, compliant, and ready for downstream integration, significantly reducing manual data entry errors and improving pipeline velocity.

---

## Demo
![Data Quality Auditor workflow screenshot showing spreadsheet input, AI validation, and error reporting](image.png)
**Alt text (SEO-ready):** Data Quality Auditor Uplizd workflow for automated spreadsheet validation, data hygiene, and error reporting using AI and Composio integrations.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=appveyor)](https://uplizd.ai/solutions/2adb158c-177b-5c54-9e69-755634a23ea5)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** data hygiene, spreadsheet automation, dromo, data validation, crm, data sync, ai workflow, composio
- This solution bridges the gap between raw data ingestion and clean, actionable records by automating the audit process for enterprise datasets.

---

## Who is this for?
This solution is designed for professionals who manage high-volume data imports and require a reliable, automated way to maintain data integrity.

- **Data Operations Manager**
    - Ensures that all incoming data meets organizational standards before hitting the CRM.
- **Sales Operations Analyst**
    - Maintains clean lead lists and prevents duplicate or malformed entries from stalling the sales pipeline.
- **Marketing Coordinator**
    - Validates contact information and list formatting to improve campaign deliverability and engagement.
- **Database Administrator**
    - Automates the audit of bulk imports, reducing the time spent on manual data cleanup and troubleshooting.

---

## Features
- **Automated Data Validation**
    - Instantly flags missing fields, incorrect formats, or invalid data types within uploaded spreadsheets.
- **Intelligent Error Reporting**
    - Generates concise summaries of data quality issues, allowing users to address specific rows rather than entire files.
- **Standardization Engine**
    - Automatically formats phone numbers, addresses, and email strings to match your internal database requirements.
- **Composio-Powered Integration**
    - Seamlessly connects with your existing CRM and spreadsheet tools to push cleaned data directly to the source.
- **Real-time Audit Logs**
    - Maintains a history of all changes and validations performed, ensuring full transparency and compliance.

---

## Use Cases
**Bulk CRM Import Hygiene**
- Automatically scrubbing lead lists for duplicate entries before importing into Salesforce or HubSpot.
- Standardizing job titles and company names to ensure accurate territory routing and lead scoring.

**Customer Data Compliance**
- Auditing contact databases to ensure all records contain mandatory fields required for GDPR or CCPA compliance.
- Identifying and flagging expired or incomplete contact information for manual review by the sales team.

**Operational Efficiency**
- Reducing the manual labor involved in cleaning CSV exports from third-party vendors.
- Automating the reconciliation of account data between legacy systems and modern cloud platforms.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the **Data Quality Auditor**.
2. Click "Import" to add the workflow to your workspace.
3. Connect your preferred spreadsheet and CRM accounts via the integration settings.
4. Ensure nodes are correctly mapped from the **Chat Input** to the **Agent** and finally to the **Composio Toolset**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file path or raw data content for the audit.
- **Agent**: Analyzes the data against predefined validation rules and identifies anomalies.
- **Composio Toolset**: Executes the necessary API calls to update or flag records in your connected CRM.
- **Chat Output**: Returns a detailed audit report and a summary of actions taken.

### 3) Run the Flow
Open the Uplizd Playground and test the workflow with the following prompts:
- `Audit the uploaded file 'leads_q3.csv' and highlight any missing email addresses.`
- `Standardize the phone number format for all entries in the current spreadsheet.`
- `Check for duplicate account names in the recent import and provide a summary report.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting data quality rules and identifying discrepancies.
- **Instruction Pattern:**
    - "Act as a data quality specialist; identify missing or malformed fields based on the provided schema."
    - "Prioritize accuracy by flagging any ambiguous entries for human review."
    - "Maintain a professional tone when summarizing audit results for the end user."

### 2) Composio Toolset Node
- **API Key:** Ensure your Composio API key is active and authorized for the target CRM and file storage services.
- **Connection Scope:** Grant read/write access to the specific folders or CRM objects required for your audit tasks.

### 3) Tool Availability
- **Data Parsing Tools:** For reading and interpreting various spreadsheet formats (CSV, XLSX).
- **CRM Connector:** For fetching and updating records in real-time.
- **Validation Library:** A suite of regex and logic-based tools for checking field integrity.

---

## Related Solutions
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) - Monitor and maintain account compliance standards.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize and resolve data conflicts across multiple platforms.
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with external intelligence.
