# Box Storage Optimizer (Uplizd) - Intelligent file lifecycle and storage management

## Summary
The Box Storage Optimizer is an automated AI workflow designed to streamline cloud storage hygiene by identifying stale files, managing folder permissions, and optimizing storage consumption. By leveraging the Composio Toolset to interface directly with Box, this solution enables IT administrators and operations teams to maintain a lean, secure, and organized digital workspace, reducing manual cleanup efforts and ensuring compliance with data retention policies.

---

## Demo
![Box Storage Optimizer workflow interface showing file cleanup and storage analysis nodes](image.png)
**Alt text (SEO-ready):** Box Storage Optimizer workflow interface showing automated file cleanup, storage analysis, and cloud data management using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/96948f53-41c6-5230-99ef-680d0a368bb8)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** box, cloud storage, data hygiene, storage optimization, automation, file management, composio, ai workflow
- This solution bridges the gap between raw cloud storage data and actionable cleanup tasks, providing a centralized hub for enterprise storage governance.

---

## Who is this for?
This solution is designed for professionals responsible for maintaining efficient and secure cloud storage environments.

- **IT Administrators**
    - Automate the identification and archival of inactive files to reclaim storage space.
- **Operations Managers**
    - Enforce data retention policies across departmental folders to maintain organizational hygiene.
- **Security Officers**
    - Audit folder permissions and identify public-facing links that pose potential data leakage risks.
- **Cloud Infrastructure Leads**
    - Monitor storage consumption trends to forecast capacity needs and optimize subscription costs.

---

## Features
- **Automated Stale File Detection**
    - Uses AI to scan Box directories for files that haven't been accessed in a specified timeframe, flagging them for archival or deletion.
- **Permission Audit Engine**
    - Automatically identifies folders with overly permissive access settings, allowing for rapid remediation of security gaps.
- **Intelligent Storage Reporting**
    - Generates real-time summaries of storage usage by user or department, providing visibility into high-consumption areas.
- **Composio-Powered Box Integration**
    - Seamlessly connects to Box APIs to execute file operations, metadata updates, and user permission changes without manual intervention.
- **Customizable Cleanup Policies**
    - Allows users to define specific exclusion rules and retention thresholds to ensure critical business data is never accidentally purged.

---

## Use Cases
**Storage Hygiene & Cleanup**
- Automatically move files older than 180 days to an "Archive" folder to reduce clutter.
- Identify and delete duplicate files across shared workspaces to optimize storage quotas.

**Security & Governance**
- Scan for files shared via "Public Link" and automatically restrict access to internal-only.
- Audit folder ownership to ensure that terminated employees no longer have administrative control over critical assets.

**Capacity Planning**
- Generate weekly reports on storage growth rates to help IT teams plan for license upgrades.
- Identify "heavy" users or departments to provide targeted training on storage best practices.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `box-storage-optimizer-by-box` configuration file.
3. Connect your Box account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language commands (e.g., "Find old files").
- **Agent**: Processes storage logic and determines which Box API calls are required.
- **Composio Toolset**: Executes the specific Box operations (list, delete, move, update).
- **Chat Output**: Returns a summary report of the actions taken or files identified.

### 3) Run the Flow
Use the Playground to test your storage management prompts:
- `Find all files in the 'Marketing' folder that haven't been modified in over 6 months.`
- `List all folders currently shared with external collaborators.`
- `Move all files in the 'Temporary' folder to the 'Archive' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for storage policy enforcement.
- Use a model with strong reasoning capabilities to interpret file metadata.
- Configure system instructions to prioritize data safety and confirmation before deletion.
- Set the temperature to 0.2 to ensure consistent and predictable file handling.

### 2) Composio Toolset Node
- Provide a valid Box API key with `root_readwrite` scope.
- Ensure the connection is authorized for the specific Box Enterprise ID you wish to manage.

### 3) Tool Availability
- **Box List Files**: For scanning directory contents.
- **Box Update File/Folder**: For moving or renaming assets.
- **Box Delete/Archive**: For executing cleanup tasks.
- **Box Permission Manager**: For auditing and modifying access levels.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Comprehensive security and access auditing for enterprise accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracking and reporting on the status of automated business processes.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Specialized tools for managing and auditing user permissions.
