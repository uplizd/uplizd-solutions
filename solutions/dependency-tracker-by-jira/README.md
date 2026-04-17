# Dependency Tracker by Jira (Uplizd) - Automate cross-team dependency management and monitoring

## Summary
The Dependency Tracker by Jira is an intelligent Uplizd workflow that automates the identification, tracking, and resolution of cross-team dependencies. By leveraging the Composio Toolset to interface directly with Jira, this solution provides a single source of truth for project managers and engineering leads, significantly reducing pipeline bottlenecks and improving delivery velocity through real-time synchronization.

---

## Demo
![Dependency Tracker workflow showing Jira issue linking and status updates](image.png)
**Alt text (SEO-ready):** Dependency Tracker workflow by Uplizd, automating Jira cross-team dependency management, issue linking, and project synchronization via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/331a2607-daf0-5f87-941b-4d745a0185e2)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** jira, dependency management, project management, workflow automation, composio, ai agent, task tracking, engineering operations
- This solution streamlines technical operations by connecting disparate project workflows into a unified, AI-driven tracking system.

---

## Who is this for?
This solution is designed for technical teams and project stakeholders who need to maintain visibility across complex, multi-team project environments.

- **Engineering Manager**
    - Gain real-time visibility into cross-team blockers that threaten sprint commitments.
- **Product Manager**
    - Ensure feature delivery timelines remain accurate by tracking external team dependencies.
- **Project Coordinator**
    - Automate the manual effort of cross-referencing Jira tickets across different project boards.
- **DevOps Engineer**
    - Maintain infrastructure project hygiene by automatically flagging stale or unlinked dependencies.

---

## Features
- **Automated Dependency Mapping**
    - Instantly link related Jira tickets across different projects using AI-driven context analysis.
- **Real-time Status Sync**
    - Automatically update parent tickets whenever a dependency status changes in a linked Jira board.
- **Proactive Blocker Alerts**
    - Receive intelligent notifications when a critical dependency is delayed or flagged as "at risk."
- **Composio-Powered Integration**
    - Securely connect to Jira via the Composio Toolset to perform authenticated read/write operations.
- **Customizable Workflow Logic**
    - Tailor the agent's decision-making process to match your team's specific Jira workflow and board structure.

---

## Use Cases
**Sprint Planning & Execution**
- Automatically identify missing dependencies during the sprint planning phase.
- Sync status updates between front-end and back-end team Jira boards to ensure alignment.

**Cross-Team Project Management**
- Track high-level initiatives that span multiple departments by aggregating sub-tasks into a master tracker.
- Flag stalled dependencies that have remained in a "blocked" state for more than 48 hours.

**Release Readiness**
- Generate a comprehensive report of all open dependencies before a scheduled production release.
- Automate the transition of parent tasks once all linked sub-dependencies are marked as "Done."

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import" option.
2. Upload the `dependency-tracker-by-jira` workflow file.
3. Configure your Jira credentials within the Composio connection settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives project context or specific Jira ticket IDs.
- **Agent**: Processes dependency logic and determines necessary Jira actions.
- **Composio Toolset**: Executes authenticated API calls to fetch, link, or update Jira issues.
- **Chat Output**: Returns a summary of dependency status or confirmation of updates.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Check for any blocked dependencies in the Q3 Launch project.`
- `Link Jira ticket ENG-102 as a blocker for MKT-550.`
- `Provide a status report on all dependencies currently assigned to the Platform team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a project coordinator, interpreting natural language requests and translating them into Jira actions.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a Jira expert. Always verify ticket IDs before attempting to link them."
- Instruction: "Prioritize identifying blockers that have been stagnant for more than 3 days."

### 2) Composio Toolset Node
- Provide a valid Jira API key and ensure the connection scope includes `jira:write` and `jira:read` permissions.

### 3) Tool Availability
- `jira_search_issues`: Locate tickets by summary or status.
- `jira_link_issues`: Create dependency relationships between tickets.
- `jira_get_issue_details`: Retrieve current status and assignee information.
- `jira_update_issue`: Modify ticket status or comments based on dependency changes.

---

## Related Solutions
- [Action Item Prioritizer by Rootly](../action-item-prioritizer-by-rootly/README.md) — Manage and rank incoming action items across your stack.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex business processes through automated task management.
- [Account Relationship Builder by Dynamics365](../account-relationship-builder-by-dynamics365/README.md) — Map and visualize complex stakeholder relationships in your CRM.
