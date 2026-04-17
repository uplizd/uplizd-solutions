# Client Cleanup Manager (Uplizd) - Automated workspace hygiene and client archiving

## Summary
The Client Cleanup Manager is an intelligent Uplizd workflow designed to streamline workspace maintenance by identifying and archiving inactive clients within Everhour. By automating the detection of stale accounts and executing cleanup tasks, this solution ensures your project management data remains accurate, reduces clutter, and improves pipeline velocity for operations teams.

---

## Demo
![Client Cleanup Manager workflow showing Everhour integration for automated data archiving](../image.png)
**Alt text (SEO-ready):** Client Cleanup Manager (Uplizd) workflow for automated Everhour data hygiene, client archiving, and workspace optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5be72e17-5972-5c8a-9cad-2cd4d333e348)

---

## Category
**Primary category:** Operations  
**Secondary tags:** crm, everhour, data hygiene, workspace management, automation, pipeline, composio, ai workflow  
This solution provides automated data lifecycle management to keep your professional service tools organized and compliant.

---

## Who is this for?
This solution is designed for operations professionals and managers looking to maintain a clean and efficient project environment.

*   **Operations Manager**
    *   Automates the tedious process of auditing and archiving inactive client profiles.
*   **Project Lead**
    *   Ensures team focus remains on active engagements by removing noise from the workspace.
*   **Finance Administrator**
    *   Maintains accurate billing records by ensuring only active clients are tracked in Everhour.
*   **System Administrator**
    *   Reduces data bloat and improves system performance through consistent, automated cleanup routines.

---

## Features
- **Automated Inactivity Detection**
    Real-time monitoring of client activity logs to flag accounts that have exceeded defined engagement thresholds.
- **Everhour Integration**
    Seamless connection via the Composio Toolset to perform secure read/write operations on client data.
- **Customizable Archiving Logic**
    Define specific criteria for what constitutes an "inactive" client, ensuring business-critical data is never accidentally removed.
- **Bulk Cleanup Execution**
    Process multiple client records in a single workflow run, significantly reducing manual administrative overhead.
- **Audit Trail Logging**
    Generates a summary report of all archived entities, providing transparency for compliance and record-keeping.

---

## Use Cases
**Workspace Optimization**
*   Automatically archive clients with no billable hours logged in the last 90 days.
*   Remove test or duplicate client entries that clutter the project dashboard.

**Data Hygiene Management**
*   Flag clients with incomplete profile information for manual review before final archiving.
*   Sync archive status across multiple platforms to ensure consistent data states.

**Operational Efficiency**
*   Schedule weekly cleanup runs to maintain a lean, high-performance workspace environment.
*   Generate monthly reports on archived client volume to track workspace growth and decay.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Everhour account via the Composio Toolset node.
3. Configure your inactivity threshold (e.g., days since last activity) in the Agent instructions.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup.
*   **Agent**: Analyzes client activity data against your defined criteria to identify candidates for archiving.
*   **Composio Toolset**: Executes the API calls to Everhour to update client status or move records to archive.
*   **Chat Output**: Returns a summary report of the cleanup operation, including the number of clients processed.

### 3) Run the Flow
Use the Playground to test your cleanup logic:
* `Identify all clients with no activity in the last 180 days.`
* `Archive all clients marked as 'Completed' in the project folder.`
* `Run a full workspace audit and list clients ready for cleanup.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for the cleanup process.
*   Instruct the agent to prioritize data integrity by verifying the last activity date before archiving.
*   Define the "inactive" threshold clearly within the system prompt.
*   Require the agent to output a structured summary of actions taken for audit purposes.

### 2) Composio Toolset Node
*   Requires an active Everhour API key provided through the Composio connection manager.
*   Ensure the connection scope includes read and write permissions for client and project entities.

### 3) Tool Availability
*   **Everhour Client Search**: Locates client records based on activity timestamps.
*   **Everhour Update Tool**: Modifies the status or archive flag of identified clients.
*   **Data Reporting Tool**: Formats the final cleanup summary for the Chat Output node.

---

## Related Solutions
*   [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) — Streamline your workspace configuration and onboarding.
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency and status of your automated business processes.
*   [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform comprehensive security and data audits across your accounts.
