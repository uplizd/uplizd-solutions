# Action Item Prioritizer (Uplizd) - Intelligent task ranking and workflow optimization

## Summary
The Action Item Prioritizer is an automated Uplizd AI workflow designed to streamline project management by dynamically ranking tasks based on urgency, impact, and resource availability. By integrating directly with your existing project management tools via the Composio Toolset, this solution ensures that teams focus on high-leverage activities, reducing operational friction and significantly increasing pipeline velocity.

---

## Demo
![Action Item Prioritizer workflow showing task ingestion, AI-driven prioritization, and automated update to project management tools](image.png)
**Alt text (SEO-ready):** Action Item Prioritizer workflow in Uplizd, automated task ranking, AI project management, Composio integration, and operational efficiency.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/action-item-prioritizer-by-rootly)

---

## Category
**Primary category:** Project management automation  
**Secondary tags:** `task management`, `ai workflow`, `composio`, `productivity`, `pipeline`, `rootly`, `automation`, `data sync`  
This solution bridges the gap between raw task lists and actionable execution by applying intelligent prioritization logic to your project management ecosystem.

---

## Who is this for?
This workflow is built for teams looking to eliminate manual triage and focus on what matters most.

*   **Engineering Managers**
    *   Automatically surface critical bugs and blockers to ensure sprint goals are met without manual oversight.
*   **Product Managers**
    *   Maintain a clean, prioritized backlog that reflects current business objectives and customer feedback.
*   **Operations Leads**
    *   Reduce administrative overhead by automating the classification and assignment of incoming support tickets or tasks.
*   **Individual Contributors**
    *   Receive daily, ranked task lists that highlight the highest-impact work, reducing decision fatigue.

---

## Features
- **Intelligent Task Scoring**
  Uses AI to analyze task descriptions, deadlines, and labels to calculate a priority score.
- **Real-time Tool Synchronization**
  Leverages the Composio Toolset to fetch and update tasks directly in tools like Jira, Linear, or Asana.
- **Context-Aware Routing**
  Automatically assigns tasks to the correct team member based on current workload and expertise.
- **Automated Status Updates**
  Keeps stakeholders informed by pushing priority changes back to the source project management platform.
- **Customizable Logic Gates**
  Allows users to define specific criteria for "Urgent" vs. "High Impact" tasks within the Agent node.

---

## Use Cases
**Backlog Grooming**
*   Automatically move stale, low-priority tasks to a "Backlog" folder to keep the active sprint clean.
*   Flag tasks that have missed multiple deadlines for immediate review by the team lead.

**Incident Response**
*   Prioritize incoming incident reports based on severity levels defined in the metadata.
*   Route critical security patches to the on-call engineer's dashboard instantly.

**Resource Allocation**
*   Balance team workload by re-assigning tasks when a team member's active count exceeds a defined threshold.
*   Identify "bottleneck" tasks that are blocking multiple downstream dependencies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Action Item Prioritizer template from the marketplace.
3. Connect your project management tool credentials via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual request to audit the task list.
*   **Agent**: Processes the task data, applies prioritization logic, and determines the optimal ranking.
*   **Composio Toolset**: Executes the API calls to update task statuses and priority fields in your external tools.
*   **Chat Output**: Returns a summary of the changes made and a list of the top-ranked tasks to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Prioritize the current sprint backlog based on the 'Urgent' label.`
* `Identify all tasks assigned to the engineering team that are currently stalled.`
* `Re-rank the active task list to prioritize items due within the next 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the brain of the operation, interpreting task metadata to make logical ranking decisions.
*   **Instruction Pattern:**
    *   "Analyze the provided task list for urgency and business impact."
    *   "Assign a priority score from 1-10 based on the defined criteria."
    *   "Format the output as a JSON object for the Composio Toolset to process."

### 2) Composio Toolset Node
*   **API Key:** Ensure your project management platform API key is securely stored in the Uplizd environment variables.
*   **Connection Scope:** Grant read/write access to your project management workspace to allow the agent to fetch and update task fields.

### 3) Tool Availability
*   **Task Fetcher:** Retrieves open tasks from your project management board.
*   **Priority Updater:** Updates the priority or status field of a specific task.
*   **Assignment Manager:** Modifies the assignee field based on agent-calculated workload.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales pipeline stages and automate follow-up actions.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and maintain CRM data quality through automated cleanup.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
