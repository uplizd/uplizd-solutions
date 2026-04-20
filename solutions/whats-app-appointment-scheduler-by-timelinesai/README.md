# WhatsApp Appointment Scheduler (Uplizd) - Automated meeting coordination and reminders

## Summary
The WhatsApp Appointment Scheduler by TimelinesAI is an intelligent Uplizd workflow that streamlines meeting coordination by syncing calendar availability directly with WhatsApp conversations. By leveraging the Composio Toolset, this agent eliminates back-and-forth scheduling friction, automatically creates calendar events, and sends timely confirmation reminders, ensuring high-velocity communication and improved appointment show-up rates for sales and support teams.

---

## Demo
![WhatsApp Appointment Scheduler workflow interface showing automated message parsing and calendar booking integration](image.png)
**Alt text (SEO-ready):** WhatsApp Appointment Scheduler workflow in Uplizd, featuring automated meeting booking, calendar synchronization, and WhatsApp message parsing via TimelinesAI and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a5eb21a1-4da7-5d04-8445-3925f7c5eed2)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** whatsapp, timelinesai, scheduling, calendar, customer engagement, meeting management, composio, ai workflow
- This solution bridges the gap between instant messaging and calendar management to automate the appointment lifecycle.

---

## Who is this for?
This solution is designed for teams managing high-volume client interactions who need to maintain a professional scheduling flow within informal chat channels.

- **Sales Representatives**
    - Reduce lead response time by booking discovery calls directly within the WhatsApp interface.
- **Customer Success Managers**
    - Coordinate account review meetings without leaving the client's preferred communication platform.
- **Operations Managers**
    - Standardize meeting hygiene and ensure all client touchpoints are logged in the central calendar.
- **Small Business Owners**
    - Automate appointment reminders to minimize no-shows and optimize daily availability.

---

## Features
- **Intelligent Intent Recognition**
    - The agent parses natural language in WhatsApp messages to identify scheduling requests and preferred time slots.
- **Real-time Calendar Sync**
    - Uses the Composio Toolset to query availability and book events directly into your connected calendar provider.
- **Automated Confirmation Loop**
    - Automatically triggers a confirmation message back to the user once the appointment is successfully scheduled.
- **Proactive Reminder System**
    - Configurable logic to send automated WhatsApp reminders to clients prior to the scheduled meeting time.
- **Seamless TimelinesAI Integration**
    - Leverages the TimelinesAI API to handle message routing and persistent chat context for a smooth user experience.

---

## Use Cases
**Meeting Coordination**
- Automatically convert a casual "let's talk next week" WhatsApp message into a scheduled calendar event.
- Sync multiple time zone preferences to ensure meeting times are accurate for both the agent and the client.

**Client Retention**
- Send automated follow-up messages after a meeting to request feedback or schedule the next check-in.
- Proactively offer available slots to churn-risk clients to ensure consistent engagement.

**Sales Pipeline Velocity**
- Qualify leads through chat and immediately offer a booking link or slot to keep the momentum going.
- Reduce administrative overhead by eliminating manual data entry between WhatsApp and your CRM/Calendar.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your TimelinesAI and Calendar accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming WhatsApp messages from the TimelinesAI webhook.
- **Agent**: Processes natural language intent and determines the required scheduling action.
- **Composio Toolset**: Executes calendar search, event creation, and availability checks.
- **Chat Output**: Sends the confirmation or scheduling prompt back to the user via WhatsApp.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Can we schedule a 30-minute discovery call for next Tuesday afternoon?`
- `I need to reschedule my meeting with John Doe to Wednesday at 10 AM.`
- `What does my availability look like for a quick sync on Friday?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling assistant that maintains context across the chat session.
- Instruction: "You are a professional scheduling assistant. Always confirm the date, time, and duration before finalizing a booking."
- Instruction: "If a requested slot is unavailable, suggest the next two closest open slots."
- Instruction: "Maintain a helpful and concise tone suitable for WhatsApp communication."

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and has permissions for Calendar and TimelinesAI.
- **Connection Scope**: Grant read/write access to your primary calendar to allow the agent to check for conflicts and create events.

### 3) Tool Availability
- **Calendar Search**: Query existing events to prevent double-booking.
- **Event Creation**: Add new appointments to the calendar.
- **Message Dispatcher**: Send automated WhatsApp replies via TimelinesAI.

---

## Related Solutions
- [WhatsApp Lead Qualifier (TimelinesAI)](../whats-app-lead-qualifier-by-timelinesai/README.md) — Qualify incoming leads directly within WhatsApp conversations.
- [WhatsApp Support Automator (TimelinesAI)](../whats-app-support-automator-by-timelinesai/README.md) — Automate ticket triage and support responses for faster resolution.
- [WhatsApp Webhook Integration Manager (TimelinesAI)](../whats-app-webhook-integration-manager-by-timelinesai/README.md) — Manage and route incoming webhooks for complex WhatsApp workflows.
