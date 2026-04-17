# Project Database Archiver (Uplizd) - Automated lifecycle management for Ninox project data

## Summary
The Project Database Archiver by Ninox is an intelligent Uplizd workflow designed to streamline data hygiene by automatically identifying and archiving completed project records. By leveraging the Composio Toolset to interface with Ninox, this solution ensures your active databases remain performant and clutter-free, providing a single source of truth for historical project data while maintaining pipeline velocity.

---

## Demo
![Project Database Archiver workflow showing Ninox data filtering and archival process](image.png)
**Alt text (SEO-ready):** Project Database Archiver workflow by Uplizd, Ninox data archival automation, CRM data hygiene, and automated project record management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d277c08b-ca47-5e27-b18d-edb30a63abaa)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** ninox, database management, automation, data archival, workflow, composio, ai agent, project management
- This solution optimizes database performance by automating the transition of stale project records into archival storage.

---

## Who is this for?
This solution is designed for teams managing high-volume project databases who need to maintain data integrity without manual intervention.

- **Operations Managers**
  - Automate routine data maintenance to focus on high-impact strategic initiatives.
- **Database Administrators**
  - Ensure optimal system performance by offloading completed records to archive tables.
- **Project Leads**
  - Maintain clean, actionable project lists by removing noise from active dashboards.
- **RevOps Specialists**
  - Standardize data lifecycle policies across the organization to improve reporting accuracy.

---

## Features
- **Automated Lifecycle Triggers**
  - Detects project status changes in real-time to initiate archival workflows without manual input.
- **Intelligent Data Filtering**
  - Uses AI-driven logic to distinguish between active, stalled, and completed projects based on custom criteria.
- **Ninox Integration**
  - Leverages the Composio Toolset to securely read and write data directly within your Ninox environment.
- **Compliance-Aware Archiving**
  - Ensures that sensitive project metadata is preserved during the transfer process to meet internal audit requirements.
- **Execution Logging**
  - Provides a detailed audit trail of all archived records for transparency and easy retrieval if needed.

---

## Use Cases
**Project Lifecycle Management**
- Automatically move projects marked as "Closed" or "Completed" to an archive database every Friday.
- Flag projects that have been inactive for over 90 days for manual review before archival.

**Database Performance Optimization**
- Reduce the record count in active Ninox views to improve load times and UI responsiveness.
- Segment historical data into yearly archive tables to simplify long-term reporting and analytics.

**Data Hygiene & Compliance**
- Ensure that PII or sensitive project data is moved to secure, restricted-access archive folders.
- Standardize the archival format across multiple Ninox workspaces to maintain consistent data structures.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Connect your Ninox account via the Composio Toolset interface.
3. Configure the trigger conditions based on your specific project status fields.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual command to begin the archival process.
- **Agent**: Analyzes project status and determines which records meet the archival criteria.
- **Composio Toolset**: Executes the read/write operations within the Ninox API.
- **Chat Output**: Confirms the number of records archived and provides a summary report.

### 3) Run the Flow
Use the Playground to test your archival logic with these prompts:
- `Archive all projects with status 'Completed' from the last quarter.`
- `Identify and move all inactive projects older than 180 days to the archive workspace.`
- `Run a cleanup check on the 'Client Projects' table and report back.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making layer for your data lifecycle policy.
- Use a model capable of logical reasoning to parse project dates and statuses.
- Instruction: "You are a data management assistant. Only archive records that explicitly match the 'Completed' status."
- Instruction: "Always verify the destination table exists before attempting to move data."

### 2) Composio Toolset Node
- Provide your Ninox API key within the Composio connection settings.
- Ensure the connection scope includes read/write permissions for the specific workspaces being managed.

### 3) Tool Availability
- **Ninox List Records**: Fetch project data based on status filters.
- **Ninox Create Record**: Insert data into the designated archive table.
- **Ninox Delete Record**: Remove processed records from the active table upon successful archival.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean CRM records through automated deduplication and formatting.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize project and client data across multiple platforms.
- [Workspace Usage Analyzer](../workspace-usage-analyzer/README.md) - Monitor and optimize the storage and usage patterns of your workspace data.
