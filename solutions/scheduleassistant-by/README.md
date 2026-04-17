# Schedule Assistant (Uplizd) - Automated calendar coordination and meeting management

## Summary
The Schedule Assistant by Uplizd streamlines your professional calendar by automating meeting coordination, conflict resolution, and appointment scheduling. This AI-driven workflow integrates directly with your existing calendar tools to eliminate manual back-and-forth, ensuring your pipeline velocity remains high while maintaining perfect scheduling hygiene.

---

## Demo
![Uplizd Schedule Assistant workflow showing automated calendar booking and conflict resolution](image.png)
**Alt text (SEO-ready):** Uplizd Schedule Assistant workflow for automated calendar booking, meeting scheduling, and conflict resolution using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b8c8f4ad-c058-5b6b-882e-2fd9212d3347)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** calendar, scheduling, meeting management, productivity, time management, automation, ai workflow, composio
- This solution optimizes your daily operations by bridging the gap between communication channels and your calendar availability.

---

## Who is this for?
This solution is designed for professionals who need to reclaim their time and ensure seamless meeting logistics.

- **Sales Development Representative (SDR)**
    - Automates the booking of discovery calls directly from incoming lead inquiries.
- **Account Executive (AE)**
    - Prevents double-booking and ensures high-priority prospect meetings are always scheduled.
- **Operations Manager**
    - Maintains consistent scheduling protocols across the entire team to improve operational efficiency.
- **Executive Assistant**
    - Offloads routine calendar maintenance and rescheduling tasks to an intelligent, reliable agent.

---

## Features
- **Intelligent Conflict Detection**
    - Automatically identifies overlapping commitments and suggests the next best available time slots.
- **Real-time Calendar Sync**
    - Uses the Composio Toolset to fetch and update availability across platforms in real-time.
- **Automated Meeting Invitations**
    - Generates and sends calendar invites with pre-populated meeting details and video conferencing links.
- **Natural Language Scheduling**
    - Interprets complex scheduling requests from chat inputs to execute precise calendar actions.
- **Dynamic Rescheduling**
    - Handles last-minute changes by automatically notifying stakeholders and updating the calendar event.

---

## Use Cases
**Lead Qualification & Booking**
- Automatically schedule a discovery call when a lead reaches a specific qualification score.
- Sync prospect availability with your calendar to propose three optimal meeting times via email.

**Internal Team Coordination**
- Coordinate recurring team syncs by analyzing individual team member availability.
- Manage interview scheduling by cross-referencing candidate availability with hiring manager calendars.

**Client Relationship Management**
- Proactively offer follow-up meeting slots after a deal stage transition in your CRM.
- Manage client check-in calls to ensure regular touchpoints are never missed or forgotten.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Schedule Assistant template file provided in this repository.
3. Connect your preferred calendar integration (e.g., Google Calendar, Outlook) via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting times or scheduling changes.
- **Agent**: Processes intent and extracts date, time, and participant information.
- **Composio Toolset**: Executes the API calls to read availability and write new calendar events.
- **Chat Output**: Confirms the scheduled meeting details or provides alternative slots to the user.

### 3) Run the Flow
Use the Playground to test your assistant with these prompts:
- `Schedule a 30-minute discovery call with john.doe@example.com for next Tuesday morning.`
- `Find a time for a team sync next week and send out the invites.`
- `Reschedule my 2 PM meeting with the marketing team to Thursday at 10 AM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling coordinator that prioritizes accuracy and professional tone.
- Use a system prompt that defines the agent's authority to modify calendar events.
- Ensure the agent is instructed to verify availability before confirming any booking.
- Configure the agent to ask for clarification if a request is ambiguous (e.g., "Which time zone?").

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection between Uplizd and your calendar provider.
- Set the connection scope to include read/write access for calendar events and contact lists.

### 3) Tool Availability
- **Calendar Read**: Fetch existing events and free/busy status.
- **Calendar Write**: Create, update, and delete calendar events.
- **Contact Search**: Retrieve email addresses and participant details from your CRM or contact list.

---

## Related Solutions
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Automates the creation and configuration of new client accounts.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines complex operational workflows for project management.
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Enhances account management by automating relationship tracking and engagement.
