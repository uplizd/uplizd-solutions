# Meeting Action Item Tracker (Uplizd) - Automate task extraction and follow-up from meeting transcripts

## Summary
The Meeting Action Item Tracker is an intelligent Uplizd workflow that transforms unstructured meeting transcripts into structured, actionable tasks. By leveraging the Composio Toolset to interface with Google Tasks, this solution eliminates manual data entry, ensures no follow-up item is missed, and maintains a single source of truth for project accountability across your team.

---

## Demo
![Meeting Action Item Tracker workflow showing transcript input, AI processing, and Google Tasks integration](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Action Item Tracker workflow diagram showing AI-powered transcript processing and automated task creation in Google Tasks.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d371a37b-32ee-593f-8232-ebca557b38ae)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** productivity, google tasks, meeting notes, task management, automation, ai workflow, composio, project tracking
- This solution streamlines operational efficiency by bridging the gap between verbal meeting commitments and digital task management systems.

---

## Who is this for?
This solution is designed for professionals who manage high-volume meetings and need to maintain strict accountability for action items.

- **Project Managers**
    - Ensure every project milestone discussed in meetings is captured and assigned without manual logging.
- **Executive Assistants**
    - Automate the post-meeting administrative burden of drafting and distributing task lists to stakeholders.
- **Sales Representatives**
    - Quickly convert client discovery calls into follow-up tasks to maintain momentum in the sales pipeline.
- **Team Leads**
    - Improve team transparency by syncing meeting outcomes directly into shared task boards for real-time tracking.

---

## Features
- **Intelligent Extraction**
    - Uses advanced LLM processing to identify action items, owners, and deadlines from raw meeting transcripts.
- **Google Tasks Integration**
    - Seamlessly pushes identified tasks into your Google Tasks environment via the Composio Toolset.
- **Contextual Prioritization**
    - Automatically assigns priority levels based on the urgency and context of the discussion.
- **Real-time Sync**
    - Eliminates latency between meeting conclusion and task visibility, ensuring immediate team alignment.
- **Automated Formatting**
    - Standardizes task descriptions and naming conventions for better searchability and organization.

---

## Use Cases
**Post-Meeting Productivity**
- Automatically generate a task list immediately after a Zoom or Google Meet session ends.
- Sync action items to specific Google Tasks lists based on the project or client name mentioned.

**Team Accountability**
- Assign tasks to specific team members identified in the transcript to ensure clear ownership.
- Set automated reminders for tasks that have upcoming deadlines derived from meeting dates.

**Project Lifecycle Management**
- Track the evolution of project requirements by logging new tasks as they emerge in recurring status meetings.
- Maintain a historical record of commitments made during client-facing discovery calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace and project folder.
3. Authenticate your Google Tasks account within the Composio connection settings.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw meeting transcript text.
- **Agent**: Analyzes the text to extract actionable items and metadata.
- **Composio Toolset**: Executes the API calls to create tasks in Google Tasks.
- **Chat Output**: Confirms the successful creation of tasks and displays the summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Extract action items from this transcript: [Paste Transcript Here]`
- `Create tasks for all action items found in the meeting notes: [Paste Transcript Here]`
- `Identify follow-ups for the marketing team from this meeting: [Paste Transcript Here]`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized meeting secretary.
- **Instruction Pattern:**
    - Act as a professional project assistant.
    - Extract only actionable items, ignoring general conversation.
    - Format output to match the required schema for the Google Tasks API.

### 2) Composio Toolset Node
- **API Key:** Ensure your Google Tasks API key is active in your Composio dashboard.
- **Connection Scope:** Grant read/write permissions to the specific task lists you intend to populate.

### 3) Tool Availability
- **Task Creation:** Ability to create new task entries with titles and descriptions.
- **List Management:** Ability to query and select specific Google Tasks lists.
- **Metadata Tagging:** Ability to set due dates and priority flags based on transcript context.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automate the removal of stale or completed tasks.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Rank your tasks based on project urgency and impact.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Connect meeting outcomes to broader CRM and project workflows.
