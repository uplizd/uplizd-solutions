# Daily Standup Coordinator (Uplizd) - Automated team status collection and meeting synchronization

## Summary
The Daily Standup Coordinator is an intelligent Uplizd workflow designed to automate the collection of team status updates and action items via Slack. By centralizing daily progress reports and flagging blockers in real-time, this solution eliminates manual follow-ups, ensures team alignment, and significantly improves pipeline velocity for distributed engineering and product teams.

---

## Demo
![Daily Standup Coordinator workflow showing Slack integration for automated status collection](image.png)
**Alt text (SEO-ready):** Daily Standup Coordinator Uplizd workflow showing automated Slack status collection, team progress tracking, and blocker identification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/64fc1b44-7394-548b-aae4-e8f7fc9f9c27)

---

## Category
- **Primary category:** Team Operations
- **Secondary tags:** slack, standup, team sync, automation, productivity, project management, composio, ai workflow
- This solution streamlines daily communication loops by integrating AI-driven status collection directly into your existing Slack workspace.

---

## Who is this for?
This solution is designed for high-velocity teams looking to reduce meeting overhead and improve data hygiene.

- **Engineering Managers**
    - Automate the aggregation of daily status updates to identify blockers before they impact sprint velocity.
- **Product Managers**
    - Maintain a single source of truth for feature progress without needing to manually ping individual contributors.
- **Team Leads**
    - Ensure consistent reporting across distributed time zones by standardizing the daily check-in process.
- **Operations Specialists**
    - Improve team hygiene by tracking action items and follow-ups directly from Slack threads into project management tools.

---

## Features
- **Automated Slack Reminders**
    - Trigger scheduled prompts in specific Slack channels to ensure team members submit updates on time.
- **Intelligent Status Summarization**
    - Use AI to parse unstructured status updates into concise, actionable summaries for leadership review.
- **Blocker Detection**
    - Automatically flag keywords related to delays or technical hurdles, notifying the appropriate stakeholders immediately.
- **Composio Toolset Integration**
    - Seamlessly sync collected status data with external tools like Jira, Linear, or Trello using the Composio Toolset.
- **Real-time Reporting**
    - Generate daily progress snapshots that provide visibility into team capacity and project health.

---

## Use Cases
**Meeting Efficiency**
- Automate the "what I did yesterday, what I'm doing today" loop to shorten live standup meetings.
- Collect status updates asynchronously for teams working across different global time zones.

**Blocker Management**
- Automatically create tickets in project management software when a team member reports a critical blocker.
- Escalate high-priority issues to the engineering manager's dashboard based on sentiment analysis of status updates.

**Data Hygiene & Tracking**
- Sync daily progress notes to a centralized database or document for historical performance tracking.
- Audit team activity logs to ensure alignment with current sprint goals and project milestones.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Configure your Slack API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your Slack channels and target project management tools.

### 2) Setup the Nodes
- **Chat Input**: Receives the scheduled trigger or manual status submission from Slack.
- **Agent**: Processes the natural language input, extracts key tasks, and identifies blockers.
- **Composio Toolset**: Executes the connection to your project management tools to log updates or create tickets.
- **Chat Output**: Posts a confirmation message back to the user or a summary to the team channel.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the status updates from the engineering channel for today.`
- `Identify any blockers mentioned in the team's morning standup and create a Jira ticket for each.`
- `Post a reminder to the #dev-team channel asking for status updates.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for parsing and routing status data.
- Use a model capable of high-precision instruction following (e.g., GPT-4o).
- **Recommended instruction pattern:**
    - "Extract tasks, blockers, and sentiment from the provided Slack message."
    - "If a blocker is identified, format the output for the project management tool API."
    - "Maintain a professional and encouraging tone in all automated responses."

### 2) Composio Toolset Node
- Provide your workspace API key to authorize the agent to interact with Slack and your project management suite.
- Ensure the connection scope includes `channels:history`, `chat:write`, and relevant project management write permissions.

### 3) Tool Availability
- **Slack API**: For sending reminders and reading status updates.
- **Project Management APIs (Jira/Linear/Trello)**: For logging tasks and creating blocker tickets.
- **Data Transformation Utilities**: For formatting status summaries into structured reports.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational efficiency of your automated team workflows.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks extracted from team communications.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Maintain hygiene by archiving or resolving stale action items from your project boards.
