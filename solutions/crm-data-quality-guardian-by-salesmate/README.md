# CRM Data Quality Guardian (Uplizd) - Automated CRM data hygiene and record validation

## Summary
The CRM Data Quality Guardian is an intelligent Uplizd workflow that automates data hygiene by scanning, validating, and correcting records within Salesmate CRM. By leveraging AI-driven analysis, this solution ensures your CRM remains a single source of truth, eliminating duplicate entries, fixing formatting inconsistencies, and maintaining pipeline velocity through high-quality, actionable data.

---

## Demo
![CRM Data Quality Guardian workflow interface showing automated record validation and cleanup nodes](image.png)
**Alt text (SEO-ready):** CRM Data Quality Guardian Uplizd workflow interface for automated Salesmate CRM data hygiene, record validation, and pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bf9f81b2-2358-5532-b7e9-db0aece43ca9)

---

## Category
**Primary category:** CRM data hygiene
**Secondary tags:** salesmate, crm, data quality, data sync, pipeline, automation, composio, ai workflow
This solution bridges the gap between raw CRM input and high-fidelity data readiness by automating the cleanup of contact and deal records.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data entry errors and maintain a pristine CRM environment.

- **Sales Operations Manager**
    - Ensures data integrity across the entire sales stack to improve reporting accuracy.
- **Account Executive**
    - Reduces time spent on manual record updates, allowing more focus on closing deals.
- **Revenue Operations Lead**
    - Maintains standardized data formats to ensure seamless cross-departmental collaboration.
- **Data Analyst**
    - Relies on clean, deduplicated datasets for accurate forecasting and trend analysis.

---

## Features
- **Automated Record Validation**
    - Scans Salesmate CRM records in real-time to identify missing fields and invalid data formats.
- **Intelligent Deduplication**
    - Uses AI to detect and merge duplicate contact or company profiles based on fuzzy matching logic.
- **Standardized Formatting**
    - Automatically enforces naming conventions and address formatting across all CRM entries.
- **Composio Toolset Integration**
    - Seamlessly connects to Salesmate CRM via the Composio Toolset to execute read/write operations securely.
- **Proactive Data Alerts**
    - Triggers notifications when critical data decay is detected, prompting immediate remediation.

---

## Use Cases
**Data Hygiene & Maintenance**
- Automatically format phone numbers and email addresses to match company standards.
- Identify and flag incomplete lead profiles that lack essential qualification criteria.

**Pipeline Optimization**
- Clean up stale deal stages to ensure the sales pipeline reflects accurate forecasting data.
- Standardize lead source attribution fields to improve ROI reporting on marketing campaigns.

**Compliance & Security**
- Audit contact records for outdated consent flags to maintain GDPR and CCPA compliance.
- Remove orphaned records that are no longer associated with active accounts or opportunities.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the CRM Data Quality Guardian workflow.
3. Authenticate your Salesmate CRM account within the Composio connection settings.
4. Ensure nodes are correctly mapped and the agent is linked to the Salesmate toolset.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or manual request to initiate a data audit.
- **Agent**: Analyzes the CRM data against defined quality rules using the LLM.
- **Composio Toolset**: Executes the specific API calls to update or delete records in Salesmate.
- **Chat Output**: Provides a summary report of the records cleaned, merged, or flagged.

### 3) Run the Flow
- `Audit all contact records created in the last 30 days for missing phone numbers.`
- `Find and merge duplicate company profiles in Salesmate that share the same domain.`
- `Standardize the job title field for all leads in the 'New' stage.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the data steward, interpreting quality rules and executing logic.
- Instruct the agent to prioritize data accuracy and record completeness.
- Define specific formatting rules (e.g., "Always capitalize company names").
- Set the agent to request human confirmation before executing bulk deletions.

### 2) Composio Toolset Node
- Provide your Salesmate API key via the Composio dashboard.
- Set the connection scope to include `read` and `write` permissions for Contacts, Deals, and Accounts.

### 3) Tool Availability
- **List Records**: Retrieve CRM data for analysis.
- **Update Record**: Apply corrections to specific fields.
- **Merge Records**: Consolidate duplicate entries into a single master record.
- **Delete Record**: Remove obsolete or orphaned data points.

---

## Related Solutions
- [../account-research-agent-by-onepage/README.md](../account-research-agent-by-onepage/README.md) - Automate account intelligence gathering.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms.
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) - Monitor account health and compliance status.
