# Action Item Cleanup Agent (Uplizd) - Automate task archival and workspace hygiene

## Summary
The Action Item Cleanup Agent is an intelligent workflow designed to streamline project management by automatically identifying, archiving, and purging completed or obsolete action items. By leveraging the Composio Toolset to interface with your task management platforms, this agent ensures your workspace remains clutter-free, improving pipeline velocity and maintaining a single source of truth for active project deliverables.

---

## Demo
![Action Item Cleanup Agent workflow interface showing automated task filtering and archival logic](image.png)
**Alt text (SEO-ready):** Uplizd Action Item Cleanup Agent workflow interface showing automated task filtering, archival logic, and task management integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/eadfb174-717a-51a9-bfbb-47a6ebeb70a3)

---

## Category
**Primary category:** Operations
**Secondary tags:** task management, data hygiene, workflow automation, project management, composio, ai agent, productivity, cleanup

This solution optimizes operational efficiency by automating the maintenance of task databases and project boards.

---

## Who is this for?
This agent is designed for teams looking to reduce manual administrative overhead and maintain high-quality project data.

*   **Project Managers**
    *   Automate the archival of completed sprints to keep boards focused on current priorities.
*   **Operations Leads**
    *   Enforce data hygiene policies across the organization by purging obsolete action items.
*   **Team Leads**
    *   Reduce cognitive load for team members by ensuring only active, relevant tasks appear in daily views.
*   **System Administrators**
    *   Maintain platform performance and organization by preventing the accumulation of stale data.

---

## Features
- **Automated Task Filtering**
  Utilizes intelligent criteria to distinguish between active, pending, and completed action items across your integrated platforms.
- **Smart Archival Logic**
  Automatically moves resolved tasks to archive folders or status buckets based on pre-defined temporal rules.
- **Obsolete Item Detection**
  Identifies tasks that have remained stagnant beyond a set threshold, flagging them for review or automated removal.
- **Composio-Powered Integration**
  Seamlessly connects with popular task management tools to execute cleanup actions without manual intervention.
- **Customizable Cleanup Rules**
  Allows users to define specific triggers and conditions for what constitutes a "completed" or "obsolete" item.

---

## Use Cases
**Project Lifecycle Management**
*   Automatically archive tasks marked as "Done" older than 30 days to clear project backlogs.
*   Move abandoned tasks from the current sprint to a "Future Consideration" board to maintain focus.

**Operational Data Hygiene**
*   Identify and remove duplicate action items created by accidental sync errors or user input.
*   Batch-update status fields for tasks that have missed their due dates by more than two weeks.

**Team Productivity Optimization**
*   Clean up personal task lists by archiving items that have been marked as "Won't Do" or "Cancelled."
*   Generate a weekly summary report of all archived items for management review before final deletion.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your task management tool via the Composio connection prompt.
4. Ensure nodes are correctly mapped and all API credentials are saved in the configuration panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or scheduled interval instructions.
*   **Agent**: Processes the cleanup logic based on your defined archival rules.
*   **Composio Toolset**: Executes the API calls to archive or delete tasks in your connected platform.
*   **Chat Output**: Confirms the number of items processed and provides a summary of actions taken.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
* `Archive all tasks in the 'Q3 Project' board that have been marked as 'Completed' for more than 14 days.`
* `Identify and move all tasks with a 'Stale' status older than 30 days to the 'Archive' folder.`
* `Clean up my workspace by removing all tasks that were cancelled or marked as 'Won't Do' last month.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for task categorization.
*   Follow strict rules for identifying "Completed" vs "Obsolete" status.
*   Prioritize data safety by requiring confirmation for bulk deletions.
*   Maintain a neutral, professional tone in the summary output.

### 2) Composio Toolset Node
Requires an active API key for your task management platform (e.g., Jira, Asana, Trello). Ensure the connection scope includes "Read" and "Write" permissions for task management objects.

### 3) Tool Availability
*   **Task Retrieval**: Fetching lists of items based on status and date filters.
*   **Task Update**: Modifying status fields or moving items to archive boards.
*   **Task Deletion**: Securely removing obsolete records from the workspace.

---

## Related Solutions
* [Action Item Prioritizer (../action-item-prioritizer-by-rootly/README.md)](../action-item-prioritizer-by-rootly/README.md) - Organize and rank incoming tasks by urgency and impact.
* [Workflow Health Monitor (../workflow-health-monitor-by-dailybot/README.md)](../workflow-health-monitor-by-dailybot/README.md) - Track the efficiency and status of your team's automated workflows.
* [CRM Data Hygiene Manager (../crm-data-hygiene-manager/README.md)](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate records within your CRM ecosystem.
