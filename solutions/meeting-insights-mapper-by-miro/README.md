# Meeting Insights Mapper (Uplizd) - Transform meeting transcripts into visual strategy boards

## Summary
The Meeting Insights Mapper is an intelligent Uplizd workflow that automates the extraction of key takeaways, action items, and strategic themes from raw meeting transcripts. By leveraging AI to parse unstructured conversation data and mapping it directly to visual collaboration tools like Miro, this solution eliminates manual documentation, ensures team alignment, and accelerates project velocity by turning talk into actionable visual assets.

---

## Demo
![Meeting Insights Mapper workflow showing transcript processing into visual mind maps and action boards](image.png)

**Alt text (SEO-ready):** Meeting Insights Mapper Uplizd workflow for automated transcript analysis, Miro board generation, and action item tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4d7aec85-5555-56c3-87ba-6dee9430c8eb)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** miro, meeting insights, transcript analysis, project management, workflow automation, ai agent, composio, collaboration
- This solution bridges the gap between verbal communication and visual project management by automating the synthesis of meeting data into actionable board templates.

---

## Who is this for?
This solution is designed for teams that need to turn high-volume meeting data into structured visual workflows.

- **Project Managers**
    - Automatically convert meeting outcomes into organized task boards and project roadmaps.
- **Product Designers**
    - Rapidly translate user feedback sessions into visual mind maps for feature ideation.
- **Sales Leads**
    - Map client requirements and pain points directly to account strategy boards.
- **Operations Managers**
    - Standardize the documentation of meeting decisions to ensure cross-departmental alignment.

---

## Features
- **Automated Transcript Parsing**
    - Uses advanced LLMs to identify speakers, key decisions, and follow-up tasks from raw audio-to-text inputs.
- **Miro Board Integration**
    - Seamlessly connects with the Composio Toolset to create, update, and organize visual cards on Miro boards.
- **Action Item Extraction**
    - Automatically detects and assigns action items with owners and deadlines based on meeting context.
- **Strategic Theme Mapping**
    - Clusters related ideas into visual themes, helping teams visualize the "big picture" of long-form discussions.
- **Real-time Sync**
    - Ensures that as soon as a transcript is processed, the corresponding visual board is updated, keeping remote teams in sync.

---

## Use Cases
**Meeting Documentation**
- Converting hour-long brainstorming sessions into concise, visual mind maps.
- Archiving meeting decisions in a searchable, visual format for future reference.

**Project Planning**
- Translating project kickoff meeting notes into structured Kanban boards.
- Updating project status boards immediately following weekly syncs.

**Client Strategy**
- Mapping client feedback from discovery calls directly into account strategy canvases.
- Visualizing competitive intelligence gathered during stakeholder interviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `meeting-insights-mapper` configuration file.
3. Connect your preferred LLM and Miro credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw meeting transcript text.
- **Agent**: Analyzes the text to extract insights, action items, and themes.
- **Composio Toolset**: Executes commands to create or update Miro boards.
- **Chat Output**: Confirms the successful mapping and provides a link to the updated board.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Map the following transcript into a Miro mind map: [Paste Transcript]`
- `Extract action items from this meeting and create a task list on my 'Project Alpha' board.`
- `Summarize the key strategic themes from this transcript and organize them as sticky notes on a new board.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized meeting analyst.
- **Instruction Pattern:**
    - "Act as an expert project coordinator who excels at synthesizing unstructured conversation."
    - "Identify all explicit action items, assignees, and deadlines mentioned in the transcript."
    - "Structure the output into logical categories suitable for visual representation on a Miro board."

### 2) Composio Toolset Node
- **API Key:** Ensure your Miro API key is active within the Composio dashboard.
- **Connection Scope:** Grant read/write access to your specific Miro team workspace.

### 3) Tool Availability
- **Miro Board Creation**: Capability to initialize new boards from templates.
- **Widget/Sticky Note Management**: Ability to add, move, and color-code items.
- **Text Extraction**: Advanced parsing for identifying key entities and action verbs.

---

## Related Solutions
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automates the facilitation of interactive workshop sessions.
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manages and deploys standardized workshop templates for team collaboration.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Ranks and manages follow-up tasks based on urgency and impact.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the execution and efficiency of team collaboration workflows.
