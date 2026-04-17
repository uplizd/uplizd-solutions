# Meeting Notes Processor (Uplizd) - Automate structured documentation from raw meeting transcripts

## Summary
The Meeting Notes Processor is an intelligent Uplizd workflow that transforms unstructured meeting transcripts into professional, actionable documentation. By leveraging AI to parse conversation data, it extracts key decisions, action items, and summaries, ensuring your team maintains a single source of truth and high pipeline velocity without the manual overhead of administrative note-taking.

---

## Demo
![Meeting Notes Processor dashboard showing transcript parsing into structured action items and summary](image.png)
**Alt text (SEO-ready):** Meeting Notes Processor Uplizd workflow dashboard showing automated transcript parsing, action item extraction, and Notion integration for improved team productivity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d26c813a-1b36-55ad-bce5-9cc22b97fdf6)

---

## Category
**Operations**
*Tags:* `notion`, `meeting-notes`, `automation`, `productivity`, `ai-workflow`, `composio`, `data-hygiene`
This solution streamlines administrative operations by automating the conversion of raw meeting data into organized, searchable knowledge base entries.

---

## Who is this for?
This solution is designed for professionals who need to maintain clear communication and accountability across distributed teams.

*   **Project Managers**
    *   Automatically track project milestones and ensure no task is lost after stakeholder syncs.
*   **Sales Representatives**
    *   Capture critical client requirements and follow-up tasks immediately after discovery calls.
*   **Operations Leads**
    *   Maintain consistent documentation standards across all internal and external meetings.
*   **Team Leads**
    *   Quickly distribute meeting summaries to ensure alignment on team goals and immediate next steps.

---

## Features
- **Automated Transcript Parsing**
  Processes raw audio-to-text inputs to identify speakers, topics, and key discussion points in real-time.
- **Action Item Extraction**
  Uses AI to isolate specific commitments and tasks, assigning them to the correct owners based on context.
- **Notion Integration**
  Seamlessly pushes structured summaries and task lists directly into your Notion workspace via the Composio Toolset.
- **Intelligent Summarization**
  Generates concise executive summaries that highlight decisions made and blockers identified during the meeting.
- **Workflow Hygiene**
  Standardizes meeting output formats, preventing data decay and ensuring all notes are searchable and categorized.

---

## Use Cases
**Project Documentation**
*   Syncing weekly sprint planning notes directly into project management databases.
*   Archiving historical meeting decisions for future reference and onboarding.

**Sales Pipeline Management**
*   Updating CRM or Notion deal records with key discovery call insights.
*   Automating the creation of follow-up tasks for account executives after prospect meetings.

**Team Alignment**
*   Distributing post-meeting summaries to stakeholders who were unable to attend.
*   Tracking cross-departmental action items to ensure organizational accountability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Notion account via the Composio Toolset node.
3. Configure your preferred LLM in the Agent node settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw meeting transcript text.
*   **Agent**: Analyzes the text to extract action items, decisions, and summaries.
*   **Composio Toolset**: Connects to Notion to create or update pages.
*   **Chat Output**: Confirms the successful creation of the meeting note document.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
*   `"Process this transcript: [Paste Transcript Here] and create a new meeting note in Notion."`
*   `"Summarize the following meeting and extract all action items assigned to John: [Paste Transcript Here]."`
*   `"Create a project update note in Notion based on these discussion points: [Paste Points Here]."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary intelligence layer for parsing and structuring data.
*   Use a high-reasoning model (e.g., GPT-4o or Claude 3.5) for accurate task extraction.
*   Instruction pattern: Define the output schema (Title, Summary, Action Items, Attendees).
*   Instruction pattern: Enforce a professional, objective tone for all generated summaries.

### 2) Composio Toolset Node
*   Requires a valid Notion API key and authorized workspace access.
*   Ensure the connection scope includes "Read/Write" permissions for the target database.

### 3) Tool Availability
*   `notion_create_page`: For generating new meeting documentation.
*   `notion_update_database_item`: For appending action items to existing project trackers.
*   `notion_search`: To locate relevant project pages before updating.

---

## Related Solutions
*   [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from meeting notes.
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automate broader business processes beyond meeting notes.
*   [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Maintain deep client context alongside meeting documentation.
