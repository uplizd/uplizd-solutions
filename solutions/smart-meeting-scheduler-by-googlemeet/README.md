# Smart Meeting Scheduler (Uplizd) - Automate Google Meet session creation and calendar management

## Summary
The Smart Meeting Scheduler (Uplizd) is an intelligent workflow automation that bridges the gap between calendar events and video conferencing infrastructure. By leveraging the Composio Toolset to interface with Google Calendar and Google Meet, this solution eliminates manual scheduling friction, ensures meeting links are generated instantly upon event creation, and maintains a single source of truth for your professional availability.

---

## Demo
![Smart Meeting Scheduler workflow diagram showing Google Calendar integration and automated Meet link generation](image.png)
**Alt text (SEO-ready):** Smart Meeting Scheduler (Uplizd) workflow diagram demonstrating automated Google Meet link generation and calendar synchronization via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-8a0877ce--7c03--5157--947c--5e0cf015e29b-blue)](https://uplizd.ai/solutions/8a0877ce-7c03-5157-947c-5e0cf015e29b)

---

## Category
**Primary category:** Operations  
**Secondary tags:** google meet, google calendar, scheduling, automation, meeting management, composio, ai workflow, productivity  
This solution streamlines administrative scheduling tasks by connecting calendar events directly to video conferencing tools.

---

## Who is this for?
This solution is designed for professionals and teams looking to reduce meeting overhead and eliminate manual scheduling errors.

- **Operations Managers**
    - Automate the creation of recurring team syncs and client onboarding sessions without manual intervention.
- **Sales Representatives**
    - Ensure every prospect meeting has a valid video link generated instantly upon calendar invite acceptance.
- **Executive Assistants**
    - Manage complex calendars with high-volume meeting requests while ensuring consistent video conferencing settings.
- **Project Managers**
    - Maintain organized meeting logs with automated link generation for cross-functional project check-ins.

---

## Features
- **Instant Meet Generation**
  Automatically generates and attaches unique Google Meet links to calendar events as soon as they are created.
- **Calendar Sync Intelligence**
  Real-time monitoring of calendar updates to ensure meeting details remain consistent across all platforms.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely authenticate and execute commands within your Google Workspace environment.
- **Conflict Resolution**
  Detects overlapping events and provides proactive alerts to ensure your schedule remains optimized and error-free.
- **Customizable Meeting Metadata**
  Allows for the automated injection of meeting agendas and participant lists directly into the event description.

---

## Use Cases
**Client Engagement**
- Automatically generate Meet links for discovery calls booked through external scheduling tools.
- Update meeting descriptions with pre-call documentation or CRM-linked opportunity details.

**Internal Team Operations**
- Create recurring daily stand-up sessions with persistent video links for remote teams.
- Manage large-scale department meetings by automating invitation distribution and link generation.

**Administrative Efficiency**
- Batch-process meeting requests from email threads into structured calendar entries with video links.
- Clean up expired or cancelled meeting links to maintain a tidy and professional calendar view.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `smart-meeting-scheduler` JSON configuration file.
3. Connect your Google Workspace credentials within the Composio integration settings.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API connections are active.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting scheduling.
- **Agent**: Interprets intent and extracts date, time, and participant information.
- **Composio Toolset**: Executes the Google Calendar API calls to create events and generate Meet links.
- **Chat Output**: Confirms the meeting creation and provides the generated link to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your scheduler with these prompts:
- `Schedule a 30-minute meeting with the marketing team for tomorrow at 10 AM.`
- `Create a Google Meet session for my client call with John Doe on Friday at 2 PM.`
- `Set up a recurring weekly sync for project updates every Monday at 9 AM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer between user intent and calendar actions.
- Use a model with strong function-calling capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to always verify the availability of the requested time slot before confirming.
- Ensure the agent is configured to request missing information (like participant emails) if not provided in the input.

### 2) Composio Toolset Node
- Provide a valid Google Workspace API key with `calendar` and `meet` scopes.
- Ensure the connection is authorized for the specific user account managing the calendar.

### 3) Tool Availability
- `google_calendar_create_event`: Creates the calendar entry.
- `google_calendar_get_availability`: Checks for scheduling conflicts.
- `google_meet_generate_link`: Creates the video conferencing session.
- `google_calendar_update_event`: Appends meeting links to existing events.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automate customer support interactions with voice-enabled AI.
- [account-setup-agent-by-salesforce](../account-setup-agent-by-salesforce/README.md) - Streamline new account creation and data entry in Salesforce.
- [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex business workflows and task automation.
