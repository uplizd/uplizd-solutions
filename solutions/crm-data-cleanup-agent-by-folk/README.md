# CRM Data Cleanup Agent (Uplizd) - Automated Folk CRM hygiene and duplicate resolution

## Summary
The CRM Data Cleanup Agent is an intelligent Uplizd workflow designed to maintain data integrity within Folk CRM by automatically identifying and merging duplicate records. By leveraging AI-driven analysis, this solution ensures your contact and company databases remain accurate, reducing manual administrative overhead and improving pipeline velocity through reliable, clean customer data.

---

## Demo
![CRM Data Cleanup Agent dashboard showing duplicate contact detection and merge confirmation in Folk CRM](image.png)
**Alt text (SEO-ready):** CRM Data Cleanup Agent for Folk CRM, showing automated duplicate detection, contact merging, and data hygiene workflow in Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=appveyor)](https://uplizd.ai/solutions/6340a205-79e3-5357-905e-fb28b00e9553)

---

## Category
- **Primary category:** CRM data hygiene
- **Secondary tags:** folk, crm, data cleaning, deduplication, automation, composio, ai workflow, sales operations
- This solution bridges the gap between raw CRM data and actionable intelligence by automating the tedious process of record reconciliation.

---

## Who is this for?
This workflow is designed for teams managing high-volume contact databases who need to prevent data decay and maintain a single source of truth.

- **Sales Operations Manager**
    - Automates routine data maintenance, allowing the team to focus on closing deals rather than manual record management.
- **CRM Administrator**
    - Ensures the database remains compliant and organized without requiring custom scripts or complex manual exports.
- **Account Executive**
    - Eliminates confusion caused by duplicate contact entries, ensuring all interaction history is consolidated in one place.
- **Growth Marketer**
    - Improves campaign targeting accuracy by ensuring outreach lists are clean, deduplicated, and ready for segmentation.

---

## Features
- **Intelligent Deduplication**
    - Uses AI to identify duplicate contacts and companies based on fuzzy matching of names, emails, and domains.
- **Automated Merge Logic**
    - Safely merges redundant records while preserving the most recent interaction data and custom field values.
- **Folk CRM Integration**
    - Utilizes the Composio Toolset to securely read and write directly to your Folk CRM environment.
- **Real-time Data Hygiene**
    - Runs on-demand or on a schedule to catch new duplicates as soon as they are introduced into the system.
- **Audit Logging**
    - Provides a clear record of all merged entities, allowing for easy verification of changes made to the database.

---

## Use Cases
**Database Maintenance**
- Automatically merge duplicate contact records created by multiple team members during lead entry.
- Consolidate company profiles that share the same domain but have slightly different naming conventions.

**Sales Pipeline Optimization**
- Ensure that all historical communication logs are centralized under a single, primary contact record.
- Prevent duplicate outreach efforts by maintaining a clean, unified view of every prospect's status.

**Compliance and Reporting**
- Standardize contact information across the CRM to ensure accurate reporting on lead sources and conversion rates.
- Remove stale or redundant records to keep CRM usage within storage limits and improve search performance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your Folk CRM account via the Composio Toolset node.
3. Configure your desired matching threshold in the Agent node settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command to initiate the cleanup process.
- **Agent**: Analyzes the CRM data and determines which records are duplicates based on provided logic.
- **Composio Toolset**: Executes the API calls to fetch, compare, and merge records within Folk CRM.
- **Chat Output**: Returns a summary report of all records processed and merged during the session.

### 3) Run the Flow
Open the Uplizd Playground and use the following prompts:
- `Find and merge all duplicate contacts in my CRM.`
- `Scan for company records with the same domain and merge them.`
- `Clean up my database by identifying redundant entries for the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for record reconciliation.
- Instruct the agent to prioritize records with the most recent activity timestamps.
- Define specific fields (e.g., email, phone) as primary keys for duplicate identification.
- Set a confidence threshold to require manual approval for high-risk merges.

### 2) Composio Toolset Node
- Provide your Folk CRM API key within the Composio configuration.
- Ensure the connection scope includes read/write permissions for contacts and companies.

### 3) Tool Availability
- `folk_get_contacts`: Retrieve existing contact lists for analysis.
- `folk_merge_records`: Execute the consolidation of identified duplicate entities.
- `folk_search_companies`: Identify company records sharing identical domain identifiers.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms to ensure consistency.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Advanced tools for formatting and compliance-aware data cleanup.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Enrich your CRM records with external account intelligence.
