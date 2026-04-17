# Sprint Planner (Uplizd) - Intelligent issue distribution and cycle capacity management

## Summary
The Sprint Planner (Uplizd) is an AI-driven workflow that automates the distribution of engineering issues across team cycles by analyzing real-time capacity and task complexity. By integrating directly with Linear, this solution eliminates manual planning overhead, ensures balanced workloads, and maintains sprint velocity, providing engineering managers with a single source of truth for team bandwidth and project timelines.

---

## Demo
![Sprint Planner workflow interface showing issue distribution across Linear cycles](image.png)
**Alt text (SEO-ready):** Uplizd Sprint Planner workflow interface showing automated issue distribution and capacity management using Linear and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/71bcc788-f982-5aee-9840-649a9590304d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** linear, sprint planning, capacity management, engineering productivity, workflow automation, composio, ai agent, project management.
This solution streamlines sprint operations by syncing task allocation with team availability, ensuring data-driven planning cycles.

---

## Who is this for?
This solution is designed for technical teams looking to optimize their development cycles and reduce planning friction.

- **Engineering Manager**
  - Automates the assignment of tickets based on developer bandwidth and historical velocity.
- **Product Manager**
  - Ensures sprint goals align with realistic team capacity and current project backlogs.
- **DevOps Lead**
  - Maintains visibility into sprint health and identifies potential bottlenecks before they impact delivery.
- **Scrum Master**
  - Facilitates faster sprint planning sessions by providing AI-generated distribution recommendations.

---

## Features
- **Intelligent Capacity Analysis**
  - Automatically calculates team bandwidth by pulling real-time data from Linear to prevent over-allocation.
- **Automated Issue Distribution**
  - Uses AI to map incoming issues to the most appropriate team members based on skill sets and current load.
- **Linear Integration**
  - Leverages the Composio Toolset to read and write directly to Linear, ensuring all sprint updates are reflected in real-time.
- **Dynamic Cycle Balancing**
  - Adjusts task distribution dynamically as sprint priorities shift or team members become available.
- **Velocity-Driven Planning**
  - Incorporates historical performance metrics to predict realistic completion dates for sprint cycles.

---

## Use Cases
**Sprint Cycle Optimization**
- Automatically populating a new sprint cycle with prioritized issues from the backlog.
- Rebalancing tasks mid-sprint when a team member's availability changes unexpectedly.

**Backlog Hygiene**
- Identifying stalled or unassigned issues that require immediate attention before a sprint begins.
- Tagging and categorizing issues based on complexity to ensure balanced distribution.

**Team Performance Tracking**
- Generating reports on sprint completion rates compared to initial capacity estimates.
- Monitoring individual developer load to prevent burnout and maintain consistent output.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in the Uplizd builder.
2. Connect your Linear account via the Composio Toolset configuration node.
3. Configure your target team and cycle settings in the Agent node instructions.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the sprint planning request or trigger signal.
- **Agent**: Processes the request, analyzes capacity, and determines task distribution.
- **Composio Toolset**: Executes API calls to Linear to fetch issues and update assignments.
- **Chat Output**: Returns the finalized sprint plan and distribution summary to the user.

### 3) Run the Flow
Use the Playground to test your planning logic with these prompts:
- `Plan the next sprint using all unassigned high-priority issues in the 'Web' project.`
- `Review current team capacity and rebalance the 'Mobile' sprint if anyone is over-allocated.`
- `Generate a summary of the current sprint load and identify any bottlenecks in the workflow.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical project manager.
- Focus on balancing tasks based on team member capacity.
- Prioritize issues labeled as 'Critical' or 'High' during the distribution phase.
- Maintain a neutral, data-driven tone when reporting on sprint health.

### 2) Composio Toolset Node
- **API Key**: Ensure your Linear API key is active within the Composio dashboard.
- **Connection Scope**: Grant read/write access to your Linear workspace to allow the agent to modify issue assignments and cycle states.

### 3) Tool Availability
- **Linear Issue Fetcher**: Retrieves backlog items and project metadata.
- **Linear Assignment Manager**: Updates issue assignees and cycle associations.
- **Capacity Calculator**: Analyzes team member workloads and historical velocity.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamlines cross-platform task automation and business processes.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automates CRM account provisioning and data entry workflows.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Intelligent sorting and management of incident-related action items.
