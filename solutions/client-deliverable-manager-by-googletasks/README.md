# Client Deliverable Manager (Uplizd) - Automated project milestone and deliverable tracking

## Summary
The Client Deliverable Manager is an intelligent Uplizd workflow designed to streamline project management by automating the tracking of milestones and client deliverables. By integrating directly with Google Tasks, this solution ensures project hygiene, reduces manual status reporting, and maintains a single source of truth for project timelines, enabling teams to maintain high pipeline velocity and deliver work on schedule.

---

## Demo
![Client Deliverable Manager workflow showing Google Tasks integration and automated status updates](image.png)
**Alt text (SEO-ready):** Client Deliverable Manager Uplizd workflow, automated project milestone tracking, Google Tasks integration, and project management automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/595452b7-0ebf-5a09-80c9-4c55a7546c8f)

---

## Category
**Primary category:** Operations  
**Secondary tags:** project management, google tasks, workflow automation, client deliverables, milestone tracking, task management, productivity, composio  
This solution bridges the gap between client expectations and operational execution by automating task status synchronization.

---

## Who is this for?
This solution is designed for project-driven teams looking to eliminate manual status updates and improve client transparency.

* **Project Managers**
    * Automate the tracking of complex project milestones without manual entry.
* **Account Executives**
    * Provide real-time status updates to clients based on the latest task progress.
* **Operations Leads**
    * Maintain clean project data and ensure no deliverable slips through the cracks.
* **Client Success Managers**
    * Proactively identify stalled deliverables before they impact client satisfaction.

---

## Features
- **Automated Milestone Tracking**
  Automatically syncs project progress against defined milestones within Google Tasks.
- **Real-time Status Updates**
  Triggers immediate status changes in your project dashboard when tasks are marked complete.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely connect and interact with your Google Tasks environment.
- **Proactive Deadline Monitoring**
  Identifies upcoming due dates and alerts the team to potential bottlenecks in the pipeline.
- **Centralized Data Hygiene**
  Ensures all deliverable metadata is standardized, preventing data decay across project boards.

---

## Use Cases
**Project Milestone Management**
* Syncing high-level project phases with granular task lists in Google Tasks.
* Automatically updating project status fields based on the completion of key deliverables.

**Client Communication**
* Generating automated progress reports for stakeholders based on task completion data.
* Alerting account managers when critical client deliverables are nearing their due date.

**Operational Efficiency**
* Reducing manual data entry by mapping project updates directly to task management tools.
* Standardizing the workflow for how deliverables are tracked from initiation to final sign-off.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Client Deliverable Manager template provided via the Run on Uplizd link.
3. Connect your Google account and authorize the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives project update requests or milestone queries from the user.
* **Agent**: Processes natural language instructions to determine which task needs updating or tracking.
* **Composio Toolset**: Executes the specific API calls to read/write data in Google Tasks.
* **Chat Output**: Returns a summary of the action taken or the current status of the requested deliverable.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Check the status of the 'Q3 Website Launch' milestone in Google Tasks.`
* `Mark the 'Final Design Review' deliverable as complete for the Acme Corp project.`
* `List all upcoming deliverables due in the next 48 hours for the marketing team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for all task-related logic.
* Use a model capable of high-precision instruction following.
* Ensure the system prompt emphasizes accurate mapping of natural language to task IDs.
* Configure the agent to prioritize data integrity when updating task statuses.

### 2) Composio Toolset Node
* Provide your valid API key to authenticate the connection.
* Set the scope to allow read/write access to your Google Tasks lists.

### 3) Tool Availability
* **Task Retrieval**: Fetching lists and individual task details.
* **Task Updating**: Modifying completion status, due dates, and task descriptions.
* **Task Creation**: Adding new deliverables to existing project lists.

---

## Related Solutions
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automates the onboarding and setup process for new client accounts.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamlines general business processes and task routing.
* [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) — Tracks the status of maintenance and operational work orders.
