# Smart Meeting Scheduler (Uplizd) - Automated meeting orchestration and participant management

## Summary
The Smart Meeting Scheduler is an intelligent Uplizd workflow designed to streamline calendar management by automating meeting creation, participant invitations, and schedule conflict resolution. By integrating directly with Zoom, this solution eliminates manual scheduling friction, ensuring that meeting logistics are handled in real-time to maximize team productivity and pipeline velocity.

---

## Demo
![Smart Meeting Scheduler workflow interface showing Zoom integration nodes and automated scheduling logic](image.png)
**Alt text (SEO-ready):** Smart Meeting Scheduler Uplizd workflow for automated Zoom meeting creation, participant management, and calendar synchronization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/d59032c2-8071-5876-8655-c7ed437099c3)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** zoom, scheduling, calendar, automation, meeting management, productivity, composio, ai workflow
- This solution optimizes operational efficiency by automating the end-to-end lifecycle of professional meetings.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting schedules and require a reliable, automated way to handle logistics.

- **Sales Representatives**
    - Automate follow-up meeting creation immediately after discovery calls to maintain momentum.
- **Executive Assistants**
    - Reduce administrative overhead by delegating complex scheduling tasks to an intelligent agent.
- **Project Managers**
    - Ensure consistent meeting cadences for cross-functional teams without manual calendar coordination.
- **Customer Success Managers**
    - Streamline onboarding session scheduling to improve client satisfaction and time-to-value.

---

## Features
- **Automated Meeting Creation**
    - Instantly generate Zoom meeting links and calendar events based on natural language requests.
- **Intelligent Participant Management**
    - Automatically add required attendees and distribute meeting details via integrated communication channels.
- **Real-time Conflict Detection**
    - Leverage the Composio Toolset to cross-reference availability and prevent scheduling overlaps.
- **Dynamic Agenda Integration**
    - Populate meeting descriptions with relevant context or action items extracted from previous chat history.
- **Seamless Zoom Connectivity**
    - Utilize secure API integrations to manage meeting settings, security, and recording preferences automatically.

---

## Use Cases
**Sales Pipeline Acceleration**
- Automatically schedule discovery calls with leads directly from CRM-linked chat threads.
- Sync meeting outcomes back to the CRM to keep deal stages updated without manual entry.

**Operational Efficiency**
- Coordinate recurring internal syncs by automatically finding the next available time slot for all participants.
- Manage large-scale webinar scheduling by automating the registration and link distribution process.

**Customer Support & Success**
- Schedule technical support deep-dive sessions based on ticket priority and agent availability.
- Automate the booking of quarterly business reviews (QBRs) to ensure consistent client engagement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the solution template.
2. Select "Import" to load the workflow into your Uplizd workspace.
3. Authenticate your Zoom and calendar accounts within the integration settings.
4. Ensure nodes are correctly connected from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts natural language requests for meeting times and participants.
- **Agent**: Processes scheduling intent and maps requirements to tool calls.
- **Composio Toolset**: Executes Zoom API commands to create meetings and manage calendar events.
- **Chat Output**: Confirms meeting details, sends invite links, and provides a summary to the user.

### 3) Run the Flow
Use the Playground to test your scheduler with these prompts:
- `Schedule a 30-minute discovery call with john.doe@example.com for tomorrow at 2 PM.`
- `Create a Zoom meeting for the project sync team next Monday at 10 AM and send the invite.`
- `Find a time for a follow-up meeting with the client and generate a Zoom link.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for scheduling logic.
- Use a model capable of high-precision tool calling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: Always verify participant availability before confirming a meeting time.
- Instruction: Ensure all Zoom meeting settings (e.g., waiting room, recording) are applied based on the user's default preferences.

### 2) Composio Toolset Node
- Provide your Zoom API key and ensure the connection scope includes `meeting:write` and `calendar:read`.
- Configure the toolset to allow the agent to read/write to your primary calendar.

### 3) Tool Availability
- **Zoom Meeting Manager**: Create, update, and delete meeting instances.
- **Calendar Sync Tool**: Check availability and block time slots.
- **Participant Notifier**: Send meeting invitations and updates to specified email addresses.

---

## Related Solutions
- [Zoom Usage Intelligence Agent](../zoom-usage-intelligence-agent/README.md) — Analyze meeting patterns and attendance data.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gather prospect intelligence before scheduling meetings.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Manage follow-up tasks generated during scheduled meetings.
