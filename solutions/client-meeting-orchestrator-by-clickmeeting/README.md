# Client Meeting Orchestrator (Uplizd) - Streamline scheduling and follow-up workflows

## Summary
The Client Meeting Orchestrator (Uplizd) is an intelligent automation workflow designed to eliminate the friction of manual meeting management. By integrating ClickMeeting with your CRM and communication channels, this solution ensures that meeting invitations, participant tracking, and post-meeting follow-ups are handled autonomously, allowing teams to focus on high-value client interactions rather than administrative logistics.

---

## Demo
![Client Meeting Orchestrator workflow showing automated scheduling and follow-up triggers in the Uplizd builder](image.png)
**Alt text (SEO-ready):** Client Meeting Orchestrator workflow automation for ClickMeeting, CRM scheduling, and automated follow-up sequences on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/891776ea-d08f-54f3-b0f8-6e41359d5bb6)

---

## Category
**Primary category:** Operations  
**Secondary tags:** `clickmeeting`, `scheduling`, `meeting-automation`, `crm`, `client-relations`, `workflow-automation`, `composio`  
This solution bridges the gap between video conferencing platforms and business operations to ensure seamless meeting lifecycle management.

---

## Who is this for?
This solution is designed for professionals who manage high volumes of client interactions and need to maintain a consistent, professional communication cadence.

* **Account Managers**
    * Automate the scheduling of recurring check-ins and ensure no follow-up task is missed after a client call.
* **Sales Representatives**
    * Reduce time spent on manual calendar coordination and focus on closing deals through automated meeting reminders.
* **Customer Success Managers**
    * Maintain high engagement levels by triggering personalized post-meeting summaries and action items automatically.
* **Operations Leads**
    * Standardize the meeting lifecycle across the organization to ensure data hygiene and consistent client experience.

---

## Features
- **Automated Scheduling**
  Syncs availability and creates meeting instances directly within ClickMeeting based on CRM triggers.
- **Real-time Participant Sync**
  Automatically registers attendees and updates their status in your CRM system as they join sessions.
- **Intelligent Follow-up**
  Triggers personalized email or Slack notifications post-meeting based on attendance and meeting duration.
- **Action Item Extraction**
  Uses the Agent node to parse meeting transcripts and identify key takeaways for CRM logging.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely bridge ClickMeeting APIs with your existing tech stack.

---

## Use Cases
**Meeting Lifecycle Management**
* Automating the creation of ClickMeeting rooms when a deal reaches a specific stage in the CRM.
* Sending automated calendar invites and pre-meeting materials to participants upon registration.

**Post-Meeting Engagement**
* Automatically logging meeting attendance and duration back to the client record in the CRM.
* Sending a personalized "Thank You" and summary document to clients immediately after the meeting ends.

**Operational Efficiency**
* Rescheduling or canceling meetings based on real-time updates from the client via email or chat.
* Generating weekly reports on meeting frequency and attendance rates for team performance reviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Client Meeting Orchestrator template from the solution library.
3. Connect your ClickMeeting and CRM accounts via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the trigger event (e.g., "New Meeting Request" or "Meeting Ended").
* **Agent:** Processes the intent, parses meeting details, and determines the necessary action.
* **Composio Toolset:** Executes the specific ClickMeeting API calls or CRM updates required.
* **Chat Output:** Confirms the action completion or surfaces errors for manual intervention.

### 3) Run the Flow
Use the Playground to test your orchestration:
* `Schedule a new client meeting with [Client Name] for next Tuesday at 2 PM.`
* `Send a follow-up email to all attendees of the meeting [Meeting ID] with the summary.`
* `Update the CRM status for all participants who attended the session today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator, interpreting meeting data and mapping it to tool actions.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
* Ensure the system prompt emphasizes accurate extraction of meeting times and participant emails.
* Configure the agent to handle missing information by requesting clarification via the Chat Output.

### 2) Composio Toolset Node
* Provide your API key for the ClickMeeting and CRM integrations.
* Set the connection scope to allow read/write access to meeting schedules and contact records.

### 3) Tool Availability
* `clickmeeting_create_meeting`: For generating new session links.
* `crm_update_contact`: For logging meeting history.
* `email_send_template`: For automated follow-up communications.

---

## Related Solutions
* [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) — Manage collaborative sessions and workshop logistics.
* [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Strengthen client ties through automated CRM data management.
* [Customer Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) — Route and manage incoming support inquiries efficiently.
