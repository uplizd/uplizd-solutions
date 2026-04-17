# Smart Meeting Transcriber (Uplizd) - Automated audio-to-text meeting intelligence

## Summary
The Smart Meeting Transcriber by Astica AI automates the conversion of audio recordings into high-fidelity transcripts, enabling teams to capture actionable insights from every conversation. By leveraging advanced speech-to-text processing, this Uplizd workflow eliminates manual note-taking, ensures a single source of truth for meeting records, and accelerates pipeline velocity by making spoken information instantly searchable and actionable.

---

## Demo
![Smart Meeting Transcriber workflow showing audio input processing through Astica AI and Composio Toolset to generate structured meeting transcripts](image.png)
**Alt text (SEO-ready):** Smart Meeting Transcriber workflow on Uplizd, featuring Astica AI speech-to-text, automated meeting documentation, and Composio integration for team productivity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAHAAABAAAB)](https://uplizd.ai/solutions/061e3855-920d-5fd1-8a15-e8da1ae9088d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** `meeting`, `transcription`, `astica-ai`, `productivity`, `automation`, `ai-workflow`, `composio`, `documentation`

This solution streamlines meeting operations by integrating intelligent transcription directly into your existing communication and project management workflows.

---

## Who is this for?
This workflow is designed for professionals who need to turn spoken communication into structured data.

- **Project Managers**
    - Ensure all action items are captured and tracked without manual documentation.
- **Sales Representatives**
    - Review client feedback and discovery call details to improve deal qualification.
- **Executive Assistants**
    - Maintain accurate meeting minutes and summaries for leadership review.
- **Customer Success Managers**
    - Document customer pain points and feature requests directly from support calls.

---

## Features
- **Automated Transcription**
    - Converts raw audio files into clean, readable text using high-performance Astica AI models.
- **Contextual Summarization**
    - Extracts key discussion points and decisions from long-form audio automatically.
- **Composio Toolset Integration**
    - Seamlessly pushes transcripts to your preferred CRM or project management tools.
- **Real-time Processing**
    - Reduces the latency between meeting conclusion and data availability for the team.
- **Searchable Knowledge Base**
    - Transforms ephemeral audio into a permanent, searchable repository of company knowledge.

---

## Use Cases
**Meeting Documentation**
- Automatically generate meeting minutes for recurring team syncs.
- Archive transcripts in your internal wiki for future reference.

**Sales Intelligence**
- Identify key objections raised during discovery calls for sales coaching.
- Log customer sentiment and product feedback directly into your CRM.

**Action Item Tracking**
- Extract tasks and deadlines from project meetings for immediate assignment.
- Sync meeting follow-ups to your task management platform via Composio.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Meeting Transcriber template from the marketplace.
3. Connect your Astica AI and relevant CRM/Tooling credentials.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the audio file URL or raw recording data.
- **Agent**: Processes the audio, performs transcription, and summarizes the content.
- **Composio Toolset**: Executes actions to save the transcript to your integrated platforms.
- **Chat Output**: Returns the final transcript and a summary of extracted action items.

### 3) Run the Flow
Use the Playground to test your transcription pipeline:
- `Transcribe the recording at [URL] and summarize the key action items.`
- `Create a meeting summary from this audio and post it to my project board.`
- `Extract all customer feedback from the provided meeting recording.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a transcription and summarization engine.
- Use a high-context model to ensure long meetings are processed accurately.
- Instruct the agent to identify speakers and separate action items from general discussion.
- Configure the system prompt to maintain a professional, concise tone.

### 2) Composio Toolset Node
- Provide your API key to enable secure connections to your external tools.
- Set the connection scope to allow the agent to write to your documentation or CRM platforms.

### 3) Tool Availability
- **Transcription Service**: Astica AI audio-to-text engine.
- **CRM/Project Connectors**: Tools for pushing summaries to Salesforce, Jira, or Notion.
- **File Handler**: Utility for processing various audio formats (MP3, WAV, M4A).

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Manage voice-based customer support interactions.
- [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Organize and prioritize tasks extracted from meetings.
- [account-research-assistant-by-zoominfo](../account-research-assistant-by-zoominfo/README.md) - Enrich account data using insights gathered from client calls.
