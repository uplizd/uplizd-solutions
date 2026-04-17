# Meeting Cancellation Optimizer (Uplizd) - Automate rescheduling and minimize calendar friction

## Summary
The Meeting Cancellation Optimizer is an intelligent Uplizd AI workflow designed to handle last-minute meeting cancellations, identify optimal rescheduling slots, and maintain calendar hygiene. By integrating with Calendly, this solution automates the communication loop between hosts and attendees, ensuring that canceled appointments are immediately addressed to preserve pipeline velocity and professional scheduling standards.

---

## Demo
![Meeting Cancellation Optimizer workflow screenshot showing the integration between Chat Input, Agent, Calendly Composio Toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Meeting Cancellation Optimizer workflow for automated rescheduling, featuring Uplizd AI, Calendly integration, and real-time calendar management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e2fe2888-02fe-59fc-af47-dacfb51ca351)

---

## Category
**Primary category:** Operations
**Secondary tags:** calendly, scheduling, calendar management, meeting automation, sales operations, customer success, workflow automation, ai agent
This solution streamlines meeting lifecycle management by automating the rescheduling process to reduce administrative overhead and improve attendee experience.

---

## Who is this for?
This solution is designed for professionals who manage high-volume scheduling and need to maintain calendar efficiency without manual intervention.

*   **Sales Representatives**
    *   Instantly offer alternative time slots to prospects to prevent deal stalls after a cancellation.
*   **Customer Success Managers**
    *   Automate the rescheduling of onboarding or check-in calls to ensure consistent client engagement.
*   **Executive Assistants**
    *   Reduce the back-and-forth email volume by letting the AI propose new meeting times based on real-time availability.
*   **Operations Managers**
    *   Maintain clean calendar data and ensure no meeting opportunity is lost due to manual scheduling delays.

---

## Features
- **Automated Rescheduling Logic**
  The agent detects cancellations and automatically triggers a search for the next available time slots in the host's calendar.
- **Calendly Integration**
  Leverages the Composio Toolset to securely interact with Calendly APIs for real-time event management and availability checks.
- **Context-Aware Communication**
  Drafts personalized rescheduling messages that maintain professional tone while providing clear calls to action for the attendee.
- **Real-Time Calendar Sync**
  Ensures that proposed slots are cross-referenced against existing commitments to avoid double-booking.
- **Proactive Follow-up**
  Automatically notifies the relevant stakeholders once a new time has been successfully proposed or confirmed.

---

## Use Cases
**Sales Pipeline Protection**
*   Automatically send a rescheduling link to a prospect immediately after they cancel a discovery call.
*   Update the CRM status of a lead if a meeting is canceled and no new time is selected within 24 hours.

**Client Success & Support**
*   Reschedule recurring quarterly business reviews (QBRs) without manual coordination.
*   Offer priority slots to high-value clients when a conflict arises in the support schedule.

**Administrative Efficiency**
*   Sync canceled meeting details across multiple platforms to keep team calendars accurate.
*   Generate a summary report of all canceled and rescheduled meetings at the end of each week.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the solution in your workspace.
2. Select your preferred environment and click "Import Flow."
3. Connect your Calendly account via the Composio integration settings.
4. Ensure nodes are correctly mapped and the Agent has access to the necessary calendar permissions.

### 2) Setup the Nodes
*   **Chat Input**: Receives the cancellation notification or rescheduling request.
*   **Agent**: Analyzes the meeting context and determines the best course of action.
*   **Composio Toolset**: Executes the Calendly API calls to fetch availability and update event times.
*   **Chat Output**: Delivers the proposed new time or confirmation message to the user.

### 3) Run the Flow
Use the Playground to test the agent's response to various cancellation scenarios:
*   `"A prospect just canceled their demo for tomorrow, please find the next available slot and email them."`
*   `"Check my calendar for the next 3 days and propose two new times to the client who canceled our meeting."`
*   `"What is the status of the meeting that was canceled by the client this morning?"`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling assistant that balances professional courtesy with efficiency.
*   Prioritize the host's primary calendar availability when suggesting new times.
*   Maintain a helpful, non-intrusive tone in all automated communications.
*   Always verify the event ID before attempting to modify or reschedule a meeting.

### 2) Composio Toolset Node
Requires a valid Calendly API key connected through the Composio platform. Ensure the scope includes `read` and `write` access to your calendar events.

### 3) Tool Availability
*   **Calendly List Events**: Retrieve details of the canceled meeting.
*   **Calendly Get Availability**: Query open slots for the upcoming week.
*   **Calendly Update Event**: Modify the meeting time once a new slot is selected.
*   **Email/Notification Tools**: Send the rescheduling proposal to the attendee.

---

## Related Solutions
*   [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate CRM account creation and configuration.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales stages and follow-up workflows.
*   [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) — Monitor and manage operational risks.
