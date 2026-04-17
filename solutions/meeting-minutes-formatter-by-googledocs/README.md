# Meeting Minutes Formatter (Uplizd) - Automate professional documentation from raw meeting notes

## Summary
The Meeting Minutes Formatter is an AI-powered workflow that transforms unstructured meeting transcripts and rough notes into polished, professional meeting minutes. By leveraging the Composio Toolset to interface with Google Docs, this solution ensures that critical action items, key decisions, and discussion summaries are captured accurately, saving teams hours of manual documentation time and maintaining a single source of truth for project alignment.

---

## Demo
![Meeting Minutes Formatter workflow showing raw text input being processed into a structured Google Doc](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Minutes Formatter workflow, automated Google Docs documentation, AI-driven meeting summary, and action item extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b7779d30-c156-5976-8b42-6bdd4ce429d9)

---

## Category
**Primary category:** Operations
**Secondary tags:** google docs, meeting minutes, productivity, automation, ai workflow, documentation, composio, team collaboration.
This solution streamlines administrative overhead by automating the translation of raw meeting discourse into structured, shareable business documentation.

---

## Who is this for?
This solution is designed for professionals who need to maintain clear records of team alignment and project progress without spending hours on manual drafting.

*   **Project Managers**
    *   Ensures project status and decisions are documented immediately after syncs.
*   **Executive Assistants**
    *   Reduces the time spent formatting notes, allowing focus on high-level administrative tasks.
*   **Sales Operations**
    *   Captures key client requirements and follow-up tasks directly from discovery calls.
*   **Team Leads**
    *   Maintains accountability by automatically extracting and assigning action items to team members.

---

## Features
- **Intelligent Transcription Parsing**
    Automatically identifies speaker intent and separates casual conversation from core business decisions.
- **Structured Output Generation**
    Formats raw text into professional templates including headers, bulleted action items, and summary sections.
- **Google Docs Integration**
    Uses the Composio Toolset to push finalized minutes directly into your team's shared Google Drive folders.
- **Action Item Extraction**
    Detects specific tasks, owners, and deadlines mentioned during the meeting for immediate tracking.
- **Real-time Processing**
    Processes inputs instantly, ensuring that meeting records are available for team review before the next session begins.

---

## Use Cases
**Post-Meeting Documentation**
*   Convert raw Zoom or Google Meet transcripts into formal meeting minutes.
*   Archive meeting summaries in dedicated Google Docs folders for historical reference.

**Project Management Syncs**
*   Extract action items and assign them to specific project phases within documentation.
*   Summarize key blockers and decisions to keep remote teams aligned on project velocity.

**Sales Discovery Calls**
*   Summarize client pain points and requirements from discovery call transcripts.
*   Generate follow-up emails or internal briefs based on the structured meeting output.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Minutes Formatter template from the solution library.
3. Connect your Google Docs account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw meeting transcript or rough notes.
*   **Agent**: Analyzes the text, identifies key takeaways, and structures the content.
*   **Composio Toolset**: Executes the creation of the document in Google Docs.
*   **Chat Output**: Confirms the document creation and provides a link to the new file.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Format the following transcript into meeting minutes: [Paste Transcript]`
* `Create a summary document for the project sync meeting held on October 12th.`
* `Extract all action items from these notes and add them to a new Google Doc titled 'Team Sync Minutes'.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional scribe, focusing on clarity and brevity.
*   Instruction: "You are a professional meeting secretary. Extract key decisions, action items, and summary points."
*   Instruction: "Maintain a neutral, professional tone suitable for corporate documentation."
*   Instruction: "Always identify the owner and deadline for any action items found in the text."

### 2) Composio Toolset Node
*   **API Key**: Ensure your Google Docs integration is authenticated within the Composio dashboard.
*   **Connection Scope**: Grant permissions for the agent to create and edit documents within your specified Google Drive directory.

### 3) Tool Availability
*   `google_docs_create_document`: Used to generate the new file.
*   `google_docs_append_text`: Used to insert the structured summary into the document.
*   `google_docs_share_file`: Optional tool to share the document with team members via email.

---

## Related Solutions
*   [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automate the resolution and tracking of meeting-derived tasks.
*   [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Rank and organize action items based on urgency and project impact.
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track team productivity and meeting efficiency metrics over time.
