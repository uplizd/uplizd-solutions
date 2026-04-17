# Meeting Follow-up Assistant (Uplizd) - Automate post-meeting recaps and action items

## Summary
The Meeting Follow-up Assistant is an intelligent Uplizd workflow designed to streamline post-meeting communication by automatically transcribing, summarizing, and distributing action items to participants. By leveraging the Composio Toolset to integrate with Zoom and your preferred communication channels, this solution eliminates manual administrative overhead, ensures accountability, and maintains pipeline velocity by keeping stakeholders aligned immediately after a call.

---

## Demo
![Meeting Follow-up Assistant workflow diagram showing Zoom integration, AI summarization, and automated email distribution](image.png)
**Alt text (SEO-ready):** Meeting Follow-up Assistant workflow for automated Zoom transcript analysis, AI-driven action item extraction, and CRM/Email synchronization on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/626ae4ce-6530-5a42-a3f6-ce98029d5bad)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** zoom, meeting notes, action items, sales operations, ai workflow, composio, productivity, follow-up
This solution bridges the gap between live meeting insights and actionable CRM records to improve team efficiency.

---

## Who is this for?
This workflow is designed for professionals who need to maintain momentum after client interactions without manual data entry.

- **Account Executives**
    - Automate the delivery of meeting summaries and next steps to prospects within minutes of a call.
- **Sales Managers**
    - Ensure consistent follow-up quality across the team by standardizing the recap process.
- **Project Managers**
    - Automatically track action items and assign tasks to team members based on meeting transcripts.
- **Customer Success Managers**
    - Capture client feedback and feature requests directly from Zoom recordings for internal reporting.

---

## Features
- **Automated Transcription Processing**
    - Uses AI to ingest raw Zoom transcripts and filter out filler words for clear, concise documentation.
- **Intelligent Action Item Extraction**
    - Automatically identifies commitments, deadlines, and owners mentioned during the conversation.
- **Composio-Powered CRM Integration**
    - Seamlessly pushes meeting summaries and follow-up tasks directly into your CRM or project management tool.
- **Customizable Follow-up Templates**
    - Generates personalized email drafts based on the specific tone and context of the meeting.
- **Real-time Notification Triggers**
    - Alerts relevant stakeholders via email or Slack as soon as the meeting recap is finalized.

---

## Use Cases
**Sales Pipeline Velocity**
- Automatically send a "Thank You" email with a summary of discussed points to prospects immediately after a demo.
- Update CRM opportunity fields with new requirements identified during the discovery call.

**Project & Task Management**
- Convert verbal agreements into Jira tickets or Asana tasks without manual input.
- Sync meeting action items to a shared team calendar to ensure deadlines are met.

**Internal Knowledge Sharing**
- Generate executive summaries for internal stakeholders who were unable to attend the live session.
- Archive meeting highlights in a centralized knowledge base for future reference.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Follow-up Assistant template from the library.
3. Authenticate your Zoom and CRM/Email accounts within the integration settings.
4. Ensure nodes are correctly mapped from the Chat Input to the Agent, then to the Composio Toolset, and finally to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the meeting ID or transcript text.
- **Agent**: Analyzes the text to extract key insights and action items.
- **Composio Toolset**: Executes the API calls to update your CRM or send emails.
- **Chat Output**: Confirms the successful distribution of the follow-up.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize the meeting with [Client Name] and draft a follow-up email.`
- `Extract all action items from the transcript and create tasks in my CRM.`
- `Identify key pain points mentioned in the call and notify the account manager.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your administrative assistant, focusing on accuracy and professional tone.
- **Instruction Pattern:**
    - "Extract only actionable items and assign them to the mentioned stakeholders."
    - "Maintain a professional and helpful tone in all generated follow-up emails."
    - "Summarize the meeting in three bullet points followed by a list of next steps."

### 2) Composio Toolset Node
Connect your specific CRM (e.g., Salesforce, HubSpot) and communication tools (e.g., Gmail, Slack) via the Composio Toolset. Ensure the connection scope includes read/write access to meeting objects and email/messaging APIs.

### 3) Tool Availability
- **Zoom API**: For retrieving meeting transcripts and metadata.
- **CRM Connector**: For updating opportunity records and activity logs.
- **Email/Messaging API**: For sending automated follow-up communications.

---

## Related Solutions
- [Zoom Usage Intelligence Agent](../zoom-usage-intelligence-agent/README.md) - Analyze meeting frequency and participant engagement metrics.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Enrich account data before and after client meetings.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from various communication channels.
