# Sales Meeting Coordinator (Uplizd) - Automate prospect scheduling and follow-up workflows

## Summary
The Sales Meeting Coordinator is an intelligent Uplizd workflow designed to streamline the scheduling lifecycle by automating calendar availability checks, meeting confirmations, and post-meeting follow-up tasks. By integrating directly with your calendar and CRM, this solution eliminates manual coordination overhead, reduces scheduling friction, and ensures that every prospect interaction is logged and followed up on with precision, ultimately increasing pipeline velocity.

---

## Demo
![Sales Meeting Coordinator workflow interface showing automated calendar scheduling and CRM integration steps](image.png)
**Alt text (SEO-ready):** Sales Meeting Coordinator Uplizd workflow for automated calendar scheduling, CRM integration, and prospect follow-up automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5c2f236d-90e1-5f7a-a7ce-c628d8e309f3)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, calendly, meeting scheduling, sales operations, lead follow-up, composio, ai workflow, pipeline management
- This solution bridges the gap between calendar availability and CRM data, ensuring seamless meeting management for high-performing sales teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual administrative tasks from their daily sales cycle.

- **Account Executives**
    - Spend less time on back-and-forth email scheduling and more time closing deals.
- **Sales Development Representatives (SDRs)**
    - Automate the hand-off process from lead qualification to booked discovery meetings.
- **Sales Operations Managers**
    - Standardize meeting documentation and CRM logging across the entire sales organization.
- **Customer Success Managers**
    - Ensure timely follow-ups and recurring check-ins are scheduled without manual intervention.

---

## Features
- **Automated Availability Sync**
    - Real-time calendar synchronization ensures the agent only proposes slots that are genuinely open.
- **CRM Integration**
    - Automatically updates lead or opportunity status in your CRM once a meeting is successfully booked.
- **Intelligent Follow-up Triggers**
    - Automatically schedules post-meeting tasks or sends personalized follow-up emails based on meeting outcomes.
- **Conflict Resolution**
    - Detects and manages overlapping requests to prevent double-booking of high-priority prospect calls.
- **Composio Toolset Connectivity**
    - Leverages the Composio Toolset to securely interface with calendar APIs and CRM platforms without custom middleware.

---

## Use Cases
**Discovery Call Scheduling**
- Automatically parse incoming meeting requests from email and propose the next three available slots.
- Update the lead record in the CRM to "Discovery Scheduled" upon confirmation.

**Post-Meeting Follow-up**
- Trigger a personalized follow-up email template 30 minutes after a meeting concludes.
- Create a follow-up task in the CRM for the assigned Account Executive to review meeting notes.

**Calendar Hygiene**
- Identify and remove "stalled" or unconfirmed meeting invites that have exceeded a 48-hour response window.
- Sync meeting details back to the CRM to ensure a single source of truth for prospect engagement history.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your calendar and CRM connections via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific calendar and CRM environment.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for meeting times or follow-up actions.
- **Agent**: Processes scheduling logic, interprets availability, and determines the next best action.
- **Composio Toolset**: Executes the API calls to read/write calendar events and update CRM records.
- **Chat Output**: Confirms the action taken or provides a summary of the scheduled meeting details.

### 3) Run the Flow
Use the Playground to test the workflow with prompts such as:
- `Schedule a 30-minute discovery call with John Doe for next Tuesday morning.`
- `Check my calendar for availability and propose three times to the lead in the latest email.`
- `Update the CRM for the meeting with Acme Corp and schedule a follow-up for next Friday.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a scheduling assistant that interprets intent and manages tool execution.
- **Instruction Pattern:**
    - Always verify calendar availability before confirming a time slot.
    - Maintain a professional and helpful tone consistent with sales best practices.
    - If a conflict occurs, suggest alternative times based on the user's current calendar state.

### 2) Composio Toolset Node
- **API Key:** Provide your unique Composio API key to enable secure integration.
- **Connection Scope:** Ensure the agent has read/write access to your primary calendar and the specific CRM objects (Leads/Opportunities).

### 3) Tool Availability
- **Calendar API:** Fetch availability, create events, and delete/modify existing bookings.
- **CRM API:** Search for contacts, update lead status, and create follow-up tasks.
- **Email API:** Send confirmation notifications and follow-up templates to prospects.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate prospect intelligence gathering before meetings.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage deal stages and pipeline velocity after the meeting is booked.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensure prospect data remains consistent across platforms.
