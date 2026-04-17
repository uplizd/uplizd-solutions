# Smart Meeting Recorder (Uplizd) - Automated meeting capture and intelligent workflow management

## Summary
The Smart Meeting Recorder (Uplizd) streamlines meeting operations by automatically triggering recordings and managing post-meeting workflows based on participant lists and discussion topics. This solution ensures that critical business conversations are captured, transcribed, and indexed, providing teams with a single source of truth and reducing the administrative burden of manual meeting documentation.

---

## Demo
![Smart Meeting Recorder workflow dashboard showing automated recording triggers and participant-based meeting management](image.png)
**Alt text (SEO-ready):** Smart Meeting Recorder dashboard by Uplizd, showing automated meeting capture, participant-based triggers, and AI-driven workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/671b5ab5-eb00-552e-9206-84d573a55e9c)

---

## Category
**Primary category:** Operations
**Secondary tags:** meeting management, recallai, automation, productivity, workflow, transcription, ai assistant, team collaboration.
This solution bridges the gap between live communication and actionable data by automating the recording lifecycle for high-stakes business meetings.

---

## Who is this for?
This solution is designed for professionals who need to maintain accurate records of complex discussions and ensure follow-up actions are never missed.

*   **Project Managers**
    *   Ensures all stakeholder decisions are recorded and indexed for project audit trails.
*   **Sales Representatives**
    *   Captures prospect requirements and objections automatically to improve deal closing velocity.
*   **Executive Assistants**
    *   Automates the documentation of board meetings and leadership syncs to focus on high-value support.
*   **Customer Success Managers**
    *   Maintains a searchable history of client feedback and support requests directly from meeting transcripts.

---

## Features
- **Automated Recording Triggers**
  Intelligently starts recording sessions based on calendar invites, specific participant lists, or predefined meeting topics.
- **Composio-Powered Integration**
  Seamlessly connects meeting data with your existing CRM and project management tools using the Composio Toolset.
- **Real-time Transcription Processing**
  Processes audio streams into high-fidelity text, allowing the agent to extract key insights and action items immediately.
- **Participant-Based Logic**
  Customizes recording rules based on the seniority or role of attendees, ensuring compliance and focus on critical meetings.
- **Centralized Meeting Repository**
  Organizes all recordings and summaries in one location, facilitating easy search and retrieval for team members.

---

## Use Cases
**Meeting Documentation**
*   Automatically generate and store meeting minutes in your internal wiki or document management system.
*   Flag specific segments of a meeting for review based on keywords like "budget," "timeline," or "risk."

**Sales Pipeline Management**
*   Sync meeting action items directly to your CRM to ensure follow-up tasks are assigned to the correct account owner.
*   Analyze prospect sentiment during discovery calls to score deal health and identify potential churn signals.

**Operational Efficiency**
*   Trigger automated follow-up emails to participants containing a summary of the meeting and assigned action items.
*   Archive meeting recordings to cloud storage with automated naming conventions based on date, topic, and participants.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your RecallAI and CRM/Tool connections within the builder.
4. Ensure nodes are correctly mapped to your specific API credentials and environment settings.

### 2) Setup the Nodes
*   **Chat Input**: Receives the meeting trigger signal or manual request to initiate recording.
*   **Agent**: Analyzes the meeting context and determines the necessary actions based on your instructions.
*   **Composio Toolset**: Executes API calls to RecallAI for recording and your CRM for data logging.
*   **Chat Output**: Confirms the recording status and provides a summary of the processed meeting data.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Record all meetings today involving the 'Enterprise Sales' team.`
* `Summarize the last meeting with the client 'Acme Corp' and update the CRM notes.`
* `Find all meetings where 'budget' was discussed and extract the action items.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for meeting intelligence and tool execution.
*   Maintain a neutral, professional tone for all meeting summaries.
*   Prioritize the extraction of "Action Items" and "Key Decisions" in every transcript analysis.
*   Use the Composio Toolset to verify data existence before attempting to update external records.

### 2) Composio Toolset Node
Connect your RecallAI API key and your target CRM (e.g., Salesforce, HubSpot) to the Composio Toolset node. Ensure the connection scope includes read/write access to meetings, contacts, and tasks.

### 3) Tool Availability
*   **RecallAI**: Start/Stop recording, fetch transcripts, list meeting participants.
*   **CRM Connector**: Create/Update tasks, append notes to contact records, search account history.
*   **Notification Service**: Send summary emails or Slack alerts to relevant stakeholders.

---

## Related Solutions
* [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Automate voice-based customer support interactions.
* [account-research-assistant-by-zoominfo](../account-research-assistant-by-zoominfo/README.md) - Enrich account data with deep research and intelligence.
* [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from team communications.
