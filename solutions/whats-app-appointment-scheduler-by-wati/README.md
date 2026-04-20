# WhatsApp Appointment Scheduler (Uplizd) - Automate meeting bookings via WhatsApp

## Summary
The WhatsApp Appointment Scheduler by WATI is an intelligent Uplizd workflow that bridges the gap between conversational messaging and calendar management. By leveraging the Composio Toolset to interface with scheduling platforms, this solution enables businesses to capture, qualify, and confirm appointments directly within a WhatsApp chat interface, reducing friction in the booking process and ensuring a single source of truth for your team's availability.

---

## Demo
![WhatsApp Appointment Scheduler workflow interface showing chat input, agent processing, and calendar confirmation](image.png)
**Alt text (SEO-ready):** WhatsApp Appointment Scheduler workflow by Uplizd, demonstrating automated meeting booking, calendar integration, and WhatsApp messaging automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d44f35c1-4b17-54d1-ab16-061f30706ab8)

---

## Category
- **Primary category:** Communication
- **Secondary tags:** whatsapp, wati, scheduling, calendar, automation, customer engagement, ai workflow, composio
- This solution streamlines customer interactions by integrating real-time calendar availability with the ubiquity of WhatsApp messaging.

---

## Who is this for?
This solution is designed for customer-facing teams looking to eliminate manual back-and-forth scheduling.

- **Sales Representatives**
    - Automate lead follow-up and meeting booking without leaving the WhatsApp interface.
- **Customer Success Managers**
    - Simplify the process of scheduling check-in calls and training sessions with existing clients.
- **Small Business Owners**
    - Provide a professional, 24/7 booking experience that works directly on mobile devices.
- **Operations Managers**
    - Centralize appointment data and reduce no-shows through automated confirmation flows.

---

## Features
- **Real-time Availability Sync**
    - Connects directly to your calendar to fetch open slots and present them to users instantly.
- **Conversational Booking Logic**
    - Uses an AI agent to interpret natural language requests and map them to available time blocks.
- **Automated Confirmation**
    - Triggers instant WhatsApp notifications to both the host and the attendee upon successful booking.
- **WATI Integration**
    - Leverages WATI’s robust API to handle message delivery and status updates reliably.
- **Composio-Powered Tooling**
    - Utilizes the Composio Toolset to securely execute calendar operations and CRM updates.

---

## Use Cases
**Lead Qualification & Booking**
- Automatically offer a discovery call slot immediately after a lead expresses interest in a WhatsApp message.
- Sync qualified lead details from the chat directly into your CRM during the booking process.

**Client Support Scheduling**
- Allow clients to request technical support sessions by simply typing their preferred time in WhatsApp.
- Automatically reschedule existing appointments based on client availability updates sent via chat.

**Service Appointment Management**
- Enable customers to book service visits or consultations by selecting from pre-defined time windows.
- Send automated reminders via WhatsApp 24 hours before the scheduled appointment time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Authenticate your WATI and Calendar accounts within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the customer's intent and scheduling request.
- **Agent**: Processes the natural language input to determine the requested time and intent.
- **Composio Toolset**: Executes the calendar lookup and booking action based on agent instructions.
- **Chat Output**: Delivers the confirmation message or follow-up questions to the user.

### 3) Run the Flow
Test your agent in the Uplizd Playground:
- `I would like to book a 30-minute discovery call for next Tuesday.`
- `Can you check if there is availability for a meeting on Thursday afternoon?`
- `I need to schedule a support session as soon as possible, what are your earliest slots?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the conversational interface for your scheduling logic.
- Instruct the agent to prioritize the user's preferred time zone.
- Configure the agent to ask for missing information (e.g., email or company name) before finalizing.
- Ensure the agent maintains a professional and helpful tone consistent with your brand.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication between the agent and your scheduling tools.
- Set the connection scope to allow read/write access to your primary calendar and WATI account.

### 3) Tool Availability
- **Calendar API**: For checking availability and creating events.
- **WATI API**: For sending and receiving WhatsApp messages.
- **CRM Connector**: For logging appointment details against customer profiles.

---

## Related Solutions
- [WhatsApp Lead Qualifier (WATI)](../whats-app-lead-qualifier-by-wati/README.md) - Qualify incoming leads directly through WhatsApp conversations.
- [WhatsApp Order Status Agent (WATI)](../whats-app-order-status-agent-by-wati/README.md) - Provide real-time order tracking updates via WhatsApp.
- [WhatsApp Support Triage Agent (WATI)](../whats-app-support-triage-agent-by-wati/README.md) - Automatically categorize and route incoming support tickets.
