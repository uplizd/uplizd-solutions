# Incident Action Item Tracker (Uplizd) - Automate post-incident remediation and task tracking

## Summary
The Incident Action Item Tracker is an intelligent Uplizd workflow designed to streamline the post-incident lifecycle by automatically capturing, categorizing, and assigning action items from Rootly incident reports. By bridging the gap between incident response and task management, this solution ensures that critical remediation steps are never missed, reducing MTTR (Mean Time To Resolution) and improving overall operational reliability.

---

## Demo
![Incident Action Item Tracker workflow dashboard showing Rootly integration and automated task assignment](image.png)
**Alt text (SEO-ready):** Uplizd Incident Action Item Tracker workflow for Rootly, automating post-incident task management, remediation tracking, and team assignment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1c71114c-659c-5d72-8c0d-3b9f774560ce)

---

## Category
**Primary category:** Operations
**Secondary tags:** incident management, rootly, task tracking, automation, devops, remediation, workflow, composio

This solution optimizes incident response by automating the transition from post-mortem analysis to actionable engineering tasks.

---

## Who is this for?
This workflow is designed for technical teams looking to standardize their incident remediation process.

- **Incident Commander**
    - Ensures all post-incident action items are captured and tracked in a centralized system immediately following an incident.
- **Site Reliability Engineer (SRE)**
    - Reduces manual overhead by automating the creation of Jira or GitHub issues directly from Rootly incident summaries.
- **Engineering Manager**
    - Gains visibility into team workload and remediation progress through automated status updates and task prioritization.
- **DevOps Lead**
    - Maintains high system availability by ensuring that root cause analysis findings are converted into actionable development tickets.

---

## Features
- **Automated Extraction**
    - Uses AI to parse Rootly incident logs and identify specific action items, owners, and deadlines.
- **Cross-Platform Sync**
    - Seamlessly pushes identified action items to project management tools like Jira, Linear, or GitHub Issues via the Composio Toolset.
- **Priority Scoring**
    - Automatically assigns severity levels to action items based on the incident impact analysis.
- **Real-time Notifications**
    - Triggers alerts to relevant team members in Slack or Microsoft Teams once an action item is assigned.
- **Audit Trail Generation**
    - Maintains a comprehensive log of all remediation tasks linked back to the original incident for compliance and reporting.

---

## Use Cases
**Post-Incident Remediation**
- Automatically generate Jira tickets from Rootly post-mortem summaries to ensure no follow-up task is dropped.
- Assign remediation tasks to the correct on-call engineer based on the service ownership metadata.

**Operational Hygiene**
- Track the aging of incident action items and send reminders to owners for overdue tasks.
- Aggregate incident data to identify recurring issues that require structural engineering changes.

**Compliance & Reporting**
- Generate weekly reports of completed vs. pending action items for leadership reviews.
- Ensure all high-severity incidents have documented follow-up tasks to satisfy audit requirements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import Workflow" to add the Incident Action Item Tracker to your workspace.
3. Connect your Rootly and Project Management (e.g., Jira/GitHub) accounts via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the incident ID or summary text from the user.
- **Agent**: Processes the incident data to extract actionable items and determine priority.
- **Composio Toolset**: Executes API calls to create tasks in your connected project management system.
- **Chat Output**: Confirms the successful creation of tasks and provides a summary of assigned items.

### 3) Run the Flow
Use the Playground to test your setup with these prompts:
- `Extract action items from Rootly incident INC-402 and create Jira tickets.`
- `List all pending remediation tasks for the last incident involving the payment gateway.`
- `Assign all high-priority action items from the recent database outage to the SRE team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires clear instructions to maintain consistency in task creation.
- Focus on extracting clear, actionable titles and descriptions from raw incident logs.
- Map incident severity levels to your internal project management priority fields.
- Ensure the agent requests clarification if an assigned owner cannot be identified.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure authentication with your incident and task management platforms.
- Set the connection scope to include read access for Rootly and write access for your project management tool.

### 3) Tool Availability
- **Rootly API**: For fetching incident details and post-mortem logs.
- **Jira/Linear/GitHub API**: For creating, updating, and assigning remediation tasks.
- **Slack/Teams API**: For sending automated task assignment notifications.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automate the archival and cleanup of stale incident tasks.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Intelligent scoring and ranking of incident remediation tasks.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Manage customer-facing support tickets alongside internal incident tasks.
