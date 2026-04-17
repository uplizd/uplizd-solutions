# Smart Meeting Scheduler (Uplizd) - Automate calendar coordination and meeting logistics

## Summary
The Smart Meeting Scheduler is an intelligent Uplizd workflow that streamlines calendar management by syncing directly with Microsoft Teams and your calendar provider. By leveraging AI to interpret natural language requests, it eliminates back-and-forth scheduling friction, automatically identifying availability, creating meeting invites, and ensuring all participants are aligned, resulting in improved pipeline velocity and reduced administrative overhead.

---

## Demo
![Smart Meeting Scheduler workflow interface showing natural language scheduling prompts and Microsoft Teams integration](image.png)
**Alt text (SEO-ready):** Smart Meeting Scheduler Uplizd workflow interface for automated Microsoft Teams calendar management and AI-driven meeting coordination.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQ19G3+QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcUAAAAF0lEQVR42mP8z8AARsBAMGIQjBqYAgA5/QABJ938+gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/70da9314-1763-5b80-90f5-6e796add05ea)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** microsoft teams, calendar, scheduling, ai workflow, productivity, meeting management, composio, sales operations  
This solution bridges the gap between communication platforms and scheduling tools to automate the meeting lifecycle for high-performing teams.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting cadences and require automated, error-free scheduling.

* **Sales Development Representatives (SDRs)**
    * Automates the booking of discovery calls directly from prospect email threads.
* **Account Executives (AEs)**
    * Ensures meeting invites are populated with correct Teams links and agenda details without manual entry.
* **Operations Managers**
    * Maintains calendar hygiene by preventing double-bookings and ensuring consistent meeting formatting.
* **Executive Assistants**
    * Reduces time spent on calendar coordination by delegating availability checks to an intelligent agent.

---

## Features
- **Natural Language Scheduling**
  Interprets intent from chat inputs to propose, confirm, and update meeting times automatically.
- **Microsoft Teams Integration**
  Generates unique meeting links and populates invite details directly through the Composio Toolset.
- **Real-time Availability Sync**
  Checks calendar status across platforms to ensure proposed times are conflict-free.
- **Automated Agenda Population**
  Automatically attaches context or meeting goals to calendar invites based on previous conversation history.
- **Proactive Conflict Resolution**
  Identifies scheduling overlaps and suggests alternative slots based on participant availability.

---

## Use Cases
**Discovery Call Booking**
* Automatically schedule discovery calls when a lead expresses interest in a demo.
* Sync meeting details to the CRM to ensure the sales pipeline remains updated.

**Internal Team Syncs**
* Coordinate recurring team stand-ups based on shared availability windows.
* Automatically generate Teams meeting links for all internal project touchpoints.

**Follow-up Meeting Management**
* Schedule follow-up sessions immediately after a successful sales call.
* Update existing calendar events if a participant requests a time change via chat.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Meeting Scheduler JSON template provided in this repository.
3. Connect your Microsoft Teams and Calendar accounts via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives natural language requests for meeting times.
* **Agent**: Processes the request, extracts time/date entities, and determines the best action.
* **Composio Toolset**: Executes the API calls to Microsoft Teams and your calendar provider.
* **Chat Output**: Confirms the scheduled meeting details or asks for clarification if slots are unavailable.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Schedule a 30-minute discovery call with John Doe for next Tuesday at 2 PM.`
* `Find a time for a team sync with the sales department later this week.`
* `Reschedule my 4 PM meeting with Sarah to tomorrow morning instead.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling coordinator that maintains context across multiple conversation turns.
* Use a model with strong function-calling capabilities (e.g., GPT-4o).
* Instruction: "Always verify availability before confirming a meeting time."
* Instruction: "If a conflict is detected, suggest three alternative time slots."

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure access to Microsoft Teams and calendar APIs.
* Ensure the connection scope includes `Calendars.ReadWrite` and `OnlineMeetings.ReadWrite`.

### 3) Tool Availability
* `calendar_list_events`: To check existing commitments.
* `calendar_create_event`: To finalize the booking.
* `teams_create_meeting`: To generate the virtual meeting link.
* `calendar_update_event`: To handle rescheduling requests.

---

## Related Solutions
* [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage and nurture complex account relationships within Dynamics 365.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on prospects to prepare for scheduled meetings.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline end-to-end business processes and task management.
