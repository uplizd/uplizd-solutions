# Meeting Transcription Processor (Uplizd) - Automated meeting intelligence and action item extraction

## Summary
The Meeting Transcription Processor by Uplizd leverages advanced AI to transform raw meeting audio and video recordings into structured, actionable intelligence. By integrating with Rev.ai and your existing project management stack, this workflow automatically generates high-fidelity transcripts, summarizes key discussion points, and extracts follow-up tasks, ensuring your team maintains perfect alignment without the manual overhead of note-taking.

---

## Demo
![Meeting Transcription Processor workflow showing audio input, Rev.ai transcription, and action item extraction](image.png)
**Alt text (SEO-ready):** Meeting Transcription Processor by Uplizd, AI-powered meeting notes, Rev.ai transcription workflow, automated action item extraction, and team productivity integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/53443e9f-42f3-5547-a4b6-f039dec0292a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meeting intelligence, transcription, rev.ai, productivity, action items, workflow automation, composio, ai assistant
- This solution streamlines post-meeting workflows by converting unstructured audio data into organized, searchable business intelligence.

---

## Who is this for?
This solution is designed for professionals who need to capture meeting outcomes efficiently and ensure accountability across distributed teams.

- **Project Managers**
    - Automatically sync meeting action items to project boards to track progress and deadlines.
- **Sales Representatives**
    - Capture prospect requirements and pain points directly from discovery calls for better CRM data hygiene.
- **Executive Assistants**
    - Generate concise executive summaries from long-form recordings to save hours of manual documentation.
- **Engineering Leads**
    - Document technical decisions and sprint planning outcomes without interrupting the flow of conversation.

---

## Features
- **Automated Transcription**
    - High-accuracy speech-to-text processing powered by Rev.ai for clear, readable meeting records.
- **Action Item Extraction**
    - Intelligent parsing of conversation threads to identify and assign follow-up tasks automatically.
- **Contextual Summarization**
    - AI-driven synthesis of meeting objectives, key decisions, and open questions into a structured format.
- **Seamless Integrations**
    - Direct connectivity to project management and CRM tools via the Composio Toolset for immediate data routing.
- **Real-time Processing**
    - Rapid turnaround from audio upload to finalized documentation, enabling immediate team follow-up.

---

## Use Cases
**Meeting Documentation**
- Transcribing internal strategy sessions to ensure all stakeholders have a single source of truth.
- Converting client discovery calls into structured meeting minutes for account records.

**Task Management**
- Automatically creating tickets in project management tools based on identified action items.
- Updating CRM opportunity notes with key takeaways from sales meetings.

**Knowledge Management**
- Building a searchable repository of historical meeting insights for onboarding and reference.
- Tracking the evolution of project requirements over a series of recurring status calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Rev.ai API credentials to the transcription node.
3. Configure your target project management or CRM tool within the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the audio file URL or raw recording file for processing.
- **Agent**: Analyzes the transcript to identify key themes, decisions, and action items.
- **Composio Toolset**: Executes the creation of tasks or notes in your connected third-party applications.
- **Chat Output**: Returns the final summary and confirmation of created tasks to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Process this meeting recording and list all action items assigned to the team.`
- `Summarize the key decisions made during this call and update the CRM with the notes.`
- `Extract the technical requirements discussed in the meeting and create a new project task.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized meeting analyst.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for best results.
- **Recommended instruction pattern:**
    - "Act as a professional meeting scribe and project coordinator."
    - "Prioritize accuracy in identifying task owners and specific deadlines."
    - "Maintain a professional, concise tone in all generated summaries."

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure access to your integrated platforms.
- Set the connection scope to allow the agent to read/write to your specific project management or CRM workspace.

### 3) Tool Availability
- **Transcription Tools**: Rev.ai integration for audio processing.
- **Project Management Tools**: Jira, Asana, or Trello connectors for task creation.
- **CRM Connectors**: Salesforce or HubSpot integration for updating account records.

---

## Related Solutions
- [Action Item Prioritizer (Rootly)](../action-item-prioritizer-by-rootly/README.md) — Organize and rank tasks extracted from various communication channels.
- [Account Research Assistant (ZoomInfo)](../account-research-agent-by-onepage/README.md) — Gather deep account intelligence to prepare for high-stakes meetings.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent data across your platforms after meeting updates are processed.
