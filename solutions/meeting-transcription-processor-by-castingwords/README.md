# Meeting Transcription Processor (Uplizd) - Automated meeting intelligence and documentation

## Summary
The Meeting Transcription Processor by CastingWords is an automated Uplizd AI workflow designed to streamline post-meeting documentation. By integrating advanced transcription capabilities with intelligent processing, this solution transforms raw audio recordings into structured summaries, action items, and searchable transcripts, ensuring teams maintain a single source of truth without the manual overhead of note-taking.

---

## Demo
![Meeting Transcription Processor workflow diagram showing audio input, CastingWords transcription, and AI summary output](image.png)
**Alt text (SEO-ready):** Uplizd meeting transcription workflow, CastingWords audio processing, automated meeting summary and action item extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d274fdb9-41a4-556b-b7f9-7f66bfbea096)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** transcription, meeting intelligence, productivity, ai workflow, composio, documentation, castingwords, automation.
This solution bridges the gap between spoken conversation and actionable data, categorizing it under core operational productivity tools.

---

## Who is this for?
This workflow is designed for professionals who need to convert high-volume meeting audio into structured, actionable intelligence.

- **Project Managers**
    - Automatically generate meeting minutes and track project milestones from recorded discussions.
- **Sales Representatives**
    - Capture key customer requirements and follow-up tasks directly from discovery calls.
- **Executive Assistants**
    - Reduce manual documentation time by automating the transcription and summarization of board meetings.
- **Customer Success Managers**
    - Maintain accurate records of client feedback and support requests to improve retention strategies.

---

## Features
- **High-Accuracy Transcription**
    - Leverages CastingWords to provide human-quality text conversion from diverse audio formats.
- **Automated Summary Generation**
    - Uses the Agent node to distill long-form transcripts into concise executive summaries.
- **Action Item Extraction**
    - Identifies and formats specific tasks, owners, and deadlines mentioned during the meeting.
- **Seamless Integration**
    - Connects audio sources to the Composio Toolset for efficient data routing and storage.
- **Real-Time Processing**
    - Enables rapid turnaround from meeting conclusion to team-wide distribution of insights.

---

## Use Cases
**Meeting Documentation**
- Converting hour-long team syncs into structured bullet points for internal wikis.
- Archiving client call transcripts for compliance and historical reference.

**Task Management**
- Automatically syncing identified action items to project management boards.
- Assigning follow-up tasks to team members based on meeting context.

**Strategic Analysis**
- Identifying recurring pain points or feature requests across multiple customer discovery calls.
- Analyzing sentiment and tone in executive meetings to gauge project health.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Transcription Processor template from the solution library.
3. Authenticate your CastingWords and relevant CRM/storage connectors via the Composio dashboard.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the audio file URL or raw recording data.
- **Agent**: Processes the transcription text to extract summaries and action items.
- **Composio Toolset**: Executes the transcription request and pushes data to your preferred destination.
- **Chat Output**: Returns the formatted meeting summary and task list to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Transcribe the meeting recording at [URL] and extract all action items.`
- `Summarize this transcript into a 3-bullet executive summary for the product team.`
- `Identify the key decisions made in this meeting and list the assigned owners.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine to interpret transcribed text.
- Set the system prompt to prioritize clarity and professional tone.
- Configure the model to identify specific entities like dates, names, and task deadlines.
- Enable structured output formatting (e.g., Markdown or JSON) for downstream compatibility.

### 2) Composio Toolset Node
- Provide your CastingWords API key within the Composio configuration.
- Define the scope to allow the agent to read audio files and write text summaries to your connected apps.

### 3) Tool Availability
- **Transcription Engine**: CastingWords audio-to-text processing.
- **Data Parser**: Regex and NLP-based extraction for action items.
- **Notification Service**: Optional integration to email summaries to meeting participants.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Organize and rank tasks extracted from meetings.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Automate follow-up actions based on meeting outcomes.
- [Customer Support Voice Agent](../247-customer-support-voice-agent-by-bolna/README.md) — Manage voice-based customer interactions and support tickets.
