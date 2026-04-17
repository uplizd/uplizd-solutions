# Meeting Follow-up Assistant (Uplizd) - Automate post-meeting action items and scheduling

## Summary
The Meeting Follow-up Assistant is an intelligent Uplizd workflow designed to streamline post-meeting productivity by automatically extracting action items, drafting follow-up emails, and coordinating scheduling tasks. By integrating directly with your calendar and communication tools, this solution eliminates manual administrative overhead, ensures no commitments are missed, and maintains high pipeline velocity for sales and project management teams.

---

## Demo
![Meeting Follow-up Assistant workflow diagram showing calendar integration and automated email dispatch](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Follow-up Assistant workflow for automated calendar scheduling, email follow-ups, and action item tracking using Composio and AI agents.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/77ba10c4-3fbb-5f8a-9276-9ae16acabeda)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meeting, calendar, follow-up, automation, productivity, scheduling, email, ai workflow
- This solution bridges the gap between meeting insights and execution, ensuring that every conversation leads to measurable progress.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meeting schedules and need to maintain consistent follow-through.

- **Sales Representatives**
  - Automate post-call email sequences to keep prospects engaged and move deals through the pipeline faster.
- **Project Managers**
  - Instantly capture action items from meeting transcripts and assign them to the correct team members.
- **Executive Assistants**
  - Streamline the scheduling of follow-up sessions and coordination of calendar invites without manual back-and-forth.
- **Customer Success Managers**
  - Ensure client feedback and requested resources are delivered promptly after every check-in call.

---

## Features
- **Automated Action Extraction**
  - Uses AI to parse meeting transcripts and identify key tasks, deadlines, and owners automatically.
- **Calendar Synchronization**
  - Leverages the Composio Toolset to read and write calendar events, ensuring follow-up meetings are booked seamlessly.
- **Context-Aware Email Drafting**
  - Generates personalized follow-up emails based on the specific context and decisions made during the meeting.
- **Real-time CRM Updates**
  - Automatically logs meeting summaries and follow-up status into your connected CRM platform.
- **Multi-Platform Integration**
  - Connects with major calendar and email providers to ensure a unified workflow across your existing tech stack.

---

## Use Cases
**Post-Sales Follow-up**
- Send automated summaries to prospects immediately after a demo call with clear next steps.
- Schedule follow-up discovery calls based on availability detected in the prospect's calendar.

**Project Management Coordination**
- Extract action items from internal syncs and push them directly to project management tools.
- Send automated reminders to stakeholders regarding upcoming project milestones discussed in meetings.

**Client Relationship Management**
- Draft personalized "thank you" notes that reference specific pain points discussed during client meetings.
- Sync meeting outcomes to CRM fields to maintain a clean and accurate record of client interactions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Follow-up Assistant template from the library.
3. Connect your required calendar and email accounts via the Composio integration portal.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the meeting transcript or summary notes from the user.
- **Agent**: Analyzes the input to extract action items and draft follow-up communications.
- **Composio Toolset**: Executes calendar bookings, email sending, and CRM updates.
- **Chat Output**: Displays the confirmation of actions taken and the draft content created.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the meeting transcript provided and draft a follow-up email to the client with the identified action items.`
- `Based on the meeting notes, schedule a follow-up call for next Tuesday at 10 AM and send an invite.`
- `Extract all action items from this meeting and update the corresponding opportunity in the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your administrative assistant, focusing on accuracy and professional tone.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for best results.
- Set the system prompt to prioritize clarity, brevity, and professional business language.
- Ensure the agent is instructed to verify all calendar dates against the current user timezone.

### 2) Composio Toolset Node
- Provide your Composio API key in the node settings.
- Ensure the connection scope includes `calendar.read`, `calendar.write`, `email.send`, and `crm.write` permissions.

### 3) Tool Availability
- **Calendar Tools**: List events, create events, and check availability.
- **Email Tools**: Draft messages, send emails, and manage templates.
- **CRM Tools**: Update opportunity records, add meeting notes, and log interactions.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups to maintain pipeline velocity.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score opportunities based on meeting signals and lead data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across platforms to ensure consistent meeting records.
