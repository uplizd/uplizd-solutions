# Deadline Escalation Manager (Uplizd) - Automated project risk mitigation and task prioritization

## Summary
The Deadline Escalation Manager is an intelligent Uplizd workflow designed to proactively identify at-risk tasks within Wrike, automatically triggering escalation protocols and resource reallocation requests. By bridging the gap between project management data and real-time communication, this solution ensures that project managers and team leads maintain pipeline velocity and prevent critical bottlenecks before they impact delivery timelines.

---

## Demo
![Deadline Escalation Manager workflow showing Wrike task monitoring and automated notification triggers](image.png)
**Alt text (SEO-ready):** Deadline Escalation Manager workflow in Uplizd, featuring Wrike integration for automated project risk mitigation, task escalation, and resource reallocation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4d3e64da-7f0f-542e-8bb3-2835c2bd7585)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** wrike, project management, task automation, escalation, resource allocation, pipeline velocity, workflow, ai agent
- This solution streamlines operational oversight by automating the identification and escalation of stalled or high-risk project tasks.

---

## Who is this for?
This solution is designed for operations teams and project managers who need to maintain strict delivery schedules across complex project portfolios.

- **Project Manager**
    - Automates the identification of stalled tasks to prevent project slippage.
- **Operations Lead**
    - Ensures resource allocation remains aligned with shifting project priorities.
- **Team Lead**
    - Receives real-time alerts for critical path items requiring immediate intervention.
- **Resource Manager**
    - Gains visibility into capacity constraints caused by unexpected deadline pressures.

---

## Features
- **Automated Risk Detection**
    - Monitors Wrike task statuses and due dates in real-time to flag potential delays before they occur.
- **Intelligent Escalation Logic**
    - Triggers automated notifications to stakeholders based on predefined urgency levels and project impact.
- **Resource Reallocation Support**
    - Suggests adjustments to task assignments to balance workloads when deadlines are at risk.
- **Composio-Powered Wrike Integration**
    - Leverages the Composio Toolset to securely read, update, and manage task metadata directly within Wrike.
- **Customizable Thresholds**
    - Allows users to define specific time-based or priority-based triggers for escalation workflows.

---

## Use Cases
**Proactive Risk Management**
- Automatically flag tasks that remain in a "In Progress" state within 24 hours of their due date.
- Escalate high-priority project items to the relevant department head if no update is provided by the assignee.

**Resource Optimization**
- Identify team members with overloaded schedules and suggest task reassignments to underutilized staff.
- Generate weekly reports on recurring bottleneck patterns to improve future project planning.

**Communication & Alignment**
- Send automated Slack or email summaries to stakeholders when project milestones are missed.
- Sync escalation status back to Wrike custom fields to ensure a single source of truth for all project stakeholders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deadline Escalation Manager template from the solution library.
3. Connect your Wrike account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal from the Wrike webhook or manual user query.
- **Agent**: Analyzes task urgency and determines the appropriate escalation path.
- **Composio Toolset**: Executes read/write operations within Wrike to update task status or assign resources.
- **Chat Output**: Delivers the summary of actions taken to the project dashboard or communication channel.

### 3) Run the Flow
Use the Playground to test your escalation logic with these prompts:
- `Check for all high-priority tasks in Wrike due within the next 48 hours and flag those without an update.`
- `Escalate the 'Q3 Marketing Launch' project tasks that are currently stalled to the Project Lead.`
- `Identify tasks assigned to 'John Doe' that are past due and suggest a redistribution of work.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, interpreting project data and applying business logic.
- **Instruction Pattern:**
    - Focus on identifying "at-risk" status based on current date vs. task due date.
    - Prioritize tasks marked as "High Priority" in Wrike metadata.
    - Maintain a professional, objective tone when drafting escalation notifications.

### 2) Composio Toolset Node
- Requires an active Wrike API key configured within the Composio platform.
- Connection scope should include `read_tasks`, `update_tasks`, and `list_users` to facilitate effective resource management.

### 3) Tool Availability
- `wrike_get_task`: Retrieve specific task details and current status.
- `wrike_update_task`: Update task priority, assignee, or custom fields.
- `wrike_list_tasks`: Scan project folders for upcoming or overdue deadlines.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor overall team productivity and workflow efficiency.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track account-level health metrics and usage patterns.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automatically rank and assign action items based on urgency.
