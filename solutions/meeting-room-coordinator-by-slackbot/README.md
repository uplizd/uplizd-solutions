# Meeting Room Coordinator (Uplizd) - Automate Slack-based meeting room scheduling and conflict resolution

## Summary
The Meeting Room Coordinator is an intelligent Uplizd workflow that synchronizes Slack communication with calendar booking systems to streamline office space management. By automating room availability checks and conflict resolution, this solution eliminates manual scheduling friction, ensures a single source of truth for workspace occupancy, and significantly improves team coordination and pipeline velocity for office operations.

---

## Demo
![Meeting Room Coordinator workflow showing Slack integration with calendar booking nodes](image.png)
**Alt text (SEO-ready):** Meeting Room Coordinator Uplizd workflow for Slack-based room booking, calendar synchronization, and automated conflict resolution.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-31b18695--cee2--51d8--b510--a8c612b15b4b-blue)](https://uplizd.ai/solutions/31b18695-cee2-51d8-b510-a8c612b15b4b)

---

## Category
**Primary category:** Workplace operations  
**Secondary tags:** slack, calendar, scheduling, automation, office management, composio, ai workflow, room booking  
This solution bridges the gap between real-time team communication in Slack and structured calendar data to optimize physical workspace utilization.

---

## Who is this for?
This solution is designed for teams looking to eliminate scheduling bottlenecks and improve office resource transparency.

- **Office Manager**
    - Automates room allocation and prevents double-booking conflicts without manual oversight.
- **Operations Lead**
    - Gains visibility into workspace usage patterns to optimize office layout and resource distribution.
- **Team Lead**
    - Reduces time spent coordinating meeting logistics by enabling instant room booking via Slack.
- **IT Administrator**
    - Ensures secure, authenticated access to calendar APIs through the Composio Toolset.

---

## Features
- **Real-time Availability Sync**
    - Instantly queries calendar data to provide accurate room availability status directly in Slack.
- **Automated Conflict Resolution**
    - Detects overlapping bookings and proactively suggests alternative time slots or rooms using AI logic.
- **Slack-Native Interface**
    - Enables users to book, cancel, or reschedule meetings without leaving their primary communication hub.
- **Composio Toolset Integration**
    - Leverages secure, pre-configured connectors to interact with Google Calendar or Microsoft Outlook seamlessly.
- **Smart Notification System**
    - Sends automated booking confirmations and reminders to all meeting participants to reduce no-shows.

---

## Use Cases
**Meeting Scheduling**
- Automatically finding and booking the nearest available conference room based on attendee count.
- Rescheduling recurring team syncs when a room conflict is detected by the system.

**Office Resource Management**
- Tracking room utilization rates to identify underused spaces during peak office hours.
- Managing desk or "hot-seat" reservations for hybrid employees arriving on specific days.

**Communication & Alerts**
- Notifying meeting organizers via Slack when a room becomes available due to a cancellation.
- Providing daily summaries of room bookings to the office management team for maintenance planning.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON configuration file for the Meeting Room Coordinator.
3. Connect your Slack and Calendar accounts via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language booking requests from Slack users.
- **Agent**: Processes intent, checks constraints, and determines the best available room.
- **Composio Toolset**: Executes API calls to read/write calendar events and verify room status.
- **Chat Output**: Delivers confirmation messages or conflict alerts back to the Slack channel.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Book a conference room for 5 people tomorrow at 2 PM for 1 hour.`
- `Is the main boardroom available for a team sync on Friday morning?`
- `Cancel my 3 PM meeting in the library and find me another room for that time.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between Slack and your calendar provider.
- Use a model capable of high-precision tool calling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize "first available" logic when no preference is specified.
- Ensure the agent is configured to ask for clarification if multiple rooms meet the criteria.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure authentication.
- Set the connection scope to include `calendar.read` and `calendar.write` permissions.

### 3) Tool Availability
- **Calendar Search**: Capability to query availability across multiple room calendars.
- **Event Creation**: Ability to create, update, and delete calendar entries.
- **Slack Messaging**: Capability to send direct messages or channel notifications.

---

## Related Solutions
- [../work-hours-compliance-monitor-by-timely/README.md](../work-hours-compliance-monitor-by-timely/README.md) - Monitor and ensure adherence to team work-hour policies.
- [../workspace-usage-analyzer-by-baserow/README.md](../workspace-usage-analyzer-by-baserow/README.md) - Analyze and report on physical workspace utilization data.
- [../workshop-facilitator-agent-by-mural/README.md](../workshop-facilitator-agent-by-mural/README.md) - Automate the setup and management of collaborative workshop sessions.
