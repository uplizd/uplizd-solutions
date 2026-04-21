# Stakeholder Communication Hub (Uplizd) - Automated project status and stakeholder updates

## Summary
The Stakeholder Communication Hub is an intelligent Uplizd workflow designed to streamline project transparency by automatically syncing epic and story updates from Shortcut to your key stakeholders. By leveraging the Composio Toolset, this solution eliminates manual reporting overhead, ensuring that project progress, blockers, and milestone completions are communicated in real-time, maintaining a single source of truth for cross-functional teams.

---

## Demo
![Stakeholder Communication Hub workflow showing Shortcut epic updates being processed by an AI agent and delivered to stakeholders](image.png)
**Alt text (SEO-ready):** Uplizd Stakeholder Communication Hub workflow, Shortcut project management automation, AI-driven stakeholder reporting, and automated epic status updates.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6aa46022-45b0-5410-8858-79a556ef5fef)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** shortcut, project management, stakeholder communication, automation, reporting, ai workflow, composio, team alignment.
This solution bridges the gap between technical project tracking and executive visibility through automated, context-aware status reporting.

---

## Who is this for?
This solution is designed for teams that need to maintain high-velocity project updates without manual documentation.

- **Product Managers**
    - Automate the generation of weekly status reports for stakeholders based on real-time epic progress.
- **Engineering Leads**
    - Reduce time spent on status updates by letting the AI summarize completed stories and current blockers.
- **Operations Managers**
    - Ensure consistent communication across departments by standardizing how project health is reported.
- **Customer Success Managers**
    - Proactively inform clients about feature release timelines and project milestones directly from engineering data.

---

## Features
- **Automated Epic Summarization**
    - Automatically parses Shortcut epic data to generate concise, human-readable status summaries.
- **Real-time Progress Tracking**
    - Monitors story state changes to trigger updates the moment a milestone is reached.
- **Stakeholder-Ready Formatting**
    - Translates technical ticket jargon into business-friendly language for non-technical stakeholders.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely query and interact with your Shortcut workspace.
- **Customizable Notification Triggers**
    - Configure the agent to report on specific labels, priority levels, or completion percentages.

---

## Use Cases
**Project Status Reporting**
- Generate weekly "State of the Union" reports for leadership teams based on active epic progress.
- Automatically notify stakeholders when high-priority epics move from "In Progress" to "Ready for Review."

**Blocker & Risk Management**
- Identify and escalate stalled stories or epics that have been blocked for more than 48 hours.
- Provide immediate visibility into resource constraints by summarizing comments on blocked tickets.

**Milestone & Release Communication**
- Send automated release notes to internal teams once a collection of stories is marked as "Done."
- Keep cross-functional partners updated on shifting timelines when epic due dates are adjusted in Shortcut.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the template in your workspace.
2. Connect your Shortcut account via the Composio integration settings.
3. Configure your notification channels (e.g., Slack or Email) in the Output node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Triggers the workflow based on a schedule or manual request.
- **Agent**: Processes project data and synthesizes status updates.
- **Composio Toolset**: Executes API calls to fetch epics, stories, and comments from Shortcut.
- **Chat Output**: Delivers the final summary to your designated communication channel.

### 3) Run the Flow
Use the Playground to test your communication triggers:
- `Summarize the progress of the Q3 Mobile App Epic.`
- `List all blockers currently affecting the Web Dashboard project.`
- `Draft a status update for stakeholders regarding the upcoming API migration.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a project communications assistant.
- Use a model with strong summarization capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a project reporting assistant. Focus on progress, blockers, and upcoming milestones."
- Instruction: "Maintain a professional, concise tone suitable for executive stakeholders."

### 2) Composio Toolset Node
- Provide your Shortcut API key within the Composio dashboard.
- Ensure the connection scope includes read access to your workspace's epics, stories, and comments.

### 3) Tool Availability
- `shortcut_list_epics`: Fetch active epics and their current status.
- `shortcut_get_story_details`: Retrieve specific progress data for individual tasks.
- `shortcut_list_comments`: Extract context from team discussions to identify blockers.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign project action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track team velocity and overall project health metrics.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage stakeholder engagement and CRM-based project tracking.
