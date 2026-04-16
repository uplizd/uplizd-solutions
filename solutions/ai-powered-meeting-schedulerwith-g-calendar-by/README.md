# AI-Powered Meeting Scheduler (Uplizd) - Automate calendar availability and scheduling

## Summary
The AI-Powered Meeting Scheduler streamlines your calendar management by intelligently parsing meeting requests and syncing directly with Google Calendar. This Uplizd workflow eliminates manual scheduling friction, reduces double-bookings, and ensures your availability is always up-to-date, providing a seamless experience for both internal teams and external stakeholders.

---

## Demo
![AI-Powered Meeting Scheduler workflow interface showing Chat Input, Agent node, Google Calendar toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** AI-Powered Meeting Scheduler workflow on Uplizd, demonstrating automated Google Calendar integration, real-time availability sync, and AI-driven meeting coordination.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/6d9f38b4-6b23-5f40-ab01-d3f694c0e900)

---

## Category
- **Primary category:** Productivity Automation
- **Secondary tags:** google calendar, scheduling, time management, ai workflow, calendar sync, automation, composio, meeting management
- This solution optimizes time-blocking and scheduling workflows by connecting AI agents directly to your Google Calendar ecosystem.

---

## Who is this for?
This solution is designed for professionals who need to reclaim their time and eliminate the back-and-forth of scheduling.

- **Sales Representatives**
    - Automatically book discovery calls and demos without manual calendar cross-referencing.
- **Executive Assistants**
    - Manage complex calendars and prioritize high-value meetings through intelligent AI triage.
- **Project Managers**
    - Coordinate team syncs and stakeholder updates by instantly identifying open slots.
- **Freelancers & Consultants**
    - Provide clients with frictionless booking experiences that sync directly to your primary calendar.

---

## Features
- **Intelligent Intent Parsing**
    - Uses natural language processing to extract date, time, and duration requirements from unstructured chat inputs.
- **Real-time Calendar Sync**
    - Leverages the Composio Toolset to perform live lookups and event creation in Google Calendar.
- **Conflict Resolution**
    - Automatically detects overlapping commitments and suggests the next best available time slots.
- **Automated Event Creation**
    - Instantly generates calendar invites with meeting details, descriptions, and participant information.
- **Composio-Powered Connectivity**
    - Securely manages authentication and API interactions between the agent and your Google account.

---

## Use Cases
**Sales Pipeline Velocity**
- Instantly schedule follow-up meetings with leads immediately after a discovery call.
- Block out time for deal preparation based on upcoming opportunity deadlines.

**Team Coordination**
- Sync internal project syncs across multiple team members' calendars automatically.
- Manage recurring status updates without manual entry or email threads.

**Client Relationship Management**
- Allow clients to request meetings via chat, with the agent handling the availability check.
- Send automated confirmation details to participants once a slot is successfully reserved.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the AI-Powered Meeting Scheduler template from the solution library.
3. Connect your Google Calendar account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting times.
- **Agent**: Processes the request and determines the necessary calendar action.
- **Composio Toolset**: Executes the Google Calendar API commands to check or book slots.
- **Chat Output**: Confirms the scheduled meeting details or provides alternative options to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Check my availability for tomorrow and suggest three 30-minute slots for a client call.`
- `Schedule a meeting with John Doe for next Tuesday at 2 PM for one hour regarding the project launch.`
- `Do I have any conflicts on Friday afternoon? If so, move my 3 PM meeting to Monday morning.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling assistant that maintains your professional availability constraints.
- Instruction: "You are a professional scheduling assistant. Always verify calendar availability before confirming a booking."
- Instruction: "If a requested time is unavailable, suggest the two closest alternatives."
- Instruction: "Ensure all calendar events include a clear title and the participant's name."

### 2) Composio Toolset Node
- Requires a valid Google Calendar API key or OAuth connection.
- Ensure the connection scope includes `calendar.events` and `calendar.readonly` permissions.

### 3) Tool Availability
- `list_events`: Retrieve current calendar commitments.
- `create_event`: Add new meetings to the calendar.
- `get_free_busy`: Identify open time slots for scheduling.
- `update_event`: Modify existing meeting details or times.

---

## Related Solutions
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Build and maintain stronger client relationships through automated CRM tracking.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline end-to-end business operations and task management.
- [../workspace-setup-optimizer-by-clockify/README.md](../workspace-setup-optimizer-by-clockify/README.md) - Optimize time tracking and workspace productivity metrics.
