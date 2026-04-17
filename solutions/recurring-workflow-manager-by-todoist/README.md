# Recurring Workflow Manager (Uplizd) - Automate and scale repetitive task sequences

## Summary
The Recurring Workflow Manager by Todoist is an intelligent automation solution designed to streamline repetitive task sequences and project management cycles. By leveraging the Uplizd AI engine and Composio Toolset, this workflow eliminates manual scheduling overhead, ensures consistent task execution, and provides teams with a single source of truth for recurring operational requirements.

---

## Demo
![Recurring Workflow Manager dashboard showing automated task creation and scheduling in Todoist](image.png)
**Alt text (SEO-ready):** Recurring Workflow Manager dashboard showing automated task creation and scheduling in Todoist, powered by Uplizd AI workflow and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8e274644-490f-5836-8049-1122621ef52e)

---

## Category
**Primary category:** Operations
**Secondary tags:** todoist, task management, workflow automation, productivity, recurring tasks, task scheduling, composio, ai workflow.
This solution bridges the gap between static task lists and dynamic, AI-driven operational management.

---

## Who is this for?
This solution is designed for teams and individuals looking to eliminate manual administrative friction in their daily operations.

*   **Project Managers**
    *   Automate the creation of recurring project milestones and status check-ins without manual entry.
*   **Operations Leads**
    *   Standardize operational checklists to ensure compliance and consistency across recurring business cycles.
*   **Team Leads**
    *   Reduce administrative burden on direct reports by automating routine task assignments.
*   **Individual Contributors**
    *   Maintain focus on high-impact work by offloading repetitive maintenance tasks to an intelligent agent.

---

## Features
- **Intelligent Scheduling**
    Automates the generation of tasks based on custom intervals, ensuring no recurring item is ever missed.
- **Composio Integration**
    Seamlessly connects with Todoist to read, write, and update tasks in real-time using secure API authentication.
- **Dynamic Task Context**
    Allows the AI agent to inject relevant project metadata and priority levels into every generated task.
- **Error-Resilient Execution**
    Monitors workflow health to ensure that if a connection drops, tasks are queued and retried automatically.
- **Centralized Oversight**
    Provides a clear audit trail of all automated task creations within the Uplizd interface.

---

## Use Cases
**Routine Project Maintenance**
*   Automatically generate weekly project status update tasks for all active client accounts.
*   Create recurring end-of-month cleanup tasks for project backlogs.

**Operational Compliance**
*   Schedule recurring security audit tasks to ensure team adherence to internal protocols.
*   Automate the creation of quarterly performance review preparation tasks.

**Team Productivity**
*   Sync recurring meeting preparation tasks to team members' Todoist boards 24 hours before scheduled sessions.
*   Automate daily stand-up task reminders to keep remote teams aligned.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your Todoist account within the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or schedule parameters.
*   **Agent**: Processes the logic and determines the task frequency and content.
*   **Composio Toolset**: Executes the creation of tasks directly within your Todoist project.
*   **Chat Output**: Confirms successful task creation or alerts the user to scheduling conflicts.

### 3) Run the Flow
Use the Playground to test your automation with these prompts:
* `Create a recurring task in the 'Marketing' project to 'Review Analytics' every Monday at 9 AM.`
* `Set up a daily task for 'Team Sync' in the 'General' folder for the next 30 days.`
* `List all existing recurring tasks in my 'Operations' project and verify their next due dates.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for task logic and natural language interpretation.
*   **Instruction Pattern:**
    *   "You are an expert task management assistant; interpret natural language requests into specific Todoist task parameters."
    *   "Always verify the project ID before attempting to create or modify tasks."
    *   "If a requested frequency is ambiguous, ask the user for clarification before proceeding."

### 2) Composio Toolset Node
*   **API Key:** Provide your Todoist API token via the Composio dashboard.
*   **Connection Scope:** Ensure the agent has `task:write` and `project:read` permissions enabled.

### 3) Tool Availability
*   `todoist_create_task`: Creates new tasks with specific due dates and priorities.
*   `todoist_get_projects`: Retrieves project IDs for accurate task routing.
*   `todoist_list_tasks`: Audits existing tasks to prevent duplication.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and reliability of your automated task pipelines.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on urgency and impact.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Maintain hygiene in your task management systems by archiving stale items.
