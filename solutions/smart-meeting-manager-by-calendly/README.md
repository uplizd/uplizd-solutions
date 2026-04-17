# Smart Meeting Manager (Uplizd) - Automated meeting lifecycle orchestration and follow-up

## Summary
The Smart Meeting Manager by Uplizd streamlines the entire meeting lifecycle by automating scheduling, preparation, and post-meeting action item tracking. By integrating directly with Calendly and your communication stack, this AI workflow eliminates manual administrative overhead, ensures meeting readiness, and maintains pipeline velocity by automatically logging outcomes and follow-ups.

---

## Demo
![Smart Meeting Manager workflow interface showing Calendly integration and automated follow-up nodes](image.png)
**Alt text (SEO-ready):** Smart Meeting Manager Uplizd workflow, automated meeting scheduling and follow-up agent powered by Composio and Calendly.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e432f5b8-3cfe-5256-b084-68be3dd339be)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** `calendly`, `meeting management`, `scheduling`, `automation`, `workflow`, `composio`, `ai assistant`, `productivity`
- This solution bridges the gap between calendar availability and CRM data hygiene, ensuring every meeting results in actionable intelligence.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting schedules and need to maintain consistent follow-up protocols.

- **Sales Representatives**
    - Automate post-meeting CRM updates and ensure no lead falls through the cracks after a discovery call.
- **Customer Success Managers**
    - Streamline recurring check-in meetings and ensure client feedback is captured in real-time.
- **Executive Assistants**
    - Reduce manual coordination time by automating pre-meeting briefings and post-meeting summary distribution.
- **Operations Managers**
    - Standardize the meeting lifecycle across the organization to improve data consistency and pipeline visibility.

---

## Features
- **Automated Scheduling**
  Syncs with Calendly to manage availability and trigger workflows the moment a meeting is booked.
- **Pre-Meeting Briefings**
  Automatically pulls attendee history and relevant CRM data to prepare the host before the call begins.
- **Real-time Action Tracking**
  Identifies and extracts action items during the meeting for immediate assignment and tracking.
- **CRM Integration**
  Uses the Composio Toolset to push meeting summaries and follow-up tasks directly into your CRM platform.
- **Intelligent Follow-up**
  Drafts and schedules personalized follow-up emails based on the specific context and outcomes of the meeting.

---

## Use Cases
**Meeting Preparation**
- Automatically generate a pre-call dossier containing recent interaction history and account status.
- Send automated reminders to participants with agenda items to ensure meeting efficiency.

**Post-Meeting Execution**
- Log meeting notes and key takeaways into the CRM immediately after the call concludes.
- Create follow-up tasks for team members based on identified action items and deadlines.

**Pipeline Hygiene**
- Update lead or opportunity stages based on the sentiment and outcome captured during the meeting.
- Flag stalled opportunities that require immediate attention or re-engagement strategies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Workflow" to add the Smart Meeting Manager to your Uplizd dashboard.
3. Connect your Calendly and CRM accounts via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives meeting details or manual trigger commands.
- **Agent**: Processes meeting context and determines the necessary follow-up actions.
- **Composio Toolset**: Executes API calls to Calendly, CRM, and email clients.
- **Chat Output**: Confirms successful logging and displays generated follow-up drafts.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the meeting with John Doe from yesterday and create a follow-up task in the CRM.`
- `Prepare a briefing document for my upcoming meeting with Acme Corp.`
- `Check my calendar for today and draft follow-up emails for all completed discovery calls.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for meeting analysis and data routing.
- Instruction: "Act as a professional meeting assistant; prioritize accuracy in data extraction."
- Instruction: "Ensure all follow-up tasks are assigned to the correct owner in the CRM."
- Instruction: "Maintain a professional and helpful tone in all generated communication."

### 2) Composio Toolset Node
- Requires a valid API key for the Calendly and CRM integrations.
- Scope should include read/write access to calendar events, contacts, and task objects.

### 3) Tool Availability
- **Calendly API**: For retrieving event details and participant information.
- **CRM Connector**: For updating opportunity stages and logging meeting notes.
- **Email Client**: For sending automated follow-up correspondence.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive intelligence gathering for pre-meeting preparation.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Advanced logic for sorting and assigning meeting-derived tasks.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensures meeting data remains consistent across your entire tech stack.
