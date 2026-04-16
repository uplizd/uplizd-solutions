# Change Request Auto-Processor (Uplizd) - Intelligent ServiceNow change management automation

## Summary
The Change Request Auto-Processor is an intelligent Uplizd workflow designed to streamline IT service management by automating the validation, routing, and approval lifecycle of change requests. By leveraging the Composio Toolset to interface directly with ServiceNow, this solution eliminates manual bottlenecks, ensures compliance with standardized change protocols, and accelerates pipeline velocity for DevOps and IT operations teams.

---

## Demo
![Change Request Auto-Processor workflow interface showing ServiceNow integration nodes](image.png)
**Alt text (SEO-ready):** Change Request Auto-Processor workflow in Uplizd, automating ServiceNow change management, IT service request routing, and approval workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e8c6544f-766f-535e-a1b2-a568c066b580)

---

## Category
- **Primary category:** IT Operations
- **Secondary tags:** servicenow, change management, itsm, automation, devops, workflow orchestration, composio, incident response
- This solution bridges the gap between incoming change requests and automated system execution, ensuring consistent IT governance.

---

## Who is this for?
This workflow is designed for IT and DevOps professionals who need to maintain system stability while increasing deployment frequency.

- **IT Operations Manager**
    - Ensures all change requests meet compliance standards before reaching the approval stage.
- **DevOps Engineer**
    - Reduces manual overhead by automating the transition of change requests through pipeline stages.
- **Service Desk Lead**
    - Accelerates ticket resolution times by providing real-time status updates and automated routing.
- **Compliance Officer**
    - Maintains a clear audit trail of all change request validations and automated approval actions.

---

## Features
- **Automated Request Validation**
    - Automatically checks incoming change requests against predefined criteria to ensure all required fields and documentation are present.
- **Intelligent Routing**
    - Dynamically assigns change requests to the appropriate technical teams based on the service category and risk level.
- **ServiceNow Integration**
    - Utilizes the Composio Toolset to perform real-time read/write operations directly within your ServiceNow environment.
- **Standardized Approval Workflows**
    - Triggers automated approval requests for low-risk changes, significantly reducing the time spent in manual review cycles.
- **Real-time Status Sync**
    - Keeps stakeholders informed by pushing status updates back to the source platform as the change request progresses.

---

## Use Cases
**Change Management Lifecycle**
- Automatically validating change request urgency and impact scores upon submission.
- Routing high-risk changes to senior engineering leads for manual review while auto-approving standard changes.

**Compliance & Governance**
- Ensuring every change request is linked to a valid incident or problem ticket before processing.
- Generating automated audit logs for every state transition within the ServiceNow environment.

**Operational Efficiency**
- Reducing the time-to-implementation for routine infrastructure updates by eliminating manual data entry.
- Syncing change request status updates across internal communication channels to maintain team alignment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to load the workflow template into your Uplizd workspace.
3. Connect your ServiceNow credentials via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw change request details or trigger event.
- **Agent**: Processes the request, validates data, and determines the appropriate action.
- **Composio Toolset**: Executes the specific ServiceNow API calls to update records.
- **Chat Output**: Returns the confirmation or status report to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Validate the latest change request in ServiceNow and check if it meets the standard risk criteria.`
- `Route the pending change request CR-1024 to the Cloud Infrastructure team for review.`
- `Update the status of all approved change requests to 'Scheduled' for the upcoming maintenance window.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central decision-maker for request validation and routing.
- Instruction: "You are an IT operations assistant. Analyze incoming change requests for completeness and risk."
- Instruction: "Use the ServiceNow toolset to retrieve, validate, and update change request records."
- Instruction: "Maintain a professional tone and provide clear summaries of actions taken."

### 2) Composio Toolset Node
- Requires a valid ServiceNow API key and appropriate read/write permissions.
- Ensure the connection scope includes `change_request` and `incident` tables.

### 3) Tool Availability
- `servicenow_get_change_request`: Retrieve details for specific CR IDs.
- `servicenow_update_change_request`: Modify fields such as state, priority, or assignment group.
- `servicenow_list_requests`: Query for pending or high-priority change requests.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automates the resolution and cleanup of post-incident action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Intelligent prioritization of technical action items and tasks.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational health and efficiency of automated workflows.
