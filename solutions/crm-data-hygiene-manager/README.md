# CRM Data Hygiene Manager (Uplizd) - Automated Maintenance for a Pristine CRM

## Summary
A Uplizd AI workflow that acts as a continuous "cleanup crew" for your CRM, automatically identifying and fixing data decay, formatting errors, and obsolete records to ensure peak system performance.

---

## Demo

![Uplizd CRM Data Hygiene Manager flow identifying and fixing data decay and formatting errors in CRM](../image.png)

**Alt text (SEO-ready):** Uplizd CRM Data Hygiene Manager scanning and cleaning CRM records to maintain high data quality and system hygiene.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/8ae36f06-4dc8-5f19-8c30-3830e5e1ff27/)

---
## Who is this for?
This workflow is built for organizations that struggle with "data rot" and want to automate the maintenance of their customer database:

- CRM Administrators
    - Automate the routine tasks of cleaning up old data and enforcing data entry standards.

- Marketing Operations (MOps)
    - Ensure your email lists are always clean and your segments are accurate for every campaign.

- Sales Managers
    - Give your reps a CRM they actually trust by removing clutter and fixing broken records.

- Data Compliance Officers
    - Automatically flag or remove data that no longer meets retention policies or GDPR standards.

---

## Features

- **Continuous Data Scanning**  
  Proactively monitors your CRM for records with missing info, invalid formats, or "junk" data.

- **Automated Formatting Fixes**  
  Instantly fixes common issues like inconsistent phone formats, improper capitalization, and whitespace.

- **Obsolete Record Identification**  
  Flags contacts and companies that have been inactive for a predefined period for archiving or deletion.

- **Data Decay Prevention**  
  Uses AI to verify if information is still current (e.g., checking if a company still exists or a contact has moved).

- **Hygiene Health Reporting**  
  Provides a summary of the "health" of your CRM and the specific actions taken during each cleanup cycle.

---

## Use Cases

- **Cleanup Lead Ingestion**
  - Automatically clean up leads coming from low-quality web forms before they hit the sales queue.
  - Standardize "Job Titles" into a set of predefined categories for better segmentation.

- **Annual Database Refresh**
  - Run a comprehensive scan to identify "dead" emails and outdated company profiles.
  - Archive or delete records that haven't been touched in over 24 months.

- **Data Quality Enforcement**
  - Enforce "United States" instead of "US" or "USA" across all address fields.
  - Standardize company names (e.g., "Google Inc" to "Google").

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
5. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Composio Toolset**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → receives cleanup commands or maintenance schedules.
- **Agent** → decide which hygiene rules to apply based on the request.
- **Composio Toolset** → provides tools for bulk record updates and validation services.
- **Chat Output** → confirmation of cleanup tasks and records improved.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Enter a request such as:
   - `"Clean up all records with missing phone numbers"`
   - `"Standardize the 'Industry' field for all accounts"`
   - `"Identify contacts that haven't opened an email in 1 year"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is focused on data maintenance and quality control.

Recommended instruction pattern:
- Enforce strict formatting rules
- Prioritize accuracy over speed
- Never delete data without a clear "archival" step or confirmation

### 2) Composio Toolset Node
Requires your **Composio API Key** and a connection to your CRM (Salesforce, HubSpot, etc.).

### 3) Tool Availability
The agent can call tools for:
- Bulk data updates
- Record deletion and archival
- Format validation and correction
- CRM list/segment retrieval

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[Deal Pipeline Manager](../deal-pipeline-manager/README.md)**  
  Automatically update deal progress and create follow-up tasks for your sales team.

* **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.
