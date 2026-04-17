# Daily Standup Bot (Uplizd) - Automate team check-ins and meeting summaries

## Summary
The Daily Standup Bot by Chatwork streamlines team communication by automating the collection of daily progress updates, blockers, and goals. By integrating directly with your team's chat environment, this Uplizd workflow ensures consistent reporting, reduces manual follow-up time, and provides leadership with a consolidated view of team velocity and project health.

---

## Demo
![Daily Standup Bot workflow interface showing automated collection of team status updates and summary generation](image.png)
**Alt text (SEO-ready):** Daily Standup Bot Uplizd workflow for automated team status collection, progress tracking, and Chatwork integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/18a29d99-f521-5a8d-acf2-0abfe5b02b21)

---

## Category
- **Primary category:** Team Collaboration
- **Secondary tags:** chatbot, chatwork, daily standup, project management, team sync, automated reporting, workflow automation, internal communications
- This solution bridges the gap between fragmented team updates and actionable project insights through intelligent automated aggregation.

---

## Who is this for?
This solution is designed for distributed teams and managers looking to eliminate meeting fatigue and improve reporting hygiene.

- **Engineering Managers**
    - Automate the collection of daily blockers to proactively resolve technical bottlenecks.
- **Project Leads**
    - Maintain a consistent pulse on project velocity without manual status chasing.
- **Remote Team Members**
    - Provide quick, asynchronous updates that keep the team aligned across time zones.
- **Operations Specialists**
    - Centralize team activity data to improve resource allocation and project forecasting.

---

## Features
- **Automated Update Collection**
    - Triggers scheduled prompts to team members to submit their daily progress, preventing missed reports.
- **Intelligent Summarization**
    - Uses AI to synthesize individual updates into a concise team-wide summary for management review.
- **Blocker Identification**
    - Automatically flags critical blockers or delays in the daily feed for immediate attention by team leads.
- **Chatwork Integration**
    - Leverages the Composio Toolset to post and retrieve messages directly within your existing Chatwork workspace.
- **Historical Reporting**
    - Archives daily updates to create a searchable history of team progress and project evolution over time.

---

## Use Cases
**Team Alignment & Sync**
- Collect daily "What I did," "What I'm doing," and "Blockers" from all team members automatically.
- Generate a morning summary report that highlights team goals for the day ahead.

**Project Health Monitoring**
- Track the resolution time of blockers reported by team members to identify process inefficiencies.
- Aggregate status updates to provide stakeholders with high-level project progress reports without manual data entry.

**Operational Efficiency**
- Reduce the time spent in live standup meetings by handling routine status updates asynchronously.
- Ensure all team members are aligned on priorities by broadcasting the aggregated summary to the team channel.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project folder to import the workflow.
3. Authenticate your Chatwork account within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the daily status update text from team members.
- **Agent**: Processes the input, extracts key progress metrics, and identifies blockers.
- **Composio Toolset**: Executes the API calls to post summaries and retrieve team messages in Chatwork.
- **Chat Output**: Delivers the formatted summary or confirmation message back to the team channel.

### 3) Run the Flow
Use the Playground to test the bot's response to various inputs:
- `Summarize the team updates from today and highlight any blockers.`
- `Post a reminder to the team channel to submit their daily standup updates.`
- `Extract the progress made on the 'Q3 Launch' project from the latest chat history.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your team updates.
- **Role:** Act as a professional project assistant that synthesizes team communications.
- **Instruction Pattern:**
    - Focus on extracting actionable items and blockers from unstructured text.
    - Maintain a professional, encouraging tone in all team-facing communications.
    - Prioritize clarity and brevity when generating the daily summary report.

### 2) Composio Toolset Node
- **API Key:** Ensure your Chatwork API key is active and has permissions to read/write to the relevant team channels.
- **Connection Scope:** Limit the toolset scope to the specific channels used for daily standup reporting.

### 3) Tool Availability
- **Message Retrieval:** Ability to pull recent messages from specific Chatwork threads.
- **Message Posting:** Ability to send formatted summaries and reminders to team channels.
- **User Identification:** Ability to map updates to specific team members for accurate reporting.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the efficiency and status of your automated workflows.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage and nurture professional connections within your CRM.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks based on urgency and impact.
