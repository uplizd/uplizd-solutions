# WhatsApp Appointment Scheduler (Uplizd) - Automated booking and consultation management

## Summary
The WhatsApp Appointment Scheduler by 2Chat is an intelligent AI workflow that enables seamless scheduling of meetings and consultations directly within WhatsApp conversations. By leveraging the Composio Toolset to interface with calendar systems, this solution eliminates manual coordination, reduces scheduling friction, and ensures real-time availability updates, providing a frictionless experience for both businesses and their clients.

---

## Demo
![WhatsApp Appointment Scheduler workflow interface showing chat input, agent processing, and calendar integration](image.png)
**Alt text (SEO-ready):** WhatsApp Appointment Scheduler workflow in Uplizd showing automated calendar booking, 2Chat integration, and AI-driven scheduling logic.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/38e289ed-b4eb-57dd-97fd-68bcea48b141)

---

## Category
**Primary category:** Communication automation
**Secondary tags:** whatsapp, 2chat, scheduling, calendar, ai workflow, customer engagement, appointment booking, composio
This solution bridges the gap between conversational messaging and operational calendar management to streamline lead conversion.

---

## Who is this for?
This solution is designed for teams looking to automate their intake process and reduce administrative overhead in client-facing roles.

*   **Sales Representatives**
    *   Automate the booking of discovery calls without leaving the WhatsApp interface.
*   **Customer Success Managers**
    *   Streamline the scheduling of onboarding sessions and follow-up consultations.
*   **Small Business Owners**
    *   Provide 24/7 self-service appointment booking to improve client satisfaction.
*   **Operations Managers**
    *   Centralize booking data to ensure consistent pipeline velocity and resource allocation.

---

## Features
- **Real-time Availability Sync**
  Connects directly to your calendar to display accurate, real-time openings to clients.
- **Automated Confirmation Logic**
  Instantly triggers calendar invites and confirmation messages upon successful booking.
- **Conversational Intent Recognition**
  Uses AI to parse natural language requests for specific dates and times within WhatsApp.
- **Multi-Platform Integration**
  Powered by the Composio Toolset to ensure reliable communication between 2Chat and calendar APIs.
- **Conflict Prevention**
  Automatically checks for existing commitments to prevent double-booking of time slots.

---

## Use Cases
**Client Consultation Booking**
*   Allow leads to request and confirm a 30-minute discovery call via WhatsApp.
*   Automatically send a calendar invite link once the user selects a preferred time.

**Service Appointment Management**
*   Enable existing customers to reschedule or confirm service visits without human intervention.
*   Send automated reminders via WhatsApp 24 hours before the scheduled appointment.

**Lead Qualification & Scheduling**
*   Qualify incoming leads through a brief chat before offering a booking link for a sales call.
*   Sync appointment details directly into your CRM to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your 2Chat and Calendar accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the incoming WhatsApp message from the client.
*   **Agent**: Processes the intent and determines the requested time slot.
*   **Composio Toolset**: Executes the calendar lookup and booking action.
*   **Chat Output**: Delivers the confirmation or follow-up message to the user.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these prompts:
* `I would like to book a 30-minute consultation for next Tuesday afternoon.`
* `Can you check if there are any openings for a meeting this coming Friday?`
* `I need to schedule a follow-up call, what is your availability for next week?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the conversational interface between the user and your calendar.
*   Maintain a professional and helpful tone throughout the booking process.
*   Always confirm the date and time zone before finalizing an appointment.
*   If a requested slot is unavailable, suggest the two closest alternatives.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Composio API key is active and authorized for calendar access.
*   **Connection Scope**: Grant read/write permissions to your primary business calendar to allow the agent to fetch availability and create events.

### 3) Tool Availability
*   `calendar_list_events`: To check current availability.
*   `calendar_create_event`: To finalize the booking.
*   `calendar_get_timezone`: To ensure scheduling accuracy across regions.

---

## Related Solutions
* [WhatsApp Lead Qualifier (2Chat)](../whats-app-lead-qualifier-by2chat/README.md) - Qualify incoming leads directly through WhatsApp.
* [WhatsApp Support Triage Agent (2Chat)](../whats-app-support-triage-agent-by2chat/README.md) - Automate support ticket routing and initial responses.
* [WhatsApp Order Status Agent (2Chat)](../whats-app-order-status-agent-by2chat/README.md) - Provide real-time order tracking updates to customers.
* [WhatsApp Feedback Collection Agent (2Chat)](../whats-app-feedback-collection-agent-by2chat/README.md) - Gather post-interaction feedback automatically.
