# AI Scheduling Chatbot with GPT-4, Calendly, and Gmail (Uplizd) - Automate meeting bookings and email follow-ups

## Summary
The AI Scheduling Chatbot with GPT-4, Calendly, and Gmail is an autonomous workflow designed to streamline appointment management and communication. By integrating LLM-driven intent recognition with calendar availability and email outreach, this solution eliminates manual scheduling friction, ensures timely follow-ups, and provides a seamless booking experience for leads and clients alike.

---

## Demo
![AI Chatbot interface showing a conversation flow with GPT-4, Calendly integration, and Gmail email confirmation](image.png)
**Alt text (SEO-ready):** Uplizd AI scheduling chatbot workflow using GPT-4, Calendly for meeting bookings, and Gmail for automated email notifications.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2f488a20-3c8c-593f-8fb5-a6b5e18c8302)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, calendly, gmail, scheduling, ai agent, composio, lead management, meeting automation
- This solution bridges the gap between conversational AI and operational scheduling to automate the entire lead-to-meeting lifecycle.

---

## Who is this for?
This workflow is designed for teams looking to reclaim time spent on administrative scheduling tasks.

- **Sales Development Representatives (SDRs)**
    - Automate the qualification and booking of discovery calls directly from chat interactions.
- **Customer Success Managers**
    - Simplify the process of scheduling recurring check-ins or support sessions without back-and-forth emails.
- **Small Business Owners**
    - Provide 24/7 booking availability to potential clients while maintaining a professional, personalized communication style.
- **Operations Managers**
    - Standardize the meeting booking process and ensure every interaction is logged and confirmed via email.

---

## Features
- **Intelligent Intent Recognition**
    - Uses GPT-4 to parse natural language requests and determine if a user wants to schedule, reschedule, or inquire about availability.
- **Real-time Calendly Integration**
    - Leverages the Composio Toolset to fetch live availability and create calendar events instantly.
- **Automated Gmail Confirmation**
    - Triggers personalized email follow-ups via Gmail immediately after a successful booking to confirm details.
- **Context-Aware Conversational Flow**
    - Maintains conversation history to ensure the agent remembers user preferences and previous interactions.
- **Seamless Tool Orchestration**
    - Connects disparate platforms (Chat, Calendly, Gmail) into a single, unified pipeline using the Uplizd builder.

---

## Use Cases
**Lead Qualification & Booking**
- Automatically qualify inbound leads via chat and offer immediate booking slots for high-intent prospects.
- Send a confirmation email via Gmail with meeting details and pre-call materials once the slot is secured.

**Client Support & Retention**
- Allow existing clients to request support calls through a chatbot interface without human intervention.
- Sync support meeting times directly to the team's calendar and send automated calendar invites.

**Internal Meeting Coordination**
- Facilitate quick syncs between internal teams by checking shared availability through the agent.
- Automate the follow-up process by sending meeting summaries or action items to participants' Gmail inboxes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Calendly and Gmail accounts within the Composio connection settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language request for a meeting.
- **Agent**: Processes the request using GPT-4 to determine the necessary tool calls.
- **Composio Toolset**: Executes the Calendly booking and Gmail notification actions.
- **Chat Output**: Delivers the final confirmation or response back to the user.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `I'd like to schedule a 30-minute discovery call for next Tuesday.`
- `Can you check my availability for tomorrow and book a meeting with the client?`
- `Send a confirmation email to the client regarding our meeting scheduled for 2 PM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central brain for intent parsing and tool selection.
- **Role:** Act as a professional scheduling assistant that is helpful, concise, and efficient.
- **Instruction Pattern:** 
    - Always verify the user's time zone before checking availability.
    - Confirm all meeting details with the user before finalizing the booking.
    - Use the Gmail tool only after a successful Calendly booking event.

### 2) Composio Toolset Node
- **API Key:** Ensure your Composio API key is active and authorized for both Calendly and Gmail.
- **Connection Scope:** Grant read/write access to your calendar events and Gmail sending permissions.

### 3) Tool Availability
- **Calendly:** `get_availability`, `create_meeting`, `list_event_types`
- **Gmail:** `send_email`, `list_threads`, `get_message`

---

## Related Solutions
- [Account Research Assistant by Zoominfo](../account-research-assistant-by-zoominfo/README.md) — Automate lead intelligence gathering.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize customer data across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales stages and follow-up cadences.
