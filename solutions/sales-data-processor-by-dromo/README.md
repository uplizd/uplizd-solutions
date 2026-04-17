# Sales Data Processor (Uplizd) - Automated CRM Data Validation and Cleaning

## Summary
The Sales Data Processor (Uplizd) is an intelligent workflow designed to automate the ingestion, validation, and sanitization of sales data files. By leveraging the Composio Toolset to interface with CRM platforms, this solution eliminates manual data entry errors, ensures pipeline hygiene, and accelerates the time-to-value for sales operations teams managing complex lead and opportunity datasets.

---

## Demo
![Sales Data Processor workflow interface showing automated file ingestion and CRM validation nodes](image.png)
**Alt text (SEO-ready):** Sales Data Processor workflow in Uplizd for automated CRM data validation, file cleaning, and sales pipeline hygiene using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d2523ca3-2d49-52f7-8652-8010e8bfec65)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, data hygiene, sales operations, data sync, pipeline, composio, ai workflow, data validation
- This solution bridges the gap between raw sales data uploads and structured CRM records, ensuring high-quality data entry for RevOps teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maintain a single source of truth within their CRM.

- **Sales Operations Manager**
    - Automates the tedious process of cleaning and importing bulk lead lists into the CRM.
- **Account Executive**
    - Reduces time spent on manual data entry, allowing more focus on closing deals and pipeline management.
- **RevOps Analyst**
    - Ensures data integrity across the sales stack by enforcing validation rules during the ingestion phase.
- **Sales Development Representative**
    - Quickly validates prospect contact information and lead status before initiating outreach sequences.

---

## Features
- **Automated Data Validation**
    - Automatically checks incoming sales files for missing fields, incorrect formats, and duplicate entries before CRM submission.
- **Intelligent CRM Mapping**
    - Uses the Composio Toolset to intelligently map CSV or Excel columns to specific CRM objects like Leads, Contacts, or Opportunities.
- **Real-time Error Reporting**
    - Provides immediate feedback on failed rows or validation errors, allowing users to correct data issues within the chat interface.
- **Bulk Processing Efficiency**
    - Handles large datasets with high throughput, ensuring that bulk updates do not stall or trigger API rate limits.
- **Customizable Sanitization Rules**
    - Allows for the definition of custom cleaning logic, such as standardizing phone numbers, email casing, or job title formatting.

---

## Use Cases
**Lead List Management**
- Automatically cleaning and uploading cold lead lists from third-party events into the CRM.
- Identifying and merging duplicate records to prevent lead collision between BDR territories.

**Pipeline Hygiene**
- Validating that all new opportunity entries contain mandatory fields like "Close Date" and "Expected Revenue."
- Syncing updated deal stages from external spreadsheets back into the primary CRM system.

**Data Compliance & Standardization**
- Ensuring all incoming contact data adheres to regional formatting standards (e.g., GDPR-compliant address fields).
- Standardizing industry and company size categories to ensure accurate reporting and territory assignment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Sales Data Processor.
2. Click "Import" to add the workflow to your workspace.
3. Connect your preferred CRM integration via the Composio Toolset settings.
4. Ensure nodes are correctly mapped and all API credentials are authorized in the configuration panel.

### 2) Setup the Nodes
- **Chat Input**: Accepts user prompts and file upload triggers.
- **Agent**: Processes the data, applies validation logic, and determines the target CRM object.
- **Composio Toolset**: Executes the API calls to read, validate, and write data to the CRM.
- **Chat Output**: Confirms successful processing or highlights specific rows that require manual intervention.

### 3) Run the Flow
Use the Playground to test your data processing:
- `Process the attached sales_leads_q3.csv and upload to Salesforce.`
- `Validate the current pipeline file and flag any deals missing a close date.`
- `Clean the contact list and update existing records in HubSpot.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data steward, interpreting file structures and enforcing business rules.
- Instruction: "Analyze the provided file structure and map columns to CRM fields."
- Instruction: "Validate data against mandatory CRM schema requirements."
- Instruction: "Report any data anomalies or formatting errors back to the user clearly."

### 2) Composio Toolset Node
- **API Key**: Ensure your CRM API key is active within the Composio dashboard.
- **Connection Scope**: Grant read/write permissions for the specific CRM objects (Leads, Contacts, Opportunities) you intend to process.

### 3) Tool Availability
- **CRM Read/Write**: Ability to fetch existing records for deduplication and write new validated entries.
- **File Parser**: Capability to read and interpret CSV, XLSX, and JSON data formats.
- **Data Validator**: Logic-based tool to check for null values, regex patterns, and field constraints.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain data quality through automated cleanup and deduplication.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and track stalled opportunities.
- [Account Research Agent](../account-research-agent/README.md) - Gather intelligence on accounts to enrich CRM records.
