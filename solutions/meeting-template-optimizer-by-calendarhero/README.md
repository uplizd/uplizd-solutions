# Meeting Template Optimizer (Uplizd) - Automate agenda creation and meeting structure

## Summary
The Meeting Template Optimizer is an intelligent Uplizd AI workflow designed to streamline meeting preparation by automatically selecting and applying the most effective agenda templates based on meeting context. By leveraging the Composio Toolset to interface with calendar and documentation platforms, this solution ensures consistent meeting hygiene, reduces administrative overhead for organizers, and improves overall meeting productivity.

---

## Demo
![Meeting Template Optimizer workflow interface showing automated agenda selection and calendar integration](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Template Optimizer workflow, automated agenda generation, Composio calendar integration, and meeting productivity tool.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/29902c2f-e61f-552e-bd00-479d526d8af7)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meeting management, agenda automation, productivity, calendar sync, workflow automation, composio, ai assistant
- This solution optimizes internal and external meeting workflows by standardizing documentation and preparation processes.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting schedules and require consistent, high-quality meeting outcomes.

- **Operations Managers**
    - Standardize meeting structures across teams to ensure consistent data capture and follow-up.
- **Executive Assistants**
    - Automate the preparation of agendas and pre-read materials, saving hours of manual coordination.
- **Project Managers**
    - Ensure that recurring syncs and status updates follow a repeatable, outcome-oriented format.
- **Sales Leads**
    - Align discovery and demo calls with proven templates to increase conversion and pipeline velocity.

---

## Features
- **Context-Aware Selection**
    - Automatically identifies the meeting type (e.g., 1:1, All-Hands, Discovery) and selects the corresponding template.
- **Dynamic Agenda Generation**
    - Populates meeting documents with relevant talking points, action items, and attendee-specific data.
- **Calendar Integration**
    - Uses the Composio Toolset to read calendar events and push agenda links directly into meeting invites.
- **Real-time Formatting**
    - Ensures all generated agendas adhere to company branding and documentation standards.
- **Feedback Loop**
    - Learns from meeting outcomes to suggest template improvements based on historical performance.

---

## Use Cases
**Meeting Preparation**
- Automatically attach a standard discovery agenda to new sales calls identified in the CRM.
- Sync internal project sync agendas with the latest status updates from project management tools.

**Workflow Standardization**
- Apply a consistent "Retrospective" template to all end-of-sprint meetings across engineering teams.
- Generate pre-read documents for executive briefings to ensure stakeholders are prepared in advance.

**Administrative Efficiency**
- Reduce manual copy-pasting by auto-populating meeting descriptions with links to relevant project folders.
- Trigger agenda creation workflows immediately upon calendar invite creation for specific meeting titles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the Meeting Template Optimizer.
2. Click "Import" to add the workflow to your workspace.
3. Connect your calendar and documentation tool accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the meeting title and participant list from your calendar trigger.
- **Agent**: Analyzes the meeting context and selects the optimal template from your library.
- **Composio Toolset**: Executes API calls to update calendar invites or create new documents.
- **Chat Output**: Confirms the agenda has been applied and provides a link to the meeting document.

### 3) Run the Flow
Use the Playground to test the flow with these prompts:
- `Apply the 'Discovery Call' template to the meeting titled 'Demo with Acme Corp' at 2 PM.`
- `Generate a 'Weekly Sync' agenda for the engineering team meeting.`
- `Update the 'Project Kickoff' meeting with the standard template and notify the participants.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for template selection and data insertion.
- Use a model capable of structured output to ensure templates are formatted correctly.
- Instruct the agent to prioritize meeting context over generic templates.
- Ensure the agent is configured to handle missing data gracefully by using placeholders.

### 2) Composio Toolset Node
- Provide the necessary API keys for your calendar (e.g., Google Calendar, Outlook) and documentation platforms (e.g., Notion, Google Docs).
- Set the connection scope to allow the agent to read event details and write to document storage.

### 3) Tool Availability
- **Calendar API**: For reading meeting metadata and updating invite descriptions.
- **Document API**: For creating and editing agenda files.
- **Notification Service**: For alerting organizers when an agenda has been successfully attached.

---

## Related Solutions
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Automate the selection and deployment of collaborative workshop boards.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Extract and rank action items from meeting transcripts.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex operational workflows across multiple business tools.
