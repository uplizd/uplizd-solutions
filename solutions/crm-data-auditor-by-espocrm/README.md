# CRM Data Auditor (Uplizd) - Automated integrity and validation for EspoCRM

## Summary
The CRM Data Auditor (Uplizd) is an intelligent workflow designed to automate the validation, hygiene, and integrity monitoring of your EspoCRM database. By leveraging the Composio Toolset, this solution identifies inconsistencies, duplicate records, and missing field data in real-time, ensuring your sales and marketing teams operate with a single source of truth and high-velocity data accuracy.

---

## Demo
![CRM Data Auditor dashboard showing automated validation results and data hygiene alerts](image.png)

**Alt text (SEO-ready):** CRM Data Auditor dashboard showing automated validation results and data hygiene alerts for EspoCRM, powered by Uplizd and Composio for improved data quality.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBfQDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMAAAD//wMEAAU=)](https://uplizd.ai/solutions/50dd948a-5830-521a-874d-3135740b712b)

---

## Category
**Primary Category:** CRM Data Hygiene
**Secondary Tags:** `espocrm`, `data audit`, `data integrity`, `automation`, `composio`, `crm`, `data validation`

This solution streamlines CRM maintenance by automating the identification and remediation of data quality issues within EspoCRM.

---

## Who is this for?
This solution is built for teams managing complex customer datasets who need to maintain high-quality records without manual intervention.

*   **Sales Operations Manager**
    *   Ensures clean pipeline data by automatically flagging incomplete or outdated lead information.
*   **CRM Administrator**
    *   Reduces manual cleanup time by automating routine data validation and integrity checks.
*   **Data Analyst**
    *   Maintains reliable reporting metrics by ensuring the underlying CRM data is accurate and standardized.
*   **Revenue Operations Lead**
    *   Improves cross-departmental alignment by maintaining a consistent and trustworthy customer database.

---

## Features
- **Automated Data Validation**
  Real-time scanning of EspoCRM records to identify missing fields, incorrect formats, and potential data decay.
- **Intelligent Duplicate Detection**
  Leverages the Composio Toolset to cross-reference new entries against existing records to prevent CRM bloat.
- **Customizable Audit Rules**
  Define specific criteria for "clean" data, allowing the agent to prioritize high-value accounts or specific lead stages.
- **Actionable Reporting**
  Generates automated summaries of data health, providing clear insights into which records require immediate attention.
- **Seamless EspoCRM Integration**
  Directly connects to your EspoCRM instance to perform bulk updates and record corrections without leaving the Uplizd flow.

---

## Use Cases
**Data Hygiene Maintenance**
*   Automatically flag and notify owners of records missing critical contact information like email or phone numbers.
*   Standardize address and industry field formatting across all new and existing CRM entries.

**Pipeline Integrity**
*   Identify stalled opportunities that have not been updated within a specific timeframe for immediate review.
*   Audit lead source attribution to ensure marketing spend is accurately reflected in CRM reporting.

**Compliance & Security**
*   Scan for outdated PII (Personally Identifiable Information) to ensure adherence to data retention policies.
*   Verify that all active accounts are linked to valid, verified primary contacts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the CRM Data Auditor template from the marketplace.
3. Authenticate your EspoCRM credentials within the connection settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the audit trigger or manual request from the user.
*   **Agent**: Processes the audit logic and interprets data quality rules.
*   **Composio Toolset**: Executes API calls to fetch and update records in EspoCRM.
*   **Chat Output**: Delivers the final audit report and summary of actions taken.

### 3) Run the Flow
Use the Playground to test your audit logic with these prompts:
* `Audit all leads created in the last 7 days for missing email addresses.`
* `Find and report all duplicate accounts based on company name.`
* `Standardize the industry field for all active accounts in the North America region.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the analytical engine that interprets CRM data and applies business logic.
*   Focus on identifying missing or malformed data patterns.
*   Prioritize clear, actionable summaries for the end user.
*   Maintain a neutral, professional tone for all audit reports.

### 2) Composio Toolset Node
Requires a valid EspoCRM API key with read/write permissions for the `Account`, `Lead`, and `Opportunity` modules. Ensure the connection scope includes `list`, `read`, and `update` capabilities.

### 3) Tool Availability
*   **Record Fetcher**: Retrieves lists of records based on filtered criteria.
*   **Data Validator**: Checks field values against predefined schema requirements.
*   **Record Updater**: Performs bulk or individual updates to correct data entries.
*   **Notification Dispatcher**: Sends audit summaries to the designated CRM admin.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple platforms and CRMs.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and optimize your sales pipeline stages.
