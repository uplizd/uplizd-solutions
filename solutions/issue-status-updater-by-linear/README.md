# Issue Status Updater (Uplizd) - Automated Linear issue synchronization and lifecycle management

## Summary
The Issue Status Updater is an intelligent Uplizd workflow designed to automate the synchronization of Linear issue states with external events and project management triggers. By leveraging the Composio Toolset, this solution eliminates manual status updates, ensuring that your engineering pipeline remains accurate, reducing context switching for developers, and maintaining a single source of truth for project velocity.

---

## Demo
![Linear issue status synchronization workflow showing automated state transitions triggered by external events](image.png)
**Alt text (SEO-ready):** Linear issue status synchronization workflow showing automated state transitions triggered by external events in Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/fae85d19-ad00-5d2a-af62-d16388e86957)

---

## Category
**Primary category:** Operations  
**Secondary tags:** linear, project management, workflow automation, issue tracking, engineering operations, composio, ai workflow, data sync  
This solution streamlines engineering operations by bridging the gap between external triggers and Linear issue lifecycle management.

---

## Who is this for?
This solution is designed for technical teams looking to reduce manual administrative overhead in their development lifecycle.

*   **Engineering Managers**
    *   Ensures real-time visibility into sprint progress without requiring manual status updates from the team.
*   **Product Managers**
    *   Maintains accurate project timelines by automatically reflecting external feedback or deployment status in Linear.
*   **DevOps Engineers**
    *   Automates the transition of issues based on CI/CD pipeline events or infrastructure monitoring alerts.
*   **Technical Leads**
    *   Reduces administrative friction, allowing developers to focus on code rather than updating ticket statuses.

---

## Features
- **Automated Status Transitions**
  Trigger Linear issue updates based on external events, such as pull request merges or deployment completions.
- **Real-time Sync Engine**
  Utilizes the Composio Toolset to ensure that state changes are reflected in Linear with minimal latency.
- **Conditional Logic Routing**
  Apply intelligent filtering to determine which issues require updates based on priority, labels, or assignee.
- **Error Handling & Logging**
  Built-in verification steps to ensure status updates are successfully committed to the Linear API.
- **Customizable Trigger Mapping**
  Easily map diverse external signals—from Slack messages to GitHub webhooks—to specific Linear status workflows.

---

## Use Cases
**Deployment Lifecycle Management**
*   Automatically move Linear issues to "Done" when a corresponding GitHub release is published.
*   Transition tickets to "In QA" once a staging environment deployment is confirmed.

**Cross-Platform Incident Response**
*   Update Linear issue status to "In Progress" when an incident is acknowledged in a tool like Rootly.
*   Close associated tickets automatically when an external monitoring alert is resolved.

**Feedback-Driven Development**
*   Move issues to "Needs Review" when a customer support ticket is linked to a development task.
*   Re-open issues automatically if a regression is detected by automated testing suites.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Issue Status Updater template from the solution library.
3. Connect your Linear workspace via the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual command to initiate the update.
*   **Agent**: Processes the event data and determines the appropriate Linear status transition.
*   **Composio Toolset**: Executes the authenticated API calls to the Linear platform.
*   **Chat Output**: Confirms the successful update or logs any errors encountered during the process.

### 3) Run the Flow
Use the Playground to test your triggers with the following prompts:
* `Update Linear issue ENG-123 to 'In Progress' because the PR has been merged.`
* `Check the status of all high-priority issues and move them to 'Backlog' if they have been stale for 14 days.`
* `Sync the status of issue ENG-456 with the latest deployment update from the production pipeline.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making layer for your issue lifecycle.
*   **Instruction Pattern:**
    *   Identify the unique Linear issue ID from the incoming event payload.
    *   Map the external event status to the corresponding Linear workflow state.
    *   Verify the current state of the issue before attempting a transition to prevent conflicts.

### 2) Composio Toolset Node
*   **API Key:** Ensure your Linear API key is securely stored in the Composio connection settings.
*   **Connection Scope:** Grant the agent permission to read and write issues within your target Linear team.

### 3) Tool Availability
*   **Linear API:** Capability to fetch, update, and comment on issues.
*   **Event Parser:** Capability to normalize incoming JSON payloads from webhooks.
*   **State Validator:** Capability to check current issue metadata to ensure valid transitions.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on urgency.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Manage and archive stale action items across your stack.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the efficiency and status of your team's operational workflows.
