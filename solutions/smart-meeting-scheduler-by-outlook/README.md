# Smart Meeting Scheduler (Uplizd) - Automated cross-timezone calendar coordination

## Summary
The Smart Meeting Scheduler is an intelligent Uplizd AI workflow designed to streamline calendar management and eliminate scheduling friction. By leveraging the Composio Toolset to interface directly with Outlook, this solution automates the discovery of mutual availability, handles complex time zone conversions, and sends calendar invites, providing a single source of truth for busy teams and ensuring pipeline velocity remains high by reducing administrative overhead.

---

## Demo
![Smart Meeting Scheduler workflow interface showing Outlook calendar integration and agent-driven scheduling logic](image.png)
**Alt text (SEO-ready):** Smart Meeting Scheduler Uplizd workflow, automated calendar management, Outlook integration, AI-driven scheduling, time zone coordination.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d4f128e4-5c1a-5b4f-b2c5-501ca463f14e)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** `calendar`, `outlook`, `scheduling`, `time zone`, `automation`, `composio`, `ai workflow`, `productivity`
- This solution optimizes operational efficiency by automating the manual back-and-forth of meeting coordination through intelligent calendar integration.

---

## Who is this for?
This solution is designed for professionals and teams looking to reclaim time lost to manual scheduling and calendar logistics.

- **Sales Representatives**
    - Automate meeting bookings with prospects immediately after a discovery call to maintain momentum.
- **Executive Assistants**
    - Coordinate complex multi-attendee schedules across global time zones without manual calendar cross-referencing.
- **Project Managers**
    - Sync team availability for recurring syncs and project milestones without constant email threads.
- **Customer Success Managers**
    - Ensure timely follow-up meetings are scheduled to drive account health and usage adoption.

---

## Features
- **Intelligent Availability Detection**
    - Automatically queries Outlook calendars to identify open slots that align with all required participants.
- **Multi-Time Zone Normalization**
    - Handles complex time zone conversions, ensuring meeting invites are sent in the correct local time for every attendee.
- **Automated Invite Generation**
    - Triggers calendar invites directly via the Composio Toolset, eliminating the need for manual entry in Outlook.
- **Conflict Resolution Logic**
    - Detects overlapping commitments and suggests the next best available time window based on priority.
- **Real-time Sync**
    - Maintains a live connection between the AI agent and your calendar to ensure data hygiene and scheduling accuracy.

---

## Use Cases
**Sales Pipeline Acceleration**
- Automatically schedule follow-up discovery calls immediately after lead qualification.
- Sync demo sessions with prospect availability to reduce the sales cycle duration.

**Team Coordination**
- Organize recurring weekly stand-ups by finding the optimal time for distributed global teams.
- Manage cross-departmental project syncs by identifying gaps in shared calendars.

**Client Relationship Management**
- Book quarterly business reviews (QBRs) automatically based on account health triggers.
- Coordinate onboarding sessions for new clients to ensure a seamless start to the partnership.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Smart Meeting Scheduler to your Uplizd workspace.
3. Connect your Outlook account within the Composio integration settings.
4. Ensure nodes are correctly mapped and the agent is authorized to access your calendar.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting times and attendee details.
- **Agent**: Processes meeting constraints and interacts with the calendar logic.
- **Composio Toolset**: Executes the API calls to read availability and create Outlook events.
- **Chat Output**: Confirms the scheduled meeting details or reports availability conflicts.

### 3) Run the Flow
Use the Playground to test the agent with prompts like:
- `Schedule a 30-minute discovery call with john.doe@example.com for next Tuesday morning.`
- `Find a time for a team sync next week that works for everyone in the EST and PST time zones.`
- `Check my calendar for tomorrow and book a 1-hour slot for a project review with the design team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling coordinator, prioritizing accuracy and clear communication.
- Instruction: Always verify participant availability before proposing a time.
- Instruction: Convert all requested times to the attendee's local time zone.
- Instruction: Provide a clear confirmation summary including the meeting subject, time, and attendees.

### 2) Composio Toolset Node
- **API Key**: Ensure your Outlook/Microsoft Graph API key is active in the Composio dashboard.
- **Connection Scope**: Grant `Calendars.ReadWrite` permissions to allow the agent to manage events.

### 3) Tool Availability
- `list_calendar_events`: Retrieves existing commitments to identify free blocks.
- `create_calendar_event`: Generates the final invite in Outlook.
- `get_user_timezone`: Fetches attendee location data for accurate scheduling.

---

## Related Solutions
- [Account Research Assistant by Zoominfo](../account-research-assistant-by-zoominfo/README.md) - Gather prospect intelligence to inform meeting agendas.
- [Account Relationship Builder by Dynamics365](../account-relationship-builder-by-dynamics365/README.md) - Manage long-term client connections and CRM data.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Extend scheduling triggers into broader operational workflows.
