# Task Completion Agent (Uplizd) - Automate Salesforce task management and routine updates

## Summary
The Task Completion Agent is an intelligent Uplizd workflow designed to streamline sales operations by automating the lifecycle of routine tasks within Salesforce. By leveraging the Composio Toolset, the agent identifies pending items, executes updates, and appends detailed notes, ensuring your CRM remains a single source of truth. This solution enhances pipeline velocity and data hygiene, allowing sales teams to focus on high-value activities rather than manual administrative upkeep.

---

## Demo
![Task Completion Agent workflow interface showing automated Salesforce task updates and note synchronization](image.png)

**Alt text (SEO-ready):** Uplizd Task Completion Agent workflow for Salesforce, showing automated task status updates, note synchronization, and CRM data management integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1a1f7fa0-c0b6-5082-84a1-4de30b4e16f6)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** salesforce, crm, task management, automation, data hygiene, pipeline, composio, ai workflow

This solution bridges the gap between daily sales activities and CRM record-keeping to ensure consistent data entry.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual CRM overhead and improve operational efficiency.

- **Sales Operations Manager**
    - Standardizes task completion protocols across the entire sales organization.
- **Account Executive**
    - Eliminates repetitive data entry, allowing more time for client-facing interactions.
- **Sales Development Representative**
    - Ensures that follow-up activities are logged and updated in real-time without manual intervention.
- **Revenue Operations Lead**
    - Maintains high-quality CRM data hygiene by automating the logging of routine task outcomes.

---

## Features
- **Automated Task Updates**
    - Instantly transition task statuses in Salesforce based on AI-driven triggers or natural language input.
- **Contextual Note Generation**
    - Automatically generate and append detailed completion notes to Salesforce tasks based on interaction history.
- **Composio Toolset Integration**
    - Utilizes secure, authenticated connections to Salesforce to perform CRUD operations on tasks and activities.
- **Real-time CRM Sync**
    - Ensures that updates made within the Uplizd workflow are reflected immediately in your Salesforce environment.
- **Intelligent Error Handling**
    - Validates task requirements before execution to prevent data conflicts and ensure compliance with CRM field rules.

---

## Use Cases
**Routine Sales Administration**
- Automatically mark "Follow-up" tasks as complete after an email or call interaction is logged.
- Update task priority levels based on the outcome of recent client communications.

**Pipeline Velocity Optimization**
- Trigger automated task creation for the next stage in the sales cycle once a current task is completed.
- Sync activity logs across multiple related opportunities to provide a unified view of account progress.

**Data Hygiene and Reporting**
- Standardize the formatting of completion notes to ensure reporting dashboards provide accurate, readable insights.
- Audit and close stale tasks that have passed their due date to keep the sales pipeline clean and actionable.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Task Completion Agent template from the solution library.
3. Connect your Salesforce account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language commands regarding task status updates.
- **Agent**: Processes instructions and determines the necessary Salesforce API calls.
- **Composio Toolset**: Executes the specific Salesforce actions (e.g., `updateTask`, `addNote`).
- **Chat Output**: Confirms the successful completion of the task update to the user.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Mark the task 'Follow up with Acme Corp' as completed and add a note that the client requested a demo next week.`
- `Update the status of all overdue tasks for the current account to 'Deferred'.`
- `Find the task related to 'Q3 Renewal' and append a note stating the contract was sent for signature.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for CRM interactions.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5).
- **Recommended instruction pattern:**
    - Always verify the Task ID before attempting an update.
    - Summarize interaction notes concisely to fit within Salesforce character limits.
    - If a task is not found, ask the user for the specific Task ID or Subject line.

### 2) Composio Toolset Node
- Provide your Salesforce API credentials within the Composio dashboard.
- Ensure the connection scope includes `api`, `refresh_token`, and `full` access to tasks and activities.

### 3) Tool Availability
- `salesforce_update_task`: Modify status, priority, or completion date.
- `salesforce_add_task_note`: Append text to the activity history.
- `salesforce_search_tasks`: Locate tasks by subject, date, or owner.

---

## Related Solutions
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the creation and configuration of new accounts in Salesforce.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and identifies stalled deals for SalesOps.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Cleans and standardizes CRM data to prevent decay and ensure compliance.
