# Meeting Recording Manager (Uplizd) - Automate meeting organization and insight distribution

## Summary
The Meeting Recording Manager by Uplizd streamlines post-meeting workflows by automatically processing Zoom recordings, extracting key action items, and distributing summaries to relevant stakeholders. This solution eliminates manual documentation overhead, ensuring that meeting intelligence is captured, organized, and actionable within your existing productivity stack.

---

## Demo
![Meeting Recording Manager workflow showing Zoom integration, AI summarization, and automated distribution to team channels](image.png)

**Alt text (SEO-ready):** Meeting Recording Manager by Uplizd workflow for automated Zoom recording summarization, AI-driven action item extraction, and team communication integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a948d417-6ace-5417-864b-5934baa211ca)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** zoom, meeting management, ai workflow, productivity, automation, action items, composio, team collaboration.
- This solution bridges the gap between raw video conferencing data and structured team output, serving as a central hub for meeting intelligence.

---

## Who is this for?
This solution is designed for teams looking to reclaim time spent on manual meeting administration and ensure consistent follow-through on commitments.

- **Project Managers**
    - Automatically track project milestones and blockers discussed during syncs without manual note-taking.
- **Sales Representatives**
    - Instantly log client feedback and follow-up requirements into the CRM immediately after a Zoom call.
- **Operations Leads**
    - Maintain a searchable, organized repository of meeting outcomes to improve cross-departmental transparency.
- **Executive Assistants**
    - Ensure that leadership meeting decisions are captured accurately and delegated to the correct team members.

---

## Features
- **Automated Transcription Processing**
    - Leverages advanced AI to convert Zoom audio into accurate, structured text logs for analysis.
- **Intelligent Action Item Extraction**
    - Automatically identifies tasks, owners, and deadlines from meeting dialogue using the Composio Toolset.
- **Cross-Platform Sync**
    - Seamlessly pushes meeting summaries and tasks to project management tools and team communication channels.
- **Real-Time Notification Alerts**
    - Triggers immediate updates to stakeholders as soon as a meeting recording is processed and summarized.
- **Customizable Summary Templates**
    - Configures output formats to match company standards, ensuring consistent reporting across all departments.

---

## Use Cases
**Meeting Documentation**
- Automatically generate professional meeting minutes from Zoom recordings.
- Archive searchable transcripts in your internal knowledge base for future reference.

**Task Management**
- Convert verbal commitments made during calls into actionable tickets in project management software.
- Assign action items to team members based on the context of the meeting discussion.

**Sales & Client Success**
- Capture key client pain points and feature requests directly from discovery calls.
- Sync meeting outcomes to CRM profiles to maintain a comprehensive history of client interactions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Recording Manager template from the solution library.
3. Connect your Zoom and project management accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the Zoom recording link or metadata trigger.
- **Agent**: Processes the transcript and extracts key insights using predefined instructions.
- **Composio Toolset**: Executes API calls to update your project management or CRM platforms.
- **Chat Output**: Confirms the successful distribution of the summary to your team channels.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Process the latest Zoom recording from today and summarize the action items for the marketing team.`
- `Extract all technical requirements mentioned in the meeting with the engineering lead and create Jira tickets.`
- `Summarize the client discovery call and update the account notes in Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your meeting data.
- **Role:** Act as a professional meeting secretary and project coordinator.
- **Instruction Pattern:**
    - Identify all speakers and distinguish between general discussion and actionable commitments.
    - Format output into clear sections: Summary, Action Items, and Key Decisions.
    - Maintain a neutral, professional tone suitable for corporate documentation.

### 2) Composio Toolset Node
- **API Key:** Provide your unique Composio API key to enable secure integration with Zoom and your productivity tools.
- **Connection Scope:** Ensure the toolset has read access to Zoom recordings and write access to your target project management or CRM platform.

### 3) Tool Availability
- **Zoom API:** For fetching recording transcripts and metadata.
- **Project Management Tools:** For creating and updating tasks (e.g., Jira, Asana, Trello).
- **CRM Connectors:** For logging meeting summaries against specific account records.
- **Communication APIs:** For sending automated summaries to Slack or Microsoft Teams.

---

## Related Solutions
- [Zoom Usage Intelligence Agent](../zoom-usage-intelligence-agent/README.md) — Analyze meeting frequency and platform engagement metrics.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Organize and rank tasks extracted from various project workflows.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Connect disparate business processes into a unified automation pipeline.
