# Research Archive Cleaner (Uplizd) - Automated workspace maintenance for Dovetail research archives

## Summary
The Research Archive Cleaner is an intelligent Uplizd workflow designed to maintain high-signal research environments by automatically identifying, categorizing, and archiving completed projects within Dovetail. By automating the transition from active research to long-term storage, this solution reduces workspace clutter, improves knowledge retrieval speed, and ensures team-wide adherence to data hygiene standards without manual intervention.

---

## Demo
![Research Archive Cleaner workflow interface showing project filtering and archival status](image.png)
**Alt text (SEO-ready):** Uplizd Research Archive Cleaner workflow interface showing automated project filtering, Dovetail integration, and archival status for research operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bec7142e-5d29-52cf-94bd-eb88d30400e9)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** research, dovetail, data hygiene, archive, automation, knowledge management, workflow, productivity
- This solution streamlines research operations by enforcing automated lifecycle management for project data.

---

## Who is this for?
This solution is designed for research and operations teams looking to scale their insights repository while maintaining organizational clarity.

- **Research Operations Manager**
    - Ensures the research workspace remains performant and free of stale, completed project data.
- **UX Researcher**
    - Focuses on active discovery by offloading the administrative burden of project archival and status updates.
- **Knowledge Manager**
    - Maintains a clean, searchable source of truth by enforcing consistent archival naming and storage conventions.
- **Product Designer**
    - Quickly locates relevant historical insights by ensuring only active, high-priority projects occupy the primary workspace.

---

## Features
- **Automated Project Lifecycle**
    - Triggers archival actions based on project completion status or defined inactivity thresholds within Dovetail.
- **Intelligent Metadata Tagging**
    - Automatically applies standardized tags to archived projects to ensure future searchability and compliance.
- **Bulk Archival Processing**
    - Efficiently handles large volumes of completed research assets to prevent workspace bloat during high-velocity cycles.
- **Cross-Platform Sync**
    - Leverages the Composio Toolset to bridge Dovetail project status with external notification or logging systems.
- **Customizable Archival Logic**
    - Allows teams to define specific criteria for what constitutes a "completed" project, ensuring no critical data is moved prematurely.

---

## Use Cases
**Workspace Maintenance**
- Automatically archive projects marked as "Finalized" in the project dashboard after a 7-day grace period.
- Move inactive research projects to a dedicated "Archive" folder to improve workspace load times.

**Data Governance**
- Enforce naming conventions on archived projects to ensure consistent taxonomy across the entire research organization.
- Audit project permissions during the archival process to restrict access to sensitive historical data.

**Operational Efficiency**
- Notify stakeholders via Slack or email once a research project has been successfully transitioned to the archive.
- Generate a summary report of archived projects to keep leadership informed of research output and repository growth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Research Archive Cleaner template from the solution library.
3. Connect your Dovetail API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup process.
- **Agent**: Processes project metadata and evaluates archival criteria against current workspace status.
- **Composio Toolset**: Executes the API calls to update project status and move files within Dovetail.
- **Chat Output**: Confirms successful archival and provides a summary log of processed projects.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Archive all projects marked as 'Completed' in the last 30 days.`
- `Identify and archive projects with no activity for over 3 months.`
- `Run a dry-run report of projects eligible for archival without moving them.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision engine for project lifecycle management.
- Use a model with strong reasoning capabilities to interpret project status fields accurately.
- Instruct the agent to prioritize data integrity and error handling during bulk operations.
- Configure the system prompt to strictly adhere to the defined archival criteria provided in the input.

### 2) Composio Toolset Node
- Provide a valid Dovetail API key with read/write permissions for projects and folders.
- Ensure the connection scope includes `project:write` and `folder:manage` capabilities.

### 3) Tool Availability
- **Project Fetcher**: Retrieves lists of projects based on status and date filters.
- **Status Updater**: Modifies project metadata to trigger archival states.
- **Folder Manager**: Handles the movement of project assets into designated archive directories.
- **Notification Utility**: Sends confirmation logs to designated team channels.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates gathering and organizing account intelligence.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Maintains hygiene by resolving stale action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and efficiency of automated processes.
