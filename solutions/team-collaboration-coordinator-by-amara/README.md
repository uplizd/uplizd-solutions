# Team Collaboration Coordinator (Uplizd) - Streamline cross-functional workflows and task assignments

## Summary
The Team Collaboration Coordinator is an intelligent Uplizd AI workflow designed to centralize communication, automate task distribution, and synchronize project updates across distributed teams. By leveraging the Composio Toolset to integrate with your existing collaboration platforms, this solution eliminates manual status tracking, reduces meeting overhead, and ensures a single source of truth for project velocity and team accountability.

---

## Demo
![Team Collaboration Coordinator workflow dashboard showing automated task routing and status updates](image.png)
**Alt text (SEO-ready):** Team Collaboration Coordinator Uplizd workflow, automated task assignment, cross-functional team synchronization, and project management integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/33cdf134-ac67-5b86-a26a-d7b5e111db8c)

---

## Category
**Primary category:** Team Operations
**Secondary tags:** collaboration, project management, task automation, team sync, workflow optimization, composio, ai agent, productivity

This solution bridges the gap between fragmented communication channels and project management tools to maintain team alignment.

---

## Who is this for?
This solution is designed for high-velocity teams looking to reduce administrative friction and improve project transparency.

* **Project Managers**
    * Automate the delegation of action items and track completion status in real-time.
* **Operations Leads**
    * Standardize cross-departmental workflows to ensure consistent project handoffs.
* **Team Leads**
    * Gain visibility into team bandwidth and identify bottlenecks before they impact deadlines.
* **Individual Contributors**
    * Receive clear, prioritized task assignments directly within their preferred collaboration tools.

---

## Features
- **Automated Task Routing**
    Automatically parse meeting notes or chat threads to assign tasks to the correct team members.
- **Real-time Sync**
    Maintain bi-directional synchronization between communication platforms and project management software.
- **Intelligent Status Reporting**
    Generate automated progress summaries to keep stakeholders informed without manual status updates.
- **Contextual Context Injection**
    Use the Composio Toolset to fetch relevant project history and documentation for every new task.
- **Bottleneck Detection**
    Identify stalled tasks or overdue items and proactively notify the relevant team leads.

---

## Use Cases
**Project Coordination**
* Automatically convert Slack or Teams discussions into actionable Jira or Asana tickets.
* Sync project milestones across multiple departments to prevent scheduling conflicts.

**Team Accountability**
* Send automated daily reminders for pending action items to ensure deadlines are met.
* Aggregate individual task completion data into weekly team performance reports.

**Meeting Follow-up**
* Extract action items from recorded meeting transcripts and assign them to owners.
* Update project documentation automatically based on decisions made during team syncs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Team Collaboration Coordinator.
2. Click "Import" to load the workflow into your workspace.
3. Connect your required API credentials for your project management and chat tools via the Composio dashboard.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all integration triggers.

### 2) Setup the Nodes
* **Chat Input**: Captures raw team communication or meeting transcripts.
* **Agent**: Processes text to identify tasks, owners, and deadlines.
* **Composio Toolset**: Executes CRUD operations on your project management platforms.
* **Chat Output**: Delivers confirmation messages and task summaries to the team.

### 3) Run the Flow
Use the Playground to test the agent with your team's specific data:
* `Summarize the action items from the last engineering sync and assign them to the respective owners.`
* `Check for any overdue tasks in the marketing project board and notify the team leads.`
* `Create a new project task based on the following discussion: [paste transcript here].`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for parsing intent and managing task lifecycle.
* Use a model capable of high-precision instruction following (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruct the agent to prioritize accuracy in task extraction and entity mapping.
* Configure the agent to maintain a neutral, professional tone when communicating task updates.

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure access to your project management suite.
* Define the connection scope to include only the specific workspaces or boards required for the workflow.

### 3) Tool Availability
* **Task Management**: Create, update, and fetch tasks (Jira, Asana, Trello).
* **Communication**: Post updates and reminders (Slack, Microsoft Teams).
* **Documentation**: Retrieve project context and historical data (Notion, Google Drive).

---

## Related Solutions
* [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Streamline workshop planning and participant engagement.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track team productivity and identify workflow bottlenecks.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on urgency and impact.
