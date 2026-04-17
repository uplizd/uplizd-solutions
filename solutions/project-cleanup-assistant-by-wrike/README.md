# Project Cleanup Assistant (Uplizd) - Automate project archiving and workspace hygiene

## Summary
The Project Cleanup Assistant is an intelligent Uplizd workflow designed to streamline project management by automatically identifying, archiving, and organizing completed tasks and projects within Wrike. By automating the transition of stale data to archive states, this solution ensures your workspace remains clutter-free, improves team focus on active initiatives, and maintains a single source of truth for project status.

---

## Demo
![Project Cleanup Assistant workflow showing automated Wrike task archiving and status updates](image.png)
**Alt text (SEO-ready):** Project Cleanup Assistant workflow for Wrike, showing automated project archiving, workspace hygiene, and task management using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2933ee20-cb24-5120-af6b-4f46660236ec)

---

## Category
- **Primary category:** Project management
- **Secondary tags:** wrike, project cleanup, workspace hygiene, automation, data management, workflow optimization, composio, ai agent
- This solution helps teams maintain operational efficiency by automating the lifecycle management of projects and tasks.

---

## Who is this for?
This assistant is designed for teams looking to reduce manual administrative overhead and maintain a clean, actionable project environment.

- **Project Managers**
    - Automatically archive completed projects to keep dashboards focused on current deliverables.
- **Operations Leads**
    - Enforce workspace hygiene standards across the organization without manual oversight.
- **Team Leads**
    - Reduce noise in project views by moving stale tasks to appropriate archive folders.
- **System Administrators**
    - Maintain data integrity and performance by ensuring completed work is systematically offloaded.

---

## Features
- **Automated Archiving**
    - Trigger project moves based on completion status or custom date thresholds in Wrike.
- **Workspace Hygiene Rules**
    - Define custom logic to identify abandoned or stalled projects that require attention.
- **Intelligent Status Mapping**
    - Automatically update task statuses to 'Archived' or 'Completed' upon project closure.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to execute secure, real-time API calls directly to your Wrike instance.
- **Customizable Triggers**
    - Set specific time-based or event-based triggers to run cleanup cycles during off-peak hours.

---

## Use Cases
**Project Lifecycle Management**
- Automatically move projects to an 'Archive' folder once the final milestone is marked as complete.
- Identify projects with no activity for over 30 days and flag them for manager review.

**Workspace Organization**
- Clean up duplicate or test projects created during onboarding by identifying naming patterns.
- Batch update task permissions when a project is transitioned to an archive state.

**Operational Reporting**
- Generate a summary report of all archived projects for quarterly performance reviews.
- Sync archive status across linked tools to ensure consistent data visibility for stakeholders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your Wrike account via the Composio integration portal.
3. Configure your project folder IDs and archive destination settings in the node properties.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup process.
- **Agent**: Processes the logic to determine which projects meet the criteria for archiving.
- **Composio Toolset**: Executes the Wrike API actions to update project status and move folders.
- **Chat Output**: Returns a confirmation log detailing which projects were successfully archived.

### 3) Run the Flow
Use the Playground to test your cleanup logic:
- `Archive all projects in the 'Q1 2024' folder that are marked as completed.`
- `List all projects that have been inactive for more than 60 days.`
- `Move all completed tasks from the 'Marketing' workspace to the 'Archive' folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-maker for your workspace hygiene policy.
- Use a clear, instruction-based prompt to define what constitutes a "completed" project.
- Set the temperature to 0.2 for consistent, rule-based execution.
- Ensure the agent has access to the current project metadata provided by the Wrike toolset.

### 2) Composio Toolset Node
- Provide your Wrike API credentials via the Composio connection manager.
- Ensure the connection scope includes `read` and `write` permissions for project and task management.

### 3) Tool Availability
- **Wrike Project Search**: Locate projects by name, status, or date.
- **Wrike Update Task/Project**: Modify status, folder location, and custom field values.
- **Wrike Folder Management**: Create or move items into designated archive structures.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automate the resolution and cleanup of stale action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and maintain the health of your team's automated workflows.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline the creation and organization of new account structures.
