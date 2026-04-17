# Smart Meeting Scheduler (Uplizd) - Context-aware automated calendar management

## Summary
The Smart Meeting Scheduler (Uplizd) is an intelligent AI workflow designed to streamline calendar management by autonomously coordinating availability, resolving scheduling conflicts, and confirming appointments across your team's tools. By leveraging the Composio Toolset, this solution acts as a single source of truth for your calendar, reducing administrative overhead and ensuring high-velocity pipeline management through automated meeting logistics.

---

## Demo
![Smart Meeting Scheduler workflow interface showing calendar integration and agent decision nodes](image.png)
**Alt text (SEO-ready):** Smart Meeting Scheduler Uplizd workflow, automated calendar management, Composio toolset integration, and AI-driven meeting coordination.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fcfcb191-79e0-5471-9691-bf87b1181291)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** calendar, scheduling, automation, productivity, composio, ai workflow, meeting management, time optimization
- This solution bridges the gap between communication platforms and calendar providers to automate complex scheduling tasks.

---

## Who is this for?
This solution is designed for professionals who need to reclaim time spent on manual coordination and scheduling logistics.

- **Sales Representatives**
    - Automate follow-up meeting bookings immediately after lead qualification to increase conversion rates.
- **Operations Managers**
    - Standardize meeting cadences across departments to ensure consistent team alignment and resource availability.
- **Executive Assistants**
    - Offload repetitive calendar management tasks to an AI agent that handles availability checks and time-zone conversions.
- **Customer Success Managers**
    - Facilitate seamless recurring check-in scheduling without the back-and-forth email overhead.

---

## Features
- **Context-Aware Scheduling**
  The agent analyzes participant availability and existing calendar constraints to suggest optimal meeting times.
- **Composio Toolset Integration**
  Seamlessly connects with calendar APIs to read availability and write new events in real-time.
- **Conflict Resolution**
  Automatically detects overlapping commitments and proposes alternative slots based on user preferences.
- **Automated Invitations**
  Triggers calendar invites and notification emails to all participants once a slot is confirmed.
- **Dynamic Time-Zone Handling**
  Intelligently adjusts meeting times for global participants to prevent scheduling errors across regions.

---

## Use Cases
**Sales Pipeline Velocity**
- Automatically schedule discovery calls immediately after a lead is marked as 'Qualified' in your CRM.
- Sync follow-up meetings with account executives based on real-time availability in the CRM.

**Team Coordination**
- Coordinate recurring internal syncs by identifying the best time for all required stakeholders.
- Manage cross-departmental project check-ins by scanning shared team calendars.

**Customer Support Logistics**
- Schedule technical deep-dive sessions for high-priority support tickets without manual email threads.
- Automate the booking of onboarding sessions for new clients upon account activation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Meeting Scheduler JSON template provided in the repository.
3. Connect your preferred calendar and communication tool credentials via the integration settings.
4. Ensure nodes are correctly mapped to your specific API endpoints and that the agent has the necessary permissions to read/write calendar events.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting times or scheduling constraints.
- **Agent**: Processes the request, checks availability, and determines the optimal meeting slot.
- **Composio Toolset**: Executes the API calls to verify availability and create the calendar event.
- **Chat Output**: Confirms the scheduled meeting details or requests further clarification if conflicts arise.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
- `Schedule a 30-minute discovery call with John Doe for next Tuesday morning.`
- `Find a time for a team sync next week where everyone is available for at least one hour.`
- `Reschedule my meeting with the marketing team to Thursday afternoon due to a conflict.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling coordinator.
- **Recommended instruction pattern:**
    - Act as a professional scheduling assistant with access to calendar data.
    - Prioritize availability windows provided by the user while respecting existing calendar blocks.
    - Always confirm the meeting details (time, duration, participants) before finalizing the event.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure tool execution.
- **Connection Scope:** Ensure the connection scope includes `calendar.read` and `calendar.write` permissions.

### 3) Tool Availability
- **Calendar Search:** Query availability across specific date ranges.
- **Event Creation:** Generate new calendar entries with participant lists and descriptions.
- **Conflict Checker:** Identify overlapping events and suggest alternative time slots.

---

## Related Solutions
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Automate account creation and onboarding workflows.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline operational tasks and field management.
- [../workforce-onboarding-automator-by-connecteam/README.md](../workforce-onboarding-automator-by-connecteam/README.md) - Manage new hire scheduling and documentation.
