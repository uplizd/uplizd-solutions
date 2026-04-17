# Smart Standup Coordinator (Uplizd) - Automated daily standup facilitation and progress tracking

## Summary
The Smart Standup Coordinator (Uplizd) automates daily team synchronization by intelligently collecting status updates, identifying blockers, and summarizing progress for stakeholders. This workflow eliminates manual follow-ups, ensures team alignment, and provides a single source of truth for project velocity, benefiting team leads and project managers who require real-time visibility into daily operations.

---

## Demo
![Smart Standup Coordinator workflow showing automated chat input, agent processing, and DailyBot integration](image.png)
**Alt text (SEO-ready):** Smart Standup Coordinator Uplizd workflow for automated daily standup collection, progress tracking, and team status reporting using DailyBot integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e79d86e4-e32f-5fe3-b2db-c09222af0cf6)

---

## Category
**Primary category:** Operations
**Secondary tags:** dailybot, standup, team sync, project management, workflow automation, productivity, ai assistant, team communication.
This solution streamlines team communication by bridging the gap between daily status updates and centralized project tracking.

---

## Who is this for?
This solution is designed for high-performing teams looking to optimize their daily rituals and reduce administrative overhead.

* **Engineering Manager**
    * Automates the collection of daily blockers to proactively resolve technical bottlenecks.
* **Project Manager**
    * Maintains a real-time pulse on project velocity without manual status chasing.
* **Team Lead**
    * Facilitates consistent team alignment and ensures everyone is focused on high-priority tasks.
* **Operations Coordinator**
    * Standardizes reporting formats across multiple squads for better cross-departmental visibility.

---

## Features
- **Automated Status Collection**
  Triggers daily prompts to team members via DailyBot to gather updates without manual intervention.
- **Blocker Identification**
  Uses AI to scan incoming updates for keywords related to delays, dependencies, or technical hurdles.
- **Contextual Summarization**
  Aggregates individual responses into a concise, readable summary for leadership review.
- **Composio Toolset Integration**
  Connects directly with DailyBot and project management platforms to sync status data in real-time.
- **Actionable Insights**
  Provides clear visibility into team progress and highlights critical items requiring immediate attention.

---

## Use Cases
**Daily Team Synchronization**
* Automating the collection of "what was done" and "what is planned" from distributed team members.
* Sending a consolidated daily digest to Slack or Microsoft Teams for immediate team awareness.

**Blocker Management**
* Flagging high-priority blockers to the relevant manager as soon as they are reported in a standup.
* Tracking the resolution status of reported blockers across multiple consecutive daily standups.

**Project Velocity Tracking**
* Linking daily progress updates to specific project milestones within your management tool.
* Generating end-of-week performance reports based on the daily data collected throughout the sprint.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your DailyBot and communication platform credentials.
4. Ensure nodes are correctly mapped to your specific team channels and project boards.

### 2) Setup the Nodes
* **Chat Input**: Receives raw status updates from team members.
* **Agent**: Analyzes the input for progress metrics and blocker keywords.
* **Composio Toolset**: Connects to DailyBot to fetch updates and push summaries.
* **Chat Output**: Delivers the synthesized report to the designated team channel.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Summarize the team's progress for today and highlight any critical blockers.`
* `Fetch the latest standup updates from the engineering squad and format them for the project lead.`
* `Identify which team members have not submitted their status update for today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your standup data.
* Focus on extracting "Blockers" vs "Completed Tasks."
* Maintain a professional, concise tone for all generated summaries.
* Prioritize urgency when identifying project risks or technical impediments.

### 2) Composio Toolset Node
Requires a valid DailyBot API key and appropriate read/write permissions for your team's communication channels. Ensure the connection scope includes access to historical standup logs.

### 3) Tool Availability
* **DailyBot API**: For fetching and posting standup data.
* **Project Management Connectors**: For syncing updates to your task tracking system.
* **Notification Services**: For alerting managers of critical blockers.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the efficiency and performance of your automated team workflows.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on urgency and impact.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Maintain hygiene in your task lists by identifying and closing stale items.
