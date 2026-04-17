# Project Cleanup Assistant (Uplizd) - Automated project archiving and workspace organization

## Summary
The Project Cleanup Assistant is an intelligent Uplizd workflow designed to streamline project management by automatically identifying, organizing, and archiving completed tasks and projects. By leveraging the Composio Toolset to interface with your project management platforms, this solution ensures your workspace remains clutter-free, improving team focus and data hygiene without manual intervention.

---

## Demo
![Project Cleanup Assistant workflow interface showing automated archiving logic](image.png)
**Alt text (SEO-ready):** Uplizd project cleanup assistant workflow for automated project archiving, data hygiene, and workspace management using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/da0728a6-ec1c-576d-924d-854e591f54e4)

---

## Category
**Primary category:** Productivity automation
**Secondary tags:** project management, data hygiene, workflow automation, archiving, composio, workspace optimization, task management, ai agent.
This solution bridges the gap between active project tracking and long-term data maintenance by automating the lifecycle of completed work items.

---

## Who is this for?
This solution is designed for teams looking to maintain high-velocity workspaces and clear project documentation.

*   **Project Managers**
    *   Reduce administrative overhead by automating the transition of projects from active to archived status.
*   **Operations Leads**
    *   Maintain consistent workspace hygiene across the organization to ensure reporting accuracy.
*   **Team Leads**
    *   Prevent task fatigue by clearing completed items from active dashboards and views.
*   **DevOps Engineers**
    *   Automate the cleanup of stale project resources and tickets to keep integration pipelines lean.

---

## Features
- **Automated Status Detection**
    Real-time monitoring of project boards to identify items marked as "Completed" or "Done" based on custom triggers.
- **Intelligent Archiving Logic**
    Conditional logic that moves completed projects to designated archive folders or status buckets, keeping active views clean.
- **Composio Toolset Integration**
    Seamless connectivity with popular project management platforms to execute read/write actions securely.
- **Data Hygiene Reporting**
    Automatic logging of archived items, providing a clear audit trail of completed work for stakeholders.
- **Customizable Cleanup Rules**
    Flexible configuration settings to define what constitutes a "completed" project, including time-based or status-based triggers.

---

## Use Cases
**Workspace Maintenance**
*   Automatically archive projects that have remained in a "Completed" status for more than 30 days.
*   Move completed sub-tasks to a separate archive database to reduce noise in primary project views.

**Resource Management**
*   Trigger cleanup workflows to close out project-related tickets once the primary project status is updated.
*   Flag incomplete projects that have missed their deadline for manual review by the project manager.

**Compliance and Auditing**
*   Generate a monthly summary of all archived projects to ensure documentation standards are met.
*   Sync project archive status across multiple platforms to maintain a single source of truth for project history.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Cleanup Assistant template from the solution library.
3. Connect your project management tool credentials via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual command to initiate the cleanup process.
*   **Agent**: Evaluates project status against your defined criteria and determines which items require archiving.
*   **Composio Toolset**: Executes the API calls to update project statuses and move items to archive folders.
*   **Chat Output**: Confirms the number of projects processed and provides a summary of the cleanup actions taken.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
* `Identify all projects marked as 'Done' and move them to the 'Archive' folder.`
* `List all projects that haven't been updated in 60 days for review.`
* `Run the cleanup routine for the 'Q3 Marketing' project board.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for your project lifecycle.
*   Instruct the agent to prioritize accuracy when identifying project statuses.
*   Define clear "archive" criteria to prevent accidental deletion of active work.
*   Set the agent to provide a concise summary report after every execution.

### 2) Composio Toolset Node
*   Provide your API key for the target project management platform (e.g., Jira, Asana, Trello).
*   Ensure the connection scope includes read/write permissions for project and task objects.

### 3) Tool Availability
*   **Project Fetcher**: Retrieves current project lists and statuses.
*   **Status Updater**: Modifies project or task status fields.
*   **Archive Mover**: Transfers items to designated archive containers.
*   **Audit Logger**: Records all cleanup actions to an external log or chat output.

---

## Related Solutions
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automates the identification and resolution of stale action items.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the efficiency and status of team workflows.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitors account activity and usage patterns for better data management.
